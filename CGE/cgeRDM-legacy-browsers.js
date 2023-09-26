/*************** 
 * Cgerdm Test *
 ***************/


// store info about the experiment session:
let expName = 'cgeRDM';  // from the Builder filename that created this script
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
  psychoJS.setRedirectUrls(('https://udenver.qualtrics.com/jfe/form/SV_a4qaGzutOwOjcPk?PROLIFIC_PID=' + expInfo['participant']), 'https://app.prolific.co/submissions/complete?cc=C7B3UXTE');

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
    
    settingUpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    settingUpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    settingUpComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    pracStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    pracStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    pracStartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    trials.forEach(function() {
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
    });
    
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
    staticRDM.forEach(function() {
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
    });
    
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
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(computeEstimatesRoutineBegin(snapshot));
      trials_2LoopScheduler.add(computeEstimatesRoutineEachFrame());
      trials_2LoopScheduler.add(computeEstimatesRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
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
    dynamicRDM.forEach(function() {
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
    });
    
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
    
    practiceTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    practiceTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    practiceTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    isiPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    isiPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    isiPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    itiPrac_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    itiPrac_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    itiPrac_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    postPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    postPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    postPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    choiceWindowComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    choiceWindowComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    choiceWindowComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    isiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    isiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    isiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    showOutcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    showOutcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    showOutcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    computeEstimatesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    computeEstimatesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    computeEstimatesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    loadDynamicChoicesetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    loadDynamicChoicesetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    loadDynamicChoicesetComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    startDynamicTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    startDynamicTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    startDynamicTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    showOutcomeDynamicComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    showOutcomeDynamicComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    showOutcomeDynamicComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    rdmToSpanTransitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    rdmToSpanTransitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    rdmToSpanTransitionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    ENDComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    ENDComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    ENDComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
