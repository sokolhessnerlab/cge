# CGE Data Analysis Script
#
# Script to analyze the data collected in-person for CGE during Fall '23 & Winter '24
# (Control & Gambling & Eyetracking) study.
#

rm(list=ls()); # Clear the workspace


# STEP 1: SET YOUR WORKING DIRECTORY!
# On PSH's computers...
setwd('/Users/sokolhessner/Documents/gitrepos/cge/');
# On Von's PC Laptop "tabletas"...
setwd('C:/Users/jvonm/Documents/GitHub/cge');

# STEP 2: then run from here on the same
config = config::get()

#### Loading Data #### 
# Von - May need just in case tabletas disappears again Sys.setenv(R_CONFIG_ACTIVE = 'tabletas')
Sys.setenv(R_CONFIG_ACTIVE = 'tabletas')

setwd(config$path$data$processed)

# #Von's 
# setwd('S:/shlab/Projects/CGE/data/preprocessed')

# Load Decision-Making Data
fn = dir(pattern = glob2rx('cge_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
data_dm = read.csv(fn[number_of_files]) # decision-making data

# Load Working Memory Data
fn = dir(pattern = glob2rx('cge_processed_complexspan_data_*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
complexSpanScores = read.csv(fn[number_of_files]) # working memory data 

# Load Qualtrics Survey Data
fn = dir(pattern = glob2rx('cge_processed_survey_data_*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
survey_data = read.csv(fn[number_of_files]) # working memory data 

number_of_subjects = length(unique(data_dm$subjectnumber));

#### Data Quality Checks & Exclusions ####

# Exclude on the basis of DM task performance
# (using... check trials, RTs, choices)

# EXCLUSION: Check Trials
check_trial_failurerate = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  check_trial_index = which(tmpdata$ischecktrial==1);
  correct_answers = (0.5 * tmpdata$riskyopt1[check_trial_index] +
                       0.5 * tmpdata$riskyopt2[check_trial_index]) > tmpdata$safe[check_trial_index];
  check_trial_failurerate[subj] = length(which(!tmpdata$choice[check_trial_index] == correct_answers))/length(check_trial_index);
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green', 
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('All Subjects; Subj ', subj),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
}

check_trial_criterion = 0.2; # The maximum percent of check trials that can be missed
# (there were 10 check trials)
# chance is 0.5, perfect is 0.0.

keep_check_trial = check_trial_failurerate <= check_trial_criterion; # 3 did not meet criteria: 16, 45, 76 (4/5/24)

# EXCLUSION: RTs

mean_rts = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  mean_rts[subj] = mean(tmpdata$reactiontime, na.rm = T)
}

keep_dm_rt = mean_rts > 0.85;

mean_rts[keep_dm_rt]
hist(mean_rts[keep_dm_rt]) # histogram of mean rts
mean(mean_rts[keep_dm_rt]) # mean rt 1.59362 seconds (4/4/24)

### Survey Exclusions 
# quick responses to surveys (still figuring out how that should be done)
# questionable pattern of responses to surveys (nail in the coffin)


#### Create clean data frames ####

keep_participants = which(keep_check_trial & keep_dm_rt);

# Create clean data frames for data!
clean_data_dm = data_dm[data_dm$subjectnumber %in% keep_participants,]
clean_data_complexspan = complexSpanScores[complexSpanScores$subjectnumber %in% keep_participants,]
clean_data_survey = survey_data[survey_data$subjectID %in% keep_participants,]

number_of_clean_subjects = length(keep_participants); 
number_of_clean_subjects # 85 participants (4/5/24)

#### BASIC DATA ANALYSIS ####

# (Separately for DM & WM, & Qualtrics data)
# Descriptives & simple averages of task performance

#### Survey Analysis #### 
library(corrplot)

# DATA: age, ethnicity, education, firstgen, politicalorientation, IUS_probability, IUS_inihibitory, IUS, NCS, SNS_ability, SNS_preference, SNS, PSS
# ANALYSIS: min, max, mean, SD, median, variance
# GRAPHS: histograms, scatterplots, correlograms, pairwise correlations

# Age
mean(clean_data_survey$age) # 19.8 years old (4/5/24)
range(clean_data_survey$age) # 12-35 (4/5/24) I think there is a typo - cge074 put 12
sd(clean_data_survey$age) # 2.63 years (4/5/24)
hist(clean_data_survey$age)

# Main Questionnaire Scores: 

# NCS
mean(clean_data_survey$NCS, na.rm = T) # M = 59.40476
sd(clean_data_survey$NCS, na.rm = T) # SD = 10.85293
median(clean_data_survey$NCS, na.rm = T) # 60
range(clean_data_survey$NCS, na.rm = T) # 39-80
# IUS
mean(clean_data_survey$IUS, na.rm = T) # M = 33.82143
sd(clean_data_survey$IUS, na.rm = T) # SD = 8.067726
median(clean_data_survey$IUS, na.rm = T) # 33
range(clean_data_survey$IUS, na.rm = T) # 16-57
# SNS
mean(clean_data_survey$SNS, na.rm = T) # M = 4.05506
sd(clean_data_survey$SNS, na.rm = T) # SD = 0.8809717
median(clean_data_survey$SNS, na.rm = T) # 4.125
range(clean_data_survey$SNS, na.rm = T) # 1.625-5.875
# PSS
mean(clean_data_survey$PSS, na.rm = T) # M = 22.96429
sd(clean_data_survey$PSS, na.rm = T) # SD = 6.340625
median(clean_data_survey$PSS, na.rm = T) # 23
range(clean_data_survey$PSS, na.rm = T) # 7-43

cor_matrix = cor(cbind(clean_data_survey[,c('NCS','IUS','SNS','PSS')],clean_data_complexspan['compositeSpanScore']),
                 use = 'complete.obs');
cor.test(clean_data_survey$NCS, clean_data_survey$IUS) # r(82) = -0.239142, p = 0.02846
cor.test(clean_data_survey$NCS, clean_data_survey$SNS) # n.s., r(82) = 0.1917, p = 0.08066 
cor.test(clean_data_survey$NCS, clean_data_survey$PSS) # r(82) = -0.2855222, p = 0.008471
cor.test(clean_data_survey$IUS, clean_data_survey$SNS) # n.s., r(82) = 0.139341, p = 0.2062
cor.test(clean_data_survey$IUS, clean_data_survey$PSS) # r(82) = 0.4737519, p = 5.321e-06 
cor.test(clean_data_survey$SNS, clean_data_survey$PSS) # n.s., r(82) = -0.1120716, p = 0.3101
cor.test(clean_data_survey$NCS, clean_data_complexspan$compositeSpanScore) # n.s., r(79) = 0.04481055, p = 0.6912
cor.test(clean_data_survey$IUS, clean_data_complexspan$compositeSpanScore) # n.s., r(79) = -0.003903688, p = 0.9724
cor.test(clean_data_survey$SNS, clean_data_complexspan$compositeSpanScore) # n.s., r(79) = 0.262511, p = 0.01791
cor.test(clean_data_survey$PSS, clean_data_complexspan$compositeSpanScore) # n.s., r(79) = -0.1300933, p = 0.247

plot(cbind(clean_data_survey[,c('NCS','IUS','SNS','PSS')],clean_data_complexspan['compositeSpanScore']));

# Higher NCS, Lower IUS - maybe because people with higher NFC are more open to and like uncertainty because it allows them to think
# Higher NCS, Lower PSS

# Higher IUS, Higher PSS

# NO RELATIONSHIPS TO WORKING MEMORY COMPOSITE SPAN - reflects similar findings in da Silva Castanheira et al. (2021)

corrplot(cor_matrix, type = 'lower')
# Positive = blue
# Negative = red

# Any similarities to working memory span? - (Von) what is this question referring to?

# TAKEAWAYS: - does this still hold true?
# Because of several inter-item correlations, it's not wise to include these in the same model
# and we should expect some of these to perform similarly (i.e. PSS & IUS may be similar).
# However, because they're unrelated to composite span, we can freely include them alongside
# composite working memory span (and related variables). 

par(mfrow = c(2,2)) # Allowing graphs to plot 2 x 2
hist(clean_data_survey$NCS, ylab = '', xlab = 'Score', main = 'Need for Cognition (NCS)')
abline(v = mean(clean_data_survey$NCS, na.rm = T), col = 'red', lwd = 5)

hist(clean_data_survey$IUS, ylab = '', xlab = 'Score', main = 'Intolerance of Uncertainty (IUS)')
abline(v = mean(clean_data_survey$IUS, na.rm = T), col = 'blue', lwd = 5)

hist(clean_data_survey$SNS, ylab = '', xlab = 'Score', main = 'Subjective Numerancy Scale (SNS)')
abline(v = mean(clean_data_survey$SNS, na.rm = T), col = 'green', lwd = 5)

hist(clean_data_survey$PSS, ylab = '', xlab = 'Score', main = 'Perceived Stress Scale (PSS)')
abline(v = mean(clean_data_survey$PSS, na.rm = T), col = 'magenta', lwd = 5)

par(mfrow = c(1,1)) # Returning graphs to plot 1 at a time

# Make binary categorical variables for clean_data_dm based on each of the major Surveys (Con) Why empty when called?


clean_data_dm$NCS_HighP1_LowN1 = (clean_data_dm$NCS >= median(clean_data_survey$NCS, na.rm = T))*2-1;
clean_data_dm$IUS_HighP1_LowN1 = (clean_data_dm$IUS >= median(clean_data_survey$IUS, na.rm = T))*2-1;
clean_data_dm$SNS_HighP1_LowN1 = (clean_data_dm$SNS >= median(clean_data_survey$SNS, na.rm = T))*2-1;
clean_data_dm$PSS_HighP1_LowN1 = (clean_data_dm$PSS >= median(clean_data_survey$PSS, na.rm = T))*2-1;



#### DM task Analysis ####
# Analysis for static trials: Mean p(gamble), optimization
mean_pgamble = array(dim = c(number_of_clean_subjects,1));
static_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
dynamic_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easyACC_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easyREJ_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]; # defines this person's data
  mean_pgamble[subj] = mean(tmpdata$choice, na.rm = T);
  static_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$static0dynamic1 == 0], na.rm=T);
  dynamic_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$static0dynamic1 == 1], na.rm=T);
  easy_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$easyP1difficultN1 == 1], na.rm = T);
  diff_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$easyP1difficultN1 == -1], na.rm = T);
  easyACC_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP > .5)], na.rm = T);
  easyREJ_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP < .5)], na.rm = T);
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green', 
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('Kept Subjects; Subj ', subj_id),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
}

# Create simple summary object with p(gamble) descriptives
column_names_rdm = c(
  'mean_pgamble',
  'static_mean_pgamble',
  'dynamic_mean_pgamble', 
  'easy_mean_pgamble',
  'diff_mean_pgamble', 
  'easyACC_mean_pgamble', 
  'easyREJ_mean_pgamble'
);

data_rdm = array(data = NA, dim = c(0, length(column_names_rdm)));
colnames(data_rdm) <-column_names_rdm
data_rdm <- data.frame(mean_pgamble,static_mean_pgamble,dynamic_mean_pgamble,easy_mean_pgamble,diff_mean_pgamble,easyACC_mean_pgamble,easyREJ_mean_pgamble)

#Q:standard error, means, range for gambling behavior for particpants

#Define function
sem <- function(x) sd(x)/sqrt(length(x));

# Calculate M's and SEMs
mean(mean_pgamble) # 0.497775
mean(static_mean_pgamble) # 0.5089402
mean(dynamic_mean_pgamble) # 0.4930427
sem(mean_pgamble) # 0.01143445
sem(static_mean_pgamble) # 0.01492569
sem(dynamic_mean_pgamble) # 0.01449466

mean(easyACC_mean_pgamble) # 0.9343611
mean(easyREJ_mean_pgamble) # 0.06401623
sem(easyACC_mean_pgamble) # 0.009493229
sem(easyREJ_mean_pgamble) # 0.00588866

mean(diff_mean_pgamble) # 0.4863754
sem(diff_mean_pgamble) # 0.02614511

min(mean_pgamble) # 0.2647059
max(mean_pgamble) # 0.8235294

# Q: How did risk-taking compare across the different dynamic trial types?
# e.g. easy accept vs. easy reject vs. difficult
hist(easyACC_mean_pgamble,
     col = rgb(0,1,0,.5), breaks = seq(from = 0, to = 1, by = 0.05), xlim = c(0,1),
     xlab = 'Mean Probability of Risk-Taking', ylab = 'Frequency', 
     main = 'Average Risk-Taking Behavior By Trial Type')
