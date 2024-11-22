
### CGE Thesis Analyses ###



### All Required Hierarchical Linear Regressions ### - not using these anymore

## Setting Up

rm(list=ls())

library(dplyr)
library(lme4)
library(lmerTest)
library(nlme)
library(tidyverse)

# Loading Data
clean_data_dm_vonkim <- read.csv("C:\\Users\\jvonm\\Documents\\CGE_R_Scripts\\clean_data_dm_090424.csv")

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
  group_by(subjectnumber, curr_diff, easyP1difficultN1_prev) %>%
  summarize(
    n = n(),
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )

data_cont_diff <- clean_data_dm_vonkim %>% # current and previous difficulty
  group_by(subjectnumber, easyP1difficultN1_prev) %>%
  summarize(
    n = n(),
    currDiffCont = all_diff_cont,
    WMCgroup = mean(capacity_HighP1_lowN1_best, na.rm = T),
    NFCgroup = mean(NCS_HighP1_LowN1, na.rm = T),
    meanRT = mean(reactiontime, na.rm = T),
    sdRT = sd(reactiontime, na.rm = T)
  )


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


# Subject Level Average RTs ~ Current Difficulty
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

# ~ When regressing current and previous difficulty, WMC, and NFC on average subject level RTs,
# regression coefficients revealed an effect of current difficulty, β = -0.23(0.02) , p < .001,
# but not previous difficulty, β = 0.01(0.01), p = .16, WMC, β = 0.02(0.03), p =.53, or NFC, β = 0.01(0.03), p = 0.72.

# Compare m1 models
AIC(m1_curr_meanRT) # 13.04949 - the better model???
AIC(m1_prev_meanRT) # 42.95589
AIC(m1_WMC_meanRT) # 89.44398
AIC(m1_NFC_meanRT) # 85.45728
AIC(m1_all_meanRT) # 22.97317

## Model 2: Trial-by-Trial RTs

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


m2_allNoNFC_trialRT_intfx <- lmer(sqrtRT ~ 1 +
                               easyP1difficultN1 *
                               easyP1difficultN1_prev *
                               capacity_HighP1_lowN1_best +
                               (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_allNoNFC_trialRT_intfx)

m2_allNoWMC_trialRT_intfx <- lmer(sqrtRT ~ 1 +
                               easyP1difficultN1 *
                               easyP1difficultN1_prev *
                               NCS_HighP1_LowN1 +
                               (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_allNoWMC_trialRT_intfx)




# ~ When regressing current and previous difficulty, WMC, and NFC on trial-by-trial RTs,
# regression coefficients revealed an effect of current, β = -0.04(0.002), p < .001, and
# previous difficulty, β = 0.004(0.002), p < .01,
# but not WMC, β = -0.003(0.01), p = 0.8 or NFC, β = 0.1(0.01), p = 0.4

# Removed NFC, & WMC
m2_remove1_trialRT <- lmer(sqrtRT ~ 1 +
                         easyP1difficultN1 +
                         easyP1difficultN1_prev +
                         (1 | subjectnumber), data = clean_data_dm_vonkim)
summary(m2_remove1_trialRT)

# ~ After removing WMC and NFC from the model, the new model regression coefficients revealed an effect of current, β = -0.05(0.002), p < .001, and
# previous difficulty, β = 0.004(0.002), p < .01.


AIC(m2_curr_trialRT) # -8603.169 - the best model???
AIC(m2_prev_trialRT) # -7955.998
AIC(m2_wmc_trialRT) # -7867.486
AIC(m2_nfc_trialRT) # -8007.781
AIC(m2_all_trialRT) # -8494.012
AIC(m2_remove1_trialRT) # -8594.652



## Model 4: RT Variability

# Current Difficulty
m4_curr_sdRT <- lmer(sdRT ~ 1 +
                       curr_diff +
                       (1 | subjectnumber), data = data_curr_diff)
summary(m4_curr_sdRT)

plot(x = data_curr_diff$curr_diff, y = data_curr_diff$meanRT, type = 'l', ylim = c(0, 3),
     main = 'Current Difficulty on RT Variability', xlab = 'Current Difficulty', ylab = 'RT Variability')

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

m4_all_sdRT_intfx <- lmer(sdRT ~ 1 +
                      curr_diff *
                      easyP1difficultN1_prev *
                      WMCgroup *
                      NFCgroup +
                      (1 | subjectnumber), data = data_currprev_diff)
summary(m4_all_sdRT_intfx)

# ~ When regressing current and previous difficulty, WMC and NFC on RT variability,
# regression coefficients revealed an effect of current difficulty, β = -0.06(0.009) , p < .001, but not
# previous difficulty β = -0.003(0.005), p = .56, WMC, β = -0.006(0.01), p = .65, or NFC, β = -0.009(0.01), p = 0.47.

# Compare m4 models
AIC(m4_curr_sdRT) # -345.8712
AIC(m4_prev_sdRT) # -352.31 - the better model???
AIC(m4_WMC_sdRT) # -318.9577
AIC(m4_NFC_sdRT) # -324.1173
AIC(m4_all_sdRT) # -314.3598




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
















