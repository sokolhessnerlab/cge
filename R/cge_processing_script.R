# CGE Data Processing Script
#
# Script to process the data collected from CGE during Fall 2023 and Winter 2024 in the CGE
# (Control & Gambling Task with Eyetracking) study.


# STEP 1: SET YOUR WORKING DIRECTORY!
# On PSH's computers...
setwd('/Users/sokolhessner/Documents/gitrepos/cge/');
# On Von's PC Laptop "tabletas"...
setwd('???');


# STEP 2: then run from here on the same
config = config::get()

setwd(config$path$data$raw)

# List all the data files
rdmfn = dir(pattern = glob2rx('cgeRDM_*.csv'),full.names = T, recursive = T);
sspfn = dir(pattern = glob2rx('cgeSYMSPANbothReal_*.csv'), full.names = T, recursive = T);
ospfn = dir(pattern = glob2rx('cgeOSPANbothReal_*.csv'), full.names = T, recursive = T);
qualfn = dir(pattern = glob2rx('*Survey*.csv'), full.names = T, recursive = T);

# Identify the number of participants from the file listing
number_of_subjects = length(rdmfn);


### Qualtrics Processing
#   IUS-12 (Intolerance for Uncertainty)
#   NCS-18 (Need for Cognition)
#   SNS (Subjective Numeracy),
#   PSS (Perceived Stress), & Demographics ###

raw_qualtrics_data = read.csv(qualfn[(length(qualfn))]); # Load the last Qualtrics file, assuming naming convention sorts the files so that last is most recent!

survey_colnames = c(
  'subjectID',
  'age',
  'gender',
  'ethnicity',
  'race',
  'education',
  'firstgen',
  'politicalorientation',
  'IUS',
  'NCS',
  'SNS',
  'PSS'
);

survey_data = array(data = NA, dim = c(number_of_subjects, length(survey_colnames)));
colnames(survey_data) <- survey_colnames;
survey_data = as.data.frame(survey_data)

raw_qualtrics_data$EI.1[15] = '007'; # replacing 'CGE007' with the numeric value
raw_qualtrics_data = raw_qualtrics_data[-3,]; # deleting an early test line

# Make indices to identify which rows to keep!
ind_complete = raw_qualtrics_data$Finished == 1; # completed the survey
ind_nottest = raw_qualtrics_data$EI.1 < 900; # Subject IDs should be < 900

ind_overall = ind_complete & ind_nottest;
cat(sprintf('Qualtrics data has %g participants; decision-making data has %g participants.\n', sum(ind_overall), number_of_subjects))

survey_data$subjectID = as.numeric(raw_qualtrics_data$EI.1[ind_overall])
#... do other columns!


### Prepping for Subject-Level Task Data Loop ###

# Store some basic information about size of the decision-making task
num_static_trials = 50;
num_dynamic_trials = 120;
number_of_dm_trials_per_person = num_static_trials + num_dynamic_trials; # static = 50, dynamic = 120

# Set up variables to hold decision-making data & qualtrics
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
  'bestMu',
  'ospan',
  'symspan',
  'complexspan',
  'NFC',
  'PSS',
  'SNS',
  'IUS',
  'Demo'
);

data_dm = array(data = NA, dim = c(0, length(column_names_dm)));
colnames(data_dm) <- column_names_dm

# Set up variables to hold working memory data
number_of_ospan_trials_per_person = 25;
number_of_sspan_trials_per_person = 14;

ospanExclude = c();
sspanExclude = c();
complexSpanExclude = as.data.frame(matrix(data=0, 
                                          nrow = number_of_subjects, 
                                          ncol=3, 
                                          dimnames=list(c(NULL), c("subjectnumber", "ospanExclude", "symspanExclude"))));
complexSpanExclude$subjectnumber = 1:number_of_subjects;

complexSpanScores = as.data.frame(matrix(data=NA, 
                                         nrow = number_of_subjects, 
                                         ncol=4, 
                                         dimnames=list(c(NULL), c("subjectnumber", "ospanScore", "symspanScore", "compositeSpanScore"))));