hist(easyREJ_mean_pgamble,
     col = rgb(1,0,0,.5), breaks = seq(from = 0, to = 1, by = 0.05), add = TRUE)
hist(diff_mean_pgamble,
     col = rgb(0,0,1,.5), breaks = seq(from = 0, to = 1, by = 0.05), add = TRUE)
# A: As expected red < blue < green (easy reject < difficult < easy accept), blue is more spread out 


# Q: Can we collapse across easy accept & reject trials based on relative distance of CHOICES from 0.5?
plot(abs(easyACC_mean_pgamble-.5),abs(easyREJ_mean_pgamble-.5),xlim = c(0,.5), ylim = c(0,.5),
     xlab = 'Easy Accept', ylab = 'Easy Reject', 
     main = 'Distance of Observed p(risky) from 0.5 (chance) for EASY trial subtypes',
     pch = 19, col = rgb(0,0,0,.2), cex = 2)
lines(x = c(0,1), y = c(0,1), col = 'blue')

# Statistically test relative difficulty observed in easy ACC vs. easy REJ
t.test(abs(easyACC_mean_pgamble-.5), abs(easyREJ_mean_pgamble-.5), paired = T) # n.s., t(84) = -0.001622718, p = 0.8801

# A: Yes, we can treat all easy trials as similarly easy (whether easy ACC or REJ), not sig different 2/9/24


#### Optimization Function Creation ####

# Function to calculate choice probabilities
choice_probability <- function(parameters, choiceset) {
  # A function to calculate the probability of taking a risky option
  # using a prospect theory model.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  #
  # PSH & AR June 2022
  
  # extract  parameters
  rho = as.double(parameters[1]); # risk attitudes
  mu = as.double(parameters[2]); # choice consistency
  
  # Correct parameter bounds
  if(rho <= 0){
    rho = .Machine$double.eps;
  }
  
  if(mu < 0){
    mu = 0;
  }
  
  # calculate utility of the two options
  utility_risky_option = 0.5 * choiceset$riskyoption1^rho + 
    0.5 * choiceset$riskyoption2^rho;
  utility_safe_option = choiceset$safeoption^rho;
  
  # normalize values using this term
  div <- max(choiceset[,1:3])^rho; # decorrelates rho & mu
  
  # calculate the probability of selecting the risky option
  p = 1/(1+exp(-mu/div*(utility_risky_option - utility_safe_option)));
  
  return(p)
}

# Likelihood function
negLLprospect_cge <- function(parameters,choiceset,choices) {
  # A negative log likelihood function for a prospect-theory estimation.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  # Assumes choices are binary/logical, with 1 = risky, 0 = safe.
  #
  # Peter Sokol-Hessner
  # July 2021
  
  choiceP = choice_probability(parameters, choiceset);
  
  likelihood = choices * choiceP + (1 - choices) * (1-choiceP);
  likelihood[likelihood == 0] = 0.000000000000001; # 1e-15, i.e. 14 zeros followed by a 1
  
  nll <- -sum(log(likelihood));
  return(nll)
}


#### Optimization ####
eps = .Machine$double.eps;
lower_bounds = c(eps, 0); # R, M
upper_bounds = c(2,80); 
number_of_parameters = length(lower_bounds);

# Create placeholders for parameters, errors, NLL (and anything else you want)
number_of_iterations = 200; # 100 or more
estimated_parameters = array(dim = c(number_of_clean_subjects,2));
estimated_parameter_errors = array(dim = c(number_of_clean_subjects,2));
NLLs = array(dim = c(number_of_clean_subjects,1));

clean_data_dm$all_choiceP = NA;

cat('Beginning Optimization\n')

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  print(subj_id)
  
  tmpdata = clean_data_dm[(clean_data_dm$subjectnumber == subj_id) & 
                            (clean_data_dm$static0dynamic1 == 0) & 
                            is.finite(clean_data_dm$choice),]; # defines this person's data
  
  temp_parameters = array(dim = c(number_of_iterations,number_of_parameters));
  temp_hessians = array(dim = c(number_of_iterations,number_of_parameters,number_of_parameters));
  temp_NLLs = array(dim = c(number_of_iterations,1));
  
  choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
  colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
  
  # tic() # start the timer
  
  for(iter in 1:number_of_iterations){
    # Randomly set initial values within supported values
    # using uniformly-distributed values. Many ways to do this!
    
    initial_values = runif(number_of_parameters, min = lower_bounds, max = upper_bounds)
    
    temp_output = optim(initial_values, negLLprospect_cge,
                        choiceset = choiceset,
                        choices = tmpdata$choice,
                        lower = lower_bounds,
                        upper = upper_bounds,
                        method = "L-BFGS-B",
                        hessian = T)
    
    # Store the output we need access to later
    temp_parameters[iter,] = temp_output$par; # parameter values
    temp_hessians[iter,,] = temp_output$hessian; # SEs
    temp_NLLs[iter,] = temp_output$value; # the NLLs
  }
  
  # Compare output; select the best one
  NLLs[subj] = min(temp_NLLs); # the best NLL for this person
  best_ind = which(temp_NLLs == NLLs[subj])[1]; # the index of that NLL
  
  estimated_parameters[subj,] = temp_parameters[best_ind,] # the parameters
  estimated_parameter_errors[subj,] = sqrt(diag(solve(temp_hessians[best_ind,,]))); # the SEs
  
  # Calculating all choice probabilities for this participant, given best-fit parameters
  all_choice_ind = (clean_data_dm$subjectnumber == subj_id) & is.finite(clean_data_dm$choice)
  tmpdata = clean_data_dm[all_choice_ind,]; # defines this person's data
  
  choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
  colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
  
  clean_data_dm$all_choiceP[all_choice_ind] = choice_probability(temp_parameters[best_ind,],choiceset);
}


#### Grid Search ####

### Q: Does optimized analysis match grid search analysis?###

n_rho_values = 200; # SET THIS TO THE DESIRED DEGREE OF FINENESS
n_mu_values = 201; # IBID

rho_values = seq(from = 0.3, to = 2.2, length.out = n_rho_values); # the range of fit-able values
mu_values = seq(from = 7, to = 80, length.out = n_mu_values);

best_rhos = array(dim = c(number_of_clean_subjects,1));
best_mus = array(dim = c(number_of_clean_subjects,1));

cat('Beginning Grid Search\n')

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  print(subj_id)
  #   
  tmpdata = clean_data_dm[(clean_data_dm$subjectnumber == subj_id) & 
                            (clean_data_dm$static0dynamic1 == 0) & 
                            is.finite(clean_data_dm$choice),]; # defines this person's data
  
  choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
  colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
  
  grid_nll_values = array(dim = c(n_rho_values, n_mu_values));
  
  for(r in 1:n_rho_values){
    for(m in 1:n_mu_values){
      grid_nll_values[r,m] = negLLprospect_cge(c(rho_values[r],mu_values[m]), choiceset, tmpdata$choice)
    }
  }
  
  min_nll = min(grid_nll_values); # identify the single best value
  indexes = which(grid_nll_values == min_nll, arr.ind = T); # Get indices for that single best value
  
  best_rhos[subj] = rho_values[indexes[1]]; # what are the corresponding rho & mu values?
  best_mus[subj] = mu_values[indexes[2]];
}

# look at all best rho & mu per participant
grid_bestRho = array(dim = c(number_of_clean_subjects,1));
grid_bestMu = array(dim = c(number_of_clean_subjects,1));
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  grid_bestRho[subj] = rho_values[unique(tmpdata$bestRho)];
  grid_bestMu[subj] = mu_values[unique(tmpdata$bestMu)];
}

# First, check fresh grid search best Rho & Mu against experiment-executed grid search Rho & Mu
# (should be trivial and match!)

if (any((grid_bestRho - best_rhos) != 0)){
  print('MISMATCH!')
}else{
  print('Grid search values match (as expected)')
}

# Grid search replicates (which it should!) (4/11/24)

# Then check estimated parameters vs. grid search parameters
plot(grid_bestRho,estimated_parameters[,1], main = 'RHO', 
     xlab = 'Grid Search Estimate', ylab = 'Optimization estimate', 
     xlim = c(0, 2), ylim = c(0, 2))
lines(c(0, 2), c(0, 2))

plot(grid_bestMu,estimated_parameters[,2], main = 'MU',
     xlab = 'Grid Search Estimate', ylab = 'Optimization estimate',
     xlim = c(0, 100), ylim = c(0, 100))
lines(c(0, 100), c(0, 100))

