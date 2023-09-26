#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on September 26, 2023, at 14:34
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
psychopyVersion = '2022.2.4'
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
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\cge\\Old PyschopyTask\\tasks_RDM_digitSpan\\CGTbothTasks.py',
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
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
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
# Run 'Begin Experiment' code from code
instructionsTextHeight = 0.04;
letterTextHeight = 0.1;
wrap = 1.6
Instructions = visual.TextStim(win=win, name='Instructions',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nOnce "V-Left" and "N-Right" appear on the screen, you may press "V" to select the option on the left and "N" to choose the option on the right.\n\nPress "enter" to move on to the next screen.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
inst1 = keyboard.Keyboard()

# --- Initialize components for Routine "pracStart" ---
startPract = visual.TextStim(win=win, name='startPract',
    text='There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startPracResp = keyboard.Keyboard()

# --- Initialize components for Routine "practiceTask" ---
# Run 'Begin Experiment' code from randLoc
textHeight = 0.05;
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback" ---
noRespTxt = visual.TextStim(win=win, name='noRespTxt',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=textHeight, wrapWidth=None, ori=0, 
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "postPrac" ---
postPracText = visual.TextStim(win=win, name='postPracText',
    text='Practice complete.\n\nWhen you are ready to start the real task, press "V" or "N".\n',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
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
settingUpForPart2 = visual.TextStim(win=win, name='settingUpForPart2',
    text='The first round of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "loadDynamicChoiceset" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
staticLoadChoiceset = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='staticLoadChoiceset')

# --- Initialize components for Routine "startDynamicTask" ---
moveToRDMpart2 = visual.TextStim(win=win, name='moveToRDMpart2',
    text='When you are ready to begin the next round of the gambling task, press "enter".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "rdmToSpanTransition" ---
breaktxt = visual.TextStim(win=win, name='breaktxt',
    text="You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stopBreak = keyboard.Keyboard()

# --- Initialize components for Routine "SpanGeneralInstructions" ---
GenInsText = visual.TextStim(win=win, name='GenInsText',
    text="In this task you will be asked to memorize a series of numbers and recall them. \n\nYou will do this twice, once recalling the numbers in the order as presented on the screen and once recalling the numbers in the reverse order presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. \n\nYou will complete 2 practice sets prior to starting each round of this task.\n\nPress 'enter' to continue.",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
movealong = keyboard.Keyboard()

# --- Initialize components for Routine "FSInstructions" ---
FSGenInsText = visual.TextStim(win=win, name='FSGenInsText',
    text='The practice for the forwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 3 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nIf you make a mistake you can use backspace to correct it.  \n\nDo not use spaces. \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startPractice = keyboard.Keyboard()

# --- Initialize components for Routine "ShowNumbersPractice" ---
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_practice = visual.TextStim(win=win, name='pres_text_practice',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "RecallPractice" ---
recall_txtPractice = visual.TextStim(win=win, name='recall_txtPractice',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice',
     autoLog=True,
)
cont_buttonPractice = visual.ImageStim(
    win=win,
    name='cont_buttonPractice', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice = event.Mouse(win=win)
x, y = [None, None]
mousePractice.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackPractice" ---
feedbac_textPractice = visual.TextStim(win=win, name='feedbac_textPractice',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "StartRealFS" ---
praccomplete = visual.TextStim(win=win, name='praccomplete',
    text="Practice complete! \n\nYou are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nPress 'enter' to start the task.",
    font='Open Sans',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startFSreal = keyboard.Keyboard()

# --- Initialize components for Routine "selectNumbers" ---
# Run 'Begin Experiment' code from selectNumbersFS
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitFS = 3;
maxDigitFS = 16;
#minDigitBS = 2;
#maxDigitBS = 15;
nTrialsFS = 0;
#nTrialsBS = 0;
correct = [];
incorrectCount = 0;


# --- Initialize components for Routine "ShowNumbers" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_text = visual.TextStim(win=win, name='presentation_text',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall" ---
recall_txt = visual.TextStim(win=win, name='recall_txt',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
cont_button = visual.ImageStim(
    win=win,
    name='cont_button', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "InstructionsBS" ---
BSGenInsText = visual.TextStim(win=win, name='BSGenInsText',
    text='The practice for the backwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 2 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the REVERSE order they were presented on the screen. \n\nFor example, if the numbers presented are 6 then 2, your response should be 26.\n\nIf you make a mistake you can use backspace to correct it.  \n\nDo not use spaces. \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startBSprac = keyboard.Keyboard()

# --- Initialize components for Routine "showNumbersPracticeBS" ---
fixation_3 = visual.TextStim(win=win, name='fixation_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_practice_2 = visual.TextStim(win=win, name='pres_text_practice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recallPracticeBS" ---
recall_txtPractice_2 = visual.TextStim(win=win, name='recall_txtPractice_2',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice_2',
     autoLog=True,
)
cont_buttonPractice_2 = visual.ImageStim(
    win=win,
    name='cont_buttonPractice_2', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice_2 = event.Mouse(win=win)
x, y = [None, None]
mousePractice_2.mouseClock = core.Clock()

# --- Initialize components for Routine "feedbackPracticeBS" ---
feedbac_textPractice_2 = visual.TextStim(win=win, name='feedbac_textPractice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "startRealBS" ---
praccompleteBS = visual.TextStim(win=win, name='praccompleteBS',
    text="Practice complete!\n\nYou are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nPress 'enter' to start the task.",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startBSreal = keyboard.Keyboard()

# --- Initialize components for Routine "selectNumbersBS" ---
# Run 'Begin Experiment' code from selectNumbersBScode
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitBS = 2;
maxDigitBS = 15;
nTrialsBS = 0;
correct = [];
incorrectCount = 0;

# --- Initialize components for Routine "showNumbersBS" ---
fixationBS = visual.TextStim(win=win, name='fixationBS',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_textBS = visual.TextStim(win=win, name='presentation_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "RecallBS" ---
recall_txtBS = visual.TextStim(win=win, name='recall_txtBS',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxBS = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxBS',
     autoLog=True,
)
cont_buttonBS = visual.ImageStim(
    win=win,
    name='cont_buttonBS', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouseBS = event.Mouse(win=win)
x, y = [None, None]
mouseBS.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackBS" ---
feedback_textBS = visual.TextStim(win=win, name='feedback_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to Qualtrics.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
routineForceEnded = False
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
        routineForceEnded = True
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
routineForceEnded = False
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
        routineForceEnded = True
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgtRDMPractice.xlsx', selection='0:2'),
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
    routineForceEnded = False
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
        
        
    pracLossRounded = '$%.0f' % round(riskyLoss,0)
    pracGainRounded = '$%.2f' % round(riskyGain,2)
    pracSafeRounded = '$%.2f' % round(alternative,2)
    circleRight.setFillColor([1,1,1])
    circleRight.setLineColor([1,1,1])
    lineLeft.setPos(targetPos)
    lossTxt.setPos(lossLoc)
    lossTxt.setText(pracLossRounded

)
    gainTxt.setPos(gainLoc)
    gainTxt.setText(pracGainRounded)
    safeTxt.setPos(safeLoc)
    safeTxt.setText(pracSafeRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isiPrac" ---
    continueRoutine = True
    routineForceEnded = False
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
            routineForceEnded = True
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
    routineForceEnded = False
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
    
    if outcome == riskyLoss:
        pracFeedbackRounded = "$%.0f" % round(outcome,0)
    else:
        pracFeedbackRounded = "$%.2f" % round(outcome,2)
    noRespTxt.setPos(noRespLoc)
    ocGamble.setPos(ocGambleLoc)
    ocSafe.setPos(ocSafeLoc)
    outcomeText.setColor('black', colorSpace='rgb')
    outcomeText.setPos(ocLoc)
    outcomeText.setText(pracFeedbackRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "itiPrac_2" ---
    continueRoutine = True
    routineForceEnded = False
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
            routineForceEnded = True
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
    
# completed 1 repeats of 'trials'


# --- Prepare to start Routine "postPrac" ---
continueRoutine = True
routineForceEnded = False
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
        routineForceEnded = True
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
    routineForceEnded = False
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
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    circleRightReal.setFillColor([1,1,1])
    circleRightReal.setLineColor([1,1,1])
    lineLeftReal.setPos(targetPos)
    lossTxtReal.setPos(lossLoc)
    lossTxtReal.setText(lossRounded)
    gainTxtReal.setPos(gainLoc)
    gainTxtReal.setText(gainRounded)
    safeTxtReal.setPos(safeLoc)
    safeTxtReal.setText(safeRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    routineForceEnded = False
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
    while continueRoutine and routineTimer.getTime() < 0.5:
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
            if tThisFlipGlobal > isiTextReal.tStartRefresh + .5-frameTolerance:
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedbackReal
    import random
    import math
    if not realChoice.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        riskyLoss = math.nan
        riskyGain = math.nan
        certain = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
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
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
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
    
    
    if outcome == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcome,0)
    else:
        feedbackRounded = "$%.2f" % round(outcome,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLoss)
    riskygain_values.append(riskyGain)
    certain_values.append(certain)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    outcomeTextReal.setColor('black', colorSpace='rgb')
    outcomeTextReal.setPos(ocLoc)
    outcomeTextReal.setText(feedbackRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    routineForceEnded = False
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
    while continueRoutine and routineTimer.getTime() < 1.0:
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
            if tThisFlipGlobal > itiTextReal.tStartRefresh + 1-frameTolerance:
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1 repeats of 'staticRDM'


# --- Prepare to start Routine "computeEstimates" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from gridSearchCode

### Grid Search Code
import math 

# Prepare choice set values to remove any nans
finiteChoices = []
finiteGainVals = []
finiteSafeVals = []
finiteLossVals = []

# just save trial things where participant responded
for t in range(len(choices)):
    if math.isfinite(choices[t]):
        finiteChoices.append(choices[t])
        finiteGainVals.append(riskygain_values[t])
        finiteSafeVals.append(certain_values[t])
        finiteLossVals.append(riskyloss_values[t])


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
        nll_new = negLLprospect_cgt([rho_values[r], mu_values[m]], finiteGainVals, finiteLossVals, finiteSafeVals, finiteChoices);
        if nll_new < best_nll_value:
            best_nll_value = nll_new;
            bestR = r + 1; # "+1" corrects for diff. in python vs. R indexing
            bestM = m + 1; # "+1" corrects for diff. in python vs. R indexing

print('The best R index is', bestR, 'while the best M index is', bestM, ', with an NLL of', best_nll_value);

fname.append("../tasks_RDM_digitSpan/bespoke_choicesets/bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM))
dynamicChoiceSet = fname[0]  # Set routine start values for dynamicChoiceSet
thisExp.addData('dynamicChoiceSet.routineStartVal', dynamicChoiceSet)  # Save exp start value
bestRho = bestR  # Set routine start values for bestRho
bestMu = bestM  # Set routine start values for bestMu
# keep track of which components have finished
computeEstimatesComponents = [settingUpForPart2]
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
    
    # *settingUpForPart2* updates
    if settingUpForPart2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        settingUpForPart2.frameNStart = frameN  # exact frame index
        settingUpForPart2.tStart = t  # local t and not account for scr refresh
        settingUpForPart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(settingUpForPart2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'settingUpForPart2.started')
        settingUpForPart2.setAutoDraw(True)
    if settingUpForPart2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > settingUpForPart2.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            settingUpForPart2.tStop = t  # not accounting for scr refresh
            settingUpForPart2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'settingUpForPart2.stopped')
            settingUpForPart2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
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
# the Routine "computeEstimates" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "loadDynamicChoiceset" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
loadDynamicChoicesetComponents = [text, staticLoadChoiceset]
for thisComponent in loadDynamicChoicesetComponents:
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

# --- Run Routine "loadDynamicChoiceset" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    # *staticLoadChoiceset* period
    if staticLoadChoiceset.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        staticLoadChoiceset.frameNStart = frameN  # exact frame index
        staticLoadChoiceset.tStart = t  # local t and not account for scr refresh
        staticLoadChoiceset.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(staticLoadChoiceset, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('staticLoadChoiceset.started', t)
        staticLoadChoiceset.start(2)
    elif staticLoadChoiceset.status == STARTED:  # one frame should pass before updating params and completing
        # Updating other components during *staticLoadChoiceset*
        text.setText('')
        # Component updates done
        staticLoadChoiceset.complete()  # finish the static period
        staticLoadChoiceset.tStop = staticLoadChoiceset.tStart + 2  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loadDynamicChoicesetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "loadDynamicChoiceset" ---
for thisComponent in loadDynamicChoicesetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "startDynamicTask" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
startDynamicTaskComponents = [moveToRDMpart2, key_resp]
for thisComponent in startDynamicTaskComponents:
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

# --- Run Routine "startDynamicTask" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *moveToRDMpart2* updates
    if moveToRDMpart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moveToRDMpart2.frameNStart = frameN  # exact frame index
        moveToRDMpart2.tStart = t  # local t and not account for scr refresh
        moveToRDMpart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moveToRDMpart2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moveToRDMpart2.started')
        moveToRDMpart2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startDynamicTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startDynamicTask" ---
for thisComponent in startDynamicTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "startDynamicTask" was not non-slip safe, so reset the non-slip timer
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
    routineForceEnded = False
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
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    circleRightReal.setFillColor([1,1,1])
    circleRightReal.setLineColor([1,1,1])
    lineLeftReal.setPos(targetPos)
    lossTxtReal.setPos(lossLoc)
    lossTxtReal.setText(lossRounded)
    gainTxtReal.setPos(gainLoc)
    gainTxtReal.setText(gainRounded)
    safeTxtReal.setPos(safeLoc)
    safeTxtReal.setText(safeRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "isi" ---
    continueRoutine = True
    routineForceEnded = False
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
    while continueRoutine and routineTimer.getTime() < 0.5:
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
            if tThisFlipGlobal > isiTextReal.tStartRefresh + .5-frameTolerance:
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "showOutcome" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedbackReal
    import random
    import math
    if not realChoice.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        riskyLoss = math.nan
        riskyGain = math.nan
        certain = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
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
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
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
    
    
    if outcome == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcome,0)
    else:
        feedbackRounded = "$%.2f" % round(outcome,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLoss)
    riskygain_values.append(riskyGain)
    certain_values.append(certain)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    outcomeTextReal.setColor('black', colorSpace='rgb')
    outcomeTextReal.setPos(ocLoc)
    outcomeTextReal.setText(feedbackRounded)
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    routineForceEnded = False
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
    while continueRoutine and routineTimer.getTime() < 1.0:
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
            if tThisFlipGlobal > itiTextReal.tStartRefresh + 1-frameTolerance:
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
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'dynamicRDM'


# --- Prepare to start Routine "rdmToSpanTransition" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
stopBreak.keys = []
stopBreak.rt = []
_stopBreak_allKeys = []
# keep track of which components have finished
rdmToSpanTransitionComponents = [breaktxt, stopBreak]
for thisComponent in rdmToSpanTransitionComponents:
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

# --- Run Routine "rdmToSpanTransition" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breaktxt* updates
    if breaktxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        breaktxt.frameNStart = frameN  # exact frame index
        breaktxt.tStart = t  # local t and not account for scr refresh
        breaktxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breaktxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'breaktxt.started')
        breaktxt.setAutoDraw(True)
    
    # *stopBreak* updates
    waitOnFlip = False
    if stopBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stopBreak.frameNStart = frameN  # exact frame index
        stopBreak.tStart = t  # local t and not account for scr refresh
        stopBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stopBreak, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'stopBreak.started')
        stopBreak.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(stopBreak.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(stopBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if stopBreak.status == STARTED and not waitOnFlip:
        theseKeys = stopBreak.getKeys(keyList=['return'], waitRelease=False)
        _stopBreak_allKeys.extend(theseKeys)
        if len(_stopBreak_allKeys):
            stopBreak.keys = _stopBreak_allKeys[-1].name  # just the last key pressed
            stopBreak.rt = _stopBreak_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rdmToSpanTransitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rdmToSpanTransition" ---
for thisComponent in rdmToSpanTransitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if stopBreak.keys in ['', [], None]:  # No response was made
    stopBreak.keys = None
thisExp.addData('stopBreak.keys',stopBreak.keys)
if stopBreak.keys != None:  # we had a response
    thisExp.addData('stopBreak.rt', stopBreak.rt)
thisExp.nextEntry()
# the Routine "rdmToSpanTransition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "SpanGeneralInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
movealong.keys = []
movealong.rt = []
_movealong_allKeys = []
# keep track of which components have finished
SpanGeneralInstructionsComponents = [GenInsText, movealong]
for thisComponent in SpanGeneralInstructionsComponents:
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

# --- Run Routine "SpanGeneralInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GenInsText* updates
    if GenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GenInsText.frameNStart = frameN  # exact frame index
        GenInsText.tStart = t  # local t and not account for scr refresh
        GenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GenInsText.started')
        GenInsText.setAutoDraw(True)
    
    # *movealong* updates
    waitOnFlip = False
    if movealong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movealong.frameNStart = frameN  # exact frame index
        movealong.tStart = t  # local t and not account for scr refresh
        movealong.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movealong, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movealong.started')
        movealong.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(movealong.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(movealong.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if movealong.status == STARTED and not waitOnFlip:
        theseKeys = movealong.getKeys(keyList=['return'], waitRelease=False)
        _movealong_allKeys.extend(theseKeys)
        if len(_movealong_allKeys):
            movealong.keys = _movealong_allKeys[-1].name  # just the last key pressed
            movealong.rt = _movealong_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SpanGeneralInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SpanGeneralInstructions" ---
for thisComponent in SpanGeneralInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if movealong.keys in ['', [], None]:  # No response was made
    movealong.keys = None
thisExp.addData('movealong.keys',movealong.keys)
if movealong.keys != None:  # we had a response
    thisExp.addData('movealong.rt', movealong.rt)
thisExp.nextEntry()
# the Routine "SpanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "FSInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
startPractice.keys = []
startPractice.rt = []
_startPractice_allKeys = []
# keep track of which components have finished
FSInstructionsComponents = [FSGenInsText, startPractice]
for thisComponent in FSInstructionsComponents:
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

# --- Run Routine "FSInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FSGenInsText* updates
    if FSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FSGenInsText.frameNStart = frameN  # exact frame index
        FSGenInsText.tStart = t  # local t and not account for scr refresh
        FSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FSGenInsText.started')
        FSGenInsText.setAutoDraw(True)
    
    # *startPractice* updates
    waitOnFlip = False
    if startPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startPractice.frameNStart = frameN  # exact frame index
        startPractice.tStart = t  # local t and not account for scr refresh
        startPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startPractice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startPractice.started')
        startPractice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startPractice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startPractice.status == STARTED and not waitOnFlip:
        theseKeys = startPractice.getKeys(keyList=['return'], waitRelease=False)
        _startPractice_allKeys.extend(theseKeys)
        if len(_startPractice_allKeys):
            startPractice.keys = _startPractice_allKeys[-1].name  # just the last key pressed
            startPractice.rt = _startPractice_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FSInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "FSInstructions" ---
for thisComponent in FSInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startPractice.keys in ['', [], None]:  # No response was made
    startPractice.keys = None
thisExp.addData('startPractice.keys',startPractice.keys)
if startPractice.keys != None:  # we had a response
    thisExp.addData('startPractice.rt', startPractice.rt)
thisExp.nextEntry()
# the Routine "FSInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialFSPractice = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='trialFSPractice')
thisExp.addLoop(trialFSPractice)  # add the loop to the experiment
thisTrialFSPractice = trialFSPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
if thisTrialFSPractice != None:
    for paramName in thisTrialFSPractice:
        exec('{} = thisTrialFSPractice[paramName]'.format(paramName))

for thisTrialFSPractice in trialFSPractice:
    currentLoop = trialFSPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
    if thisTrialFSPractice != None:
        for paramName in thisTrialFSPractice:
            exec('{} = thisTrialFSPractice[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    DigitLoopPractice = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DigitLoopPractice')
    thisExp.addLoop(DigitLoopPractice)  # add the loop to the experiment
    thisDigitLoopPractice = DigitLoopPractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
    if thisDigitLoopPractice != None:
        for paramName in thisDigitLoopPractice:
            exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
    
    for thisDigitLoopPractice in DigitLoopPractice:
        currentLoop = DigitLoopPractice
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
        if thisDigitLoopPractice != None:
            for paramName in thisDigitLoopPractice:
                exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbersPractice" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        pres_text_practice.setText(str(digits)[DigitLoopPractice.thisN])
        # keep track of which components have finished
        ShowNumbersPracticeComponents = [fixation_2, pres_text_practice]
        for thisComponent in ShowNumbersPracticeComponents:
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
        
        # --- Run Routine "ShowNumbersPractice" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    fixation_2.setAutoDraw(False)
            
            # *pres_text_practice* updates
            if pres_text_practice.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice.frameNStart = frameN  # exact frame index
                pres_text_practice.tStart = t  # local t and not account for scr refresh
                pres_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice.started')
                pres_text_practice.setAutoDraw(True)
            if pres_text_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice.tStop = t  # not accounting for scr refresh
                    pres_text_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice.stopped')
                    pres_text_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbersPractice" ---
        for thisComponent in ShowNumbersPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'DigitLoopPractice'
    
    
    # --- Prepare to start Routine "RecallPractice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textboxPractice.reset()
    # setup some python lists for storing info about the mousePractice
    mousePractice.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallPracticeComponents = [recall_txtPractice, textboxPractice, cont_buttonPractice, mousePractice]
    for thisComponent in RecallPracticeComponents:
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
    
    # --- Run Routine "RecallPractice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice* updates
        if recall_txtPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice.frameNStart = frameN  # exact frame index
            recall_txtPractice.tStart = t  # local t and not account for scr refresh
            recall_txtPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice.started')
            recall_txtPractice.setAutoDraw(True)
        
        # *textboxPractice* updates
        if textboxPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice.frameNStart = frameN  # exact frame index
            textboxPractice.tStart = t  # local t and not account for scr refresh
            textboxPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice.started')
            textboxPractice.setAutoDraw(True)
        
        # *cont_buttonPractice* updates
        if cont_buttonPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice.frameNStart = frameN  # exact frame index
            cont_buttonPractice.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice.started')
            cont_buttonPractice.setAutoDraw(True)
        # *mousePractice* updates
        if mousePractice.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice.frameNStart = frameN  # exact frame index
            mousePractice.tStart = t  # local t and not account for scr refresh
            mousePractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice.started', t)
            mousePractice.status = STARTED
            mousePractice.mouseClock.reset()
            prevButtonState = mousePractice.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice)
                        clickableList = cont_buttonPractice
                    except:
                        clickableList = [cont_buttonPractice]
                    for obj in clickableList:
                        if obj.contains(mousePractice):
                            gotValidClick = True
                            mousePractice.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallPractice" ---
    for thisComponent in RecallPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialFSPractice.addData('textboxPractice.text',textboxPractice.text)
    # Run 'End Routine' code from code_3practice
    #for r in range(len(digitsForTrial)):
    #    digitsForTrial[r] = str(digitsForTrial[r])
    
    #digitsForTrial = ''.join(digitsForTrial)
    
    if textboxPractice.text == str(digits):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialFSPractice (TrialHandler)
    x, y = mousePractice.getPos()
    buttons = mousePractice.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice)
            clickableList = cont_buttonPractice
        except:
            clickableList = [cont_buttonPractice]
        for obj in clickableList:
            if obj.contains(mousePractice):
                gotValidClick = True
                mousePractice.clicked_name.append(obj.name)
    trialFSPractice.addData('mousePractice.x', x)
    trialFSPractice.addData('mousePractice.y', y)
    trialFSPractice.addData('mousePractice.leftButton', buttons[0])
    trialFSPractice.addData('mousePractice.midButton', buttons[1])
    trialFSPractice.addData('mousePractice.rightButton', buttons[2])
    if len(mousePractice.clicked_name):
        trialFSPractice.addData('mousePractice.clicked_name', mousePractice.clicked_name[0])
    # the Routine "RecallPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackPractice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    feedbac_textPractice.setText(fbTxt)
    # keep track of which components have finished
    FeedbackPracticeComponents = [feedbac_textPractice]
    for thisComponent in FeedbackPracticeComponents:
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
    
    # --- Run Routine "FeedbackPractice" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice* updates
        if feedbac_textPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice.frameNStart = frameN  # exact frame index
            feedbac_textPractice.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice.started')
            feedbac_textPractice.setAutoDraw(True)
        if feedbac_textPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice.tStop = t  # not accounting for scr refresh
                feedbac_textPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice.stopped')
                feedbac_textPractice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackPractice" ---
    for thisComponent in FeedbackPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialFSPractice'


# --- Prepare to start Routine "StartRealFS" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
startFSreal.keys = []
startFSreal.rt = []
_startFSreal_allKeys = []
# keep track of which components have finished
StartRealFSComponents = [praccomplete, startFSreal]
for thisComponent in StartRealFSComponents:
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

# --- Run Routine "StartRealFS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccomplete* updates
    if praccomplete.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccomplete.frameNStart = frameN  # exact frame index
        praccomplete.tStart = t  # local t and not account for scr refresh
        praccomplete.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccomplete, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccomplete.started')
        praccomplete.setAutoDraw(True)
    
    # *startFSreal* updates
    waitOnFlip = False
    if startFSreal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startFSreal.frameNStart = frameN  # exact frame index
        startFSreal.tStart = t  # local t and not account for scr refresh
        startFSreal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startFSreal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startFSreal.started')
        startFSreal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startFSreal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startFSreal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startFSreal.status == STARTED and not waitOnFlip:
        theseKeys = startFSreal.getKeys(keyList=['return'], waitRelease=False)
        _startFSreal_allKeys.extend(theseKeys)
        if len(_startFSreal_allKeys):
            startFSreal.keys = _startFSreal_allKeys[-1].name  # just the last key pressed
            startFSreal.rt = _startFSreal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartRealFSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StartRealFS" ---
for thisComponent in StartRealFSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startFSreal.keys in ['', [], None]:  # No response was made
    startFSreal.keys = None
thisExp.addData('startFSreal.keys',startFSreal.keys)
if startFSreal.keys != None:  # we had a response
    thisExp.addData('startFSreal.rt', startFSreal.rt)
thisExp.nextEntry()
# the Routine "StartRealFS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsFS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber.xlsx', selection='0:3'),
    seed=None, name='trialsFS')
thisExp.addLoop(trialsFS)  # add the loop to the experiment
thisTrialsFS = trialsFS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsFS.rgb)
if thisTrialsFS != None:
    for paramName in thisTrialsFS:
        exec('{} = thisTrialsFS[paramName]'.format(paramName))

for thisTrialsFS in trialsFS:
    currentLoop = trialsFS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsFS.rgb)
    if thisTrialsFS != None:
        for paramName in thisTrialsFS:
            exec('{} = thisTrialsFS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbers" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersFS
    import random
    
    nTrialsFS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsFS ==1:
        digitSpan = minDigitFS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitFS:
        digitSpan = minDigitFS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersComponents = []
    for thisComponent in selectNumbersComponents:
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
    
    # --- Run Routine "selectNumbers" ---
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectNumbersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbers" ---
    for thisComponent in selectNumbersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoop = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoop')
    thisExp.addLoop(digitLoop)  # add the loop to the experiment
    thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
    if thisDigitLoop != None:
        for paramName in thisDigitLoop:
            exec('{} = thisDigitLoop[paramName]'.format(paramName))
    
    for thisDigitLoop in digitLoop:
        currentLoop = digitLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                exec('{} = thisDigitLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbers" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeFS
        tmpNumber = digitsForTrial[digitLoop.thisN]
        presentation_text.setText(tmpNumber)
        # keep track of which components have finished
        ShowNumbersComponents = [fixation, presentation_text]
        for thisComponent in ShowNumbersComponents:
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
        
        # --- Run Routine "ShowNumbers" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *presentation_text* updates
            if presentation_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_text.frameNStart = frameN  # exact frame index
                presentation_text.tStart = t  # local t and not account for scr refresh
                presentation_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_text.started')
                presentation_text.setAutoDraw(True)
            if presentation_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_text.tStop = t  # not accounting for scr refresh
                    presentation_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_text.stopped')
                    presentation_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbers" ---
        for thisComponent in ShowNumbersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeFS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoop'
    
    
    # --- Prepare to start Routine "Recall" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textbox.reset()
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallComponents = [recall_txt, textbox, cont_button, mouse_3]
    for thisComponent in RecallComponents:
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
    
    # --- Run Routine "Recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txt* updates
        if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txt.frameNStart = frameN  # exact frame index
            recall_txt.tStart = t  # local t and not account for scr refresh
            recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txt.started')
            recall_txt.setAutoDraw(True)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            textbox.setAutoDraw(True)
        
        # *cont_button* updates
        if cont_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_button.frameNStart = frameN  # exact frame index
            cont_button.tStart = t  # local t and not account for scr refresh
            cont_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_button.started')
            cont_button.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_button)
                        clickableList = cont_button
                    except:
                        clickableList = [cont_button]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall" ---
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsFS.addData('textbox.text',textbox.text)
    # Run 'End Routine' code from code_3
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textbox.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsFS (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_button)
            clickableList = cont_button
        except:
            clickableList = [cont_button]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    trialsFS.addData('mouse_3.x', x)
    trialsFS.addData('mouse_3.y', y)
    trialsFS.addData('mouse_3.leftButton', buttons[0])
    trialsFS.addData('mouse_3.midButton', buttons[1])
    trialsFS.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        trialsFS.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    feedback_text.setText(fbTxt)
    # keep track of which components have finished
    FeedbackComponents = [feedback_text]
    for thisComponent in FeedbackComponents:
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
    
    # --- Run Routine "Feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsFS'


# --- Prepare to start Routine "InstructionsBS" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
startBSprac.keys = []
startBSprac.rt = []
_startBSprac_allKeys = []
# keep track of which components have finished
InstructionsBSComponents = [BSGenInsText, startBSprac]
for thisComponent in InstructionsBSComponents:
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

# --- Run Routine "InstructionsBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BSGenInsText* updates
    if BSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSGenInsText.frameNStart = frameN  # exact frame index
        BSGenInsText.tStart = t  # local t and not account for scr refresh
        BSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BSGenInsText.started')
        BSGenInsText.setAutoDraw(True)
    
    # *startBSprac* updates
    waitOnFlip = False
    if startBSprac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startBSprac.frameNStart = frameN  # exact frame index
        startBSprac.tStart = t  # local t and not account for scr refresh
        startBSprac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startBSprac, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startBSprac.started')
        startBSprac.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startBSprac.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startBSprac.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startBSprac.status == STARTED and not waitOnFlip:
        theseKeys = startBSprac.getKeys(keyList=['return'], waitRelease=False)
        _startBSprac_allKeys.extend(theseKeys)
        if len(_startBSprac_allKeys):
            startBSprac.keys = _startBSprac_allKeys[-1].name  # just the last key pressed
            startBSprac.rt = _startBSprac_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsBS" ---
for thisComponent in InstructionsBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startBSprac.keys in ['', [], None]:  # No response was made
    startBSprac.keys = None
thisExp.addData('startBSprac.keys',startBSprac.keys)
if startBSprac.keys != None:  # we had a response
    thisExp.addData('startBSprac.rt', startBSprac.rt)
thisExp.nextEntry()
# the Routine "InstructionsBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsPracticeBS = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='trialsPracticeBS')
thisExp.addLoop(trialsPracticeBS)  # add the loop to the experiment
thisTrialsPracticeBS = trialsPracticeBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
if thisTrialsPracticeBS != None:
    for paramName in thisTrialsPracticeBS:
        exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))

for thisTrialsPracticeBS in trialsPracticeBS:
    currentLoop = trialsPracticeBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
    if thisTrialsPracticeBS != None:
        for paramName in thisTrialsPracticeBS:
            exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    digitLoopPracticeBS = data.TrialHandler(nReps=digitSpanReverse, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopPracticeBS')
    thisExp.addLoop(digitLoopPracticeBS)  # add the loop to the experiment
    thisDigitLoopPracticeBS = digitLoopPracticeBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
    if thisDigitLoopPracticeBS != None:
        for paramName in thisDigitLoopPracticeBS:
            exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
    
    for thisDigitLoopPracticeBS in digitLoopPracticeBS:
        currentLoop = digitLoopPracticeBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
        if thisDigitLoopPracticeBS != None:
            for paramName in thisDigitLoopPracticeBS:
                exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersPracticeBS" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        pres_text_practice_2.setText(str(digitsReverse)[digitLoopPracticeBS.thisN])
        # keep track of which components have finished
        showNumbersPracticeBSComponents = [fixation_3, pres_text_practice_2]
        for thisComponent in showNumbersPracticeBSComponents:
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
        
        # --- Run Routine "showNumbersPracticeBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_3* updates
            if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_3.frameNStart = frameN  # exact frame index
                fixation_3.tStart = t  # local t and not account for scr refresh
                fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.started')
                fixation_3.setAutoDraw(True)
            if fixation_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_3.tStop = t  # not accounting for scr refresh
                    fixation_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                    fixation_3.setAutoDraw(False)
            
            # *pres_text_practice_2* updates
            if pres_text_practice_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice_2.frameNStart = frameN  # exact frame index
                pres_text_practice_2.tStart = t  # local t and not account for scr refresh
                pres_text_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice_2.started')
                pres_text_practice_2.setAutoDraw(True)
            if pres_text_practice_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice_2.tStop = t  # not accounting for scr refresh
                    pres_text_practice_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice_2.stopped')
                    pres_text_practice_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersPracticeBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersPracticeBS" ---
        for thisComponent in showNumbersPracticeBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpanReverse repeats of 'digitLoopPracticeBS'
    
    
    # --- Prepare to start Routine "recallPracticeBS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textboxPractice_2.reset()
    # setup some python lists for storing info about the mousePractice_2
    mousePractice_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    recallPracticeBSComponents = [recall_txtPractice_2, textboxPractice_2, cont_buttonPractice_2, mousePractice_2]
    for thisComponent in recallPracticeBSComponents:
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
    
    # --- Run Routine "recallPracticeBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice_2* updates
        if recall_txtPractice_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice_2.frameNStart = frameN  # exact frame index
            recall_txtPractice_2.tStart = t  # local t and not account for scr refresh
            recall_txtPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice_2.started')
            recall_txtPractice_2.setAutoDraw(True)
        
        # *textboxPractice_2* updates
        if textboxPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice_2.frameNStart = frameN  # exact frame index
            textboxPractice_2.tStart = t  # local t and not account for scr refresh
            textboxPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice_2.started')
            textboxPractice_2.setAutoDraw(True)
        
        # *cont_buttonPractice_2* updates
        if cont_buttonPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice_2.frameNStart = frameN  # exact frame index
            cont_buttonPractice_2.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice_2.started')
            cont_buttonPractice_2.setAutoDraw(True)
        # *mousePractice_2* updates
        if mousePractice_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice_2.frameNStart = frameN  # exact frame index
            mousePractice_2.tStart = t  # local t and not account for scr refresh
            mousePractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice_2.started', t)
            mousePractice_2.status = STARTED
            mousePractice_2.mouseClock.reset()
            prevButtonState = mousePractice_2.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice_2.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice_2)
                        clickableList = cont_buttonPractice_2
                    except:
                        clickableList = [cont_buttonPractice_2]
                    for obj in clickableList:
                        if obj.contains(mousePractice_2):
                            gotValidClick = True
                            mousePractice_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recallPracticeBS" ---
    for thisComponent in recallPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsPracticeBS.addData('textboxPractice_2.text',textboxPractice_2.text)
    # Run 'End Routine' code from code_3practice_2
    if textboxPractice_2.text == str(digitsReverseCorrAnswer):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsPracticeBS (TrialHandler)
    x, y = mousePractice_2.getPos()
    buttons = mousePractice_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice_2)
            clickableList = cont_buttonPractice_2
        except:
            clickableList = [cont_buttonPractice_2]
        for obj in clickableList:
            if obj.contains(mousePractice_2):
                gotValidClick = True
                mousePractice_2.clicked_name.append(obj.name)
    trialsPracticeBS.addData('mousePractice_2.x', x)
    trialsPracticeBS.addData('mousePractice_2.y', y)
    trialsPracticeBS.addData('mousePractice_2.leftButton', buttons[0])
    trialsPracticeBS.addData('mousePractice_2.midButton', buttons[1])
    trialsPracticeBS.addData('mousePractice_2.rightButton', buttons[2])
    if len(mousePractice_2.clicked_name):
        trialsPracticeBS.addData('mousePractice_2.clicked_name', mousePractice_2.clicked_name[0])
    # the Routine "recallPracticeBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedbackPracticeBS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    feedbac_textPractice_2.setText(fbTxt)
    # keep track of which components have finished
    feedbackPracticeBSComponents = [feedbac_textPractice_2]
    for thisComponent in feedbackPracticeBSComponents:
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
    
    # --- Run Routine "feedbackPracticeBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice_2* updates
        if feedbac_textPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice_2.frameNStart = frameN  # exact frame index
            feedbac_textPractice_2.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.started')
            feedbac_textPractice_2.setAutoDraw(True)
        if feedbac_textPractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice_2.tStop = t  # not accounting for scr refresh
                feedbac_textPractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.stopped')
                feedbac_textPractice_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedbackPracticeBS" ---
    for thisComponent in feedbackPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsPracticeBS'


# --- Prepare to start Routine "startRealBS" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
startBSreal.keys = []
startBSreal.rt = []
_startBSreal_allKeys = []
# keep track of which components have finished
startRealBSComponents = [praccompleteBS, startBSreal]
for thisComponent in startRealBSComponents:
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

# --- Run Routine "startRealBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccompleteBS* updates
    if praccompleteBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccompleteBS.frameNStart = frameN  # exact frame index
        praccompleteBS.tStart = t  # local t and not account for scr refresh
        praccompleteBS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccompleteBS, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccompleteBS.started')
        praccompleteBS.setAutoDraw(True)
    
    # *startBSreal* updates
    waitOnFlip = False
    if startBSreal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startBSreal.frameNStart = frameN  # exact frame index
        startBSreal.tStart = t  # local t and not account for scr refresh
        startBSreal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startBSreal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startBSreal.started')
        startBSreal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startBSreal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startBSreal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startBSreal.status == STARTED and not waitOnFlip:
        theseKeys = startBSreal.getKeys(keyList=['return'], waitRelease=False)
        _startBSreal_allKeys.extend(theseKeys)
        if len(_startBSreal_allKeys):
            startBSreal.keys = _startBSreal_allKeys[-1].name  # just the last key pressed
            startBSreal.rt = _startBSreal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startRealBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startRealBS" ---
for thisComponent in startRealBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startBSreal.keys in ['', [], None]:  # No response was made
    startBSreal.keys = None
thisExp.addData('startBSreal.keys',startBSreal.keys)
if startBSreal.keys != None:  # we had a response
    thisExp.addData('startBSreal.rt', startBSreal.rt)
thisExp.nextEntry()
# the Routine "startRealBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsBS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber.xlsx', selection='0:3'),
    seed=None, name='trialsBS')
thisExp.addLoop(trialsBS)  # add the loop to the experiment
thisTrialsBS = trialsBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
if thisTrialsBS != None:
    for paramName in thisTrialsBS:
        exec('{} = thisTrialsBS[paramName]'.format(paramName))

for thisTrialsBS in trialsBS:
    currentLoop = trialsBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
    if thisTrialsBS != None:
        for paramName in thisTrialsBS:
            exec('{} = thisTrialsBS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbersBS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersBScode
    import random
    
    nTrialsBS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsBS ==1:
        correct = [];
        digitSpan = minDigitBS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitBS:
        digitSpan = minDigitBS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersBSComponents = []
    for thisComponent in selectNumbersBSComponents:
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
    
    # --- Run Routine "selectNumbersBS" ---
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectNumbersBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbersBS" ---
    for thisComponent in selectNumbersBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoopBS = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopBS')
    thisExp.addLoop(digitLoopBS)  # add the loop to the experiment
    thisDigitLoopBS = digitLoopBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
    if thisDigitLoopBS != None:
        for paramName in thisDigitLoopBS:
            exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
    
    for thisDigitLoopBS in digitLoopBS:
        currentLoop = digitLoopBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
        if thisDigitLoopBS != None:
            for paramName in thisDigitLoopBS:
                exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersBS" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeBS
        tmpNumber = digitsForTrial[digitLoopBS.thisN]
        presentation_textBS.setText(tmpNumber)
        # keep track of which components have finished
        showNumbersBSComponents = [fixationBS, presentation_textBS]
        for thisComponent in showNumbersBSComponents:
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
        
        # --- Run Routine "showNumbersBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationBS* updates
            if fixationBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationBS.frameNStart = frameN  # exact frame index
                fixationBS.tStart = t  # local t and not account for scr refresh
                fixationBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationBS.started')
                fixationBS.setAutoDraw(True)
            if fixationBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationBS.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationBS.tStop = t  # not accounting for scr refresh
                    fixationBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationBS.stopped')
                    fixationBS.setAutoDraw(False)
            
            # *presentation_textBS* updates
            if presentation_textBS.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_textBS.frameNStart = frameN  # exact frame index
                presentation_textBS.tStart = t  # local t and not account for scr refresh
                presentation_textBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_textBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_textBS.started')
                presentation_textBS.setAutoDraw(True)
            if presentation_textBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_textBS.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_textBS.tStop = t  # not accounting for scr refresh
                    presentation_textBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_textBS.stopped')
                    presentation_textBS.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersBS" ---
        for thisComponent in showNumbersBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeBS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoopBS'
    
    
    # --- Prepare to start Routine "RecallBS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textboxBS.reset()
    # setup some python lists for storing info about the mouseBS
    mouseBS.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RecallBSComponents = [recall_txtBS, textboxBS, cont_buttonBS, mouseBS]
    for thisComponent in RecallBSComponents:
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
    
    # --- Run Routine "RecallBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtBS* updates
        if recall_txtBS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtBS.frameNStart = frameN  # exact frame index
            recall_txtBS.tStart = t  # local t and not account for scr refresh
            recall_txtBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtBS.started')
            recall_txtBS.setAutoDraw(True)
        
        # *textboxBS* updates
        if textboxBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxBS.frameNStart = frameN  # exact frame index
            textboxBS.tStart = t  # local t and not account for scr refresh
            textboxBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxBS.started')
            textboxBS.setAutoDraw(True)
        
        # *cont_buttonBS* updates
        if cont_buttonBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonBS.frameNStart = frameN  # exact frame index
            cont_buttonBS.tStart = t  # local t and not account for scr refresh
            cont_buttonBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonBS.started')
            cont_buttonBS.setAutoDraw(True)
        # *mouseBS* updates
        if mouseBS.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseBS.frameNStart = frameN  # exact frame index
            mouseBS.tStart = t  # local t and not account for scr refresh
            mouseBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseBS.started', t)
            mouseBS.status = STARTED
            mouseBS.mouseClock.reset()
            prevButtonState = mouseBS.getPressed()  # if button is down already this ISN'T a new click
        if mouseBS.status == STARTED:  # only update if started and not finished!
            buttons = mouseBS.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonBS)
                        clickableList = cont_buttonBS
                    except:
                        clickableList = [cont_buttonBS]
                    for obj in clickableList:
                        if obj.contains(mouseBS):
                            gotValidClick = True
                            mouseBS.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallBS" ---
    for thisComponent in RecallBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsBS.addData('textboxBS.text',textboxBS.text)
    # Run 'End Routine' code from code_3BS
    digitsForTrial.reverse(); # reverse order for backward span
    
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textboxBS.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsBS (TrialHandler)
    x, y = mouseBS.getPos()
    buttons = mouseBS.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonBS)
            clickableList = cont_buttonBS
        except:
            clickableList = [cont_buttonBS]
        for obj in clickableList:
            if obj.contains(mouseBS):
                gotValidClick = True
                mouseBS.clicked_name.append(obj.name)
    trialsBS.addData('mouseBS.x', x)
    trialsBS.addData('mouseBS.y', y)
    trialsBS.addData('mouseBS.leftButton', buttons[0])
    trialsBS.addData('mouseBS.midButton', buttons[1])
    trialsBS.addData('mouseBS.rightButton', buttons[2])
    if len(mouseBS.clicked_name):
        trialsBS.addData('mouseBS.clicked_name', mouseBS.clicked_name[0])
    # the Routine "RecallBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackBS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    feedback_textBS.setText(fbTxt)
    # keep track of which components have finished
    FeedbackBSComponents = [feedback_textBS]
    for thisComponent in FeedbackBSComponents:
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
    
    # --- Run Routine "FeedbackBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_textBS* updates
        if feedback_textBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_textBS.frameNStart = frameN  # exact frame index
            feedback_textBS.tStart = t  # local t and not account for scr refresh
            feedback_textBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_textBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_textBS.started')
            feedback_textBS.setAutoDraw(True)
        if feedback_textBS.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_textBS.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_textBS.tStop = t  # not accounting for scr refresh
                feedback_textBS.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_textBS.stopped')
                feedback_textBS.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackBS" ---
    for thisComponent in FeedbackBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsBS'


# --- Prepare to start Routine "END" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [ThankYou]
for thisComponent in ENDComponents:
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

# --- Run Routine "END" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.tStart = t  # local t and not account for scr refresh
        ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ThankYou.started')
        ThankYou.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "END" ---
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
