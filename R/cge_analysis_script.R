# CGE Data Analysis Script
#
# Script to analyze the data collected in-person for CGE during Fall '23 & Winter '24
# (Control & Gambling & Eyetracking) study.
#

rm(list=ls()); # Clear the workspace

# identify the working directory paths
main_wd = '/Volumes/shlab/Projects/CGT/CGT_study2/';
processeddata_wd = paste0(main_wd,'processeddata_study2/');

#### Loading Data ####
setwd(processeddata_wd);

# Load Decision-Making Data
fn = dir(pattern = glob2rx('cgt_processed_decisionmaking*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
data_dm = read.csv(fn[number_of_files]) # decision-making data

# Load Working Memory Data
fn = dir(pattern = glob2rx('cgt_processed_workingmemory*.csv'),full.names = T);
number_of_files = length(fn) # ASSUMES YOU WANT THE MOST-RECENT PROCESSED DATA
data_wm = read.csv(fn[number_of_files]) # working memory data 

number_of_subjects = length(unique(data_dm$subjectnumber));

#### Data Quality Checks & Exclusions ####

# Exclude on the basis of DM task performance
# (using... check trials, RTs, choices)

# EXCLUSION: Check Trials
check_trial_failure = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  check_trial_index = which(tmpdata$ischecktrial==1);
  correct_answers = (0.5 * tmpdata$riskyopt1[check_trial_index] +
                       0.5 * tmpdata$riskyopt2[check_trial_index]) > tmpdata$safe[check_trial_index];
  check_trial_failure[subj] = length(which(!tmpdata$choice[check_trial_index] == correct_answers))/length(check_trial_index);
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green', 
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('All Subjects; Subj ', subj),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
}

check_trial_criterion = 0.1; # The maximum percent of check trials that can be missed
# (there were 10 check trials)
# chance is 0.5, perfect is 0.0.

keep_check_trial = check_trial_failure <= check_trial_criterion;

# EXCLUSION: RTs

mean_rts = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  mean_rts[subj] = mean(tmpdata$reactiontime, na.rm = T)
}

keep_dm_rt = mean_rts > 0.85;

mean_rts[keep_dm_rt]
hist(mean_rts[keep_dm_rt]) # histogram of mean rts
mean(mean_rts[keep_dm_rt]) # new mean rt 1.40 seconds


#### Create clean data frames ####

keep_participants = which(keep_check_trial & keep_dm_rt);

# Create clean data frames for data!
clean_data_dm = data_dm[data_dm$subjectnumber %in% keep_participants,]
clean_data_wm = data_wm[data_wm$subjectnumber %in% keep_participants,]

number_of_clean_subjects = length(keep_participants);


#### BASIC DATA ANALYSIS ####

# (Separately for DM & WM data)
# Descriptives & simple averages of task performance

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
mean(mean_pgamble)
mean(static_mean_pgamble)
mean(dynamic_mean_pgamble)
sem(mean_pgamble)
sem(static_mean_pgamble)
sem(dynamic_mean_pgamble)

mean(easyACC_mean_pgamble)
mean(easyREJ_mean_pgamble)
sem(easyACC_mean_pgamble)
sem(easyREJ_mean_pgamble)

mean(diff_mean_pgamble)
sem(diff_mean_pgamble)

min(mean_pgamble)
max(mean_pgamble)

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
# A: As expected red < blue < green (easy reject < difficult < easy acc), blue is more spread out 


# Q: Can we collapse across easy accept & reject trials based on relative distance of CHOICES from 0.5?
plot(abs(easyACC_mean_pgamble-.5),abs(easyREJ_mean_pgamble-.5),xlim = c(0,.5), ylim = c(0,.5),
     xlab = 'Easy Accept', ylab = 'Easy Reject', 
     main = 'Distance of Observed p(risky) from 0.5 (chance) for EASY trial subtypes',
     pch = 19, col = rgb(0,0,0,.2), cex = 2)
lines(x = c(0,1), y = c(0,1), col = 'blue')