hist(grid_bestRho - estimated_parameters[,1], xlim = c(-2,2),
     breaks = seq(from = -2, to = 2, by = 0.02), main = 'Difference in Rho Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
hist(grid_bestMu - estimated_parameters[,2], xlim = c(-100,100), 
     breaks = seq(from = -100, to = 100, by = 0.5), main = 'Difference in Mu Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
# This is supposed to look silly! Should cluster around 0
# ... and it does, as of 4/5/24!

t.test(grid_bestRho, estimated_parameters[,1], paired = T) # no sig. diff (rho)... 4/11/24 (t(84) = 1.7804, p = 0.07862)
t.test(grid_bestMu, estimated_parameters[,2], paired = T) # no sig. diff (mu)... 4/11/24 (t(84) = 1.8545, p = 0.06718)

cor.test(grid_bestRho, estimated_parameters[,1]) # both extremely highly correlated. r(83) = 0.9974685, p = 2.2e-16
cor.test(grid_bestMu, estimated_parameters[,2]) # r(83) = 0.9997898, p = 2.2e-16

# A: YES, grid-search values match optimized values very closely.

# Who are our subjects? 
mean_params = colMeans(estimated_parameters);

hist(estimated_parameters[,1], xlim = c(0,2),
     breaks = seq(from = 0, to = 2, by = 0.2), main = '',
     ylab = 'Participants', xlab = 'Rho (risk attitudes)')
lines(x = c(1,1), y = c(0,50), col = 'black', lwd = 2, lty = 'dashed')
lines(x = c(mean_params[1], mean_params[1]), y = c(0,50), col = 'green', lwd = 5, lend = 'butt')
# Seems evenly spread around 1 (risk neutral)

hist(estimated_parameters[,2], xlim = c(0,upper_bounds[2]),
     breaks = seq(from = 0, to = upper_bounds[2], by = 8), main = '',
     ylab = 'Participants', xlab = 'Mu (consistency)')
lines(x = c(mean_params[2], mean_params[2]), y = c(0,50), col = 'orange', lwd = 5, lend = 'butt')
# Seems positively skewed. Around 20-30.

#### Setup for Regressions ####

### Create Continuous difficulty metric ###
clean_data_dm$diff_cont = abs(abs(clean_data_dm$choiceP - 0.5)*2-1); # JUST for the easy/difficult dynamic trials
clean_data_dm$all_diff_cont = abs(abs(clean_data_dm$all_choiceP - 0.5)*2-1); # for ALL trials

clean_data_dm$prev_all_diff_cont = c(NA,clean_data_dm$all_diff_cont[1:(length(clean_data_dm$all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev2_all_diff_cont = c(NA,clean_data_dm$prev_all_diff_cont[1:(length(clean_data_dm$prev_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev2_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev3_all_diff_cont = c(NA,clean_data_dm$prev2_all_diff_cont[1:(length(clean_data_dm$prev2_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev3_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev4_all_diff_cont = c(NA,clean_data_dm$prev3_all_diff_cont[1:(length(clean_data_dm$prev3_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev4_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev5_all_diff_cont = c(NA,clean_data_dm$prev4_all_diff_cont[1:(length(clean_data_dm$prev4_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev5_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev6_all_diff_cont = c(NA,clean_data_dm$prev5_all_diff_cont[1:(length(clean_data_dm$prev5_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev6_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev7_all_diff_cont = c(NA,clean_data_dm$prev6_all_diff_cont[1:(length(clean_data_dm$prev6_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev7_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

clean_data_dm$prev8_all_diff_cont = c(NA,clean_data_dm$prev7_all_diff_cont[1:(length(clean_data_dm$prev7_all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev8_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

# EASY = 0
# DIFFICULT = 1


#### Basic RT analysis ####

# Q:DO RT differ across conditions? Reaction times for easy risky, easy safe, and hard (hard > easy (either))
#mean easy RT 
mean_rt_easy = array(dim = c(number_of_clean_subjects, 1));
mean_rt_diff = array(dim = c(number_of_clean_subjects, 1));
median_rt_easy = array(dim = c(number_of_clean_subjects, 1));
median_rt_diff = array(dim = c(number_of_clean_subjects, 1));
mean_rt_easyACC = array(dim = c(number_of_clean_subjects, 1));
mean_rt_easyREJ = array(dim = c(number_of_clean_subjects, 1));
var_rt_easy = array(dim = c(number_of_clean_subjects, 1));
var_rt_diff = array(dim = c(number_of_clean_subjects, 1));
mean_rt_static = array(dim = c(number_of_clean_subjects, 1));
mean_rt_dynamic = array(dim = c(number_of_clean_subjects, 1));


for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,];
  
  mean_rt_static[subj] = mean(tmpdata$reactiontime[(tmpdata$static0dynamic1 == 0)],na.rm = T); 
  mean_rt_dynamic[subj] = mean(tmpdata$reactiontime[(tmpdata$static0dynamic1 == 1)], na.rm = T);
  
  # Identify just EASY dynamic data
  tmpdataEasyDyn = tmpdata[tmpdata$easyP1difficultN1 == 1,];
  
  # RTs within easy dynamic data
  mean_rt_easy[subj] = mean(tmpdataEasyDyn$reactiontime, na.rm = T)
  median_rt_easy[subj] = median(tmpdataEasyDyn$reactiontime, na.rm = T)
  mean_rt_easyACC[subj] = mean(tmpdataEasyDyn$reactiontime[(tmpdataEasyDyn$choiceP > .5)], na.rm = T);
  mean_rt_easyREJ[subj] = mean(tmpdataEasyDyn$reactiontime[(tmpdataEasyDyn$choiceP < .5)], na.rm = T);
  var_rt_easy[subj] = var(tmpdataEasyDyn$reactiontime, na.rm = T);
  
  # Identify just DIFFICULT dynamic data
  tmpdataDiffDyn = tmpdata[tmpdata$easyP1difficultN1 == -1,];
  
  mean_rt_diff[subj] = mean(tmpdataDiffDyn$reactiontime, na.rm = T)
  median_rt_diff[subj] = median(tmpdataDiffDyn$reactiontime, na.rm = T)
  var_rt_diff[subj] = var(tmpdataDiffDyn$reactiontime, na.rm = T);
  
}


# RTs between easy & difficult
plot(mean_rt_diff, mean_rt_easy,
     main = 'Average RT By Trial Type', xlab = "Mean RT Difficult", ylab = "Mean RT Easy",
     xlim = c(0.75, 2.75), ylim = c(0.75, 2.75))
lines(c(0, 2.75), c(0, 2.75))
points(mean(mean_rt_diff), mean(mean_rt_easy), pch = 16, col = rgb(1, 0, 1, .75), cex = 2.5)

plot(median_rt_diff, median_rt_easy, 
     main = 'Median RT By Trial Type', xlab = "Median RT Difficult", ylab = "Median RT Easy", 
     xlim = c(0.75, 2.75), ylim = c(0.75, 2.75))
lines(c(0, 2.75), c(0, 2.75))
points(mean(median_rt_diff), mean(median_rt_easy), pch = 16, col = rgb(1, 0, 1, .75), cex = 2.5)

# test easy RTs vs. diff. RTs 
rt_mean_test = t.test(mean_rt_easy,mean_rt_diff, paired = T) # VERY significant (t(84) = -10.368, p = 2.2e-16)
rt_mean_test
rt_median_test = t.test(median_rt_easy,median_rt_diff, paired = T) # VERY significant (t(84) = -10.184, p = 2.493e-16)
rt_median_test 
#A: yes, looks like on average rt of difficult decisions was slower than avg rt of easy decisions 4/11/24

# Test for the across-participant variances in RTs by trial type
rt_mean_vartest = var.test(mean_rt_easy,mean_rt_diff); # F(84) = 0.42266, p = 0.0001059
rt_mean_vartest
var(mean_rt_easy)
var(mean_rt_diff)
rt_median_vartest = var.test(median_rt_easy,median_rt_diff); # F(84) = 0.36058, p = 4.987e-06
rt_median_vartest
# A: RTs are more variable across people for diff. than easy trials

yl = ceiling(max(c(max(mean_rt_diff),max(mean_rt_easy)))*10)/10
plot(mean_rt_easy, mean_rt_diff, xlab = 'Easy trials', ylab = 'Difficult trials',
     main = 'Across-Participant Variances in RT',
     sub = sprintf('variance test p = %.03f', var_test_within$p.value), 
     xlim = c(0,yl), ylim = c(0,yl))
lines(c(0,.6), c(0,.6), col = 'black', lty = 'dashed', lwd = 1.5)


# differences between variance of RTs in conditions WITHIN person
var_test_within = t.test(var_rt_easy,var_rt_diff, paired = T); # t(84) = -5.8504, p = 9.154e-08
var_test_within


yl = ceiling(max(c(max(var_rt_diff),max(var_rt_easy)))*10)/10
plot(var_rt_easy, var_rt_diff, xlab = 'Easy trials', ylab = 'Difficult trials',
     main = 'Within-Trial-Type Variances in RT',
     sub = sprintf('paired t-test p = %.03f', var_test_within$p.value), 
     xlim = c(0,yl), ylim = c(0,yl))
lines(c(0,.6), c(0,.6), col = 'black', lty = 'dashed', lwd = 1.5)

# RTs on difficult trials are more variable WITHIN person than their RTs on easy trials


# per person basis of easy RTs vs diff. RTs??
#Q: are easy choices similarly fast across people & are difficult choices similarly slower across people? 
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]; # identify this person's data
  
  # test their easy trials vs. their difficult trials
  diff_stat_result = t.test(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == 1], tmpdata$reactiontime[tmpdata$easyP1difficultN1 == -1]);
  var_stat_results = var.test(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == 1], tmpdata$reactiontime[tmpdata$easyP1difficultN1 == -1]);
  
  hist(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == -1], 
       breaks = seq(from = 0, to = 4, by = .25), col = rgb(1,0,0,0.6), xlim = c(0,4), ylim = c(0,30),
       main = sprintf('Subject %g: t-test p = %.03f; var test p = %.03f', subj_id, diff_stat_result$p.value, var_stat_results$p.value));
  hist(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == 1], 
       breaks = seq(from = 0, to = 4, by = .25), col = rgb(0,0,1,0.6), add = T)
}


# test easy ACC vs. easy REJ RTs (and plot against each other)
# Q: Can we treat easy ACC & REJ RTs as the same kind of thing? 
t.test(mean_rt_easyACC,mean_rt_easyREJ, paired = T); # not sig. diff between easy types 4/25/23 (t(84) = 0.28963, p = 0.7728)
plot(mean_rt_easyACC, mean_rt_easyREJ, main = 'Reaction Times on Easy Trials', 
     xlab = 'Easy ACCEPT trials', ylab = 'Easy REJECT trials', xlim = c(0,4), ylim = c(0,4))
lines(c(0,4), c(0,4))

# A: yes they are very similar & not significantly different, what we want to see. CAN collapse easy REJ and easy ACC as "easy"


#### SUBSEQUENT DIFFICULTY ANALYSIS ####

#Q:Does RT change depending on subsequent trial types? # Something Anna wanted to examine - Underpowered?
#mean RT subsequent #
diff_diff_mean_rt = array(dim = c(number_of_clean_subjects, 1));
easy_easy_mean_rt = array(dim = c(number_of_clean_subjects, 1));
easy_diff_mean_rt = array(dim = c(number_of_clean_subjects, 1));
diff_easy_mean_rt = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  easy_easy_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                        (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
  
  diff_diff_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == -1) & 
                                                        (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  diff_easy_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == 1) & 
                                                        (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  easy_diff_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                        (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
}

# does prev. trial type influence RT on the current trial 
t.test(easy_easy_mean_rt, diff_easy_mean_rt, paired = T); # NOT for easy 4/5/24 (t(84) = 0.72255, p = 0.472)
t.test(diff_diff_mean_rt, easy_diff_mean_rt, paired = T); # NOT for difficult 4/5/24 (t(84) = 1.6342, p = 0.106)
# A: Not at this level.

# Plot the current trial as a function of prev. trial type
plot(easy_easy_mean_rt, diff_easy_mean_rt, xlim = c(0.75,2.2), ylim = c(0.75,2.2),
     main = 'EASY TRIALS', xlab = 'Previous trial was EASY', ylab = 'Previous trial was DIFFICULT'); lines(c(0,3), c(0,3)); # NOT for easy
plot(easy_diff_mean_rt, diff_diff_mean_rt, xlim = c(0.75,2.2), ylim = c(0.75,2.2),
     main = 'DIFFICULT TRIALS', xlab = 'Previous trial was EASY', ylab = 'Previous trial was DIFFICULT'); lines(c(0,3), c(0,3)); # NOT for difficult

t.test(diff_diff_mean_rt, easy_easy_mean_rt, paired = T); # not sig diff 4/5/24 (t(84) = -0.075654, p = 0.9399)
#A: it looks like RT based upon subsequent trials is not sig different at this level


#Q: Does gambling behavior change based upon previous trial difficulty? 
#mean p_gamble subsequent 
diff_diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
diff_easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  diff_diff_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  easy_easy_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
  
  
  easy_diff_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  
  diff_easy_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
}  

t.test(diff_diff_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 2/25/24 (t(84) = 0.054225, p = 0.9569)
t.test(diff_easy_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 2/25/24 (t(84) = -0.69596, p = 0.4884)
t.test(diff_diff_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 2/25/24 (t(84) = 0.15362, p = 0.8783)

#A: it looks like pgamble based upon subsequent trials is not significantly different, difficulty doesn't show effect on p gamble.
# - may be due to not having intermediate pgambles?

### WORKING MEMORY BASIC ANALYSIS ###

cat(sprintf('Out of a total of %i participants, we have O-Span scores for %i, Sym-Span scores for %i, and composite span scores for %i.\n',
              number_of_subjects, 
              sum(is.finite(complexSpanScores$ospanScore)), 
              sum(is.finite(complexSpanScores$symspanScore)), 
              sum(is.finite(complexSpanScores$compositeSpanScore))))
# Out of a total of 88 participants, we have O-Span scores for 73, Sym-Span scores for 74, and composite span scores for 85.
cat(sprintf('%i participants have both scores, %i participants are missing only one score, and %i participants are missing both scores.\n',
            sum(is.finite(complexSpanScores$ospanScore) & is.finite(complexSpanScores$symspanScore)),
            sum(xor(is.finite(complexSpanScores$ospanScore),is.finite(complexSpanScores$symspanScore))),
            number_of_subjects-sum(is.finite(complexSpanScores$compositeSpanScore))))
# 62 participants have both scores, 23 participants are missing only one score, and 3 participants are missing both scores.

# Mean, Median, and Variance of ospan, symspan, and compositespan
mean_ospan = mean(complexSpanScores$ospanScore, na.rm = T)
mean_symspan = mean(complexSpanScores$symspanScore, na.rm = T)
mean_compositespan = mean(complexSpanScores$compositeSpanScore, na.rm = T)

sd_ospan = sd(complexSpanScores$ospanScore, na.rm = T)
sd_symspan = sd(complexSpanScores$symspanScore, na.rm = T)
sd_compositespan = sd(complexSpanScores$compositeSpanScore, na.rm = T)

median_ospan = median(complexSpanScores$ospanScore, na.rm = T)
median_symspan = median(complexSpanScores$symspanScore, na.rm = T)
median_compositespan = median(complexSpanScores$compositeSpanScore, na.rm = T)

variance_ospan = var(complexSpanScores$ospanScore, na.rm = T)
variance_symspan = var(complexSpanScores$symspanScore, na.rm = T)
variance_compositespan = var(complexSpanScores$compositeSpanScore, na.rm = T)

# Include in the processing - Correlation between OSpan and SymSpan
ospanScores = complexSpanScores$ospanScore
symspanScores = complexSpanScores$symspanScore
compositeSpanScores = complexSpanScores$compositeSpanScore

cor.test(ospanScores, symspanScores) # r(60) = 0.3703213, p = 0.00305 (as of 2/25/24)
var.test(ospanScores, symspanScores) # similar variance (F(72) = 0.95278, p = 0.8378 as of 2/25/24)
t.test(ospanScores, symspanScores, paired = T) # t(61) = 0.14979, p = 0.8814 (as of 2/12/24)

# SUMMARY: O-Span & Sym-Span scores are correlated with each other, and not significantly 
# different from one another. They are NOT redundant (i.e., correlation is ~0.4).

plot(ospanScores, symspanScores, 
     pch = 19, col = rgb(.5, .5, .5, .5), 
     xlim = c(0, 1), ylim = c(0, 1), cex = 2.5,
     xlab = 'OSpan Scores', ylab = 'SymSpan Scores', 
     main = 'Complex Span Scores')
lines(x = c(-1, 2), y = c(-1, 2)) # so line extends to edge

capacity_HighP1_lowN1 = (compositeSpanScores > median_compositespan)*2-1;

sum(capacity_HighP1_lowN1 == 1, na.rm = T) # 41
sum(capacity_HighP1_lowN1 == -1, na.rm = T) # 44

# Plot the distribution w/ the median value
hist(compositeSpanScores, breaks = 10, xlab = 'Composite Span Score', main = 'Distribution of Spans');
abline(v = median_compositespan, col = 'red', lwd = 5)


clean_data_dm$capacity_HighP1_lowN1 = NA;

for(s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s];
  clean_data_dm$capacity_HighP1_lowN1[clean_data_dm$subjectnumber == subj_id] = capacity_HighP1_lowN1[s];
}

clean_data_dm$complexspan_demeaned = clean_data_dm$complexspan - mean_compositespan;

plot(sort(compositeSpanScores))
abline(h = median_compositespan, col = 'red', lwd = 2)



#### Regressions ####

# RT on trials regressions
library(lme4)
library(lmerTest)

clean_data_dm$sqrtRT = sqrt(clean_data_dm$reactiontime);

## Model 0: Current RT based on current easy difficult
m0_diffcat = lm(sqrtRT ~ 1 + easyP1difficultN1, data = clean_data_dm); # LM
summary(m0_diffcat) # difficulty predicts RT!

m0_diffcat_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber), data = clean_data_dm); # LMER
summary(m0_diffcat_rfx) # Same with RFX! 

m0_diffcat_dynonly_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber),
                          data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_diffcat_dynonly_rfx) # Same with only dynamic trials

# Takeaway: In all cases, difficult is slower than easy! Use: m0_diffcat_rfx

# use continuous diff metric instead of easy/difficult 
m0_diffcont = lm(sqrtRT ~ 1 + diff_cont , data = clean_data_dm);
summary(m0_diffcont) # matches categorical

m0_diffcont_rfx = lmer(sqrtRT ~ 1 + diff_cont + (1 | subjectnumber), data = clean_data_dm);
summary(m0_diffcont_rfx) # matches categorical

m0_diffcont_dynonly_rfx = lmer(sqrtRT ~ 1 + diff_cont + (1 | subjectnumber),
                               data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_diffcont_dynonly_rfx) # matches categorical

# TAKEAWAY: Nothing new here, matches categorical, as expected (diff_cont is practically categorical!)

m0_alldiffcont = lm(sqrtRT ~ 1 + all_diff_cont, data = clean_data_dm);
summary(m0_alldiffcont) # matches categorical

m0_alldiffcont_rfx = lmer(sqrtRT ~ 1 + all_diff_cont + (1 | subjectnumber), data = clean_data_dm);
summary(m0_alldiffcont_rfx) # matches categorical

# IN ALL CASES, PEOPLE ARE SLOWER ON DIFFICULT TRIALS THAN EASY TRIALS.
# UNAFFECTED BY CATEGORICAL/CONTINUOUS
# UNAFFECTED BY DYNAMIC ONLY VS. ALL TRIALS

# Which model should we use? 
# It's between m0_diffcat_rfx and m0_alldiffcont_rfx
AIC(m0_diffcat_rfx) # -8603.169
AIC(m0_alldiffcont_rfx) # -8783.393 <- BETTER (more negative)

anova(m0_diffcat_rfx,m0_alldiffcont_rfx) # CONFIRMS that all_diff_cont outperforms easyp1difficultn1
# p < 2e-16 (it's reported as '0') for continuous as better than categorical ???

# xval_plot = seq(from = 0, to = 1, by = .1);
# 
# predict_data_m0 = clean_data_dm[0,];
# predict_data_m0[1:20,] = NA;
# predict_data_m0$all_diff_cont[1:10] = xval_plot
# # predict_data_m0$all_diff_cont[11:20] = xval_plot
# 
# predict_output_m0 = predict(m0_alldiffcont_rfx, newdata = predict_data_m0, type = 'response', re.form = NA)^2
# 
# plot(x = xval_plot, y = predict_output_m0[1:20], 
#      type = 'l', lwd = 5, col = 'purple', 
#      main = 'Effect of current difficulty', xlab = 'Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')


# Plot the simple main effect of difficulty
xval_plot = seq(from = 0, to = 1, by = .1);
coef_vals = fixef(m0_alldiffcont_rfx)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["all_diff_cont"])^2, 
     type = 'l', lwd = 5, col = 'purple', 
     main = 'Effect of current difficulty', xlab = 'Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')

# # Alternative Approach using data points and abline function
# plot(x = clean_data_dm$all_diff_cont, y = clean_data_dm$sqrtRT)
# abline(reg = m0_alldiffcont, col = 'red') # regression must be an LM or GLM, not LMER or GLMER



# BIG TAKEAWAY:
# Across categorical and two kinds of continuous difficulty, difficult trials are slower. 
#
# m0_alldiffcont_rfx is best (see AICs)




## Model 1: PREVIOUS DIFFICULTY: Create Shifted versions of difficulty for use in regressions

# input shifted version of desired content
clean_data_dm$easyP1difficultN1_prev = c(0,clean_data_dm$easyP1difficultN1[1:(length(clean_data_dm$easyP1difficultN1)-1)])
# fix the few problematic trials (#1)
clean_data_dm$easyP1difficultN1_prev[clean_data_dm$trialnumber == 1] = 0;
# input shifted version of desired content
clean_data_dm$sqrtRT_prev = c(NA,clean_data_dm$sqrtRT[1:(length(clean_data_dm$sqrtRT)-1)])
# fix the few problematic trials (#1)
clean_data_dm$sqrtRT_prev[clean_data_dm$trialnumber == 1] = NA;


# Does previous difficulty influence subsequent RT? 
# LMs
m1_diffcat_prev = lm(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev, data = clean_data_dm);
summary(m1_diffcat_prev) # slight effect, OPPOSITE to main pattern (p = 0.0466 as of 2/25/24)
#  (if prev. trial easy, slower on current trial .... OR
#   if prev. trial difficult, faster on current trial)

m1_diffcat_prev_intxn = lm(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev, data = clean_data_dm);
summary(m1_diffcat_prev_intxn) # no interaction, same main effect as m1_diffcat_prev

# LMERs, i.e. RFX Versions
m1_diffcat_prev_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev + 
                             (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffcat_prev_rfx) # previous difficulty has strong effect (p = 0.02)
# Same direction as in m1_diffcat_prev

m1_diffcat_prev_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffcat_prev_intxn_rfx) # no interaction, same main effect.

# TAKEAWAY: Previous categorical difficulty has OPPOSITE effect on current RTs as current difficulty.
#    THIS IS DIFFERENT FROM CGT! CGT HAD NO MAIN EFFECT OF PREV. CATEGORICAL DIFFICULTY.

m1_prev_alldiffCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont + 
                                                (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_alldiffCont_intxn_rfx) # Previous CONTINUOUS difficulty is VERY significant (p = 1.2e-7), no interaction w/ current diff
# Sign is negative: the more difficult the prev. trial was, the faster people were on the current trial
# ... facilitory? "giving up"? 

# CAREFUL! These are different models with different #s of datapoints in them. 
# !!!!!    CANNOT DIRECTLY COMPARE AICs     !!!!!
# AIC(m1_prev_alldiffCont_intxn_rfx) # -6376.622 <-- BETTER (more negative)
# AIC(m1_diffcat_prev_intxn_rfx) # -6208.394


xval_plot = seq(from = 0, to = 1, length.out = 10)

predict_data_m1 = clean_data_dm[0,];
predict_data_m1[1:20,] = NA;
predict_data_m1$all_diff_cont[1:10] = xval_plot
predict_data_m1$all_diff_cont[11:20] = xval_plot
predict_data_m1$prev_all_diff_cont[1:10] = 0;
predict_data_m1$prev_all_diff_cont[11:20] = 1;

predict_output_m1 = predict(m1_prev_alldiffCont_intxn_rfx, newdata = predict_data_m1, type = 'response', re.form = NA)^2

# Plot it!
plot(x = xval_plot, y = predict_output_m1[1:10], 
     type = 'l', lwd = 5, col = 'blue', 
     main = 'Effect of current & previous difficulty', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25, 2))
lines(x = xval_plot, y = predict_output_m1[11:20], 
      lwd = 5, col = 'red')

# BLUE = previous trial easy
# RED = previous trial difficult

# How far back does the previous difficulty effect go? Let's look **4 trials back**
m1_prev_alldiffCont_back4_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                       all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                       (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_alldiffCont_back4_intxn_rfx) 
# All 4 are significant. 

m1_prev_alldiffCont_back8_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             prev5_all_diff_cont + prev6_all_diff_cont + prev7_all_diff_cont + prev8_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_alldiffCont_back8_intxn_rfx) 
# Looks like it peters out ~7 trials back. LONG LASTING EFFECTS! 

# Trying out each difficult trial back

only_finite_index = 
  is.finite(
      clean_data_dm$all_diff_cont + 
      clean_data_dm$prev_all_diff_cont + 
      clean_data_dm$prev2_all_diff_cont + 
      clean_data_dm$prev3_all_diff_cont + 
      clean_data_dm$prev4_all_diff_cont + 
      clean_data_dm$prev5_all_diff_cont + 
      clean_data_dm$prev6_all_diff_cont + 
      clean_data_dm$prev7_all_diff_cont + 
      clean_data_dm$prev8_all_diff_cont)


# -1 trial back
m1_prev_alldiffCont_back1_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back1_intxn_rfx) 

# -2 trials back
m1_prev_alldiffCont_back2_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back2_intxn_rfx) 

# -3 trials back
m1_prev_alldiffCont_back3_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back3_intxn_rfx) 

# -4 trials back
m1_prev_alldiffCont_back4_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back4_intxn_rfx) 

# -5 trials back
m1_prev_alldiffCont_back5_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             prev5_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back5_intxn_rfx) 

# -6 trials back
m1_prev_alldiffCont_back6_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             prev5_all_diff_cont + prev6_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back6_intxn_rfx) 

# -7 trials back
m1_prev_alldiffCont_back7_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             prev5_all_diff_cont + prev6_all_diff_cont + prev7_all_diff_cont +
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back7_intxn_rfx) 

# -8 trials back
m1_prev_alldiffCont_back8_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                             all_diff_cont + prev_all_diff_cont + prev2_all_diff_cont + prev3_all_diff_cont + prev4_all_diff_cont + 
                                             prev5_all_diff_cont + prev6_all_diff_cont + prev7_all_diff_cont + prev8_all_diff_cont + 
                                             (1 | subjectnumber), data = clean_data_dm[only_finite_index,]);
summary(m1_prev_alldiffCont_back8_intxn_rfx) 

AIC(m1_prev_alldiffCont_back1_intxn_rfx)
AIC(m1_prev_alldiffCont_back2_intxn_rfx)
AIC(m1_prev_alldiffCont_back3_intxn_rfx)
AIC(m1_prev_alldiffCont_back4_intxn_rfx)
AIC(m1_prev_alldiffCont_back5_intxn_rfx)
AIC(m1_prev_alldiffCont_back6_intxn_rfx)
AIC(m1_prev_alldiffCont_back7_intxn_rfx)
AIC(m1_prev_alldiffCont_back8_intxn_rfx)

diff_trajectory = clean_data_dm$prev_all_diff_cont*-2.5593e-2 + clean_data_dm$prev2_all_diff_cont*-1.323-2 + clean_data_dm$prev3_all_diff_cont*1.499e-2
plot(diff_trajectory[1:170], type = 'l')

## Model 2: What role does high/low cognitive capacity have on CURRENT TRIAL EFFECTS
m2_capacityCatDiff_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1 + 
                                      (1 | subjectnumber), data = clean_data_dm);
summary(m2_capacityCatDiff_intxn_rfx) # Capacity interacts with current easy/difficult CATEGORICALLY
# Sign of interaction indicates... 
#   HIGH capacity people have greater easy/difficult effect
#   LOW capacity people have smaller easy/difficult effect


m2_capacityContDiff_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * capacity_HighP1_lowN1 + 
                                       (1 | subjectnumber), data = clean_data_dm);
summary(m2_capacityContDiff_intxn_rfx)
# SAME PATTERN If you use continuous difficulty instead of categorical difficulty

# effect of difficulty is 0.118 for HIGH CAPACITY
# effect of difficulty is 0.100 for LOW CAPACITY


AIC(m2_capacityCatDiff_intxn_rfx) # AIC: -5874.978
AIC(m2_capacityContDiff_intxn_rfx) # AIC: -6026.223 (CONTINUOUS IS BETTER)


# Model 3: What role does high/low cognitive capacity have on CURRENT AND PREVIOUS TRIAL EFFECTS

m3_prev_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                       easyP1difficultN1 * easyP1difficultN1_prev * capacity_HighP1_lowN1 + 
                                       (1 | subjectnumber), data = clean_data_dm);
summary(m3_prev_capacityCat_intxn_rfx)
# Current difficulty predicts higher RT
# Previous difficulty predicts lower RT
# Current difficulty predicts EVEN HIGHER RT for people with high capacity. 

#Q: separate easy and difficult based upon experienced difficulty
clean_data_dm$easy = as.double(clean_data_dm$easyP1difficultN1 == 1)
clean_data_dm$difficult = as.double(clean_data_dm$easyP1difficultN1 == -1)

m3_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + easy * capacity_HighP1_lowN1 + difficult * capacity_HighP1_lowN1 + 
                                  (1 | subjectnumber), data = clean_data_dm);
summary(m3_capacityCat_intxn_rfx)
# Very significant interaction between difficult and capacity, indicating that the above effect is almost
# entirely due to higher RTs for people with higher capacity on DIFFICULT trials specifically.


# Continuous difficulty (including previous) and categorical capacity
m3_prev_diffCont_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1 + 
                                                (1 | subjectnumber), data = clean_data_dm);
summary(m3_prev_diffCont_capacityCat_intxn_rfx)
# Besides main effects of current and previous difficulty, NO INTERACTIONS between capacity and 
# difficulty (current or previous).



# DON'T COMPARE m3_prev_capacityCat_intxn_rfx AND m3_prev_diffCont_capacityCat_intxn_rfx (HAVE DIFFERENT
# NUMBERS OF TRIALS B/C OF HOW PREVIOUS DIFFICULTY WAS CODED; USED 0'S AT OVERLAP POINTS INSTEAD OF
# NAs AS USED IN CONTINUOUS DIFFICULTY)
# AIC(m3_prev_capacityCat_intxn_rfx)
AIC(m3_prev_diffCont_capacityCat_intxn_rfx) # Be careful when reporting; has fewer datapoints b/c of NAs


# Plot this??
# 
# MODEL OUTPUT
#                                                        Estimate Std. Error         df t value Pr(>|t|)    
#   (Intercept)                                             1.222e+00  1.333e-02  6.778e+01  91.669  < 2e-16 ***
#   all_diff_cont                                           1.085e-01  6.697e-03  9.839e+03  16.204  < 2e-16 ***
#   prev_all_diff_cont                                     -3.647e-02  6.721e-03  9.840e+03  -5.426 5.91e-08 ***
#   capacity_HighP1_lowN1                                  -1.606e-02  1.333e-02  6.778e+01  -1.205    0.233    
#   all_diff_cont:prev_all_diff_cont                        6.487e-03  1.014e-02  9.834e+03   0.640    0.522    
#   all_diff_cont:capacity_HighP1_lowN1                     8.721e-03  6.697e-03  9.839e+03   1.302    0.193    
#   prev_all_diff_cont:capacity_HighP1_lowN1                6.921e-03  6.721e-03  9.840e+03   1.030    0.303    
#   all_diff_cont:prev_all_diff_cont:capacity_HighP1_lowN1  4.349e-05  1.014e-02  9.834e+03   0.004    0.997    
#
# Current difficulty = slower RTs (found previously)
# Prev. difficulty = faster RTs (found previously)
# Curr. & prev. difficulty do NOT interact to influence reaction time. 
# 
# Capacity = no net effect! [contrary to hypotheses]
#
# in CGT, Capacity interacted with CURRENT difficulty to potentiate slowing due to difficulty
# for high capacity people, and attenuate that effect for low capacity people. NOT SO IN CGE!
# 
# in CGT, Capacity had trending interaction with previous difficulty to almost eliminate the effect of prev. difficulty
# for high capacity folks, but potentiate it for low capacity folks. NOT SO IN CGE! 

xval_plot = seq(from = 0, to = 1, length.out = 10)
predict_data_m3_H = clean_data_dm[0,];
predict_data_m3_H[1:20,] = NA;
predict_data_m3_H$all_diff_cont[1:10] = xval_plot
predict_data_m3_H$all_diff_cont[11:20] = xval_plot
predict_data_m3_H$prev_all_diff_cont[1:10] = 0;
predict_data_m3_H$prev_all_diff_cont[11:20] = 1;
predict_data_m3_H$capacity_HighP1_lowN1 = 1;

predict_data_m3_L = predict_data_m3_H;
predict_data_m3_L$capacity_HighP1_lowN1 = -1;

predict_output_m3_H = predict(m3_prev_diffCont_capacityCat_intxn_rfx, newdata = predict_data_m3_H, type = 'response', re.form = NA)^2
predict_output_m3_L = predict(m3_prev_diffCont_capacityCat_intxn_rfx, newdata = predict_data_m3_L, type = 'response', re.form = NA)^2

#HIGH CAPACITY PLOT
# First plot PREV easy & CAPACITY high
plot(x = xval_plot, y = predict_output_m3_H[1:10], 
     type = 'l', lwd = 5, col = 'blue', 
     main = 'Effect of current & previous difficulty: HIGH CAP', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25, 2))
# Second plot PREV diff & CAPACITY high
lines(x = xval_plot, y = predict_output_m3_H[11:20], 
      lwd = 5, col = 'red')

#SEPERATE INTO TWO PLOTS (LOW CAPACITY BELOW)
# Third plot PREV easy & CAPACITY low
plot(x = xval_plot, y = predict_output_m3_L[1:10], 
     type = 'l',lwd = 5, col = 'blue',
     main = 'Effect of current & previous difficulty: LOW CAP', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25,2))
# Fourth (last) plot PREV diff & CAPACITY low
lines(x = xval_plot, y = predict_output_m3_L[11:20], 
      lwd = 5, col = 'red')

# RED = previous trial easy
# BLUE = previous trial difficult


m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont + 
                                                (1 | subjectnumber),
                                                data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == 1,]);
summary(m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx)
# Fixed effects:
#   Estimate Std. Error         df t value Pr(>|t|)    
#   (Intercept)                       1.206e+00  1.750e-02  3.289e+01  68.920  < 2e-16 ***
#   all_diff_cont                     1.172e-01  8.756e-03  4.845e+03  13.387  < 2e-16 ***
#   prev_all_diff_cont               -2.957e-02  8.816e-03  4.845e+03  -3.355 0.000801 ***
#   all_diff_cont:prev_all_diff_cont  6.550e-03  1.346e-02  4.843e+03   0.486 0.626637   

# Contrary to CGT, there *IS* a significant effect of previous difficulty for high capacity folks.

m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx = lmer(sqrtRT ~ 1 + 
                                                        all_diff_cont * prev_all_diff_cont + 
                                                        (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == -1,]);
summary(m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx)
# Fixed effects:
#   Estimate Std. Error         df t value Pr(>|t|)    
#   (Intercept)                       1.238e+00  2.005e-02  3.495e+01  61.757  < 2e-16 ***
#   all_diff_cont                     9.980e-02  1.018e-02  4.995e+03   9.806  < 2e-16 ***
#   prev_all_diff_cont               -4.340e-02  1.018e-02  4.995e+03  -4.261 2.07e-05 ***
#   all_diff_cont:prev_all_diff_cont  6.464e-03  1.519e-02  4.992e+03   0.425     0.67    

# The effect of previous difficulty is STRONGER in low capacity people (just not sig. so)

# THESE FINDINGS TOTALLY PARALLEL THE COMPLEX INTERACTIVE MODEL ABOVE AND BACK UP THE OBSERVATIONS MADE THERE.

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s];
  clean_data_dm$diff_cont[subj_id] = abs(abs(clean_data_dm$choiceP[subj_id] - 0.5)*2-1); # JUST for the easy/difficult dynamic trials
  clean_data_dm$all_diff_cont[subj_id] = abs(abs(clean_data_dm$all_choiceP[subj_id] - 0.5)*2-1); # for ALL trials
  clean_data_dm$capacity_HighP1_lowN1[clean_data_dm$subjectnumber == subj_id] = capacity_HighP1_lowN1[s];
  
  m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx = lmer(sqrtRT ~ 1 + 
                                                          all_diff_cont * prev_all_diff_cont + 
                                                          (1 | subjectnumber),
                                                        data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == 1,]);
  summary(m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx)
  
  m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx = lmer(sqrtRT ~ 1 + 
                                                         all_diff_cont * prev_all_diff_cont + 
                                                         (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == -1,]);
  summary(m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx)
} 

