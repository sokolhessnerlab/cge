/***************************** 
 * Cgtgamblingspantasks Test *
 *****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'CGTgamblingSpanTasks';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
psychoJS.start({
  expName,
  expInfo,
  resources: [
    // relative path to index.html
    { name: 'digitSpanTrialNumber.xlsx', path: 'digitSpanTrialNumber.xlsx' },
    { name: 'CGT-choice-set.csv', path: 'CGT-choice-set.csv' },
    { name: 'cgtRDMPractice.xlsx', path: 'cgtRDMPractice.xlsx' },
    { name: 'continue.png', path: 'continue.png' },
    { name: 'digitSpanPractice.xlsx', path: 'digitSpanPractice.xlsx' },
    // absolute path:
    //{ name: 'trialTypes_B.xls', path: 'http://a.website.org/a.path/trialTypes_B.xls' }
  ]
});
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(settingUpRoutineBegin());
flowScheduler.add(settingUpRoutineEachFrame());
flowScheduler.add(settingUpRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(pracStartRoutineBegin());
flowScheduler.add(pracStartRoutineEachFrame());
flowScheduler.add(pracStartRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(postPracRoutineBegin());
flowScheduler.add(postPracRoutineEachFrame());
flowScheduler.add(postPracRoutineEnd());
const staticRDMLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(staticRDMLoopBegin(staticRDMLoopScheduler));
flowScheduler.add(staticRDMLoopScheduler);
flowScheduler.add(staticRDMLoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(loadDynamicChoicesetRoutineBegin());
flowScheduler.add(loadDynamicChoicesetRoutineEachFrame());
flowScheduler.add(loadDynamicChoicesetRoutineEnd());
flowScheduler.add(startDynamicTaskRoutineBegin());
flowScheduler.add(startDynamicTaskRoutineEachFrame());
flowScheduler.add(startDynamicTaskRoutineEnd());
const dynamicRDMLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(dynamicRDMLoopBegin(dynamicRDMLoopScheduler));
flowScheduler.add(dynamicRDMLoopScheduler);
flowScheduler.add(dynamicRDMLoopEnd);
flowScheduler.add(rdmToSpanTransitionRoutineBegin());
flowScheduler.add(rdmToSpanTransitionRoutineEachFrame());
flowScheduler.add(rdmToSpanTransitionRoutineEnd());
flowScheduler.add(SpanGeneralInstructionsRoutineBegin());
flowScheduler.add(SpanGeneralInstructionsRoutineEachFrame());
flowScheduler.add(SpanGeneralInstructionsRoutineEnd());
flowScheduler.add(SpanReminder1RoutineBegin());
flowScheduler.add(SpanReminder1RoutineEachFrame());
flowScheduler.add(SpanReminder1RoutineEnd());
flowScheduler.add(SpanReminder2RoutineBegin());
flowScheduler.add(SpanReminder2RoutineEachFrame());
flowScheduler.add(SpanReminder2RoutineEnd());
flowScheduler.add(FSInstructionsRoutineBegin());
flowScheduler.add(FSInstructionsRoutineEachFrame());
flowScheduler.add(FSInstructionsRoutineEnd());
const trialFSPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialFSPracticeLoopBegin(trialFSPracticeLoopScheduler));
flowScheduler.add(trialFSPracticeLoopScheduler);
flowScheduler.add(trialFSPracticeLoopEnd);
flowScheduler.add(StartRealFSRoutineBegin());
flowScheduler.add(StartRealFSRoutineEachFrame());
flowScheduler.add(StartRealFSRoutineEnd());
const trialsFSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsFSLoopBegin(trialsFSLoopScheduler));
flowScheduler.add(trialsFSLoopScheduler);
flowScheduler.add(trialsFSLoopEnd);
flowScheduler.add(FStoBStransitionRoutineBegin());
flowScheduler.add(FStoBStransitionRoutineEachFrame());
flowScheduler.add(FStoBStransitionRoutineEnd());
flowScheduler.add(InstructionsBSRoutineBegin());
flowScheduler.add(InstructionsBSRoutineEachFrame());
flowScheduler.add(InstructionsBSRoutineEnd());
const trialsPracticeBSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeBSLoopBegin(trialsPracticeBSLoopScheduler));
flowScheduler.add(trialsPracticeBSLoopScheduler);
flowScheduler.add(trialsPracticeBSLoopEnd);
flowScheduler.add(startRealBSRoutineBegin());
flowScheduler.add(startRealBSRoutineEachFrame());
flowScheduler.add(startRealBSRoutineEnd());
const trialsBSLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsBSLoopBegin(trialsBSLoopScheduler));
flowScheduler.add(trialsBSLoopScheduler);
flowScheduler.add(trialsBSLoopEnd);
flowScheduler.add(ENDRoutineBegin());
flowScheduler.add(ENDRoutineEachFrame());
flowScheduler.add(ENDRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'CGT-choice-set.csv', 'path': 'CGT-choice-set.csv'},
    {'name': 'cgtRDMPractice.xlsx', 'path': 'cgtRDMPractice.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.1';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls(('https://udenver.qualtrics.com/jfe/form/SV_a4qaGzutOwOjcPk?id=' + expInfo['participant']), 'https://du.sona-systems.com');

  return Scheduler.Event.NEXT;
}


var settingUpClock;
var instructionsTextHeight;
var lettersTextHeight;
var wrap;
var instructionsClock;
var Instructions;
var inst1;
var pracStartClock;
var startPract;
var startPracResp;
var practiceTaskClock;
var textHeight;
var circleLeft;
var circleRight;
var lineLeft;
var orText;
var lossTxt;
var gainTxt;
var safeTxt;
var vLeft;
var nRight;
var choice1;
var isiPracClock;
var isiText;
var feedbackClock;
var noRespLoc;
var ocLoc;
var ocGambleLoc;
var ocSafeLoc;
var hideGamLoc;
var noRespTxt;
var ocGamble;
var ocSafe;
var outcomeText;
var hideGamble;
var itiPrac_2Clock;
var itiText;
var postPracClock;
var postPracText;
var postPractResp;
var choiceWindowClock;
var circleLeftReal;
var circleRightReal;
var lineLeftReal;
var orTextReal;
var lossTxtReal;
var gainTxtReal;
var safeTxtReal;
var vLeftReal;
var nRightReal;
var realChoice;
var isiClock;
var isiTextReal;
var showOutcomeClock;
var choices;
var outcomes;
var noRespTxtReal;
var ocGambleReal;
var ocSafeReal;
var outcomeTextReal;
var hideGambleReal;
var itiClock;
var itiTextReal;
var computeEstimatesClock;
var settingUpForPart2;
var loadDynamicChoicesetClock;
var startDynamicTaskClock;
var moveToRDMpart2;
var key_resp;
var showOutcomeDynamicClock;
var noRespTxtReal_3;
var ocGambleReal_3;
var ocSafeReal_3;
var outcomeTextReal_3;
var hideGambleReal_3;
var rdmToSpanTransitionClock;
var breaktxt;
var stopBreak;
var letterTextHeight;
var SpanGeneralInstructionsClock;
var GenInsText;
var movealong;
var SpanReminder1Clock;
var Reminder1;
var movealong2;
var SpanReminder2Clock;
var Reminder2;
var movealong3;
var FSInstructionsClock;
var FSGenInsText;
var startPractice;
var ShowNumbersPracticeClock;
var fixation_2;
var pres_text_practice;
var RecallPracticeClock;
var recall_txtPractice;
var textboxPractice;
var cont_buttonPractice;
var mousePractice;
var FeedbackPracticeClock;
var feedbac_textPractice;
var StartRealFSClock;
var praccomplete;
var startFSreal;
var selectNumbersClock;
var ShowNumbersClock;
var fixation;
var presentation_text;
var RecallClock;
var recall_txt;
var textbox;
var cont_button;
var mouse_3;
var FeedbackClock;
var feedback_text;
var FStoBStransitionClock;
var roundTransition;
var moveToBS;
var InstructionsBSClock;
var BSGenInsText;
var startBSprac;
var showNumbersPracticeBSClock;
var fixation_3;
var pres_text_practice_2;
var recallPracticeBSClock;
var recall_txtPractice_2;
var textboxPractice_2;
var cont_buttonPractice_2;
var mousePractice_2;
var feedbackPracticeBSClock;
var feedbac_textPractice_2;
var startRealBSClock;
var praccompleteBS;
var startBSreal;
var selectNumbersBSClock;
var showNumbersBSClock;
var fixationBS;
var presentation_textBS;
var RecallBSClock;
var recall_txtBS;
var textboxBS;
var cont_buttonBS;
var mouseBS;
var FeedbackBSClock;
var feedback_textBS;
var ENDClock;
var ThankYou;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "settingUp"
  settingUpClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  instructionsTextHeight = 0.05;
  lettersTextHeight = 0.1;
  wrap = 1.5;
  
  
  var initITIstatic
  var initITIdynamic
  
  
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nYou may press "V" to select the option on the left and "N" to select the option on the right.\n\nPress "enter" to move on to the next screen.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  inst1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracStart"
  pracStartClock = new util.Clock();
  startPract = new visual.TextStim({
    win: psychoJS.window,
    name: 'startPract',
    text: 'There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  startPracResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceTask"
  practiceTaskClock = new util.Clock();
  // Run 'Begin Experiment' code from randLoc
  textHeight = 0.05;
  
  circleLeft = new visual.Rect ({
    win: psychoJS.window, name: 'circleLeft', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [(- 0.4), 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  circleRight = new visual.Rect ({
    win: psychoJS.window, name: 'circleRight', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0.4, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  lineLeft = new visual.Rect ({
    win: psychoJS.window, name: 'lineLeft', 
    width: [0.5, 0.01][0], height: [0.5, 0.01][1],
    ori: 0, pos: [0, 0],
    lineWidth: 3, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  orText = new visual.TextStim({
    win: psychoJS.window,
    name: 'orText',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  lossTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'lossTxt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  gainTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'gainTxt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  safeTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'safeTxt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  vLeft = new visual.TextStim({
    win: psychoJS.window,
    name: 'vLeft',
    text: 'V-Left',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  nRight = new visual.TextStim({
    win: psychoJS.window,
    name: 'nRight',
    text: 'N-Right',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  choice1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "isiPrac"
  isiPracClock = new util.Clock();
  isiText = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiText',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  var outcome, noRespLoc, ocLoc, ocGambleLoc, ocSafeLoc, hideGamLoc, pracFeedbackRounded, extraITI;
  
  
  
  noRespLoc = [0,0]
  ocLoc= [0,0]
  ocGambleLoc = [0,0]
  ocSafeLoc = [0,0]
  hideGamLoc = [0,0]
  
  noRespTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'noRespTxt',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: textHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ocGamble = new visual.Rect ({
    win: psychoJS.window, name: 'ocGamble', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  ocSafe = new visual.Rect ({
    win: psychoJS.window, name: 'ocSafe', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  outcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'outcomeText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  hideGamble = new visual.Rect ({
    win: psychoJS.window, name: 'hideGamble', 
    width: [0.6, 0.3][0], height: [0.6, 0.3][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "itiPrac_2"
  itiPrac_2Clock = new util.Clock();
  itiText = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiText',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "postPrac"
  postPracClock = new util.Clock();
  postPracText = new visual.TextStim({
    win: psychoJS.window,
    name: 'postPracText',
    text: 'Practice complete.\n\nWhen you are ready to start ROUND 1 of the task, press "V" or "N".\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  postPractResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "choiceWindow"
  choiceWindowClock = new util.Clock();
  // Run 'Begin Experiment' code from randLoc_2
  var realloc
  circleLeftReal = new visual.Rect ({
    win: psychoJS.window, name: 'circleLeftReal', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [(- 0.4), 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  circleRightReal = new visual.Rect ({
    win: psychoJS.window, name: 'circleRightReal', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0.4, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  lineLeftReal = new visual.Rect ({
    win: psychoJS.window, name: 'lineLeftReal', 
    width: [0.5, 0.01][0], height: [0.5, 0.01][1],
    ori: 0, pos: [0, 0],
    lineWidth: 3, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  orTextReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'orTextReal',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  lossTxtReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'lossTxtReal',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  gainTxtReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'gainTxtReal',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  safeTxtReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'safeTxtReal',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  vLeftReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'vLeftReal',
    text: 'V-Left',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  nRightReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'nRightReal',
    text: 'N-Right',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  realChoice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "isi"
  isiClock = new util.Clock();
  isiTextReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiTextReal',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "showOutcome"
  showOutcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from codeFeedbackReal
  var actualITI
  choices= []
  outcomes = []
  
  
  noRespTxtReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'noRespTxtReal',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ocGambleReal = new visual.Rect ({
    win: psychoJS.window, name: 'ocGambleReal', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  ocSafeReal = new visual.Rect ({
    win: psychoJS.window, name: 'ocSafeReal', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  outcomeTextReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'outcomeTextReal',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  hideGambleReal = new visual.Rect ({
    win: psychoJS.window, name: 'hideGambleReal', 
    width: [0.6, 0.3][0], height: [0.6, 0.3][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  itiTextReal = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiTextReal',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "computeEstimates"
  computeEstimatesClock = new util.Clock();
  settingUpForPart2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'settingUpForPart2',
    text: 'ROUND 1 of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "loadDynamicChoiceset"
  loadDynamicChoicesetClock = new util.Clock();
  // Initialize components for Routine "startDynamicTask"
  startDynamicTaskClock = new util.Clock();
  moveToRDMpart2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'moveToRDMpart2',
    text: 'When you are ready to start ROUND 2 of the task, press "V" or "N".',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "showOutcomeDynamic"
  showOutcomeDynamicClock = new util.Clock();
  // Run 'Begin Experiment' code from codeFeedbackReal_3
  choices= []
  outcomes = []
  
  
  noRespTxtReal_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'noRespTxtReal_3',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ocGambleReal_3 = new visual.Rect ({
    win: psychoJS.window, name: 'ocGambleReal_3', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  ocSafeReal_3 = new visual.Rect ({
    win: psychoJS.window, name: 'ocSafeReal_3', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  outcomeTextReal_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'outcomeTextReal_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  hideGambleReal_3 = new visual.Rect ({
    win: psychoJS.window, name: 'hideGambleReal_3', 
    width: [0.6, 0.3][0], height: [0.6, 0.3][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "rdmToSpanTransition"
  rdmToSpanTransitionClock = new util.Clock();
  breaktxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'breaktxt',
    text: "You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  stopBreak = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from setUpTextFormatting
  instructionsTextHeight = 0.04;
  letterTextHeight = 0.1;
  wrap = 1.6;
  
  // Initialize components for Routine "SpanGeneralInstructions"
  SpanGeneralInstructionsClock = new util.Clock();
  GenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'GenInsText',
    text: "In this task you will be asked to memorize a series of numbers and recall them. \n\nYou will do this twice, once recalling the numbers in the order as presented on the screen and once recalling the numbers in the reverse order as presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. \n\nYou will complete 2 practice sets prior to starting each round of this task.\n\nPress 'enter' to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  movealong = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SpanReminder1"
  SpanReminder1Clock = new util.Clock();
  Reminder1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Reminder1',
    text: "Your performance on this task does not affect your compensation. \n\nThis task is supposed to be challenging - you are not expected to nor do you need to remember everything or get everything correct! \n\nPress 'enter' to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  movealong2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SpanReminder2"
  SpanReminder2Clock = new util.Clock();
  Reminder2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Reminder2',
    text: "We are interested in how many digits you can reliably and truthfully recall. \n\nPlease do your best, and do not cheat (e.g. write down or photograph digits). Thank you for completing this task honestly!\n\nPress 'enter' to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  movealong3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FSInstructions"
  FSInstructionsClock = new util.Clock();
  FSGenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'FSGenInsText',
    text: 'The practice for the forwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 3 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nFor example, if the numbers displayed on the screen are 5 then 7, the correct response is 57.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ShowNumbersPractice"
  ShowNumbersPracticeClock = new util.Clock();
  fixation_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  pres_text_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text_practice',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RecallPractice"
  RecallPracticeClock = new util.Clock();
  recall_txtPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtPractice',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxPractice = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxPractice',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonPractice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonPractice', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mousePractice = new core.Mouse({
    win: psychoJS.window,
  });
  mousePractice.mouseClock = new util.Clock();
  // Initialize components for Routine "FeedbackPractice"
  FeedbackPracticeClock = new util.Clock();
  feedbac_textPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbac_textPractice',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "StartRealFS"
  StartRealFSClock = new util.Clock();
  praccomplete = new visual.TextStim({
    win: psychoJS.window,
    name: 'praccomplete',
    text: "Practice complete! \n\nYou are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startFSreal = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "selectNumbers"
  selectNumbersClock = new util.Clock();
  // Run 'Begin Experiment' code from selectNumbersFS
  var digitSpan, digitsForTrial, nTrialsFS, correctCount, incorrectCount;
  
  //nTrialsFS = 0;
  // Initialize components for Routine "ShowNumbers"
  ShowNumbersClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  presentation_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentation_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
  recall_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txt',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_button', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "FStoBStransition"
  FStoBStransitionClock = new util.Clock();
  roundTransition = new visual.TextStim({
    win: psychoJS.window,
    name: 'roundTransition',
    text: 'The first round of the letter task is complete!\n\nPress "enter" to continue to the last round.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  moveToBS = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "InstructionsBS"
  InstructionsBSClock = new util.Clock();
  BSGenInsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'BSGenInsText',
    text: 'The practice for the backwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 2 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the REVERSE order they were presented on the screen. \n\nFor example, if the numbers presented are 6 then 2, your response should be 26.\n\nPlease DO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startBSprac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "showNumbersPracticeBS"
  showNumbersPracticeBSClock = new util.Clock();
  fixation_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  pres_text_practice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text_practice_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "recallPracticeBS"
  recallPracticeBSClock = new util.Clock();
  recall_txtPractice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtPractice_2',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxPractice_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxPractice_2',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonPractice_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonPractice_2', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mousePractice_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mousePractice_2.mouseClock = new util.Clock();
  // Initialize components for Routine "feedbackPracticeBS"
  feedbackPracticeBSClock = new util.Clock();
  feedbac_textPractice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbac_textPractice_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "startRealBS"
  startRealBSClock = new util.Clock();
  praccompleteBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'praccompleteBS',
    text: "Practice complete!\n\nYou are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startBSreal = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "selectNumbersBS"
  selectNumbersBSClock = new util.Clock();
  // Run 'Begin Experiment' code from selectNumbersBScode
  var nTrialsBS
  
  //nTrialsBS = 0;
  // Initialize components for Routine "showNumbersBS"
  showNumbersBSClock = new util.Clock();
  fixationBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationBS',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  presentation_textBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentation_textBS',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: letterTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "RecallBS"
  RecallBSClock = new util.Clock();
  recall_txtBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txtBS',
    text: 'Recall',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  textboxBS = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxBS',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: letterTextHeight,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  cont_buttonBS = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cont_buttonBS', units : undefined, 
    image : 'continue.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.4)], size : [0.3, 0.07],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouseBS = new core.Mouse({
    win: psychoJS.window,
  });
  mouseBS.mouseClock = new util.Clock();
  // Initialize components for Routine "FeedbackBS"
  FeedbackBSClock = new util.Clock();
  feedback_textBS = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_textBS',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "END"
  ENDClock = new util.Clock();
  ThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankYou',
    text: 'Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to Qualtrics.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var settingUpComponents;
function settingUpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'settingUp' ---
    t = 0;
    settingUpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    settingUpComponents = [];
    
    for (const thisComponent of settingUpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function settingUpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'settingUp' ---
    // get current time
    t = settingUpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of settingUpComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var initITIstatic;
var initITIdynamic;
function settingUpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'settingUp' ---
    for (const thisComponent of settingUpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    function shuffle(array) {
      let currentIndex = array.length,  randomIndex;
    
      // While there remain elements to shuffle.
      while (currentIndex != 0) {
    
        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
    
        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex], array[currentIndex]];
      }
    
      return array;
    }
    
    // initialize ITIs
    initITIstatic = Array(25).fill([1, 1.5]).flat();
    initITIdynamic = Array(60).fill([1, 1.5]).flat();
    
    // shuffle the ITIs using the function above
    initITIstatic = shuffle(initITIstatic);
    initITIdynamic = shuffle(initITIdynamic);
    
    // save the ITIs
    psychoJS.experiment.addData('initITIstatic', initITIstatic)
    psychoJS.experiment.addData('initITIdynamic', initITIdynamic)
    
    // the Routine "settingUp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _inst1_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    inst1.keys = undefined;
    inst1.rt = undefined;
    _inst1_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(Instructions);
    instructionsComponents.push(inst1);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instructions* updates
    if (t >= 0.0 && Instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions.tStart = t;  // (not accounting for frame time here)
      Instructions.frameNStart = frameN;  // exact frame index
      
      Instructions.setAutoDraw(true);
    }

    
    // *inst1* updates
    if (t >= 2 && inst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1.tStart = t;  // (not accounting for frame time here)
      inst1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { inst1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { inst1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { inst1.clearEvents(); });
    }

    if (inst1.status === PsychoJS.Status.STARTED) {
      let theseKeys = inst1.getKeys({keyList: ['return'], waitRelease: false});
      _inst1_allKeys = _inst1_allKeys.concat(theseKeys);
      if (_inst1_allKeys.length > 0) {
        inst1.keys = _inst1_allKeys[_inst1_allKeys.length - 1].name;  // just the last key pressed
        inst1.rt = _inst1_allKeys[_inst1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(inst1.corr, level);
    }
    psychoJS.experiment.addData('inst1.keys', inst1.keys);
    if (typeof inst1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('inst1.rt', inst1.rt);
        routineTimer.reset();
        }
    
    inst1.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startPracResp_allKeys;
var pracStartComponents;
function pracStartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracStart' ---
    t = 0;
    pracStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startPracResp.keys = undefined;
    startPracResp.rt = undefined;
    _startPracResp_allKeys = [];
    // keep track of which components have finished
    pracStartComponents = [];
    pracStartComponents.push(startPract);
    pracStartComponents.push(startPracResp);
    
    for (const thisComponent of pracStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pracStartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracStart' ---
    // get current time
    t = pracStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startPract* updates
    if (t >= 0.0 && startPract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startPract.tStart = t;  // (not accounting for frame time here)
      startPract.frameNStart = frameN;  // exact frame index
      
      startPract.setAutoDraw(true);
    }

    
    // *startPracResp* updates
    if (t >= 2 && startPracResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startPracResp.tStart = t;  // (not accounting for frame time here)
      startPracResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startPracResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startPracResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startPracResp.clearEvents(); });
    }

    if (startPracResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = startPracResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _startPracResp_allKeys = _startPracResp_allKeys.concat(theseKeys);
      if (_startPracResp_allKeys.length > 0) {
        startPracResp.keys = _startPracResp_allKeys[_startPracResp_allKeys.length - 1].name;  // just the last key pressed
        startPracResp.rt = _startPracResp_allKeys[_startPracResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pracStartComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracStart' ---
    for (const thisComponent of pracStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startPracResp.corr, level);
    }
    psychoJS.experiment.addData('startPracResp.keys', startPracResp.keys);
    if (typeof startPracResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startPracResp.rt', startPracResp.rt);
        routineTimer.reset();
        }
    
    startPracResp.stop();
    // the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cgtRDMPractice.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(practiceTaskRoutineBegin(snapshot));
      trialsLoopScheduler.add(practiceTaskRoutineEachFrame());
      trialsLoopScheduler.add(practiceTaskRoutineEnd(snapshot));
      trialsLoopScheduler.add(isiPracRoutineBegin(snapshot));
      trialsLoopScheduler.add(isiPracRoutineEachFrame());
      trialsLoopScheduler.add(isiPracRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(itiPrac_2RoutineBegin(snapshot));
      trialsLoopScheduler.add(itiPrac_2RoutineEachFrame());
      trialsLoopScheduler.add(itiPrac_2RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var staticRDM;
function staticRDMLoopBegin(staticRDMLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    staticRDM = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'CGT-choice-set.csv',
      seed: undefined, name: 'staticRDM'
    });
    psychoJS.experiment.addLoop(staticRDM); // add the loop to the experiment
    currentLoop = staticRDM;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStaticRDM of staticRDM) {
      snapshot = staticRDM.getSnapshot();
      staticRDMLoopScheduler.add(importConditions(snapshot));
      staticRDMLoopScheduler.add(choiceWindowRoutineBegin(snapshot));
      staticRDMLoopScheduler.add(choiceWindowRoutineEachFrame());
      staticRDMLoopScheduler.add(choiceWindowRoutineEnd(snapshot));
      staticRDMLoopScheduler.add(isiRoutineBegin(snapshot));
      staticRDMLoopScheduler.add(isiRoutineEachFrame());
      staticRDMLoopScheduler.add(isiRoutineEnd(snapshot));
      staticRDMLoopScheduler.add(showOutcomeRoutineBegin(snapshot));
      staticRDMLoopScheduler.add(showOutcomeRoutineEachFrame());
      staticRDMLoopScheduler.add(showOutcomeRoutineEnd(snapshot));
      staticRDMLoopScheduler.add(itiRoutineBegin(snapshot));
      staticRDMLoopScheduler.add(itiRoutineEachFrame());
      staticRDMLoopScheduler.add(itiRoutineEnd(snapshot));
      staticRDMLoopScheduler.add(staticRDMLoopEndIteration(staticRDMLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function staticRDMLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(staticRDM);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function staticRDMLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(computeEstimatesRoutineBegin(snapshot));
      trials_2LoopScheduler.add(computeEstimatesRoutineEachFrame());
      trials_2LoopScheduler.add(computeEstimatesRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var dynamicRDM;
function dynamicRDMLoopBegin(dynamicRDMLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    dynamicRDM = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: dynamicChoicesetResourceName,
      seed: undefined, name: 'dynamicRDM'
    });
    psychoJS.experiment.addLoop(dynamicRDM); // add the loop to the experiment
    currentLoop = dynamicRDM;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDynamicRDM of dynamicRDM) {
      snapshot = dynamicRDM.getSnapshot();
      dynamicRDMLoopScheduler.add(importConditions(snapshot));
      dynamicRDMLoopScheduler.add(choiceWindowRoutineBegin(snapshot));
      dynamicRDMLoopScheduler.add(choiceWindowRoutineEachFrame());
      dynamicRDMLoopScheduler.add(choiceWindowRoutineEnd(snapshot));
      dynamicRDMLoopScheduler.add(isiRoutineBegin(snapshot));
      dynamicRDMLoopScheduler.add(isiRoutineEachFrame());
      dynamicRDMLoopScheduler.add(isiRoutineEnd(snapshot));
      dynamicRDMLoopScheduler.add(showOutcomeDynamicRoutineBegin(snapshot));
      dynamicRDMLoopScheduler.add(showOutcomeDynamicRoutineEachFrame());
      dynamicRDMLoopScheduler.add(showOutcomeDynamicRoutineEnd(snapshot));
      dynamicRDMLoopScheduler.add(itiRoutineBegin(snapshot));
      dynamicRDMLoopScheduler.add(itiRoutineEachFrame());
      dynamicRDMLoopScheduler.add(itiRoutineEnd(snapshot));
      dynamicRDMLoopScheduler.add(dynamicRDMLoopEndIteration(dynamicRDMLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function dynamicRDMLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(dynamicRDM);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function dynamicRDMLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialFSPractice;
function trialFSPracticeLoopBegin(trialFSPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialFSPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanPractice.xlsx',
      seed: undefined, name: 'trialFSPractice'
    });
    psychoJS.experiment.addLoop(trialFSPractice); // add the loop to the experiment
    currentLoop = trialFSPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialFSPractice of trialFSPractice) {
      snapshot = trialFSPractice.getSnapshot();
      trialFSPracticeLoopScheduler.add(importConditions(snapshot));
      const DigitLoopPracticeLoopScheduler = new Scheduler(psychoJS);
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopBegin(DigitLoopPracticeLoopScheduler, snapshot));
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopScheduler);
      trialFSPracticeLoopScheduler.add(DigitLoopPracticeLoopEnd);
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineBegin(snapshot));
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineEachFrame());
      trialFSPracticeLoopScheduler.add(RecallPracticeRoutineEnd(snapshot));
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineBegin(snapshot));
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineEachFrame());
      trialFSPracticeLoopScheduler.add(FeedbackPracticeRoutineEnd(snapshot));
      trialFSPracticeLoopScheduler.add(trialFSPracticeLoopEndIteration(trialFSPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var DigitLoopPractice;
function DigitLoopPracticeLoopBegin(DigitLoopPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    DigitLoopPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'DigitLoopPractice'
    });
    psychoJS.experiment.addLoop(DigitLoopPractice); // add the loop to the experiment
    currentLoop = DigitLoopPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopPractice of DigitLoopPractice) {
      snapshot = DigitLoopPractice.getSnapshot();
      DigitLoopPracticeLoopScheduler.add(importConditions(snapshot));
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineBegin(snapshot));
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineEachFrame());
      DigitLoopPracticeLoopScheduler.add(ShowNumbersPracticeRoutineEnd(snapshot));
      DigitLoopPracticeLoopScheduler.add(DigitLoopPracticeLoopEndIteration(DigitLoopPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function DigitLoopPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(DigitLoopPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function DigitLoopPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialFSPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialFSPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialFSPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsFS;
function trialsFSLoopBegin(trialsFSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsFS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanTrialNumber.xlsx',
      seed: undefined, name: 'trialsFS'
    });
    psychoJS.experiment.addLoop(trialsFS); // add the loop to the experiment
    currentLoop = trialsFS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsFS of trialsFS) {
      snapshot = trialsFS.getSnapshot();
      trialsFSLoopScheduler.add(importConditions(snapshot));
      trialsFSLoopScheduler.add(selectNumbersRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(selectNumbersRoutineEachFrame());
      trialsFSLoopScheduler.add(selectNumbersRoutineEnd(snapshot));
      const digitLoopLoopScheduler = new Scheduler(psychoJS);
      trialsFSLoopScheduler.add(digitLoopLoopBegin(digitLoopLoopScheduler, snapshot));
      trialsFSLoopScheduler.add(digitLoopLoopScheduler);
      trialsFSLoopScheduler.add(digitLoopLoopEnd);
      trialsFSLoopScheduler.add(RecallRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(RecallRoutineEachFrame());
      trialsFSLoopScheduler.add(RecallRoutineEnd(snapshot));
      trialsFSLoopScheduler.add(FeedbackRoutineBegin(snapshot));
      trialsFSLoopScheduler.add(FeedbackRoutineEachFrame());
      trialsFSLoopScheduler.add(FeedbackRoutineEnd(snapshot));
      trialsFSLoopScheduler.add(trialsFSLoopEndIteration(trialsFSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoop;
function digitLoopLoopBegin(digitLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoop'
    });
    psychoJS.experiment.addLoop(digitLoop); // add the loop to the experiment
    currentLoop = digitLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoop of digitLoop) {
      snapshot = digitLoop.getSnapshot();
      digitLoopLoopScheduler.add(importConditions(snapshot));
      digitLoopLoopScheduler.add(ShowNumbersRoutineBegin(snapshot));
      digitLoopLoopScheduler.add(ShowNumbersRoutineEachFrame());
      digitLoopLoopScheduler.add(ShowNumbersRoutineEnd(snapshot));
      digitLoopLoopScheduler.add(digitLoopLoopEndIteration(digitLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsFSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsFS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsFSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsPracticeBS;
function trialsPracticeBSLoopBegin(trialsPracticeBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPracticeBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanPractice.xlsx',
      seed: undefined, name: 'trialsPracticeBS'
    });
    psychoJS.experiment.addLoop(trialsPracticeBS); // add the loop to the experiment
    currentLoop = trialsPracticeBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsPracticeBS of trialsPracticeBS) {
      snapshot = trialsPracticeBS.getSnapshot();
      trialsPracticeBSLoopScheduler.add(importConditions(snapshot));
      const digitLoopPracticeBSLoopScheduler = new Scheduler(psychoJS);
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopBegin(digitLoopPracticeBSLoopScheduler, snapshot));
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopScheduler);
      trialsPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopEnd);
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineBegin(snapshot));
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineEachFrame());
      trialsPracticeBSLoopScheduler.add(recallPracticeBSRoutineEnd(snapshot));
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineBegin(snapshot));
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineEachFrame());
      trialsPracticeBSLoopScheduler.add(feedbackPracticeBSRoutineEnd(snapshot));
      trialsPracticeBSLoopScheduler.add(trialsPracticeBSLoopEndIteration(trialsPracticeBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoopPracticeBS;
function digitLoopPracticeBSLoopBegin(digitLoopPracticeBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoopPracticeBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoopPracticeBS'
    });
    psychoJS.experiment.addLoop(digitLoopPracticeBS); // add the loop to the experiment
    currentLoop = digitLoopPracticeBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopPracticeBS of digitLoopPracticeBS) {
      snapshot = digitLoopPracticeBS.getSnapshot();
      digitLoopPracticeBSLoopScheduler.add(importConditions(snapshot));
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineBegin(snapshot));
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineEachFrame());
      digitLoopPracticeBSLoopScheduler.add(showNumbersPracticeBSRoutineEnd(snapshot));
      digitLoopPracticeBSLoopScheduler.add(digitLoopPracticeBSLoopEndIteration(digitLoopPracticeBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopPracticeBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoopPracticeBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopPracticeBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsPracticeBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsPracticeBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsPracticeBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialsBS;
function trialsBSLoopBegin(trialsBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'digitSpanTrialNumber.xlsx',
      seed: undefined, name: 'trialsBS'
    });
    psychoJS.experiment.addLoop(trialsBS); // add the loop to the experiment
    currentLoop = trialsBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsBS of trialsBS) {
      snapshot = trialsBS.getSnapshot();
      trialsBSLoopScheduler.add(importConditions(snapshot));
      trialsBSLoopScheduler.add(selectNumbersBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(selectNumbersBSRoutineEachFrame());
      trialsBSLoopScheduler.add(selectNumbersBSRoutineEnd(snapshot));
      const digitLoopBSLoopScheduler = new Scheduler(psychoJS);
      trialsBSLoopScheduler.add(digitLoopBSLoopBegin(digitLoopBSLoopScheduler, snapshot));
      trialsBSLoopScheduler.add(digitLoopBSLoopScheduler);
      trialsBSLoopScheduler.add(digitLoopBSLoopEnd);
      trialsBSLoopScheduler.add(RecallBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(RecallBSRoutineEachFrame());
      trialsBSLoopScheduler.add(RecallBSRoutineEnd(snapshot));
      trialsBSLoopScheduler.add(FeedbackBSRoutineBegin(snapshot));
      trialsBSLoopScheduler.add(FeedbackBSRoutineEachFrame());
      trialsBSLoopScheduler.add(FeedbackBSRoutineEnd(snapshot));
      trialsBSLoopScheduler.add(trialsBSLoopEndIteration(trialsBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoopBS;
function digitLoopBSLoopBegin(digitLoopBSLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoopBS = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoopBS'
    });
    psychoJS.experiment.addLoop(digitLoopBS); // add the loop to the experiment
    currentLoop = digitLoopBS;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoopBS of digitLoopBS) {
      snapshot = digitLoopBS.getSnapshot();
      digitLoopBSLoopScheduler.add(importConditions(snapshot));
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineBegin(snapshot));
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineEachFrame());
      digitLoopBSLoopScheduler.add(showNumbersBSRoutineEnd(snapshot));
      digitLoopBSLoopScheduler.add(digitLoopBSLoopEndIteration(digitLoopBSLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoopBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(digitLoopBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function digitLoopBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsBSLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsBS);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsBSLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var targetPos;
var lossLoc;
var gainLoc;
var safeLoc;
var pracLossRounded;
var pracGainRounded;
var pracSafeRounded;
var _choice1_allKeys;
var practiceTaskComponents;
function practiceTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceTask' ---
    t = 0;
    practiceTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from randLoc
    var pracLossRounded, pracGainRounded, pracSafeRounded
    
    if ((loc === 1)) {
        targetPos = [(- 0.4), 0];
    } else {
        targetPos = [0.4, 0];
    }
    if ((loc === 1)) {
        lossLoc = [(- 0.4), (- 0.1)];
        gainLoc = [(- 0.4), 0.1];
        safeLoc = [0.4, 0];
    } else {
        lossLoc = [0.4, (- 0.1)];
        gainLoc = [0.4, 0.1];
        safeLoc = [(- 0.4), 0];
    }
    
    
    //pracLossRounded = riskyLoss
    //pracGainRounded = riskyGain
    //pracSafeRounded = alternative
    
    /*
     function roundToTwo(num) {    
            return +(Math.round(num + "e+2")  + "e-2");
     }
    */
    
    pracLossRounded = `$${Math.round(riskyLoss)}`;
    //pracGainRounded = `$${roundToTwo(riskyGain*100)/100}`;
    //pracSafeRounded = `$${roundToTwo(alternative*100)/100}`;
    
    pracGainRounded = `$${Math.round(riskyGain*100)/100}`;
    pracSafeRounded = `$${Math.round(alternative*100)/100}`;
    
    //console.log(pracLossRounded)
    //console.log(pracGainRounded)
    //console.log(pracSafeRounded)
    circleRight.setFillColor(new util.Color([1, 1, 1]));
    circleRight.setLineColor(new util.Color([1, 1, 1]));
    lineLeft.setPos(targetPos);
    lossTxt.setPos(lossLoc);
    lossTxt.setText(pracLossRounded);
    gainTxt.setPos(gainLoc);
    gainTxt.setText(pracGainRounded);
    safeTxt.setPos(safeLoc);
    safeTxt.setText(pracSafeRounded);
    choice1.keys = undefined;
    choice1.rt = undefined;
    _choice1_allKeys = [];
    // keep track of which components have finished
    practiceTaskComponents = [];
    practiceTaskComponents.push(circleLeft);
    practiceTaskComponents.push(circleRight);
    practiceTaskComponents.push(lineLeft);
    practiceTaskComponents.push(orText);
    practiceTaskComponents.push(lossTxt);
    practiceTaskComponents.push(gainTxt);
    practiceTaskComponents.push(safeTxt);
    practiceTaskComponents.push(vLeft);
    practiceTaskComponents.push(nRight);
    practiceTaskComponents.push(choice1);
    
    for (const thisComponent of practiceTaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practiceTaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceTask' ---
    // get current time
    t = practiceTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *circleLeft* updates
    if (t >= 0 && circleLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      circleLeft.tStart = t;  // (not accounting for frame time here)
      circleLeft.frameNStart = frameN;  // exact frame index
      
      circleLeft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (circleLeft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      circleLeft.setAutoDraw(false);
    }
    
    // *circleRight* updates
    if (t >= 0.0 && circleRight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      circleRight.tStart = t;  // (not accounting for frame time here)
      circleRight.frameNStart = frameN;  // exact frame index
      
      circleRight.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (circleRight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      circleRight.setAutoDraw(false);
    }
    
    // *lineLeft* updates
    if (t >= 0.0 && lineLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lineLeft.tStart = t;  // (not accounting for frame time here)
      lineLeft.frameNStart = frameN;  // exact frame index
      
      lineLeft.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lineLeft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lineLeft.setAutoDraw(false);
    }
    
    // *orText* updates
    if (t >= 0.0 && orText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      orText.tStart = t;  // (not accounting for frame time here)
      orText.frameNStart = frameN;  // exact frame index
      
      orText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (orText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      orText.setAutoDraw(false);
    }
    
    // *lossTxt* updates
    if (t >= 0.0 && lossTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lossTxt.tStart = t;  // (not accounting for frame time here)
      lossTxt.frameNStart = frameN;  // exact frame index
      
      lossTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lossTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lossTxt.setAutoDraw(false);
    }
    
    // *gainTxt* updates
    if (t >= 0.0 && gainTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gainTxt.tStart = t;  // (not accounting for frame time here)
      gainTxt.frameNStart = frameN;  // exact frame index
      
      gainTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (gainTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      gainTxt.setAutoDraw(false);
    }
    
    // *safeTxt* updates
    if (t >= 0.0 && safeTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      safeTxt.tStart = t;  // (not accounting for frame time here)
      safeTxt.frameNStart = frameN;  // exact frame index
      
      safeTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (safeTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      safeTxt.setAutoDraw(false);
    }
    
    // *vLeft* updates
    if (t >= 0 && vLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vLeft.tStart = t;  // (not accounting for frame time here)
      vLeft.frameNStart = frameN;  // exact frame index
      
      vLeft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (vLeft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      vLeft.setAutoDraw(false);
    }
    
    // *nRight* updates
    if (t >= 0 && nRight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nRight.tStart = t;  // (not accounting for frame time here)
      nRight.frameNStart = frameN;  // exact frame index
      
      nRight.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (nRight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nRight.setAutoDraw(false);
    }
    
    // *choice1* updates
    if (t >= 0 && choice1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice1.tStart = t;  // (not accounting for frame time here)
      choice1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choice1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choice1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choice1.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice1.status = PsychoJS.Status.FINISHED;
  }

    if (choice1.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice1.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _choice1_allKeys = _choice1_allKeys.concat(theseKeys);
      if (_choice1_allKeys.length > 0) {
        choice1.keys = _choice1_allKeys[_choice1_allKeys.length - 1].name;  // just the last key pressed
        choice1.rt = _choice1_allKeys[_choice1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceTaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceTaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceTask' ---
    for (const thisComponent of practiceTaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(choice1.corr, level);
    }
    psychoJS.experiment.addData('choice1.keys', choice1.keys);
    if (typeof choice1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice1.rt', choice1.rt);
        routineTimer.reset();
        }
    
    choice1.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var isiPracComponents;
function isiPracRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'isiPrac' ---
    t = 0;
    isiPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    isiPracComponents = [];
    isiPracComponents.push(isiText);
    
    for (const thisComponent of isiPracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function isiPracRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'isiPrac' ---
    // get current time
    t = isiPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *isiText* updates
    if (t >= 0.0 && isiText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isiText.tStart = t;  // (not accounting for frame time here)
      isiText.frameNStart = frameN;  // exact frame index
      
      isiText.setAutoDraw(true);
    }

    frameRemains = 0.0 + isi - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isiText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isiText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of isiPracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function isiPracRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'isiPrac' ---
    for (const thisComponent of isiPracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "isiPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var outcome;
var extraITI;
var pracFeedbackRounded;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeFeedback
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (choice1.keys === undefined){
        outcome = " ";
        noRespLoc = [0,0];
        ocLoc = [5,5];
        ocGambleLoc = [5,5];
        ocSafeLoc = [5,5];
        hideGamLoc = [5,5];
        extraITI = 0;
    }else if(choice1.keys =='v' && loc ==1) {
        outcome = random_item([riskyGain, riskyLoss])
        extraITI = 4-choice1.rt
        if(outcome == riskyGain){
            ocLoc = [-.4,.1];
            ocGambleLoc = [-.4,0];
            ocSafeLoc = [5,5];
            noRespLoc = [5,5];
            hideGamLoc = [-.4,-.125];
        } else if (outcome ==riskyLoss){
            ocLoc = [-.4,-.1];
            ocGambleLoc = [-.4,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [-.4,.125];
            noRespLoc = [5,5];
        }
    } else if(choice1.keys == 'v' && loc ==2){
        extraITI = 4-choice1.rt
        outcome = alternative
        ocLoc = [-.4,0];
        ocGambleLoc = [5,5];
        ocSafeLoc = ocLoc;
        hideGamLoc = ocGambleLoc;
        noRespLoc = [5,5];
    } else if (choice1.keys=='n' && loc ==1){
        extraITI = 4-choice1.rt
        outcome = alternative
        ocLoc = [.4,0];
        ocGambleLoc = [5,5];
        ocSafeLoc = ocLoc;
        hideGamLoc = ocGambleLoc;
        noRespLoc = [5,5];
    } else if (choice1.keys =='n' && loc ==2){
        outcome = random_item([riskyGain, riskyLoss]);
        extraITI = 4-choice1.rt
        if (outcome == riskyGain){
            ocLoc = [.4,.1];
            ocGambleLoc = [.4,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [.4,-.125];
            noRespLoc = [5,5];
        } else if (outcome == riskyLoss){
            ocLoc = [.4,-.1];
            ocGambleLoc = [.4,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [.4,.125];
            noRespLoc = [5,5];
        }
    }
    
    /*
     function roundToTwo(num) {    
            return +(Math.round(num + "e+2")  + "e-2");
     }
    */
    
    if (outcome == riskyLoss){
        //pracFeedbackRounded = $${Math.round(outcome)}
        pracFeedbackRounded = "$" + Math.round(outcome)
    } else {
        //pracFeedbackRounded = $${Math.round(outcome*100)/100};
        //pracFeedbackRounded = "$" + Math.round(outcome*100)/100
        pracFeedbackRounded = "$" + (Math.round(outcome*100)/100).toFixed(2)
    }
    
    //console.log("rounded feedback:",pracFeedbackRounded)
    //console.log("extra ITI", extraITI)
    //console.log("rt",choice1.rt)
    //console.log("iti", iti)
    //console.log("combined itis", extraITI + iti)
    
    noRespTxt.setPos(noRespLoc);
    ocGamble.setPos(ocGambleLoc);
    ocSafe.setPos(ocSafeLoc);
    outcomeText.setColor(new util.Color('black'));
    outcomeText.setPos(ocLoc);
    outcomeText.setText(pracFeedbackRounded);
    hideGamble.setPos(hideGamLoc);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(noRespTxt);
    feedbackComponents.push(ocGamble);
    feedbackComponents.push(ocSafe);
    feedbackComponents.push(outcomeText);
    feedbackComponents.push(hideGamble);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *noRespTxt* updates
    if (t >= 0.0 && noRespTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noRespTxt.tStart = t;  // (not accounting for frame time here)
      noRespTxt.frameNStart = frameN;  // exact frame index
      
      noRespTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noRespTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noRespTxt.setAutoDraw(false);
    }
    
    // *ocGamble* updates
    if (t >= 0.0 && ocGamble.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocGamble.tStart = t;  // (not accounting for frame time here)
      ocGamble.frameNStart = frameN;  // exact frame index
      
      ocGamble.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocGamble.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocGamble.setAutoDraw(false);
    }
    
    // *ocSafe* updates
    if (t >= 0.0 && ocSafe.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocSafe.tStart = t;  // (not accounting for frame time here)
      ocSafe.frameNStart = frameN;  // exact frame index
      
      ocSafe.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocSafe.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocSafe.setAutoDraw(false);
    }
    
    // *outcomeText* updates
    if (t >= 0.0 && outcomeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcomeText.tStart = t;  // (not accounting for frame time here)
      outcomeText.frameNStart = frameN;  // exact frame index
      
      outcomeText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outcomeText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outcomeText.setAutoDraw(false);
    }
    
    // *hideGamble* updates
    if (t >= 0.0 && hideGamble.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hideGamble.tStart = t;  // (not accounting for frame time here)
      hideGamble.frameNStart = frameN;  // exact frame index
      
      hideGamble.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (hideGamble.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      hideGamble.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from codeFeedback
    psychoJS.experiment.addData('outcome', outcome)
    psychoJS.experiment.addData('extraITI', extraITI)
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var itiPrac_2Components;
function itiPrac_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'itiPrac_2' ---
    t = 0;
    itiPrac_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    itiPrac_2Components = [];
    itiPrac_2Components.push(itiText);
    
    for (const thisComponent of itiPrac_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function itiPrac_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'itiPrac_2' ---
    // get current time
    t = itiPrac_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *itiText* updates
    if (t >= 0.0 && itiText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      itiText.tStart = t;  // (not accounting for frame time here)
      itiText.frameNStart = frameN;  // exact frame index
      
      itiText.setAutoDraw(true);
    }

    frameRemains = 0.0 + (iti + extraITI) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (itiText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      itiText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of itiPrac_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiPrac_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'itiPrac_2' ---
    for (const thisComponent of itiPrac_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "itiPrac_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _postPractResp_allKeys;
var postPracComponents;
function postPracRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'postPrac' ---
    t = 0;
    postPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    postPractResp.keys = undefined;
    postPractResp.rt = undefined;
    _postPractResp_allKeys = [];
    // keep track of which components have finished
    postPracComponents = [];
    postPracComponents.push(postPracText);
    postPracComponents.push(postPractResp);
    
    for (const thisComponent of postPracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function postPracRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'postPrac' ---
    // get current time
    t = postPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *postPracText* updates
    if (t >= 0.0 && postPracText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postPracText.tStart = t;  // (not accounting for frame time here)
      postPracText.frameNStart = frameN;  // exact frame index
      
      postPracText.setAutoDraw(true);
    }

    
    // *postPractResp* updates
    if (t >= 0.0 && postPractResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postPractResp.tStart = t;  // (not accounting for frame time here)
      postPractResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { postPractResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { postPractResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { postPractResp.clearEvents(); });
    }

    if (postPractResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = postPractResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _postPractResp_allKeys = _postPractResp_allKeys.concat(theseKeys);
      if (_postPractResp_allKeys.length > 0) {
        postPractResp.keys = _postPractResp_allKeys[_postPractResp_allKeys.length - 1].name;  // just the last key pressed
        postPractResp.rt = _postPractResp_allKeys[_postPractResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of postPracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function postPracRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'postPrac' ---
    for (const thisComponent of postPracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(postPractResp.corr, level);
    }
    psychoJS.experiment.addData('postPractResp.keys', postPractResp.keys);
    if (typeof postPractResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('postPractResp.rt', postPractResp.rt);
        routineTimer.reset();
        }
    
    postPractResp.stop();
    // the Routine "postPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var realloc;
var lossRounded;
var gainRounded;
var safeRounded;
var _realChoice_allKeys;
var choiceWindowComponents;
function choiceWindowRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'choiceWindow' ---
    t = 0;
    choiceWindowClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from randLoc_2
    var gainLoc, gainRounded, lossLoc, lossRounded, safeLoc, safeRounded, targetPos;
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    realloc = random_item([1, 2]);
    
    if ((realloc === 1)) {
        targetPos = [(- 0.4), 0];
    } else {
        targetPos = [0.4, 0];
    }
    if ((realloc === 1)) {
        lossLoc = [(- 0.4), (- 0.1)];
        gainLoc = [(- 0.4), 0.1];
        safeLoc = [0.4, 0];
    } else {
        lossLoc = [0.4, (- 0.1)];
        gainLoc = [0.4, 0.1];
        safeLoc = [(- 0.4), 0];
    }
    
    //console.log(realloc)
    
    /*
     function roundToTwo(num) {    
            return +(Math.round(num + "e+2")  + "e-2");
     }
    */
    
    lossRounded = `$${Math.round(riskyoption2)}`;
    gainRounded = `$${(Math.round(riskyoption1*100)/100).toFixed(2)}`;
    safeRounded = `$${(Math.round(safeoption*100)/100).toFixed(2)}`;
    
    //lossRounded = `$${Math.round(riskyoption2)}`;
    //gainRounded = `$${Math.round(riskyoption1*100)/100}`;
    //safeRounded = `$${Math.round(safeoption*100)/100}`;
    
    circleRightReal.setFillColor(new util.Color([1, 1, 1]));
    circleRightReal.setLineColor(new util.Color([1, 1, 1]));
    lineLeftReal.setPos(targetPos);
    lossTxtReal.setPos(lossLoc);
    lossTxtReal.setText(lossRounded);
    gainTxtReal.setPos(gainLoc);
    gainTxtReal.setText(gainRounded);
    safeTxtReal.setPos(safeLoc);
    safeTxtReal.setText(safeRounded);
    realChoice.keys = undefined;
    realChoice.rt = undefined;
    _realChoice_allKeys = [];
    // keep track of which components have finished
    choiceWindowComponents = [];
    choiceWindowComponents.push(circleLeftReal);
    choiceWindowComponents.push(circleRightReal);
    choiceWindowComponents.push(lineLeftReal);
    choiceWindowComponents.push(orTextReal);
    choiceWindowComponents.push(lossTxtReal);
    choiceWindowComponents.push(gainTxtReal);
    choiceWindowComponents.push(safeTxtReal);
    choiceWindowComponents.push(vLeftReal);
    choiceWindowComponents.push(nRightReal);
    choiceWindowComponents.push(realChoice);
    
    for (const thisComponent of choiceWindowComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function choiceWindowRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'choiceWindow' ---
    // get current time
    t = choiceWindowClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *circleLeftReal* updates
    if (t >= 0 && circleLeftReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      circleLeftReal.tStart = t;  // (not accounting for frame time here)
      circleLeftReal.frameNStart = frameN;  // exact frame index
      
      circleLeftReal.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (circleLeftReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      circleLeftReal.setAutoDraw(false);
    }
    
    // *circleRightReal* updates
    if (t >= 0.0 && circleRightReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      circleRightReal.tStart = t;  // (not accounting for frame time here)
      circleRightReal.frameNStart = frameN;  // exact frame index
      
      circleRightReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (circleRightReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      circleRightReal.setAutoDraw(false);
    }
    
    // *lineLeftReal* updates
    if (t >= 0.0 && lineLeftReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lineLeftReal.tStart = t;  // (not accounting for frame time here)
      lineLeftReal.frameNStart = frameN;  // exact frame index
      
      lineLeftReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lineLeftReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lineLeftReal.setAutoDraw(false);
    }
    
    // *orTextReal* updates
    if (t >= 0.0 && orTextReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      orTextReal.tStart = t;  // (not accounting for frame time here)
      orTextReal.frameNStart = frameN;  // exact frame index
      
      orTextReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (orTextReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      orTextReal.setAutoDraw(false);
    }
    
    // *lossTxtReal* updates
    if (t >= 0.0 && lossTxtReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lossTxtReal.tStart = t;  // (not accounting for frame time here)
      lossTxtReal.frameNStart = frameN;  // exact frame index
      
      lossTxtReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lossTxtReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lossTxtReal.setAutoDraw(false);
    }
    
    // *gainTxtReal* updates
    if (t >= 0.0 && gainTxtReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gainTxtReal.tStart = t;  // (not accounting for frame time here)
      gainTxtReal.frameNStart = frameN;  // exact frame index
      
      gainTxtReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (gainTxtReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      gainTxtReal.setAutoDraw(false);
    }
    
    // *safeTxtReal* updates
    if (t >= 0.0 && safeTxtReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      safeTxtReal.tStart = t;  // (not accounting for frame time here)
      safeTxtReal.frameNStart = frameN;  // exact frame index
      
      safeTxtReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (safeTxtReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      safeTxtReal.setAutoDraw(false);
    }
    
    // *vLeftReal* updates
    if (t >= 0 && vLeftReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vLeftReal.tStart = t;  // (not accounting for frame time here)
      vLeftReal.frameNStart = frameN;  // exact frame index
      
      vLeftReal.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (vLeftReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      vLeftReal.setAutoDraw(false);
    }
    
    // *nRightReal* updates
    if (t >= 0 && nRightReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nRightReal.tStart = t;  // (not accounting for frame time here)
      nRightReal.frameNStart = frameN;  // exact frame index
      
      nRightReal.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (nRightReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nRightReal.setAutoDraw(false);
    }
    
    // *realChoice* updates
    if (t >= 0 && realChoice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realChoice.tStart = t;  // (not accounting for frame time here)
      realChoice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { realChoice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { realChoice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { realChoice.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realChoice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realChoice.status = PsychoJS.Status.FINISHED;
  }

    if (realChoice.status === PsychoJS.Status.STARTED) {
      let theseKeys = realChoice.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _realChoice_allKeys = _realChoice_allKeys.concat(theseKeys);
      if (_realChoice_allKeys.length > 0) {
        realChoice.keys = _realChoice_allKeys[_realChoice_allKeys.length - 1].name;  // just the last key pressed
        realChoice.rt = _realChoice_allKeys[_realChoice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of choiceWindowComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choiceWindowRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'choiceWindow' ---
    for (const thisComponent of choiceWindowComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from randLoc_2
    psychoJS.experiment.addData("realloc", realloc);
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(realChoice.corr, level);
    }
    psychoJS.experiment.addData('realChoice.keys', realChoice.keys);
    if (typeof realChoice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('realChoice.rt', realChoice.rt);
        routineTimer.reset();
        }
    
    realChoice.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var isiComponents;
function isiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'isi' ---
    t = 0;
    isiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    isiComponents = [];
    isiComponents.push(isiTextReal);
    
    for (const thisComponent of isiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function isiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'isi' ---
    // get current time
    t = isiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *isiTextReal* updates
    if (t >= 0.0 && isiTextReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isiTextReal.tStart = t;  // (not accounting for frame time here)
      isiTextReal.frameNStart = frameN;  // exact frame index
      
      isiTextReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isiTextReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isiTextReal.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of isiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function isiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'isi' ---
    for (const thisComponent of isiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var outcometmp;
var choicetmp;
var actualITI;
var feedbackRounded;
var showOutcomeComponents;
function showOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showOutcome' ---
    t = 0;
    showOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeFeedbackReal
    var choicetmp, feedbackRounded, outcometmp, outcomes, choices;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (realChoice.keys === undefined) {
        outcometmp = Math.nan;
        choicetmp = Math.nan;
        noRespLoc = [0, 0];
        ocLoc = [5, 5];
        ocGambleLoc = [5, 5];
        ocSafeLoc = [5, 5];
        hideGamLoc = [5, 5];
        extraITI = 0;
    } else if (realChoice.keys === "v" && realloc === 1) {
         outcometmp = random_item([riskyoption1, riskyoption2]);
         choicetmp = 1;
         extraITI = 4-realChoice.rt
         if (outcometmp === riskyoption1) {
              ocLoc = [(- 0.4), 0.1];
              ocGambleLoc = [(- 0.4), 0];
              ocSafeLoc = [5, 5];
              noRespLoc = [5, 5];
              hideGamLoc = [(- 0.4), (- 0.125)];
         } else if (outcometmp === riskyoption2) {
              ocLoc = [(- 0.4), (- 0.1)];
              ocGambleLoc = [(- 0.4), 0];
              ocSafeLoc = [5, 5];
              hideGamLoc = [(- 0.4), 0.125];
              noRespLoc = [5, 5];
         }
     } else if (realChoice.keys === "v" && realloc === 2) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoice.rt
         ocLoc = [(- 0.4), 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
     } else if (realChoice.keys === "n" && realloc === 1) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoice.rt
         ocLoc = [0.4, 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
    } else if (realChoice.keys === "n" && realloc === 2) {
        outcometmp = random_item([riskyoption1, riskyoption2]);
        choicetmp = 1;
        extraITI = 4-realChoice.rt
        if (outcometmp === riskyoption1) {
            ocLoc = [0.4, 0.1];
            ocGambleLoc = [0.4, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.4, (- 0.125)];
            noRespLoc = [5, 5];
        } else if (outcometmp === riskyoption2) {
            ocLoc = [0.4, (- 0.1)];
            ocGambleLoc = [0.4, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.4, 0.125];
            noRespLoc = [5, 5];
        }
    }
    
    actualITI = initITIstatic[staticRDM.thisN] + extraITI
    
    
    if (outcometmp === riskyoption2) {
        feedbackRounded = "$" + Math.round(outcometmp)
    } else {
        feedbackRounded = "$" + (Math.round(outcometmp*100)/100).toFixed(2)
        //feedbackRounded = "$" + Math.round(outcometmp*100)/100
    }
    
    /*
    console.log("outcome rounded:",feedbackRounded)
    console.log("gain:",riskyoption1)
    console.log("loss:",riskyoption2)
    console.log("safe:",safeoption)
    console.log("outcome:", outcometmp)
    console.log("choice:", choicetmp)
    console.log("extra iti:", extraITI)
    console.log("rt", realChoice.rt)
    console.log("actualITI", actualITI)
    console.log("init ITI", initITIstatic[staticRDM.thisN])
    */
    
    psychoJS.experiment.addData("outcomes", outcometmp);
    psychoJS.experiment.addData("choices", choicetmp);
    psychoJS.experiment.addData("extraITI", extraITI);
    psychoJS.experiment.addData("actualITI",actualITI)
    psychoJS.experiment.addData("init ITI", initITIstatic[staticRDM.thisN])
    
    noRespTxtReal.setPos(noRespLoc);
    ocGambleReal.setPos(ocGambleLoc);
    ocSafeReal.setPos(ocSafeLoc);
    outcomeTextReal.setColor(new util.Color('black'));
    outcomeTextReal.setPos(ocLoc);
    outcomeTextReal.setText(feedbackRounded);
    hideGambleReal.setPos(hideGamLoc);
    // keep track of which components have finished
    showOutcomeComponents = [];
    showOutcomeComponents.push(noRespTxtReal);
    showOutcomeComponents.push(ocGambleReal);
    showOutcomeComponents.push(ocSafeReal);
    showOutcomeComponents.push(outcomeTextReal);
    showOutcomeComponents.push(hideGambleReal);
    
    for (const thisComponent of showOutcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showOutcome' ---
    // get current time
    t = showOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *noRespTxtReal* updates
    if (t >= 0.0 && noRespTxtReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noRespTxtReal.tStart = t;  // (not accounting for frame time here)
      noRespTxtReal.frameNStart = frameN;  // exact frame index
      
      noRespTxtReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noRespTxtReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noRespTxtReal.setAutoDraw(false);
    }
    
    // *ocGambleReal* updates
    if (t >= 0.0 && ocGambleReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocGambleReal.tStart = t;  // (not accounting for frame time here)
      ocGambleReal.frameNStart = frameN;  // exact frame index
      
      ocGambleReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocGambleReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocGambleReal.setAutoDraw(false);
    }
    
    // *ocSafeReal* updates
    if (t >= 0.0 && ocSafeReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocSafeReal.tStart = t;  // (not accounting for frame time here)
      ocSafeReal.frameNStart = frameN;  // exact frame index
      
      ocSafeReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocSafeReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocSafeReal.setAutoDraw(false);
    }
    
    // *outcomeTextReal* updates
    if (t >= 0.0 && outcomeTextReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcomeTextReal.tStart = t;  // (not accounting for frame time here)
      outcomeTextReal.frameNStart = frameN;  // exact frame index
      
      outcomeTextReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outcomeTextReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outcomeTextReal.setAutoDraw(false);
    }
    
    // *hideGambleReal* updates
    if (t >= 0.0 && hideGambleReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hideGambleReal.tStart = t;  // (not accounting for frame time here)
      hideGambleReal.frameNStart = frameN;  // exact frame index
      
      hideGambleReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (hideGambleReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      hideGambleReal.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showOutcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showOutcome' ---
    for (const thisComponent of showOutcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from codeFeedbackReal
    outcomes.push(outcometmp);
    choices.push(choicetmp);
    //riskyloss_values.push(riskyLossReal);
    //riskygain_values.push(riskyGainReal);
    //certain_values.push(certain);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var itiComponents;
function itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'iti' ---
    t = 0;
    itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(itiTextReal);
    
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'iti' ---
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *itiTextReal* updates
    if (t >= 0.0 && itiTextReal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      itiTextReal.tStart = t;  // (not accounting for frame time here)
      itiTextReal.frameNStart = frameN;  // exact frame index
      
      itiTextReal.setAutoDraw(true);
    }

    frameRemains = 0.0 + actualITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (itiTextReal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      itiTextReal.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'iti' ---
    for (const thisComponent of itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pulledData;
var finiteData;
var finiteChoices;
var finiteGainVals;
var finiteLossVals;
var finiteSafeVals;
var n_rho_values;
var n_mu_values;
var rmin;
var rmax;
var rstep;
var mmin;
var mmax;
var mstep;
var rho_values;
var mu_values;
var best_nll_value;
var str_bestR;
var str_bestM;
var fname;
var dynamicChoiceSetFilepath;
var computeEstimatesComponents;
function computeEstimatesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'computeEstimates' ---
    t = 0;
    computeEstimatesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from gridSearchCode
    // Access the data from previous RDM task and save only the trials where participant responded on time
    var pulledData, finiteChoices, finiteGainVals, finiteSafeVals, finiteLossVals
    
    pulledData = psychoJS.experiment._trialsData
    //console.log("pulled data:", pulledData)
    finiteData = pulledData.filter((trial) => (trial['realChoice.keys'] =='v' || trial['realChoice.keys'] =='n'));
    //console.log("finite data:", finiteData)
    finiteChoices = finiteData.map((trial) => trial['choices']);
    finiteGainVals = finiteData.map((trial) => trial['riskyoption1']);
    finiteLossVals = finiteData.map((trial) => trial['riskyoption2']);
    finiteSafeVals = finiteData.map((trial) => trial['safeoption']);
    
    /*
    console.log("finite choices:", finiteChoices)
    console.log("finite gain values:", finiteGainVals)
    console.log("finite loss values:", finiteLossVals)
    console.log("finite safe values:",finiteSafeVals)
    */
    
    // Function Definitions
    var fname, dynamicChoiceSetFilename;
    
    function choice_probability(parameters, riskyGv, riskyLv, certv) {
      var rho, mu, nTrials, div, utility_risky_option, utility_safe_option, p
      
      rho = parameters[0];
      mu = parameters[1];
    
      nTrials = riskyGv.length;
    
      div = Math.max.apply(Math,riskyGv) ** rho;
    
      //utility_risky_option = [];
      //utility_safe_option = [];
      p = Array()
      
      for (let i = 0; i < nTrials; i++){
        utility_risky_option = 0.5 * Math.pow(riskyGv[i],rho) + 0.5 * Math.pow(riskyLv[i],rho);
        utility_safe_option = Math.pow(certv[i],rho);
        
        //console.log(utility_risky_option)
        //console.log(utility_safe_option)
    
        p[i] = 1/(1 + Math.exp(-mu/div*(utility_risky_option - utility_safe_option)))
        //p.push(1/(1 + Math.exp(-mu/div*(utility_risky_option - utility_safe_option))))
      }
      //console.log(p)
      return p
    }
    
    
    function negLLprospect_cgt(parameters, riskyGv, riskyLv, certv, choices, likelihood, negloglikelihood) {
      
      var choiceProb, nTrials, nll, likelihood, negloglikelihood
      
      choiceProb = choice_probability(parameters, riskyGv, riskyLv, certv);
      //console.log("choiceprob:", choiceProb)
    
      nTrials = riskyGv.length;
    
      likelihood = Array()
      negloglikelihood = Array()
      
      for (let t = 0; t < nTrials; t++){
        likelihood[t] = choices[t]*choiceProb[t] + (1-choices[t])*(1-choiceProb[t]);
        if (likelihood[t] == 0){
          likelihood[t] = 0.000000000000001;
        }
        negloglikelihood[t] = -Math.log(likelihood[t]);
      }
    
      nll = negloglikelihood.reduce((partialSum, a) => partialSum + a, 0);
    
      return nll
    }
    
    // Grid Search Code
    
    var bestM, bestR, best_nll_value, mmax, mmin, mstep, mu_values, n_mu_values, n_rho_values, nll_new, rho_values, rmax, rmin, rstep;
    
    n_rho_values = 200;
    n_mu_values = 201;
    
    //console.log('n_rho_values', n_rho_values)
    //console.log('n_mu_values', n_mu_values)
    
    rmin = 0.3
    rmax = 2.2
    rstep = (rmax - rmin)/(n_rho_values-1)
    
    /*
    console.log('rmin', rmin)
    console.log('rmax', rmax)
    console.log('rstep', rstep)
    */
    
    mmin = 7
    mmax = 80
    mstep = (mmax - mmin)/(n_mu_values-1)
    
    /*
    console.log('mmin', mmin)
    console.log('mmax', mmax)
    console.log('mstep', mstep)
    */
    
    rho_values = Array()
    mu_values = Array()
    
    for (let r = 0; r < n_rho_values; r++){  
      rho_values[r] = [rmin + r*rstep]; // creates the rho values
    }
    
    for (let m = 0; m < n_mu_values; m++){
      mu_values[m] = [mmin + m*mstep]; // creates the mu values
    }
    
    best_nll_value = 1e10; // a preposterously bad first nll
    
    for (let r = 0; r < n_rho_values; r++){
      for (let m = 0; m < n_mu_values; m++){
        nll_new = negLLprospect_cgt([rho_values[r], mu_values[m]], finiteGainVals, finiteLossVals, finiteSafeVals, finiteChoices);
        if (nll_new < best_nll_value) {
          best_nll_value = nll_new;
          bestR = r + 1; // +1 corrects for diff. in javascript vs. R indexing
          bestM = m + 1; // +1 corrects for diff. in javascript vs. R indexing
        }
      }
    }
    
    // print indices of best-fitting parameter values + NLL
    //console.log("The best R index is",bestR,"while the best M index is",bestM,", with an NLL of",best_nll_value)
    
    var str_bestR, str_bestM
    // Format the indices for good printing to filename
    str_bestR = String(bestR);
    if(str_bestR.length == 1){
      str_bestR = "00" + str_bestR;
    } else if (str_bestR.length == 2) {
      str_bestR = "0" + str_bestR;
    }
    
    str_bestM = String(bestM);
    if(str_bestM.length == 1){
      str_bestM = "00" + str_bestM;
    } else if (str_bestM.length == 2) {
      str_bestM = "0" + str_bestM;
    }
    
    // The file name to use in part 2
    fname = "bespoke_choiceset_rhoInd" + str_bestR + "_muInd" + str_bestM + ".csv";
    dynamicChoiceSetFilepath = "bespoke_choicesets/" + fname
    //console.log("dynamic choiceset:", dynamicChoiceSetFilepath)
    
    // save information
    psychoJS.experiment.addData("dynamicChoiceSetName", fname);
    psychoJS.experiment.addData("dynamicChoiceSetPath", dynamicChoiceSetFilepath);
    psychoJS.experiment.addData("bestRho",bestR)
    psychoJS.experiment.addData("bestMu", bestM)
    // keep track of which components have finished
    computeEstimatesComponents = [];
    computeEstimatesComponents.push(settingUpForPart2);
    
    for (const thisComponent of computeEstimatesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function computeEstimatesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'computeEstimates' ---
    // get current time
    t = computeEstimatesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *settingUpForPart2* updates
    if (t >= 0 && settingUpForPart2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      settingUpForPart2.tStart = t;  // (not accounting for frame time here)
      settingUpForPart2.frameNStart = frameN;  // exact frame index
      
      settingUpForPart2.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (settingUpForPart2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      settingUpForPart2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of computeEstimatesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function computeEstimatesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'computeEstimates' ---
    for (const thisComponent of computeEstimatesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pulledDataForDynamicRDM;
var getDynamicCSpath;
var getDynamicCSname;
var dynamicChoicesetResourceName;
var dynamicChoicesetResourcePath;
var loadDynamicChoicesetComponents;
function loadDynamicChoicesetRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'loadDynamicChoiceset' ---
    t = 0;
    loadDynamicChoicesetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var pulledDataForDynamicRDM, dynamicChoicesetResource
    
    pulledDataForDynamicRDM = psychoJS.experiment._trialsData
    //console.log("pulled data:", pulledDataForDynamicRDM)
    
    // just pull out the column of data that has the path and filename
    getDynamicCSpath = pulledDataForDynamicRDM.map((trial) => trial['dynamicChoiceSetPath']);
    getDynamicCSname = pulledDataForDynamicRDM.map((trial) => trial['dynamicChoiceSetName']);
    
    // print in console to make sure it worked
    //console.log("pulled filepath vector:", getDynamicCSpath)
    //console.log("pulled filename vector:", getDynamicCSname)
    
    // now just get the file name and file path (these are the last element in getchoicesetResource*
    dynamicChoicesetResourceName = getDynamicCSname[getDynamicCSname.length -1]
    dynamicChoicesetResourcePath = getDynamicCSpath[getDynamicCSpath.length -1]
    
    //console.log("pulled filename:", dynamicChoicesetResourceName)
    //console.log("pulled filepath:", dynamicChoicesetResourcePath)
    
    psychoJS._serverManager.prepareResources([
      // relative path to index.html
      { name: dynamicChoicesetResourceName, path: dynamicChoicesetResourcePath},
    ]);
    
    
    // keep track of which components have finished
    loadDynamicChoicesetComponents = [];
    
    for (const thisComponent of loadDynamicChoicesetComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function loadDynamicChoicesetRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'loadDynamicChoiceset' ---
    // get current time
    t = loadDynamicChoicesetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of loadDynamicChoicesetComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function loadDynamicChoicesetRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'loadDynamicChoiceset' ---
    for (const thisComponent of loadDynamicChoicesetComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "loadDynamicChoiceset" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var startDynamicTaskComponents;
function startDynamicTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startDynamicTask' ---
    t = 0;
    startDynamicTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    startDynamicTaskComponents = [];
    startDynamicTaskComponents.push(moveToRDMpart2);
    startDynamicTaskComponents.push(key_resp);
    
    for (const thisComponent of startDynamicTaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startDynamicTaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startDynamicTask' ---
    // get current time
    t = startDynamicTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *moveToRDMpart2* updates
    if (t >= 0.0 && moveToRDMpart2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveToRDMpart2.tStart = t;  // (not accounting for frame time here)
      moveToRDMpart2.frameNStart = frameN;  // exact frame index
      
      moveToRDMpart2.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startDynamicTaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startDynamicTaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startDynamicTask' ---
    for (const thisComponent of startDynamicTaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "startDynamicTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var showOutcomeDynamicComponents;
function showOutcomeDynamicRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showOutcomeDynamic' ---
    t = 0;
    showOutcomeDynamicClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeFeedbackReal_3
    var choicetmp, feedbackRounded, outcometmp, outcomes, choices;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (realChoice.keys === undefined) {
        outcometmp = Math.nan;
        choicetmp = Math.nan;
        noRespLoc = [0, 0];
        ocLoc = [5, 5];
        ocGambleLoc = [5, 5];
        ocSafeLoc = [5, 5];
        hideGamLoc = [5, 5];
        extraITI = 0;
    } else if (realChoice.keys === "v" && realloc === 1) {
         outcometmp = random_item([riskyoption1, riskyoption2]);
         choicetmp = 1;
         extraITI = 4-realChoice.rt
         if (outcometmp === riskyoption1) {
              ocLoc = [(- 0.4), 0.1];
              ocGambleLoc = [(- 0.4), 0];
              ocSafeLoc = [5, 5];
              noRespLoc = [5, 5];
              hideGamLoc = [(- 0.4), (- 0.125)];
         } else if (outcometmp === riskyoption2) {
              ocLoc = [(- 0.4), (- 0.1)];
              ocGambleLoc = [(- 0.4), 0];
              ocSafeLoc = [5, 5];
              hideGamLoc = [(- 0.4), 0.125];
              noRespLoc = [5, 5];
         }
     } else if (realChoice.keys === "v" && realloc === 2) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoice.rt
         ocLoc = [(- 0.4), 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
     } else if (realChoice.keys === "n" && realloc === 1) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoice.rt
         ocLoc = [0.4, 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
    } else if (realChoice.keys === "n" && realloc === 2) {
        outcometmp = random_item([riskyoption1, riskyoption2]);
        choicetmp = 1;
        extraITI = 4-realChoice.rt
        if (outcometmp === riskyoption1) {
            ocLoc = [0.4, 0.1];
            ocGambleLoc = [0.4, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.4, (- 0.125)];
            noRespLoc = [5, 5];
        } else if (outcometmp === riskyoption2) {
            ocLoc = [0.4, (- 0.1)];
            ocGambleLoc = [0.4, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.4, 0.125];
            noRespLoc = [5, 5];
        }
    }
    
    actualITI = initITIdynamic[dynamicRDM.thisN] + extraITI
    
    
    if (outcometmp === riskyoption2) {
        feedbackRounded = "$" + Math.round(outcometmp)
    } else {
        feedbackRounded = "$" + (Math.round(outcometmp*100)/100).toFixed(2)
        //feedbackRounded = "$" + Math.round(outcometmp*100)/100
    }
    
    /*
    console.log("gain:",riskyoption1)
    console.log("loss:",riskyoption2)
    console.log("safe:",safeoption)
    console.log("outcome:", outcometmp)
    console.log("choice:", choicetmp)
    console.log("extra iti:", extraITI)
    console.log("rt", realChoice.rt)
    console.log("actualITI", actualITI)
    console.log("init ITI", initITIdynamic[dynamicRDM.thisN])
    */
    
    
    psychoJS.experiment.addData("outcomes", outcometmp);
    psychoJS.experiment.addData("choices", choicetmp);
    psychoJS.experiment.addData("extraITI", extraITI);
    psychoJS.experiment.addData("actualITI",actualITI)
    psychoJS.experiment.addData("init ITI", initITIdynamic[dynamicRDM.thisN])
    
    noRespTxtReal_3.setPos(noRespLoc);
    ocGambleReal_3.setPos(ocGambleLoc);
    ocSafeReal_3.setPos(ocSafeLoc);
    outcomeTextReal_3.setColor(new util.Color('black'));
    outcomeTextReal_3.setPos(ocLoc);
    outcomeTextReal_3.setText(feedbackRounded);
    hideGambleReal_3.setPos(hideGamLoc);
    // keep track of which components have finished
    showOutcomeDynamicComponents = [];
    showOutcomeDynamicComponents.push(noRespTxtReal_3);
    showOutcomeDynamicComponents.push(ocGambleReal_3);
    showOutcomeDynamicComponents.push(ocSafeReal_3);
    showOutcomeDynamicComponents.push(outcomeTextReal_3);
    showOutcomeDynamicComponents.push(hideGambleReal_3);
    
    for (const thisComponent of showOutcomeDynamicComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showOutcomeDynamicRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showOutcomeDynamic' ---
    // get current time
    t = showOutcomeDynamicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *noRespTxtReal_3* updates
    if (t >= 0.0 && noRespTxtReal_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noRespTxtReal_3.tStart = t;  // (not accounting for frame time here)
      noRespTxtReal_3.frameNStart = frameN;  // exact frame index
      
      noRespTxtReal_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noRespTxtReal_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noRespTxtReal_3.setAutoDraw(false);
    }
    
    // *ocGambleReal_3* updates
    if (t >= 0.0 && ocGambleReal_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocGambleReal_3.tStart = t;  // (not accounting for frame time here)
      ocGambleReal_3.frameNStart = frameN;  // exact frame index
      
      ocGambleReal_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocGambleReal_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocGambleReal_3.setAutoDraw(false);
    }
    
    // *ocSafeReal_3* updates
    if (t >= 0.0 && ocSafeReal_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ocSafeReal_3.tStart = t;  // (not accounting for frame time here)
      ocSafeReal_3.frameNStart = frameN;  // exact frame index
      
      ocSafeReal_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ocSafeReal_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ocSafeReal_3.setAutoDraw(false);
    }
    
    // *outcomeTextReal_3* updates
    if (t >= 0.0 && outcomeTextReal_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcomeTextReal_3.tStart = t;  // (not accounting for frame time here)
      outcomeTextReal_3.frameNStart = frameN;  // exact frame index
      
      outcomeTextReal_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outcomeTextReal_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outcomeTextReal_3.setAutoDraw(false);
    }
    
    // *hideGambleReal_3* updates
    if (t >= 0.0 && hideGambleReal_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hideGambleReal_3.tStart = t;  // (not accounting for frame time here)
      hideGambleReal_3.frameNStart = frameN;  // exact frame index
      
      hideGambleReal_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (hideGambleReal_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      hideGambleReal_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showOutcomeDynamicComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showOutcomeDynamicRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showOutcomeDynamic' ---
    for (const thisComponent of showOutcomeDynamicComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from codeFeedbackReal_3
    outcomes.push(outcometmp);
    choices.push(choicetmp);
    //riskyloss_values.push(riskyLossReal);
    //riskygain_values.push(riskyGainReal);
    //certain_values.push(certain);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _stopBreak_allKeys;
var rdmToSpanTransitionComponents;
function rdmToSpanTransitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdmToSpanTransition' ---
    t = 0;
    rdmToSpanTransitionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stopBreak.keys = undefined;
    stopBreak.rt = undefined;
    _stopBreak_allKeys = [];
    // keep track of which components have finished
    rdmToSpanTransitionComponents = [];
    rdmToSpanTransitionComponents.push(breaktxt);
    rdmToSpanTransitionComponents.push(stopBreak);
    
    for (const thisComponent of rdmToSpanTransitionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdmToSpanTransitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdmToSpanTransition' ---
    // get current time
    t = rdmToSpanTransitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breaktxt* updates
    if (t >= 0.0 && breaktxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breaktxt.tStart = t;  // (not accounting for frame time here)
      breaktxt.frameNStart = frameN;  // exact frame index
      
      breaktxt.setAutoDraw(true);
    }

    
    // *stopBreak* updates
    if (t >= 0.0 && stopBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stopBreak.tStart = t;  // (not accounting for frame time here)
      stopBreak.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { stopBreak.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { stopBreak.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { stopBreak.clearEvents(); });
    }

    if (stopBreak.status === PsychoJS.Status.STARTED) {
      let theseKeys = stopBreak.getKeys({keyList: ['return'], waitRelease: false});
      _stopBreak_allKeys = _stopBreak_allKeys.concat(theseKeys);
      if (_stopBreak_allKeys.length > 0) {
        stopBreak.keys = _stopBreak_allKeys[_stopBreak_allKeys.length - 1].name;  // just the last key pressed
        stopBreak.rt = _stopBreak_allKeys[_stopBreak_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of rdmToSpanTransitionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rdmToSpanTransitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdmToSpanTransition' ---
    for (const thisComponent of rdmToSpanTransitionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(stopBreak.corr, level);
    }
    psychoJS.experiment.addData('stopBreak.keys', stopBreak.keys);
    if (typeof stopBreak.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('stopBreak.rt', stopBreak.rt);
        routineTimer.reset();
        }
    
    stopBreak.stop();
    // the Routine "rdmToSpanTransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong_allKeys;
var SpanGeneralInstructionsComponents;
function SpanGeneralInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanGeneralInstructions' ---
    t = 0;
    SpanGeneralInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong.keys = undefined;
    movealong.rt = undefined;
    _movealong_allKeys = [];
    // keep track of which components have finished
    SpanGeneralInstructionsComponents = [];
    SpanGeneralInstructionsComponents.push(GenInsText);
    SpanGeneralInstructionsComponents.push(movealong);
    
    for (const thisComponent of SpanGeneralInstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanGeneralInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanGeneralInstructions' ---
    // get current time
    t = SpanGeneralInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *GenInsText* updates
    if (t >= 0.0 && GenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GenInsText.tStart = t;  // (not accounting for frame time here)
      GenInsText.frameNStart = frameN;  // exact frame index
      
      GenInsText.setAutoDraw(true);
    }

    
    // *movealong* updates
    if (t >= 0.0 && movealong.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong.tStart = t;  // (not accounting for frame time here)
      movealong.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong.clearEvents(); });
    }

    if (movealong.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong.getKeys({keyList: ['return'], waitRelease: false});
      _movealong_allKeys = _movealong_allKeys.concat(theseKeys);
      if (_movealong_allKeys.length > 0) {
        movealong.keys = _movealong_allKeys[_movealong_allKeys.length - 1].name;  // just the last key pressed
        movealong.rt = _movealong_allKeys[_movealong_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanGeneralInstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanGeneralInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanGeneralInstructions' ---
    for (const thisComponent of SpanGeneralInstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong.corr, level);
    }
    psychoJS.experiment.addData('movealong.keys', movealong.keys);
    if (typeof movealong.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong.rt', movealong.rt);
        routineTimer.reset();
        }
    
    movealong.stop();
    // the Routine "SpanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong2_allKeys;
var SpanReminder1Components;
function SpanReminder1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanReminder1' ---
    t = 0;
    SpanReminder1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong2.keys = undefined;
    movealong2.rt = undefined;
    _movealong2_allKeys = [];
    // keep track of which components have finished
    SpanReminder1Components = [];
    SpanReminder1Components.push(Reminder1);
    SpanReminder1Components.push(movealong2);
    
    for (const thisComponent of SpanReminder1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanReminder1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanReminder1' ---
    // get current time
    t = SpanReminder1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Reminder1* updates
    if (t >= 0.0 && Reminder1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Reminder1.tStart = t;  // (not accounting for frame time here)
      Reminder1.frameNStart = frameN;  // exact frame index
      
      Reminder1.setAutoDraw(true);
    }

    
    // *movealong2* updates
    if (t >= 0.0 && movealong2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong2.tStart = t;  // (not accounting for frame time here)
      movealong2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong2.clearEvents(); });
    }

    if (movealong2.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong2.getKeys({keyList: ['return'], waitRelease: false});
      _movealong2_allKeys = _movealong2_allKeys.concat(theseKeys);
      if (_movealong2_allKeys.length > 0) {
        movealong2.keys = _movealong2_allKeys[_movealong2_allKeys.length - 1].name;  // just the last key pressed
        movealong2.rt = _movealong2_allKeys[_movealong2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanReminder1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanReminder1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanReminder1' ---
    for (const thisComponent of SpanReminder1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong2.corr, level);
    }
    psychoJS.experiment.addData('movealong2.keys', movealong2.keys);
    if (typeof movealong2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong2.rt', movealong2.rt);
        routineTimer.reset();
        }
    
    movealong2.stop();
    // the Routine "SpanReminder1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _movealong3_allKeys;
var SpanReminder2Components;
function SpanReminder2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SpanReminder2' ---
    t = 0;
    SpanReminder2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    movealong3.keys = undefined;
    movealong3.rt = undefined;
    _movealong3_allKeys = [];
    // keep track of which components have finished
    SpanReminder2Components = [];
    SpanReminder2Components.push(Reminder2);
    SpanReminder2Components.push(movealong3);
    
    for (const thisComponent of SpanReminder2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SpanReminder2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SpanReminder2' ---
    // get current time
    t = SpanReminder2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Reminder2* updates
    if (t >= 0.0 && Reminder2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Reminder2.tStart = t;  // (not accounting for frame time here)
      Reminder2.frameNStart = frameN;  // exact frame index
      
      Reminder2.setAutoDraw(true);
    }

    
    // *movealong3* updates
    if (t >= 0.0 && movealong3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movealong3.tStart = t;  // (not accounting for frame time here)
      movealong3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { movealong3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { movealong3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { movealong3.clearEvents(); });
    }

    if (movealong3.status === PsychoJS.Status.STARTED) {
      let theseKeys = movealong3.getKeys({keyList: ['return'], waitRelease: false});
      _movealong3_allKeys = _movealong3_allKeys.concat(theseKeys);
      if (_movealong3_allKeys.length > 0) {
        movealong3.keys = _movealong3_allKeys[_movealong3_allKeys.length - 1].name;  // just the last key pressed
        movealong3.rt = _movealong3_allKeys[_movealong3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SpanReminder2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SpanReminder2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SpanReminder2' ---
    for (const thisComponent of SpanReminder2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(movealong3.corr, level);
    }
    psychoJS.experiment.addData('movealong3.keys', movealong3.keys);
    if (typeof movealong3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('movealong3.rt', movealong3.rt);
        routineTimer.reset();
        }
    
    movealong3.stop();
    // the Routine "SpanReminder2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startPractice_allKeys;
var FSInstructionsComponents;
function FSInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FSInstructions' ---
    t = 0;
    FSInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startPractice.keys = undefined;
    startPractice.rt = undefined;
    _startPractice_allKeys = [];
    // keep track of which components have finished
    FSInstructionsComponents = [];
    FSInstructionsComponents.push(FSGenInsText);
    FSInstructionsComponents.push(startPractice);
    
    for (const thisComponent of FSInstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FSInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FSInstructions' ---
    // get current time
    t = FSInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FSGenInsText* updates
    if (t >= 0.0 && FSGenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FSGenInsText.tStart = t;  // (not accounting for frame time here)
      FSGenInsText.frameNStart = frameN;  // exact frame index
      
      FSGenInsText.setAutoDraw(true);
    }

    
    // *startPractice* updates
    if (t >= 0.0 && startPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startPractice.tStart = t;  // (not accounting for frame time here)
      startPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startPractice.clearEvents(); });
    }

    if (startPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = startPractice.getKeys({keyList: ['return'], waitRelease: false});
      _startPractice_allKeys = _startPractice_allKeys.concat(theseKeys);
      if (_startPractice_allKeys.length > 0) {
        startPractice.keys = _startPractice_allKeys[_startPractice_allKeys.length - 1].name;  // just the last key pressed
        startPractice.rt = _startPractice_allKeys[_startPractice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FSInstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FSInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FSInstructions' ---
    for (const thisComponent of FSInstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startPractice.corr, level);
    }
    psychoJS.experiment.addData('startPractice.keys', startPractice.keys);
    if (typeof startPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startPractice.rt', startPractice.rt);
        routineTimer.reset();
        }
    
    startPractice.stop();
    // the Routine "FSInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ShowNumbersPracticeComponents;
function ShowNumbersPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowNumbersPractice' ---
    t = 0;
    ShowNumbersPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    //console.log(digits)
    
    pres_text_practice.setText(digits.toString()[DigitLoopPractice.thisN]);
    // keep track of which components have finished
    ShowNumbersPracticeComponents = [];
    ShowNumbersPracticeComponents.push(fixation_2);
    ShowNumbersPracticeComponents.push(pres_text_practice);
    
    for (const thisComponent of ShowNumbersPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowNumbersPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowNumbersPractice' ---
    // get current time
    t = ShowNumbersPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_2* updates
    if (t >= 0.0 && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_2.setAutoDraw(false);
    }
    
    // *pres_text_practice* updates
    if (t >= 1 && pres_text_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text_practice.tStart = t;  // (not accounting for frame time here)
      pres_text_practice.frameNStart = frameN;  // exact frame index
      
      pres_text_practice.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text_practice.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowNumbersPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowNumbersPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowNumbersPractice' ---
    for (const thisComponent of ShowNumbersPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var RecallPracticeComponents;
function RecallPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RecallPractice' ---
    t = 0;
    RecallPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxPractice.setText('');
    textboxPractice.refresh();
    // setup some python lists for storing info about the mousePractice
    mousePractice.clicked_name = [];
    gotValidClick = false; // until a click is received
    // this is a temporary fix to allow editable textbox to be used on several trials
    textboxPractice.refresh()
    // keep track of which components have finished
    RecallPracticeComponents = [];
    RecallPracticeComponents.push(recall_txtPractice);
    RecallPracticeComponents.push(textboxPractice);
    RecallPracticeComponents.push(cont_buttonPractice);
    RecallPracticeComponents.push(mousePractice);
    
    for (const thisComponent of RecallPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function RecallPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RecallPractice' ---
    // get current time
    t = RecallPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtPractice* updates
    if (t >= 0 && recall_txtPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtPractice.tStart = t;  // (not accounting for frame time here)
      recall_txtPractice.frameNStart = frameN;  // exact frame index
      
      recall_txtPractice.setAutoDraw(true);
    }

    
    // *textboxPractice* updates
    if (t >= 0 && textboxPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxPractice.tStart = t;  // (not accounting for frame time here)
      textboxPractice.frameNStart = frameN;  // exact frame index
      
      textboxPractice.setAutoDraw(true);
    }

    
    // *cont_buttonPractice* updates
    if (t >= 0 && cont_buttonPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonPractice.tStart = t;  // (not accounting for frame time here)
      cont_buttonPractice.frameNStart = frameN;  // exact frame index
      
      cont_buttonPractice.setAutoDraw(true);
    }

    // *mousePractice* updates
    if (t >= 0 && mousePractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mousePractice.tStart = t;  // (not accounting for frame time here)
      mousePractice.frameNStart = frameN;  // exact frame index
      
      mousePractice.status = PsychoJS.Status.STARTED;
      mousePractice.mouseClock.reset();
      prevButtonState = mousePractice.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mousePractice.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mousePractice.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonPractice]) {
            if (obj.contains(mousePractice)) {
              gotValidClick = true;
              mousePractice.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
var fbTxt;
var _mouseXYs;
function RecallPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RecallPractice' ---
    for (const thisComponent of RecallPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxPractice.text',textboxPractice.text)
    // Run 'End Routine' code from code_3practice
    if ((textboxPractice.text === digits.toString())) {
        correct = 1;
        fbTxt = "Correct!";
    } else {
        correct = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correct);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mousePractice.getPos();
    _mouseButtons = mousePractice.getPressed();
    psychoJS.experiment.addData('mousePractice.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mousePractice.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mousePractice.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mousePractice.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mousePractice.rightButton', _mouseButtons[2]);
    if (mousePractice.clicked_name.length > 0) {
      psychoJS.experiment.addData('mousePractice.clicked_name', mousePractice.clicked_name[0]);}
    // the Routine "RecallPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackPracticeComponents;
function FeedbackPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FeedbackPractice' ---
    t = 0;
    FeedbackPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedbac_textPractice.setText(fbTxt);
    // keep track of which components have finished
    FeedbackPracticeComponents = [];
    FeedbackPracticeComponents.push(feedbac_textPractice);
    
    for (const thisComponent of FeedbackPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FeedbackPractice' ---
    // get current time
    t = FeedbackPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbac_textPractice* updates
    if (t >= 0.0 && feedbac_textPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbac_textPractice.tStart = t;  // (not accounting for frame time here)
      feedbac_textPractice.frameNStart = frameN;  // exact frame index
      
      feedbac_textPractice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbac_textPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbac_textPractice.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FeedbackPractice' ---
    for (const thisComponent of FeedbackPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startFSreal_allKeys;
var StartRealFSComponents;
function StartRealFSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'StartRealFS' ---
    t = 0;
    StartRealFSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startFSreal.keys = undefined;
    startFSreal.rt = undefined;
    _startFSreal_allKeys = [];
    // keep track of which components have finished
    StartRealFSComponents = [];
    StartRealFSComponents.push(praccomplete);
    StartRealFSComponents.push(startFSreal);
    
    for (const thisComponent of StartRealFSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartRealFSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StartRealFS' ---
    // get current time
    t = StartRealFSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *praccomplete* updates
    if (t >= 0.0 && praccomplete.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      praccomplete.tStart = t;  // (not accounting for frame time here)
      praccomplete.frameNStart = frameN;  // exact frame index
      
      praccomplete.setAutoDraw(true);
    }

    
    // *startFSreal* updates
    if (t >= 0.0 && startFSreal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startFSreal.tStart = t;  // (not accounting for frame time here)
      startFSreal.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startFSreal.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startFSreal.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startFSreal.clearEvents(); });
    }

    if (startFSreal.status === PsychoJS.Status.STARTED) {
      let theseKeys = startFSreal.getKeys({keyList: ['return'], waitRelease: false});
      _startFSreal_allKeys = _startFSreal_allKeys.concat(theseKeys);
      if (_startFSreal_allKeys.length > 0) {
        startFSreal.keys = _startFSreal_allKeys[_startFSreal_allKeys.length - 1].name;  // just the last key pressed
        startFSreal.rt = _startFSreal_allKeys[_startFSreal_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartRealFSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRealFSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StartRealFS' ---
    for (const thisComponent of StartRealFSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startFSreal.corr, level);
    }
    psychoJS.experiment.addData('startFSreal.keys', startFSreal.keys);
    if (typeof startFSreal.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startFSreal.rt', startFSreal.rt);
        routineTimer.reset();
        }
    
    startFSreal.stop();
    // the Routine "StartRealFS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var numbersToChoose;
var minDigitFS;
var maxDigitFS;
var nTrialsFS;
var incorrectCount;
var digitSpan;
var digitsForTrial;
var checkingNumbers;
var startN;
var endN;
var selectNumbersComponents;
function selectNumbersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'selectNumbers' ---
    t = 0;
    selectNumbersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from selectNumbersFS
    //import * as random from 'random';
    var checkingNumbers, endN, singleNumber, startN, tmpFirst, tmpSecond, numbersToChoose, minDigitFS, maxDigitFS;
    
    numbersToChoose = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    minDigitFS = 3;
    maxDigitFS = 16;
    //correctCount = [];
    //incorrectCount = 0;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    //nTrialsFS += 1;
    //nTrialsFS = nTrialsFS+1;
    
    nTrialsFS = trialsFS.thisN
    //console.log("nTrialsFS:", nTrialsFS)
    
    // make incorrect count 0 on the first trial
    if (nTrialsFS === 0){
        incorrectCount = 0;
    }
    
    if (correctCount === 0) {
        incorrectCount = incorrectCount + 1;
    }
    
    //if ((nTrialsFS === 1)) {
    if (nTrialsFS === 0) {
        digitSpan = minDigitFS;
    } else if (nTrialsFS !== 0) {
        if (correctCount ===1) {
            digitSpan = (digitSpan +1)
            incorrectCount = 0;
        } else if (correctCount === 0 && incorrectCount < 2){
            digitSpan = digitSpan
        } else if (correctCount === 0 && incorrectCount === 2){
            digitSpan = (digitSpan - 1);
            incorrectCount = 0;
        }      
    }
    
    /*
    console.log("digit span:",digitSpan)
    console.log("correct count:", correctCount)
    console.log("incorrectCount:", incorrectCount)
    */
    
    if ((digitSpan < minDigitFS)) {
        digitSpan = minDigitFS;
    }
    
    digitsForTrial = [];
    while ((digitsForTrial.length < digitSpan)) {
        if ((digitSpan <= 9)) {
            singleNumber = random_item(numbersToChoose);
            if ((util.count(digitsForTrial, singleNumber) < 1)) {
                digitsForTrial.push(singleNumber);
            }
        } else {
            if ((digitSpan > 9)) {
                singleNumber = random_item(numbersToChoose);
                if (((digitsForTrial.length < 9) && (util.count(digitsForTrial, singleNumber) === 0))) {
                    digitsForTrial.push(singleNumber);
                }
                if (((digitsForTrial.length >= 9) && (util.count(digitsForTrial, singleNumber) < 2))) {
                    digitsForTrial.push(singleNumber);
                }
            }
        }
    }
    checkingNumbers = true;
    startN = 1;
    endN = (digitsForTrial.length - 1);
    while (checkingNumbers) {
        for (var n, _pj_c = 0, _pj_a = util.range(startN, endN), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            n = _pj_a[_pj_c];
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] + 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] - 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] - 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] + 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
        }
        checkingNumbers = false;
    }
    
    //console.log(digitSpan)
    //console.log(digitsForTrial)
    // keep track of which components have finished
    selectNumbersComponents = [];
    
    for (const thisComponent of selectNumbersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function selectNumbersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'selectNumbers' ---
    // get current time
    t = selectNumbersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selectNumbersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function selectNumbersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'selectNumbers' ---
    for (const thisComponent of selectNumbersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tmpNumber;
var ShowNumbersComponents;
function ShowNumbersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowNumbers' ---
    t = 0;
    ShowNumbersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from getTmpNumberCodeFS
    var tmpNumber
    tmpNumber = digitsForTrial[digitLoop.thisN];
    
    presentation_text.setText(tmpNumber);
    // keep track of which components have finished
    ShowNumbersComponents = [];
    ShowNumbersComponents.push(fixation);
    ShowNumbersComponents.push(presentation_text);
    
    for (const thisComponent of ShowNumbersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowNumbersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowNumbers' ---
    // get current time
    t = ShowNumbersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *presentation_text* updates
    if (t >= 1 && presentation_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentation_text.tStart = t;  // (not accounting for frame time here)
      presentation_text.frameNStart = frameN;  // exact frame index
      
      presentation_text.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentation_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentation_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowNumbersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowNumbersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowNumbers' ---
    for (const thisComponent of ShowNumbersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from getTmpNumberCodeFS
    psychoJS.experiment.addData("digitsForTrial", digitsForTrial);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RecallComponents;
function RecallRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Recall' ---
    t = 0;
    RecallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textbox.setText('');
    textbox.refresh();
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallComponents = [];
    RecallComponents.push(recall_txt);
    RecallComponents.push(textbox);
    RecallComponents.push(cont_button);
    RecallComponents.push(mouse_3);
    
    for (const thisComponent of RecallComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecallRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Recall' ---
    // get current time
    t = RecallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txt* updates
    if (t >= 0 && recall_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txt.tStart = t;  // (not accounting for frame time here)
      recall_txt.frameNStart = frameN;  // exact frame index
      
      recall_txt.setAutoDraw(true);
    }

    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }

    
    // *cont_button* updates
    if (t >= 0.0 && cont_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_button.tStart = t;  // (not accounting for frame time here)
      cont_button.frameNStart = frameN;  // exact frame index
      
      cont_button.setAutoDraw(true);
    }

    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_button]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correctCount;
function RecallRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Recall' ---
    for (const thisComponent of RecallComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textbox.text',textbox.text)
    // Run 'End Routine' code from code_3
    for (var r, _pj_c = 0, _pj_a = util.range(digitsForTrial.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        r = _pj_a[_pj_c];
        digitsForTrial[r] = digitsForTrial[r].toString();
    }
    digitsForTrial = digitsForTrial.join("");
    if ((textbox.text === digitsForTrial.toString())) {
        correctCount = 1;
        fbTxt = "Correct!";
    } else {
        correctCount = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correctCount);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    // the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Feedback' ---
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedback_text.setText(fbTxt);
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(feedback_text);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Feedback' ---
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Feedback' ---
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _moveToBS_allKeys;
var FStoBStransitionComponents;
function FStoBStransitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FStoBStransition' ---
    t = 0;
    FStoBStransitionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    moveToBS.keys = undefined;
    moveToBS.rt = undefined;
    _moveToBS_allKeys = [];
    // keep track of which components have finished
    FStoBStransitionComponents = [];
    FStoBStransitionComponents.push(roundTransition);
    FStoBStransitionComponents.push(moveToBS);
    
    for (const thisComponent of FStoBStransitionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FStoBStransitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FStoBStransition' ---
    // get current time
    t = FStoBStransitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *roundTransition* updates
    if (t >= 0.0 && roundTransition.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      roundTransition.tStart = t;  // (not accounting for frame time here)
      roundTransition.frameNStart = frameN;  // exact frame index
      
      roundTransition.setAutoDraw(true);
    }

    
    // *moveToBS* updates
    if (t >= 0.0 && moveToBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveToBS.tStart = t;  // (not accounting for frame time here)
      moveToBS.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { moveToBS.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { moveToBS.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { moveToBS.clearEvents(); });
    }

    if (moveToBS.status === PsychoJS.Status.STARTED) {
      let theseKeys = moveToBS.getKeys({keyList: ['return'], waitRelease: false});
      _moveToBS_allKeys = _moveToBS_allKeys.concat(theseKeys);
      if (_moveToBS_allKeys.length > 0) {
        moveToBS.keys = _moveToBS_allKeys[_moveToBS_allKeys.length - 1].name;  // just the last key pressed
        moveToBS.rt = _moveToBS_allKeys[_moveToBS_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FStoBStransitionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FStoBStransitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FStoBStransition' ---
    for (const thisComponent of FStoBStransitionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(moveToBS.corr, level);
    }
    psychoJS.experiment.addData('moveToBS.keys', moveToBS.keys);
    if (typeof moveToBS.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('moveToBS.rt', moveToBS.rt);
        routineTimer.reset();
        }
    
    moveToBS.stop();
    // the Routine "FStoBStransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startBSprac_allKeys;
var InstructionsBSComponents;
function InstructionsBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstructionsBS' ---
    t = 0;
    InstructionsBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startBSprac.keys = undefined;
    startBSprac.rt = undefined;
    _startBSprac_allKeys = [];
    // keep track of which components have finished
    InstructionsBSComponents = [];
    InstructionsBSComponents.push(BSGenInsText);
    InstructionsBSComponents.push(startBSprac);
    
    for (const thisComponent of InstructionsBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstructionsBS' ---
    // get current time
    t = InstructionsBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BSGenInsText* updates
    if (t >= 0.0 && BSGenInsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BSGenInsText.tStart = t;  // (not accounting for frame time here)
      BSGenInsText.frameNStart = frameN;  // exact frame index
      
      BSGenInsText.setAutoDraw(true);
    }

    
    // *startBSprac* updates
    if (t >= 0.0 && startBSprac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startBSprac.tStart = t;  // (not accounting for frame time here)
      startBSprac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startBSprac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startBSprac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startBSprac.clearEvents(); });
    }

    if (startBSprac.status === PsychoJS.Status.STARTED) {
      let theseKeys = startBSprac.getKeys({keyList: ['return'], waitRelease: false});
      _startBSprac_allKeys = _startBSprac_allKeys.concat(theseKeys);
      if (_startBSprac_allKeys.length > 0) {
        startBSprac.keys = _startBSprac_allKeys[_startBSprac_allKeys.length - 1].name;  // just the last key pressed
        startBSprac.rt = _startBSprac_allKeys[_startBSprac_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstructionsBS' ---
    for (const thisComponent of InstructionsBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startBSprac.corr, level);
    }
    psychoJS.experiment.addData('startBSprac.keys', startBSprac.keys);
    if (typeof startBSprac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startBSprac.rt', startBSprac.rt);
        routineTimer.reset();
        }
    
    startBSprac.stop();
    // the Routine "InstructionsBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var showNumbersPracticeBSComponents;
function showNumbersPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showNumbersPracticeBS' ---
    t = 0;
    showNumbersPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    pres_text_practice_2.setText(digitsReverse.toString()[digitLoopPracticeBS.thisN]);
    // keep track of which components have finished
    showNumbersPracticeBSComponents = [];
    showNumbersPracticeBSComponents.push(fixation_3);
    showNumbersPracticeBSComponents.push(pres_text_practice_2);
    
    for (const thisComponent of showNumbersPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showNumbersPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showNumbersPracticeBS' ---
    // get current time
    t = showNumbersPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_3* updates
    if (t >= 0.0 && fixation_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_3.tStart = t;  // (not accounting for frame time here)
      fixation_3.frameNStart = frameN;  // exact frame index
      
      fixation_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_3.setAutoDraw(false);
    }
    
    // *pres_text_practice_2* updates
    if (t >= 1 && pres_text_practice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text_practice_2.tStart = t;  // (not accounting for frame time here)
      pres_text_practice_2.frameNStart = frameN;  // exact frame index
      
      pres_text_practice_2.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text_practice_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text_practice_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showNumbersPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showNumbersPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showNumbersPracticeBS' ---
    for (const thisComponent of showNumbersPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var recallPracticeBSComponents;
function recallPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'recallPracticeBS' ---
    t = 0;
    recallPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxPractice_2.setText('');
    textboxPractice_2.refresh();
    // setup some python lists for storing info about the mousePractice_2
    mousePractice_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // this is a temporary fix to allow editable textbox to be used on several trials
    textboxPractice_2.refresh()
    // keep track of which components have finished
    recallPracticeBSComponents = [];
    recallPracticeBSComponents.push(recall_txtPractice_2);
    recallPracticeBSComponents.push(textboxPractice_2);
    recallPracticeBSComponents.push(cont_buttonPractice_2);
    recallPracticeBSComponents.push(mousePractice_2);
    
    for (const thisComponent of recallPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function recallPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'recallPracticeBS' ---
    // get current time
    t = recallPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtPractice_2* updates
    if (t >= 0 && recall_txtPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtPractice_2.tStart = t;  // (not accounting for frame time here)
      recall_txtPractice_2.frameNStart = frameN;  // exact frame index
      
      recall_txtPractice_2.setAutoDraw(true);
    }

    
    // *textboxPractice_2* updates
    if (t >= 0.0 && textboxPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxPractice_2.tStart = t;  // (not accounting for frame time here)
      textboxPractice_2.frameNStart = frameN;  // exact frame index
      
      textboxPractice_2.setAutoDraw(true);
    }

    
    // *cont_buttonPractice_2* updates
    if (t >= 0.0 && cont_buttonPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonPractice_2.tStart = t;  // (not accounting for frame time here)
      cont_buttonPractice_2.frameNStart = frameN;  // exact frame index
      
      cont_buttonPractice_2.setAutoDraw(true);
    }

    // *mousePractice_2* updates
    if (t >= 0.0 && mousePractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mousePractice_2.tStart = t;  // (not accounting for frame time here)
      mousePractice_2.frameNStart = frameN;  // exact frame index
      
      mousePractice_2.status = PsychoJS.Status.STARTED;
      mousePractice_2.mouseClock.reset();
      prevButtonState = mousePractice_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mousePractice_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mousePractice_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonPractice_2]) {
            if (obj.contains(mousePractice_2)) {
              gotValidClick = true;
              mousePractice_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recallPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recallPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'recallPracticeBS' ---
    for (const thisComponent of recallPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxPractice_2.text',textboxPractice_2.text)
    // Run 'End Routine' code from code_3practice_2
    if ((textboxPractice_2.text === digitsReverseCorrAnswer.toString())) {
        correct = 1;
        fbTxt = "Correct!";
    } else {
        correct = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correct);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mousePractice_2.getPos();
    _mouseButtons = mousePractice_2.getPressed();
    psychoJS.experiment.addData('mousePractice_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mousePractice_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mousePractice_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mousePractice_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mousePractice_2.rightButton', _mouseButtons[2]);
    if (mousePractice_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mousePractice_2.clicked_name', mousePractice_2.clicked_name[0]);}
    // the Routine "recallPracticeBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackPracticeBSComponents;
function feedbackPracticeBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedbackPracticeBS' ---
    t = 0;
    feedbackPracticeBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedbac_textPractice_2.setText(fbTxt);
    // keep track of which components have finished
    feedbackPracticeBSComponents = [];
    feedbackPracticeBSComponents.push(feedbac_textPractice_2);
    
    for (const thisComponent of feedbackPracticeBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackPracticeBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedbackPracticeBS' ---
    // get current time
    t = feedbackPracticeBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbac_textPractice_2* updates
    if (t >= 0.0 && feedbac_textPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbac_textPractice_2.tStart = t;  // (not accounting for frame time here)
      feedbac_textPractice_2.frameNStart = frameN;  // exact frame index
      
      feedbac_textPractice_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbac_textPractice_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbac_textPractice_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackPracticeBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackPracticeBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedbackPracticeBS' ---
    for (const thisComponent of feedbackPracticeBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startBSreal_allKeys;
var startRealBSComponents;
function startRealBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startRealBS' ---
    t = 0;
    startRealBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startBSreal.keys = undefined;
    startBSreal.rt = undefined;
    _startBSreal_allKeys = [];
    // keep track of which components have finished
    startRealBSComponents = [];
    startRealBSComponents.push(praccompleteBS);
    startRealBSComponents.push(startBSreal);
    
    for (const thisComponent of startRealBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startRealBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startRealBS' ---
    // get current time
    t = startRealBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *praccompleteBS* updates
    if (t >= 0.0 && praccompleteBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      praccompleteBS.tStart = t;  // (not accounting for frame time here)
      praccompleteBS.frameNStart = frameN;  // exact frame index
      
      praccompleteBS.setAutoDraw(true);
    }

    
    // *startBSreal* updates
    if (t >= 0.0 && startBSreal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startBSreal.tStart = t;  // (not accounting for frame time here)
      startBSreal.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startBSreal.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startBSreal.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startBSreal.clearEvents(); });
    }

    if (startBSreal.status === PsychoJS.Status.STARTED) {
      let theseKeys = startBSreal.getKeys({keyList: ['return'], waitRelease: false});
      _startBSreal_allKeys = _startBSreal_allKeys.concat(theseKeys);
      if (_startBSreal_allKeys.length > 0) {
        startBSreal.keys = _startBSreal_allKeys[_startBSreal_allKeys.length - 1].name;  // just the last key pressed
        startBSreal.rt = _startBSreal_allKeys[_startBSreal_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startRealBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRealBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startRealBS' ---
    for (const thisComponent of startRealBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startBSreal.corr, level);
    }
    psychoJS.experiment.addData('startBSreal.keys', startBSreal.keys);
    if (typeof startBSreal.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startBSreal.rt', startBSreal.rt);
        routineTimer.reset();
        }
    
    startBSreal.stop();
    // the Routine "startRealBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var minDigitBS;
var maxDigitBS;
var nTrialsBS;
var selectNumbersBSComponents;
function selectNumbersBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'selectNumbersBS' ---
    t = 0;
    selectNumbersBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from selectNumbersBScode
    //import * as random from 'random';
    var checkingNumbers,endN, singleNumber, startN, tmpFirst, tmpSecond, numbersToChoose, minDigitBS, maxDigitBS
    
    numbersToChoose = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    minDigitBS = 2;
    maxDigitBS = 15;
    //correct = [];
    //incorrectCount = 0;
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    
    
    //nTrialsBS += 1;
    nTrialsBS = trialsBS.thisN
    //console.log("nTrialsBS:", nTrialsBS)
    
    // reset incorrect count on the first trial
    if (nTrialsBS ===0) {
        incorrectCount = 0
        correctCount = Math.nan
    }
    
    if (correctCount === 0) {
        incorrectCount = incorrectCount + 1;
    }
    
    if (nTrialsBS === 0) {
        //correctCount = 0;
        digitSpan = minDigitBS;
    } else if (nTrialsBS !==0){
        if (correctCount ===1){
            digitSpan = (digitSpan + 1);
            incorrectCount = 0;
        } else if (correctCount === 0 && incorrectCount < 2) {
            digitSpan = digitSpan;
        } else if (correctCount === 0 && incorrectCount === 2) {
            digitSpan = (digitSpan - 1);
            incorrectCount = 0;
        }
    }
    
    /*
    console.log("digit span:",digitSpan)
    console.log("correct count:", correctCount)
    console.log("incorrectCount:", incorrectCount)
    */
    
    if (digitSpan < minDigitBS) {
        digitSpan = minDigitBS;
    }
    
    digitsForTrial = [];
    while ((digitsForTrial.length < digitSpan)) {
        if ((digitSpan <= 9)) {
            singleNumber = random_item(numbersToChoose);
            if ((util.count(digitsForTrial, singleNumber) < 1)) {
                digitsForTrial.push(singleNumber);
            }
        } else {
            if ((digitSpan > 9)) {
                singleNumber = random_item(numbersToChoose);
                if (((digitsForTrial.length < 9) && (util.count(digitsForTrial, singleNumber) === 0))) {
                    digitsForTrial.push(singleNumber);
                }
                if (((digitsForTrial.length >= 9) && (util.count(digitsForTrial, singleNumber) < 2))) {
                    digitsForTrial.push(singleNumber);
                }
            }
        }
    }
    checkingNumbers = true;
    startN = 1;
    endN = (digitsForTrial.length - 1);
    while (checkingNumbers) {
        for (var n, _pj_c = 0, _pj_a = util.range(startN, endN), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            n = _pj_a[_pj_c];
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] + 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] - 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
            if (((digitsForTrial[n] === (digitsForTrial[(n - 1)] - 1)) && (digitsForTrial[n] === (digitsForTrial[(n + 1)] + 1)))) {
                tmpFirst = digitsForTrial[n];
                tmpSecond = digitsForTrial[(n - 1)];
                digitsForTrial[n] = tmpSecond;
                digitsForTrial[(n - 1)] = tmpFirst;
            }
        }
        checkingNumbers = false;
    }
    
    //console.log("digitSpan:", digitSpan)
    //console.log("digitSpan:", digitsForTrial)
    // keep track of which components have finished
    selectNumbersBSComponents = [];
    
    for (const thisComponent of selectNumbersBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function selectNumbersBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'selectNumbersBS' ---
    // get current time
    t = selectNumbersBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selectNumbersBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function selectNumbersBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'selectNumbersBS' ---
    for (const thisComponent of selectNumbersBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var showNumbersBSComponents;
function showNumbersBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'showNumbersBS' ---
    t = 0;
    showNumbersBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from getTmpNumberCodeBS
    tmpNumber = digitsForTrial[digitLoopBS.thisN];
    
    presentation_textBS.setText(tmpNumber);
    // keep track of which components have finished
    showNumbersBSComponents = [];
    showNumbersBSComponents.push(fixationBS);
    showNumbersBSComponents.push(presentation_textBS);
    
    for (const thisComponent of showNumbersBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function showNumbersBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'showNumbersBS' ---
    // get current time
    t = showNumbersBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationBS* updates
    if (t >= 0.0 && fixationBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationBS.tStart = t;  // (not accounting for frame time here)
      fixationBS.frameNStart = frameN;  // exact frame index
      
      fixationBS.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationBS.setAutoDraw(false);
    }
    
    // *presentation_textBS* updates
    if (t >= 1 && presentation_textBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentation_textBS.tStart = t;  // (not accounting for frame time here)
      presentation_textBS.frameNStart = frameN;  // exact frame index
      
      presentation_textBS.setAutoDraw(true);
    }

    frameRemains = 1 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentation_textBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentation_textBS.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of showNumbersBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function showNumbersBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'showNumbersBS' ---
    for (const thisComponent of showNumbersBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from getTmpNumberCodeBS
    psychoJS.experiment.addData("digitsForTrial", digitsForTrial);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RecallBSComponents;
function RecallBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RecallBS' ---
    t = 0;
    RecallBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textboxBS.setText('');
    textboxBS.refresh();
    // setup some python lists for storing info about the mouseBS
    mouseBS.clicked_name = [];
    gotValidClick = false; // until a click is received
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallBSComponents = [];
    RecallBSComponents.push(recall_txtBS);
    RecallBSComponents.push(textboxBS);
    RecallBSComponents.push(cont_buttonBS);
    RecallBSComponents.push(mouseBS);
    
    for (const thisComponent of RecallBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecallBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RecallBS' ---
    // get current time
    t = RecallBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txtBS* updates
    if (t >= 0 && recall_txtBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txtBS.tStart = t;  // (not accounting for frame time here)
      recall_txtBS.frameNStart = frameN;  // exact frame index
      
      recall_txtBS.setAutoDraw(true);
    }

    
    // *textboxBS* updates
    if (t >= 0.0 && textboxBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxBS.tStart = t;  // (not accounting for frame time here)
      textboxBS.frameNStart = frameN;  // exact frame index
      
      textboxBS.setAutoDraw(true);
    }

    
    // *cont_buttonBS* updates
    if (t >= 0.0 && cont_buttonBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_buttonBS.tStart = t;  // (not accounting for frame time here)
      cont_buttonBS.frameNStart = frameN;  // exact frame index
      
      cont_buttonBS.setAutoDraw(true);
    }

    // *mouseBS* updates
    if (t >= 0.0 && mouseBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseBS.tStart = t;  // (not accounting for frame time here)
      mouseBS.frameNStart = frameN;  // exact frame index
      
      mouseBS.status = PsychoJS.Status.STARTED;
      mouseBS.mouseClock.reset();
      prevButtonState = mouseBS.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseBS.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseBS.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_buttonBS]) {
            if (obj.contains(mouseBS)) {
              gotValidClick = true;
              mouseBS.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecallBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RecallBS' ---
    for (const thisComponent of RecallBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textboxBS.text',textboxBS.text)
    // Run 'End Routine' code from code_3BS
    function reversed(x) {
        var revList;
        revList = [];
        for (var i = 0, _pj_a = x.length; (i < _pj_a); i += 1) {
            revList.push(x[((x.length - 1) - i)]);
        }
        return revList;
    }
    
    digitsForTrial = reversed(digitsForTrial)
    //console.log("reversed digits:", digitsForTrial)
    
    for (var r, _pj_c = 0, _pj_a = util.range(digitsForTrial.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        r = _pj_a[_pj_c];
        digitsForTrial[r] = digitsForTrial[r].toString();
    }
    digitsForTrial = digitsForTrial.join("");
    if ((textboxBS.text === digitsForTrial.toString())) {
        correctCount = 1;
        fbTxt = "Correct!";
    } else {
        correctCount = 0;
        fbTxt = "Incorrect";
    }
    psychoJS.experiment.addData("correct", correctCount);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouseBS.getPos();
    _mouseButtons = mouseBS.getPressed();
    psychoJS.experiment.addData('mouseBS.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouseBS.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouseBS.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouseBS.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouseBS.rightButton', _mouseButtons[2]);
    if (mouseBS.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouseBS.clicked_name', mouseBS.clicked_name[0]);}
    // the Routine "RecallBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FeedbackBSComponents;
function FeedbackBSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FeedbackBS' ---
    t = 0;
    FeedbackBSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedback_textBS.setText(fbTxt);
    // keep track of which components have finished
    FeedbackBSComponents = [];
    FeedbackBSComponents.push(feedback_textBS);
    
    for (const thisComponent of FeedbackBSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackBSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FeedbackBS' ---
    // get current time
    t = FeedbackBSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_textBS* updates
    if (t >= 0.0 && feedback_textBS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_textBS.tStart = t;  // (not accounting for frame time here)
      feedback_textBS.frameNStart = frameN;  // exact frame index
      
      feedback_textBS.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_textBS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_textBS.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackBSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackBSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FeedbackBS' ---
    for (const thisComponent of FeedbackBSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ENDComponents;
function ENDRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'END' ---
    t = 0;
    ENDClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ENDComponents = [];
    ENDComponents.push(ThankYou);
    
    for (const thisComponent of ENDComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ENDRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'END' ---
    // get current time
    t = ENDClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ThankYou* updates
    if (t >= 0.0 && ThankYou.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ThankYou.tStart = t;  // (not accounting for frame time here)
      ThankYou.frameNStart = frameN;  // exact frame index
      
      ThankYou.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ThankYou.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ThankYou.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ENDComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ENDRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'END' ---
    for (const thisComponent of ENDComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  // Run 'End Experiment' code from codeFeedbackReal_dynamic
  psychoJS.experiment.addData("outcomes", outcomes);
  psychoJS.experiment.addData("choices", choices);
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
