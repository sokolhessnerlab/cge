# CGE Eyetracking Data Processing Script
#
# Script to process the eyetracking data collected from the CGE (Control & Gambling 
# Task with Eyetracking) study.

# Major To-Do's:
# - convert pupil data to millimeters (req. calibration procedure)
# - Establish cutoffs for...
#   - what counts as a 'blink' (to extend)
#   - what counts as 'a gap that's too long to interpolate over'
#   - what are acceptable limits in terms of...
#       - missing samples
#       - blinks
#       - calibration quality
#       - or other metric (% eyegaze off-screen?)
# - Align timestamps from python output w/ eyelink timestamps
#   - start timestamp
#   - then trial timestamps


# UNCOMMENT THIS BLOCK WHEN DONE

# # STEP 1: SET YOUR WORKING DIRECTORY!
# # On PSH's computers...
# setwd('/Users/sokolhessner/Documents/gitrepos/cge/');
# # On Von's PC Laptop "tabletas"...
# setwd('C:/Users/jvonm/Documents/GitHub/cge');
# 
# 
# # STEP 2: then run from here on the same
# config = config::get();
# 
# setwd(config$path$data$raw);
setwd('~/Desktop/tmp_et_CGE/')

# STEP 3: Get the file names
cat('Identifying file locations.\n');
etfn = dir(pattern = glob2rx('cge*.asc'),full.names = T, recursive = T);


# STEP 4: SET UP FOR SUBJECT LOOP
library('eyelinker') # for eyelink-specific file interaction
library('zoo') # for interpolation
# library('gazer') # Requires R 4.2 or higher; may need to upgrade?

number_of_subjects = length(etfn);

# for (s in 1:number_of_subjects){
# 
# }

s = 1; 

cat(sprintf('Reading eye-tracking data for %i.\n',s))
raw_et_data = read.asc(etfn[s], samples = T, events = F)
cat(sprintf('Eye-tracking data loaded.\n',s))

# Settings:
# 1000 Hz sample rate
# 1280 (w) x 1024 (h) screen size)
# Diameter pupil data type (not area)
original_sample_rate = raw_et_data$info$sample.rate

# How to visualize the data
# NOTE: these are slow to execute because the dataset is so large (~1.2 million datapoints/person)
# Gaze location (coordinates (0,0) are TOP LEFT)
plot(raw_et_data$raw$xp, -raw_et_data$raw$yp, pch = 16, cex = .5, col = rgb(1,0,0,.1), 
     xlim = c(-200, raw_et_data$info$screen.x + 200), ylim = c(200, -raw_et_data$info$screen.y-200))
lines(x = c(0, raw_et_data$info$screen.x, raw_et_data$info$screen.x, 0, 0), 
      y = c(0, 0, -raw_et_data$info$screen.y, -raw_et_data$info$screen.y, 0))
plot(raw_et_data$raw$ps, type = 'l') # the pupil dilation data

# Code to construct a low-res 'heatmap' that displays more easily than the full data. 
# xres = 50;
# yres = 51;
# heatmap_density = array(data = NA, dim = c(xres, yres));
# xd = raw_et_data$info$screen.x;
# yd = raw_et_data$info$screen.y;
# for (x in 1:xres){
#   print(x)
#   for (y in 1:yres){
#     heatmap_density[x,y] = sum((raw_et_data$raw$xp >= (xd/xres*(x-1))) & (raw_et_data$raw$xp < (xd/xres*x)) & 
#                                (raw_et_data$raw$yp >= (yd/yres*(y-1))) & (raw_et_data$raw$yp < (yd/yres*y)),
#                                na.rm = T);
#   }
# }
# image(z = log(heatmap_density))


##### Processing #####

pupil_data_raw = raw_et_data$raw$ps;
time_data = raw_et_data$raw$time; # UNCORRECTED! in milliseconds

# 1. Extend blink points
missing_points_ind = which(is.na(pupil_data_raw)); # index of all missing datapoints
blink_init_sample = missing_points_ind[c(1,which(diff(missing_points_ind) > 1) + 1)] # first sample of missing data epochs
blink_final_sample = missing_points_ind[c(which(diff(missing_points_ind) > 1), length(missing_points_ind))] # final sample
blink_length = time_data[blink_final_sample] - time_data[blink_init_sample]; # length in ms

blink_data = as.data.frame(cbind(blink_init_sample, blink_final_sample, blink_length))
hist(blink_data$blink_length, xlab = 'milliseconds', main = 'Blink Lengths', breaks = 200) # opt: visualize blink lengths

# Summarize Missing Data
number_of_missing_samples = length(missing_points_ind);
percent_of_missing_samples = number_of_missing_samples/length(pupil_data_raw);
number_of_blinks = length(blink_init_sample);

cat(sprintf('Participant %i: Missing %i samples (%.1f%%), with %i blinks.\n', 
            s, number_of_missing_samples, percent_of_missing_samples*100, number_of_blinks))

blink_length_threshold = 20; # milliseconds (ms) what counts as a 'blink'? There are plenty of super-short missing samples.
na_fill = 100; # how many milliseconds to expand the blinks
pupil_data_extend = pupil_data_raw;

for (b in 1:number_of_blinks){
  if (blink_data$blink_length[b] > blink_length_threshold){
    pupil_data_extend[(which(time_data > (time_data[blink_init_sample[b]] - na_fill))[1]):
                        ((which(time_data > (time_data[blink_final_sample[b]] + na_fill))[1])-1)] = NA;
  }
}
cat('Blinks extended.\n')

# 2. Interpolate

# Interpolate linearly across NA gaps
cat('Interpolating...')
pupil_data_extend_interp = na.approx(pupil_data_extend);
cat('NA gaps linearly interpolated.\n')
# technically, this approach linearly interpolates across datapoints, not timepoints
# i.e. if one or more timepoints are simply missing (not that they would be NAs, but 
# that they would not be *present*), this would inaccurately interpolate. This is 
# probably fine, though - missing samples are not expected, and the harm done would
# be pretty minor.

# 3. Replace excessively long missing sections with NAs
maximum_allowable_missing = 1000; # ms; what should this value be? 

for (b in 1:number_of_blinks){
  if (blink_data$blink_length[b] >= maximum_allowable_missing) {
    pupil_data_extend_interp[blink_data$blink_init_sample[b]:blink_final_sample[b]] = NA;
  }
}

# 4. Smooth (10-point moving window)
cat('Smoothing... ')
smoothing_window_width = 10; # points to smooth over; 10 pts @ 1000Hz = 10ms
pupil_data_extend_interp_smooth = rollapply(pupil_data_extend_interp, 
                                            width = smoothing_window_width, FUN = 'mean', partial = T,
                                            align = 'center', na.rm = T)
cat('Pupillometry smoothed.\n')

# 4. Convert pupil diameter data to mm
pupil_data_extend_interp_smooth_mm = pupil_data_extend_interp_smooth; # MUST DO THIS!
# SEE THIS LINK: https://researchwiki.solo.universiteitleiden.nl/xwiki/wiki/researchwiki.solo.universiteitleiden.nl/view/Hardware/EyeLink/#:~:text=EyeLink%20reports%20pupil%20size%20as,circle%20with%20a%20known%20diameter.