for(s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s];
  clean_data_dm$capacity_HighP1_lowN1[clean_data_dm$subjectnumber == subj_id] = capacity_HighP1_lowN1[s];
}

# Examine best-fitting threshold values
possible_threshold_values = sort(unique(compositeSpanScores))+.000001;
possible_threshold_values = possible_threshold_values[1:(length(possible_threshold_values)-1)];

all_aic_values = array(data = NA, dim = length(possible_threshold_values));

clean_data_dm$capacity_HighP1_lowN1_temp = NA;

for(ind in 1:length(possible_threshold_values)){
  break_val = possible_threshold_values[ind];
  clean_data_dm$capacity_HighP1_lowN1_temp[clean_data_dm$complexspan > break_val] = 1;
  clean_data_dm$capacity_HighP1_lowN1_temp[clean_data_dm$complexspan < break_val] = -1;

  cat(sprintf('This many people are < break_val: %g\n',sum(compositeSpanScores<break_val, na.rm = T)))
  
  if((sum(compositeSpanScores<break_val, na.rm = T) == 1) | (sum(compositeSpanScores>break_val, na.rm = T) == 1)){
    next # don't use any categorizations that create a 'group' with just 1 person
  }
  
  m3_tmp = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_temp + 
                                                  (1 | subjectnumber), data = clean_data_dm, REML = F);
  all_aic_values[ind] = AIC(m3_tmp)
}

