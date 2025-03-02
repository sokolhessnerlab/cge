
### CGE Thesis Analyses ###



### All Required Hierarchical Linear Regressions ### - not using these anymore

## Setting Up

#rm(list=ls())

library(dplyr)
library(lme4)
library(lmerTest)
library(nlme)
library(tidyverse)

# Loading Data
#clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\CGE_R_Scripts\\clean_data_dm_090424.csv")
clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\GitHub\\cge\\R\\Proposal_CGE_R_Scripts\\clean_data_dm_112224.csv")

# Excluding Subjects
clean_data_dm_vonkim <- clean_data_dm_vonkim[clean_data_dm_vonkim$subjectnumber != 16, ]
clean_data_dm_vonkim <- clean_data_dm_vonkim[clean_data_dm_vonkim$subjectnumber != 45, ]
clean_data_dm_vonkim <- clean_data_dm_vonkim[clean_data_dm_vonkim$subjectnumber != 76, ]

# Removing Static
clean_data_dm_vonkim <- clean_data_dm_vonkim[clean_data_dm_vonkim$easyP1difficultN1 != 0,]
clean_data_dm_vonkim <- clean_data_dm_vonkim[clean_data_dm_vonkim$easyP1difficultN1_prev != 0,]

# Turning Choice Difficulty into a Factor
clean_data_dm_vonkim$curr_diff <- factor(clean_data_dm_vonkim$easyP1difficultN1,
                                         levels = c(-1, 1),
                                         labels = c("difficult", "easy"))

# fixing capacity
clean_data_dm_vonkim$capacity_HighP1_lowN1_best = round(clean_data_dm_vonkim$capacity_HighP1_lowN1_best)

# Creating Data Frames for Regressions
data_curr_diff <- clean_data_dm_vonkim %>% # only current difficulty
  group_by(subjectnumber, curr_diff) %>%
  summarize(
    n = n(),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

data_prev_diff <- clean_data_dm_vonkim %>% # only previous difficulty
  group_by(subjectnumber, easyP1difficultN1_prev) %>%
  summarize(
    n = n(),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

data_WMC <- clean_data_dm_vonkim %>% # only WMC
  group_by(subjectnumber) %>%
  summarize(
    n = n(),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

data_NFC <- clean_data_dm_vonkim %>% # only NFC
  group_by(subjectnumber) %>%
  summarize(
    n = n(),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

data_currprev_diff <- clean_data_dm_vonkim %>% # current and previous difficulty
  group_by(subjectnumber, easyP1difficultN1, easyP1difficultN1_prev) %>%
  summarize(
    n = n(),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )


# data_cont_diff <- clean_data_dm_vonkim %>% # current and previous difficulty
#   group_by(subjectnumber, easyP1difficultN1_prev) %>%
#   summarize(
#     n = n(),
#     currDiffCont = all_diff_cont,
#     WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
#     NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
#     meanRT = mean(reactiontime, na.rm = T),
#     sdRT = sd(reactiontime, na.rm = T)
#   )


##### Model 1: Subject Level Average RTs #####

# summary(m2_best_cap)
# xval_plot = seq(from = 0, to = 1, by = .1);
# coef_vals = fixef(m2_best_cap)
#
# plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["all_diff_cont"] +
#                            1*xval_plot*coef_vals["all_diff_cont:capacity_HighP1_lowN1_best"] +
#                            1*coef_vals["capacity_HighP1_lowN1_best"])^2,
#      type = 'l', lwd = 5, col = 'purple4',
#      main = 'Effect of current difficulty', xlab = 'Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')
# lines(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["all_diff_cont"] +
#                             -1*xval_plot*coef_vals["all_diff_cont:capacity_HighP1_lowN1_best"]+
#                             -1*coef_vals["capacity_HighP1_lowN1_best"])^2,
#       lwd = 5, col = 'purple1')


# Subject Level Average RTs ~ Current Difficulty ####
m1_curr_meanRT <- lmer(meanRT ~ 1 +
                         curr_diff +
                         (1 | subjectnumber), data = data_curr_diff)
summary(m1_curr_meanRT)

plot(x = data_curr_diff$curr_diff, y = data_curr_diff$meanRT, type = 'l', ylim = c(0, 3),
     main = 'Current Difficulty on Subject Level Mean RTs', xlab = 'Current Difficulty', ylab = 'Mean RTs')

# ~ When regressing current difficulty on average subject level RTs,
# regression coefficients indicate an effect of current difficulty, β = -0.24(0.3), p < .001.
# When a choice was easy, participants took .24 s less to make a choice.


# Previous Difficulty
m1_prev_meanRT <- lmer(meanRT ~ 1 +
                         easyP1difficultN1_prev +
                         (1 | subjectnumber), data = data_prev_diff)
summary(m1_prev_meanRT)

#plot(x = data_prev_diff$easyP1difficultN1_prev, y = data_prev_diff$meanRT, type = 'l',
#    main = 'Previous Difficulty on Mean RTs', xlab = 'Previous Difficulty', ylab = 'Mean RTs')

xval_plot = seq(from = 0, to = 1, by = .1);
coef_vals = fixef(m1_prev_meanRT)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["easyP1difficultN1_prev"]),
     type = 'l', lwd = 5, col = 'purple4',
     main = 'Effect of Previous Difficulty', xlab = 'Previous Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')

boxplot(meanRT ~ easyP1difficultN1_prev, data = data_prev_diff, ylim = c(0, 3),
        main = "Previous Difficulty on Subject Level RTs", ylab = "Reaction Time (seconds)", xlab = "Previous Difficulty",
        names = c("Difficult", "Easy"))

# ~ When regressing previous difficulty on average subject level RTs,
# regression coefficients indicate an effect of previous difficulty, β = 0.01(0.01), p < .01.
# When a previous choice was easy, participants took .01 s more to make a choice between the current choice options.

# WMC
m1_WMC_meanRT <- lm(meanRT ~ WMCgroup, data = data_WMC)
summary(m1_WMC_meanRT)

# plot(x = data_WMC$WMCgroup, y = data_WMC$meanRT, type = 'l',
#      main = 'WMC on Mean RTs', xlab = 'WMC', ylab = 'Mean RTs')

xval_plot = seq(from = 0, to = 1, by = .1);
coef_vals = coef(m1_WMC_meanRT)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["WMCgroup"]),
     type = 'l', lwd = 5, col = 'purple4',
     main = 'Effect of WMC', xlab = 'WMC (0 = low, 1 = high)', ylab = 'Reaction Time (seconds)')