# Statistically test relative difficulty observed in easy ACC vs. easy REJ
t.test(abs(easyACC_mean_pgamble-.5), abs(easyREJ_mean_pgamble-.5), paired = T)

# A: Yes, we can treat all easy trials as similarly easy (whether easy ACC or REJ), not sig different 3/7/23


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
negLLprospect_cgt <- function(parameters,choiceset,choices) {
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
    
    temp_output = optim(initial_values, negLLprospect_cgt,
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
      grid_nll_values[r,m] = negLLprospect_cgt(c(rho_values[r],mu_values[m]), choiceset, tmpdata$choice)
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

# Grid search replicates (which it should!)

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
     breaks = seq(from = -2, to = 2, by = 0.05), main = 'Difference in Rho Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
hist(grid_bestMu - estimated_parameters[,2], xlim = c(-100,100), 
     breaks = seq(from = -100, to = 100, by = 1), main = 'Difference in Mu Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
# This is supposed to look silly! Should cluster around 0
# ... and it does, as of 3/7/23!

t.test(grid_bestRho, estimated_parameters[,1], paired = T) # no sig. diff (rho)... 4/2/23
t.test(grid_bestMu, estimated_parameters[,2], paired = T) # no sig. diff (mu)... 4/2/23

cor.test(grid_bestRho, estimated_parameters[,1]) # both extremely highly correlated. 
cor.test(grid_bestMu, estimated_parameters[,2])

# A: YES, grid-search values match optimized values very closely.


#### Setup for Regressions ####

### Create Continuous difficulty metric ###
clean_data_dm$diff_cont = abs(abs(clean_data_dm$choiceP - 0.5)*2-1); # JUST for the easy/difficult dynamic trials
clean_data_dm$all_diff_cont = abs(abs(clean_data_dm$all_choiceP - 0.5)*2-1); # for ALL trials

clean_data_dm$prev_all_diff_cont = c(NA,clean_data_dm$all_diff_cont[1:(length(clean_data_dm$all_diff_cont)-1)]) # for ALL trials
clean_data_dm$prev_all_diff_cont[clean_data_dm$trialnumber == 1] = NA;

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
plot(mean_rt_diff, mean_rt_easy, main = 'Average RT By Trial Type', xlab = "Mean RT Difficult", ylab = "Mean RT Easy", xlim = c(0.75, 2.75), ylim = c(0.75, 2.75))
lines(c(0, 2.75), c(0, 2.75))

plot(median_rt_diff, median_rt_easy, main = 'Median RT By Trial Type', xlab = "Median RT Difficult", ylab = "Median RT Easy", xlim = c(0.75, 2.75), ylim = c(0.75, 2.75))
lines(c(0, 2.75), c(0, 2.75))

# test easy RTs vs. diff. RTs 
rt_mean_test = t.test(mean_rt_easy,mean_rt_diff, paired = T); # VERY significant
rt_median_test = t.test(median_rt_easy,median_rt_diff, paired = T); # VERY significant
#A: yes, looks like on average rt of difficult decisions was slower than avg rt of easy decisions 4/2/23

# Test for the across-participant variances in RTs by trial type
rt_mean_vartest = var.test(mean_rt_easy,mean_rt_diff); # p = 0.03856
rt_median_vartest = var.test(median_rt_easy,median_rt_diff); # p = 0.005846
# A:RTs more variable across people for diff. than easy trials


# differences between variance of RTs in conditions WITHIN person
var_test_within = t.test(var_rt_easy,var_rt_diff, paired = T);

plot(var_rt_easy, var_rt_diff, xlab = 'Easy trials', ylab = 'Difficult trials',
     main = 'Within-Trial-Type Variances in RT',
     sub = sprintf('paired t-test p = %.03f', var_test_within$p.value), 
     xlim = c(0,.6), ylim = c(0,.6))
#points(var_rt_easy[tmpdata$easyP1difficultN1 == 1], var_rt_diff[tmpdata$easyP1difficultN1 == 1], col = 'green')
#points(var_rt_easy[tmpdata$easyP1difficultN1 == -1], var_rt_diff[tmpdata$easyP1difficultN1 == -1], col = 'red')
lines(c(0,.6), c(0,.6), col = 'green', lwd = 1.5)

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
t.test(mean_rt_easyACC,mean_rt_easyREJ, paired = T); #not sig. diff between easy types 3/7/23
plot(mean_rt_easyACC, mean_rt_easyREJ, main = 'Reaction Times on Easy Trials', 
     xlab = 'Easy ACCEPT trials', ylab = 'Easy REJECT trials', xlim = c(0,4), ylim = c(0,4))
lines(c(0,4), c(0,4))

# A: yes they are very similar & not significantly different, what we want to see. CAN collapse easy REJ and easy ACC as "easy"


#### SUBSEQUENT DIFFICULTY ANALYSIS ####

#Q:Does RT change depending on subsequent trial types? 
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
t.test(easy_easy_mean_rt, diff_easy_mean_rt, paired = T); # NOT for easy 4/2/23
t.test(diff_diff_mean_rt, easy_diff_mean_rt, paired = T); # NOT for difficult 4/2/23
# A: Not at this level.

# Plot the current trial as a function of prev. trial type
plot(easy_easy_mean_rt, diff_easy_mean_rt, xlim = c(0.75,2.2), ylim = c(0.75,2.2),
     main = 'EASY TRIALS', xlab = 'Previous trial was EASY', ylab = 'Previous trial was DIFFICULT'); lines(c(0,3), c(0,3)); # NOT for easy
plot(easy_diff_mean_rt, diff_diff_mean_rt, xlim = c(0.75,2.2), ylim = c(0.75,2.2),
     main = 'DIFFICULT TRIALS', xlab = 'Previous trial was EASY', ylab = 'Previous trial was DIFFICULT'); lines(c(0,3), c(0,3)); # NOT for difficult

t.test(diff_diff_mean_rt, easy_easy_mean_rt, paired = T); # not sig diff 4/2/23
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

t.test(diff_diff_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 4/2/23
t.test(diff_easy_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 4/2/23
t.test(diff_diff_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 4/2/23

#A: it looks like pgamble based upon subsequent trials is not significantly differnt, difficulty doesnt show effect on p gamble.



#### WM Task Analysis ####

## TOTAL NUMBER FS & BS Correct (FS & BS)
FS_correct = array(dim = c(number_of_clean_subjects,1));
BS_correct = array(dim = c(number_of_clean_subjects,1));

for (subj in 1:number_of_clean_subjects) {
  subj_id = keep_participants[subj]
  tmpdata = data_wm[data_wm$subjectnumber == subj_id, ]
  # defines this person's data
  FS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 1], na.rm =
                           T)
  
  BS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 0], na.rm =
                           T)
}
## Q:is there a statistically sig difference between number of FS and BS #correct/14? 
t.test(FS_correct, BS_correct, paired = T);
#A: not significant diff (3/7/23), suggestive that overall number of trials correct on either fs or bs is similar.
#total number correct doesnt really tell us anything... exlcude from resutls manuscript! 

# FS & BS max number_digits/length when correct (BEST SPAN)
#Q: is there a difference in max number of digits correct in FS vs BS (comparing fs max digit length correct to bs)
best_span_FS = array(dim = c(number_of_clean_subjects,1));
best_span_BS = array(dim = c(number_of_clean_subjects,1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_wm[data_wm$subjectnumber == subj_id,]
  best_span_FS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);
  best_span_BS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 0) & (tmpdata$correct == 1)], na.rm = T);
}

