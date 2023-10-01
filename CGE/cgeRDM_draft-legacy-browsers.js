/********************* 
 * Cgerdm_Draft Test *
 *********************/


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
flowScheduler.add(cgeRDMsetupRoutineBegin());
flowScheduler.add(cgeRDMsetupRoutineEachFrame());
flowScheduler.add(cgeRDMsetupRoutineEnd());
flowScheduler.add(cgeRDMstartRoutineBegin());
flowScheduler.add(cgeRDMstartRoutineEachFrame());
flowScheduler.add(cgeRDMstartRoutineEnd());
flowScheduler.add(practiceStartRoutineBegin());
flowScheduler.add(practiceStartRoutineEachFrame());
flowScheduler.add(practiceStartRoutineEnd());
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin(practiceTrialsLoopScheduler));
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);
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
  expInfo['psychopyVersion'] = '2022.2.4';
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


var cgeRDMsetupClock;
var instructionsTextHeight;
var lettersTextHeight;
var wrap;
var cgeRDMstartClock;
var cgeRDMstartTxt;
var cgeRDMstartResp;
var practiceStartClock;
var pracStartTxt;
var pracStartResp;
var pracChoicesClock;
var textHeight;
var pracCircLeft;
var pracCircRight;
var pracRiskLine;
var pracORtxt;
var pracTriNum;
var pracLossTxt;
var pracGainTxt;
var pracSafeTxt;
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
var pracNoRespTxt;
var pracRiskOC;
var pracSafeOC;
var pracOCtxt;
var pracHideRisk;
var pracITIClock;
var itiPracFix;
var staticStartClock;
var statStartTxt;
var statStartResp;
var realChoicesClock;
var realCircLeft;
var realCircRight;
var realRiskLine;
var realORtxt;
var realPracNum;
var realLossTxt;
var realGainTxt;
var realSafeTxt;
var realVleft;
var realNright;
var realChoiceResp;
var realISIClock;
var isiRealFix;
var statOutcomeClock;
var choices;
var outcomes;
var statNoRespTxt;
var statRiskOC;
var statSafeOC;
var statOCtxt;
var statHideRisk;
var realITIClock;
var itiRealFix;
var computeBestFitClock;
var setupBestFitTxt;
var loadingDynamicChoicesClock;
var loadDynaChoicesTxt;
var loadDynaChoices;
var dynamicStartClock;
var dynaStartTxt;
var dynaStartResp;
var dynaOutcomeClock;
var dynaNoRespTxt;
var dynaRiskOC;
var dynaSafeOC;
var dynaOCtxt;
var dynaHideRisk;
var cgeRDMendClock;
var cgeRDMendTxt;
var cgeRDMendResp;
var ENDClock;
var ThankYou;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "cgeRDMsetup"
  cgeRDMsetupClock = new util.Clock();
  // Run 'Begin Experiment' code from cgeRDMsetupCode
  instructionsTextHeight = 0.05;
  lettersTextHeight = 0.1;
  wrap = 1.5;
  
  var initITIstatic
  var initITIdynamic
  
  
  
  // Initialize components for Routine "cgeRDMstart"
  cgeRDMstartClock = new util.Clock();
  cgeRDMstartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'cgeRDMstartTxt',
    text: 'As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nYou may press "V" to select the option on the left and "N" to select the option on the right.\n\nPress "enter" to move on to the next screen.',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  cgeRDMstartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceStart"
  practiceStartClock = new util.Clock();
  pracStartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracStartTxt',
    text: 'There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  pracStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracChoices"
  pracChoicesClock = new util.Clock();
  textHeight = 0.05;
  
  pracCircLeft = new visual.Polygon ({
    win: psychoJS.window, name: 'pracCircLeft', 
    edges: leftShape, size:circLeft,
    ori: 0, pos: circLeftLoc,
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  pracCircRight = new visual.Polygon ({
    win: psychoJS.window, name: 'pracCircRight', 
    edges: rightShape, size:circRight,
    ori: 0, pos: circRightLoc,
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  pracRiskLine = new visual.Polygon ({
    win: psychoJS.window, name: 'pracRiskLine', 
    edges: 4, size:riskLine,
    ori: 0, pos: [0, 0],
    lineWidth: 3, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  pracORtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracORtxt',
    text: 'OR',
    font: choiceFont,
    units: undefined, 
    pos: ORtextLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -4.0 
  });
  
  pracTriNum = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracTriNum',
    text: '',
    font: trialNumFont,
    units: undefined, 
    pos: trialNumLoc, height: trialNumHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(trialNumColor),  opacity: undefined,
    depth: -5.0 
  });
  
  pracLossTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracLossTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -6.0 
  });
  
  pracGainTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracGainTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -7.0 
  });
  
  pracSafeTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracSafeTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -8.0 
  });
  
  pracVleft = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracVleft',
    text: 'V-Left',
    font: choiceFont,
    units: undefined, 
    pos: VleftLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -9.0 
  });
  
  pracNright = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracNright',
    text: 'N-Right',
    font: choiceFont,
    units: undefined, 
    pos: NrightLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -10.0 
  });
  
  pracChoiceResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracISI"
  pracISIClock = new util.Clock();
  isiPracFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiPracFix',
    text: '+',
    font: fixCrossFont,
    units: undefined, 
    pos: fixCrossLoc, height: FixCrossHeight,  wrapWidth: undefined, ori: 0,
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
  
  pracNoRespTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracNoRespTxt',
    text: 'You did not respond in time\n',
    font: NoRespFont,
    units: undefined, 
    pos: [0, 0], height: NoRespTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  pracRiskOC = new visual.Polygon ({
    win: psychoJS.window, name: 'pracRiskOC', 
    edges: 130, size:circLeft,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  pracSafeOC = new visual.Polygon ({
    win: psychoJS.window, name: 'pracSafeOC', 
    edges: 130, size:circRight,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  pracOCtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracOCtxt',
    text: '',
    font: ocFont,
    units: undefined, 
    pos: [0, 0], height: ocTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  pracHideRisk = new visual.Polygon ({
    win: psychoJS.window, name: 'pracHideRisk', 
    edges: 4, size:riskHide,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "pracITI"
  pracITIClock = new util.Clock();
  itiPracFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiPracFix',
    text: '+',
    font: fixCrossFont,
    units: undefined, 
    pos: fixCrossLoc, height: FixCrossHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "staticStart"
  staticStartClock = new util.Clock();
  statStartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'statStartTxt',
    text: 'Practice complete.\n\nWhen you are ready to start ROUND 1 of the task, press "V" or "N".\n',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  statStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "realChoices"
  realChoicesClock = new util.Clock();
  // Run 'Begin Experiment' code from realChoiceRandLoc
  var realloc
  realCircLeft = new visual.Polygon ({
    win: psychoJS.window, name: 'realCircLeft', 
    edges: 130, size:circLeft,
    ori: 0, pos: circLeftLoc,
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  realCircRight = new visual.Polygon ({
    win: psychoJS.window, name: 'realCircRight', 
    edges: 130, size:circRight,
    ori: 0, pos: circRightLoc,
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  realRiskLine = new visual.Polygon ({
    win: psychoJS.window, name: 'realRiskLine', 
    edges: 4, size:riskLine,
    ori: 0, pos: [0, 0],
    lineWidth: 3, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  realORtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'realORtxt',
    text: 'OR',
    font: choiceFont,
    units: undefined, 
    pos: ORtextLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -4.0 
  });
  
  realPracNum = new visual.TextStim({
    win: psychoJS.window,
    name: 'realPracNum',
    text: '',
    font: trialNumFont,
    units: undefined, 
    pos: trialNumLoc, height: trialNumHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(trialNumColor),  opacity: undefined,
    depth: -5.0 
  });
  
  realLossTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'realLossTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -6.0 
  });
  
  realGainTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'realGainTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -7.0 
  });
  
  realSafeTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'realSafeTxt',
    text: '',
    font: choiceValueFont,
    units: undefined, 
    pos: [0, 0], height: choiceValuesTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color1),  opacity: 1,
    depth: -8.0 
  });
  
  realVleft = new visual.TextStim({
    win: psychoJS.window,
    name: 'realVleft',
    text: 'V-Left',
    font: choiceFont,
    units: undefined, 
    pos: VleftLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -9.0 
  });
  
  realNright = new visual.TextStim({
    win: psychoJS.window,
    name: 'realNright',
    text: 'N-Right',
    font: choiceFont,
    units: undefined, 
    pos: NrightLoc, height: choiceTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -10.0 
  });
  
  realChoiceResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "realISI"
  realISIClock = new util.Clock();
  isiRealFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'isiRealFix',
    text: '+',
    font: fixCrossFont,
    units: undefined, 
    pos: fixCrossLoc, height: FixCrossHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "statOutcome"
  statOutcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from statOCcode
  var actualITI
  choices= []
  outcomes = []
  
  
  statNoRespTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'statNoRespTxt',
    text: 'You did not respond in time\n',
    font: NoRespFont,
    units: undefined, 
    pos: [0, 0], height: NoRespTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  statRiskOC = new visual.Polygon ({
    win: psychoJS.window, name: 'statRiskOC', 
    edges: 130, size:circLeft,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  statSafeOC = new visual.Polygon ({
    win: psychoJS.window, name: 'statSafeOC', 
    edges: 130, size:circRight,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  statOCtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'statOCtxt',
    text: '',
    font: ocFont,
    units: undefined, 
    pos: [0, 0], height: ocTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  statHideRisk = new visual.Polygon ({
    win: psychoJS.window, name: 'statHideRisk', 
    edges: 4, size:riskHide,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "realITI"
  realITIClock = new util.Clock();
  itiRealFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'itiRealFix',
    text: '+',
    font: fixCrossFont,
    units: undefined, 
    pos: fixCrossLoc, height: FixCrossHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "computeBestFit"
  computeBestFitClock = new util.Clock();
  setupBestFitTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupBestFitTxt',
    text: 'ROUND 1 of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "loadingDynamicChoices"
  loadingDynamicChoicesClock = new util.Clock();
  loadDynaChoicesTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'loadDynaChoicesTxt',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  loadDynaChoices = {
    status: PsychoJS.Status.NOT_STARTED
  };
  // Initialize components for Routine "dynamicStart"
  dynamicStartClock = new util.Clock();
  dynaStartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynaStartTxt',
    text: 'When you are ready to start ROUND 2 of the task, press "V" or "N".',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: undefined,
    depth: 0.0 
  });
  
  dynaStartResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "dynaOutcome"
  dynaOutcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from dynaOCcode
  choices= []
  outcomes = []
  
  
  dynaNoRespTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynaNoRespTxt',
    text: 'You did not respond in time\n',
    font: NoRespFont,
    units: undefined, 
    pos: [0, 0], height: NoRespTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color(color2),  opacity: 1,
    depth: -1.0 
  });
  
  dynaRiskOC = new visual.Polygon ({
    win: psychoJS.window, name: 'dynaRiskOC', 
    edges: 130, size:circLeft,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  dynaSafeOC = new visual.Polygon ({
    win: psychoJS.window, name: 'dynaSafeOC', 
    edges: 130, size:circRight,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color2),
    fillColor: new util.Color(color2),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  dynaOCtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'dynaOCtxt',
    text: '',
    font: ocFont,
    units: undefined, 
    pos: [0, 0], height: ocTextHeight,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  dynaHideRisk = new visual.Polygon ({
    win: psychoJS.window, name: 'dynaHideRisk', 
    edges: 4, size:riskHide,
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color(color1),
    fillColor: new util.Color(color1),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "cgeRDMend"
  cgeRDMendClock = new util.Clock();
  cgeRDMendTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'cgeRDMendTxt',
    text: "You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
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
    text: 'Thank you! You have sucessfully completed the second portion of this study.\n\nIf you have not already done so, \nplease notify the experimenter with by pressing the white doorbell button.',
    font: instructionsFont,
    units: undefined, 
    pos: instructLoc, height: instructionsTextHeight,  wrapWidth: wrap, ori: 0.0,
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
var cgeRDMsetupComponents;
function cgeRDMsetupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cgeRDMsetup' ---
    t = 0;
    cgeRDMsetupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    cgeRDMsetupComponents = [];
    
    cgeRDMsetupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function cgeRDMsetupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cgeRDMsetup' ---
    // get current time
    t = cgeRDMsetupClock.getTime();
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
    cgeRDMsetupComponents.forEach( function(thisComponent) {
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
function cgeRDMsetupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cgeRDMsetup' ---
    cgeRDMsetupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from cgeRDMsetupCode
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
    
    // the Routine "cgeRDMsetup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _cgeRDMstartResp_allKeys;
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
    cgeRDMstartResp.keys = undefined;
    cgeRDMstartResp.rt = undefined;
    _cgeRDMstartResp_allKeys = [];
    // keep track of which components have finished
    cgeRDMstartComponents = [];
    cgeRDMstartComponents.push(cgeRDMstartTxt);
    cgeRDMstartComponents.push(cgeRDMstartResp);
    
    cgeRDMstartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *cgeRDMstartTxt* updates
    if (t >= 0.0 && cgeRDMstartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cgeRDMstartTxt.tStart = t;  // (not accounting for frame time here)
      cgeRDMstartTxt.frameNStart = frameN;  // exact frame index
      
      cgeRDMstartTxt.setAutoDraw(true);
    }

    
    // *cgeRDMstartResp* updates
    if (t >= 2 && cgeRDMstartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cgeRDMstartResp.tStart = t;  // (not accounting for frame time here)
      cgeRDMstartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { cgeRDMstartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { cgeRDMstartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { cgeRDMstartResp.clearEvents(); });
    }

    if (cgeRDMstartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = cgeRDMstartResp.getKeys({keyList: ['return'], waitRelease: false});
      _cgeRDMstartResp_allKeys = _cgeRDMstartResp_allKeys.concat(theseKeys);
      if (_cgeRDMstartResp_allKeys.length > 0) {
        cgeRDMstartResp.keys = _cgeRDMstartResp_allKeys[_cgeRDMstartResp_allKeys.length - 1].name;  // just the last key pressed
        cgeRDMstartResp.rt = _cgeRDMstartResp_allKeys[_cgeRDMstartResp_allKeys.length - 1].rt;
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
    cgeRDMstartComponents.forEach( function(thisComponent) {
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


function cgeRDMstartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cgeRDMstart' ---
    cgeRDMstartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(cgeRDMstartResp.corr, level);
    }
    psychoJS.experiment.addData('cgeRDMstartResp.keys', cgeRDMstartResp.keys);
    if (typeof cgeRDMstartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('cgeRDMstartResp.rt', cgeRDMstartResp.rt);
        routineTimer.reset();
        }
    
    cgeRDMstartResp.stop();
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
var practiceStartComponents;
function practiceStartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceStart' ---
    t = 0;
    practiceStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    pracStartResp.keys = undefined;
    pracStartResp.rt = undefined;
    _pracStartResp_allKeys = [];
    // keep track of which components have finished
    practiceStartComponents = [];
    practiceStartComponents.push(pracStartTxt);
    practiceStartComponents.push(pracStartResp);
    
    practiceStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practiceStartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceStart' ---
    // get current time
    t = practiceStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracStartTxt* updates
    if (t >= 0.0 && pracStartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracStartTxt.tStart = t;  // (not accounting for frame time here)
      pracStartTxt.frameNStart = frameN;  // exact frame index
      
      pracStartTxt.setAutoDraw(true);
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
    practiceStartComponents.forEach( function(thisComponent) {
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


function practiceStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceStart' ---
    practiceStartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    // the Routine "practiceStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practiceTrials;
function practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'cgeRDMPractice.xlsx', pracChoices),
      seed: undefined, name: 'practiceTrials'
    });
    psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
    currentLoop = practiceTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceTrials.forEach(function() {
      snapshot = practiceTrials.getSnapshot();
    
      practiceTrialsLoopScheduler.add(importConditions(snapshot));
      practiceTrialsLoopScheduler.add(pracChoicesRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(pracChoicesRoutineEachFrame());
      practiceTrialsLoopScheduler.add(pracChoicesRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(pracISIRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(pracISIRoutineEachFrame());
      practiceTrialsLoopScheduler.add(pracISIRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(pracOutcomeRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(pracOutcomeRoutineEachFrame());
      practiceTrialsLoopScheduler.add(pracOutcomeRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(pracITIRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(pracITIRoutineEachFrame());
      practiceTrialsLoopScheduler.add(pracITIRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialsLoopEndIteration(practiceTrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceTrialsLoopEndIteration(scheduler, snapshot) {
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
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'CGT-choice-set.csv', statChoices),
      seed: undefined, name: 'staticTrials'
    });
    psychoJS.experiment.addLoop(staticTrials); // add the loop to the experiment
    currentLoop = staticTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    staticTrials.forEach(function() {
      snapshot = staticTrials.getSnapshot();
    
      staticTrialsLoopScheduler.add(importConditions(snapshot));
      staticTrialsLoopScheduler.add(realChoicesRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realChoicesRoutineEachFrame());
      staticTrialsLoopScheduler.add(realChoicesRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(realISIRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realISIRoutineEachFrame());
      staticTrialsLoopScheduler.add(realISIRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(statOutcomeRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(statOutcomeRoutineEachFrame());
      staticTrialsLoopScheduler.add(statOutcomeRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(realITIRoutineBegin(snapshot));
      staticTrialsLoopScheduler.add(realITIRoutineEachFrame());
      staticTrialsLoopScheduler.add(realITIRoutineEnd(snapshot));
      staticTrialsLoopScheduler.add(staticTrialsLoopEndIteration(staticTrialsLoopScheduler, snapshot));
    });
    
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
    BestFit.forEach(function() {
      snapshot = BestFit.getSnapshot();
    
      BestFitLoopScheduler.add(importConditions(snapshot));
      BestFitLoopScheduler.add(computeBestFitRoutineBegin(snapshot));
      BestFitLoopScheduler.add(computeBestFitRoutineEachFrame());
      BestFitLoopScheduler.add(computeBestFitRoutineEnd(snapshot));
      BestFitLoopScheduler.add(BestFitLoopEndIteration(BestFitLoopScheduler, snapshot));
    });
    
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
      trialList: TrialHandler.importConditions(psychoJS.serverManager, fname[0], dynaChoices),
      seed: undefined, name: 'dynamicTrials'
    });
    psychoJS.experiment.addLoop(dynamicTrials); // add the loop to the experiment
    currentLoop = dynamicTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    dynamicTrials.forEach(function() {
      snapshot = dynamicTrials.getSnapshot();
    
      dynamicTrialsLoopScheduler.add(importConditions(snapshot));
      dynamicTrialsLoopScheduler.add(realChoicesRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realChoicesRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realChoicesRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(realISIRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realISIRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realISIRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(dynaOutcomeRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(dynaOutcomeRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(dynaOutcomeRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(realITIRoutineBegin(snapshot));
      dynamicTrialsLoopScheduler.add(realITIRoutineEachFrame());
      dynamicTrialsLoopScheduler.add(realITIRoutineEnd(snapshot));
      dynamicTrialsLoopScheduler.add(dynamicTrialsLoopEndIteration(dynamicTrialsLoopScheduler, snapshot));
    });
    
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
var pracChoicesComponents;
function pracChoicesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracChoices' ---
    t = 0;
    pracChoicesClock.reset(); // clock
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
    pracTriNum.setText(pracNum);
    pracLossTxt.setPos(lossLoc);
    pracLossTxt.setText(pracLossRounded);
    pracGainTxt.setPos(gainLoc);
    pracGainTxt.setText(pracGainRounded);
    pracSafeTxt.setPos(safeLoc);
    pracSafeTxt.setText(pracSafeRounded);
    pracChoiceResp.keys = undefined;
    pracChoiceResp.rt = undefined;
    _pracChoiceResp_allKeys = [];
    // keep track of which components have finished
    pracChoicesComponents = [];
    pracChoicesComponents.push(pracCircLeft);
    pracChoicesComponents.push(pracCircRight);
    pracChoicesComponents.push(pracRiskLine);
    pracChoicesComponents.push(pracORtxt);
    pracChoicesComponents.push(pracTriNum);
    pracChoicesComponents.push(pracLossTxt);
    pracChoicesComponents.push(pracGainTxt);
    pracChoicesComponents.push(pracSafeTxt);
    pracChoicesComponents.push(pracVleft);
    pracChoicesComponents.push(pracNright);
    pracChoicesComponents.push(pracChoiceResp);
    
    pracChoicesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function pracChoicesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracChoices' ---
    // get current time
    t = pracChoicesClock.getTime();
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
    
    // *pracORtxt* updates
    if (t >= 0.0 && pracORtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracORtxt.tStart = t;  // (not accounting for frame time here)
      pracORtxt.frameNStart = frameN;  // exact frame index
      
      pracORtxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracORtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracORtxt.setAutoDraw(false);
    }
    
    // *pracTriNum* updates
    if (t >= 0.0 && pracTriNum.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracTriNum.tStart = t;  // (not accounting for frame time here)
      pracTriNum.frameNStart = frameN;  // exact frame index
      
      pracTriNum.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracTriNum.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracTriNum.setAutoDraw(false);
    }
    
    // *pracLossTxt* updates
    if (t >= 0.0 && pracLossTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracLossTxt.tStart = t;  // (not accounting for frame time here)
      pracLossTxt.frameNStart = frameN;  // exact frame index
      
      pracLossTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracLossTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracLossTxt.setAutoDraw(false);
    }
    
    // *pracGainTxt* updates
    if (t >= 0.0 && pracGainTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracGainTxt.tStart = t;  // (not accounting for frame time here)
      pracGainTxt.frameNStart = frameN;  // exact frame index
      
      pracGainTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracGainTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracGainTxt.setAutoDraw(false);
    }
    
    // *pracSafeTxt* updates
    if (t >= 0.0 && pracSafeTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracSafeTxt.tStart = t;  // (not accounting for frame time here)
      pracSafeTxt.frameNStart = frameN;  // exact frame index
      
      pracSafeTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracSafeTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracSafeTxt.setAutoDraw(false);
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
    pracChoicesComponents.forEach( function(thisComponent) {
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


function pracChoicesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracChoices' ---
    pracChoicesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    pracISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    pracISIComponents.forEach( function(thisComponent) {
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


function pracISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracISI' ---
    pracISIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    pracNoRespTxt.setPos(noRespLoc);
    pracRiskOC.setPos(ocGambleLoc);
    pracSafeOC.setPos(ocSafeLoc);
    pracOCtxt.setColor(new util.Color(color1));
    pracOCtxt.setPos(ocLoc);
    pracOCtxt.setText(pracFeedbackRounded);
    pracHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    pracOutcomeComponents = [];
    pracOutcomeComponents.push(pracNoRespTxt);
    pracOutcomeComponents.push(pracRiskOC);
    pracOutcomeComponents.push(pracSafeOC);
    pracOutcomeComponents.push(pracOCtxt);
    pracOutcomeComponents.push(pracHideRisk);
    
    pracOutcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *pracNoRespTxt* updates
    if (t >= 0.0 && pracNoRespTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracNoRespTxt.tStart = t;  // (not accounting for frame time here)
      pracNoRespTxt.frameNStart = frameN;  // exact frame index
      
      pracNoRespTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracNoRespTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracNoRespTxt.setAutoDraw(false);
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
    
    // *pracOCtxt* updates
    if (t >= 0.0 && pracOCtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracOCtxt.tStart = t;  // (not accounting for frame time here)
      pracOCtxt.frameNStart = frameN;  // exact frame index
      
      pracOCtxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pracOCtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pracOCtxt.setAutoDraw(false);
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
    pracOutcomeComponents.forEach( function(thisComponent) {
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


function pracOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracOutcome' ---
    pracOutcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    pracITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    pracITIComponents.forEach( function(thisComponent) {
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


function pracITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracITI' ---
    pracITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "pracITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _statStartResp_allKeys;
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
    statStartResp.keys = undefined;
    statStartResp.rt = undefined;
    _statStartResp_allKeys = [];
    // keep track of which components have finished
    staticStartComponents = [];
    staticStartComponents.push(statStartTxt);
    staticStartComponents.push(statStartResp);
    
    staticStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *statStartTxt* updates
    if (t >= 0.0 && statStartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statStartTxt.tStart = t;  // (not accounting for frame time here)
      statStartTxt.frameNStart = frameN;  // exact frame index
      
      statStartTxt.setAutoDraw(true);
    }

    
    // *statStartResp* updates
    if (t >= 0.0 && statStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statStartResp.tStart = t;  // (not accounting for frame time here)
      statStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { statStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { statStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { statStartResp.clearEvents(); });
    }

    if (statStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = statStartResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _statStartResp_allKeys = _statStartResp_allKeys.concat(theseKeys);
      if (_statStartResp_allKeys.length > 0) {
        statStartResp.keys = _statStartResp_allKeys[_statStartResp_allKeys.length - 1].name;  // just the last key pressed
        statStartResp.rt = _statStartResp_allKeys[_statStartResp_allKeys.length - 1].rt;
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
    staticStartComponents.forEach( function(thisComponent) {
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


function staticStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'staticStart' ---
    staticStartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(statStartResp.corr, level);
    }
    psychoJS.experiment.addData('statStartResp.keys', statStartResp.keys);
    if (typeof statStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('statStartResp.rt', statStartResp.rt);
        routineTimer.reset();
        }
    
    statStartResp.stop();
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
var realChoicesComponents;
function realChoicesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'realChoices' ---
    t = 0;
    realChoicesClock.reset(); // clock
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
    realPracNum.setText(realNum);
    realLossTxt.setPos(lossLoc);
    realLossTxt.setText(lossRounded);
    realGainTxt.setPos(gainLoc);
    realGainTxt.setText(gainRounded);
    realSafeTxt.setPos(safeLoc);
    realSafeTxt.setText(safeRounded);
    realChoiceResp.keys = undefined;
    realChoiceResp.rt = undefined;
    _realChoiceResp_allKeys = [];
    // keep track of which components have finished
    realChoicesComponents = [];
    realChoicesComponents.push(realCircLeft);
    realChoicesComponents.push(realCircRight);
    realChoicesComponents.push(realRiskLine);
    realChoicesComponents.push(realORtxt);
    realChoicesComponents.push(realPracNum);
    realChoicesComponents.push(realLossTxt);
    realChoicesComponents.push(realGainTxt);
    realChoicesComponents.push(realSafeTxt);
    realChoicesComponents.push(realVleft);
    realChoicesComponents.push(realNright);
    realChoicesComponents.push(realChoiceResp);
    
    realChoicesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function realChoicesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'realChoices' ---
    // get current time
    t = realChoicesClock.getTime();
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
    
    // *realORtxt* updates
    if (t >= 0.0 && realORtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realORtxt.tStart = t;  // (not accounting for frame time here)
      realORtxt.frameNStart = frameN;  // exact frame index
      
      realORtxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realORtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realORtxt.setAutoDraw(false);
    }
    
    // *realPracNum* updates
    if (t >= 0.0 && realPracNum.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realPracNum.tStart = t;  // (not accounting for frame time here)
      realPracNum.frameNStart = frameN;  // exact frame index
      
      realPracNum.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realPracNum.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realPracNum.setAutoDraw(false);
    }
    
    // *realLossTxt* updates
    if (t >= 0.0 && realLossTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realLossTxt.tStart = t;  // (not accounting for frame time here)
      realLossTxt.frameNStart = frameN;  // exact frame index
      
      realLossTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realLossTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realLossTxt.setAutoDraw(false);
    }
    
    // *realGainTxt* updates
    if (t >= 0.0 && realGainTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realGainTxt.tStart = t;  // (not accounting for frame time here)
      realGainTxt.frameNStart = frameN;  // exact frame index
      
      realGainTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realGainTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realGainTxt.setAutoDraw(false);
    }
    
    // *realSafeTxt* updates
    if (t >= 0.0 && realSafeTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      realSafeTxt.tStart = t;  // (not accounting for frame time here)
      realSafeTxt.frameNStart = frameN;  // exact frame index
      
      realSafeTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (realSafeTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      realSafeTxt.setAutoDraw(false);
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
    realChoicesComponents.forEach( function(thisComponent) {
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


function realChoicesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realChoices' ---
    realChoicesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    realISIComponents.push(isiRealFix);
    
    realISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *isiRealFix* updates
    if (t >= 0.0 && isiRealFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isiRealFix.tStart = t;  // (not accounting for frame time here)
      isiRealFix.frameNStart = frameN;  // exact frame index
      
      isiRealFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (isiRealFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      isiRealFix.setAutoDraw(false);
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
    realISIComponents.forEach( function(thisComponent) {
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


function realISIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realISI' ---
    realISIComponents.forEach( function(thisComponent) {
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
var statOutcomeComponents;
function statOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'statOutcome' ---
    t = 0;
    statOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from statOCcode
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
    
    statNoRespTxt.setPos(noRespLoc);
    statRiskOC.setPos(ocGambleLoc);
    statSafeOC.setPos(ocSafeLoc);
    statOCtxt.setColor(new util.Color(color1));
    statOCtxt.setPos(ocLoc);
    statOCtxt.setText(feedbackRounded);
    statHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    statOutcomeComponents = [];
    statOutcomeComponents.push(statNoRespTxt);
    statOutcomeComponents.push(statRiskOC);
    statOutcomeComponents.push(statSafeOC);
    statOutcomeComponents.push(statOCtxt);
    statOutcomeComponents.push(statHideRisk);
    
    statOutcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function statOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'statOutcome' ---
    // get current time
    t = statOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *statNoRespTxt* updates
    if (t >= 0.0 && statNoRespTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statNoRespTxt.tStart = t;  // (not accounting for frame time here)
      statNoRespTxt.frameNStart = frameN;  // exact frame index
      
      statNoRespTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (statNoRespTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      statNoRespTxt.setAutoDraw(false);
    }
    
    // *statRiskOC* updates
    if (t >= 0.0 && statRiskOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statRiskOC.tStart = t;  // (not accounting for frame time here)
      statRiskOC.frameNStart = frameN;  // exact frame index
      
      statRiskOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (statRiskOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      statRiskOC.setAutoDraw(false);
    }
    
    // *statSafeOC* updates
    if (t >= 0.0 && statSafeOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statSafeOC.tStart = t;  // (not accounting for frame time here)
      statSafeOC.frameNStart = frameN;  // exact frame index
      
      statSafeOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (statSafeOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      statSafeOC.setAutoDraw(false);
    }
    
    // *statOCtxt* updates
    if (t >= 0.0 && statOCtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statOCtxt.tStart = t;  // (not accounting for frame time here)
      statOCtxt.frameNStart = frameN;  // exact frame index
      
      statOCtxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (statOCtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      statOCtxt.setAutoDraw(false);
    }
    
    // *statHideRisk* updates
    if (t >= 0.0 && statHideRisk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      statHideRisk.tStart = t;  // (not accounting for frame time here)
      statHideRisk.frameNStart = frameN;  // exact frame index
      
      statHideRisk.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (statHideRisk.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      statHideRisk.setAutoDraw(false);
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
    statOutcomeComponents.forEach( function(thisComponent) {
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


function statOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'statOutcome' ---
    statOutcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from statOCcode
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
    realITIComponents.push(itiRealFix);
    
    realITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *itiRealFix* updates
    if (t >= 0.0 && itiRealFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      itiRealFix.tStart = t;  // (not accounting for frame time here)
      itiRealFix.frameNStart = frameN;  // exact frame index
      
      itiRealFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + actualITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (itiRealFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      itiRealFix.setAutoDraw(false);
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
    realITIComponents.forEach( function(thisComponent) {
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


function realITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'realITI' ---
    realITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    computeBestFitComponents.push(setupBestFitTxt);
    
    computeBestFitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *setupBestFitTxt* updates
    if (t >= 0 && setupBestFitTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupBestFitTxt.tStart = t;  // (not accounting for frame time here)
      setupBestFitTxt.frameNStart = frameN;  // exact frame index
      
      setupBestFitTxt.setAutoDraw(true);
    }

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (setupBestFitTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      setupBestFitTxt.setAutoDraw(false);
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
    computeBestFitComponents.forEach( function(thisComponent) {
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


function computeBestFitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'computeBestFit' ---
    computeBestFitComponents.forEach( function(thisComponent) {
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
    loadingDynamicChoicesComponents.push(loadDynaChoicesTxt);
    loadingDynamicChoicesComponents.push(loadDynaChoices);
    
    loadingDynamicChoicesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *loadDynaChoicesTxt* updates
    if (t >= 0.0 && loadDynaChoicesTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loadDynaChoicesTxt.tStart = t;  // (not accounting for frame time here)
      loadDynaChoicesTxt.frameNStart = frameN;  // exact frame index
      
      loadDynaChoicesTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loadDynaChoicesTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loadDynaChoicesTxt.setAutoDraw(false);
    }
    // start downloading resources specified by component loadDynaChoices
    if (t >= 2 && loadDynaChoices.status === PsychoJS.Status.NOT_STARTED) {
      console.log('register and start downloading resources specified by component loadDynaChoices');
      await psychoJS.serverManager.prepareResources(core.ServerManager.ALL_RESOURCES);
      loadDynaChoices.status = PsychoJS.Status.STARTED;
    }
    // check on the resources specified by component loadDynaChoices
    if (t >= null && loadDynaChoices.status === PsychoJS.Status.STARTED) {
      if (psychoJS.serverManager.getResourceStatus(core.ServerManager.ALL_RESOURCES) === core.ServerManager.ResourceStatus.DOWNLOADED) {
        console.log('finished downloading resources specified by component loadDynaChoices');
        loadDynaChoices.status = PsychoJS.Status.FINISHED;
      } else {
        console.log('resource specified in loadDynaChoices took longer than expected to download');
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
    loadingDynamicChoicesComponents.forEach( function(thisComponent) {
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


function loadingDynamicChoicesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'loadingDynamicChoices' ---
    loadingDynamicChoicesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "loadingDynamicChoices" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _dynaStartResp_allKeys;
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
    dynaStartResp.keys = undefined;
    dynaStartResp.rt = undefined;
    _dynaStartResp_allKeys = [];
    // keep track of which components have finished
    dynamicStartComponents = [];
    dynamicStartComponents.push(dynaStartTxt);
    dynamicStartComponents.push(dynaStartResp);
    
    dynamicStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *dynaStartTxt* updates
    if (t >= 0.0 && dynaStartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaStartTxt.tStart = t;  // (not accounting for frame time here)
      dynaStartTxt.frameNStart = frameN;  // exact frame index
      
      dynaStartTxt.setAutoDraw(true);
    }

    
    // *dynaStartResp* updates
    if (t >= 0.0 && dynaStartResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaStartResp.tStart = t;  // (not accounting for frame time here)
      dynaStartResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dynaStartResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dynaStartResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dynaStartResp.clearEvents(); });
    }

    if (dynaStartResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = dynaStartResp.getKeys({keyList: ['v', 'n'], waitRelease: false});
      _dynaStartResp_allKeys = _dynaStartResp_allKeys.concat(theseKeys);
      if (_dynaStartResp_allKeys.length > 0) {
        dynaStartResp.keys = _dynaStartResp_allKeys[_dynaStartResp_allKeys.length - 1].name;  // just the last key pressed
        dynaStartResp.rt = _dynaStartResp_allKeys[_dynaStartResp_allKeys.length - 1].rt;
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
    dynamicStartComponents.forEach( function(thisComponent) {
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


function dynamicStartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dynamicStart' ---
    dynamicStartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(dynaStartResp.corr, level);
    }
    psychoJS.experiment.addData('dynaStartResp.keys', dynaStartResp.keys);
    if (typeof dynaStartResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dynaStartResp.rt', dynaStartResp.rt);
        routineTimer.reset();
        }
    
    dynaStartResp.stop();
    // the Routine "dynamicStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var dynaOutcomeComponents;
function dynaOutcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dynaOutcome' ---
    t = 0;
    dynaOutcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from dynaOCcode
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
    
    dynaNoRespTxt.setPos(noRespLoc);
    dynaRiskOC.setPos(ocGambleLoc);
    dynaSafeOC.setPos(ocSafeLoc);
    dynaOCtxt.setColor(new util.Color(color1));
    dynaOCtxt.setPos(ocLoc);
    dynaOCtxt.setText(feedbackRounded);
    dynaHideRisk.setPos(hideGamLoc);
    // keep track of which components have finished
    dynaOutcomeComponents = [];
    dynaOutcomeComponents.push(dynaNoRespTxt);
    dynaOutcomeComponents.push(dynaRiskOC);
    dynaOutcomeComponents.push(dynaSafeOC);
    dynaOutcomeComponents.push(dynaOCtxt);
    dynaOutcomeComponents.push(dynaHideRisk);
    
    dynaOutcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function dynaOutcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dynaOutcome' ---
    // get current time
    t = dynaOutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dynaNoRespTxt* updates
    if (t >= 0.0 && dynaNoRespTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaNoRespTxt.tStart = t;  // (not accounting for frame time here)
      dynaNoRespTxt.frameNStart = frameN;  // exact frame index
      
      dynaNoRespTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynaNoRespTxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynaNoRespTxt.setAutoDraw(false);
    }
    
    // *dynaRiskOC* updates
    if (t >= 0.0 && dynaRiskOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaRiskOC.tStart = t;  // (not accounting for frame time here)
      dynaRiskOC.frameNStart = frameN;  // exact frame index
      
      dynaRiskOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynaRiskOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynaRiskOC.setAutoDraw(false);
    }
    
    // *dynaSafeOC* updates
    if (t >= 0.0 && dynaSafeOC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaSafeOC.tStart = t;  // (not accounting for frame time here)
      dynaSafeOC.frameNStart = frameN;  // exact frame index
      
      dynaSafeOC.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynaSafeOC.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynaSafeOC.setAutoDraw(false);
    }
    
    // *dynaOCtxt* updates
    if (t >= 0.0 && dynaOCtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaOCtxt.tStart = t;  // (not accounting for frame time here)
      dynaOCtxt.frameNStart = frameN;  // exact frame index
      
      dynaOCtxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynaOCtxt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynaOCtxt.setAutoDraw(false);
    }
    
    // *dynaHideRisk* updates
    if (t >= 0.0 && dynaHideRisk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dynaHideRisk.tStart = t;  // (not accounting for frame time here)
      dynaHideRisk.frameNStart = frameN;  // exact frame index
      
      dynaHideRisk.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dynaHideRisk.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dynaHideRisk.setAutoDraw(false);
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
    dynaOutcomeComponents.forEach( function(thisComponent) {
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


function dynaOutcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dynaOutcome' ---
    dynaOutcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from dynaOCcode
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
    cgeRDMendComponents.push(cgeRDMendTxt);
    cgeRDMendComponents.push(cgeRDMendResp);
    
    cgeRDMendComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *cgeRDMendTxt* updates
    if (t >= 0.0 && cgeRDMendTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cgeRDMendTxt.tStart = t;  // (not accounting for frame time here)
      cgeRDMendTxt.frameNStart = frameN;  // exact frame index
      
      cgeRDMendTxt.setAutoDraw(true);
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
    cgeRDMendComponents.forEach( function(thisComponent) {
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


function cgeRDMendRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cgeRDMend' ---
    cgeRDMendComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
