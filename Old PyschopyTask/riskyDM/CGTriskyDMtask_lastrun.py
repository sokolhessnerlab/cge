#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on Thu Jul 28 15:29:24 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'CGTriskyDMtask'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/shlab/Documents/GitHub/cgt/PyschopyTask/riskyDM/CGTriskyDMtask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1024, 576], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instructions" ---
Instructions = visual.TextStim(win=win, name='Instructions',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nOnce "V-Left" and "N-Right" appear on the screen, you may press "V" to select the option on the left and "N" to choose the option on the right.\n\nPress "enter" to move on to the next screen.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inst1 = keyboard.Keyboard()

# --- Initialize components for Routine "pracStart" ---
startPract = visual.TextStim(win=win, name='startPract',
    text='There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startPracResp = keyboard.Keyboard()

# --- Initialize components for Routine "practiceTask" ---
circleLeft = visual.Rect(
    win=win, name='circleLeft',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-1.0, interpolate=True)
circleRight = visual.Rect(
    win=win, name='circleRight',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
lineLeft = visual.Rect(
    win=win, name='lineLeft',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
orText = visual.TextStim(win=win, name='orText',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
lossTxt = visual.TextStim(win=win, name='lossTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
gainTxt = visual.TextStim(win=win, name='gainTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
safeTxt = visual.TextStim(win=win, name='safeTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
vLeft = visual.TextStim(win=win, name='vLeft',
    text='V-Left',
    font='Arial',
    pos=(-.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
nRight = visual.TextStim(win=win, name='nRight',
    text='N-Right',
    font='Arial',
    pos=(.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
choice1 = keyboard.Keyboard()

# --- Initialize components for Routine "isiPrac" ---
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback" ---
noRespTxt = visual.TextStim(win=win, name='noRespTxt',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ocGamble = visual.Rect(
    win=win, name='ocGamble',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafe = visual.Rect(
    win=win, name='ocSafe',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeText = visual.TextStim(win=win, name='outcomeText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
hideGamble = visual.Rect(
    win=win, name='hideGamble',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "itiPrac_2" ---
itiText = visual.TextStim(win=win, name='itiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "postPrac" ---
postPracText = visual.TextStim(win=win, name='postPracText',
    text='Practice complete.\n\nWhen you are ready to start the real task, press "V" or "N".\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
postPractResp = keyboard.Keyboard()

# --- Initialize components for Routine "choiceWindow" ---
# Run 'Begin Experiment' code from randLoc_2
loc = [];
circleLeftReal = visual.Rect(
    win=win, name='circleLeftReal',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-1.0, interpolate=True)
circleRightReal = visual.Rect(
    win=win, name='circleRightReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
lineLeftReal = visual.Rect(
    win=win, name='lineLeftReal',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
orTextReal = visual.TextStim(win=win, name='orTextReal',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
lossTxtReal = visual.TextStim(win=win, name='lossTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
gainTxtReal = visual.TextStim(win=win, name='gainTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
safeTxtReal = visual.TextStim(win=win, name='safeTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
vLeftReal = visual.TextStim(win=win, name='vLeftReal',
    text='V-Left',
    font='Arial',
    pos=(-.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
nRightReal = visual.TextStim(win=win, name='nRightReal',
    text='N-Right',
    font='Arial',
    pos=(.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realChoice = keyboard.Keyboard()

# --- Initialize components for Routine "isi" ---
isiTextReal = visual.TextStim(win=win, name='isiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "showOutcome" ---
# Run 'Begin Experiment' code from codeFeedbackReal
riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []
noRespTxtReal = visual.TextStim(win=win, name='noRespTxtReal',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ocGambleReal = visual.Rect(
    win=win, name='ocGambleReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafeReal = visual.Rect(
    win=win, name='ocSafeReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeTextReal = visual.TextStim(win=win, name='outcomeTextReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
hideGambleReal = visual.Rect(
    win=win, name='hideGambleReal',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "iti" ---
itiTextReal = visual.TextStim(win=win, name='itiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "computeEstimates" ---
# Run 'Begin Experiment' code from gridSearchCode
import math

### Function Definitions

def choice_probability(parameters, riskyGv, riskyLv, certv):
    # Pull out parameters
    rho = parameters[0];
    mu = parameters[1];
    
    nTrials = len(riskyGv);
    
    # Calculate utility of the two options
    utility_riskygain_value = [math.pow(value, rho) for value in riskyGv];
    utility_riskyloss_value = [math.pow(value, rho) for value in riskyLv];
    utility_risky_option = [.5 * utility_riskygain_value[t] + .5 * utility_riskyloss_value[t] for t in range(nTrials)];
    utility_safe_option = [math.pow(value, rho) for value in certv]
    
    # Normalize values with div
    div = max(riskyGv)**rho;
    
    # Softmax
    p = [1/(1 + math.exp(-mu/div*(utility_risky_option[t] - utility_safe_option[t]))) for t in range(nTrials)];
    return p

def negLLprospect_cgt(parameters, riskyGv, riskyLv, certv, choices):
    choiceP = choice_probability(parameters, riskyGv, riskyLv, certv);
    
    nTrials = len(choiceP);
    
    likelihood = [choices[t]*choiceP[t] + (1-choices[t])*(1-choiceP[t]) for t in range(nTrials)];
    zeroindex = [likelihood[t] == 0 for t in range(nTrials)];
    for ind in range(nTrials):
        if zeroindex[ind]:
            likelihood[ind] = 0.000000000000001;
    
    loglikelihood = [math.log(likelihood[t]) for t in range(nTrials)];
    
    nll = -sum(loglikelihood);
    return nll

fname =[];




# Set experiment start values for variable component dynamicChoiceSet
dynamicChoiceSet = ''
dynamicChoiceSetContainer = []
# Set experiment start values for variable component bestRho
bestRho = ''
bestRhoContainer = []
# Set experiment start values for variable component bestMu
bestMu = ''
bestMuContainer = []
showPart2fileName = visual.TextStim(win=win, name='showPart2fileName',
    text='',
    font='Open Sans',
    pos=(-.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
moveAlong = keyboard.Keyboard()

# --- Initialize components for Routine "choiceWindow" ---
# Run 'Begin Experiment' code from randLoc_2
loc = [];
circleLeftReal = visual.Rect(
    win=win, name='circleLeftReal',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-1.0, interpolate=True)
circleRightReal = visual.Rect(
    win=win, name='circleRightReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.4,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
lineLeftReal = visual.Rect(
    win=win, name='lineLeftReal',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
orTextReal = visual.TextStim(win=win, name='orTextReal',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
lossTxtReal = visual.TextStim(win=win, name='lossTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
gainTxtReal = visual.TextStim(win=win, name='gainTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
safeTxtReal = visual.TextStim(win=win, name='safeTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
vLeftReal = visual.TextStim(win=win, name='vLeftReal',
    text='V-Left',
    font='Arial',
    pos=(-.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
nRightReal = visual.TextStim(win=win, name='nRightReal',
    text='N-Right',
    font='Arial',
    pos=(.4, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realChoice = keyboard.Keyboard()

# --- Initialize components for Routine "isi" ---
isiTextReal = visual.TextStim(win=win, name='isiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "showOutcome" ---
# Run 'Begin Experiment' code from codeFeedbackReal
riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []
noRespTxtReal = visual.TextStim(win=win, name='noRespTxtReal',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ocGambleReal = visual.Rect(
    win=win, name='ocGambleReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafeReal = visual.Rect(
    win=win, name='ocSafeReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeTextReal = visual.TextStim(win=win, name='outcomeTextReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
hideGambleReal = visual.Rect(
    win=win, name='hideGambleReal',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "iti" ---
itiTextReal = visual.TextStim(win=win, name='itiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "selectOutcome" ---

# --- Initialize components for Routine "endOfTask" ---
endRedirect = visual.TextStim(win=win, name='endRedirect',
    text='This part of the experiment is complete. \n\nYou will be redirected in a few moments\n to the next part of the study.\n\nThank you.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
inst1.keys = []
inst1.rt = []
_inst1_allKeys = []
# keep track of which components have finished
instructionsComponents = [Instructions, inst1]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions.started')
        Instructions.setAutoDraw(True)
    
    # *inst1* updates
    waitOnFlip = False
    if inst1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        inst1.frameNStart = frameN  # exact frame index
        inst1.tStart = t  # local t and not account for scr refresh
        inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'inst1.started')
        inst1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(inst1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(inst1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if inst1.status == STARTED and not waitOnFlip:
        theseKeys = inst1.getKeys(keyList=["return"], waitRelease=False)
        _inst1_allKeys.extend(theseKeys)
        if len(_inst1_allKeys):
            inst1.keys = _inst1_allKeys[-1].name  # just the last key pressed
            inst1.rt = _inst1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if inst1.keys in ['', [], None]:  # No response was made
    inst1.keys = None
thisExp.addData('inst1.keys',inst1.keys)
if inst1.keys != None:  # we had a response
    thisExp.addData('inst1.rt', inst1.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pracStart" ---
continueRoutine = True
# update component parameters for each repeat
startPracResp.keys = []
startPracResp.rt = []
_startPracResp_allKeys = []
# keep track of which components have finished
pracStartComponents = [startPract, startPracResp]
for thisComponent in pracStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pracStart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startPract* updates
    if startPract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startPract.frameNStart = frameN  # exact frame index
        startPract.tStart = t  # local t and not account for scr refresh
        startPract.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startPract, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startPract.started')
        startPract.setAutoDraw(True)
    
    # *startPracResp* updates
    waitOnFlip = False
    if startPracResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        startPracResp.frameNStart = frameN  # exact frame index
        startPracResp.tStart = t  # local t and not account for scr refresh
        startPracResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startPracResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startPracResp.started')
        startPracResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startPracResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startPracResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startPracResp.status == STARTED and not waitOnFlip:
        theseKeys = startPracResp.getKeys(keyList=['v','n'], waitRelease=False)
        _startPracResp_allKeys.extend(theseKeys)
        if len(_startPracResp_allKeys):
            startPracResp.keys = _startPracResp_allKeys[-1].name  # just the last key pressed
            startPracResp.rt = _startPracResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pracStart" ---
for thisComponent in pracStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startPracResp.keys in ['', [], None]:  # No response was made
    startPracResp.keys = None
thisExp.addData('startPracResp.keys',startPracResp.keys)
if startPracResp.keys != None:  # we had a response
    thisExp.addData('startPracResp.rt', startPracResp.rt)
thisExp.nextEntry()
# the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgtPractice.xlsx', selection='0:2'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practiceTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from randLoc
    if loc==1:
        targetPos=[-.4,0]
    else:
        targetPos=[.4,0]
    
    if loc==1:
        lossLoc=[-.4,-.1]
        gainLoc=[-.4,.1]
        safeLoc=[.4,0]
    else:
        lossLoc=[.4,-.1]
        gainLoc=[.4,.1]
        safeLoc=[-.4,0]
    circleRight.setFillColor([1,1,1])
    circleRight.setLineColor([1,1,1])
    lineLeft.setPos(targetPos)
    lossTxt.setPos(lossLoc)
    lossTxt.setText(round(riskyLoss,2)

)
    gainTxt.setPos(gainLoc)
    gainTxt.setText(round(riskyGain,2))
    safeTxt.setPos(safeLoc)
    safeTxt.setText(round(alternative,2))
    choice1.keys = []
    choice1.rt = []
    _choice1_allKeys = []
    # keep track of which components have finished
    practiceTaskComponents = [circleLeft, circleRight, lineLeft, orText, lossTxt, gainTxt, safeTxt, vLeft, nRight, choice1]
    for thisComponent in practiceTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practiceTask" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circleLeft* updates
        if circleLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            circleLeft.frameNStart = frameN  # exact frame index
            circleLeft.tStart = t  # local t and not account for scr refresh
            circleLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleLeft.started')
            circleLeft.setAutoDraw(True)
        if circleLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleLeft.tStop = t  # not accounting for scr refresh
                circleLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleLeft.stopped')
                circleLeft.setAutoDraw(False)
        
        # *circleRight* updates
        if circleRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circleRight.frameNStart = frameN  # exact frame index
            circleRight.tStart = t  # local t and not account for scr refresh
            circleRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleRight.started')
            circleRight.setAutoDraw(True)
        if circleRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleRight.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleRight.tStop = t  # not accounting for scr refresh
                circleRight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleRight.stopped')
                circleRight.setAutoDraw(False)
        
        # *lineLeft* updates
        if lineLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lineLeft.frameNStart = frameN  # exact frame index
            lineLeft.tStart = t  # local t and not account for scr refresh
            lineLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lineLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lineLeft.started')
            lineLeft.setAutoDraw(True)
        if lineLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lineLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lineLeft.tStop = t  # not accounting for scr refresh
                lineLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lineLeft.stopped')
                lineLeft.setAutoDraw(False)
        
        # *orText* updates
        if orText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            orText.frameNStart = frameN  # exact frame index
            orText.tStart = t  # local t and not account for scr refresh
            orText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'orText.started')
            orText.setAutoDraw(True)
        if orText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > orText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                orText.tStop = t  # not accounting for scr refresh
                orText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'orText.stopped')
                orText.setAutoDraw(False)
        
        # *lossTxt* updates
        if lossTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lossTxt.frameNStart = frameN  # exact frame index
            lossTxt.tStart = t  # local t and not account for scr refresh
            lossTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lossTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lossTxt.started')
            lossTxt.setAutoDraw(True)
        if lossTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lossTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lossTxt.tStop = t  # not accounting for scr refresh
                lossTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lossTxt.stopped')
                lossTxt.setAutoDraw(False)
        
        # *gainTxt* updates
        if gainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gainTxt.frameNStart = frameN  # exact frame index
            gainTxt.tStart = t  # local t and not account for scr refresh
            gainTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gainTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'gainTxt.started')
            gainTxt.setAutoDraw(True)
        if gainTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gainTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                gainTxt.tStop = t  # not accounting for scr refresh
                gainTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gainTxt.stopped')
                gainTxt.setAutoDraw(False)
        
        # *safeTxt* updates
        if safeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeTxt.frameNStart = frameN  # exact frame index
            safeTxt.tStart = t  # local t and not account for scr refresh
            safeTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'safeTxt.started')
            safeTxt.setAutoDraw(True)
        if safeTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > safeTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                safeTxt.tStop = t  # not accounting for scr refresh
                safeTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'safeTxt.stopped')
                safeTxt.setAutoDraw(False)
        
        # *vLeft* updates
        if vLeft.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            vLeft.frameNStart = frameN  # exact frame index
            vLeft.tStart = t  # local t and not account for scr refresh
            vLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'vLeft.started')
            vLeft.setAutoDraw(True)
        if vLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vLeft.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vLeft.tStop = t  # not accounting for scr refresh
                vLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vLeft.stopped')
                vLeft.setAutoDraw(False)
        
        # *nRight* updates
        if nRight.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nRight.frameNStart = frameN  # exact frame index
            nRight.tStart = t  # local t and not account for scr refresh
            nRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nRight.started')
            nRight.setAutoDraw(True)
        if nRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nRight.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                nRight.tStop = t  # not accounting for scr refresh
                nRight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nRight.stopped')
                nRight.setAutoDraw(False)
        
        # *choice1* updates
        waitOnFlip = False
        if choice1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            choice1.frameNStart = frameN  # exact frame index
            choice1.tStart = t  # local t and not account for scr refresh
            choice1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'choice1.started')
            choice1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                choice1.tStop = t  # not accounting for scr refresh
                choice1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'choice1.stopped')
                choice1.status = FINISHED
        if choice1.status == STARTED and not waitOnFlip:
            theseKeys = choice1.getKeys(keyList=['v','n'], waitRelease=False)
            _choice1_allKeys.extend(theseKeys)
            if len(_choice1_allKeys):
                choice1.keys = _choice1_allKeys[-1].name  # just the last key pressed
                choice1.rt = _choice1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceTask" ---
    for thisComponent in practiceTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if choice1.keys in ['', [], None]:  # No response was made
        choice1.keys = None
    trials.addData('choice1.keys',choice1.keys)
    if choice1.keys != None:  # we had a response
        trials.addData('choice1.rt', choice1.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isiPrac" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiPracComponents = [isiText]
    for thisComponent in isiPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "isiPrac" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiText* updates
        if isiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiText.frameNStart = frameN  # exact frame index
            isiText.tStart = t  # local t and not account for scr refresh
            isiText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiText.started')
            isiText.setAutoDraw(True)
        if isiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiText.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiText.tStop = t  # not accounting for scr refresh
                isiText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiText.stopped')
                isiText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isiPrac" ---
    for thisComponent in isiPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isiPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedback
    import random
    if not choice1.keys:
        outcome = " "
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif choice1.keys == 'v' and loc == 1:
        outcome = random.choice([riskyGain, riskyLoss])
        if outcome == riskyGain:
            ocLoc = [-.4,.1]
            ocGambleLoc = [-.4,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.4,-.125]
        elif outcome == riskyLoss:
             ocLoc = [-.4,-.1]
             ocGambleLoc = [-.4,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.4,.125]
             noRespLoc = [5,5]
    elif choice1.keys == 'v' and loc == 2:
        outcome = alternative
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif choice1.keys == 'n' and loc ==1:
        outcome = alternative
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif choice1.keys == 'n' and loc ==2:
        outcome = random.choice([riskyGain, riskyLoss])
        if outcome == riskyGain:
            ocLoc = [.4,.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,-.125]
            noRespLoc = [5,5]
        elif outcome == riskyLoss:
            ocLoc = [.4,-.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,.125]
            noRespLoc = [5,5]
    
    
    noRespTxt.setPos(noRespLoc)
    ocGamble.setPos(ocGambleLoc)
    ocSafe.setPos(ocSafeLoc)
    outcomeText.setColor('black', colorSpace='rgb')
    outcomeText.setPos(ocLoc)
    outcomeText.setText(round(outcome,2))
    hideGamble.setPos(hideGamLoc)
    # keep track of which components have finished
    feedbackComponents = [noRespTxt, ocGamble, ocSafe, outcomeText, hideGamble]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noRespTxt* updates
        if noRespTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noRespTxt.frameNStart = frameN  # exact frame index
            noRespTxt.tStart = t  # local t and not account for scr refresh
            noRespTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noRespTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noRespTxt.started')
            noRespTxt.setAutoDraw(True)
        if noRespTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noRespTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                noRespTxt.tStop = t  # not accounting for scr refresh
                noRespTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noRespTxt.stopped')
                noRespTxt.setAutoDraw(False)
        
        # *ocGamble* updates
        if ocGamble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocGamble.frameNStart = frameN  # exact frame index
            ocGamble.tStart = t  # local t and not account for scr refresh
            ocGamble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocGamble, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocGamble.started')
            ocGamble.setAutoDraw(True)
        if ocGamble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocGamble.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocGamble.tStop = t  # not accounting for scr refresh
                ocGamble.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocGamble.stopped')
                ocGamble.setAutoDraw(False)
        
        # *ocSafe* updates
        if ocSafe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocSafe.frameNStart = frameN  # exact frame index
            ocSafe.tStart = t  # local t and not account for scr refresh
            ocSafe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocSafe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocSafe.started')
            ocSafe.setAutoDraw(True)
        if ocSafe.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocSafe.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocSafe.tStop = t  # not accounting for scr refresh
                ocSafe.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocSafe.stopped')
                ocSafe.setAutoDraw(False)
        
        # *outcomeText* updates
        if outcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcomeText.frameNStart = frameN  # exact frame index
            outcomeText.tStart = t  # local t and not account for scr refresh
            outcomeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcomeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcomeText.started')
            outcomeText.setAutoDraw(True)
        if outcomeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcomeText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                outcomeText.tStop = t  # not accounting for scr refresh
                outcomeText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcomeText.stopped')
                outcomeText.setAutoDraw(False)
        
        # *hideGamble* updates
        if hideGamble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hideGamble.frameNStart = frameN  # exact frame index
            hideGamble.tStart = t  # local t and not account for scr refresh
            hideGamble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hideGamble, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'hideGamble.started')
            hideGamble.setAutoDraw(True)
        if hideGamble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hideGamble.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hideGamble.tStop = t  # not accounting for scr refresh
                hideGamble.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hideGamble.stopped')
                hideGamble.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from codeFeedback
    thisExp.addData('outcome', outcome)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "itiPrac_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiPrac_2Components = [itiText]
    for thisComponent in itiPrac_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "itiPrac_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiText* updates
        if itiText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiText.frameNStart = frameN  # exact frame index
            itiText.tStart = t  # local t and not account for scr refresh
            itiText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiText.started')
            itiText.setAutoDraw(True)
        if itiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiText.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                itiText.tStop = t  # not accounting for scr refresh
                itiText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiText.stopped')
                itiText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiPrac_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "itiPrac_2" ---
    for thisComponent in itiPrac_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "itiPrac_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials'


# --- Prepare to start Routine "postPrac" ---
continueRoutine = True
# update component parameters for each repeat
postPractResp.keys = []
postPractResp.rt = []
_postPractResp_allKeys = []
# keep track of which components have finished
postPracComponents = [postPracText, postPractResp]
for thisComponent in postPracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postPrac" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *postPracText* updates
    if postPracText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postPracText.frameNStart = frameN  # exact frame index
        postPracText.tStart = t  # local t and not account for scr refresh
        postPracText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postPracText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'postPracText.started')
        postPracText.setAutoDraw(True)
    
    # *postPractResp* updates
    waitOnFlip = False
    if postPractResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postPractResp.frameNStart = frameN  # exact frame index
        postPractResp.tStart = t  # local t and not account for scr refresh
        postPractResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postPractResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'postPractResp.started')
        postPractResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(postPractResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(postPractResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if postPractResp.status == STARTED and not waitOnFlip:
        theseKeys = postPractResp.getKeys(keyList=['v','n'], waitRelease=False)
        _postPractResp_allKeys.extend(theseKeys)
        if len(_postPractResp_allKeys):
            postPractResp.keys = _postPractResp_allKeys[-1].name  # just the last key pressed
            postPractResp.rt = _postPractResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postPracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postPrac" ---
for thisComponent in postPracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if postPractResp.keys in ['', [], None]:  # No response was made
    postPractResp.keys = None
thisExp.addData('postPractResp.keys',postPractResp.keys)
if postPractResp.keys != None:  # we had a response
    thisExp.addData('postPractResp.rt', postPractResp.rt)
thisExp.nextEntry()
# the Routine "postPrac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
staticRDM = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CGT-choice-set.csv', selection='0:3'),
    seed=None, name='staticRDM')
thisExp.addLoop(staticRDM)  # add the loop to the experiment
thisStaticRDM = staticRDM.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStaticRDM.rgb)
if thisStaticRDM != None:
    for paramName in thisStaticRDM:
        exec('{} = thisStaticRDM[paramName]'.format(paramName))

for thisStaticRDM in staticRDM:
    currentLoop = staticRDM
    # abbreviate parameter names if possible (e.g. rgb = thisStaticRDM.rgb)
    if thisStaticRDM != None:
        for paramName in thisStaticRDM:
            exec('{} = thisStaticRDM[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "choiceWindow" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from randLoc_2
    import random
    
    loc = random.choice([1,2])
    
    if loc==1:
        targetPos=[-.4,0]
    else:
        targetPos=[.4,0]
    
    if loc==1:
        lossLoc=[-.4,-.1]
        gainLoc=[-.4,.1]
        safeLoc=[.4,0]
    else:
        lossLoc=[.4,-.1]
        gainLoc=[.4,.1]
        safeLoc=[-.4,0]
    circleRightReal.setFillColor([1,1,1])
    circleRightReal.setLineColor([1,1,1])
    lineLeftReal.setPos(targetPos)
    lossTxtReal.setPos(lossLoc)
    lossTxtReal.setText(round(riskyoption2,2))
    gainTxtReal.setPos(gainLoc)
    gainTxtReal.setText(round(riskyoption1,2))
    safeTxtReal.setPos(safeLoc)
    safeTxtReal.setText(round(safeoption,2))
    realChoice.keys = []
    realChoice.rt = []
    _realChoice_allKeys = []
    # keep track of which components have finished
    choiceWindowComponents = [circleLeftReal, circleRightReal, lineLeftReal, orTextReal, lossTxtReal, gainTxtReal, safeTxtReal, vLeftReal, nRightReal, realChoice]
    for thisComponent in choiceWindowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choiceWindow" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circleLeftReal* updates
        if circleLeftReal.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            circleLeftReal.frameNStart = frameN  # exact frame index
            circleLeftReal.tStart = t  # local t and not account for scr refresh
            circleLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleLeftReal.started')
            circleLeftReal.setAutoDraw(True)
        if circleLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleLeftReal.tStop = t  # not accounting for scr refresh
                circleLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleLeftReal.stopped')
                circleLeftReal.setAutoDraw(False)
        
        # *circleRightReal* updates
        if circleRightReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circleRightReal.frameNStart = frameN  # exact frame index
            circleRightReal.tStart = t  # local t and not account for scr refresh
            circleRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleRightReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleRightReal.started')
            circleRightReal.setAutoDraw(True)
        if circleRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleRightReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleRightReal.tStop = t  # not accounting for scr refresh
                circleRightReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleRightReal.stopped')
                circleRightReal.setAutoDraw(False)
        
        # *lineLeftReal* updates
        if lineLeftReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lineLeftReal.frameNStart = frameN  # exact frame index
            lineLeftReal.tStart = t  # local t and not account for scr refresh
            lineLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lineLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lineLeftReal.started')
            lineLeftReal.setAutoDraw(True)
        if lineLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lineLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lineLeftReal.tStop = t  # not accounting for scr refresh
                lineLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lineLeftReal.stopped')
                lineLeftReal.setAutoDraw(False)
        
        # *orTextReal* updates
        if orTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            orTextReal.frameNStart = frameN  # exact frame index
            orTextReal.tStart = t  # local t and not account for scr refresh
            orTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'orTextReal.started')
            orTextReal.setAutoDraw(True)
        if orTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > orTextReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                orTextReal.tStop = t  # not accounting for scr refresh
                orTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'orTextReal.stopped')
                orTextReal.setAutoDraw(False)
        
        # *lossTxtReal* updates
        if lossTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lossTxtReal.frameNStart = frameN  # exact frame index
            lossTxtReal.tStart = t  # local t and not account for scr refresh
            lossTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lossTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lossTxtReal.started')
            lossTxtReal.setAutoDraw(True)
        if lossTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lossTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lossTxtReal.tStop = t  # not accounting for scr refresh
                lossTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lossTxtReal.stopped')
                lossTxtReal.setAutoDraw(False)
        
        # *gainTxtReal* updates
        if gainTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gainTxtReal.frameNStart = frameN  # exact frame index
            gainTxtReal.tStart = t  # local t and not account for scr refresh
            gainTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gainTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'gainTxtReal.started')
            gainTxtReal.setAutoDraw(True)
        if gainTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gainTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                gainTxtReal.tStop = t  # not accounting for scr refresh
                gainTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gainTxtReal.stopped')
                gainTxtReal.setAutoDraw(False)
        
        # *safeTxtReal* updates
        if safeTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeTxtReal.frameNStart = frameN  # exact frame index
            safeTxtReal.tStart = t  # local t and not account for scr refresh
            safeTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'safeTxtReal.started')
            safeTxtReal.setAutoDraw(True)
        if safeTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > safeTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                safeTxtReal.tStop = t  # not accounting for scr refresh
                safeTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'safeTxtReal.stopped')
                safeTxtReal.setAutoDraw(False)
        
        # *vLeftReal* updates
        if vLeftReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            vLeftReal.frameNStart = frameN  # exact frame index
            vLeftReal.tStart = t  # local t and not account for scr refresh
            vLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'vLeftReal.started')
            vLeftReal.setAutoDraw(True)
        if vLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vLeftReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vLeftReal.tStop = t  # not accounting for scr refresh
                vLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vLeftReal.stopped')
                vLeftReal.setAutoDraw(False)
        
        # *nRightReal* updates
        if nRightReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nRightReal.frameNStart = frameN  # exact frame index
            nRightReal.tStart = t  # local t and not account for scr refresh
            nRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nRightReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nRightReal.started')
            nRightReal.setAutoDraw(True)
        if nRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nRightReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                nRightReal.tStop = t  # not accounting for scr refresh
                nRightReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nRightReal.stopped')
                nRightReal.setAutoDraw(False)
        
        # *realChoice* updates
        waitOnFlip = False
        if realChoice.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            realChoice.frameNStart = frameN  # exact frame index
            realChoice.tStart = t  # local t and not account for scr refresh
            realChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realChoice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realChoice.started')
            realChoice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(realChoice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(realChoice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if realChoice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realChoice.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                realChoice.tStop = t  # not accounting for scr refresh
                realChoice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realChoice.stopped')
                realChoice.status = FINISHED
        if realChoice.status == STARTED and not waitOnFlip:
            theseKeys = realChoice.getKeys(keyList=['v','n'], waitRelease=False)
            _realChoice_allKeys.extend(theseKeys)
            if len(_realChoice_allKeys):
                realChoice.keys = _realChoice_allKeys[-1].name  # just the last key pressed
                realChoice.rt = _realChoice_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceWindowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choiceWindow" ---
    for thisComponent in choiceWindowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from randLoc_2
    thisExp.addData("loc", loc)
    # check responses
    if realChoice.keys in ['', [], None]:  # No response was made
        realChoice.keys = None
    staticRDM.addData('realChoice.keys',realChoice.keys)
    if realChoice.keys != None:  # we had a response
        staticRDM.addData('realChoice.rt', realChoice.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = [isiTextReal]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "isi" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiTextReal* updates
        if isiTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiTextReal.frameNStart = frameN  # exact frame index
            isiTextReal.tStart = t  # local t and not account for scr refresh
            isiTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiTextReal.started')
            isiTextReal.setAutoDraw(True)
        if isiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiTextReal.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiTextReal.tStop = t  # not accounting for scr refresh
                isiTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiTextReal.stopped')
                isiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isi" ---
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedbackReal
    import random
    import math
    if not realChoice.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        if outcometmp == riskyoption1:
            ocLoc = [-.4,.1]
            ocGambleLoc = [-.4,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.4,-.125]
        elif outcometmp == riskyoption2:
             ocLoc = [-.4,-.1]
             ocGambleLoc = [-.4,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.4,.125]
             noRespLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        if outcometmp == riskyoption1:
            ocLoc = [.4,.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,-.125]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.4,-.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,.125]
            noRespLoc = [5,5]
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyoption2)
    riskygain_values.append(riskyoption1)
    certain_values.append(safeoption)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    outcomeTextReal.setColor('black', colorSpace='rgb')
    outcomeTextReal.setPos(ocLoc)
    outcomeTextReal.setText(round(outcometmp,2))
    hideGambleReal.setPos(hideGamLoc)
    # keep track of which components have finished
    showOutcomeComponents = [noRespTxtReal, ocGambleReal, ocSafeReal, outcomeTextReal, hideGambleReal]
    for thisComponent in showOutcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "showOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noRespTxtReal* updates
        if noRespTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noRespTxtReal.frameNStart = frameN  # exact frame index
            noRespTxtReal.tStart = t  # local t and not account for scr refresh
            noRespTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noRespTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noRespTxtReal.started')
            noRespTxtReal.setAutoDraw(True)
        if noRespTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noRespTxtReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                noRespTxtReal.tStop = t  # not accounting for scr refresh
                noRespTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noRespTxtReal.stopped')
                noRespTxtReal.setAutoDraw(False)
        
        # *ocGambleReal* updates
        if ocGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocGambleReal.frameNStart = frameN  # exact frame index
            ocGambleReal.tStart = t  # local t and not account for scr refresh
            ocGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocGambleReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocGambleReal.started')
            ocGambleReal.setAutoDraw(True)
        if ocGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocGambleReal.tStop = t  # not accounting for scr refresh
                ocGambleReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocGambleReal.stopped')
                ocGambleReal.setAutoDraw(False)
        
        # *ocSafeReal* updates
        if ocSafeReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocSafeReal.frameNStart = frameN  # exact frame index
            ocSafeReal.tStart = t  # local t and not account for scr refresh
            ocSafeReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocSafeReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocSafeReal.started')
            ocSafeReal.setAutoDraw(True)
        if ocSafeReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocSafeReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocSafeReal.tStop = t  # not accounting for scr refresh
                ocSafeReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocSafeReal.stopped')
                ocSafeReal.setAutoDraw(False)
        
        # *outcomeTextReal* updates
        if outcomeTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcomeTextReal.frameNStart = frameN  # exact frame index
            outcomeTextReal.tStart = t  # local t and not account for scr refresh
            outcomeTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcomeTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcomeTextReal.started')
            outcomeTextReal.setAutoDraw(True)
        if outcomeTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcomeTextReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                outcomeTextReal.tStop = t  # not accounting for scr refresh
                outcomeTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcomeTextReal.stopped')
                outcomeTextReal.setAutoDraw(False)
        
        # *hideGambleReal* updates
        if hideGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hideGambleReal.frameNStart = frameN  # exact frame index
            hideGambleReal.tStart = t  # local t and not account for scr refresh
            hideGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hideGambleReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'hideGambleReal.started')
            hideGambleReal.setAutoDraw(True)
        if hideGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hideGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hideGambleReal.tStop = t  # not accounting for scr refresh
                hideGambleReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hideGambleReal.stopped')
                hideGambleReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in showOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "showOutcome" ---
    for thisComponent in showOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from codeFeedbackReal
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiComponents = [itiTextReal]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "iti" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiTextReal* updates
        if itiTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiTextReal.frameNStart = frameN  # exact frame index
            itiTextReal.tStart = t  # local t and not account for scr refresh
            itiTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiTextReal.started')
            itiTextReal.setAutoDraw(True)
        if itiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiTextReal.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                itiTextReal.tStop = t  # not accounting for scr refresh
                itiTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiTextReal.stopped')
                itiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iti" ---
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'staticRDM'


# --- Prepare to start Routine "computeEstimates" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from gridSearchCode

### Grid Search Code

# Prepare rho & mu values
n_rho_values = 200;
n_mu_values = 201;

rmin = 0.3
rmax = 2.2
rstep = (rmax - rmin)/(n_rho_values-1)

mmin = 7
mmax = 80
mstep = (mmax - mmin)/(n_mu_values-1)

rho_values = [];
mu_values = [];

for r in range(n_rho_values):
    rho_values += [rmin + r*rstep];

for m in range(n_mu_values):
    mu_values += [mmin + m*mstep];

# Execute the grid search
best_nll_value = 1e10; # a preposterously bad first NLL

for r in range(n_rho_values):
    for m in range(n_mu_values):
        nll_new = negLLprospect_cgt([rho_values[r], mu_values[m]], riskygain_values, riskyloss_values, certain_values, choices);
        if nll_new < best_nll_value:
            best_nll_value = nll_new;
            bestR = r + 1; # "+1" corrects for diff. in python vs. R indexing
            bestM = m + 1; # "+1" corrects for diff. in python vs. R indexing

print('The best R index is', bestR, 'while the best M index is', bestM, ', with an NLL of', best_nll_value);

fname.append("../choiceset/bespoke_choicesets/bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM))
dynamicChoiceSet = fname[0]  # Set routine start values for dynamicChoiceSet
thisExp.addData('dynamicChoiceSet.routineStartVal', dynamicChoiceSet)  # Save exp start value
bestRho = bestR  # Set routine start values for bestRho
bestMu = bestM  # Set routine start values for bestMu
moveAlong.keys = []
moveAlong.rt = []
_moveAlong_allKeys = []
# keep track of which components have finished
computeEstimatesComponents = [showPart2fileName, moveAlong]
for thisComponent in computeEstimatesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "computeEstimates" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *showPart2fileName* updates
    if showPart2fileName.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        showPart2fileName.frameNStart = frameN  # exact frame index
        showPart2fileName.tStart = t  # local t and not account for scr refresh
        showPart2fileName.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(showPart2fileName, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'showPart2fileName.started')
        showPart2fileName.setAutoDraw(True)
    if showPart2fileName.status == STARTED:  # only update if drawing
        showPart2fileName.setText("dynamic choice set name:\n" + fname[0] + "\nbestRho:" + str(bestRho) + "\nbestMu:" + str(bestMu), log=False)
    
    # *moveAlong* updates
    waitOnFlip = False
    if moveAlong.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        moveAlong.frameNStart = frameN  # exact frame index
        moveAlong.tStart = t  # local t and not account for scr refresh
        moveAlong.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moveAlong, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moveAlong.started')
        moveAlong.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(moveAlong.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(moveAlong.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if moveAlong.status == STARTED and not waitOnFlip:
        theseKeys = moveAlong.getKeys(keyList=['return'], waitRelease=False)
        _moveAlong_allKeys.extend(theseKeys)
        if len(_moveAlong_allKeys):
            moveAlong.keys = _moveAlong_allKeys[-1].name  # just the last key pressed
            moveAlong.rt = _moveAlong_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in computeEstimatesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "computeEstimates" ---
for thisComponent in computeEstimatesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('dynamicChoiceSet.routineEndVal', dynamicChoiceSet)  # Save end routine value
thisExp.addData('bestRho.routineEndVal', bestRho)  # Save end routine value
thisExp.addData('bestMu.routineEndVal', bestMu)  # Save end routine value
# check responses
if moveAlong.keys in ['', [], None]:  # No response was made
    moveAlong.keys = None
thisExp.addData('moveAlong.keys',moveAlong.keys)
if moveAlong.keys != None:  # we had a response
    thisExp.addData('moveAlong.rt', moveAlong.rt)
thisExp.nextEntry()
# the Routine "computeEstimates" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
dynamicRDM = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(fname[0], selection='0:3'),
    seed=None, name='dynamicRDM')
thisExp.addLoop(dynamicRDM)  # add the loop to the experiment
thisDynamicRDM = dynamicRDM.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDynamicRDM.rgb)
if thisDynamicRDM != None:
    for paramName in thisDynamicRDM:
        exec('{} = thisDynamicRDM[paramName]'.format(paramName))

for thisDynamicRDM in dynamicRDM:
    currentLoop = dynamicRDM
    # abbreviate parameter names if possible (e.g. rgb = thisDynamicRDM.rgb)
    if thisDynamicRDM != None:
        for paramName in thisDynamicRDM:
            exec('{} = thisDynamicRDM[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "choiceWindow" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from randLoc_2
    import random
    
    loc = random.choice([1,2])
    
    if loc==1:
        targetPos=[-.4,0]
    else:
        targetPos=[.4,0]
    
    if loc==1:
        lossLoc=[-.4,-.1]
        gainLoc=[-.4,.1]
        safeLoc=[.4,0]
    else:
        lossLoc=[.4,-.1]
        gainLoc=[.4,.1]
        safeLoc=[-.4,0]
    circleRightReal.setFillColor([1,1,1])
    circleRightReal.setLineColor([1,1,1])
    lineLeftReal.setPos(targetPos)
    lossTxtReal.setPos(lossLoc)
    lossTxtReal.setText(round(riskyoption2,2))
    gainTxtReal.setPos(gainLoc)
    gainTxtReal.setText(round(riskyoption1,2))
    safeTxtReal.setPos(safeLoc)
    safeTxtReal.setText(round(safeoption,2))
    realChoice.keys = []
    realChoice.rt = []
    _realChoice_allKeys = []
    # keep track of which components have finished
    choiceWindowComponents = [circleLeftReal, circleRightReal, lineLeftReal, orTextReal, lossTxtReal, gainTxtReal, safeTxtReal, vLeftReal, nRightReal, realChoice]
    for thisComponent in choiceWindowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choiceWindow" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circleLeftReal* updates
        if circleLeftReal.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            circleLeftReal.frameNStart = frameN  # exact frame index
            circleLeftReal.tStart = t  # local t and not account for scr refresh
            circleLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleLeftReal.started')
            circleLeftReal.setAutoDraw(True)
        if circleLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleLeftReal.tStop = t  # not accounting for scr refresh
                circleLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleLeftReal.stopped')
                circleLeftReal.setAutoDraw(False)
        
        # *circleRightReal* updates
        if circleRightReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circleRightReal.frameNStart = frameN  # exact frame index
            circleRightReal.tStart = t  # local t and not account for scr refresh
            circleRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleRightReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circleRightReal.started')
            circleRightReal.setAutoDraw(True)
        if circleRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleRightReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleRightReal.tStop = t  # not accounting for scr refresh
                circleRightReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circleRightReal.stopped')
                circleRightReal.setAutoDraw(False)
        
        # *lineLeftReal* updates
        if lineLeftReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lineLeftReal.frameNStart = frameN  # exact frame index
            lineLeftReal.tStart = t  # local t and not account for scr refresh
            lineLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lineLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lineLeftReal.started')
            lineLeftReal.setAutoDraw(True)
        if lineLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lineLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lineLeftReal.tStop = t  # not accounting for scr refresh
                lineLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lineLeftReal.stopped')
                lineLeftReal.setAutoDraw(False)
        
        # *orTextReal* updates
        if orTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            orTextReal.frameNStart = frameN  # exact frame index
            orTextReal.tStart = t  # local t and not account for scr refresh
            orTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'orTextReal.started')
            orTextReal.setAutoDraw(True)
        if orTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > orTextReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                orTextReal.tStop = t  # not accounting for scr refresh
                orTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'orTextReal.stopped')
                orTextReal.setAutoDraw(False)
        
        # *lossTxtReal* updates
        if lossTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lossTxtReal.frameNStart = frameN  # exact frame index
            lossTxtReal.tStart = t  # local t and not account for scr refresh
            lossTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lossTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lossTxtReal.started')
            lossTxtReal.setAutoDraw(True)
        if lossTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lossTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lossTxtReal.tStop = t  # not accounting for scr refresh
                lossTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lossTxtReal.stopped')
                lossTxtReal.setAutoDraw(False)
        
        # *gainTxtReal* updates
        if gainTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gainTxtReal.frameNStart = frameN  # exact frame index
            gainTxtReal.tStart = t  # local t and not account for scr refresh
            gainTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gainTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'gainTxtReal.started')
            gainTxtReal.setAutoDraw(True)
        if gainTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gainTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                gainTxtReal.tStop = t  # not accounting for scr refresh
                gainTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gainTxtReal.stopped')
                gainTxtReal.setAutoDraw(False)
        
        # *safeTxtReal* updates
        if safeTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeTxtReal.frameNStart = frameN  # exact frame index
            safeTxtReal.tStart = t  # local t and not account for scr refresh
            safeTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'safeTxtReal.started')
            safeTxtReal.setAutoDraw(True)
        if safeTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > safeTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                safeTxtReal.tStop = t  # not accounting for scr refresh
                safeTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'safeTxtReal.stopped')
                safeTxtReal.setAutoDraw(False)
        
        # *vLeftReal* updates
        if vLeftReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            vLeftReal.frameNStart = frameN  # exact frame index
            vLeftReal.tStart = t  # local t and not account for scr refresh
            vLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vLeftReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'vLeftReal.started')
            vLeftReal.setAutoDraw(True)
        if vLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vLeftReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vLeftReal.tStop = t  # not accounting for scr refresh
                vLeftReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vLeftReal.stopped')
                vLeftReal.setAutoDraw(False)
        
        # *nRightReal* updates
        if nRightReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nRightReal.frameNStart = frameN  # exact frame index
            nRightReal.tStart = t  # local t and not account for scr refresh
            nRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nRightReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nRightReal.started')
            nRightReal.setAutoDraw(True)
        if nRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nRightReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                nRightReal.tStop = t  # not accounting for scr refresh
                nRightReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nRightReal.stopped')
                nRightReal.setAutoDraw(False)
        
        # *realChoice* updates
        waitOnFlip = False
        if realChoice.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            realChoice.frameNStart = frameN  # exact frame index
            realChoice.tStart = t  # local t and not account for scr refresh
            realChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realChoice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realChoice.started')
            realChoice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(realChoice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(realChoice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if realChoice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realChoice.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                realChoice.tStop = t  # not accounting for scr refresh
                realChoice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realChoice.stopped')
                realChoice.status = FINISHED
        if realChoice.status == STARTED and not waitOnFlip:
            theseKeys = realChoice.getKeys(keyList=['v','n'], waitRelease=False)
            _realChoice_allKeys.extend(theseKeys)
            if len(_realChoice_allKeys):
                realChoice.keys = _realChoice_allKeys[-1].name  # just the last key pressed
                realChoice.rt = _realChoice_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceWindowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choiceWindow" ---
    for thisComponent in choiceWindowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from randLoc_2
    thisExp.addData("loc", loc)
    # check responses
    if realChoice.keys in ['', [], None]:  # No response was made
        realChoice.keys = None
    dynamicRDM.addData('realChoice.keys',realChoice.keys)
    if realChoice.keys != None:  # we had a response
        dynamicRDM.addData('realChoice.rt', realChoice.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = [isiTextReal]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "isi" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiTextReal* updates
        if isiTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiTextReal.frameNStart = frameN  # exact frame index
            isiTextReal.tStart = t  # local t and not account for scr refresh
            isiTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiTextReal.started')
            isiTextReal.setAutoDraw(True)
        if isiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiTextReal.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiTextReal.tStop = t  # not accounting for scr refresh
                isiTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiTextReal.stopped')
                isiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "isi" ---
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "isi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedbackReal
    import random
    import math
    if not realChoice.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        if outcometmp == riskyoption1:
            ocLoc = [-.4,.1]
            ocGambleLoc = [-.4,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.4,-.125]
        elif outcometmp == riskyoption2:
             ocLoc = [-.4,-.1]
             ocGambleLoc = [-.4,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.4,.125]
             noRespLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        if outcometmp == riskyoption1:
            ocLoc = [.4,.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,-.125]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.4,-.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,.125]
            noRespLoc = [5,5]
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyoption2)
    riskygain_values.append(riskyoption1)
    certain_values.append(safeoption)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    outcomeTextReal.setColor('black', colorSpace='rgb')
    outcomeTextReal.setPos(ocLoc)
    outcomeTextReal.setText(round(outcometmp,2))
    hideGambleReal.setPos(hideGamLoc)
    # keep track of which components have finished
    showOutcomeComponents = [noRespTxtReal, ocGambleReal, ocSafeReal, outcomeTextReal, hideGambleReal]
    for thisComponent in showOutcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "showOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noRespTxtReal* updates
        if noRespTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noRespTxtReal.frameNStart = frameN  # exact frame index
            noRespTxtReal.tStart = t  # local t and not account for scr refresh
            noRespTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noRespTxtReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noRespTxtReal.started')
            noRespTxtReal.setAutoDraw(True)
        if noRespTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noRespTxtReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                noRespTxtReal.tStop = t  # not accounting for scr refresh
                noRespTxtReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noRespTxtReal.stopped')
                noRespTxtReal.setAutoDraw(False)
        
        # *ocGambleReal* updates
        if ocGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocGambleReal.frameNStart = frameN  # exact frame index
            ocGambleReal.tStart = t  # local t and not account for scr refresh
            ocGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocGambleReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocGambleReal.started')
            ocGambleReal.setAutoDraw(True)
        if ocGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocGambleReal.tStop = t  # not accounting for scr refresh
                ocGambleReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocGambleReal.stopped')
                ocGambleReal.setAutoDraw(False)
        
        # *ocSafeReal* updates
        if ocSafeReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocSafeReal.frameNStart = frameN  # exact frame index
            ocSafeReal.tStart = t  # local t and not account for scr refresh
            ocSafeReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocSafeReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ocSafeReal.started')
            ocSafeReal.setAutoDraw(True)
        if ocSafeReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocSafeReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocSafeReal.tStop = t  # not accounting for scr refresh
                ocSafeReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ocSafeReal.stopped')
                ocSafeReal.setAutoDraw(False)
        
        # *outcomeTextReal* updates
        if outcomeTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcomeTextReal.frameNStart = frameN  # exact frame index
            outcomeTextReal.tStart = t  # local t and not account for scr refresh
            outcomeTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcomeTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcomeTextReal.started')
            outcomeTextReal.setAutoDraw(True)
        if outcomeTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcomeTextReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                outcomeTextReal.tStop = t  # not accounting for scr refresh
                outcomeTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcomeTextReal.stopped')
                outcomeTextReal.setAutoDraw(False)
        
        # *hideGambleReal* updates
        if hideGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hideGambleReal.frameNStart = frameN  # exact frame index
            hideGambleReal.tStart = t  # local t and not account for scr refresh
            hideGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hideGambleReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'hideGambleReal.started')
            hideGambleReal.setAutoDraw(True)
        if hideGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hideGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hideGambleReal.tStop = t  # not accounting for scr refresh
                hideGambleReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hideGambleReal.stopped')
                hideGambleReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in showOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "showOutcome" ---
    for thisComponent in showOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from codeFeedbackReal
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiComponents = [itiTextReal]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "iti" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiTextReal* updates
        if itiTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiTextReal.frameNStart = frameN  # exact frame index
            itiTextReal.tStart = t  # local t and not account for scr refresh
            itiTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiTextReal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiTextReal.started')
            itiTextReal.setAutoDraw(True)
        if itiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiTextReal.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                itiTextReal.tStop = t  # not accounting for scr refresh
                itiTextReal.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiTextReal.stopped')
                itiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iti" ---
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'dynamicRDM'


# --- Prepare to start Routine "selectOutcome" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
selectOutcomeComponents = []
for thisComponent in selectOutcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "selectOutcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in selectOutcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "selectOutcome" ---
for thisComponent in selectOutcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "selectOutcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "endOfTask" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
endOfTaskComponents = [endRedirect]
for thisComponent in endOfTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "endOfTask" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endRedirect* updates
    if endRedirect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endRedirect.frameNStart = frameN  # exact frame index
        endRedirect.tStart = t  # local t and not account for scr refresh
        endRedirect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endRedirect, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endRedirect.started')
        endRedirect.setAutoDraw(True)
    if endRedirect.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endRedirect.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            endRedirect.tStop = t  # not accounting for scr refresh
            endRedirect.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endRedirect.stopped')
            endRedirect.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endOfTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endOfTask" ---
for thisComponent in endOfTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