t.test(best_span_FS, best_span_BS, paired = T);
#A: yes, significant difference between max digit number/length FS correct compared to BS correct (4/2/23)!Suggestive that people have different capcities FS and BS

cor.test(best_span_BS,best_span_FS)
#A: yes, very correlated (r = 0.71, p = 7.9e-9)! 
plot(best_span_BS, best_span_FS, 
     pch = 19, col = rgb(.5, .5, .5, .3), 
     xlim = c(0, 12.5), ylim = c(0, 12.5), cex = 2.5,
     xlab = 'Best Forwards Span', ylab = 'Best Backwards Span', 
     main = 'Forward vs Backwards Capacity')
lines(x = c(0, 12), y = c(0, 12))

# Collapse spans into a single span measure
best_span_overall = rowMeans(cbind(best_span_FS,best_span_BS))

# COG CONTROL REGRESSION & RT- use digit span info to account for capacity... #help says there are variablelengths!! 
#must use median split
#create median split values:
medianSpan = median(best_span_overall);
capacity_HighP1_lowN1 = (best_span_overall > medianSpan)*2-1;

clean_data_dm$capacity_HighP1_lowN1 = NA;
clean_data_dm$best_span_overall = NA;

for(s in 1:number_of_clean_subjects){
  subj_id = keep_participants[s];
  clean_data_dm$capacity_HighP1_lowN1[clean_data_dm$subjectnumber == subj_id] = capacity_HighP1_lowN1[s];
  clean_data_dm$best_span_overall[clean_data_dm$subjectnumber == subj_id] = best_span_overall[s];
}

