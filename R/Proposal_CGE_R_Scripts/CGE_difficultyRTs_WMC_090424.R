###########################
# VON and KIM working on CGE-MA thesis
# September 4 2024
# Focusing on calculating and analysing RTs for choice difficulty
# As described in MA proposal: "RT difference between easy and difficult
# decisions (easy decision RTs - difficult decision RTs) in high and low WMC
###########################


# BE CAREFUL -- THIS CLEANS OUT EVERYTHING IN R'S MEMORY
rm(list=ls())

library(dplyr)
library(lme4)
library(lmerTest)
library(nlme)
library(tidyverse)

### All Required Hierarchical Linear Regressions ### 

## Setting Up

clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\CGE_R_Scripts\\clean_data_dm_090424.csv")

clean_data_dm_vonkim$diff_cont = abs(abs(clean_data_dm_vonkim$choiceP - 0.5)*2-1); # JUST for the easy/difficult dynamic trials
clean_data_dm_vonkim$prev_diff_cont = c(NA,clean_data_dm_vonkim$diff_cont[1:(length(clean_data_dm_vonkim$diff_cont)-1)]) # for dynamic trials
clean_data_dm_vonkim$prev_diff_cont[clean_data_dm_vonkim$trialnumber == 1] = NA;

clean_data_dm_vonkim$meanRT = mean(clean_data_dm_vonkim$reactiontime, na.rm = T)
clean_data_dm_vonkim$sdRT = sd(clean_data_dm_vonkim$reactiontime, na.rm = T)

clean_data_dm_vonkim$sqrtRTmean = mean(clean_data_dm_vonkim$sqrtRT, na.rm = T)
clean_data_dm_vonkim$sqrtRTsd = sd(clean_data_dm_vonkim$sqrtRT, na.rm = T)

thesisDF <- clean_data_dm_vonkim %>%
  select(subjectnumber,
         trialnumber,
         static0dynamic1,
         easyP1difficultN1,
         easyP1difficultN1_prev,
         diff_cont,
         prev_diff_cont,
         all_diff_cont,
         prev_all_diff_cont,
         capacity_HighP1_lowN1_best,
         NCS_HighP1_LowN1,
         reactiontime,
         sqrtRT,
         meanRT,
         sdRT,
         sqrtRTmean,
         sqrtRTsd
  )

thesisDF <- thesisDF %>%
  rename(
    subID = subjectnumber,
    trial = trialnumber,
    WMC_highP1lowN1 = capacity_HighP1_lowN1_best,
    NCS_highP1lowN1 = NCS_HighP1_LowN1,
    RT = reactiontime
  )