best_aic = min(all_aic_values, na.rm = T);
best_threshold = possible_threshold_values[which(all_aic_values == best_aic)];

cat(sprintf('The best fitting model uses a CompositeSpan threshold value of %g.\n', best_threshold))
cat(sprintf('The best AIC obtained with the CompositeSpan was %0.2f\n', best_aic))

plot(sort(compositeSpanScores), xlab = 'Participants', ylab = 'Span')
abline(h = best_threshold, col = 'blue', lwd = 4)
abline(h = median_compositespan, col = 'red', lwd = 4, lty = 'dotted') # median value
legend('topleft', legend = c('Span','Best threshold','Median span'), col = c('black','blue', 'red'), lty = 1)

plot(x = possible_threshold_values, y = all_aic_values, type = 'l', col = 'green', xlab = 'Thresholds', ylab = 'AIC values (lower better)')
abline(v = median_compositespan, col = 'red', lwd = 4, lty = 'dotted')
abline(v = best_threshold, col = 'blue', lwd = 4)

# The best-fitting threshold (just slightly above the median value) is 0.6571439

break_val = best_threshold; # as of 2/25/24, this was 0.6571439

capacity_HighP1_lowN1_Best = (compositeSpanScores[keep_participants] > break_val)*2 - 1;

clean_data_dm$capacity_HighP1_lowN1_best[clean_data_dm$complexspan > break_val] = 1;
clean_data_dm$capacity_HighP1_lowN1_best[clean_data_dm$complexspan < break_val] = -1;

m3_best = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                 (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best)
m3_best_summary = summary(m3_best);
m3_best_meanlik = exp(-m3_best_summary$logLik/nobs(m3_best));
cat(sprintf('The best mean likelihood obtained with the CompositeSpan was %0.4f\n', m3_best_meanlik))

m3_best_nointxn = lmer(sqrtRT ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                 (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_nointxn)


m3_best_HighCap_only = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont + 
                              (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1_best == 1,], REML = F);