clean_data_dm$best_span_overall_original = clean_data_dm$best_span_overall;
clean_data_dm$best_span_overall = clean_data_dm$best_span_overall - mean(clean_data_dm$best_span_overall)

# Two options for visualizing Span.
hist(best_span_overall, breaks = seq(from = 4.25, to = 11.75, by = .5))
abline(v = medianSpan, col = 'red', lwd = 4)

plot(sort(best_span_overall))
abline(h = medianSpan, col = 'red', lwd = 4)


mean((best_span_FS < median(best_span_FS)) == (best_span_BS < median(best_span_BS)))
# median splits on only forward span & on only backward span agree about categorization 86% of the time - GOOD!



#### Regressions ####

# RT on trials regressions
library(lme4)
library(lmerTest)

clean_data_dm$sqrtRT = sqrt(clean_data_dm$reactiontime);

## Model 0: Current RT based on current easy difficult
m0_diffcat = lm(sqrtRT ~ 1 + easyP1difficultN1, data = clean_data_dm); # LM
summary(m0_diffcat)

m0_diffcat_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber), data = clean_data_dm); # LMER
summary(m0_diffcat_rfx)

m0_diffcat_dynonly_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber),
                          data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_diffcat_dynonly_rfx)

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

# Which model should we use? 
# It's between m0_diffcat_rfx and m0_alldiffcont_rfx
AIC(m0_diffcat_rfx) # -4898.179
AIC(m0_alldiffcont_rfx) # -4924.883 <- BETTER (more negative)

anova(m0_diffcat_rfx,m0_alldiffcont_rfx) # CONFIRMS that all_diff_cont outperforms easyp1difficuln1

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
# m0_alldiffcont_rfx is best (AIC: -4924.883; AIC(m0_diffcat_rfx) is -4898.179)




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
summary(m1_diffcat_prev) # no effect

m1_diffcat_prev_intxn = lm(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev, data = clean_data_dm);
summary(m1_diffcat_prev_intxn) # no effect

# LMERs, i.e. RFX Versions
m1_diffcat_prev_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev + 
                             (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffcat_prev_rfx) # no effect

m1_diffcat_prev_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffcat_prev_intxn_rfx) # no effect

# TAKEAWAY: Previous categorical difficulty has no effect on subsequent RTs

m1_prev_alldiffCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont + 
                                                (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_alldiffCont_intxn_rfx) # Previous CONTINUOUS difficulty is significant (p < 0.03), no interaction w/ current diff
# Sign is negative: the more difficult the prev. trial was, the faster people were on the current trial
# ... facilitatory? 
#
# 
# Thinking this through... restricting the above RFX regression to JUST static or JUST dynamic data does not yield a significant
# effect of previous difficulty (static: -0.003, p = .86; dynamic: 0.01, p = 0.24). Both alternative regressions return, as 
# expected, positive effects of current difficulty on reaction time. 