boxplot(meanRT ~ WMCgroup, data = data_WMC, ylim = c(0, 3),
        main = "Effect of WMC Group on Reaction Time", ylab = "Reaction Time (seconds)", xlab = "WMC Group",
        names = c("Low WMC", "High WMC"))

# ~ When regressing WMC on average subject level RTs,
# regression coefficients indicate no effect of WMC, β = 0.01(0.03), p = .68.

# NFC
m1_NFC_meanRT <- lm(meanRT ~ NFCgroup, data = data_NFC)
summary(m1_NFC_meanRT)

# plot(x = data_NFC$NFCgroup, y = data_NFC$meanRT, type = 'l',
#      main = 'NFC on Mean RTs', xlab = 'NFC', ylab = 'Mean RTs')

coef_vals = coef(m1_NFC_meanRT)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["NFCgroup"]),
     type = 'l', lwd = 5, col = 'purple4',
     main = 'Effect of NFC', xlab = 'NFC (0 = low, 1 = high)', ylab = 'Reaction Time (seconds)')

boxplot(meanRT ~ NFCgroup, data = data_NFC, ylim = c(0, 3),
        main = "Effect of NFC Group on Reaction Time", ylab = "Reaction Time (seconds)", xlab = "NFC Group",
        names = c("Low NFC", "High NFC"))

# ~ When regressing NFC on average subject level RTs,
# regression coefficients indicate no effect of NFC, β = 0.01(0.03), p = .64

# Current, Previous, WMC, & NFC
m1_all_meanRT <- lmer(meanRT ~ 1 +
                        curr_diff +
                        easyP1difficultN1_prev +
                        WMCgroup +
                        NFCgroup +
                        (1 | subjectnumber), data = data_currprev_diff)
summary(m1_all_meanRT)


m1_all_meanRT_intfx <- lmer(meanRT ~ 1 +
                        curr_diff *
                        easyP1difficultN1_prev *
                        WMCgroup *
                        NFCgroup +
                        (1 | subjectnumber), data = data_currprev_diff)
summary(m1_all_meanRT_intfx)

# (Intercept)                                             1.685e+00  3.276e-02  8.645e+01  51.450  < 2e-16 ***
# curr_diffeasy                                          -2.507e-01  1.561e-02  2.310e+02 -16.061  < 2e-16 ***
# easyP1difficultN1_prev                                  6.502e-03  1.104e-02  2.310e+02   0.589    0.556
# WMCgroup                                                5.077e-02  3.276e-02  8.645e+01   1.550    0.125
# NFCgroup                                                8.112e-03  3.276e-02  8.645e+01   0.248    0.805
# curr_diffeasy:easyP1difficultN1_prev                    1.306e-03  1.561e-02  2.310e+02   0.084    0.933
# curr_diffeasy:WMCgroup                                 -6.248e-02  1.561e-02  2.310e+02  -4.002 8.47e-05 ***
# easyP1difficultN1_prev:WMCgroup                        -1.635e-02  1.104e-02  2.310e+02  -1.481    0.140
# curr_diffeasy:NFCgroup                                  8.968e-03  1.561e-02  2.310e+02   0.574    0.566
# easyP1difficultN1_prev:NFCgroup                        -7.466e-04  1.104e-02  2.310e+02  -0.068    0.946
# WMCgroup:NFCgroup                                       4.821e-03  3.276e-02  8.645e+01   0.147    0.883
# curr_diffeasy:easyP1difficultN1_prev:WMCgroup           1.018e-02  1.561e-02  2.310e+02   0.652    0.515
# curr_diffeasy:easyP1difficultN1_prev:NFCgroup          -6.671e-03  1.561e-02  2.310e+02  -0.427    0.670
# curr_diffeasy:WMCgroup:NFCgroup                         1.432e-03  1.561e-02  2.310e+02   0.092    0.927
# easyP1difficultN1_prev:WMCgroup:NFCgroup                1.251e-02  1.104e-02  2.310e+02   1.134    0.258
# curr_diffeasy:easyP1difficultN1_prev:WMCgroup:NFCgroup -1.852e-02  1.561e-02  2.310e+02  -1.186    0.237