summary(m3_best_HighCap_only)

m3_best_LowCap_only = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont + 
                             (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1_best == -1,], REML = F);
summary(m3_best_LowCap_only)


# Re-do easy/difficult regression w/ this split
m3_capacityCat_intxn_rfx_bestcap = lmer(sqrtRT ~ 1 + easy * capacity_HighP1_lowN1_best + 
                                          difficult * capacity_HighP1_lowN1_best + 
                                  (1 | subjectnumber), data = clean_data_dm);
summary(m3_capacityCat_intxn_rfx_bestcap)
# With this "best split", BOTH easy and difficult are different by capacity?
# This is dynamic-ONLY (using easy/difficult as categorical)


m2_best_cap = lmer(sqrtRT ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + 
                  (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m2_best_cap)
xval_plot = seq(from = 0, to = 1, by = .1);
coef_vals = fixef(m2_best_cap)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["all_diff_cont"] + 
                           1*xval_plot*coef_vals["all_diff_cont:capacity_HighP1_lowN1_best"] + 
                           1*coef_vals["capacity_HighP1_lowN1_best"])^2, 
     type = 'l', lwd = 5, col = 'purple4', 
     main = 'Effect of current difficulty', xlab = 'Difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)')
lines(x = xval_plot, y = (coef_vals["(Intercept)"] + xval_plot*coef_vals["all_diff_cont"] + 
                            -1*xval_plot*coef_vals["all_diff_cont:capacity_HighP1_lowN1_best"]+ 
                            -1*coef_vals["capacity_HighP1_lowN1_best"])^2, 
      lwd = 5, col = 'purple1')



# xval_plot = seq(from = 0, to = 1, by = .1); # current difficulty (easy = 0, difficult = 1)
# prev_trial_diff = c(0,1); # easy = 0, difficult = 1
# capacity = c(1, -1); # HIGH = 1, low = -1
# coef_vals = fixef(m3_best)

xval_plot = seq(from = 0, to = 1, length.out = 10)
predict_data_m3_best_H = clean_data_dm[0,];
predict_data_m3_best_H[1:20,] = NA;
predict_data_m3_best_H$all_diff_cont[1:10] = xval_plot
predict_data_m3_best_H$all_diff_cont[11:20] = xval_plot
predict_data_m3_best_H$prev_all_diff_cont[1:10] = 0;
predict_data_m3_best_H$prev_all_diff_cont[11:20] = 1;
predict_data_m3_best_H$capacity_HighP1_lowN1_best = 1;

predict_data_m3_best_L = predict_data_m3_best_H;
predict_data_m3_best_L$capacity_HighP1_lowN1_best = -1;

predict_output_m3_best_H = predict(m3_best, newdata = predict_data_m3_best_H, type = 'response', re.form = NA)^2
predict_output_m3_best_L = predict(m3_best, newdata = predict_data_m3_best_L, type = 'response', re.form = NA)^2


#HIGH CAPACITY PLOT
# First plot PREV easy & CAPACITY high
plot(x = xval_plot, y = predict_output_m3_best_H[1:10], 
     type = 'l', lwd = 5, col = 'blue', 
     main = 'Effect of current & previous difficulty: HIGH CAP', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25, 1.85))
# Second plot PREV diff & CAPACITY high
lines(x = xval_plot, y = predict_output_m3_best_H[11:20], 
      lwd = 5, col = 'red')

#SEPERATE INTO TWO PLOTS (LOW CAPACITY BELOW)
# Third plot PREV easy & CAPACITY low
plot(x = xval_plot, y = predict_output_m3_best_L[1:10], 
     type = 'l',lwd = 5, col = 'blue',
     main = 'Effect of current & previous difficulty: LOW CAP', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25,1.85))
# Fourth (last) plot PREV diff & CAPACITY low
lines(x = xval_plot, y = predict_output_m3_best_L[11:20], 
      lwd = 5, col = 'red')


# Are we better off using O-Span or Sym-Span (vs. Composite Span)?

# Examine best-fitting threshold values: OSPAN
possible_threshold_values_Ospan = sort(unique(ospanScores))+.000001;
possible_threshold_values_Ospan = possible_threshold_values_Ospan[1:(length(possible_threshold_values_Ospan)-1)];

all_aic_values = array(data = NA, dim = length(possible_threshold_values_Ospan));
all_meanLik_values = array(data = NA, dim = length(possible_threshold_values_Ospan));

clean_data_dm$capacity_HighP1_lowN1_Ospan_temp = NA;

for(ind in 1:length(possible_threshold_values_Ospan)){
  break_val = possible_threshold_values_Ospan[ind];
  clean_data_dm$capacity_HighP1_lowN1_Ospan_temp[clean_data_dm$ospan > break_val] = 1;
  clean_data_dm$capacity_HighP1_lowN1_Ospan_temp[clean_data_dm$ospan < break_val] = -1;
  
  cat(sprintf('This many people are < break_val: %g\n',sum(ospanScores<break_val, na.rm = T)))
  
  if((sum(ospanScores<break_val, na.rm = T) == 1) | (sum(ospanScores>break_val, na.rm = T) == 1)){
    next # don't use any categorizations that create a 'group' with just 1 person
  }
  
  m3_tmp = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_Ospan_temp + 
                  (1 | subjectnumber), data = clean_data_dm, REML = F);
  m3_tmp_summ = summary(m3_tmp);
  
  all_aic_values[ind] = AIC(m3_tmp)
  all_meanLik_values[ind] = exp(-m3_tmp_summ$logLik/nobs(m3_tmp))
}

best_Ospan_aic = min(all_aic_values, na.rm = T);
best_Ospan_threshold = possible_threshold_values_Ospan[which(all_aic_values == best_Ospan_aic)];
best_Ospan_meanlik = all_meanLik_values[which(all_aic_values == best_Ospan_aic)];

cat(sprintf('The best fitting model uses an OSpan threshold value of %g.\n', best_Ospan_threshold))
cat(sprintf('The best AIC obtained with the O-Span was %0.2f\n', best_Ospan_aic))
cat(sprintf('The best mean likelihood obtained with the Ospan was %0.4f\n', best_Ospan_meanlik))

# Examine best-fitting threshold values: SYMSPAN
possible_threshold_values_Symspan = sort(unique(symspanScores))+.000001;
possible_threshold_values_Symspan = possible_threshold_values_Symspan[1:(length(possible_threshold_values_Symspan)-1)];

all_aic_values = array(data = NA, dim = length(possible_threshold_values_Symspan));
all_meanLik_values = array(data = NA, dim = length(possible_threshold_values_Symspan));

clean_data_dm$capacity_HighP1_lowN1_Symspan_temp = NA;

for(ind in 1:length(possible_threshold_values_Symspan)){
  break_val = possible_threshold_values_Symspan[ind];
  clean_data_dm$capacity_HighP1_lowN1_Symspan_temp[clean_data_dm$symspan > break_val] = 1;
  clean_data_dm$capacity_HighP1_lowN1_Symspan_temp[clean_data_dm$symspan < break_val] = -1;
  
  cat(sprintf('This many people are < break_val: %g\n',sum(symspanScores<break_val, na.rm = T)))
  
  if((sum(symspanScores<break_val, na.rm = T) == 1) | (sum(symspanScores>break_val, na.rm = T) == 1)){
    next # don't use any categorizations that create a 'group' with just 1 person
  }
  
  m3_tmp = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_Symspan_temp + 
                  (1 | subjectnumber), data = clean_data_dm, REML = F);
  m3_tmp_summ = summary(m3_tmp);

  all_aic_values[ind] = AIC(m3_tmp)
  all_meanLik_values[ind] = exp(-m3_tmp_summ$logLik/nobs(m3_tmp))
}

best_Symspan_aic = min(all_aic_values, na.rm = T);
best_Symspan_threshold = possible_threshold_values_Symspan[which(all_aic_values == best_Symspan_aic)];
best_Symspan_meanlik = all_meanLik_values[which(all_aic_values == best_Symspan_aic)];

cat(sprintf('The best fitting model uses a SymSpan threshold value of %g.\n', best_Symspan_threshold))
cat(sprintf('The best AIC obtained with the SymSpan was %0.2f\n', best_Symspan_aic))
cat(sprintf('The best mean likelihood obtained with the SymSpan was %0.4f\n', best_Symspan_meanlik))


# Which model does best?
# Fraught question: different people & trials in these 3 models.
# (well, the Ospan & Symspan are different; composite span includes both of those, but other people too)
# Mean choice likelihood is best for SymSpan (0.7280), then Composite (0.7222), then OSpan (0.7195). Differences
# are slight, so probably prefer the model that fits more data, i.e. composite.


### Leave One Out Cross Validation ###

# xval_plot = seq(from = 0, to = 1, length.out = 10)
# predict_data_m3_H = clean_data_dm[0,];
# predict_data_m3_H[1:20,] = NA;
# predict_data_m3_H$all_diff_cont[1:10] = xval_plot
# predict_data_m3_H$all_diff_cont[11:20] = xval_plot
# predict_data_m3_H$prev_all_diff_cont[1:10] = 0;
# predict_data_m3_H$prev_all_diff_cont[11:20] = 1;
# predict_data_m3_H$capacity_HighP1_lowN1 = 1;
# 
# predict_data_m3_L = predict_data_m3_H;
# predict_data_m3_L$capacity_HighP1_lowN1 = -1;
# 
# predict_output_m3_H = predict(m3_prev_diffCont_capacityCat_intxn_rfx, newdata = predict_data_m3_H, type = 'response', re.form = NA)^2
# predict_output_m3_L = predict(m3_prev_diffCont_capacityCat_intxn_rfx, newdata = predict_data_m3_L, type = 'response', re.form = NA)^2
# 
# #HIGH CAPACITY PLOT
# # First plot PREV easy & CAPACITY high
# plot(x = xval_plot, y = predict_output_m3_H[1:10], 
#      type = 'l', lwd = 5, col = 'blue', 
#      main = 'Effect of current & previous difficulty: HIGH CAP', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
#      ylim = c(1.25, 2))
# # Second plot PREV diff & CAPACITY high
# lines(x = xval_plot, y = predict_output_m3_H[11:20], 
#       lwd = 5, col = 'red')
# 
# tmpdataDyn = tmpdata$trialnumber[tmpdata$static0dynamic1 == 1];
# tmpdataDynSamp = sample(tmpdataDyn) # use length? 
# 
# trainDynData = tmpdataDynSamp[1:108]
# testDynData = tmpdataDynSamp[109:120]

# All dynamic trials
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  tmpdataDyn = tmpdata[tmpdata$static0dynamic1 == 1,];
  tmpdataDynSamp = sample(tmpdataDyn$trialnumber)
  
  trainDynData = tmpdataDynSamp[1:108]
  testDynData = tmpdataDynSamp[109:120] 
  
  # m1_trainDynData_intxn_rfx = lmer(sqrtRT ~ 1 + 
  #                       trainDynData + 
  #                       (1 | subjectnumber), data = tmpdata);
  # summary(m1_trainDynData_intxn_rfx)
  
}

# All easy trials
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  tmpdataEasy = tmpdata[tmpdata$easyP1difficultN1 == 1,];
  tmpdataEasySamp = sample(tmpdataEasy$trialnumber)
  
  trainEasyData = tmpdataEasySamp[1:54]
  testEasyData = tmpdataEasySamp[55:60]
  
  
}

# All difficult trials
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  tmpdataDiff = tmpdata[tmpdata$easyP1difficultN1 == -1,];
  tmpdataDiffSamp = sample(tmpdataDiff$trialnumber)
  
  trainDiffData = tmpdataDiffSamp[1:54]
  testDiffData = tmpdataDiffSamp[55:60]
  
  
}



### Testing the integration of Survey Data ###  - I think this is where it breaks

# NCS, IUS, SNS, PSS

m3_best_NCS = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * NCS_HighP1_LowN1 + 
                 (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_NCS)
# NCS x SPAN x current difficulty interaction

m3_best_IUS = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * IUS_HighP1_LowN1 + 
                     (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_IUS)
# IUS x Span x current difficulty interaction
# IUS x current difficulty interaction

m3_best_SNS = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * SNS_HighP1_LowN1 + 
                     (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_SNS)
# SNS main effect

m3_best_PSS = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * PSS_HighP1_LowN1 + 
                     (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_PSS)
# PSS x Span x current difficulty interaction 

