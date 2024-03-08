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
#       - number of missing samples
#       - number of blinks
#       - calibration quality
#       - or other metric (% eyegaze off-screen?)
# - Align timestamps from python output w/ eyelink timestamps
#   - then trial timestamps


# UNCOMMENT THIS BLOCK WHEN DONE

#### STEP 1: SET YOUR WORKING DIRECTORY! ####
# # On PSH's computers...
# setwd('/Users/sokolhessner/Documents/gitrepos/cge/');
# # On Von's PC Laptop "tabletas"...
# setwd('C:/Users/jvonm/Documents/GitHub/cge');
# 
# 
#### STEP 2: then run from here on the same ####
# config = config::get();
# 
# setwd(config$path$data$raw);
setwd('~/Desktop/tmp_et_CGE/')

#### STEP 3: Get the file names ####
cat('Identifying file locations.\n');
etfn = dir(pattern = glob2rx('cge*.asc'),full.names = T, recursive = T);
rdmfn = dir(pattern = glob2rx('cgeRDM_*.csv'),full.names = T, recursive = T);


#### STEP 4: SET UP FOR SUBJECT LOOP ####
library('eyelinker') # for eyelink-specific file interaction
library('zoo') # for interpolation
# library('gazer') # Requires R 4.2 or higher; may need to upgrade?

number_of_subjects = length(etfn);

#### STEP 5: SUBJECT LOOP ####
# for (s in 1:number_of_subjects){
# 
# }

s = 3; 

cat(sprintf('Processing eye-tracking data for subject %i.\n',s))
cat('Loading eye-tracking data... ')
raw_et_data = read.asc(etfn[s], samples = T, events = F)
cat('Done.\n')

# Settings:
# 1000 Hz sample rate
# 1280 (w) x 1024 (h) screen size)
# Diameter pupil data type (not area)
original_sample_rate = raw_et_data$info$sample.rate

# # How to visualize the data
# # NOTE: these are slow to execute because the dataset is so large (~1.2 million datapoints/person)
# # Gaze location (coordinates (0,0) are TOP LEFT)
# plot(raw_et_data$raw$xp, -raw_et_data$raw$yp, pch = 16, cex = .5, col = rgb(1,0,0,.1), 
#      xlim = c(-200, raw_et_data$info$screen.x + 200), ylim = c(200, -raw_et_data$info$screen.y-200))
# lines(x = c(0, raw_et_data$info$screen.x, raw_et_data$info$screen.x, 0, 0), 
#       y = c(0, 0, -raw_et_data$info$screen.y, -raw_et_data$info$screen.y, 0))
# plot(raw_et_data$raw$ps, type = 'l') # the pupil dilation data

# # Code to construct a low-res 'heatmap' that displays more easily than the full data.
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

###### 1. Identify blink points ######
missing_points_ind = which(is.na(pupil_data_raw)); # index of all missing datapoints
blink_init_sample = missing_points_ind[c(1,which(diff(missing_points_ind) > 1) + 1)] # first sample of missing data epochs
blink_final_sample = missing_points_ind[c(which(diff(missing_points_ind) > 1), length(missing_points_ind))] # final sample
blink_length = time_data[blink_final_sample] - time_data[blink_init_sample]; # length in ms

blink_data = as.data.frame(cbind(blink_init_sample, blink_final_sample, blink_length))
hist(blink_data$blink_length, xlab = 'milliseconds', main = 'Blink Lengths', breaks = 200) # opt: visualize blink lengths

###### 2. Summarize Missing Data ###### 
number_of_missing_samples_raw = length(missing_points_ind);
percent_of_missing_samples_raw = number_of_missing_samples_raw/length(pupil_data_raw);
number_of_blinks = length(blink_init_sample);

###### 3. Extend blink points ###### 
blink_length_threshold = 20; # milliseconds (ms) what counts as a 'blink'? There are plenty of super-short missing samples.
na_fill = 100; # how many milliseconds to expand the blinks
pupil_data_extend = pupil_data_raw;

cat('Extending blink gaps... ')
for (b in 1:number_of_blinks){
  if (blink_data$blink_length[b] > blink_length_threshold){
    pupil_data_extend[(which(time_data > (time_data[blink_init_sample[b]] - na_fill))[1]):
                        ((which(time_data > (time_data[blink_final_sample[b]] + na_fill))[1])-1)] = NA;
  }
}
cat('Done.\n')

###### 4. Interpolate ###### 

# Interpolate linearly across NA gaps
cat('Interpolating linearly across data gaps... ')
pupil_data_extend_interp = na.approx(pupil_data_extend);
cat('Done.\n')
# technically, this approach linearly interpolates across datapoints, not timepoints
# i.e. if one or more timepoints are simply missing (not that they would be NAs, but 
# that they would not be *present*), this would inaccurately interpolate. This is 
# probably fine, though - missing samples are not expected, and the harm done would
# be pretty minor.

######  5. Replace excessively long missing sections with NAs ###### 
maximum_allowable_missing = 1000; # ms; what should this value be? 

for (b in 1:number_of_blinks){
  if (blink_data$blink_length[b] >= maximum_allowable_missing) {
    pupil_data_extend_interp[blink_data$blink_init_sample[b]:blink_final_sample[b]] = NA;
  }
}

###### 6. Smooth (10-point moving window) ###### 
cat('Smoothing pupil diameter data... ')
smoothing_window_width = 10; # points to smooth over; 10 pts @ 1000Hz = 10ms
pupil_data_extend_interp_smooth = rollapply(pupil_data_extend_interp, 
                                            width = smoothing_window_width, FUN = 'mean', partial = T,
                                            align = 'center', na.rm = T)
cat('Done.\n')

