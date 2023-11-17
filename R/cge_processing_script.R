# CGT Data Processing Script
#
# Script to process the data collected online during Summer 2022 in the CGT
# (Control & Gambling Task) study.

# identify the working directory paths
main_wd = '/Volumes/shlab/Projects/CGT/';

rawdata_wd = paste0(main_wd,'rawdata/');
processeddata_wd = paste0(main_wd,'processeddata/')

# set the working directory
setwd(rawdata_wd);

# List all the data files
fn = dir(pattern = glob2rx('CGTgamblingSpanTasks_2022-09*.csv'),full.names = T);

# Identify the number of participants from the file listing
number_of_subjects = length(fn);

# Store some basic information about size of the decision-making task
num_static_trials = 50;
num_dynamic_trials = 120;
number_of_dm_trials_per_person = num_static_trials + num_dynamic_trials; # static = 50, dynamic = 120

# Set up variables to hold decision-making data
column_names_dm = c(
  'trialnumber',
  'subjectnumber',
  'riskyopt1',
  'riskyopt2',
  'safe',
  'choice',
  'reactiontime',
  'outcome',
  'ischecktrial',
  'static0dynamic1',
  'easyP1difficultN1',
  'choiceP',
  'bestRho',
  'bestMu'
);

data_dm = array(data = NA, dim = c(0, length(column_names_dm)));
colnames(data_dm) <- column_names_dm

# Set up variables to hold working memory data
number_of_wm_trials_per_person = 28; # 14 forward, 14 backward

column_names_rawdata_wm = c(
  'digitsForTrial', #both FS & BS digits
  'textbox.text', #FS response
  'textboxBS.text', #BS response
  'trialNumber', #both trial number
  'digitLoop.thisRepN', #FS number of digits
  'digitLoopBS.thisRepN', #BS number of digits
  'correct' #both FS & BS
);

# this will have trials in rows, these will be col. names
column_names_wm = c(
  'trialnumber',
  'subjectnumber',
  'number_digits',
  'forward1backward0',
  'correct'
);

data_wm = array(data = NA, dim = c(0, length(column_names_wm)));
colnames(data_wm) <- column_names_wm

# Loop
for(s in 1:number_of_subjects){
  # Load in the data
  tmpdata = read.csv(fn[s]);
  
  # DECISION-MAKING DATA
  dm_data_to_add = array(data = NA, dim = c(number_of_dm_trials_per_person,length(column_names_dm)));

  dm_index_static = is.finite(tmpdata$staticRDM.thisTrialN);
  dm_index_dynamic = is.finite(tmpdata$dynamicRDM.thisTrialN);

  tmp_trialnum = c(tmpdata$staticRDM.thisTrialN[dm_index_static] + 1,
                   tmpdata$dynamicRDM.thisTrialN[dm_index_dynamic] + num_static_trials + 1);

  dm_data_to_add[,1] = tmp_trialnum; # trial number
  dm_data_to_add[,2] = s; # subject number

  tmp_riskyopt1 = c(tmpdata$riskyoption1[dm_index_static],
                    tmpdata$riskyoption1[dm_index_dynamic]);
  tmp_riskyopt2 = c(tmpdata$riskyoption2[dm_index_static],
                    tmpdata$riskyoption2[dm_index_dynamic]);
  tmp_safe = c(tmpdata$safeoption[dm_index_static],
               tmpdata$safeoption[dm_index_dynamic]);

  dm_data_to_add[,3:5] = cbind(tmp_riskyopt1,tmp_riskyopt2,tmp_safe) # dollar amounts

  dm_data_to_add[,6] = c(tmpdata$choices[dm_index_static],
                         tmpdata$choices[dm_index_dynamic]); # choices

  dm_data_to_add[,7] = c(tmpdata$realChoice.rt[dm_index_static],
                         tmpdata$realChoice.rt[dm_index_dynamic]); # RTs

  dm_data_to_add[,8] = c(tmpdata$outcomes[dm_index_static],
                         tmpdata$outcomes[dm_index_dynamic]); # outcomes

  dm_data_to_add[,9] = c(tmpdata$ischecktrial[dm_index_static],
                         array(data = 0, dim = c(1,num_dynamic_trials))); # is check trial

  dm_data_to_add[,10] = c(array(data = 0, dim = c(1,num_static_trials)),
                         array(data = 1, dim = c(1,num_dynamic_trials))); # static 0, dynamic 1

  dm_data_to_add[,11] = c(array(data = 0, dim = c(1,num_static_trials)),
                          tmpdata$easy0difficult1[dm_index_dynamic]*-2 + 1); # easy +1, difficult -1

  dm_data_to_add[,12] = c(array(data = NA, dim = c(1,num_static_trials)),
                          tmpdata$choiceP[dm_index_dynamic]); # choice probability on easy/diff dynamic trials

  dm_data_to_add[,13] = tmpdata$bestRho[is.finite(tmpdata$bestRho)];
  dm_data_to_add[,14] = tmpdata$bestMu[is.finite(tmpdata$bestMu)];


  # Add this person's DM data to the total DM data.
  data_dm = rbind(data_dm,dm_data_to_add);
  
  # WORKING MEMORY
  wm_data_to_add = array(data = NA, dim = c(number_of_wm_trials_per_person,length(column_names_wm)));
  
  wm_trial_indices = which(!is.na(tmpdata$trialNumber));
  
  wm_data_to_add[,1] = 1:number_of_wm_trials_per_person; # trial numbers
  wm_data_to_add[,2] = s; # subject number
  
  wm_data_to_add[,3] = (nchar(tmpdata$digitsForTrial[wm_trial_indices-1])-1)/2; # number of digits on the trial
  
  wm_data_to_add[1:14,4] = 1; # forward is always first
  wm_data_to_add[15:28,4] = 0; # backward is always second
  
  wm_data_to_add[,5] = tmpdata$correct[wm_trial_indices]; # correct = 1, incorrect = 0
  
  data_wm = rbind(data_wm,wm_data_to_add);
}

data_dm = as.data.frame(data_dm) # make it a data frame so it plays nice
data_wm = as.data.frame(data_wm)

# save out CSVs with the clean, compiled data!
setwd(processeddata_wd);

write.csv(data_dm, file=sprintf('cgt_processed_decisionmaking_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_wm, file=sprintf('cgt_processed_workingmemory_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);

# all done!