AIC(m3_best_NCS) # -8782.879
AIC(m3_best_IUS) # -8794.3 <- BEST AIC = IUS categorical
AIC(m3_best_SNS) # -8789.276
AIC(m3_best_PSS) # -8785.113

# NCS, IUS, and PSS all have the same interaction in their regressions - with current difficulty
# and working memory span. These interactions look like they qualify the 2-way interaction between
# current difficulty & working memory span (that's present in these regressions). THAT interaction
# best characterized as a difference in the slope of current difficulty between high and low 
# capacity participants (high cap participants have a steeper slope with current difficulty). So
# these 3-way interactions (+ve for NCS, -ve for IUS & PSS) can be broadly interpreted to indicate
# that that increasing steepness with capacity is WEAKER for people low in need for cognition / 
# high in intolerance of uncertainty / high in chronic stress (conversely, the opposite is true:
# Increasing steepness w/ increasing capacity is STRONGER in people high in need for cognition, 
# low in intolerance of uncertainty / low in chronic stress). 


m3_best_IUS_SNS = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * IUS_HighP1_LowN1 + 
                         all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * SNS_HighP1_LowN1 + 
                     (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_IUS_SNS) # AIC -6459

# We can run this regression, but... it's a lot. Many 2- & 3-way interactions. 
# AIC *is* better (-6459.4)
# 
# Brief summary:
# MAIN EFFECTS
# current difficulty + 
# previous difficulty - 
# SNS score + 
#
# TWO WAY INTERACTIONS:
# current difficulty x capacity (weak, trend) + 
# previous difficulty x capacity + 
# current difficulty x IUS - 
#
# THREE WAY INTERACTION:
# Current difficulty x capacity x IUS - 
# 

m3_best_IUS_SNS_simple = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                                all_diff_cont * prev_all_diff_cont * IUS_HighP1_LowN1 + 
                                all_diff_cont * prev_all_diff_cont * SNS_HighP1_LowN1 + 
                                (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_IUS_SNS_simple) # AIC -6443; worse than mostly-interactive version

m3_best_IUS_SNS_full = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best * IUS_HighP1_LowN1 * SNS_HighP1_LowN1 + 
                                (1 | subjectnumber), data = clean_data_dm, REML = F);
summary(m3_best_IUS_SNS_full) # AIC -6452; worse than mostly-interactive version


# m3_best_summary = summary(m3_best);
# m3_best_meanlik = exp(-m3_best_summary$logLik/nobs(m3_best));
# cat(sprintf('The best mean likelihood obtained with the CompositeSpan was %0.4f\n', m3_best_meanlik))




#### Individual Regressions ####

model_summaries = list()
lm_estimates = array(data = NA, dim = c(number_of_clean_subjects,4)); # 4 estimates
lm_pvalues = array(data = NA, dim = c(number_of_clean_subjects,4)); # 4 p-values

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  indiv_model = lm(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont, 
                   data = tmpdata);
  
  model_summaries[[s]] = summary(indiv_model)
  lm_estimates[s,] = coef(indiv_model);
  lm_pvalues[s,] = summary(indiv_model)$coefficients[,4] 
}

# Columns... 
# 1 = intercept
# 2 = all_diff_cont
# 3 = prev_all_diff_cont
# 4 = all_diff_cont:prev_all_diff_cont

# p-values... expect low numbers for big effects
plot(lm_pvalues[,2], compositeSpanScores[keep_participants]) # current difficulty
  # given big model, mostly expect negative relationship (higher span = lower/more sig. p-value)
  # LOOKS LIKE THAT
plot(lm_pvalues[,3], compositeSpanScores[keep_participants]) # previous difficulty
  # given big model, mostly expect positive relationship (higher span = higher/less sig. p-value)
  # LOOKS LIKE THAT

# Estimates... expect high values for big effects
plot(lm_estimates[,2], compositeSpanScores[keep_participants]) # current difficulty
cor.test(lm_estimates[,2], compositeSpanScores[keep_participants]) # positive w/ p = 0.087 (trend)
  # given big model, mostly expect positive relationship (higher span = larger estimate)
  # LOOKS LIKE THAT
plot(lm_estimates[,3], compositeSpanScores[keep_participants]) # previous difficulty
cor.test(lm_estimates[,3], compositeSpanScores[keep_participants]) # POSITIVE*, w/ p = 0.033    *unexpected!
  # given big model, mostly expect negative relationship (higher span = lower estimate)
  # WITH A FEW EXCEPTIONS, LOOKS LIKE THAT? 

# TAKEAWAY: Unsurprisingly, these individual-level estimates & p-values/etc are noisy. 
# Without the stabilizing effect of a hierarchical approach, these are hard to read. 
# Additionally the magnitude and significance of an estimate are two different things
# and this approach doesn't handle that gracefully. 

# PROBABLY DON'T TAKE SERIOUSLY OR USE CENTRALLY



#### Throwing In The Towel ####

### Explaining lower RTs (faster choices) after difficult trials: 
# Are low-capacity participants "throwing in the towel" after difficult choices, or 
# is their choice process *facilitated*, and thus better? 

# APPROACH:
#   1. Use all_choice_P values (calculated from estimates of rho & mu from static trials) to...
#   2. Calculate the LIKELIHOOD of data on a per-trial basis in dynamic trials, and then...
#   3. Calculate the MEAN LIKELIHOOD of dynamic trials that follow a difficult trial
#      and compare it to the MEAN LIKELIHOOD of dynamic trials that follow an easy trial
#   4. Calculate the difference in MEAN LIKELIHOOD (easy - difficult), and...
#   5. Relate that difference to capacity group and/or continuous capacity.

# 1. is already done. 

# 2. Calculate the likelihood of the choices.

clean_data_dm$all_choice_likelihood = clean_data_dm$choice * clean_data_dm$all_choiceP + (1-clean_data_dm$choice) * (1-clean_data_dm$all_choiceP);

# 3. Calculate the mean likelihood on dynamic trials after diff. vs. easy trials.

mean_choice_lik_prevEasy = array(data = NA, dim = c(number_of_clean_subjects,1));
mean_choice_lik_prevDiff = array(data = NA, dim = c(number_of_clean_subjects,1));

for (s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s]
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  mean_choice_lik_prevEasy[s] = mean(tmpdata$all_choice_likelihood[tmpdata$easyP1difficultN1_prev == 1], na.rm = T); # na.rm b/c of missed trials
  mean_choice_lik_prevDiff[s] = mean(tmpdata$all_choice_likelihood[tmpdata$easyP1difficultN1_prev == -1], na.rm = T);

  # Use this code to run this test ONLY on current difficult trials
  # mean_choice_lik_prevEasy[s] = mean(tmpdata$all_choice_likelihood[(tmpdata$easyP1difficultN1_prev == 1) & (tmpdata$easyP1difficultN1 == -1)], na.rm = T); # na.rm b/c of missed trials
  # mean_choice_lik_prevDiff[s] = mean(tmpdata$all_choice_likelihood[(tmpdata$easyP1difficultN1_prev == -1) & (tmpdata$easyP1difficultN1 == -1)], na.rm = T);

  # Use this code to run this test ONLY on current easy trials
  # mean_choice_lik_prevEasy[s] = mean(tmpdata$all_choice_likelihood[(tmpdata$easyP1difficultN1_prev == 1) & (tmpdata$easyP1difficultN1 == 1)], na.rm = T); # na.rm b/c of missed trials
  # mean_choice_lik_prevDiff[s] = mean(tmpdata$all_choice_likelihood[(tmpdata$easyP1difficultN1_prev == -1) & (tmpdata$easyP1difficultN1 == 1)], na.rm = T);
}

t.test(mean_choice_lik_prevEasy, mean_choice_lik_prevDiff, paired = T) # p = 0.09, 2/25/24
wilcox.test(mean_choice_lik_prevEasy, mean_choice_lik_prevDiff, paired = T) 
# mean choice likelihood is slightly HIGHER after difficult than after easy (0.697 vs. 0.685)

cor.test(mean_choice_lik_prevEasy, mean_choice_lik_prevDiff) # r(59) = 0.33, p = 0.009
cor.test(mean_choice_lik_prevEasy, mean_choice_lik_prevDiff, method = 'spearman') 
# Correlated w/ each other, unsurprisingly.

plot(mean_choice_lik_prevEasy, mean_choice_lik_prevDiff)
lines(x = c(0, 1), y = c(0, 1))

# 4. Calculate the difference in mean choice likelihood as a function of prev. difficulty

mean_choice_lik_relative = mean_choice_lik_prevEasy - mean_choice_lik_prevDiff;
# Positive numbers = Likelihood after easy is HIGHER than after difficult.
# Negative numbers = likelihood after easy is LOWER than after difficult.
#
# We predict more positive numbers for low-capacity folks.

# 5. Relate that difference to capacity group and/or continuous capacity.

plot(mean_choice_lik_relative, compositeSpanScores[keep_participants])
cor.test(mean_choice_lik_relative, compositeSpanScores[keep_participants]) # n.s. (p = 0.27) on 2/25/24
cor.test(mean_choice_lik_relative, compositeSpanScores[keep_participants], method = 'spearman')
# Direction of the (non-sig.) correlation is negative, as expected
# Low capacity folks have a greater gap between their choice likelihood
# after easy vs. difficult (and easy is >> difficult).

t.test(mean_choice_lik_relative[capacity_HighP1_lowN1_Best == 1], mean_choice_lik_relative[capacity_HighP1_lowN1_Best == -1])
wilcox.test(mean_choice_lik_relative[capacity_HighP1_lowN1_Best == 1], mean_choice_lik_relative[capacity_HighP1_lowN1_Best == -1])
# n.s. p = 0.63 on 2/25/24
# High cap. mean difference = -0.017
# Low cap. mean difference = -0.011 (more positive)


# Try a regression-based approach to this whole question?
likmodel_catDiff_catCap = lmer(all_choice_likelihood ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev * capacity_HighP1_lowN1_best + 
                 (1 | subjectnumber), data = clean_data_dm)
summary(likmodel_catDiff_catCap)
# no signs of anything going on in previous difficulty

likmodel_contDiff_catCap = lmer(all_choice_likelihood ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                 (1 | subjectnumber), data = clean_data_dm)
summary(likmodel_contDiff_catCap)
# no signs of anything going on in previous difficulty


# TAKEAWAY: 
# There are no strong signs in peoples' choices that after difficult trials, choice likelihood 
# is relatively lower for low capacity folks than for high capacity folks. That *would* have
# been consistent with 'giving up'. The signs are in the expected direction, but no stats 
# reach significance. 
#
# Note that no stats are instead consistent with *facilitation* after difficult trials (which
# might predict more internally-consistent choices after difficult trials). 

# This analysis likely suffers from too much breaking-into-parts (and any others going down this
# path would suffer more, e.g. is the likelihood lower, on difficult trials only, after difficult
# trials than after easy trials?)

# This analysis is ALSO fundamentally limited by our design - easy and difficult trials are 
# DESIGNED with a particular choice likelihood. That's the literal definition of what makes an
# easy trial easy etc. In particular, difficult trials, where we might expect to see the most
# movement, are designed with likelihoods *right in the middle*, so biases to act in a 
# particular way on those trials (e.g. always gamble; always safe) might be impossible to see
# as *all actions are equally (un)likely*. If anything, this counterintuitively suggests that
# EASY trials would be the place to observe unusual behavior, but we may have again hurt 
# ourselves as easy trials are SO easy as to be obvious, and not requiring much cognitive 
# work at all to decide about. In short, the way to have observed this might have been with
# trials that were in-between easy and difficult.



# Pupillometry Analyses #################

## Plotting Downsampled Pupillometry ####################
### Per-Subject Plots ###########################

baseline_window_width = 500;

bin_increment = 50; # ensure bins increment by multiples of 25ms

decision_start_bins = seq(from = -baseline_window_width, to = 3000, by = bin_increment); 
decision_end_bins = seq(from = -3000, to = baseline_window_width, by = bin_increment); 

decision_start_array = array(data = NA, dim = c(170,length(decision_start_bins)-1))
decision_end_array = array(data = NA, dim = c(170,length(decision_start_bins)-1))

