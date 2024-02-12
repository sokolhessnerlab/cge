# Pre-processing (data cleaning) for Kimberly Chiew
# December, 9, 2022
# 
# Purpose:  Deblink, smooth, baseline

### Original file name - "pre-processing by trial type - actual size" ###

# Link to McLaughlin's Eye-tracking scripts https://sites.google.com/view/drewjmclaughlin/pupillometry




rm(list=ls())
# Load packages
library(devtools)
library(gazer)
library(tidyverse)
library(zoo)
library(knitr)
library(ggplot2)
library(plyr)
library(here)

# Set working directory (change to reflect working directory of analysis computer)
file.dir <- here()
save.dir <- here()
setwd(file.dir)


#### LOAD AND PREP DATA ####

# Load compiled files (I envision this being the "raw" files from my pipeline plus intelligibility)
pupil_files <- read.csv("17_bas.csv", header = TRUE)
summary(pupil_files)

# Add column for "time" - count of the data points per trial
pupil_files$time <- NA
for (i in 1:length(pupil_files$trial)) {
  if (is.na(pupil_files$trial[i])) {
    pupil_files$time[i] <- 0
  }
  else if (i == 1) {
    pupil_files$time[i] <- 1
  } else if (pupil_files$trial[i] != pupil_files$trial[i-1]) {
    pupil_files$time[i] <- 1
  } else {
    pupil_files$time[i] <- pupil_files$time[i-1] + 1
  }
}
write.csv(pupil_files, "17_bas_timecount.csv", row.names = FALSE)

# convert pupil size to millimeters
pupil_files$actual_size <- sqrt(pupil_files$pupil)*(8/sqrt(2355.85))

# Unlist for GazeR
pupil_files <- as.data.frame(lapply(pupil_files, unlist))

# Get rid of participants and trials with too much data loss
pupil_files <- count_missing_pupil(pupil_files, missingthresh = .2)
# % trials excluded:0.762; Participants taken out:998



#### DEBLINKING & SMOOTHING ####

# Extend blink windows (if not done with DataViewer)
pup_extend <- pupil_files %>% 
  group_by(subject, trial) %>% 
  mutate(extendpupil = extend_blinks(actual_size, fillback = 200, fillforward = 100, hz = 500))

# Interpolation (set extendblinks to TRUE if using function above)
pup_interp <- interpolate_pupil(pup_extend, extendblinks = TRUE, type = "linear")

# Smoothing (5-point moving average)
rolling_mean_pupil_average <- as.data.frame(pup_interp) %>%                 # must be in a data.frame!
  select(subject, trial, time, condition, interp) %>%       
  mutate(movingavgpup = moving_average_pupil(interp, n = 5))


##### GET BASELINE VALUES #####

baseline_values <- rolling_mean_pupil_average %>%
  dplyr::filter(time > 1 & time < 500) %>%
  dplyr::group_by(subject, trial) %>%
  dplyr::summarise(baseline = mean(interp))


#### BASELINE CORRECTION ####

baseline_pupil_cond <- baseline_correction_pupil(rolling_mean_pupil_average, 
                                            pupil_colname = "movingavgpup", 
                                            baseline_window = c(1, 500), 
                                            baseline_method = "sub")
# Limit to AOI (-500 on for now)
baseline_pupil_cond <- subset(baseline_pupil_cond, subset = time >= -500)

write.csv(baseline_pupil_cond, "3_bas_processed.csv", row.names = FALSE)

#### TIMEBINNING ####

# I've chosen to downsample to 50Hz (20ms bins) 
bin.length <- 20 # length of bin in ms
data.binned <- baseline_pupil_cond %>%
  mutate(timebins = round(time/bin.length)*bin.length)
data.binned <- data.binned %>%
  dplyr::group_by(subject, trial, condition, timebins) %>% 
  dplyr::summarise(pupil.binned = mean(baselinecorrectedp)) %>%
  ungroup()

# Subset from 500 ms (start of baseline)
data.binned <- subset(data.binned, subset = timebins >= -500)

write.csv(data.binned, "3_bas_binned.csv", row.names = FALSE)

##### GET PEAK AND MEAN VALUES #####

# Limit timecourse data to AOI (300 ms to 3500 ms)
peakmean_AOI <- subset(data.binned, timebins >= 300 & timebins <= 3500)

# Summarize
peakmean_df <- data.binned %>%
  dplyr::group_by(subject, trial, condition) %>%
  dplyr::summarise(PPD = max(pupil.binned), MPD = mean(pupil.binned))

#visualizing time course
plot1 <- ggplot(data= data.binned, aes(x=timebins, y=pupil.binned)) + geom_smooth()
plot1
plot2 <- ggplot(data= data.binned, aes(x=timebins, y=pupil.binned)) + geom_smooth() + facet_wrap(~condition)
plot2
#ggsave("condition_time_course.png", plot2)