m1_allNoNFC_meanRT_intfx <- lmer(meanRT ~ 1 +
                              curr_diff *
                              easyP1difficultN1_prev *
                              WMCgroup +
                              (1 | subjectnumber), data = data_currprev_diff)
summary(m1_allNoNFC_meanRT_intfx)

# (Intercept)                                     1.693902   0.032701  90.825390  51.799  < 2e-16 ***
# curr_diffeasy                                  -0.256514   0.016308 240.000001 -15.730  < 2e-16 ***
# easyP1difficultN1_prev                          0.005523   0.011531 240.000001   0.479 0.632407
# WMCgroup                                        0.043706   0.032701  90.825390   1.337 0.184720
# curr_diffeasy:easyP1difficultN1_prev            0.002355   0.016308 240.000001   0.144 0.885287
# curr_diffeasy:WMCgroup                         -0.055550   0.016308 240.000001  -3.406 0.000772 ***
# easyP1difficultN1_prev:WMCgroup                -0.014061   0.011531 240.000001  -1.219 0.223910
# curr_diffeasy:easyP1difficultN1_prev:WMCgroup   0.006332   0.016308 240.000001   0.388 0.698138

m1_allNoNFCprev_meanRT_intfx <- lmer(meanRT ~ 1 +
                                       curr_diff *
                                       WMCgroup +
                                       (1 | subjectnumber), data = data_currprev_diff)
summary(m1_allNoNFCprev_meanRT_intfx) # the better model

# curr_diffeasy           -0.25651    0.01630 244.00000 -15.737  < 2e-16 ***
# WMCgroup                 0.04371    0.03270  90.81785   1.337 0.184708
# curr_diffeasy:WMCgroup  -0.05555    0.01630 244.00000  -3.408 0.000766 ***

# ~ When regressing current and previous difficulty, WMC, and NFC on average subject level RTs,
# regression coefficients revealed an effect of current difficulty, β = -0.23(0.02) , p < .001,
# but not previous difficulty, β = 0.01(0.01), p = .16, WMC, β = 0.02(0.03), p =.53, or NFC, β = 0.01(0.03), p = 0.72.

# Compare m1 models
AIC(m1_curr_meanRT) # 13.04949
AIC(m1_prev_meanRT) # 42.95589
AIC(m1_WMC_meanRT) # 89.44398
AIC(m1_NFC_meanRT) # 85.45728
AIC(m1_all_meanRT) # 22.97317
AIC(m1_all_meanRT_intfx) # -41.01238
AIC(m1_allNoNFC_meanRT_intfx) # -78.32277
AIC(m1_allNoNFCprev_meanRT_intfx) # -111.1359 - the better model???

## Model 2: Trial-by-Trial RTs ####