number_of_missing_samples_proc = length(which(is.na(pupil_data_extend_interp_smooth)));
percent_of_missing_samples_proc = number_of_missing_samples_proc/length(pupil_data_extend_interp_smooth);

###### 7. Convert pupil diameter data to mm ###### 
pupil_data_extend_interp_smooth_mm = pupil_data_extend_interp_smooth; # MUST DO THIS!
# SEE THIS LINK: https://researchwiki.solo.universiteitleiden.nl/xwiki/wiki/researchwiki.solo.universiteitleiden.nl/view/Hardware/EyeLink/#:~:text=EyeLink%20reports%20pupil%20size%20as,circle%20with%20a%20known%20diameter.

###### 8. Identify and extract timestamp for practice start from ET file ###### 
cat('Aligning timestamps... ')
et_file_connection = file(etfn[s],'r') # open the file connection to the ASC file.

msgs = ''; # where we'll store messages
number_of_messages = 0; # set our counter

while ( TRUE ) {
  line = readLines(et_file_connection, n = 1) # read a line of the file
  if ( length(line) == 0 ) { # if we have read the full file and there are no more lines left, stop
    break
  }
  # print(line) # for debugging
  if ('MSG' == substr(line, 1, 3)) { # if this is a 'message' line... 
    number_of_messages = number_of_messages + 1; # increment the # of messages we've found
    # print(line) # for debugging
    msgs[number_of_messages] = line; # store the message
  }
}

close(et_file_connection) # close the file connection

for (m in 1:number_of_messages){
  if ('Practice Text Shown' == substr(msgs[m], 13, 31)){ # identify the line with this text
    et_alignment_time = as.numeric(substr(msgs[65], 5, 11)) # pull out the start time from that
  }
}

time_data = time_data - et_alignment_time; # Correct all timestamps to be relative to this moment
cat('Done.\n')

##### Create Behavioral Event Timestamp Matrix ###### 
tmpdata = read.csv(rdmfn[s]); 
number_of_trials = 170

event_timestamps = array(data = NA, dim = c(number_of_trials, 4))
column_names = c(
  'decision_start',
  'decision_end',
  'outcome_start',
  'outcome_end'
)
colnames(event_timestamps) <- column_names;
event_timestamps = as.data.frame(event_timestamps)

beh_alignment_time = tmpdata$pracStartTxt.started[3];

trial_index = is.finite(tmpdata$realChoiceResp.started);

event_timestamps$decision_start = tmpdata$realChoiceResp.started[trial_index];
event_timestamps$decision_end = tmpdata$isiRealFix.started[trial_index];
event_timestamps$outcome_start = tmpdata$isiRealFix.stopped[trial_index];
event_timestamps$outcome_end = tmpdata$itiRealFix.started[trial_index];

event_timestamps[!(is.finite(tmpdata$choices[trial_index])),] = NA;

event_timestamps = event_timestamps - beh_alignment_time; # align the behavioral data to the same moment
event_timestamps = event_timestamps * 1000; # into milliseconds, like eyetracking

##### Calculate Summary Metrics of Pupillometry #####
cat('Calculating summary pupillometry measures... ')
column_names = c(
  'predecision_baseline_mean',
  'decision_mean',
  'decision_median',
  'preoutcome_baseline_mean',
  'outcome_mean',
  'outcome_median'
)
et_summary_stats = array(data = NA, dim = c(number_of_trials, length(column_names)))
colnames(et_summary_stats) <- column_names;
et_summary_stats = as.data.frame(et_summary_stats)

baseline_window_width = 500; # ms

for (t in 1:number_of_trials){
  et_summary_stats$predecision_baseline_mean[t] = 
    mean(pupil_data_extend_interp_smooth_mm[(time_data >= (event_timestamps$decision_start[t] - baseline_window_width)) & 
                                              (time_data < event_timestamps$decision_start[t])])
  
  et_summary_stats$decision_mean[t] = 
    mean(pupil_data_extend_interp_smooth_mm[(time_data >= event_timestamps$decision_start[t]) & 
                                              (time_data < event_timestamps$decision_end[t])])
  et_summary_stats$decision_median[t] = 
    median(pupil_data_extend_interp_smooth_mm[(time_data >= event_timestamps$decision_start[t]) & 
                                              (time_data < event_timestamps$decision_end[t])])

  et_summary_stats$preoutcome_baseline_mean[t] = 
    mean(pupil_data_extend_interp_smooth_mm[(time_data >= (event_timestamps$outcome_start[t] - baseline_window_width)) & 
                                              (time_data < event_timestamps$outcome_start[t])])
  
  et_summary_stats$outcome_mean[t] = 
    mean(pupil_data_extend_interp_smooth_mm[(time_data >= event_timestamps$outcome_start[t]) & 
                                              (time_data < event_timestamps$outcome_end[t])])
  et_summary_stats$outcome_median[t] = 
    median(pupil_data_extend_interp_smooth_mm[(time_data >= event_timestamps$outcome_start[t]) & 
                                                (time_data < event_timestamps$outcome_end[t])])
}

et_summary_stats$decision_mean_cor = et_summary_stats$decision_mean - et_summary_stats$predecision_baseline_mean;
et_summary_stats$outcome_mean_cor = et_summary_stats$outcome_mean - et_summary_stats$preoutcome_baseline_mean;

cat('Done.\n')

cat(sprintf('CGE%03i: RAW missing %i samples (%.1f%%); %i blinks. PROCESSED missing %i samples (%.1f%%).\n', 
            s, number_of_missing_samples_raw, percent_of_missing_samples_raw*100, number_of_blinks,
            number_of_missing_samples_proc, percent_of_missing_samples_proc*100))