complexSpanScores$subjectnumber= 1:number_of_subjects

# Loop
for(s in 1:number_of_subjects){
  
  ### OSPAN DATA ### 
  
  ospantmpdata = read.csv(ospfn[s]);
  ospantmpdata$subid = as.integer(substr(ospfn[s],6,8));
  
  
  if (any(ospantmpdata$percentCorrectMath[is.finite(ospantmpdata$percentCorrectMath)]<85)){
    ospanExclude = c(ospanExclude,ospantmpdata$subid[1]);
    complexSpanExclude$ospanExclude[s] = 1;
  } else {
    correctIndospan = which(ospantmpdata$correctCount == ospantmpdata$setSize)
    complexSpanScores$ospanScore[s] = sum(ospantmpdata$correctCount[correctIndospan])/number_of_ospan_trials_per_person;
  }
  
  ### SYMSPAN DATA ###
  sspantmpdata = read.csv(sspfn[s]);
  sspantmpdata$subid = as.integer(substr(sspfn[s],6,8));
  
  if (any(sspantmpdata$percentCorrectSym[is.finite(sspantmpdata$percentCorrectSym)]<85)){
    sspanExclude = c(sspanExclude,sspantmpdata$subid[1]);
    complexSpanExclude$symspanExclude[s] = 1;
  } else {
    correctIndsymspan = which(sspantmpdata$squareCorrectCount == sspantmpdata$setSize)
    complexSpanScores$symspanScore[s] = sum(sspantmpdata$squareCorrectCount[correctIndsymspan])/number_of_sspan_trials_per_person;
  }
  
  
  ### COMPOSITE SPAN ###
  if ((complexSpanExclude$ospanExclude[s] == 0) & (complexSpanExclude$symspanExclude[s] == 0)){ # if both scores available
    complexSpanScores$compositeSpanScore[s] = mean(c((complexSpanScores$ospanScore[s]),(complexSpanScores$symspanScore[s]))); # average the two scores
  } else if ((complexSpanExclude$ospanExclude[s] == 1) & (complexSpanExclude$symspanExclude[s] == 0)){ # if only SymSpan
    complexSpanScores$compositeSpanScore[s] = complexSpanScores$symspanScore[s];
  } else if ((complexSpanExclude$ospanExclude[s] == 0) & (complexSpanExclude$symspanExclude[s] == 1)){ # if only OSpan
    complexSpanScores$compositeSpanScore[s] = complexSpanScores$ospanScore[s];
  }; # ... else, leave it NA
  
  
  
  ### RDM Data ###
  # Load in the data
  tmpdata = read.csv(rdmfn[s]);
  
  # DECISION-MAKING DATA
  dm_data_to_add = array(data = NA, dim = c(number_of_dm_trials_per_person,length(column_names_dm)));

  dm_index_static = is.finite(tmpdata$staticTrials.thisTrialN);
  dm_index_dynamic = is.finite(tmpdata$dynamicTrials.thisTrialN);

  tmp_trialnum = c(tmpdata$staticTrials.thisTrialN[dm_index_static] + 1,
                   tmpdata$dynamicTrials.thisTrialN[dm_index_dynamic] + num_static_trials + 1);

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

  dm_data_to_add[,7] = c(tmpdata$realChoiceResp.rt[dm_index_static],
                         tmpdata$realChoiceResp.rt[dm_index_dynamic]); # RTs

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
  
  dm_data_to_add[,15] = complexSpanScores$ospanScore[s];
  dm_data_to_add[,16] = complexSpanScores$symspanScore[s];
  dm_data_to_add[,17] = complexSpanScores$compositeSpanScore[s];
  
  

  # Add this person's DM data to the total DM data.
  data_dm = rbind(data_dm,dm_data_to_add);
}

data_dm = as.data.frame(data_dm) # make it a data frame so it plays nice

# save out CSVs with the clean, compiled data!
setwd(config$path$data$processed);

write.csv(data_dm, file=sprintf('cge_processed_decisionmaking_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(complexSpanScores, file=sprintf('cge_processed_complexspan_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);

# all done!