# Current Difficulty
m2_curr_trialRT <- lmer(sqrtRT ~ 1 +
                          easyP1difficultN1 +
                          (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_curr_trialRT)

# plot(x = clean_data_dm_vonkim$easyP1difficultN1, y = clean_data_dm_vonkim$sqrtRT, type = 'l',
#      main = 'Current Difficulty on Trial RTs', xlab = 'Current Difficulty', ylab = 'Trial RTs')

# xval_plot = seq(from = 0, to = 1, by = .1);
# coef_vals = fixef(m2_curr_trialRT)
#
# plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["easyP1difficultN1"]),
#      type = 'l', lwd = 5, col = 'purple4',
#      main = 'Effect of Current Difficulty', xlab = 'Current Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')

boxplot(sqrtRT ~ easyP1difficultN1, data = clean_data_dm_vonkim, ylim = c(0, 2.5),
        main = "Current Difficulty on Trial-by-Trial RTs", ylab = "Reaction Time (seconds)", xlab = "Current Difficulty",
        names = c("Difficult", "Easy"), outline = F)

# ~ When regressing current difficulty on trial-by-trial RTs,
# regression coefficients indicate an effect of current difficulty, β = -0.05(0.002), p < .001.
# When the current choice was easy, participants took .05 s less to make a choice

# Previous Difficulty
m2_prev_trialRT <- lmer(sqrtRT ~ 1 +
                          easyP1difficultN1_prev +
                          (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_prev_trialRT)

# plot(x = clean_data_dm_vonkim$easyP1difficultN1_prev, y = clean_data_dm_vonkim$sqrtRT, type = 'l',
#      main = 'Previous on Trial RTs', xlab = 'Previous Difficulty', ylab = 'Trial RTs')

boxplot(sqrtRT ~ easyP1difficultN1_prev, data = clean_data_dm_vonkim, ylim = c(0, 2.5),
        main = "Previous Difficulty on Trial-by-Trial RTs", ylab = "Reaction Time (seconds)", xlab = "Previous Difficulty",
        names = c("Difficult", "Easy"), outline = F)

# ~ When regressing current difficulty on trial-by-trial RTs,
# regression coefficients indicate an effect of previous difficulty, β = 0.004(0.002), p < .01.
# When the previous choice was easy, participants took .004 s longer to make a choice on the current trial

# WMC
m2_wmc_trialRT <- lmer(sqrtRT ~ 1 +
                         capacity_HighP1_lowN1_best +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_wmc_trialRT)

# plot(x = clean_data_dm_vonkim$capacity_HighP1_lowN1_best, y = clean_data_dm_vonkim$sqrtRT, type = 'l',
#      main = 'WMC on Trial RTs', xlab = 'WMC', ylab = 'Trial RTs')

boxplot(sqrtRT ~ capacity_HighP1_lowN1_best, data = clean_data_dm_vonkim, ylim = c(0, 2.5),
        main = "Effect of WMC", ylab = "Reaction Time (seconds)", xlab = "WMC Group",
        names = c("Low", "High"), outline = F)

# ~ When regressing WMC on trial-by-trial RTs,
# regression coefficients indicate no effect of WMC, β = -0.004(0.01), p = .73.

# NFC
m2_nfc_trialRT <- lmer(sqrtRT ~ 1 +
                         NCS_HighP1_LowN1 +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_nfc_trialRT)

# plot(x = clean_data_dm_vonkim$NCS_HighP1_LowN1, y = clean_data_dm_vonkim$sqrtRT, type = 'l',
#      main = 'NCS on Trial RTs', xlab = 'NCS', ylab = 'Trial RTs')

boxplot(sqrtRT ~ NCS_HighP1_LowN1, data = clean_data_dm_vonkim, ylim = c(0, 2.5),
        main = "Effect of NFC", ylab = "Reaction Time (seconds)", xlab = "NFC Group",
        names = c("Low", "High"), outline = F)

# ~ When regressing NFC on trial-by-trial RTs,
# regression coefficients indicate no effect of NFC, β = 0.006(0.01), p = .61

# Current, Previous, NFC, & WMC
m2_all_trialRT <- lmer(sqrtRT ~ 1 +
                         easyP1difficultN1 +
                         easyP1difficultN1_prev +
                         capacity_HighP1_lowN1_best +
                         NCS_HighP1_LowN1 +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_all_trialRT)

m2_all_trialRT_intfx <- lmer(sqrtRT ~ 1 +
                         easyP1difficultN1 *
                         easyP1difficultN1_prev *
                         capacity_HighP1_lowN1_best *
                         NCS_HighP1_LowN1 +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_all_trialRT_intfx)

# TODO VONFIXVALUES
# easyP1difficultN1                                                                    -4.777e-02  1.818e-03  9.520e+03 -26.276  < 2e-16 ***
# easyP1difficultN1_prev                                                                3.002e-03  1.818e-03  9.520e+03   1.651   0.0987 .
# capacity_HighP1_lowN1_best                                                            7.509e-03  1.250e-02  7.700e+01   0.601   0.5497
# NCS_HighP1_LowN1                                                                      5.427e-03  1.250e-02  7.700e+01   0.434   0.6653
# easyP1difficultN1:easyP1difficultN1_prev                                             -1.539e-04  1.827e-03  9.524e+03  -0.084   0.9329
# easyP1difficultN1:capacity_HighP1_lowN1_best                                         -1.148e-02  1.818e-03  9.520e+03  -6.312 2.88e-10 ***
# easyP1difficultN1_prev:capacity_HighP1_lowN1_best                                    -4.213e-03  1.818e-03  9.520e+03  -2.318   0.0205 *
# easyP1difficultN1:NCS_HighP1_LowN1                                                    1.346e-03  1.818e-03  9.520e+03   0.740   0.4591
# easyP1difficultN1_prev:NCS_HighP1_LowN1                                              -1.716e-03  1.818e-03  9.520e+03  -0.944   0.3452
# capacity_HighP1_lowN1_best:NCS_HighP1_LowN1                                           1.690e-03  1.250e-02  7.700e+01   0.135   0.8928
# easyP1difficultN1:easyP1difficultN1_prev:capacity_HighP1_lowN1_best                   1.864e-03  1.827e-03  9.524e+03   1.020   0.3077
# easyP1difficultN1:easyP1difficultN1_prev:NCS_HighP1_LowN1                            -1.294e-03  1.827e-03  9.524e+03  -0.708   0.4788
# easyP1difficultN1:capacity_HighP1_lowN1_best:NCS_HighP1_LowN1                         1.501e-04  1.818e-03  9.520e+03   0.083   0.9342
# easyP1difficultN1_prev:capacity_HighP1_lowN1_best:NCS_HighP1_LowN1                    1.237e-03  1.818e-03  9.520e+03   0.680   0.4963
# easyP1difficultN1:easyP1difficultN1_prev:capacity_HighP1_lowN1_best:NCS_HighP1_LowN1 -3.392e-03  1.827e-03  9.524e+03  -1.857   0.0634 .

m2_all_trialRT_intfx_2wayOnly <- lmer(sqrtRT ~ 1 +
                               easyP1difficultN1 * capacity_HighP1_lowN1_best +
                               easyP1difficultN1_prev * capacity_HighP1_lowN1_best +
                               easyP1difficultN1 * NCS_HighP1_LowN1 +
                               easyP1difficultN1_prev * NCS_HighP1_LowN1 +
                               (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_all_trialRT_intfx_2wayOnly)

anova(m2_all_trialRT_intfx,m2_all_trialRT_intfx_2wayOnly) # the fully-interactive model is NOT significantly better
# the 2-way model performs best
#                                                     Estimate Std. Error         df t value Pr(>|t|)
# (Intercept)                                        1.233e+00  1.240e-02  7.799e+01  99.423  < 2e-16 ***
# easyP1difficultN1                                 -4.774e-02  1.814e-03  9.526e+03 -26.316  < 2e-16 ***
# capacity_HighP1_lowN1_best                         7.604e-03  1.238e-02  7.799e+01   0.614   0.5407
# easyP1difficultN1_prev                             3.080e-03  1.814e-03  9.526e+03   1.698   0.0896 .
# NCS_HighP1_LowN1                                   4.914e-03  1.169e-02  7.800e+01   0.420   0.6754
# easyP1difficultN1:capacity_HighP1_lowN1_best      -1.145e-02  1.811e-03  9.526e+03  -6.322 2.69e-10 ***
# capacity_HighP1_lowN1_best:easyP1difficultN1_prev -4.102e-03  1.811e-03  9.526e+03  -2.265   0.0235 *
# easyP1difficultN1:NCS_HighP1_LowN1                 1.286e-03  1.711e-03  9.526e+03   0.752   0.4523
# easyP1difficultN1_prev:NCS_HighP1_LowN1           -2.135e-03  1.711e-03  9.526e+03  -1.248   0.2121

# decision time... VONFIXVALUES
# - increases with current difficulty (which is stronger in high vs. low capacity folks; -0.055 for high cap; -0.033 for low cap)
# - decreases with previous difficulty ONLY in low capacity folks (0.0083 for low cap; 0.00062 for high cap)
# Need for cognition does NOT affect decision time alone or in interaction w/ other variables.



m2_allNoNFC_trialRT_intfx_2wayonly <- lmer(sqrtRT ~ 1 +
                               easyP1difficultN1 * capacity_HighP1_lowN1_best +
                               easyP1difficultN1_prev * capacity_HighP1_lowN1_best +
                               (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_allNoNFC_trialRT_intfx_2wayonly)


# MUST RE-FIT THIS MODEL AND THE PREVIOUS ONE TO LIMIT TO THE FOLKS W/ NFC SCORES FOR ANOVA-BASED COMPARISON
m2_allNoNFC_trialRT_intfx_2wayonly_subset <- lmer(sqrtRT ~ 1 +
                                             easyP1difficultN1 * capacity_HighP1_lowN1_best +
                                             easyP1difficultN1_prev * capacity_HighP1_lowN1_best +
                                             (1 | subjectnumber), data = clean_data_dm_vonkim[is.finite(clean_data_dm_vonkim$NCS_HighP1_LowN1),])
m2_all_trialRT_intfx_2wayOnly_subset <- lmer(sqrtRT ~ 1 +
                                        easyP1difficultN1 * capacity_HighP1_lowN1_best +
                                        easyP1difficultN1_prev * capacity_HighP1_lowN1_best +
                                        easyP1difficultN1 * NCS_HighP1_LowN1 +
                                        easyP1difficultN1_prev * NCS_HighP1_LowN1 +
                                        (1 | subjectnumber), data = clean_data_dm_vonkim[is.finite(clean_data_dm_vonkim$NCS_HighP1_LowN1),])

summary(m2_all_trialRT_intfx_2wayOnly_subset)


anova(m2_all_trialRT_intfx_2wayOnly_subset,m2_allNoNFC_trialRT_intfx_2wayonly_subset) # IT'S NOT BETTER W/ NCS IN IT!
# TODO VONFIXVALUES
# easyP1difficultN1                                                   -4.874e-02  1.816e-03  9.642e+03 -26.841  < 2e-16 ***
# easyP1difficultN1_prev                                               2.827e-03  1.816e-03  9.642e+03   1.557   0.1195
# capacity_HighP1_lowN1_best                                           6.192e-03  1.241e-02  7.999e+01   0.499   0.6191
# easyP1difficultN1:easyP1difficultN1_prev                             9.080e-06  1.824e-03  9.646e+03   0.005   0.9960
# easyP1difficultN1:capacity_HighP1_lowN1_best                        -1.034e-02  1.816e-03  9.642e+03  -5.694 1.28e-08 ***
# easyP1difficultN1_prev:capacity_HighP1_lowN1_best                   -4.073e-03  1.816e-03  9.642e+03  -2.243   0.0249 *
# easyP1difficultN1:easyP1difficultN1_prev:capacity_HighP1_lowN1_best  1.157e-03  1.824e-03  9.646e+03   0.634   0.5261

# ~ When regressing current and previous difficulty, WMC, and NFC on trial-by-trial RTs,
# regression coefficients revealed an effect of current, β = -0.04(0.002), p < .001, and
# previous difficulty, β = 0.004(0.002), p < .01,
# but not WMC, β = -0.003(0.01), p = 0.8 or NFC, β = 0.1(0.01), p = 0.4

# Removed NFC, & WMC
# m2_remove1_trialRT <- lmer(sqrtRT ~ 1 +
#                          easyP1difficultN1 +
#                          easyP1difficultN1_prev +
#                          (1 | subjectnumber), data = clean_data_dm_vonkim)
# summary(m2_remove1_trialRT)

# ~ After removing WMC and NFC from the model, the new model regression coefficients revealed an effect of current, β = -0.05(0.002), p < .001, and
# previous difficulty, β = 0.004(0.002), p < .01.


AIC(m2_curr_trialRT) # -6787.401
AIC(m2_prev_trialRT) # -6101.914
AIC(m2_wmc_trialRT) # -6013.362
AIC(m2_nfc_trialRT) # -6169.615
AIC(m2_all_trialRT) # -6694.464
#AIC(m2_remove1_trialRT) # -8594.652
AIC(m2_all_trialRT_intfx) # -6608.797
AIC(m2_allNoNFC_trialRT_intfx) # -6656.221 - the best model???




## Model 3: Pupil Window 2 ####

m3_wind2_all_intfx = lmer(wind2_effort_isi_mean ~
                            easyP1difficultN1 *
                            easyP1difficultN1_prev *
                            capacity_HighP1_lowN1_best *
                            NCS_HighP1_LowN1 +
                            (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m3_wind2_all_intfx)

m3_wind2_allNoPrev_intfx = lmer(wind2_effort_isi_mean ~
                            easyP1difficultN1 *
                            capacity_HighP1_lowN1_best *
                            NCS_HighP1_LowN1 +
                            (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m3_wind2_allNoPrev_intfx)

AIC(m3_wind2_all_intfx) # 592.9789
AIC(m3_wind2_allNoPrev_intfx) # 500.4526 - the better model???

# plot(x = clean_data_dm_vonkim$easyP1difficultN1, y = clean_data_dm_vonkim$wind2_effort_isi_mean,
#      ylim = c(min(clean_data_dm_vonkim$wind2_effort_isi_mean), max(clean_data_dm_vonkim$wind2_effort_isi_mean)))


## Model 4: RT Variability ####

# Current Difficulty
m4_curr_sdRT <- lmer(sdRT ~ 1 +
                       curr_diff +
                       (1 | subjectnumber), data = data_curr_diff)
summary(m4_curr_sdRT)

test = rev(data_curr_diff$curr_diff)

data_curr_diff$curr_diff <- factor(data_curr_diff$curr_diff, levels = rev(levels(data_curr_diff$curr_diff)))

plot(x = data_curr_diff$curr_diff, y = data_curr_diff$sdRT, type = 'l', ylim = c(min(data_curr_diff$sdRT) - .2, max(data_curr_diff$sdRT) + .2),
     main = 'RT Variability (standard deviations)', xlab = 'Current Difficulty', ylab = 'Reaction Time (seconds)')





# ~ When regressing current difficulty on RT variability,
# regression coefficients indicate an effect of current difficulty, β = -0.06(0.01), p < .001.
# When current choices were easy, participants were .06 s less variable when making a choice.


# Previous Difficulty
m4_prev_sdRT <- lmer(sdRT ~ 1 +
                       easyP1difficultN1_prev +
                       (1 | subjectnumber), data = data_prev_diff)
summary(m4_prev_sdRT)

# plot(x = data_prev_diff$prev_diff, y = data_prev_diff$sdRT, type = 'l',
#      main = 'Previous Difficulty on RT Varaibility', xlab = 'Previous Difficulty', ylab = 'RT Variability')

boxplot(sdRT ~ easyP1difficultN1_prev, data = data_prev_diff, ylim = c(0, 1),
        main = "Effect of Previous Difficulty on RT Variability", ylab = "Reaction Time (seconds)", xlab = "Previous Difficulty",
        names = c("Difficult", "Easy"))

# ~ When regressing previous difficulty on RT variability,
# regression coefficients indicate no effect of previous difficulty, β = -0.003(0.004), p = .49

# WMC
m4_WMC_sdRT <- lm(sdRT ~ WMCgroup, data = data_WMC)
summary(m4_WMC_sdRT)

# plot(x = data_WMC$WMCgroup, y = data_WMC$sdRT, type = 'l',
#      main = 'WMC on RT Variability', xlab = 'WMC', ylab = 'RT Variability')

boxplot(sdRT ~ WMCgroup, data = data_WMC, ylim = c(0, 1),
        main = "Effect of WMC Group on RT Variability", ylab = "Reaction Time (seconds)", xlab = "WMC Group",
        names = c("Low WMC", "High WMC"), outline = F)

# ~ When regressing WMC on RT variability,
# regression coefficients indicate no effect of WMC, β = 0.0006(0.02), p = .97


# NFC
m4_NFC_sdRT <- lm(sdRT ~ NFCgroup , data = data_NFC)
summary(m4_NFC_sdRT)

# plot(x = data_NFC$NFCgroup, y = data_NFC$sdRT, type = 'l',
#      main = 'NFC on RT Variability', xlab = 'NFC', ylab = 'RT Variability')

boxplot(sdRT ~ NFCgroup, data = data_NFC, ylim = c(0, 1),
        main = "Effect of NFC Group on RT Variability", ylab = "Reaction Time (seconds)", xlab = "NFC Group",
        names = c("Low NFC", "High NFC"), outline = F)

# ~ When regressing NFC on RT variability,
# regression coefficients indicate no effect of NFC, β = -0.01(0.01), p = .22

# Current, Previous, WMC, & NFC
m4_all_sdRT <- lmer(sdRT ~ 1 +
                      curr_diff +
                      easyP1difficultN1_prev +
                      WMCgroup +
                      NFCgroup +
                      (1 | subjectnumber), data = data_currprev_diff)
summary(m4_all_sdRT)

m4_all_sdRT_intfx_2wayonly <- lmer(sdRT ~ 1 +
                            easyP1difficultN1 * WMCgroup +
                            easyP1difficultN1_prev * WMCgroup +
                            easyP1difficultN1 * NFCgroup +
                            easyP1difficultN1_prev * NFCgroup +
                            (1 | subjectnumber), data = data_currprev_diff)
summary(m4_all_sdRT_intfx_2wayonly)

# (Intercept)          0.39294    0.01408 108.41122  27.903  < 2e-16 ***
# curr_diffdifficult   0.06102    0.01013  84.00000   6.025 4.33e-08 ***

# (Intercept)                      4.122e-01  1.383e-02  7.800e+01  29.798  < 2e-16 ***
# easyP1difficultN1               -3.192e-02  4.858e-03  2.370e+02  -6.571 3.14e-10 ***
# WMCgroup                        -6.272e-03  1.381e-02  7.800e+01  -0.454    0.651
# easyP1difficultN1_prev          -3.977e-03  4.858e-03  2.370e+02  -0.819    0.414
# NFCgroup                        -9.526e-03  1.304e-02  7.800e+01  -0.730    0.467
# easyP1difficultN1:WMCgroup      -5.968e-03  4.849e-03  2.370e+02  -1.231    0.220
# WMCgroup:easyP1difficultN1_prev -4.150e-03  4.849e-03  2.370e+02  -0.856    0.393
# easyP1difficultN1:NFCgroup      -1.207e-03  4.580e-03  2.370e+02  -0.263    0.792
# easyP1difficultN1_prev:NFCgroup -6.213e-04  4.580e-03  2.370e+02  -0.136    0.892


m4_currDiff_sdRT <- lmer(sdRT ~ 1 +
                           easyP1difficultN1 +
                           (1 | subjectnumber), data = data_currprev_diff)
summary(m4_currDiff_sdRT)
# (Intercept)         0.419867   0.013080  83.999994  32.099  < 2e-16 ***
# easyP1difficultN1  -0.031253   0.004506 254.000003  -6.935 3.35e-11 ***


plot(x = data_currprev_diff$easyP1difficultN1 == -1, y = data_currprev_diff$sdRT,
     type = 'l', ylim = c(min(data_currprev_diff$sdRT) - .2, max(data_currprev_diff$sdRT) + .2),
     main = 'RT Variability (standard deviations)', xlab = 'Current Difficulty', ylab = 'Reaction Time (seconds)')



m4_sdRT_pd <- lmer(sdRT ~ 1 +
                           easyP1difficultN1_prev +
                           (1 | subjectnumber), data = data_currprev_diff)
summary(m4_sdRT_pd)
# easyP1difficultN1_prev  -0.002825   0.004911 254.000001  -0.575    0.566
m4_sdRT_wmc <- lmer(sdRT ~ 1 +
                      WMCgroup +
                     (1 | subjectnumber), data = data_currprev_diff)
summary(m4_sdRT_wmc)
# WMCgroup    -0.008108   0.013794 79.999994  -0.588    0.558
m4_sdRT_nfc <- lmer(sdRT ~ 1 +
                      NFCgroup +
                      (1 | subjectnumber), data = data_currprev_diff)
summary(m4_sdRT_nfc)
# NFCgroup    -0.01554    0.01308 82.00000  -1.188    0.238

# Create the initial line plot
plot(1, type = 'n', xlim = 'n', ylim = c(min(data_currprev_diff$sdRT) - .1, max(data_currprev_diff$sdRT) + .2),
     main = 'RT Variability (standard deviations)', xlab = 'Current Difficulty', ylab = 'Reaction Time (seconds)')

# Overlay boxplots for the two categories of easyP1difficultN1
boxplot(sdRT ~ easyP1difficultN1 == -1, data = data_currprev_diff,
        add = TRUE, col = rgb(0.8, 0.8, 0.8, 0.3), outline = FALSE,
        boxwex = 0.2)  # Adjust box width to fit on the plot


# Recode the 'easyP1difficultN1' variable to factors with 'Easy' and 'Difficult' labels
data_currprev_diff$easyP1difficultN1 <- factor(data_currprev_diff$easyP1difficultN1, levels = rev(c(-1, 1)), labels = c("Easy", "Difficult"))

# Create the base plot (empty, just the axes)
plot(1, type = 'n',
     xlim = c(0.5, 2.5),  # Set limits to fit two boxplots
     ylim = c(min(data_currprev_diff$sdRT) - .1, max(data_currprev_diff$sdRT) + .2),
     main = 'RT Variability (standard deviations)',
     xlab = 'Current Difficulty',
     ylab = 'Reaction Time (seconds)',
     xaxt = 'n',  # Suppress the x-axis
     yaxt = 'n')  # Suppress the y-axis

# Overlay boxplots for the two categories: Easy and Difficult
boxplot(sdRT ~ easyP1difficultN1, data = data_currprev_diff,
        at = c(1, 2),  # Place "Easy" at 1, "Difficult" at 2
        col = rgb(0.8, 0.8, 0.8, 0.3),
        outline = FALSE,
        boxwex = 0.2,
        add = TRUE)  # Add boxplots




data_curr_diff$curr_diff <- factor(data_curr_diff$curr_diff, levels = rev(levels(data_curr_diff$curr_diff)))



m4_all_sdRT_intfx <- lmer(sdRT ~ 1 +
                      easyP1difficultN1 *
                      easyP1difficultN1_prev *
                      WMCgroup *
                      NFCgroup +
                      (1 | subjectnumber), data = data_currprev_diff)
summary(m4_all_sdRT_intfx)

# curr_diffeasy                                           -0.063227   0.009780 231.000000  -6.465 5.97e-10 ***
# easyP1difficultN1_prev                                  -0.010033   0.006916 231.000000  -1.451    0.148
# WMCgroup                                                -0.001623   0.014734  96.748043  -0.110    0.913
# NFCgroup                                                -0.003170   0.014734  96.748043  -0.215    0.830
# curr_diffeasy:easyP1difficultN1_prev                     0.012023   0.009780 231.000000   1.229    0.220
# curr_diffeasy:WMCgroup                                  -0.011075   0.009780 231.000000  -1.132    0.259
# easyP1difficultN1_prev:WMCgroup                         -0.002939   0.006916 231.000000  -0.425    0.671
# curr_diffeasy:NFCgroup                                  -0.005775   0.009780 231.000000  -0.591    0.555
# easyP1difficultN1_prev:NFCgroup                         -0.003061   0.006916 231.000000  -0.443    0.659
# WMCgroup:NFCgroup                                        0.015222   0.014734  96.748043   1.033    0.304
# curr_diffeasy:easyP1difficultN1_prev:WMCgroup           -0.002544   0.009780 231.000000  -0.260    0.795
# curr_diffeasy:easyP1difficultN1_prev:NFCgroup            0.005359   0.009780 231.000000   0.548    0.584
# curr_diffeasy:WMCgroup:NFCgroup                         -0.009939   0.009780 231.000000  -1.016    0.311
# easyP1difficultN1_prev:WMCgroup:NFCgroup                 0.002351   0.006916 231.000000   0.340    0.734
# curr_diffeasy:easyP1difficultN1_prev:WMCgroup:NFCgroup  -0.003279   0.009780 231.000000  -0.335    0.738





# curr_diffeasy  -0.062505   0.009013 254.000003  -6.935 3.35e-11 ***

# ~ When regressing current and previous difficulty, WMC and NFC on RT variability,
# regression coefficients revealed an effect of current difficulty, β = -0.06(0.009) , p < .001, but not
# previous difficulty β = -0.003(0.005), p = .56, WMC, β = -0.006(0.01), p = .65, or NFC, β = -0.009(0.01), p = 0.47.

# Compare m4 models
AIC(m4_curr_sdRT) # -259.3117
AIC(m4_prev_sdRT) # -273.2531
AIC(m4_WMC_sdRT) # -92.11725
AIC(m4_NFC_sdRT) # -97.32521
AIC(m4_all_sdRT) # -485.5346
AIC(m4_all_sdRT_intfx) # -384.6197
AIC(m4_currDiff_sdRT) # -525.2445 - the better model???



############################################
# Starting Regressions with Continuous Variables

clean_data_dm_vonkim$diff_cont = abs(abs(clean_data_dm_vonkim$choiceP - 0.5)*2-1); # JUST for the easy/difficult dynamic trials
clean_data_dm_vonkim$prev_diff_cont = c(NA,clean_data_dm_vonkim$diff_cont[1:(length(clean_data_dm_vonkim$diff_cont)-1)]) # for dynamic trials
clean_data_dm_vonkim$prev_diff_cont[clean_data_dm_vonkim$trialnumber == 1] = NA;

sdRT = sd(clean_data_dm_vonkim$reactiontime, na.rm = T)

# data_cont <- clean_data_dm_vonkim %>% # only NFC
#   group_by(subjectnumber) %>%
#   reshape(
#     n = n(),
#     diff_cont = abs(abs(clean_data_dm_vonkim$choiceP - 0.5)*2-1), # JUST for the easy/difficult dynamic trials,
#     sqrtRT = sqrtRT
#   )
#
# data_cont$prev_diff_cont = c(NA,data_cont$diff_cont[1:(length(data_cont$diff_cont)-1)]) # for dynamic trials
# data_cont$prev_diff_cont[data_cont$trialnumber == 1] = NA;


# Current, Previous, WMC, & NFC
test_all_sdRT <- lmer(sdRT ~ 1 +
                      diff_cont +
                      prev_diff_cont +
                      complexspan_demeaned +
                      NCS +
                      (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(test_all_sdRT)

test_all_sdRT_intfx <- lmer(sdRT ~ 1 +
                        diff_cont *
                        prev_diff_cont *
                        complexspan_demeaned *
                        NCS +
                        (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(test_all_sdRT_intfx)





cor.test(clean_data_dm_vonkim$NCS, clean_data_dm_vonkim$complexspan)
cor.test(clean_data_dm_vonkim$NCS, clean_data_dm_vonkim$complexspan_demeaned)
cor.test(clean_data_dm_vonkim$capacity_HighP1_lowN1_best, clean_data_dm_vonkim$NCS_HighP1_LowN1)
















