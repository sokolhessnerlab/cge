/********************* 
 * Cgerdm_Draft Test *
 *********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'cgeRDM_draft';  // from the Builder filename that created this script
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
  color: new util.Color([0.5216, 0.5216, 0.5216]),
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
flowScheduler.add(SetUpRoutineBegin());
flowScheduler.add(SetUpRoutineEachFrame());
flowScheduler.add(SetUpRoutineEnd());
flowScheduler.add(cgeRDMstartRoutineBegin());
flowScheduler.add(cgeRDMstartRoutineEachFrame());
flowScheduler.add(cgeRDMstartRoutineEnd());
flowScheduler.add(pracStartRoutineBegin());
flowScheduler.add(pracStartRoutineEachFrame());
flowScheduler.add(pracStartRoutineEnd());
const pracTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracTrialsLoopBegin(pracTrialsLoopScheduler));
flowScheduler.add(pracTrialsLoopScheduler);
flowScheduler.add(pracTrialsLoopEnd);
flowScheduler.add(staticStartRoutineBegin());
flowScheduler.add(staticStartRoutineEachFrame());
flowScheduler.add(staticStartRoutineEnd());
const staticTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(staticTrialsLoopBegin(staticTrialsLoopScheduler));
flowScheduler.add(staticTrialsLoopScheduler);
flowScheduler.add(staticTrialsLoopEnd);
const BestFitLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BestFitLoopBegin(BestFitLoopScheduler));
flowScheduler.add(BestFitLoopScheduler);
flowScheduler.add(BestFitLoopEnd);
flowScheduler.add(loadingDynamicChoicesRoutineBegin());
flowScheduler.add(loadingDynamicChoicesRoutineEachFrame());
flowScheduler.add(loadingDynamicChoicesRoutineEnd());
flowScheduler.add(dynamicStartRoutineBegin());
flowScheduler.add(dynamicStartRoutineEachFrame());
flowScheduler.add(dynamicStartRoutineEnd());
const dynamicTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(dynamicTrialsLoopBegin(dynamicTrialsLoopScheduler));
flowScheduler.add(dynamicTrialsLoopScheduler);
flowScheduler.add(dynamicTrialsLoopEnd);
flowScheduler.add(cgeRDMendRoutineBegin());
flowScheduler.add(cgeRDMendRoutineEachFrame());
flowScheduler.add(cgeRDMendRoutineEnd());
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
    {'name': 'cgeRDMPractice.xlsx', 'path': 'cgeRDMPractice.xlsx'},
    {'name': 'CGT-choice-set.csv', 'path': 'CGT-choice-set.csv'}
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


var SetUpClock;
var instructionsTextHeight;
var lettersTextHeight;
var wrap;
var cgeRDMstartClock;
var CGErdmStartText;
var CGErdmStartResp;
var pracStartClock;
var pracStartText;
var pracStartResp;
var pracChoiceClock;
var textHeight;
var pracCircLeft;
var pracCircRight;
var pracRiskLine;
var pracORtext;
var pracLossText;
var pracGainText;
var pracSafeText;
var pracVleft;
var pracNright;
var pracChoiceResp;
var pracISIClock;
var isiPracFix;
var pracOutcomeClock;
var noRespLoc;
var ocLoc;
var ocGambleLoc;
var ocSafeLoc;
var hideGamLoc;
var pracNoRespText;
var pracRiskOC;
var pracSafeOC;
var pracOCtext;
var pracHideRisk;
var pracITIClock;
var itiPracFix;
var staticStartClock;
var staticStartText;
var staticStartResp;
var realChoiceClock;
var realCircLeft;
var realCircRight;
var realRiskLine;
var realORtext;
var realLossText;
var realGainText;
var realSafeText;
var realVleft;
var realNright;
var realChoiceResp;
var realISIClock;
var isiFix;
var staticOutcomeClock;
var choices;
var outcomes;
var staticNoRespText;
var staticRiskOC;
var staticSafeOC;
var staticOCtext;
var staticHideRisk;
var realITIClock;
var itiFix;
var computeBestFitClock;
var setupBestFit;
var loadingDynamicChoicesClock;
var text;
var loadDynamicChoices;
var dynamicStartClock;
var dynamicStartText;
var dynamicStartResp;
var dynamicOutcomeClock;
var dynamicNoRespText;
var dynamicRiskOC;
var dynamicSafeOC;
var dynamicOCtext;
var dynamicHideRisk;
var cgeRDMendClock;
var cgeRDMendText;
var cgeRDMendResp;
var ENDClock;
var ThankYou;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "SetUp"
  SetUpClock = new util.Clock();
  // Run 'Begin Experiment' code from setupCode
  instructionsTextHeight = 0.05;
  lettersTextHeight = 0.1;
  wrap = 1.5;
  
  var initITIstatic
  var initITIdynamic
  
  
  
  // Initialize components for Routine "cgeRDMstart"
  cgeRDMstartClock = new util.Clock();
  CGErdmStartText = new visual.TextStim({
    win: psychoJS.window,
    name: 'CGErdmStartText',
    text: 'As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nYou may press "V" to select the option on the left and "N" to select the option on the right.\n\nPress "enter" to move on to the next screen.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  CGErdmStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracStart"
  pracStartClock = new util.Clock();
  pracStartText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracStartText',
    text: 'There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  pracStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracChoice"
  pracChoiceClock = new util.Clock();
  // Run 'Begin Experiment' code from pracChoiceRandLoc
  textHeight = 0.05;
  
  pracCircLeft = new visual.Polygon ({
    win: psychoJS.window, name: 'pracCircLeft', 
    edges: leftShape, size:[0.5, 0.5],
    ori: 0, pos: circLeftLoc,
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  pracCircRight = new visual.Polygon ({
    win: psychoJS.window, name: 'pracCircRight', 
    edges: rightShape, size:[0.5, 0.5],
    ori: 0, pos: circRightLoc,
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  pracRiskLine = new visual.Polygon ({
    win: psychoJS.window, name: 'pracRiskLine', 
    edges: 4, size:[0.5, 0.01],
    ori: 0, pos: [0, 0],
    lineWidth: 3, lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  pracORtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracORtext',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: ORtextLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -4.0 
  });
  
  pracLossText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracLossText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -5.0 
  });
  
  pracGainText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracGainText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -6.0 
  });
  
  pracSafeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracSafeText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -7.0 
  });
  
  pracVleft = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracVleft',
    text: 'V-Left',
    font: 'Arial',
    units: undefined, 
    pos: VleftLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -8.0 
  });
  
  pracNright = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracNright',
    text: 'N-Right',
    font: 'Arial',
    units: undefined, 
    pos: NrightLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -9.0 
  });
  
  pracChoiceResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracISI"
  pracISIClock = new util.Clock();
  isiPracFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiPracFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "pracOutcome"
  pracOutcomeClock = new util.Clock();
  var outcome, noRespLoc, ocLoc, ocGambleLoc, ocSafeLoc, hideGamLoc, pracFeedbackRounded, extraITI;
  
  
  
  noRespLoc = [0,0]
  ocLoc= [0,0]
  ocGambleLoc = [0,0]
  ocSafeLoc = [0,0]
  hideGamLoc = [0,0]
  
  pracNoRespText = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracNoRespText',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: textHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  pracRiskOC = new visual.Polygon({
    win: psychoJS.window, name: 'pracRiskOC', 
    edges: 100, size:[0.5, 0.5],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  pracSafeOC = new visual.Polygon({
    win: psychoJS.window, name: 'pracSafeOC', 
    edges: 100, size:[0.5, 0.5],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  pracOCtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracOCtext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  pracHideRisk = new visual.Polygon ({
    win: psychoJS.window, name: 'pracHideRisk', 
    edges: 4, size:[0.6, 0.3],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "pracITI"
  pracITIClock = new util.Clock();
  itiPracFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiPracFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "staticStart"
  staticStartClock = new util.Clock();
  staticStartText = new visual.TextStim({
    win: psychoJS.window,
    name: 'staticStartText',
    text: 'Practice complete.\n\nWhen you are ready to start ROUND 1 of the task, press "V" or "N".\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  staticStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "realChoice"
  realChoiceClock = new util.Clock();
  // Run 'Begin Experiment' code from realChoiceRandLoc
  var realloc
  realCircLeft = new visual.Rect ({
    win: psychoJS.window, name: 'realCircLeft', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: circLeftLoc,
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  realCircRight = new visual.Rect ({
    win: psychoJS.window, name: 'realCircRight', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: circRightLoc,
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  realRiskLine = new visual.Rect ({
    win: psychoJS.window, name: 'realRiskLine', 
    width: [0.5, 0.01][0], height: [0.5, 0.01][1],
    ori: 0, pos: [0, 0],
    lineWidth: 3, lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  realORtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'realORtext',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: ORtextLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -4.0 
  });
  
  realLossText = new visual.TextStim({
    win: psychoJS.window,
    name: 'realLossText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -5.0 
  });
  
  realGainText = new visual.TextStim({
    win: psychoJS.window,
    name: 'realGainText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -6.0 
  });
  
  realSafeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'realSafeText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -7.0 
  });
  
  realVleft = new visual.TextStim({
    win: psychoJS.window,
    name: 'realVleft',
    text: 'V-Left',
    font: 'Arial',
    units: undefined, 
    pos: VleftLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -8.0 
  });
  
  realNright = new visual.TextStim({
    win: psychoJS.window,
    name: 'realNright',
    text: 'N-Right',
    font: 'Arial',
    units: undefined, 
    pos: NrightLoc, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -9.0 
  });
  
  realChoiceResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "realISI"
  realISIClock = new util.Clock();
  isiFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "staticOutcome"
  staticOutcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from staticOCcode
  var actualITI
  choices= []
  outcomes = []
  
  
  staticNoRespText = new visual.TextStim({
    win: psychoJS.window,
    name: 'staticNoRespText',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  staticRiskOC = new visual.Rect ({
    win: psychoJS.window, name: 'staticRiskOC', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  staticSafeOC = new visual.Rect ({
    win: psychoJS.window, name: 'staticSafeOC', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 0.0667), 0.6392, 1.0]),
    fillColor: new util.Color([(- 0.0667), 0.6392, 1.0]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  staticOCtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'staticOCtext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  staticHideRisk = new visual.Rect ({
    win: psychoJS.window, name: 'staticHideRisk', 
    width: [0.6, 0.3][0], height: [0.6, 0.3][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "realITI"
  realITIClock = new util.Clock();
  itiFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "computeBestFit"
  computeBestFitClock = new util.Clock();
  setupBestFit = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupBestFit',
    text: 'ROUND 1 of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "loadingDynamicChoices"
  loadingDynamicChoicesClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  loadDynamicChoices = {
    status: PsychoJS.Status.NOT_STARTED
  };
  // Initialize components for Routine "dynamicStart"
  dynamicStartClock = new util.Clock();
  dynamicStartText = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynamicStartText',
    text: 'When you are ready to start ROUND 2 of the task, press "V" or "N".',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: undefined,
    depth: 0.0 
  });
  
  dynamicStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "dynamicOutcome"
  dynamicOutcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from dynamicOCcode
  choices= []
  outcomes = []
  
  
  dynamicNoRespText = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynamicNoRespText',
    text: 'You did not respond in time\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  dynamicRiskOC = new visual.Rect ({
    win: psychoJS.window, name: 'dynamicRiskOC', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  dynamicSafeOC = new visual.Rect ({
    win: psychoJS.window, name: 'dynamicSafeOC', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  dynamicOCtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynamicOCtext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  dynamicHideRisk = new visual.Rect ({
    win: psychoJS.window, name: 'dynamicHideRisk', 
    width: [0.6, 0.3][0], height: [0.6, 0.3][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "cgeRDMend"
  cgeRDMendClock = new util.Clock();
  cgeRDMendText = new visual.TextStim({
    win: psychoJS.window,
    name: 'cgeRDMendText',
    text: "You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: undefined,
    depth: 0.0 
  });
  
  cgeRDMendResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
    color: new util.Color(color2),  opacity: undefined,
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
var SetUpComponents;
function SetUpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SetUp' ---
    t = 0;
    SetUpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    SetUpComponents = [];
    
    for (const thisComponent of SetUpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SetUpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SetUp' ---
    // get current time
    t = SetUpClock.getTime();
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
    for (const thisComponent of SetUpComponents)
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
function SetUpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SetUp' ---
    for (const thisComponent of SetUpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from setupCode
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
    
    // the Routine "SetUp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _CGErdmStartResp_allKeys;
var cgeRDMstartComponents;
function cgeRDMstartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cgeRDMstart' ---
    t = 0;
    cgeRDMstartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    CGErdmStartResp.keys = undefined;
    CGErdmStartResp.rt = undefined;
    _CGErdmStartResp_allKeys = [];
    // keep track of which components have finished
    cgeRDMstartComponents = [];
    cgeRDMstartComponents.push(CGErdmStartText);
    cgeRDMstartComponents.push(CGErdmStartResp);
    
    for (const thisComponent of cgeRDMstartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cgeRDMstartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cgeRDMstart' ---
    // get current time
    t = cgeRDMstartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CGErdmStartText* updates
    if (t >= 0.0 && CGErdmStartText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CGErdmStartText.tStart = t;  // (not accounting for frame time here)
      CGErdmStartText.frameNStart = frameN;  // exact frame index
      
      CGErdmStartText.setAutoDraw(true);
    }

    
    // *CGErdmStartResp* updates
    if (t >= 2 && CGErdmStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CGErdmStartResp.tStart = t;  // (not accounting for frame time here)
      CGErdmStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CGErdmStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CGErdmStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CGErdmStartResp.clearEvents(); });
    }

    if (CGErdmStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = CGErdmStartResp.getKeys({keyList: ['return'], waitRelease: false});
      _CGErdmStartResp_allKeys = _CGErdmStartResp_allKeys.concat(theseKeys);
      if (_CGErdmStartResp_allKeys.length > 0) {
        CGErdmStartResp.keys = _CGErdmStartResp_allKeys[_CGErdmStartResp_allKeys.length - 1].name;  // just the last key pressed
        CGErdmStartResp.rt = _CGErdmStartResp_allKeys[_CGErdmStartResp_allKeys.length - 1].rt;
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
    for (const thisComponent of cgeRDMstartComponents)
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


function cgeRDMstartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cgeRDMstart' ---
    for (const thisComponent of cgeRDMstartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(CGErdmStartResp.corr, level);
    }
    psychoJS.experiment.addData('CGErdmStartResp.keys', CGErdmStartResp.keys);
    if (typeof CGErdmStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('CGErdmStartResp.rt', CGErdmStartResp.rt);
        routineTimer.reset();
        }
    
    CGErdmStartResp.stop();
    // the Routine "cgeRDMstart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _pracStartResp_allKeys;
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
    pracStartResp.keys = undefined;
    pracStartResp.rt = undefined;
    _pracStartResp_allKeys = [];
    // keep track of which components have finished
    pracStartComponents = [];
    pracStartComponents.push(pracStartText);
    pracStartComponents.push(pracStartResp);
    
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
    
    // *pracStartText* updates
    if (t >= 0.0 && pracStartText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracStartText.tStart = t;  // (not accounting for frame time here)
      pracStartText.frameNStart = frameN;  // exact frame index
      
      pracStartText.setAutoDraw(true);
    }

    
    // *pracStartResp* updates
    if (t >= 2 && pracStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracStartResp.tStart = t;  // (not accounting for frame time here)
      pracStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pracStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pracStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pracStartResp.clearEvents(); });
    }

    if (pracStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pracStartResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _pracStartResp_allKeys = _pracStartResp_allKeys.concat(theseKeys);
      if (_pracStartResp_allKeys.length > 0) {
        pracStartResp.keys = _pracStartResp_allKeys[_pracStartResp_allKeys.length - 1].name;  // just the last key pressed
        pracStartResp.rt = _pracStartResp_allKeys[_pracStartResp_allKeys.length - 1].rt;
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
      currentLoop.addResponse(pracStartResp.corr, level);
    }
    psychoJS.experiment.addData('pracStartResp.keys', pracStartResp.keys);
    if (typeof pracStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pracStartResp.rt', pracStartResp.rt);
        routineTimer.reset();
        }
    
    pracStartResp.stop();
    // the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pracTrials;
function pracTrialsLoopBegin(pracTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pracTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'cgeRDMPractice.xlsx', '0:2'),
      seed: undefined, name: 'pracTrials'
    });
    psychoJS.experiment.addLoop(pracTrials); // add the loop to the experiment
    currentLoop = pracTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracTrial of pracTrials) {
      snapshot = pracTrials.getSnapshot();
      pracTrialsLoopScheduler.add(importConditions(snapshot));
      pracTrialsLoopScheduler.add(pracChoiceRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(pracChoiceRoutineEachFrame());
      pracTrialsLoopScheduler.add(pracChoiceRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(pracISIRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(pracISIRoutineEachFrame());
      pracTrialsLoopScheduler.add(pracISIRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(pracOutcomeRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(pracOutcomeRoutineEachFrame());
      pracTrialsLoopScheduler.add(pracOutcomeRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(pracITIRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(pracITIRoutineEachFrame());
      pracTrialsLoopScheduler.add(pracITIRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(pracTrialsLoopEndIteration(pracTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function pracTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(pracTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function pracTrialsLoopEndIteration(scheduler, snapshot) {
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


var staticTrials;
function staticTrialsLoopBegin(staticTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    staticTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'CGT-choice-set.csv', '0:2'),
      seed: undefined, name: 'staticTrials'
    });
    psychoJS.experiment.addLoop(staticTrials); // add the loop to the experiment
    currentLoop = staticTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStaticTrial of staticTrials) {
      snapshot = staticTrials.getSnapshot();
      staticTrialsLoopScheduler.add(importConditions(snapshot));
      staticTrialsLoopScheduler.add(realChoiceRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realChoiceRoutineEachFrame());
      staticTrialsLoopScheduler.add(realChoiceRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(realISIRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realISIRoutineEachFrame());
      staticTrialsLoopScheduler.add(realISIRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(staticOutcomeRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(staticOutcomeRoutineEachFrame());
      staticTrialsLoopScheduler.add(staticOutcomeRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(realITIRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realITIRoutineEachFrame());
      staticTrialsLoopScheduler.add(realITIRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(staticTrialsLoopEndIteration(staticTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function staticTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(staticTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function staticTrialsLoopEndIteration(scheduler, snapshot) {
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


var BestFit;
function BestFitLoopBegin(BestFitLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    BestFit = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'BestFit'
    });
    psychoJS.experiment.addLoop(BestFit); // add the loop to the experiment
    currentLoop = BestFit;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBestFit of BestFit) {
      snapshot = BestFit.getSnapshot();
      BestFitLoopScheduler.add(importConditions(snapshot));
      BestFitLoopScheduler.add(computeBestFitRoutineBegin(snapshot));
      BestFitLoopScheduler.add(computeBestFitRoutineEachFrame());
      BestFitLoopScheduler.add(computeBestFitRoutineEnd(snapshot));
      BestFitLoopScheduler.add(BestFitLoopEndIteration(BestFitLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function BestFitLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(BestFit);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function BestFitLoopEndIteration(scheduler, snapshot) {
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


var dynamicTrials;
function dynamicTrialsLoopBegin(dynamicTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    dynamicTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, fname[0], '0:2'),
      seed: undefined, name: 'dynamicTrials'
    });
    psychoJS.experiment.addLoop(dynamicTrials); // add the loop to the experiment
    currentLoop = dynamicTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDynamicTrial of dynamicTrials) {
      snapshot = dynamicTrials.getSnapshot();
      dynamicTrialsLoopScheduler.add(importConditions(snapshot));
      dynamicTrialsLoopScheduler.add(realChoiceRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realChoiceRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realChoiceRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(realISIRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realISIRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realISIRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(dynamicOutcomeRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(dynamicOutcomeRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(dynamicOutcomeRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(realITIRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realITIRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realITIRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(dynamicTrialsLoopEndIteration(dynamicTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function dynamicTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(dynamicTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function dynamicTrialsLoopEndIteration(scheduler, snapshot) {
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
var _pracChoiceResp_allKeys;
var pracChoiceComponents;
function pracChoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracChoice' ---
    t = 0;
    pracChoiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from pracChoiceRandLoc
    var pracLossRounded, pracGainRounded, pracSafeRounded
    
    if ((loc === 1)) {
        targetPos = [(- 0.35), 0];
    } else {
        targetPos = [0.35, 0];
    }
    if ((loc === 1)) {
        lossLoc = [(- 0.35), (- 0.1)];
        gainLoc = [(- 0.35), 0.1];
        safeLoc = [0.35, 0];
    } else {
        lossLoc = [0.35, (- 0.1)];
        gainLoc = [0.35, 0.1];
        safeLoc = [(- 0.35), 0];
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
    pracCircRight.setFillColor(new util.Color(color2));
    pracCircRight.setLineColor(new util.Color(color2));
    pracRiskLine.setPos(riskLineLoc);
    pracLossText.setPos(lossLoc);
    pracLossText.setText(pracLossRounded);
    pracGainText.setPos(gainLoc);
    pracGainText.setText(pracGainRounded);
    pracSafeText.setPos(safeLoc);
    pracSafeText.setText(pracSafeRounded);
    pracChoiceResp.keys = undefined;
    pracChoiceResp.rt = undefined;
    _pracChoiceResp_allKeys = [];
    // keep track of which components have finished
    pracChoiceComponents = [];
    pracChoiceComponents.push(pracCircLeft);
    pracChoiceComponents.push(pracCircRight);
    pracChoiceComponents.push(pracRiskLine);
    pracChoiceComponents.push(pracORtext);
    pracChoiceComponents.push(pracLossText);
    pracChoiceComponents.push(pracGainText);
    pracChoiceComponents.push(pracSafeText);
    pracChoiceComponents.push(pracVleft);
    pracChoiceComponents.push(pracNright);
    pracChoiceComponents.push(pracChoiceResp);
    
    for (const thisComponent of pracChoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function pracChoiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracChoice' ---
    // get current time
    t = pracChoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracCircLeft* updates
    if (t >= 0 && pracCircLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracCircLeft.tStart = t;  // (not accounting for frame time here)
      pracCircLeft.frameNStart = frameN;  // exact frame index
      
      pracCircLeft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracCircLeft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracCircLeft.setAutoDraw(false);
    }
    
    // *pracCircRight* updates
    if (t >= 0.0 && pracCircRight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracCircRight.tStart = t;  // (not accounting for frame time here)
      pracCircRight.frameNStart = frameN;  // exact frame index
      
      pracCircRight.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracCircRight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracCircRight.setAutoDraw(false);
    }
    
    // *pracRiskLine* updates
    if (t >= 0.0 && pracRiskLine.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracRiskLine.tStart = t;  // (not accounting for frame time here)
      pracRiskLine.frameNStart = frameN;  // exact frame index
      
      pracRiskLine.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracRiskLine.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracRiskLine.setAutoDraw(false);
    }
    
    // *pracORtext* updates
    if (t >= 0.0 && pracORtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracORtext.tStart = t;  // (not accounting for frame time here)
      pracORtext.frameNStart = frameN;  // exact frame index
      
      pracORtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracORtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracORtext.setAutoDraw(false);
    }
    
    // *pracLossText* updates
    if (t >= 0.0 && pracLossText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracLossText.tStart = t;  // (not accounting for frame time here)
      pracLossText.frameNStart = frameN;  // exact frame index
      
      pracLossText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracLossText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracLossText.setAutoDraw(false);
    }
    
    // *pracGainText* updates
    if (t >= 0.0 && pracGainText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracGainText.tStart = t;  // (not accounting for frame time here)
      pracGainText.frameNStart = frameN;  // exact frame index
      
      pracGainText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracGainText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracGainText.setAutoDraw(false);
    }
    
    // *pracSafeText* updates
    if (t >= 0.0 && pracSafeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracSafeText.tStart = t;  // (not accounting for frame time here)
      pracSafeText.frameNStart = frameN;  // exact frame index
      
      pracSafeText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracSafeText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracSafeText.setAutoDraw(false);
    }
    
    // *pracVleft* updates
    if (t >= 0 && pracVleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracVleft.tStart = t;  // (not accounting for frame time here)
      pracVleft.frameNStart = frameN;  // exact frame index
      
      pracVleft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracVleft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracVleft.setAutoDraw(false);
    }
    
    // *pracNright* updates
    if (t >= 0 && pracNright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracNright.tStart = t;  // (not accounting for frame time here)
      pracNright.frameNStart = frameN;  // exact frame index
      
      pracNright.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracNright.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracNright.setAutoDraw(false);
    }
    
    // *pracChoiceResp* updates
    if (t >= 0 && pracChoiceResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracChoiceResp.tStart = t;  // (not accounting for frame time here)
      pracChoiceResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pracChoiceResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pracChoiceResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pracChoiceResp.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracChoiceResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracChoiceResp.status = PsychoJS.Status.FINISHED;
  }

    if (pracChoiceResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pracChoiceResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _pracChoiceResp_allKeys = _pracChoiceResp_allKeys.concat(theseKeys);
      if (_pracChoiceResp_allKeys.length > 0) {
        pracChoiceResp.keys = _pracChoiceResp_allKeys[_pracChoiceResp_allKeys.length - 1].name;  // just the last key pressed
        pracChoiceResp.rt = _pracChoiceResp_allKeys[_pracChoiceResp_allKeys.length - 1].rt;
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
    for (const thisComponent of pracChoiceComponents)
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


function pracChoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracChoice' ---
    for (const thisComponent of pracChoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(pracChoiceResp.corr, level);
    }
    psychoJS.experiment.addData('pracChoiceResp.keys', pracChoiceResp.keys);
    if (typeof pracChoiceResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pracChoiceResp.rt', pracChoiceResp.rt);
        routineTimer.reset();
        }
    
    pracChoiceResp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pracISIComponents;
function pracISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracISI' ---
    t = 0;
    pracISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    pracISIComponents = [];
    pracISIComponents.push(isiPracFix);
    
    for (const thisComponent of pracISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pracISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracISI' ---
    // get current time
    t = pracISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *isiPracFix* updates
    if (t >= 0.0 && isiPracFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isiPracFix.tStart = t;  // (not accounting for frame time here)
      isiPracFix.frameNStart = frameN;  // exact frame index
      
      isiPracFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + isi - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isiPracFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isiPracFix.setAutoDraw(false);
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
    for (const thisComponent of pracISIComponents)
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


function pracISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracISI' ---
    for (const thisComponent of pracISIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "pracISI" was not non-slip safe, so reset the non-slip timer
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
var pracOutcomeComponents;
function pracOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracOutcome' ---
    t = 0;
    pracOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from pracOCcode
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (pracChoiceResp.keys === undefined){
        outcome = " ";
        noRespLoc = [0,0];
        ocLoc = [5,5];
        ocGambleLoc = [5,5];
        ocSafeLoc = [5,5];
        hideGamLoc = [5,5];
        extraITI = 0;
    }else if(pracChoiceResp.keys =='v' && loc ==1) {
        outcome = random_item([riskyGain, riskyLoss])
        extraITI = 4-pracChoiceResp.rt
        if(outcome == riskyGain){
            ocLoc = [-.35,.1];
            ocGambleLoc = [-.35,0];
            ocSafeLoc = [5,5];
            noRespLoc = [5,5];
            hideGamLoc = [-.35,-.125];
        } else if (outcome ==riskyLoss){
            ocLoc = [-.35,-.1];
            ocGambleLoc = [-.35,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [-.35,.125];
            noRespLoc = [5,5];
        }
    } else if(pracChoiceResp.keys == 'v' && loc ==2){
        extraITI = 4-pracChoiceResp.rt
        outcome = alternative
        ocLoc = [-.35,0];
        ocGambleLoc = [5,5];
        ocSafeLoc = ocLoc;
        hideGamLoc = ocGambleLoc;
        noRespLoc = [5,5];
    } else if (pracChoiceResp.keys=='n' && loc ==1){
        extraITI = 4-pracChoiceResp.rt
        outcome = alternative
        ocLoc = [.35,0];
        ocGambleLoc = [5,5];
        ocSafeLoc = ocLoc;
        hideGamLoc = ocGambleLoc;
        noRespLoc = [5,5];
    } else if (pracChoiceResp.keys =='n' && loc ==2){
        outcome = random_item([riskyGain, riskyLoss]);
        extraITI = 4-pracChoiceResp.rt
        if (outcome == riskyGain){
            ocLoc = [.35,.1];
            ocGambleLoc = [.35,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [.35,-.125];
            noRespLoc = [5,5];
        } else if (outcome == riskyLoss){
            ocLoc = [.35,-.1];
            ocGambleLoc = [.35,0];
            ocSafeLoc = [5,5];
            hideGamLoc = [.35,.125];
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
    
    pracNoRespText.setPos(noRespLoc);
    pracRiskOC.setPos(ocGambleLoc);
    pracSafeOC.setPos(ocSafeLoc);
    pracOCtext.setColor(new util.Color(color1));
    pracOCtext.setPos(ocLoc);
    pracOCtext.setText(pracFeedbackRounded);
    pracHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    pracOutcomeComponents = [];
    pracOutcomeComponents.push(pracNoRespText);
    pracOutcomeComponents.push(pracRiskOC);
    pracOutcomeComponents.push(pracSafeOC);
    pracOutcomeComponents.push(pracOCtext);
    pracOutcomeComponents.push(pracHideRisk);
    
    for (const thisComponent of pracOutcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pracOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracOutcome' ---
    // get current time
    t = pracOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracNoRespText* updates
    if (t >= 0.0 && pracNoRespText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracNoRespText.tStart = t;  // (not accounting for frame time here)
      pracNoRespText.frameNStart = frameN;  // exact frame index
      
      pracNoRespText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracNoRespText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracNoRespText.setAutoDraw(false);
    }
    
    // *pracRiskOC* updates
    if (t >= 0.0 && pracRiskOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracRiskOC.tStart = t;  // (not accounting for frame time here)
      pracRiskOC.frameNStart = frameN;  // exact frame index
      
      pracRiskOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracRiskOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracRiskOC.setAutoDraw(false);
    }
    
    // *pracSafeOC* updates
    if (t >= 0.0 && pracSafeOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracSafeOC.tStart = t;  // (not accounting for frame time here)
      pracSafeOC.frameNStart = frameN;  // exact frame index
      
      pracSafeOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracSafeOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracSafeOC.setAutoDraw(false);
    }
    
    // *pracOCtext* updates
    if (t >= 0.0 && pracOCtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracOCtext.tStart = t;  // (not accounting for frame time here)
      pracOCtext.frameNStart = frameN;  // exact frame index
      
      pracOCtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracOCtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracOCtext.setAutoDraw(false);
    }
    
    // *pracHideRisk* updates
    if (t >= 0.0 && pracHideRisk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracHideRisk.tStart = t;  // (not accounting for frame time here)
      pracHideRisk.frameNStart = frameN;  // exact frame index
      
      pracHideRisk.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracHideRisk.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracHideRisk.setAutoDraw(false);
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
    for (const thisComponent of pracOutcomeComponents)
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


function pracOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracOutcome' ---
    for (const thisComponent of pracOutcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from pracOCcode
    psychoJS.experiment.addData('outcome', outcome)
    psychoJS.experiment.addData('extraITI', extraITI)
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pracITIComponents;
function pracITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracITI' ---
    t = 0;
    pracITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    pracITIComponents = [];
    pracITIComponents.push(itiPracFix);
    
    for (const thisComponent of pracITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pracITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracITI' ---
    // get current time
    t = pracITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *itiPracFix* updates
    if (t >= 0.0 && itiPracFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      itiPracFix.tStart = t;  // (not accounting for frame time here)
      itiPracFix.frameNStart = frameN;  // exact frame index
      
      itiPracFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (itiPracFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      itiPracFix.setAutoDraw(false);
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
    for (const thisComponent of pracITIComponents)
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


function pracITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracITI' ---
    for (const thisComponent of pracITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "pracITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _staticStartResp_allKeys;
var staticStartComponents;
function staticStartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'staticStart' ---
    t = 0;
    staticStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    staticStartResp.keys = undefined;
    staticStartResp.rt = undefined;
    _staticStartResp_allKeys = [];
    // keep track of which components have finished
    staticStartComponents = [];
    staticStartComponents.push(staticStartText);
    staticStartComponents.push(staticStartResp);
    
    for (const thisComponent of staticStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function staticStartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'staticStart' ---
    // get current time
    t = staticStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *staticStartText* updates
    if (t >= 0.0 && staticStartText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticStartText.tStart = t;  // (not accounting for frame time here)
      staticStartText.frameNStart = frameN;  // exact frame index
      
      staticStartText.setAutoDraw(true);
    }

    
    // *staticStartResp* updates
    if (t >= 0.0 && staticStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticStartResp.tStart = t;  // (not accounting for frame time here)
      staticStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { staticStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { staticStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { staticStartResp.clearEvents(); });
    }

    if (staticStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = staticStartResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _staticStartResp_allKeys = _staticStartResp_allKeys.concat(theseKeys);
      if (_staticStartResp_allKeys.length > 0) {
        staticStartResp.keys = _staticStartResp_allKeys[_staticStartResp_allKeys.length - 1].name;  // just the last key pressed
        staticStartResp.rt = _staticStartResp_allKeys[_staticStartResp_allKeys.length - 1].rt;
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
    for (const thisComponent of staticStartComponents)
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


function staticStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'staticStart' ---
    for (const thisComponent of staticStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(staticStartResp.corr, level);
    }
    psychoJS.experiment.addData('staticStartResp.keys', staticStartResp.keys);
    if (typeof staticStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('staticStartResp.rt', staticStartResp.rt);
        routineTimer.reset();
        }
    
    staticStartResp.stop();
    // the Routine "staticStart" was not non-slip safe, so reset the non-slip timer
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
var _realChoiceResp_allKeys;
var realChoiceComponents;
function realChoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'realChoice' ---
    t = 0;
    realChoiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from realChoiceRandLoc
    var gainLoc, gainRounded, lossLoc, lossRounded, safeLoc, safeRounded, targetPos;
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    realloc = random_item([1, 2]);
    
    if ((realloc === 1)) {
        targetPos = [(- 0.35), 0];
    } else {
        targetPos = [0.35, 0];
    }
    if ((realloc === 1)) {
        lossLoc = [(- 0.35), (- 0.1)];
        gainLoc = [(- 0.35), 0.1];
        safeLoc = [0.35, 0];
    } else {
        lossLoc = [0.35, (- 0.1)];
        gainLoc = [0.35, 0.1];
        safeLoc = [(- 0.35), 0];
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
    
    realCircRight.setFillColor(new util.Color(color2));
    realCircRight.setLineColor(new util.Color(color2));
    realRiskLine.setPos(riskLineLoc);
    realLossText.setPos(lossLoc);
    realLossText.setText(lossRounded);
    realGainText.setPos(gainLoc);
    realGainText.setText(gainRounded);
    realSafeText.setPos(safeLoc);
    realSafeText.setText(safeRounded);
    realChoiceResp.keys = undefined;
    realChoiceResp.rt = undefined;
    _realChoiceResp_allKeys = [];
    // keep track of which components have finished
    realChoiceComponents = [];
    realChoiceComponents.push(realCircLeft);
    realChoiceComponents.push(realCircRight);
    realChoiceComponents.push(realRiskLine);
    realChoiceComponents.push(realORtext);
    realChoiceComponents.push(realLossText);
    realChoiceComponents.push(realGainText);
    realChoiceComponents.push(realSafeText);
    realChoiceComponents.push(realVleft);
    realChoiceComponents.push(realNright);
    realChoiceComponents.push(realChoiceResp);
    
    for (const thisComponent of realChoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function realChoiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'realChoice' ---
    // get current time
    t = realChoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *realCircLeft* updates
    if (t >= 0 && realCircLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realCircLeft.tStart = t;  // (not accounting for frame time here)
      realCircLeft.frameNStart = frameN;  // exact frame index
      
      realCircLeft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realCircLeft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realCircLeft.setAutoDraw(false);
    }
    
    // *realCircRight* updates
    if (t >= 0.0 && realCircRight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realCircRight.tStart = t;  // (not accounting for frame time here)
      realCircRight.frameNStart = frameN;  // exact frame index
      
      realCircRight.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realCircRight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realCircRight.setAutoDraw(false);
    }
    
    // *realRiskLine* updates
    if (t >= 0.0 && realRiskLine.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realRiskLine.tStart = t;  // (not accounting for frame time here)
      realRiskLine.frameNStart = frameN;  // exact frame index
      
      realRiskLine.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realRiskLine.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realRiskLine.setAutoDraw(false);
    }
    
    // *realORtext* updates
    if (t >= 0.0 && realORtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realORtext.tStart = t;  // (not accounting for frame time here)
      realORtext.frameNStart = frameN;  // exact frame index
      
      realORtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realORtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realORtext.setAutoDraw(false);
    }
    
    // *realLossText* updates
    if (t >= 0.0 && realLossText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realLossText.tStart = t;  // (not accounting for frame time here)
      realLossText.frameNStart = frameN;  // exact frame index
      
      realLossText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realLossText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realLossText.setAutoDraw(false);
    }
    
    // *realGainText* updates
    if (t >= 0.0 && realGainText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realGainText.tStart = t;  // (not accounting for frame time here)
      realGainText.frameNStart = frameN;  // exact frame index
      
      realGainText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realGainText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realGainText.setAutoDraw(false);
    }
    
    // *realSafeText* updates
    if (t >= 0.0 && realSafeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realSafeText.tStart = t;  // (not accounting for frame time here)
      realSafeText.frameNStart = frameN;  // exact frame index
      
      realSafeText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realSafeText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realSafeText.setAutoDraw(false);
    }
    
    // *realVleft* updates
    if (t >= 0 && realVleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realVleft.tStart = t;  // (not accounting for frame time here)
      realVleft.frameNStart = frameN;  // exact frame index
      
      realVleft.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realVleft.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realVleft.setAutoDraw(false);
    }
    
    // *realNright* updates
    if (t >= 0 && realNright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realNright.tStart = t;  // (not accounting for frame time here)
      realNright.frameNStart = frameN;  // exact frame index
      
      realNright.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realNright.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realNright.setAutoDraw(false);
    }
    
    // *realChoiceResp* updates
    if (t >= 0 && realChoiceResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realChoiceResp.tStart = t;  // (not accounting for frame time here)
      realChoiceResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { realChoiceResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { realChoiceResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { realChoiceResp.clearEvents(); });
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realChoiceResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realChoiceResp.status = PsychoJS.Status.FINISHED;
  }

    if (realChoiceResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = realChoiceResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _realChoiceResp_allKeys = _realChoiceResp_allKeys.concat(theseKeys);
      if (_realChoiceResp_allKeys.length > 0) {
        realChoiceResp.keys = _realChoiceResp_allKeys[_realChoiceResp_allKeys.length - 1].name;  // just the last key pressed
        realChoiceResp.rt = _realChoiceResp_allKeys[_realChoiceResp_allKeys.length - 1].rt;
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
    for (const thisComponent of realChoiceComponents)
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


function realChoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realChoice' ---
    for (const thisComponent of realChoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from realChoiceRandLoc
    psychoJS.experiment.addData("realloc", realloc);
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(realChoiceResp.corr, level);
    }
    psychoJS.experiment.addData('realChoiceResp.keys', realChoiceResp.keys);
    if (typeof realChoiceResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('realChoiceResp.rt', realChoiceResp.rt);
        routineTimer.reset();
        }
    
    realChoiceResp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var realISIComponents;
function realISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'realISI' ---
    t = 0;
    realISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    realISIComponents = [];
    realISIComponents.push(isiFix);
    
    for (const thisComponent of realISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function realISIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'realISI' ---
    // get current time
    t = realISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *isiFix* updates
    if (t >= 0.0 && isiFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isiFix.tStart = t;  // (not accounting for frame time here)
      isiFix.frameNStart = frameN;  // exact frame index
      
      isiFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isiFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isiFix.setAutoDraw(false);
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
    for (const thisComponent of realISIComponents)
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


function realISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realISI' ---
    for (const thisComponent of realISIComponents) {
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
var staticOutcomeComponents;
function staticOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'staticOutcome' ---
    t = 0;
    staticOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from staticOCcode
    var choicetmp, feedbackRounded, outcometmp, outcomes, choices;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (realChoiceResp.keys === undefined) {
        outcometmp = Math.nan;
        choicetmp = Math.nan;
        noRespLoc = [0, 0];
        ocLoc = [5, 5];
        ocGambleLoc = [5, 5];
        ocSafeLoc = [5, 5];
        hideGamLoc = [5, 5];
        extraITI = 0;
    } else if (realChoiceResp.keys === "v" && realloc === 1) {
         outcometmp = random_item([riskyoption1, riskyoption2]);
         choicetmp = 1;
         extraITI = 4-realChoiceResp.rt
         if (outcometmp === riskyoption1) {
              ocLoc = [(- 0.35), 0.1];
              ocGambleLoc = [(- 0.35), 0];
              ocSafeLoc = [5, 5];
              noRespLoc = [5, 5];
              hideGamLoc = [(- 0.35), (- 0.125)];
         } else if (outcometmp === riskyoption2) {
              ocLoc = [(- 0.35), (- 0.1)];
              ocGambleLoc = [(- 0.35), 0];
              ocSafeLoc = [5, 5];
              hideGamLoc = [(- 0.35), 0.125];
              noRespLoc = [5, 5];
         }
     } else if (realChoiceResp.keys === "v" && realloc === 2) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoiceResp.rt
         ocLoc = [(- 0.35), 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
     } else if (realChoiceResp.keys === "n" && realloc === 1) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoiceResp.rt
         ocLoc = [0.35, 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
    } else if (realChoiceResp.keys === "n" && realloc === 2) {
        outcometmp = random_item([riskyoption1, riskyoption2]);
        choicetmp = 1;
        extraITI = 4-realChoiceResp.rt
        if (outcometmp === riskyoption1) {
            ocLoc = [0.35, 0.1];
            ocGambleLoc = [0.35, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.35, (- 0.125)];
            noRespLoc = [5, 5];
        } else if (outcometmp === riskyoption2) {
            ocLoc = [0.35, (- 0.1)];
            ocGambleLoc = [0.35, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.35, 0.125];
            noRespLoc = [5, 5];
        }
    }
    
    actualITI = initITIstatic[staticTrials.thisN] + extraITI
    
    
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
    
    staticNoRespText.setPos(noRespLoc);
    staticRiskOC.setPos(ocGambleLoc);
    staticSafeOC.setPos(ocSafeLoc);
    staticOCtext.setColor(new util.Color(color1));
    staticOCtext.setPos(ocLoc);
    staticOCtext.setText(feedbackRounded);
    staticHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    staticOutcomeComponents = [];
    staticOutcomeComponents.push(staticNoRespText);
    staticOutcomeComponents.push(staticRiskOC);
    staticOutcomeComponents.push(staticSafeOC);
    staticOutcomeComponents.push(staticOCtext);
    staticOutcomeComponents.push(staticHideRisk);
    
    for (const thisComponent of staticOutcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function staticOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'staticOutcome' ---
    // get current time
    t = staticOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *staticNoRespText* updates
    if (t >= 0.0 && staticNoRespText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticNoRespText.tStart = t;  // (not accounting for frame time here)
      staticNoRespText.frameNStart = frameN;  // exact frame index
      
      staticNoRespText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (staticNoRespText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      staticNoRespText.setAutoDraw(false);
    }
    
    // *staticRiskOC* updates
    if (t >= 0.0 && staticRiskOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticRiskOC.tStart = t;  // (not accounting for frame time here)
      staticRiskOC.frameNStart = frameN;  // exact frame index
      
      staticRiskOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (staticRiskOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      staticRiskOC.setAutoDraw(false);
    }
    
    // *staticSafeOC* updates
    if (t >= 0.0 && staticSafeOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticSafeOC.tStart = t;  // (not accounting for frame time here)
      staticSafeOC.frameNStart = frameN;  // exact frame index
      
      staticSafeOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (staticSafeOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      staticSafeOC.setAutoDraw(false);
    }
    
    // *staticOCtext* updates
    if (t >= 0.0 && staticOCtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticOCtext.tStart = t;  // (not accounting for frame time here)
      staticOCtext.frameNStart = frameN;  // exact frame index
      
      staticOCtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (staticOCtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      staticOCtext.setAutoDraw(false);
    }
    
    // *staticHideRisk* updates
    if (t >= 0.0 && staticHideRisk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      staticHideRisk.tStart = t;  // (not accounting for frame time here)
      staticHideRisk.frameNStart = frameN;  // exact frame index
      
      staticHideRisk.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (staticHideRisk.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      staticHideRisk.setAutoDraw(false);
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
    for (const thisComponent of staticOutcomeComponents)
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


function staticOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'staticOutcome' ---
    for (const thisComponent of staticOutcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from staticOCcode
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


var realITIComponents;
function realITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'realITI' ---
    t = 0;
    realITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    realITIComponents = [];
    realITIComponents.push(itiFix);
    
    for (const thisComponent of realITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function realITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'realITI' ---
    // get current time
    t = realITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *itiFix* updates
    if (t >= 0.0 && itiFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      itiFix.tStart = t;  // (not accounting for frame time here)
      itiFix.frameNStart = frameN;  // exact frame index
      
      itiFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + actualITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (itiFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      itiFix.setAutoDraw(false);
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
    for (const thisComponent of realITIComponents)
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


function realITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realITI' ---
    for (const thisComponent of realITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "realITI" was not non-slip safe, so reset the non-slip timer
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
var computeBestFitComponents;
function computeBestFitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'computeBestFit' ---
    t = 0;
    computeBestFitClock.reset(); // clock
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
    computeBestFitComponents = [];
    computeBestFitComponents.push(setupBestFit);
    
    for (const thisComponent of computeBestFitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function computeBestFitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'computeBestFit' ---
    // get current time
    t = computeBestFitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *setupBestFit* updates
    if (t >= 0 && setupBestFit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupBestFit.tStart = t;  // (not accounting for frame time here)
      setupBestFit.frameNStart = frameN;  // exact frame index
      
      setupBestFit.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (setupBestFit.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      setupBestFit.setAutoDraw(false);
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
    for (const thisComponent of computeBestFitComponents)
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


function computeBestFitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'computeBestFit' ---
    for (const thisComponent of computeBestFitComponents) {
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


var loadingDynamicChoicesComponents;
function loadingDynamicChoicesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'loadingDynamicChoices' ---
    t = 0;
    loadingDynamicChoicesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    loadingDynamicChoicesComponents = [];
    loadingDynamicChoicesComponents.push(text);
    loadingDynamicChoicesComponents.push(loadDynamicChoices);
    
    for (const thisComponent of loadingDynamicChoicesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function loadingDynamicChoicesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'loadingDynamicChoices' ---
    // get current time
    t = loadingDynamicChoicesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // start downloading resources specified by component loadDynamicChoices
    if (t >= 2 && loadDynamicChoices.status === PsychoJS.Status.NOT_STARTED) {
      console.log('register and start downloading resources specified by component loadDynamicChoices');
      await psychoJS.serverManager.prepareResources(core.ServerManager.ALL_RESOURCES);
      loadDynamicChoices.status = PsychoJS.Status.STARTED;
    }
    // check on the resources specified by component loadDynamicChoices
    if (t >= null && loadDynamicChoices.status === PsychoJS.Status.STARTED) {
      if (psychoJS.serverManager.getResourceStatus(core.ServerManager.ALL_RESOURCES) === core.ServerManager.ResourceStatus.DOWNLOADED) {
        console.log('finished downloading resources specified by component loadDynamicChoices');
        loadDynamicChoices.status = PsychoJS.Status.FINISHED;
      } else {
        console.log('resource specified in loadDynamicChoices took longer than expected to download');
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
    for (const thisComponent of loadingDynamicChoicesComponents)
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


function loadingDynamicChoicesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'loadingDynamicChoices' ---
    for (const thisComponent of loadingDynamicChoicesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "loadingDynamicChoices" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _dynamicStartResp_allKeys;
var dynamicStartComponents;
function dynamicStartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dynamicStart' ---
    t = 0;
    dynamicStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dynamicStartResp.keys = undefined;
    dynamicStartResp.rt = undefined;
    _dynamicStartResp_allKeys = [];
    // keep track of which components have finished
    dynamicStartComponents = [];
    dynamicStartComponents.push(dynamicStartText);
    dynamicStartComponents.push(dynamicStartResp);
    
    for (const thisComponent of dynamicStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function dynamicStartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dynamicStart' ---
    // get current time
    t = dynamicStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dynamicStartText* updates
    if (t >= 0.0 && dynamicStartText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicStartText.tStart = t;  // (not accounting for frame time here)
      dynamicStartText.frameNStart = frameN;  // exact frame index
      
      dynamicStartText.setAutoDraw(true);
    }

    
    // *dynamicStartResp* updates
    if (t >= 0.0 && dynamicStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicStartResp.tStart = t;  // (not accounting for frame time here)
      dynamicStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dynamicStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dynamicStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dynamicStartResp.clearEvents(); });
    }

    if (dynamicStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = dynamicStartResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _dynamicStartResp_allKeys = _dynamicStartResp_allKeys.concat(theseKeys);
      if (_dynamicStartResp_allKeys.length > 0) {
        dynamicStartResp.keys = _dynamicStartResp_allKeys[_dynamicStartResp_allKeys.length - 1].name;  // just the last key pressed
        dynamicStartResp.rt = _dynamicStartResp_allKeys[_dynamicStartResp_allKeys.length - 1].rt;
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
    for (const thisComponent of dynamicStartComponents)
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


function dynamicStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dynamicStart' ---
    for (const thisComponent of dynamicStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(dynamicStartResp.corr, level);
    }
    psychoJS.experiment.addData('dynamicStartResp.keys', dynamicStartResp.keys);
    if (typeof dynamicStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dynamicStartResp.rt', dynamicStartResp.rt);
        routineTimer.reset();
        }
    
    dynamicStartResp.stop();
    // the Routine "dynamicStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var dynamicOutcomeComponents;
function dynamicOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dynamicOutcome' ---
    t = 0;
    dynamicOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from dynamicOCcode
    var choicetmp, feedbackRounded, outcometmp, outcomes, choices;
    
    
    function random_item(items){ 
        return items[Math.floor(Math.random()*items.length)]; 
    }
    
    if (realChoiceResp.keys === undefined) {
        outcometmp = Math.nan;
        choicetmp = Math.nan;
        noRespLoc = [0, 0];
        ocLoc = [5, 5];
        ocGambleLoc = [5, 5];
        ocSafeLoc = [5, 5];
        hideGamLoc = [5, 5];
        extraITI = 0;
    } else if (realChoiceResp.keys === "v" && realloc === 1) {
         outcometmp = random_item([riskyoption1, riskyoption2]);
         choicetmp = 1;
         extraITI = 4-realChoiceResp.rt
         if (outcometmp === riskyoption1) {
              ocLoc = [(- 0.35), 0.1];
              ocGambleLoc = [(- 0.35), 0];
              ocSafeLoc = [5, 5];
              noRespLoc = [5, 5];
              hideGamLoc = [(- 0.35), (- 0.125)];
         } else if (outcometmp === riskyoption2) {
              ocLoc = [(- 0.35), (- 0.1)];
              ocGambleLoc = [(- 0.35), 0];
              ocSafeLoc = [5, 5];
              hideGamLoc = [(- 0.35), 0.125];
              noRespLoc = [5, 5];
         }
     } else if (realChoiceResp.keys === "v" && realloc === 2) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoice.rt
         ocLoc = [(- 0.35), 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
     } else if (realChoiceResp.keys === "n" && realloc === 1) {
         outcometmp = safeoption;
         choicetmp = 0;
         extraITI = 4-realChoiceResp.rt
         ocLoc = [0.35, 0];
         ocGambleLoc = [5, 5];
         ocSafeLoc = ocLoc;
         hideGamLoc = ocGambleLoc;
         noRespLoc = [5, 5];
    } else if (realChoiceResp.keys === "n" && realloc === 2) {
        outcometmp = random_item([riskyoption1, riskyoption2]);
        choicetmp = 1;
        extraITI = 4-realChoiceResp.rt
        if (outcometmp === riskyoption1) {
            ocLoc = [0.35, 0.1];
            ocGambleLoc = [0.35, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.35, (- 0.125)];
            noRespLoc = [5, 5];
        } else if (outcometmp === riskyoption2) {
            ocLoc = [0.35, (- 0.1)];
            ocGambleLoc = [0.35, 0];
            ocSafeLoc = [5, 5];
            hideGamLoc = [0.35, 0.125];
            noRespLoc = [5, 5];
        }
    }
    
    actualITI = initITIdynamic[dynamicTrials.thisN] + extraITI
    
    
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
    
    dynamicNoRespText.setPos(noRespLoc);
    dynamicRiskOC.setPos(ocGambleLoc);
    dynamicSafeOC.setPos(ocSafeLoc);
    dynamicOCtext.setColor(new util.Color(color1));
    dynamicOCtext.setPos(ocLoc);
    dynamicOCtext.setText(feedbackRounded);
    dynamicHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    dynamicOutcomeComponents = [];
    dynamicOutcomeComponents.push(dynamicNoRespText);
    dynamicOutcomeComponents.push(dynamicRiskOC);
    dynamicOutcomeComponents.push(dynamicSafeOC);
    dynamicOutcomeComponents.push(dynamicOCtext);
    dynamicOutcomeComponents.push(dynamicHideRisk);
    
    for (const thisComponent of dynamicOutcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function dynamicOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dynamicOutcome' ---
    // get current time
    t = dynamicOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dynamicNoRespText* updates
    if (t >= 0.0 && dynamicNoRespText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicNoRespText.tStart = t;  // (not accounting for frame time here)
      dynamicNoRespText.frameNStart = frameN;  // exact frame index
      
      dynamicNoRespText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynamicNoRespText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynamicNoRespText.setAutoDraw(false);
    }
    
    // *dynamicRiskOC* updates
    if (t >= 0.0 && dynamicRiskOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicRiskOC.tStart = t;  // (not accounting for frame time here)
      dynamicRiskOC.frameNStart = frameN;  // exact frame index
      
      dynamicRiskOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynamicRiskOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynamicRiskOC.setAutoDraw(false);
    }
    
    // *dynamicSafeOC* updates
    if (t >= 0.0 && dynamicSafeOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicSafeOC.tStart = t;  // (not accounting for frame time here)
      dynamicSafeOC.frameNStart = frameN;  // exact frame index
      
      dynamicSafeOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynamicSafeOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynamicSafeOC.setAutoDraw(false);
    }
    
    // *dynamicOCtext* updates
    if (t >= 0.0 && dynamicOCtext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicOCtext.tStart = t;  // (not accounting for frame time here)
      dynamicOCtext.frameNStart = frameN;  // exact frame index
      
      dynamicOCtext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynamicOCtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynamicOCtext.setAutoDraw(false);
    }
    
    // *dynamicHideRisk* updates
    if (t >= 0.0 && dynamicHideRisk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynamicHideRisk.tStart = t;  // (not accounting for frame time here)
      dynamicHideRisk.frameNStart = frameN;  // exact frame index
      
      dynamicHideRisk.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynamicHideRisk.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynamicHideRisk.setAutoDraw(false);
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
    for (const thisComponent of dynamicOutcomeComponents)
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


function dynamicOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dynamicOutcome' ---
    for (const thisComponent of dynamicOutcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from dynamicOCcode
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


var _cgeRDMendResp_allKeys;
var cgeRDMendComponents;
function cgeRDMendRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cgeRDMend' ---
    t = 0;
    cgeRDMendClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cgeRDMendResp.keys = undefined;
    cgeRDMendResp.rt = undefined;
    _cgeRDMendResp_allKeys = [];
    // keep track of which components have finished
    cgeRDMendComponents = [];
    cgeRDMendComponents.push(cgeRDMendText);
    cgeRDMendComponents.push(cgeRDMendResp);
    
    for (const thisComponent of cgeRDMendComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cgeRDMendRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cgeRDMend' ---
    // get current time
    t = cgeRDMendClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cgeRDMendText* updates
    if (t >= 0.0 && cgeRDMendText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cgeRDMendText.tStart = t;  // (not accounting for frame time here)
      cgeRDMendText.frameNStart = frameN;  // exact frame index
      
      cgeRDMendText.setAutoDraw(true);
    }

    
    // *cgeRDMendResp* updates
    if (t >= 0.0 && cgeRDMendResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cgeRDMendResp.tStart = t;  // (not accounting for frame time here)
      cgeRDMendResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { cgeRDMendResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { cgeRDMendResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { cgeRDMendResp.clearEvents(); });
    }

    if (cgeRDMendResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = cgeRDMendResp.getKeys({keyList: ['return'], waitRelease: false});
      _cgeRDMendResp_allKeys = _cgeRDMendResp_allKeys.concat(theseKeys);
      if (_cgeRDMendResp_allKeys.length > 0) {
        cgeRDMendResp.keys = _cgeRDMendResp_allKeys[_cgeRDMendResp_allKeys.length - 1].name;  // just the last key pressed
        cgeRDMendResp.rt = _cgeRDMendResp_allKeys[_cgeRDMendResp_allKeys.length - 1].rt;
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
    for (const thisComponent of cgeRDMendComponents)
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


function cgeRDMendRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cgeRDMend' ---
    for (const thisComponent of cgeRDMendComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(cgeRDMendResp.corr, level);
    }
    psychoJS.experiment.addData('cgeRDMendResp.keys', cgeRDMendResp.keys);
    if (typeof cgeRDMendResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('cgeRDMendResp.rt', cgeRDMendResp.rt);
        routineTimer.reset();
        }
    
    cgeRDMendResp.stop();
    // the Routine "cgeRDMend" was not non-slip safe, so reset the non-slip timer
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