data_difficulty_subj <- clean_data_dm_vonkim %>% # handles NAs for meanRTs so the cleaning step is uneccessary
  group_by(subjectnumber, curr_diff) %>%
  summarize(
    n = n(),
    prev_diff = first(easyP1difficultN1_prev),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

# data_thesisDF <- thesisDF %>%  ### Kept giving wonky numbers for previous difficulty
#   group_by(subID, easyP1difficultN1) %>%
#   summarize(
#     n = n(),
#     easyP1difficultN1_prev = mean(easyP1difficultN1_prev, na.rm = T),
#     WMC_highP1lowN1 = mean(WMC_highP1lowN1, na.rm = T),
#     NCS_highP1lowN1 = mean(NCS_highP1lowN1, na.rm = T),
#     meanRT = mean(meanRT, na.rm = T),
#     sdRT = mean(sdRT, na.rm = T)
#   )

clean_data_dm_vonkim$subID = clean_data_dm_vonkim$subjectnumber

clean_data_dm_vonkim$easyP1difficultN1 <- factor(clean_data_dm_vonkim$easyP1difficultN1,
                                         levels = c(-1:1),
                                         labels = c("difficult", "static", "easy"))

data_thesisDF <- clean_data_dm_vonkim %>% 
  group_by(subID, easyP1difficultN1) %>%
  summarise(
    n = n(),
    easyP1difficultN1_prev = first(easyP1difficultN1_prev),
    WMC_highP1lowN1 = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NCS_highP1lowN1 = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(clean_data_dm_vonkim$reactiontime, na.rm = T),
    sdRT = sd(clean_data_dm_vonkim$reactiontime, na.rm = T)
  )

## POINT 1: meanRTs

# Current Difficulty
m1_curr_meanRT <- lmer(meanRT ~ 1 + 
                         easyP1difficultN1 + 
                         (1 | subID), data = data_thesisDF)
summary(m1_curr_meanRT) 



# Previous Difficulty
m1_prev_meanRT <- lmer(meanRT ~ 1 +  
                         prev_diff_cont + 
                         (1 | subID), data = thesisDF)
summary(m1_prev_meanRT) 



# WMC
m1_wmc_meanRT <- lmer(meanRT ~ 1 +
                        WMC_highP1lowN1 +  
                        (1 | subID), data = thesisDF)
summary(m1_wmc_meanRT) 



# NFC
m1_nfc_meanRT <- lmer(meanRT ~ 1 + 
                        NCS_highP1lowN1 + 
                        (1 | subID), data = thesisDF)
summary(m1_nfc_meanRT) 



# Current, Previous, WMC, & NFC
m1_all_meanRT <- lmer(meanRT ~ 1 + 
                        diff_cont + 
                        prev_diff_cont + 
                        WMC_highP1lowN1 + 
                        NCS_highP1lowN1 + 
                        (1 | subID), data = thesisDF)
summary(m1_all_meanRT) 



# Compare m1 models
AIC(m1_curr_meanRT) # 13.04949 - the better model???
AIC(m1_prev_meanRT) # 90.37742
AIC(m1_wmc_meanRT) # 89.44398
AIC(m1_nfc_meanRT) # 85.45728
AIC(m1_all_meanRT) # 21.49844 

## POINT 2: trialRTs

# Current Difficulty
m2_curr_trialRT <- lmer(sqrtRT ~ 1 + 
                          diff_cont + 
                          (1 | subID), data = thesisDF)
summary(m2_curr_trialRT) 



# Previous Difficulty
m2_prev_trialRT <- lmer(sqrtRT ~ 1 + 
                          prev_diff_cont + 
                          (1 | subID), data = thesisDF)
summary(m2_prev_trialRT) 



# WMC
m2_wmc_trialRT <- lmer(sqrtRT ~ 1 + 
                         WMC_highP1lowN1 +
                         (1 | subID), data = thesisDF)
summary(m2_wmc_trialRT) 



# Current, Previous, WMC, & NCS
m2_nfc_trialRT <- lmer(sqrtRT ~ 1 +
                         NCS_highP1lowN1 +
                         (1 | subID), data = thesisDF)
summary(m2_all_trialRT)



# Current, Previous, WMC, & NCS
m2_all_trialRT <- lmer(sqrtRT ~ 1 + 
                         diff_cont + 
                         prev_diff_cont + 
                         WMC_highP1lowN1 +
                         NCS_highP1lowN1 +
                         (1 | subID), data = thesisDF)
summary(m2_all_trialRT) 



# Current Difficulty
m4_curr_sdRT <- lmer(sdRT ~ 1 + 
                       diff_cont + 
                       (1 | subID), data = thesisDF)
summary(m4_curr_sdRT) 



# Previous Difficulty
m4_prev_sdRT <- lmer(sdRT ~ 1 +  
                       prev_diff_cont + 
                       (1 | subID), data = thesisDF)
summary(m4_prev_sdRT) 



# WMC
m4_wmc_sdRT <- lmer(sdRT ~ 1 +
                      WMC_highP1lowN1 +  
                      (1 | subID), data = thesisDF)
summary(m4_wmc_sdRT) 



# NFC
m4_nfc_sdRT <- lmer(sdRT ~ 1 + 
                      NCS_highP1lowN1 + 
                      (1 | subID), data = thesisDF)
summary(m4_nfc_sdRT) 



# Current, Previous, WMC, & NFC
m4_all_sdRT <- lmer(sdRT ~ 1 + 
                      diff_cont + 
                      prev_diff_cont + 
                      WMC_highP1lowN1 + 
                      NCS_highP1lowN1 + 
                      (1 | subID), data = thesisDF)
summary(m4_all_sdRT) 




# Compare m1 models
AIC(m4_curr_sdRT) # -345.8712 - the better model???
AIC(m4_prev_sdRT) # -331.2931
AIC(m4_wmc_sdRT) # -318.9577
AIC(m4_nfc_sdRT) # -324.1173
AIC(m4_all_sdRT) # -312.3865


























############################ 
# Older versions below

data_thesisDF <- thesisDF %>% 
  group_by(subID, easyP1difficultN1) %>%
  reframe(
    n = n(),
    diff_cont = diff_cont,
    easyP1difficultN1_prev = easyP1difficultN1_prev,
    WMC_highP1lowN1 = WMC_highP1lowN1,
    NCS_highP1lowN1 = NCS_highP1lowN1,
    meanRT = meanRT,
    sdRT = sdRT
  )





###########################
# LOAD DATA
###########################

clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\CGE_R_Scripts\\clean_data_dm_090424.csv")

###########################
# FACTOR NON-NUMERIC VARIABLES
###########################

clean_data_dm_vonkim$subjectnumber <- factor(clean_data_dm_vonkim$subjectnumber)

clean_data_dm_vonkim$easyP1difficultN1 <- factor(clean_data_dm_vonkim$easyP1difficultN1,
                                                 levels = c(-1:1),
                                                 labels = c("difficult", "static", "easy"))
                                                 
###########################
# CALCULATE MEAN RTS FOR EASY AND DIFFICULT TRIALS PER PERSON
###########################

data_easyhardRTs_subj <- clean_data_dm_vonkim %>% group_by(subjectnumber, easyP1difficultN1) %>%
  summarize(
    n=n(),
    meanRT = mean(reactiontime),
    WMCgroup = mean(capacity_HighP1_lowN1_best)
  )

### Is there a way to get means through group by when there are missing values # in the main script does it handle NAs well???
# data_easyhardRTs_subj <- clean_data_dm_vonkim %>%
#   filter(!is.na(easyP1difficultN1)) %>%
#   group_by(subjectnumber, easyP1difficultN1) %>%
#   summarize(
#     n = n(),
#     meanRT = mean(reactiontime, na.rm = TRUE),
#     WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = TRUE)
#   )

# data_easyhardRTs_subj <- clean_data_dm_vonkim %>%
#   drop_na(easyP1difficultN1) %>%
#   group_by(subjectnumber, easyP1difficultN1) %>%
#   summarize(
#     n = n(),
#     meanRT = mean(reactiontime, na.rm = TRUE),
#     WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = TRUE)
#   )


# this worked successfully, but a lot of trial categories had "NA" for the mean reaction time. 
# need to go back to the clean_data_dm_vonkim dataset and figure out where individual trials do not have a valid RT because of RTs are missing, the group_by function
# will not be able to calculate the mean succesfully. 
# you can filter out the trials where RT is empty or not a valid number, THEN run the group_by on the filtered dataframe. 


# removing trials with a blank in the column "reactiontime" from clean_data_dm_vonkim
clean_data_dm_vonkim_RTs <- clean_data_dm_vonkim[!(clean_data_dm_vonkim$reactiontime == "" | is.na(clean_data_dm_vonkim$reactiontime)), ]


# now trying group_by again but on the dataframe where empty RTs are removed! 

data_easyhardRTs_subj <- clean_data_dm_vonkim_RTs %>% group_by(subjectnumber, easyP1difficultN1) %>%
  summarize(
    n=n(),
    meanRT = mean(reactiontime),
    WMCgroup = mean(capacity_HighP1_lowN1_best))


###########################
# CALCULATE DIFFERENCE SCORES BETWEEN DIFFICULT - EASY RTS PER PERSON
###########################

# reshape data_easyhardRTs_subj from long to wide 
data_easyhardRTs_subj_wide <- reshape(data_easyhardRTs_subj, idvar = "subjectnumber", timevar = "easyP1difficultN1", direction = "wide")

# this did not work correctly

# long to wide
data_easyhardRTs_subj_wide <- reshape(data_easyhardRTs_subj, 
                                      idvar = c("subjectnumber", "WMCgroup"), 
                                      timevar = "easyP1difficultN1", 
                                      v.names = c("n", "meanRT"), 
                                      direction = "wide")

# did  not work because it has NAs in WMCgroup???
data_easyhardRTs_subj$subjectnumber[is.na(data_easyhardRTs_subj$WMCgroup)] # 29, 58, 59

clean_data_easyhardRTs_subj <- data_easyhardRTs_subj[!(data_easyhardRTs_subj$WMCgroup == "" | is.na(data_easyhardRTs_subj$WMCgroup)), ]

data_easyhardRTs_subj_wide <- reshape(clean_data_easyhardRTs_subj, 
                                      idvar = c("subjectnumber", "WMCgroup"), 
                                      timevar = "easyP1difficultN1", 
                                      v.names = c("n", "meanRT"), 
                                      direction = "wide")

# still not working

# what if i remove some columns e.g., "n"
removedN <- clean_data_easyhardRTs_subj[, !names(clean_data_easyhardRTs_subj) %in% "n"]

data_removedN_wide <- reshape(removedN, 
                                      idvar = c("subjectnumber", "WMCgroup"), 
                                      timevar = "easyP1difficultN1", 
                                      v.names = "meanRT", 
                                      direction = "wide")

removedN <- clean_data_easyhardRTs_subj[, !names(clean_data_easyhardRTs_subj) %in% c("n", "WMCgroup")]

data_removedN_wide <- reshape(removedN, 
                              idvar = "subjectnumber", 
                              v.names = c("meanRT"),
                              timevar = "easyP1difficultN1",
                              direction = "wide")

# not working - all the non-working code consistently doesn't separate the choice difficulty into separate columns
# it would collapse them into a single column with a range, i.e., 1:3 for choice difficulty levels


# let's try using tidyverse method pivot_wider() ### it works!!! TT_TT
data_easyhardRTs_subj_wide <- data_easyhardRTs_subj %>%
  pivot_wider(
    names_from = easyP1difficultN1,
    values_from = c(meanRT, n) 
  )

# this created negative values - it should be positive if difficult was bigger # there may have been an issue with labeling earlier code
data_easyhardRTs_subj_wide$meanRTdifference <- data_easyhardRTs_subj_wide$meanRT_difficult - data_easyhardRTs_subj_wide$meanRT_easy

t.test(data_easyhardRTs_subj_wide$meanRTdifference[data_easyhardRTs_subj_wide$WMCgroup == 1], data_easyhardRTs_subj_wide$meanRTdifference[data_easyhardRTs_subj_wide$WMCgroup == -1], na.rm = T)

mean(data_easyhardRTs_subj_wide$meanRTdifference[data_easyhardRTs_subj_wide$WMCgroup == 1], na.rm = T) # -0.3132085
mean(data_easyhardRTs_subj_wide$meanRTdifference[data_easyhardRTs_subj_wide$WMCgroup == -1], na.rm = T) # -0.2012207

### Next Steps 
# SD_RT ~ Difficulty (within) + WMC + NFC (these are between) 
# DF - SDs for each person in RTS of choice difficulty 
# use group_by --- can be in long or wide --- wide would b useful in repeating what I've done
# send an email of the steps of the things I need to do
# do the regression for this model


data_easyhardRTs_subj <- clean_data_dm_vonkim %>% # handles NAs for meanRTs so the cleaning step is uneccessary
  group_by(subjectnumber, easyP1difficultN1) %>%
  summarize(
    n = n(),
    meanRT = mean(reactiontime),
    sdRT = sd(reactiontime, na.rm = T),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    prev_diff = mean(prev_all_diff_cont, na.rm = T)
  )

data_easyhardRTs_subj_wide <- data_easyhardRTs_subj %>% # probably don't need to make it wide
  pivot_wider(
    names_from = easyP1difficultN1,
    values_from = c(meanRT, sdRT, n) 
  )

data_easyhardRTs_subj <- data_easyhardRTs_subj[!(data_easyhardRTs_subj$meanRT == "" | is.na(data_easyhardRTs_subj$meanRT)), ]
data_easyhardRTs_subj <- data_easyhardRTs_subj[!(data_easyhardRTs_subj$WMCgroup == "" | is.na(data_easyhardRTs_subj$WMCgroup)), ]

data_easyhardRTs_subj <- data_easyhardRTs_subj[data_easyhardRTs_subj$easyP1difficultN1 != "static", ]

m1_variabilityRT <- lmer(sdRT ~ WMCgroup + NFCgroup + easyP1difficultN1 + (1 | subjectnumber), data = data_easyhardRTs_subj)
summary(m1_variabilityRT) 

# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)            0.429399   0.014199  30.242
# WMCgroup              -0.009565   0.012719  -0.752
# NFCgroup              -0.009894   0.012071  -0.820
# easyP1difficultN1easy -0.054806   0.011406  -4.805
# 
# Correlation of Fixed Effects:
#   (Intr) WMCgrp NFCgrp
# WMCgroup     0.293              
# NFCgroup    -0.079 -0.026       
# esyP1dffcN1 -0.441 -0.004  0.045

m2_meanRT <- lmer(meanRT ~ WMCgroup + NFCgroup + easyP1difficultN1 + (1 | subjectnumber), data = data_easyhardRTs_subj)
summary(m2_meanRT) 

# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)              1.61695    0.03143  51.438
# WMCgroup                -0.01925    0.02792  -0.689
# NFCgroup                 0.02070    0.02644   0.783
# easyP1difficultN1static -0.01366    0.02547  -0.536
# easyP1difficultN1easy   -0.19144    0.02368  -8.085
# 
# Correlation of Fixed Effects:
#   (Intr) WMCgrp NFCgrp esyP1dffcltN1st
# WMCgroup         0.296                              
# NFCgroup        -0.068 -0.012                       
# esyP1dffcltN1st -0.380 -0.017  0.011                
# esyP1dffcltN1sy -0.408  0.000  0.024  0.501 


######################################################
######################################################

### All Required Hierarchical Linear Regressions ### - not using these anymore

## Setting Up

clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\CGE_R_Scripts\\clean_data_dm_090424.csv")

clean_data_dm_vonkim$curr_diff <- factor(clean_data_dm_vonkim$easyP1difficultN1,
                                                 levels = c(-1:1),
                                                 labels = c("difficult", "static", "easy"))

data_difficulty_subj <- clean_data_dm_vonkim %>% # handles NAs for meanRTs so the cleaning step is uneccessary
  group_by(subjectnumber, curr_diff) %>%
  summarize(
    n = n(),
    prev_diff = first(easyP1difficultN1_prev),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

## POINT 1: meanRTs

# Current Difficulty
m1_curr_meanRT <- lmer(meanRT ~ 1 + 
                         curr_diff + 
                         (1 | subjectnumber), data = data_difficulty_subj)
summary(m1_curr_meanRT) 

 

# Previous Difficulty
m1_prev_meanRT <- lmer(meanRT ~ 1 +  
                        prev_diff + 
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m1_prev_meanRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.05363  0.2316  
# Residual                  0.04878  0.2209  
# Number of obs: 255, groups:  subjectnumber, 85
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  1.61158    0.02868  56.202
# prev_diff    0.21461    0.17070   1.257
# 
# Correlation of Fixed Effects:
#   (Intr)
# prev_diff 0.000 

# WMC
m1_WMC_meanRT <- lmer(meanRT ~ 1 +
                        WMCgroup +  
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m1_WMC_meanRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.05425  0.2329  
# Residual                  0.04818  0.2195  
# Number of obs: 246, groups:  subjectnumber, 82
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  1.59866    0.03115   51.31
# WMCgroup    -0.01653    0.03115   -0.53
# 
# Correlation of Fixed Effects:
#   (Intr)
# WMCgroup 0.341 

# NFC
m1_NFC_meanRT <- lmer(meanRT ~ 1 + 
                        NFCgroup + 
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m1_NFC_meanRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.05312  0.2305  
# Residual                  0.04700  0.2168  
# Number of obs: 252, groups:  subjectnumber, 84
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  1.60536    0.02865  56.035
# NFCgroup     0.01524    0.02865   0.532
# 
# Correlation of Fixed Effects:
#   (Intr)
# NFCgroup -0.048

# Current, Previous, WMC, & NFC
m1_all_meanRT <- lmer(meanRT ~ 1 + 
                        curr_diff + 
                        prev_diff + 
                        WMCgroup + 
                        NFCgroup + 
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m1_all_meanRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.05933  0.2436  
# Residual                  0.02803  0.1674  
# Number of obs: 243, groups:  subjectnumber, 81
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)      1.66445    0.03456  48.159
# curr_diffstatic  0.01336    0.02641   0.506
# curr_diffeasy   -0.22915    0.02671  -8.579
# prev_diff        0.02046    0.13446   0.152
# WMCgroup        -0.01321    0.03090  -0.427
# NFCgroup         0.02558    0.02919   0.876
# 
# Correlation of Fixed Effects:
#   (Intr) crr_dffst crr_dffsy prv_df WMCgrp
# crr_dffsttc -0.385                                  
# curr_diffsy -0.386  0.506                           
# prev_diff   -0.067  0.088     0.173                 
# WMCgroup     0.300  0.000     0.000     0.002       
# NFCgroup    -0.063  0.000     0.001     0.003 -0.035

# Compare m1 models
AIC(m1_curr_meanRT) # 13.04949 - the better model???
AIC(m1_prev_meanRT) # 90.37742
AIC(m1_WMC_meanRT) # 89.44398
AIC(m1_NFC_meanRT) # 85.45728
AIC(m1_all_meanRT) # 21.49844 

## POINT 2: trialRTs

# Current Difficulty
m2_curr_trialRT <- lmer(sqrtRT ~ 1 + 
                         easyP1difficultN1 + 
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_curr_trialRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.01025  0.1012  
# Residual                  0.03139  0.1772  
# Number of obs: 14388, groups:  subjectnumber, 85
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)        1.250159   0.011078  112.85
# easyP1difficultN1 -0.045429   0.001757  -25.85
# 
# Correlation of Fixed Effects:
#   (Intr)
# esyP1dffcN1 0.000 

# Previous Difficulty
m2_prev_trialRT <- lmer(sqrtRT ~ 1 + 
                         easyP1difficultN1_prev + 
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_prev_trialRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.01023  0.1011  
# Residual                  0.03284  0.1812  
# Number of obs: 14388, groups:  subjectnumber, 85
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)            1.250110   0.011072  112.90
# easyP1difficultN1_prev 0.004440   0.001805    2.46
# 
# Correlation of Fixed Effects:
#   (Intr)
# esyP1dffN1_ 0.000 

# WMC
m2_wmc_trialRT <- lmer(sqrtRT ~ 1 + 
                         capacity_HighP1_lowN1_best +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_wmc_trialRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.01033  0.1016  
# Residual                  0.03240  0.1800  
# Number of obs: 13886, groups:  subjectnumber, 82
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)                 1.246027   0.012051 103.393
# capacity_HighP1_lowN1_best -0.004251   0.012051  -0.353
# 
# Correlation of Fixed Effects:
#   (Intr)
# cpc_HP1_N1_ 0.341 

# Current, Previous, & WMC
m2_all_trialRT <- lmer(sqrtRT ~ 1 + 
                         easyP1difficultN1 + 
                         easyP1difficultN1_prev + 
                         capacity_HighP1_lowN1_best +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_all_trialRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.01035  0.1017  
# Residual                  0.03093  0.1759  
# Number of obs: 13886, groups:  subjectnumber, 82
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)                 1.246068   0.012056 103.355
# easyP1difficultN1          -0.045292   0.001776 -25.506
# easyP1difficultN1_prev      0.004285   0.001783   2.403
# capacity_HighP1_lowN1_best -0.004250   0.012056  -0.353
# 
# Correlation of Fixed Effects:
#   (Intr) esP1N1 eP1N1_
# esyP1dffcN1 0.000               
# esyP1dffN1_ 0.000  0.018        
# cpc_HP1_N1_ 0.341  0.000  0.000 

## POINT 4: sdRTs (variability)

# Current Difficulty
m4_curr_sdRT <- lmer(sdRT ~ 1 + 
                         curr_diff + 
                         (1 | subjectnumber), data = data_difficulty_subj)
summary(m4_curr_sdRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.010534 0.10264 
# Residual                  0.007915 0.08897 
# Number of obs: 255, groups:  subjectnumber, 85
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)      0.45376    0.01473  30.799
# curr_diffstatic  0.01017    0.01365   0.745
# curr_diffeasy   -0.06105    0.01365  -4.473
# 
# Correlation of Fixed Effects:
#   (Intr) crr_dffst
# crr_dffsttc -0.463          
# curr_diffsy -0.463  0.500

# Previous Difficulty
m4_prev_sdRT <- lmer(sdRT ~ 1 +  
                         prev_diff + 
                         (1 | subjectnumber), data = data_difficulty_subj)
summary(m4_prev_sdRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.010066 0.10033 
# Residual                  0.009234 0.09609 
# Number of obs: 255, groups:  subjectnumber, 85
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  0.43679    0.01244  35.126
# prev_diff    0.11778    0.07426   1.586
# 
# Correlation of Fixed Effects:
#   (Intr)
# prev_diff 0.000

# WMC
m4_WMC_sdRT <- lmer(sdRT ~ 1 +
                        WMCgroup +  
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m4_WMC_sdRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.008860 0.09413 
# Residual                  0.009456 0.09724 
# Number of obs: 246, groups:  subjectnumber, 82
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  0.42325    0.01288  32.868
# WMCgroup    -0.02828    0.01288  -2.196
# 
# Correlation of Fixed Effects:
#   (Intr)
# WMCgroup 0.341 

# NFC
m4_NFC_sdRT <- lmer(sdRT ~ 1 + 
                        NFCgroup + 
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m4_NFC_sdRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.009891 0.09945 
# Residual                  0.009265 0.09626 
# Number of obs: 252, groups:  subjectnumber, 84
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)  0.43538    0.01244  34.985
# NFCgroup    -0.01250    0.01244  -1.004
# 
# Correlation of Fixed Effects:
#   (Intr)
# NFCgroup -0.048

# Current, Previous, WMC, & NFC
m4_all_sdRT <- lmer(sdRT ~ 1 + 
                        curr_diff + 
                        prev_diff + 
                        WMCgroup + 
                        NFCgroup + 
                        (1 | subjectnumber), data = data_difficulty_subj)
summary(m4_all_sdRT) 

# Random effects:
#   Groups        Name        Variance Std.Dev.
# subjectnumber (Intercept) 0.009247 0.09616 
# Residual                  0.008096 0.08998 
# Number of obs: 243, groups:  subjectnumber, 81
# 
# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)      0.436479   0.015326  28.479
# curr_diffstatic  0.013526   0.014194   0.953
# curr_diffeasy   -0.056018   0.014355  -3.902
# prev_diff        0.069408   0.072248   0.961
# WMCgroup        -0.026561   0.012889  -2.061
# NFCgroup        -0.006677   0.012175  -0.548
# 
# Correlation of Fixed Effects:
#   (Intr) crr_dffst crr_dffsy prv_df WMCgrp
# crr_dffsttc -0.467                                  
# curr_diffsy -0.468  0.506                           
# prev_diff   -0.081  0.088     0.173                 
# WMCgroup     0.282  0.000     0.000     0.003       
# NFCgroup    -0.059  0.000     0.001     0.004 -0.035

# Compare m1 models
AIC(m4_curr_sdRT) # -345.8712 - the better model???
AIC(m4_prev_sdRT) # -331.2931
AIC(m4_WMC_sdRT) # -318.9577
AIC(m4_NFC_sdRT) # -324.1173
AIC(m4_all_sdRT) # -312.3865





















#### static wasn't removed originally

# Fixed effects:
#   Estimate Std. Error t value
# (Intercept)              0.437670   0.015280  28.643
# WMCgroup                -0.026595   0.012896  -2.062
# NFCgroup                -0.006729   0.012182  -0.552
# easyP1difficultN1static  0.012326   0.014131   0.872
# easyP1difficultN1easy   -0.058403   0.014131  -4.133
# 
# Correlation of Fixed Effects:
#   (Intr) WMCgrp NFCgrp esyP1dffcltN1st
# WMCgroup         0.283                              
# NFCgroup        -0.059 -0.035                       
# esyP1dffcltN1st -0.462  0.000  0.000                
# esyP1dffcltN1sy -0.462  0.000  0.000  0.500 








#######################################################################

#data_easyhardRTs_subj_wide$meanRTdifference = "" # didn't need
# Warning messages:
#   1: In 1:data_easyhardRTs_subj_wide$subjectnumber :
#   numerical expression has 85 elements: only the first used
# 2: Unknown or uninitialised column: `meanRTdifference`. 
# 3: In data_easyhardRTs_subj_wide$meanRTdifference[subj] <- data_easyhardRTs_subj_wide$meanRT_difficult -  :
#   number of items to replace is not a multiple of replacement length

#for (subj in 1:data_easyhardRTs_subj_wide$subjectnumber) {
#  data_easyhardRTs_subj_wide$meanRTdifference[subj] <- data_easyhardRTs_subj_wide$meanRT_difficult[subj] - data_easyhardRTs_subj_wide$meanRT_easy[subj]
#}
# this didn't work because everything is in wide format probably - I didn't need to index from the same column like I normally would do in order to do loops