for (s in 1:number_of_subjects){
  if (s %in% keep_participants){ # if they're someone we're keeping
    # find their file...
    tmp_downsampled_fn = dir(pattern = glob2rx(sprintf('cge%03i_et_processed_downsampled*.RData',s)),full.names = T, recursive = T);
    # and load only the most recent downsampled data file
    load(tmp_downsampled_fn[length(tmp_downsampled_fn)])
    downsampled_et_data = as.data.frame(downsampled_et_data);
    
    pdf(sprintf('%s/plots/cge%03i_downsampled_decision_plot.pdf',config$path$data$processed, s),
        width = 5, height = 8)

    par(mfrow = c(2,1)); # Set up the individual-level plot
    # Pre-decision | Decision Start
    # Decision End | ISI | Outcome | ITI
    plot(1, type = "n", xlab = "milliseconds", ylab = "pupil diameter (mm)", main = "Aligned to Decision Window Start",
         xlim = c(-baseline_window_width, 3000), ylim = c(2, 6))
    abline(v = 0, lty = 'dashed')
    p1_coords = par('usr');
    # pre-dec window, up until 3000 ms into the 4000ms response window

    plot(1, type = "n", xlab = "milliseconds", ylab = "pupil diameter (mm)", main = "Aligned to Choice",
         xlim = c(-3000, baseline_window_width), ylim = c(2, 6))
    abline(v = 0, lty = 'dotted')
    p2_coords = par('usr');
            # the last 3000ms of the 4000ms response window, ISI (1000), Otc (1000), and ITI (3000 or 3500ms)

    number_of_trials = length(event_timestamps[,1]);
    
    for (t in 1:number_of_trials){
      # Pre-decision baseline
      indices = (downsampled_et_data$time_data_downsampled >= (event_timestamps$decision_start[t] - baseline_window_width)) & 
        (downsampled_et_data$time_data_downsampled < event_timestamps$decision_start[t])
      pupil_tmp = downsampled_et_data$pupil_data_extend_interp_smooth_mm_downsampled[indices];
      time_tmp = downsampled_et_data$time_data_downsampled[indices] - event_timestamps$decision_start[t];
      par(usr = p1_coords)
      par(mfg = c(1,1)); lines(x = time_tmp, y = pupil_tmp, col = rgb(0,0,0,.05), lwd = 3)
      
      # Put the mean values into the bins
      for (b in 1:(length(decision_start_bins)-1)){
        tmp_bin_mean = mean(pupil_tmp[(time_tmp >= decision_start_bins[b]) & (time_tmp < decision_start_bins[b+1])], na.rm = T);
        if (!is.na(tmp_bin_mean)){
          decision_start_array[t,b] = tmp_bin_mean;
        }
      }

      # Decision (mean)
      indices = (downsampled_et_data$time_data_downsampled >= event_timestamps$decision_start[t]) & 
        (downsampled_et_data$time_data_downsampled < event_timestamps$decision_end[t]);
      pupil_tmp = downsampled_et_data$pupil_data_extend_interp_smooth_mm_downsampled[indices];
      time_tmp = downsampled_et_data$time_data_downsampled[indices] - event_timestamps$decision_start[t];
      par(usr = p1_coords)
      par(mfg = c(1,1)); lines(x = time_tmp, y = pupil_tmp, col = rgb(0,0,0,.05), lwd = 3)
      
      # Put the mean values into the bins
      for (b in 1:(length(decision_start_bins)-1)){
        tmp_bin_mean = mean(pupil_tmp[(time_tmp >= decision_start_bins[b]) & (time_tmp < decision_start_bins[b+1])], na.rm = T);
        if (!is.na(tmp_bin_mean)){
          decision_start_array[t,b] = tmp_bin_mean;
        }
      }
      
      # Decision aligned to CHOICE (mean)
      indices = (downsampled_et_data$time_data_downsampled >= event_timestamps$decision_start[t]) & 
        (downsampled_et_data$time_data_downsampled < event_timestamps$decision_end[t]);
      pupil_tmp = downsampled_et_data$pupil_data_extend_interp_smooth_mm_downsampled[indices];
      time_tmp = downsampled_et_data$time_data_downsampled[indices] - event_timestamps$decision_end[t];
      par(usr = p2_coords)
      par(mfg = c(2,1)); lines(x = time_tmp, y = pupil_tmp, col = rgb(0,0,0,.05), lwd = 3)
      
      # Put the mean values into the bins
      for (b in 1:(length(decision_end_bins)-1)){
        tmp_bin_mean = mean(pupil_tmp[(time_tmp >= decision_end_bins[b]) & (time_tmp < decision_end_bins[b+1])], na.rm = T);
        if (!is.na(tmp_bin_mean)){
          decision_end_array[t,b] = tmp_bin_mean;
        }
      }
      
      
      # Post-decision aligned to CHOICE (mean)
      indices = (downsampled_et_data$time_data_downsampled >= event_timestamps$decision_end[t]) & 
        (downsampled_et_data$time_data_downsampled < (event_timestamps$decision_end[t] + baseline_window_width));
      pupil_tmp = downsampled_et_data$pupil_data_extend_interp_smooth_mm_downsampled[indices];
      time_tmp = downsampled_et_data$time_data_downsampled[indices] - event_timestamps$decision_end[t];
      par(usr = p2_coords)
      par(mfg = c(2,1)); lines(x = time_tmp, y = pupil_tmp, col = rgb(0,0,0,.05), lwd = 3)
      
      # Put the mean values into the bins
      for (b in 1:(length(decision_end_bins)-1)){
        tmp_bin_mean = mean(pupil_tmp[(time_tmp >= decision_end_bins[b]) & (time_tmp < decision_end_bins[b+1])], na.rm = T);
        if (!is.na(tmp_bin_mean)){
          decision_end_array[t,b] = tmp_bin_mean;
        }
      }
    }
    
    par(usr = p1_coords)
    par(mfg = c(1,1)); lines(x = decision_start_bins[1:(length(decision_start_bins)-1)] + bin_increment/2, 
                             y = colMeans(decision_start_array, na.rm = T), col = rgb(1,0,0), lwd = 3)
    
    par(usr = p2_coords)
    par(mfg = c(2,1)); lines(x = decision_end_bins[1:(length(decision_end_bins)-1)] + bin_increment/2, 
                             y = colMeans(decision_end_array, na.rm = T), col = rgb(1,0,0), lwd = 3)
    
    
    dev.off() # complete the plot

  }
}


## Regressions #################

### Using continuous difficulty #################
m0_pupil_decision_cont = lmer(decision_mean ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                        (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_decision_cont)
# Negative effects of current and previous difficulty

m0_pupil_isi_cont = lmer(isi_mean ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                       (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_isi_cont)
# Negative effects of current & previous difficulty

m0_pupil_otc_cont = lmer(outcome_mean ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                           (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_otc_cont)
# Negative effects of current and previous difficulty
# INTERACTION btwn current difficulty & capacity --> higher cap have larger pupil dilation, lower cap have more constriction

m0_pupil_iti_cont = lmer(iti_mean ~ 1 + all_diff_cont * capacity_HighP1_lowN1_best + prev_all_diff_cont * capacity_HighP1_lowN1_best + 
                           (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_iti_cont)
# Negative effects of current and previous difficulty
# Trend INTERACTION btwn current difficulty & capacity (like otc, see above

### Using continuous difficulty #################
m0_pupil_decision_cat = lmer(decision_mean ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1_best + easyP1difficultN1_prev * capacity_HighP1_lowN1_best + 
                                (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_decision_cat)
# trend of previous difficulty (larger on difficult)

m0_pupil_isi_cat = lmer(isi_mean ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1_best + easyP1difficultN1_prev * capacity_HighP1_lowN1_best + 
                           (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_isi_cat)
# current difficulty (larger on easy trials)

m0_pupil_otc_cat = lmer(outcome_mean ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1_best + easyP1difficultN1_prev * capacity_HighP1_lowN1_best + 
                           (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_otc_cat)
# no effects

m0_pupil_iti_cat = lmer(iti_mean ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1_best + easyP1difficultN1_prev * capacity_HighP1_lowN1_best + 
                           (1 | subjectnumber), data = clean_data_dm)
summary(m0_pupil_iti_cat)
# current difficulty (larger on difficult)

# These effects flip-flop and move around! 






################ MOST STUFF BELOW HERE CAN BE IGNORED ################


# Continuous difficulty (including previous) and continuous capacity and categorical capacity
m1_prev_diffCont_capacityCont_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * complexspan_demeaned + 
                                                             all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1 + 
                                                             (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_diffCont_capacityCont_capacityCat_intxn_rfx)





### Using Best Span Overall ###
m1_diffCat_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * complexspan_demeaned + 
                                           (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffCat_capacityCont_intxn_rfx)
# difficulty interacts with span - difficulty's slowing of RTs is potentiated for people with high cap.

m1_prev_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                        easyP1difficultN1 * easyP1difficultN1_prev * complexspan_demeaned + 
                                        (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_capacityCont_intxn_rfx)
# same main effects (curr. difficult -> slower RTs; prev. difficulty -> faster RTs; curr. difficulty effect
# is stronger for high cap. than low cap. folks)

m1_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + easy * complexspan_demeaned + difficult * complexspan_demeaned + 
                                   (1 | subjectnumber), data = clean_data_dm);
summary(m1_capacityCont_intxn_rfx)
# easy is faster (difficult is trendingly slower); No net effect of complex span.
# but: BOTH easy & difficult are slower with complex span, but to diff. degrees?

m1_diffCont_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * complexspan_demeaned + 
                                            (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffCont_capacityCont_intxn_rfx)
# same as observed above; span interacts with current difficulty.

# Continuous difficulty (including previous) and continuous capacity
m1_prev_diffCont_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                 all_diff_cont * prev_all_diff_cont * complexspan_demeaned + 
                                                 (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_diffCont_capacityCont_intxn_rfx)
# Curr. difficulty predicts slower
# Prev. difficulty predicts faster
# Span potentiates current difficulty
# Span *trendingly* eliminates prev. difficulty? 



#### Average RTs by Capacity and Trial Type ####

#look at average RT for different types of controllers 
meanRT_capacity_High <- numeric(number_of_clean_subjects)
meanRT_capacity_Low <- numeric(number_of_clean_subjects)
meanRT_diff_capacity_High <- numeric(number_of_clean_subjects)
meanRT_diff_capacity_Low <- numeric(number_of_clean_subjects)
meanRT_easy_capacity_High <- numeric(number_of_clean_subjects)
meanRT_easy_capacity_Low <- numeric(number_of_clean_subjects)

for (subj in 1:number_of_clean_subjects) {
  subj_id <- keep_participants[subj]
  tmpdata <- clean_data_dm[clean_data_dm$subjectnumber == subj_id, ]
  meanRT_capacity_High[subj] <- mean(tmpdata$reactiontime[tmpdata$capacity_HighP1_lowN1 == 1], na.rm = TRUE)
  meanRT_capacity_Low[subj] <- mean(tmpdata$reactiontime[tmpdata$capacity_HighP1_lowN1 == -1], na.rm = TRUE)
  meanRT_diff_capacity_High[subj] <- mean(tmpdata$reactiontime[(tmpdata$capacity_HighP1_lowN1 == 1) & (tmpdata$easyP1difficultN1 == -1)], na.rm = TRUE)
  meanRT_easy_capacity_High[subj] <- mean(tmpdata$reactiontime[(tmpdata$capacity_HighP1_lowN1 == 1) & (tmpdata$easyP1difficultN1 == 1)], na.rm = TRUE)
  meanRT_diff_capacity_Low[subj] <- mean(tmpdata$reactiontime[(tmpdata$capacity_HighP1_lowN1 == -1) & (tmpdata$easyP1difficultN1 == -1)], na.rm = TRUE)
  meanRT_easy_capacity_Low[subj] <- mean(tmpdata$reactiontime[(tmpdata$capacity_HighP1_lowN1 == -1) & (tmpdata$easyP1difficultN1 == 1)], na.rm = TRUE)
}

mean(meanRT_capacity_Low, na.rm = T)
sd(meanRT_capacity_Low, na.rm = T)

mean(meanRT_capacity_High, na.rm = T)
sd(meanRT_capacity_High, na.rm = T)

t.test(meanRT_capacity_High, meanRT_capacity_Low, na.rm = T)

mean((meanRT_diff_capacity_High), na.rm = T);
sd((meanRT_diff_capacity_High), na.rm = T);
mean((meanRT_easy_capacity_High), na.rm = T);
sd((meanRT_easy_capacity_High), na.rm = T);
mean((meanRT_diff_capacity_Low), na.rm = T);
sd((meanRT_diff_capacity_Low), na.rm = T);
mean((meanRT_easy_capacity_Low), na.rm = T);
sd((meanRT_easy_capacity_Low), na.rm = T);