AIC(m1_prev_alldiffCont_intxn_rfx) # -4931.999
AIC(m1_diffcat_prev_intxn_rfx) # -4875.277

# Note that accounting for previous difficulty does outperform a model that does not (i.e. m0_alldiffcont_rfx, which had AIC 
# of -4924.883)!


# Categorically, there is no apparent effect of PREVIOUS difficulty on subsequent choices. 
# HOWEVER, using continuous difficulty (including all trials, static & dynamic), we find a small effect of 
# previous (continuous) difficulty on subsequent RTs. It's facilitatory! 

# Plot it!
xval_plot = seq(from = 0, to = 1, by = .1);
prev_trial_diff = c(0,1);
coef_vals = fixef(m1_prev_alldiffCont_intxn_rfx)

plot(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                           xval_plot*coef_vals["all_diff_cont"] + 
                           prev_trial_diff[1]*coef_vals["prev_all_diff_cont"])^2, 
     type = 'l', lwd = 5, col = 'blue', 
     main = 'Effect of current & previous difficulty', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25, 1.5))
lines(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                            xval_plot*coef_vals["all_diff_cont"] + 
                            prev_trial_diff[2]*coef_vals["prev_all_diff_cont"])^2, 
      lwd = 5, col = 'red')
# RED = previous trial difficult
# BLUE = previous trial easy




## Model 2: What role does high/low cognitive capacity have on CURRENT TRIAL EFFECTS
m2_capacityCatDiff_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1 + 
                                      (1 | subjectnumber), data = clean_data_dm);
summary(m2_capacityCatDiff_intxn_rfx)
(1.183 + 1*-0.03029 + 1*0.01499 + 1*1*-0.006186)^2 # easy, high cap
(1.183 + -1*-0.03029 + 1*0.01499 + -1*1*-0.006186)^2 # diff, high cap

(1.183 + 1*-0.03029 + -1*0.01499 + 1*-1*-0.006186)^2 # easy, low cap
(1.183 + -1*-0.03029 + -1*0.01499 + -1*-1*-0.006186)^2 # diff, low cap


m2_capacityContDiff_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * capacity_HighP1_lowN1 + 
                                       (1 | subjectnumber), data = clean_data_dm);
summary(m2_capacityContDiff_intxn_rfx)
# SAME PATTERN If you use continuous difficulty instead of categorical difficulty

AIC(m2_capacityCatDiff_intxn_rfx) # AIC: -4885.503
AIC(m2_capacityContDiff_intxn_rfx) # AIC: -4914.515 (BETTER)


# Model 3: What role does high/low cognitive capacity have on CURRENT AND PREVIOUS TRIAL EFFECTS

m3_prev_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                       easyP1difficultN1 * easyP1difficultN1_prev * capacity_HighP1_lowN1 + 
                                       (1 | subjectnumber), data = clean_data_dm);
summary(m3_prev_capacityCat_intxn_rfx)
# No effect of previous difficulty.
# Current difficulty predicts higher RT
# Current difficulty predicts EVEN HIGHER RT for people with high capacity. 

#Q: separate easy and difficult based upon experienced difficulty
clean_data_dm$easy = as.double(clean_data_dm$easyP1difficultN1 == 1)
clean_data_dm$difficult = as.double(clean_data_dm$easyP1difficultN1 == -1)

m3_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + easy * capacity_HighP1_lowN1 + difficult * capacity_HighP1_lowN1 + 
                                  (1 | subjectnumber), data = clean_data_dm);
summary(m3_capacityCat_intxn_rfx)
# Trend interaction between difficult and capacity, suggesting that the above effect is due to 
# higher RTs for people with higher capacity on DIFFICULT trials specifically.


# Continuous difficulty (including previous) and categorical capacity
m3_prev_diffCont_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1 + 
                                                (1 | subjectnumber), data = clean_data_dm);
summary(m3_prev_diffCont_capacityCat_intxn_rfx)


