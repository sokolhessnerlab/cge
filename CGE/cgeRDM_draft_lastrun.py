#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on September 29, 2023, at 02:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.1')


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
expName = 'cgeRDMtask'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE\\cgeRDM_draft_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.5216,0.5216,0.5216], colorSpace='rgb',
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

# --- Initialize components for Routine "SetUp" ---
# Run 'Begin Experiment' code from setupCode
instructionsTextHeight = .05
lettersTextHeight = .1
wrap = 1.5

initITIstatic = []
initITIdynamic = []

# Isoluminant Colors Used 
color1 = [0.5216,0.5216,0.5216]
color2 = [-0.0667,0.6392,1]
# BLUE ### Choice Shape; V, N, and OR text
# PsychoPy RGB -1:1 [-0.0667,0.6392,1] # RGB 0:255 [119,209,205]
# GREY ### Background; Choice Line
# psychopy RGB -1:1 [0.5216,0.5216,0.5216] # RGB 0:255 [194,194,194] 

### Fixed Practice Trial Locations
circLeftLoc=[-.35,0]
circRightLoc=[.35,0]
ORtextLoc=[0,0]
VleftLoc=[-.35,-.35]
NrightLoc=[.35,-.35]

# --- Initialize components for Routine "cgeRDMstart" ---
CGErdmStartText = visual.TextStim(win=win, name='CGErdmStartText',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nYou may press "V" to select the option on the left and "N" to select the option on the right.\n\nPress "enter" to move on to the next screen.',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=wrap, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
CGErdmStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "pracStart" ---
pracStartText = visual.TextStim(win=win, name='pracStartText',
    text='There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pracStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "pracChoice" ---
# Run 'Begin Experiment' code from pracChoiceRandLoc
textHeight = 0.05;
pracCircLeft = visual.ShapeStim(
    win=win, name='pracCircLeft',
    size=(.5, .5), vertices='circle',
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-1.0, interpolate=True)
pracCircRight = visual.ShapeStim(
    win=win, name='pracCircRight',
    size=(0.5, 0.5), vertices='circle',
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
pracRiskLine = visual.Rect(
    win=win, name='pracRiskLine',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-3.0, interpolate=True)
pracORtext = visual.TextStim(win=win, name='pracORtext',
    text='OR',
    font='Arial',
    pos=ORtextLoc, height=0.05, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
pracLossText = visual.TextStim(win=win, name='pracLossText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
pracGainText = visual.TextStim(win=win, name='pracGainText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
pracSafeText = visual.TextStim(win=win, name='pracSafeText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
pracVleft = visual.TextStim(win=win, name='pracVleft',
    text='V-Left',
    font='Arial',
    pos=VleftLoc, height=0.05, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
pracNright = visual.TextStim(win=win, name='pracNright',
    text='N-Right',
    font='Arial',
    pos=NrightLoc, height=0.05, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
pracChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "pracISI" ---
isiPracFix = visual.TextStim(win=win, name='isiPracFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pracOutcome" ---
pracNoRespText = visual.TextStim(win=win, name='pracNoRespText',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=textHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pracRiskOC = visual.ShapeStim(
    win=win, name='pracRiskOC',
    size=(0.5, 0.5), vertices='circle',
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-2.0, interpolate=True)
pracSafeOC = visual.ShapeStim(
    win=win, name='pracSafeOC',
    size=(0.5, 0.5), vertices='circle',
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-3.0, interpolate=True)
pracOCtext = visual.TextStim(win=win, name='pracOCtext',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
pracHideRisk = visual.Rect(
    win=win, name='pracHideRisk',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "pracITI" ---
itiPracFix = visual.TextStim(win=win, name='itiPracFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "staticStart" ---
staticStartText = visual.TextStim(win=win, name='staticStartText',
    text='Practice complete.\n\nWhen you are ready to start ROUND 1 of the task, press "V" or "N".\n',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
staticStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "realChoice" ---
# Run 'Begin Experiment' code from realChoiceRandLoc
loc = [];


realCircLeft = visual.Rect(
    win=win, name='realCircLeft',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-1.0, interpolate=True)
realCircRight = visual.Rect(
    win=win, name='realCircRight',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
realRiskLine = visual.Rect(
    win=win, name='realRiskLine',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-3.0, interpolate=True)
realORtext = visual.TextStim(win=win, name='realORtext',
    text='OR',
    font='Arial',
    pos=ORtextLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
realLossText = visual.TextStim(win=win, name='realLossText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
realGainText = visual.TextStim(win=win, name='realGainText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
realSafeText = visual.TextStim(win=win, name='realSafeText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
realVleft = visual.TextStim(win=win, name='realVleft',
    text='V-Left',
    font='Arial',
    pos=VleftLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
realNright = visual.TextStim(win=win, name='realNright',
    text='N-Right',
    font='Arial',
    pos=NrightLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "realISI" ---
isiFix = visual.TextStim(win=win, name='isiFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "staticOutcome" ---
# Run 'Begin Experiment' code from staticOCcode
actualITI = []
riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []
staticNoRespText = visual.TextStim(win=win, name='staticNoRespText',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
staticRiskOC = visual.Rect(
    win=win, name='staticRiskOC',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-2.0, interpolate=True)
staticSafeOC = visual.Rect(
    win=win, name='staticSafeOC',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-3.0, interpolate=True)
staticOCtext = visual.TextStim(win=win, name='staticOCtext',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
staticHideRisk = visual.Rect(
    win=win, name='staticHideRisk',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "realITI" ---
itiFix = visual.TextStim(win=win, name='itiFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "computeBestFit" ---
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
setupBestFit = visual.TextStim(win=win, name='setupBestFit',
    text='ROUND 1 of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "loadingDynamicChoices" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "dynamicStart" ---
dynamicStartText = visual.TextStim(win=win, name='dynamicStartText',
    text='When you are ready to start ROUND 2 of the task, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dynamicStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "realChoice" ---
# Run 'Begin Experiment' code from realChoiceRandLoc
loc = [];


realCircLeft = visual.Rect(
    win=win, name='realCircLeft',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-1.0, interpolate=True)
realCircRight = visual.Rect(
    win=win, name='realCircRight',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
realRiskLine = visual.Rect(
    win=win, name='realRiskLine',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-3.0, interpolate=True)
realORtext = visual.TextStim(win=win, name='realORtext',
    text='OR',
    font='Arial',
    pos=ORtextLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
realLossText = visual.TextStim(win=win, name='realLossText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
realGainText = visual.TextStim(win=win, name='realGainText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
realSafeText = visual.TextStim(win=win, name='realSafeText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
realVleft = visual.TextStim(win=win, name='realVleft',
    text='V-Left',
    font='Arial',
    pos=VleftLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
realNright = visual.TextStim(win=win, name='realNright',
    text='N-Right',
    font='Arial',
    pos=NrightLoc, height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "realISI" ---
isiFix = visual.TextStim(win=win, name='isiFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "dynamicOutcome" ---
# Run 'Begin Experiment' code from dynamicOCcode
riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []
dynamicNoRespText = visual.TextStim(win=win, name='dynamicNoRespText',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
dynamicRiskOC = visual.Rect(
    win=win, name='dynamicRiskOC',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-2.0, interpolate=True)
dynamicSafeOC = visual.Rect(
    win=win, name='dynamicSafeOC',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1.0000], fillColor=[-0.0667,0.6392,1.0000],
    opacity=1, depth=-3.0, interpolate=True)
dynamicOCtext = visual.TextStim(win=win, name='dynamicOCtext',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
dynamicHideRisk = visual.Rect(
    win=win, name='dynamicHideRisk',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "realITI" ---
itiFix = visual.TextStim(win=win, name='itiFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "cgeRDMend" ---
cgeRDMendText = visual.TextStim(win=win, name='cgeRDMendText',
    text="You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cgeRDMendResp = keyboard.Keyboard()

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to Qualtrics.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=[-0.0667,0.6392,1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "SetUp" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SetUpComponents = []
for thisComponent in SetUpComponents:
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

# --- Run Routine "SetUp" ---
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
    for thisComponent in SetUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SetUp" ---
for thisComponent in SetUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from setupCode
# Getting random module
import random

# Define the shuffle function (equivalent to the JavaScript version)
def shuffle(array):
    currentIndex = len(array)
    while currentIndex != 0:
        randomIndex = random.randint(0, currentIndex - 1)
        currentIndex -= 1
        array[currentIndex], array[randomIndex] = array[randomIndex], array[currentIndex]

# Initialize ITIs
initITIstatic = [1, 1.5] * 25
initITIdynamic = [1, 1.5] * 60

# Shuffle the ITIs using the shuffle function
shuffle(initITIstatic)
shuffle(initITIdynamic)

# Save the ITIs as experiment data
thisExp.addData('initITIstatic', initITIstatic)
thisExp.addData('initITIdynamic', initITIdynamic)

# the Routine "SetUp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cgeRDMstart" ---
continueRoutine = True
# update component parameters for each repeat
CGErdmStartResp.keys = []
CGErdmStartResp.rt = []
_CGErdmStartResp_allKeys = []
# keep track of which components have finished
cgeRDMstartComponents = [CGErdmStartText, CGErdmStartResp]
for thisComponent in cgeRDMstartComponents:
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

# --- Run Routine "cgeRDMstart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CGErdmStartText* updates
    if CGErdmStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CGErdmStartText.frameNStart = frameN  # exact frame index
        CGErdmStartText.tStart = t  # local t and not account for scr refresh
        CGErdmStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CGErdmStartText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'CGErdmStartText.started')
        CGErdmStartText.setAutoDraw(True)
    
    # *CGErdmStartResp* updates
    waitOnFlip = False
    if CGErdmStartResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        CGErdmStartResp.frameNStart = frameN  # exact frame index
        CGErdmStartResp.tStart = t  # local t and not account for scr refresh
        CGErdmStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CGErdmStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'CGErdmStartResp.started')
        CGErdmStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(CGErdmStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(CGErdmStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if CGErdmStartResp.status == STARTED and not waitOnFlip:
        theseKeys = CGErdmStartResp.getKeys(keyList=["return"], waitRelease=False)
        _CGErdmStartResp_allKeys.extend(theseKeys)
        if len(_CGErdmStartResp_allKeys):
            CGErdmStartResp.keys = _CGErdmStartResp_allKeys[-1].name  # just the last key pressed
            CGErdmStartResp.rt = _CGErdmStartResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cgeRDMstartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cgeRDMstart" ---
for thisComponent in cgeRDMstartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if CGErdmStartResp.keys in ['', [], None]:  # No response was made
    CGErdmStartResp.keys = None
thisExp.addData('CGErdmStartResp.keys',CGErdmStartResp.keys)
if CGErdmStartResp.keys != None:  # we had a response
    thisExp.addData('CGErdmStartResp.rt', CGErdmStartResp.rt)
thisExp.nextEntry()
# the Routine "cgeRDMstart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pracStart" ---
continueRoutine = True
# update component parameters for each repeat
pracStartResp.keys = []
pracStartResp.rt = []
_pracStartResp_allKeys = []
# keep track of which components have finished
pracStartComponents = [pracStartText, pracStartResp]
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
    
    # *pracStartText* updates
    if pracStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracStartText.frameNStart = frameN  # exact frame index
        pracStartText.tStart = t  # local t and not account for scr refresh
        pracStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracStartText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pracStartText.started')
        pracStartText.setAutoDraw(True)
    
    # *pracStartResp* updates
    waitOnFlip = False
    if pracStartResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        pracStartResp.frameNStart = frameN  # exact frame index
        pracStartResp.tStart = t  # local t and not account for scr refresh
        pracStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pracStartResp.started')
        pracStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(pracStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(pracStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pracStartResp.status == STARTED and not waitOnFlip:
        theseKeys = pracStartResp.getKeys(keyList=['v','n'], waitRelease=False)
        _pracStartResp_allKeys.extend(theseKeys)
        if len(_pracStartResp_allKeys):
            pracStartResp.keys = _pracStartResp_allKeys[-1].name  # just the last key pressed
            pracStartResp.rt = _pracStartResp_allKeys[-1].rt
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
if pracStartResp.keys in ['', [], None]:  # No response was made
    pracStartResp.keys = None
thisExp.addData('pracStartResp.keys',pracStartResp.keys)
if pracStartResp.keys != None:  # we had a response
    thisExp.addData('pracStartResp.rt', pracStartResp.rt)
thisExp.nextEntry()
# the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracTrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgtRDMPractice.xlsx', selection='0:4'),
    seed=None, name='pracTrials')
thisExp.addLoop(pracTrials)  # add the loop to the experiment
thisPracTrial = pracTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
if thisPracTrial != None:
    for paramName in thisPracTrial:
        exec('{} = thisPracTrial[paramName]'.format(paramName))

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial:
            exec('{} = thisPracTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pracChoice" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracChoiceRandLoc
    ### Randomized Practice Trial Locations
    if loc==1:
        riskLineLoc=[-.35,0] #targetPos
    else:
        riskLineLoc=[.35,0] #targetPos
    
    if loc==1:
        lossLoc=[-.35,-.1]
        gainLoc=[-.35,.1]
        safeLoc=[.35,0]
    else:
        lossLoc=[.35,-.1]
        gainLoc=[.35,.1]
        safeLoc=[-.35,0]
        
    # Rounding Presentation of Monetary Values    
    pracLossRounded = '$%.0f' % round(riskyLoss,0)
    pracGainRounded = '$%.2f' % round(riskyGain,2)
    pracSafeRounded = '$%.2f' % round(alternative,2)
    pracCircRight.setFillColor(color2)
    pracCircRight.setLineColor(color2)
    pracRiskLine.setPos(riskLineLoc)
    pracLossText.setPos(lossLoc)
    pracLossText.setText(pracLossRounded

)
    pracGainText.setPos(gainLoc)
    pracGainText.setText(pracGainRounded)
    pracSafeText.setPos(safeLoc)
    pracSafeText.setText(pracSafeRounded)
    pracChoiceResp.keys = []
    pracChoiceResp.rt = []
    _pracChoiceResp_allKeys = []
    # keep track of which components have finished
    pracChoiceComponents = [pracCircLeft, pracCircRight, pracRiskLine, pracORtext, pracLossText, pracGainText, pracSafeText, pracVleft, pracNright, pracChoiceResp]
    for thisComponent in pracChoiceComponents:
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
    
    # --- Run Routine "pracChoice" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracCircLeft* updates
        if pracCircLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pracCircLeft.frameNStart = frameN  # exact frame index
            pracCircLeft.tStart = t  # local t and not account for scr refresh
            pracCircLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracCircLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracCircLeft.started')
            pracCircLeft.setAutoDraw(True)
        if pracCircLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracCircLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracCircLeft.tStop = t  # not accounting for scr refresh
                pracCircLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracCircLeft.stopped')
                pracCircLeft.setAutoDraw(False)
        
        # *pracCircRight* updates
        if pracCircRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracCircRight.frameNStart = frameN  # exact frame index
            pracCircRight.tStart = t  # local t and not account for scr refresh
            pracCircRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracCircRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracCircRight.started')
            pracCircRight.setAutoDraw(True)
        if pracCircRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracCircRight.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracCircRight.tStop = t  # not accounting for scr refresh
                pracCircRight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracCircRight.stopped')
                pracCircRight.setAutoDraw(False)
        
        # *pracRiskLine* updates
        if pracRiskLine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracRiskLine.frameNStart = frameN  # exact frame index
            pracRiskLine.tStart = t  # local t and not account for scr refresh
            pracRiskLine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracRiskLine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracRiskLine.started')
            pracRiskLine.setAutoDraw(True)
        if pracRiskLine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracRiskLine.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracRiskLine.tStop = t  # not accounting for scr refresh
                pracRiskLine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracRiskLine.stopped')
                pracRiskLine.setAutoDraw(False)
        
        # *pracORtext* updates
        if pracORtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracORtext.frameNStart = frameN  # exact frame index
            pracORtext.tStart = t  # local t and not account for scr refresh
            pracORtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracORtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracORtext.started')
            pracORtext.setAutoDraw(True)
        if pracORtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracORtext.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracORtext.tStop = t  # not accounting for scr refresh
                pracORtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracORtext.stopped')
                pracORtext.setAutoDraw(False)
        
        # *pracLossText* updates
        if pracLossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracLossText.frameNStart = frameN  # exact frame index
            pracLossText.tStart = t  # local t and not account for scr refresh
            pracLossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracLossText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracLossText.started')
            pracLossText.setAutoDraw(True)
        if pracLossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracLossText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracLossText.tStop = t  # not accounting for scr refresh
                pracLossText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracLossText.stopped')
                pracLossText.setAutoDraw(False)
        
        # *pracGainText* updates
        if pracGainText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracGainText.frameNStart = frameN  # exact frame index
            pracGainText.tStart = t  # local t and not account for scr refresh
            pracGainText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracGainText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracGainText.started')
            pracGainText.setAutoDraw(True)
        if pracGainText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracGainText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracGainText.tStop = t  # not accounting for scr refresh
                pracGainText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracGainText.stopped')
                pracGainText.setAutoDraw(False)
        
        # *pracSafeText* updates
        if pracSafeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracSafeText.frameNStart = frameN  # exact frame index
            pracSafeText.tStart = t  # local t and not account for scr refresh
            pracSafeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracSafeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracSafeText.started')
            pracSafeText.setAutoDraw(True)
        if pracSafeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracSafeText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracSafeText.tStop = t  # not accounting for scr refresh
                pracSafeText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracSafeText.stopped')
                pracSafeText.setAutoDraw(False)
        
        # *pracVleft* updates
        if pracVleft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pracVleft.frameNStart = frameN  # exact frame index
            pracVleft.tStart = t  # local t and not account for scr refresh
            pracVleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracVleft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracVleft.started')
            pracVleft.setAutoDraw(True)
        if pracVleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracVleft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracVleft.tStop = t  # not accounting for scr refresh
                pracVleft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracVleft.stopped')
                pracVleft.setAutoDraw(False)
        
        # *pracNright* updates
        if pracNright.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pracNright.frameNStart = frameN  # exact frame index
            pracNright.tStart = t  # local t and not account for scr refresh
            pracNright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracNright, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracNright.started')
            pracNright.setAutoDraw(True)
        if pracNright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracNright.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracNright.tStop = t  # not accounting for scr refresh
                pracNright.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracNright.stopped')
                pracNright.setAutoDraw(False)
        
        # *pracChoiceResp* updates
        waitOnFlip = False
        if pracChoiceResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pracChoiceResp.frameNStart = frameN  # exact frame index
            pracChoiceResp.tStart = t  # local t and not account for scr refresh
            pracChoiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracChoiceResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracChoiceResp.started')
            pracChoiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracChoiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracChoiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracChoiceResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracChoiceResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracChoiceResp.tStop = t  # not accounting for scr refresh
                pracChoiceResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracChoiceResp.stopped')
                pracChoiceResp.status = FINISHED
        if pracChoiceResp.status == STARTED and not waitOnFlip:
            theseKeys = pracChoiceResp.getKeys(keyList=['v','n'], waitRelease=False)
            _pracChoiceResp_allKeys.extend(theseKeys)
            if len(_pracChoiceResp_allKeys):
                pracChoiceResp.keys = _pracChoiceResp_allKeys[-1].name  # just the last key pressed
                pracChoiceResp.rt = _pracChoiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracChoice" ---
    for thisComponent in pracChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracChoiceResp.keys in ['', [], None]:  # No response was made
        pracChoiceResp.keys = None
    pracTrials.addData('pracChoiceResp.keys',pracChoiceResp.keys)
    if pracChoiceResp.keys != None:  # we had a response
        pracTrials.addData('pracChoiceResp.rt', pracChoiceResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "pracISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    pracISIComponents = [isiPracFix]
    for thisComponent in pracISIComponents:
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
    
    # --- Run Routine "pracISI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiPracFix* updates
        if isiPracFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiPracFix.frameNStart = frameN  # exact frame index
            isiPracFix.tStart = t  # local t and not account for scr refresh
            isiPracFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiPracFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiPracFix.started')
            isiPracFix.setAutoDraw(True)
        if isiPracFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiPracFix.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiPracFix.tStop = t  # not accounting for scr refresh
                isiPracFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiPracFix.stopped')
                isiPracFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracISI" ---
    for thisComponent in pracISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pracISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pracOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracOCcode
    import random
    import math
    if not pracChoiceResp.keys:
        outcome = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif pracChoiceResp.keys == 'v' and loc == 1:
        outcome = random.choice([riskyGain, riskyLoss])
        extraITI = 4-pracChoiceResp.rt
        if outcome == riskyGain:
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.15] #.125
        elif outcome == riskyLoss:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.15]
             noRespLoc = [5,5]
    elif pracChoiceResp.keys == 'v' and loc == 2:
        extraITI = 4-pracChoiceResp.rt
        outcome = alternative
        ocLoc = [-.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif pracChoiceResp.keys == 'n' and loc ==1:
        extraITI = 4-pracChoiceResp.rt
        outcome = alternative
        ocLoc = [.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif pracChoiceResp.keys == 'n' and loc ==2:
        outcome = random.choice([riskyGain, riskyLoss])
        extraITI = 4-pracChoiceResp.rt
        if outcome == riskyGain:
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.15]
            noRespLoc = [5,5]
        elif outcome == riskyLoss:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.15]
            noRespLoc = [5,5]
    
    if outcome == riskyLoss:
        pracFeedbackRounded = "$%.0f" % round(outcome,0)
    else:
        pracFeedbackRounded = "$%.2f" % round(outcome,2)
    pracNoRespText.setPos(noRespLoc)
    pracRiskOC.setPos(ocGambleLoc)
    pracSafeOC.setPos(ocSafeLoc)
    pracOCtext.setColor(color1, colorSpace='rgb')
    pracOCtext.setPos(ocLoc)
    pracOCtext.setText(pracFeedbackRounded)
    pracHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    pracOutcomeComponents = [pracNoRespText, pracRiskOC, pracSafeOC, pracOCtext, pracHideRisk]
    for thisComponent in pracOutcomeComponents:
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
    
    # --- Run Routine "pracOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracNoRespText* updates
        if pracNoRespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracNoRespText.frameNStart = frameN  # exact frame index
            pracNoRespText.tStart = t  # local t and not account for scr refresh
            pracNoRespText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracNoRespText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracNoRespText.started')
            pracNoRespText.setAutoDraw(True)
        if pracNoRespText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracNoRespText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracNoRespText.tStop = t  # not accounting for scr refresh
                pracNoRespText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracNoRespText.stopped')
                pracNoRespText.setAutoDraw(False)
        
        # *pracRiskOC* updates
        if pracRiskOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracRiskOC.frameNStart = frameN  # exact frame index
            pracRiskOC.tStart = t  # local t and not account for scr refresh
            pracRiskOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracRiskOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracRiskOC.started')
            pracRiskOC.setAutoDraw(True)
        if pracRiskOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracRiskOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracRiskOC.tStop = t  # not accounting for scr refresh
                pracRiskOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracRiskOC.stopped')
                pracRiskOC.setAutoDraw(False)
        
        # *pracSafeOC* updates
        if pracSafeOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracSafeOC.frameNStart = frameN  # exact frame index
            pracSafeOC.tStart = t  # local t and not account for scr refresh
            pracSafeOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracSafeOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracSafeOC.started')
            pracSafeOC.setAutoDraw(True)
        if pracSafeOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracSafeOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracSafeOC.tStop = t  # not accounting for scr refresh
                pracSafeOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracSafeOC.stopped')
                pracSafeOC.setAutoDraw(False)
        
        # *pracOCtext* updates
        if pracOCtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOCtext.frameNStart = frameN  # exact frame index
            pracOCtext.tStart = t  # local t and not account for scr refresh
            pracOCtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOCtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracOCtext.started')
            pracOCtext.setAutoDraw(True)
        if pracOCtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracOCtext.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracOCtext.tStop = t  # not accounting for scr refresh
                pracOCtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracOCtext.stopped')
                pracOCtext.setAutoDraw(False)
        
        # *pracHideRisk* updates
        if pracHideRisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracHideRisk.frameNStart = frameN  # exact frame index
            pracHideRisk.tStart = t  # local t and not account for scr refresh
            pracHideRisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracHideRisk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracHideRisk.started')
            pracHideRisk.setAutoDraw(True)
        if pracHideRisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracHideRisk.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracHideRisk.tStop = t  # not accounting for scr refresh
                pracHideRisk.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracHideRisk.stopped')
                pracHideRisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracOutcome" ---
    for thisComponent in pracOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from pracOCcode
    thisExp.addData('outcome', outcome)
    
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "pracITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    pracITIComponents = [itiPracFix]
    for thisComponent in pracITIComponents:
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
    
    # --- Run Routine "pracITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiPracFix* updates
        if itiPracFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiPracFix.frameNStart = frameN  # exact frame index
            itiPracFix.tStart = t  # local t and not account for scr refresh
            itiPracFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiPracFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiPracFix.started')
            itiPracFix.setAutoDraw(True)
        if itiPracFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiPracFix.tStartRefresh + iti + extraITI-frameTolerance:
                # keep track of stop time/frame for later
                itiPracFix.tStop = t  # not accounting for scr refresh
                itiPracFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiPracFix.stopped')
                itiPracFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracITI" ---
    for thisComponent in pracITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pracITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pracTrials'


# --- Prepare to start Routine "staticStart" ---
continueRoutine = True
# update component parameters for each repeat
staticStartResp.keys = []
staticStartResp.rt = []
_staticStartResp_allKeys = []
# keep track of which components have finished
staticStartComponents = [staticStartText, staticStartResp]
for thisComponent in staticStartComponents:
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

# --- Run Routine "staticStart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *staticStartText* updates
    if staticStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        staticStartText.frameNStart = frameN  # exact frame index
        staticStartText.tStart = t  # local t and not account for scr refresh
        staticStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(staticStartText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'staticStartText.started')
        staticStartText.setAutoDraw(True)
    
    # *staticStartResp* updates
    waitOnFlip = False
    if staticStartResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        staticStartResp.frameNStart = frameN  # exact frame index
        staticStartResp.tStart = t  # local t and not account for scr refresh
        staticStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(staticStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'staticStartResp.started')
        staticStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(staticStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(staticStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if staticStartResp.status == STARTED and not waitOnFlip:
        theseKeys = staticStartResp.getKeys(keyList=['v','n'], waitRelease=False)
        _staticStartResp_allKeys.extend(theseKeys)
        if len(_staticStartResp_allKeys):
            staticStartResp.keys = _staticStartResp_allKeys[-1].name  # just the last key pressed
            staticStartResp.rt = _staticStartResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in staticStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "staticStart" ---
for thisComponent in staticStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if staticStartResp.keys in ['', [], None]:  # No response was made
    staticStartResp.keys = None
thisExp.addData('staticStartResp.keys',staticStartResp.keys)
if staticStartResp.keys != None:  # we had a response
    thisExp.addData('staticStartResp.rt', staticStartResp.rt)
thisExp.nextEntry()
# the Routine "staticStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
staticTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CGT-choice-set.csv', selection='0:2'),
    seed=None, name='staticTrials')
thisExp.addLoop(staticTrials)  # add the loop to the experiment
thisStaticTrial = staticTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStaticTrial.rgb)
if thisStaticTrial != None:
    for paramName in thisStaticTrial:
        exec('{} = thisStaticTrial[paramName]'.format(paramName))

for thisStaticTrial in staticTrials:
    currentLoop = staticTrials
    # abbreviate parameter names if possible (e.g. rgb = thisStaticTrial.rgb)
    if thisStaticTrial != None:
        for paramName in thisStaticTrial:
            exec('{} = thisStaticTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "realChoice" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from realChoiceRandLoc
    import random
    
    loc = random.choice([1,2])
    
    if loc==1:
        riskLineLoc=[-.35,0]
    else:
        riskLineLoc=[.35,0]
    
    if loc==1:
        lossLoc=[-.35,-.1]
        gainLoc=[-.35,.1]
        safeLoc=[.35,0]
    else:
        lossLoc=[.35,-.1]
        gainLoc=[.35,.1]
        safeLoc=[-.35,0]
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    realCircRight.setFillColor([-0.0667,0.6392,1.0000])
    realCircRight.setLineColor([-0.0667,0.6392,1.0000])
    realRiskLine.setPos(riskLineLoc)
    realLossText.setPos(lossLoc)
    realLossText.setText(lossRounded)
    realGainText.setPos(gainLoc)
    realGainText.setText(gainRounded)
    realSafeText.setPos(safeLoc)
    realSafeText.setText(safeRounded)
    realChoiceResp.keys = []
    realChoiceResp.rt = []
    _realChoiceResp_allKeys = []
    # keep track of which components have finished
    realChoiceComponents = [realCircLeft, realCircRight, realRiskLine, realORtext, realLossText, realGainText, realSafeText, realVleft, realNright, realChoiceResp]
    for thisComponent in realChoiceComponents:
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
    
    # --- Run Routine "realChoice" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *realCircLeft* updates
        if realCircLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realCircLeft.frameNStart = frameN  # exact frame index
            realCircLeft.tStart = t  # local t and not account for scr refresh
            realCircLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realCircLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realCircLeft.started')
            realCircLeft.setAutoDraw(True)
        if realCircLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realCircLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realCircLeft.tStop = t  # not accounting for scr refresh
                realCircLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realCircLeft.stopped')
                realCircLeft.setAutoDraw(False)
        
        # *realCircRight* updates
        if realCircRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realCircRight.frameNStart = frameN  # exact frame index
            realCircRight.tStart = t  # local t and not account for scr refresh
            realCircRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realCircRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realCircRight.started')
            realCircRight.setAutoDraw(True)
        if realCircRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realCircRight.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realCircRight.tStop = t  # not accounting for scr refresh
                realCircRight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realCircRight.stopped')
                realCircRight.setAutoDraw(False)
        
        # *realRiskLine* updates
        if realRiskLine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realRiskLine.frameNStart = frameN  # exact frame index
            realRiskLine.tStart = t  # local t and not account for scr refresh
            realRiskLine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realRiskLine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realRiskLine.started')
            realRiskLine.setAutoDraw(True)
        if realRiskLine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realRiskLine.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realRiskLine.tStop = t  # not accounting for scr refresh
                realRiskLine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realRiskLine.stopped')
                realRiskLine.setAutoDraw(False)
        
        # *realORtext* updates
        if realORtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realORtext.frameNStart = frameN  # exact frame index
            realORtext.tStart = t  # local t and not account for scr refresh
            realORtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realORtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realORtext.started')
            realORtext.setAutoDraw(True)
        if realORtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realORtext.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realORtext.tStop = t  # not accounting for scr refresh
                realORtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realORtext.stopped')
                realORtext.setAutoDraw(False)
        
        # *realLossText* updates
        if realLossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realLossText.frameNStart = frameN  # exact frame index
            realLossText.tStart = t  # local t and not account for scr refresh
            realLossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realLossText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realLossText.started')
            realLossText.setAutoDraw(True)
        if realLossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realLossText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realLossText.tStop = t  # not accounting for scr refresh
                realLossText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realLossText.stopped')
                realLossText.setAutoDraw(False)
        
        # *realGainText* updates
        if realGainText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realGainText.frameNStart = frameN  # exact frame index
            realGainText.tStart = t  # local t and not account for scr refresh
            realGainText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realGainText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realGainText.started')
            realGainText.setAutoDraw(True)
        if realGainText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realGainText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realGainText.tStop = t  # not accounting for scr refresh
                realGainText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realGainText.stopped')
                realGainText.setAutoDraw(False)
        
        # *realSafeText* updates
        if realSafeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realSafeText.frameNStart = frameN  # exact frame index
            realSafeText.tStart = t  # local t and not account for scr refresh
            realSafeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realSafeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realSafeText.started')
            realSafeText.setAutoDraw(True)
        if realSafeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realSafeText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realSafeText.tStop = t  # not accounting for scr refresh
                realSafeText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realSafeText.stopped')
                realSafeText.setAutoDraw(False)
        
        # *realVleft* updates
        if realVleft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realVleft.frameNStart = frameN  # exact frame index
            realVleft.tStart = t  # local t and not account for scr refresh
            realVleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realVleft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realVleft.started')
            realVleft.setAutoDraw(True)
        if realVleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realVleft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realVleft.tStop = t  # not accounting for scr refresh
                realVleft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realVleft.stopped')
                realVleft.setAutoDraw(False)
        
        # *realNright* updates
        if realNright.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realNright.frameNStart = frameN  # exact frame index
            realNright.tStart = t  # local t and not account for scr refresh
            realNright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realNright, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realNright.started')
            realNright.setAutoDraw(True)
        if realNright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realNright.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realNright.tStop = t  # not accounting for scr refresh
                realNright.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realNright.stopped')
                realNright.setAutoDraw(False)
        
        # *realChoiceResp* updates
        waitOnFlip = False
        if realChoiceResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realChoiceResp.frameNStart = frameN  # exact frame index
            realChoiceResp.tStart = t  # local t and not account for scr refresh
            realChoiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realChoiceResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realChoiceResp.started')
            realChoiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(realChoiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(realChoiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if realChoiceResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realChoiceResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realChoiceResp.tStop = t  # not accounting for scr refresh
                realChoiceResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realChoiceResp.stopped')
                realChoiceResp.status = FINISHED
        if realChoiceResp.status == STARTED and not waitOnFlip:
            theseKeys = realChoiceResp.getKeys(keyList=['v','n'], waitRelease=False)
            _realChoiceResp_allKeys.extend(theseKeys)
            if len(_realChoiceResp_allKeys):
                realChoiceResp.keys = _realChoiceResp_allKeys[-1].name  # just the last key pressed
                realChoiceResp.rt = _realChoiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realChoice" ---
    for thisComponent in realChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from realChoiceRandLoc
    thisExp.addData("loc", loc)
    # check responses
    if realChoiceResp.keys in ['', [], None]:  # No response was made
        realChoiceResp.keys = None
    staticTrials.addData('realChoiceResp.keys',realChoiceResp.keys)
    if realChoiceResp.keys != None:  # we had a response
        staticTrials.addData('realChoiceResp.rt', realChoiceResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "realISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    realISIComponents = [isiFix]
    for thisComponent in realISIComponents:
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
    
    # --- Run Routine "realISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiFix* updates
        if isiFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiFix.frameNStart = frameN  # exact frame index
            isiFix.tStart = t  # local t and not account for scr refresh
            isiFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiFix.started')
            isiFix.setAutoDraw(True)
        if isiFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiFix.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                isiFix.tStop = t  # not accounting for scr refresh
                isiFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiFix.stopped')
                isiFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realISI" ---
    for thisComponent in realISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "staticOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from staticOCcode
    import random
    import math
    if not realChoiceResp.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        riskyLossReal = math.nan
        riskyGainReal = math.nan
        certain = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoiceResp.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        if outcometmp == riskyoption1:
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.15]
        elif outcometmp == riskyoption2:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.15]
             noRespLoc = [5,5]
    elif realChoiceResp.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        ocLoc = [-.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoiceResp.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        ocLoc = [.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoiceResp.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        if outcometmp == riskyoption1:
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.15]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.15]
            noRespLoc = [5,5]
    
    actualITI = initITIstatic[staticTrials.thisN] + extraITI
    
    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLossReal)
    riskygain_values.append(riskyGainReal)
    certain_values.append(certain)
    staticNoRespText.setPos(noRespLoc)
    staticRiskOC.setPos(ocGambleLoc)
    staticSafeOC.setPos(ocSafeLoc)
    staticOCtext.setColor([0.5216,0.5216,0.5216], colorSpace='rgb')
    staticOCtext.setPos(ocLoc)
    staticOCtext.setText(feedbackRounded)
    staticHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    staticOutcomeComponents = [staticNoRespText, staticRiskOC, staticSafeOC, staticOCtext, staticHideRisk]
    for thisComponent in staticOutcomeComponents:
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
    
    # --- Run Routine "staticOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *staticNoRespText* updates
        if staticNoRespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            staticNoRespText.frameNStart = frameN  # exact frame index
            staticNoRespText.tStart = t  # local t and not account for scr refresh
            staticNoRespText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(staticNoRespText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'staticNoRespText.started')
            staticNoRespText.setAutoDraw(True)
        if staticNoRespText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > staticNoRespText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                staticNoRespText.tStop = t  # not accounting for scr refresh
                staticNoRespText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'staticNoRespText.stopped')
                staticNoRespText.setAutoDraw(False)
        
        # *staticRiskOC* updates
        if staticRiskOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            staticRiskOC.frameNStart = frameN  # exact frame index
            staticRiskOC.tStart = t  # local t and not account for scr refresh
            staticRiskOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(staticRiskOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'staticRiskOC.started')
            staticRiskOC.setAutoDraw(True)
        if staticRiskOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > staticRiskOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                staticRiskOC.tStop = t  # not accounting for scr refresh
                staticRiskOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'staticRiskOC.stopped')
                staticRiskOC.setAutoDraw(False)
        
        # *staticSafeOC* updates
        if staticSafeOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            staticSafeOC.frameNStart = frameN  # exact frame index
            staticSafeOC.tStart = t  # local t and not account for scr refresh
            staticSafeOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(staticSafeOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'staticSafeOC.started')
            staticSafeOC.setAutoDraw(True)
        if staticSafeOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > staticSafeOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                staticSafeOC.tStop = t  # not accounting for scr refresh
                staticSafeOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'staticSafeOC.stopped')
                staticSafeOC.setAutoDraw(False)
        
        # *staticOCtext* updates
        if staticOCtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            staticOCtext.frameNStart = frameN  # exact frame index
            staticOCtext.tStart = t  # local t and not account for scr refresh
            staticOCtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(staticOCtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'staticOCtext.started')
            staticOCtext.setAutoDraw(True)
        if staticOCtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > staticOCtext.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                staticOCtext.tStop = t  # not accounting for scr refresh
                staticOCtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'staticOCtext.stopped')
                staticOCtext.setAutoDraw(False)
        
        # *staticHideRisk* updates
        if staticHideRisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            staticHideRisk.frameNStart = frameN  # exact frame index
            staticHideRisk.tStart = t  # local t and not account for scr refresh
            staticHideRisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(staticHideRisk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'staticHideRisk.started')
            staticHideRisk.setAutoDraw(True)
        if staticHideRisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > staticHideRisk.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                staticHideRisk.tStop = t  # not accounting for scr refresh
                staticHideRisk.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'staticHideRisk.stopped')
                staticHideRisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in staticOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "staticOutcome" ---
    for thisComponent in staticOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from staticOCcode
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "realITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    realITIComponents = [itiFix]
    for thisComponent in realITIComponents:
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
    
    # --- Run Routine "realITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiFix* updates
        if itiFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiFix.frameNStart = frameN  # exact frame index
            itiFix.tStart = t  # local t and not account for scr refresh
            itiFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiFix.started')
            itiFix.setAutoDraw(True)
        if itiFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiFix.tStartRefresh + actualITI-frameTolerance:
                # keep track of stop time/frame for later
                itiFix.tStop = t  # not accounting for scr refresh
                itiFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiFix.stopped')
                itiFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realITI" ---
    for thisComponent in realITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "realITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'staticTrials'


# set up handler to look after randomisation of conditions etc
BestFit = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='BestFit')
thisExp.addLoop(BestFit)  # add the loop to the experiment
thisBestFit = BestFit.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBestFit.rgb)
if thisBestFit != None:
    for paramName in thisBestFit:
        exec('{} = thisBestFit[paramName]'.format(paramName))

for thisBestFit in BestFit:
    currentLoop = BestFit
    # abbreviate parameter names if possible (e.g. rgb = thisBestFit.rgb)
    if thisBestFit != None:
        for paramName in thisBestFit:
            exec('{} = thisBestFit[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "computeBestFit" ---
    continueRoutine = True
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
    
    fname.append("../CGE/bespoke_choicesets/bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM))
    dynamicChoiceSetFilename = fname[0]
    dynamicChoiceSet = fname[0]  # Set routine start values for dynamicChoiceSet
    thisExp.addData('dynamicChoiceSet.routineStartVal', dynamicChoiceSet)  # Save exp start value
    bestRho = bestR  # Set routine start values for bestRho
    bestMu = bestM  # Set routine start values for bestMu
    # keep track of which components have finished
    computeBestFitComponents = [setupBestFit]
    for thisComponent in computeBestFitComponents:
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
    
    # --- Run Routine "computeBestFit" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *setupBestFit* updates
        if setupBestFit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            setupBestFit.frameNStart = frameN  # exact frame index
            setupBestFit.tStart = t  # local t and not account for scr refresh
            setupBestFit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(setupBestFit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'setupBestFit.started')
            setupBestFit.setAutoDraw(True)
        if setupBestFit.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > setupBestFit.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                setupBestFit.tStop = t  # not accounting for scr refresh
                setupBestFit.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'setupBestFit.stopped')
                setupBestFit.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in computeBestFitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "computeBestFit" ---
    for thisComponent in computeBestFitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('dynamicChoiceSet.routineEndVal', dynamicChoiceSet)  # Save end routine value
    thisExp.addData('bestRho.routineEndVal', bestRho)  # Save end routine value
    thisExp.addData('bestMu.routineEndVal', bestMu)  # Save end routine value
    # the Routine "computeBestFit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'BestFit'


# --- Prepare to start Routine "loadingDynamicChoices" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
loadingDynamicChoicesComponents = [text]
for thisComponent in loadingDynamicChoicesComponents:
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

# --- Run Routine "loadingDynamicChoices" ---
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
        if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loadingDynamicChoicesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "loadingDynamicChoices" ---
for thisComponent in loadingDynamicChoicesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "dynamicStart" ---
continueRoutine = True
# update component parameters for each repeat
dynamicStartResp.keys = []
dynamicStartResp.rt = []
_dynamicStartResp_allKeys = []
# keep track of which components have finished
dynamicStartComponents = [dynamicStartText, dynamicStartResp]
for thisComponent in dynamicStartComponents:
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

# --- Run Routine "dynamicStart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *dynamicStartText* updates
    if dynamicStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dynamicStartText.frameNStart = frameN  # exact frame index
        dynamicStartText.tStart = t  # local t and not account for scr refresh
        dynamicStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dynamicStartText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dynamicStartText.started')
        dynamicStartText.setAutoDraw(True)
    
    # *dynamicStartResp* updates
    waitOnFlip = False
    if dynamicStartResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dynamicStartResp.frameNStart = frameN  # exact frame index
        dynamicStartResp.tStart = t  # local t and not account for scr refresh
        dynamicStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dynamicStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dynamicStartResp.started')
        dynamicStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(dynamicStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(dynamicStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if dynamicStartResp.status == STARTED and not waitOnFlip:
        theseKeys = dynamicStartResp.getKeys(keyList=['v', 'n'], waitRelease=False)
        _dynamicStartResp_allKeys.extend(theseKeys)
        if len(_dynamicStartResp_allKeys):
            dynamicStartResp.keys = _dynamicStartResp_allKeys[-1].name  # just the last key pressed
            dynamicStartResp.rt = _dynamicStartResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dynamicStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "dynamicStart" ---
for thisComponent in dynamicStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if dynamicStartResp.keys in ['', [], None]:  # No response was made
    dynamicStartResp.keys = None
thisExp.addData('dynamicStartResp.keys',dynamicStartResp.keys)
if dynamicStartResp.keys != None:  # we had a response
    thisExp.addData('dynamicStartResp.rt', dynamicStartResp.rt)
thisExp.nextEntry()
# the Routine "dynamicStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
dynamicTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(fname[0], selection='0:2'),
    seed=None, name='dynamicTrials')
thisExp.addLoop(dynamicTrials)  # add the loop to the experiment
thisDynamicTrial = dynamicTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDynamicTrial.rgb)
if thisDynamicTrial != None:
    for paramName in thisDynamicTrial:
        exec('{} = thisDynamicTrial[paramName]'.format(paramName))

for thisDynamicTrial in dynamicTrials:
    currentLoop = dynamicTrials
    # abbreviate parameter names if possible (e.g. rgb = thisDynamicTrial.rgb)
    if thisDynamicTrial != None:
        for paramName in thisDynamicTrial:
            exec('{} = thisDynamicTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "realChoice" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from realChoiceRandLoc
    import random
    
    loc = random.choice([1,2])
    
    if loc==1:
        riskLineLoc=[-.35,0]
    else:
        riskLineLoc=[.35,0]
    
    if loc==1:
        lossLoc=[-.35,-.1]
        gainLoc=[-.35,.1]
        safeLoc=[.35,0]
    else:
        lossLoc=[.35,-.1]
        gainLoc=[.35,.1]
        safeLoc=[-.35,0]
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    realCircRight.setFillColor([-0.0667,0.6392,1.0000])
    realCircRight.setLineColor([-0.0667,0.6392,1.0000])
    realRiskLine.setPos(riskLineLoc)
    realLossText.setPos(lossLoc)
    realLossText.setText(lossRounded)
    realGainText.setPos(gainLoc)
    realGainText.setText(gainRounded)
    realSafeText.setPos(safeLoc)
    realSafeText.setText(safeRounded)
    realChoiceResp.keys = []
    realChoiceResp.rt = []
    _realChoiceResp_allKeys = []
    # keep track of which components have finished
    realChoiceComponents = [realCircLeft, realCircRight, realRiskLine, realORtext, realLossText, realGainText, realSafeText, realVleft, realNright, realChoiceResp]
    for thisComponent in realChoiceComponents:
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
    
    # --- Run Routine "realChoice" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *realCircLeft* updates
        if realCircLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realCircLeft.frameNStart = frameN  # exact frame index
            realCircLeft.tStart = t  # local t and not account for scr refresh
            realCircLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realCircLeft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realCircLeft.started')
            realCircLeft.setAutoDraw(True)
        if realCircLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realCircLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realCircLeft.tStop = t  # not accounting for scr refresh
                realCircLeft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realCircLeft.stopped')
                realCircLeft.setAutoDraw(False)
        
        # *realCircRight* updates
        if realCircRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realCircRight.frameNStart = frameN  # exact frame index
            realCircRight.tStart = t  # local t and not account for scr refresh
            realCircRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realCircRight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realCircRight.started')
            realCircRight.setAutoDraw(True)
        if realCircRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realCircRight.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realCircRight.tStop = t  # not accounting for scr refresh
                realCircRight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realCircRight.stopped')
                realCircRight.setAutoDraw(False)
        
        # *realRiskLine* updates
        if realRiskLine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realRiskLine.frameNStart = frameN  # exact frame index
            realRiskLine.tStart = t  # local t and not account for scr refresh
            realRiskLine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realRiskLine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realRiskLine.started')
            realRiskLine.setAutoDraw(True)
        if realRiskLine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realRiskLine.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realRiskLine.tStop = t  # not accounting for scr refresh
                realRiskLine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realRiskLine.stopped')
                realRiskLine.setAutoDraw(False)
        
        # *realORtext* updates
        if realORtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realORtext.frameNStart = frameN  # exact frame index
            realORtext.tStart = t  # local t and not account for scr refresh
            realORtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realORtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realORtext.started')
            realORtext.setAutoDraw(True)
        if realORtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realORtext.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realORtext.tStop = t  # not accounting for scr refresh
                realORtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realORtext.stopped')
                realORtext.setAutoDraw(False)
        
        # *realLossText* updates
        if realLossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realLossText.frameNStart = frameN  # exact frame index
            realLossText.tStart = t  # local t and not account for scr refresh
            realLossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realLossText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realLossText.started')
            realLossText.setAutoDraw(True)
        if realLossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realLossText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realLossText.tStop = t  # not accounting for scr refresh
                realLossText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realLossText.stopped')
                realLossText.setAutoDraw(False)
        
        # *realGainText* updates
        if realGainText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realGainText.frameNStart = frameN  # exact frame index
            realGainText.tStart = t  # local t and not account for scr refresh
            realGainText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realGainText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realGainText.started')
            realGainText.setAutoDraw(True)
        if realGainText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realGainText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realGainText.tStop = t  # not accounting for scr refresh
                realGainText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realGainText.stopped')
                realGainText.setAutoDraw(False)
        
        # *realSafeText* updates
        if realSafeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realSafeText.frameNStart = frameN  # exact frame index
            realSafeText.tStart = t  # local t and not account for scr refresh
            realSafeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realSafeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realSafeText.started')
            realSafeText.setAutoDraw(True)
        if realSafeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realSafeText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realSafeText.tStop = t  # not accounting for scr refresh
                realSafeText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realSafeText.stopped')
                realSafeText.setAutoDraw(False)
        
        # *realVleft* updates
        if realVleft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realVleft.frameNStart = frameN  # exact frame index
            realVleft.tStart = t  # local t and not account for scr refresh
            realVleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realVleft, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realVleft.started')
            realVleft.setAutoDraw(True)
        if realVleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realVleft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realVleft.tStop = t  # not accounting for scr refresh
                realVleft.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realVleft.stopped')
                realVleft.setAutoDraw(False)
        
        # *realNright* updates
        if realNright.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realNright.frameNStart = frameN  # exact frame index
            realNright.tStart = t  # local t and not account for scr refresh
            realNright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realNright, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realNright.started')
            realNright.setAutoDraw(True)
        if realNright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realNright.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realNright.tStop = t  # not accounting for scr refresh
                realNright.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realNright.stopped')
                realNright.setAutoDraw(False)
        
        # *realChoiceResp* updates
        waitOnFlip = False
        if realChoiceResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            realChoiceResp.frameNStart = frameN  # exact frame index
            realChoiceResp.tStart = t  # local t and not account for scr refresh
            realChoiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realChoiceResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realChoiceResp.started')
            realChoiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(realChoiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(realChoiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if realChoiceResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realChoiceResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realChoiceResp.tStop = t  # not accounting for scr refresh
                realChoiceResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realChoiceResp.stopped')
                realChoiceResp.status = FINISHED
        if realChoiceResp.status == STARTED and not waitOnFlip:
            theseKeys = realChoiceResp.getKeys(keyList=['v','n'], waitRelease=False)
            _realChoiceResp_allKeys.extend(theseKeys)
            if len(_realChoiceResp_allKeys):
                realChoiceResp.keys = _realChoiceResp_allKeys[-1].name  # just the last key pressed
                realChoiceResp.rt = _realChoiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realChoice" ---
    for thisComponent in realChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from realChoiceRandLoc
    thisExp.addData("loc", loc)
    # check responses
    if realChoiceResp.keys in ['', [], None]:  # No response was made
        realChoiceResp.keys = None
    dynamicTrials.addData('realChoiceResp.keys',realChoiceResp.keys)
    if realChoiceResp.keys != None:  # we had a response
        dynamicTrials.addData('realChoiceResp.rt', realChoiceResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "realISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    realISIComponents = [isiFix]
    for thisComponent in realISIComponents:
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
    
    # --- Run Routine "realISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiFix* updates
        if isiFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiFix.frameNStart = frameN  # exact frame index
            isiFix.tStart = t  # local t and not account for scr refresh
            isiFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiFix.started')
            isiFix.setAutoDraw(True)
        if isiFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiFix.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                isiFix.tStop = t  # not accounting for scr refresh
                isiFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiFix.stopped')
                isiFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realISI" ---
    for thisComponent in realISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "dynamicOutcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from dynamicOCcode
    import random
    import math
    if not realChoiceResp.keys:
        outcometmp = math.nan
        choicetmp = math.nan
        riskyLossReal = math.nan
        riskyGainReal = math.nan
        certain = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoiceResp.keys == 'v' and loc == 1:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        if outcometmp == riskyoption1:
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.15]
        elif outcometmp == riskyoption2:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.15]
             noRespLoc = [5,5]
    elif realChoiceResp.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        ocLoc = [-.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoiceResp.keys == 'n' and loc ==1:
        outcometmp = safeoption
        choicetmp = 0
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        ocLoc = [.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoiceResp.keys == 'n' and loc ==2:
        outcometmp = random.choice([riskyoption1, riskyoption2])
        choicetmp = 1
        extraITI = 4-realChoiceResp.rt
        riskyLossReal = riskyoption2
        riskyGainReal = riskyoption1
        certain = safeoption
        if outcometmp == riskyoption1:
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.15]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.15]
            noRespLoc = [5,5]
    
    actualITI = initITIdynamic[dynamicTrials.thisN] + extraITI
    
    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLossReal)
    riskygain_values.append(riskyGainReal)
    certain_values.append(certain)
    dynamicNoRespText.setPos(noRespLoc)
    dynamicRiskOC.setPos(ocGambleLoc)
    dynamicSafeOC.setPos(ocSafeLoc)
    dynamicOCtext.setColor([0.5216,0.5216,0.5216], colorSpace='rgb')
    dynamicOCtext.setPos(ocLoc)
    dynamicOCtext.setText(feedbackRounded)
    dynamicHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    dynamicOutcomeComponents = [dynamicNoRespText, dynamicRiskOC, dynamicSafeOC, dynamicOCtext, dynamicHideRisk]
    for thisComponent in dynamicOutcomeComponents:
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
    
    # --- Run Routine "dynamicOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dynamicNoRespText* updates
        if dynamicNoRespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynamicNoRespText.frameNStart = frameN  # exact frame index
            dynamicNoRespText.tStart = t  # local t and not account for scr refresh
            dynamicNoRespText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynamicNoRespText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynamicNoRespText.started')
            dynamicNoRespText.setAutoDraw(True)
        if dynamicNoRespText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynamicNoRespText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynamicNoRespText.tStop = t  # not accounting for scr refresh
                dynamicNoRespText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynamicNoRespText.stopped')
                dynamicNoRespText.setAutoDraw(False)
        
        # *dynamicRiskOC* updates
        if dynamicRiskOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynamicRiskOC.frameNStart = frameN  # exact frame index
            dynamicRiskOC.tStart = t  # local t and not account for scr refresh
            dynamicRiskOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynamicRiskOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynamicRiskOC.started')
            dynamicRiskOC.setAutoDraw(True)
        if dynamicRiskOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynamicRiskOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynamicRiskOC.tStop = t  # not accounting for scr refresh
                dynamicRiskOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynamicRiskOC.stopped')
                dynamicRiskOC.setAutoDraw(False)
        
        # *dynamicSafeOC* updates
        if dynamicSafeOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynamicSafeOC.frameNStart = frameN  # exact frame index
            dynamicSafeOC.tStart = t  # local t and not account for scr refresh
            dynamicSafeOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynamicSafeOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynamicSafeOC.started')
            dynamicSafeOC.setAutoDraw(True)
        if dynamicSafeOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynamicSafeOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynamicSafeOC.tStop = t  # not accounting for scr refresh
                dynamicSafeOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynamicSafeOC.stopped')
                dynamicSafeOC.setAutoDraw(False)
        
        # *dynamicOCtext* updates
        if dynamicOCtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynamicOCtext.frameNStart = frameN  # exact frame index
            dynamicOCtext.tStart = t  # local t and not account for scr refresh
            dynamicOCtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynamicOCtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynamicOCtext.started')
            dynamicOCtext.setAutoDraw(True)
        if dynamicOCtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynamicOCtext.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynamicOCtext.tStop = t  # not accounting for scr refresh
                dynamicOCtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynamicOCtext.stopped')
                dynamicOCtext.setAutoDraw(False)
        
        # *dynamicHideRisk* updates
        if dynamicHideRisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynamicHideRisk.frameNStart = frameN  # exact frame index
            dynamicHideRisk.tStart = t  # local t and not account for scr refresh
            dynamicHideRisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynamicHideRisk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynamicHideRisk.started')
            dynamicHideRisk.setAutoDraw(True)
        if dynamicHideRisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynamicHideRisk.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynamicHideRisk.tStop = t  # not accounting for scr refresh
                dynamicHideRisk.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynamicHideRisk.stopped')
                dynamicHideRisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dynamicOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "dynamicOutcome" ---
    for thisComponent in dynamicOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from dynamicOCcode
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "realITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    realITIComponents = [itiFix]
    for thisComponent in realITIComponents:
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
    
    # --- Run Routine "realITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *itiFix* updates
        if itiFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiFix.frameNStart = frameN  # exact frame index
            itiFix.tStart = t  # local t and not account for scr refresh
            itiFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiFix.started')
            itiFix.setAutoDraw(True)
        if itiFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiFix.tStartRefresh + actualITI-frameTolerance:
                # keep track of stop time/frame for later
                itiFix.tStop = t  # not accounting for scr refresh
                itiFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiFix.stopped')
                itiFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realITI" ---
    for thisComponent in realITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "realITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'dynamicTrials'


# --- Prepare to start Routine "cgeRDMend" ---
continueRoutine = True
# update component parameters for each repeat
cgeRDMendResp.keys = []
cgeRDMendResp.rt = []
_cgeRDMendResp_allKeys = []
# keep track of which components have finished
cgeRDMendComponents = [cgeRDMendText, cgeRDMendResp]
for thisComponent in cgeRDMendComponents:
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

# --- Run Routine "cgeRDMend" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cgeRDMendText* updates
    if cgeRDMendText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cgeRDMendText.frameNStart = frameN  # exact frame index
        cgeRDMendText.tStart = t  # local t and not account for scr refresh
        cgeRDMendText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cgeRDMendText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cgeRDMendText.started')
        cgeRDMendText.setAutoDraw(True)
    
    # *cgeRDMendResp* updates
    waitOnFlip = False
    if cgeRDMendResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cgeRDMendResp.frameNStart = frameN  # exact frame index
        cgeRDMendResp.tStart = t  # local t and not account for scr refresh
        cgeRDMendResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cgeRDMendResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cgeRDMendResp.started')
        cgeRDMendResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(cgeRDMendResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(cgeRDMendResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if cgeRDMendResp.status == STARTED and not waitOnFlip:
        theseKeys = cgeRDMendResp.getKeys(keyList=['return'], waitRelease=False)
        _cgeRDMendResp_allKeys.extend(theseKeys)
        if len(_cgeRDMendResp_allKeys):
            cgeRDMendResp.keys = _cgeRDMendResp_allKeys[-1].name  # just the last key pressed
            cgeRDMendResp.rt = _cgeRDMendResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cgeRDMendComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cgeRDMend" ---
for thisComponent in cgeRDMendComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if cgeRDMendResp.keys in ['', [], None]:  # No response was made
    cgeRDMendResp.keys = None
thisExp.addData('cgeRDMendResp.keys',cgeRDMendResp.keys)
if cgeRDMendResp.keys != None:  # we had a response
    thisExp.addData('cgeRDMendResp.rt', cgeRDMendResp.rt)
thisExp.nextEntry()
# the Routine "cgeRDMend" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "END" ---
continueRoutine = True
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
while continueRoutine and routineTimer.getTime() < 2.0:
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
    if ThankYou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThankYou.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            ThankYou.tStop = t  # not accounting for scr refresh
            ThankYou.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ThankYou.stopped')
            ThankYou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
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
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-2.000000)

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