# DON'T COMPARE m3_prev_capacityCat_intxn_rfx AND m3_prev_diffCont_capacityCat_intxn_rfx (HAVE DIFFERENT
# NUMBERS OF TRIALS B/C OF HOW PREVIOUS DIFFICULTY WAS CODED; USED 0'S AT OVERLAP POINTS INSTEAD OF
# NAs AS USED IN CONTINUOUS DIFFICULTY)
# AIC(m3_prev_capacityCat_intxn_rfx)
AIC(m3_prev_diffCont_capacityCat_intxn_rfx) # Be careful when reporting; has fewer datapoints b/c of NAs


# Plot this??
# 
# MODEL OUTPUT
# Estimate Std. Error         df t value Pr(>|t|)    
# (Intercept)                                               1.156e+00  1.771e-02  5.594e+01  65.293  < 2e-16 ***
#   all_diff_cont                                           6.818e-02  7.912e-03  8.307e+03   8.617  < 2e-16 ***
#   prev_all_diff_cont                                     -1.946e-02  7.932e-03  8.307e+03  -2.453  0.01418 *  
#   capacity_HighP1_lowN1                                   1.383e-03  1.771e-02  5.594e+01   0.078  0.93802    
# all_diff_cont:prev_all_diff_cont                          2.624e-03  1.170e-02  8.305e+03   0.224  0.82253    
# all_diff_cont:capacity_HighP1_lowN1                       2.375e-02  7.912e-03  8.307e+03   3.002  0.00269 ** 
#   prev_all_diff_cont:capacity_HighP1_lowN1                1.387e-02  7.932e-03  8.307e+03   1.749  0.08036 .  
# all_diff_cont:prev_all_diff_cont:capacity_HighP1_lowN1   -1.810e-02  1.170e-02  8.305e+03  -1.547  0.12193    
#
# Current difficulty = slower RTs (found previously)
# Prev. difficulty = faster RTs (found previously)
# Curr. & prev. difficulty do NOT interact to influence reaction time. 
# 
# Capacity = no net effect! [contrary to hypotheses]
#
# Capacity does interact with CURRENT difficulty to potentiate slowing due to difficulty for high capacity 
# people, and attenuate that effect for low capacity people.
# 
# Capacity has trending interaction with previous difficulty to almost eliminate the effect of prev. difficulty
# for high capacity folks, but potentiate it for low capacity folks. 


xval_plot = seq(from = 0, to = 1, by = .1); # current difficulty (easy = 0, difficult = 1)
prev_trial_diff = c(0,1); # easy = 0, difficult = 1
capacity = c(1, -1); # HIGH = 1, low = -1
coef_vals = fixef(m3_prev_diffCont_capacityCat_intxn_rfx)

#HIGH CAPACITY PLOT
# First plot PREV easy & CAPACITY high
plot(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                           xval_plot*coef_vals["all_diff_cont"] + 
                           prev_trial_diff[1]*coef_vals["prev_all_diff_cont"] + 
                           xval_plot*capacity[1]* coef_vals["all_diff_cont:capacity_HighP1_lowN1"] + 
                           prev_trial_diff[1]*capacity[1]*coef_vals["prev_all_diff_cont:capacity_HighP1_lowN1"])^2, 
     type = 'l', lwd = 5, col = 'red', 
     main = 'Effect of current & previous difficulty', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25, 1.575))
# Second plot PREV diff & CAPACITY high
lines(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                            xval_plot*coef_vals["all_diff_cont"] + 
                            prev_trial_diff[2]*coef_vals["prev_all_diff_cont"] + 
                            xval_plot*capacity[1]* coef_vals["all_diff_cont:capacity_HighP1_lowN1"] + 
                            prev_trial_diff[2]*capacity[1]*coef_vals["prev_all_diff_cont:capacity_HighP1_lowN1"])^2, 
      lwd = 5, col = 'blue')

#SEPERATE INTO TWO PLOTS (LOW CAPACITY BELOW)
# Third plot PREV easy & CAPACITY low
plot(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                            xval_plot*coef_vals["all_diff_cont"] + 
                            prev_trial_diff[1]*coef_vals["prev_all_diff_cont"] + 
                            xval_plot*capacity[2]* coef_vals["all_diff_cont:capacity_HighP1_lowN1"] + 
                            prev_trial_diff[1]*capacity[2]*coef_vals["prev_all_diff_cont:capacity_HighP1_lowN1"])^2, 
     type = 'l',lwd = 5, col = 'red',
     main = 'Effect of current & previvous difficulty', xlab = 'Current difficulty (0 = easy, 1 = difficult)', ylab = 'Reaction Time (seconds)',
     ylim = c(1.25,1.575))
# Fourth (last) plot PREV diff & CAPACITY low
lines(x = xval_plot, y = (coef_vals["(Intercept)"] + 
                            xval_plot*coef_vals["all_diff_cont"] + 
                            prev_trial_diff[2]*coef_vals["prev_all_diff_cont"] + 
                            xval_plot*capacity[2]* coef_vals["all_diff_cont:capacity_HighP1_lowN1"] + 
                            prev_trial_diff[2]*capacity[2]*coef_vals["prev_all_diff_cont:capacity_HighP1_lowN1"])^2, 
      lwd = 5, col = 'blue')

# RED = previous trial easy
# BLUE = previous trial difficult


m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx = lmer(sqrtRT ~ 1 + 
                                                all_diff_cont * prev_all_diff_cont + 
                                                (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == 1,]);
summary(m3_prev_diffCont_capacityCat_intxn_HIGHONLYrfx)
# Fixed effects:
#                                       Estimate Std. Error         df t value Pr(>|t|)    
#   (Intercept)                       1.158e+00  2.802e-02  2.675e+01  41.318   <2e-16 ***
#   all_diff_cont                     9.199e-02  1.105e-02  4.129e+03   8.326   <2e-16 ***
#   prev_all_diff_cont               -5.525e-03  1.109e-02  4.129e+03  -0.498    0.619    
#   all_diff_cont:prev_all_diff_cont -1.551e-02  1.657e-02  4.128e+03  -0.936    0.349    

m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx = lmer(sqrtRT ~ 1 + 
                                                        all_diff_cont * prev_all_diff_cont + 
                                                        (1 | subjectnumber), data = clean_data_dm[clean_data_dm$capacity_HighP1_lowN1 == -1,]);
summary(m3_prev_diffCont_capacityCat_intxn_LOWONLYrfx)
# Fixed effects:
#                                       Estimate Std. Error         df t value Pr(>|t|)    
#   (Intercept)                         1.15489    0.02164   30.01978  53.377  < 2e-16 ***
#   all_diff_cont                       0.04437    0.01123 4178.80666   3.950 7.95e-05 ***
#   prev_all_diff_cont                 -0.03339    0.01125 4178.83886  -2.969    0.003 ** 
#   all_diff_cont:prev_all_diff_cont    0.02077    0.01641 4177.22139   1.266    0.206    

# THESE FINDINGS TOTALLY PARALLEL THE COMPLEX INTERACTIVE MODEL ABOVE AND BACK UP THE OBSERVATIONS MADE THERE.



# Examine best-fitting threshold values
possible_threshold_values = sort(unique(best_span_overall))+.25;
possible_threshold_values = possible_threshold_values[1:(length(possible_threshold_values)-1)];

all_aic_values = array(data = NA, dim = length(possible_threshold_values));

clean_data_dm$capacity_HighP1_lowN1_temp = NA;

for(ind in 1:length(possible_threshold_values)){
  break_val = possible_threshold_values[ind];
  clean_data_dm$capacity_HighP1_lowN1_temp[clean_data_dm$best_span_overall_original > break_val] = 1;
  clean_data_dm$capacity_HighP1_lowN1_temp[clean_data_dm$best_span_overall_original < break_val] = -1;

  cat(sprintf('This many people are < break_val: %g\n',sum(best_span_overall<break_val)))
  
  if((sum(best_span_overall<break_val) == 1) | (sum(best_span_overall>break_val) == 1)){
    next # don't use any categorizations that create a 'group' with just 1 person
  }
  
  m3_tmp = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1_temp + 
                                                  (1 | subjectnumber), data = clean_data_dm, REML = F);
  all_aic_values[ind] = AIC(m3_tmp)
}

best_aic = min(all_aic_values, na.rm = T);
best_threshold = possible_threshold_values[which(all_aic_values == best_aic)];

cat(sprintf('The best fitting model uses a threshold value of %g.\n', best_threshold))

plot(sort(best_span_overall), xlab = 'Participants', ylab = 'Span')
abline(h = best_threshold, col = 'blue', lwd = 4)
abline(h = medianSpan, col = 'red', lwd = 4, lty = 'dotted') # median value
legend('topleft', legend = c('Span','Best threshold','Median span'), col = c('black','blue', 'red'), lty = 1)

plot(x = possible_threshold_values, y = all_aic_values, type = 'l', col = 'green', xlab = 'Thresholds', ylab = 'AIC values (lower better)')

#####EXPLORATORY ANALYSES ##########


#notes for scoring 
#high scoring is a "thinker" 
#5 x 18 = highest score = 90 

#reverse score these columns needForCog_ 3,4,5,7,8,9,12,16,17
  # 1 = extremely characteristic 
  # 5 = extremely uncharacteristic

# Normal answers ranged 1-5 
  # extremely uncharacteristic of me to extremely characteristic of me 







################ MOST STUFF BELOW HERE CAN BE IGNORED ################


# Continuous difficulty (including previous) and continuous capacity and categorical capacity
m1_prev_diffCont_capacityCont_capacityCat_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * prev_all_diff_cont * best_span_overall + 
                                                             all_diff_cont * prev_all_diff_cont * capacity_HighP1_lowN1 + 
                                                             (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_diffCont_capacityCont_capacityCat_intxn_rfx)





### Using Best Span Overall ###
m1_diffCat_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * best_span_overall + 
                                           (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffCat_capacityCont_intxn_rfx)
# No effect, as expected. 

m1_prev_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                        easyP1difficultN1 * easyP1difficultN1_prev * best_span_overall + 
                                        (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_capacityCont_intxn_rfx)
# DOES NOT WORK with continuous measure of capacity

m1_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + easy * best_span_overall + difficult * best_span_overall + 
                                   (1 | subjectnumber), data = clean_data_dm);
summary(m1_capacityCont_intxn_rfx)
# Continuous span again does not work well. 

m1_diffCont_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + all_diff_cont * best_span_overall + 
                                            (1 | subjectnumber), data = clean_data_dm);
summary(m1_diffCont_capacityCont_intxn_rfx)
# No effect, as expected. 

# Continuous difficulty (including previous) and continuous capacity
m1_prev_diffCont_capacityCont_intxn_rfx = lmer(sqrtRT ~ 1 + 
                                                 all_diff_cont * prev_all_diff_cont * best_span_overall + 
                                                 (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_diffCont_capacityCont_intxn_rfx)
# Again best span is not working well here.




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

#Q: Does rt vary significantly from high to low controllers regardelss of choice type/difficulty?
#Q: Does cognitive capacity influence reaction time?Do high controllers have diff avg RT (predicted faster avg) compared to low controllers? 
#t.test(meanRT_diff_capacity_High, meanRT_diff_capacity_Low, na.rm = T);
#t.test(meanRT_easy_capacity_High, meanRT_easy_capacity_Low, na.rm = T)
#A: not significantly different, suggesting that cognitive capacity on this level, does not effect reatction time. 


#see behavioral (rt) variability in the regression based upon inc or dec of capacity?
#see individual and group differences? 



###Exploratory Analyses (Qualtrics Data) ###
#1. import Qualtrics data 



#2. quality check ie make sure pts are correct and match data  
#3. score NFC & add it to measure of CC (see citations)
#4. Run an analyses with CC see above with this measure instead? 

#NFC scoring = sum of what they reported on all 18 , highest 72 lowest -72 