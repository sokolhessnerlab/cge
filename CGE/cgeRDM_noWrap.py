#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 03, 2023, at 08:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""



import psychopy
psychopy.useVersion('2022.2.4')


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

# Run 'Before Experiment' code from etCameraSetupCode

### Setting up eye-tracker

# doET:
#   1: do eye-tracking
#   0: don't do eye-tracking
doET = 0
#subID = ''

if doET:
    # Calling relevant eye-tracker modules
    import pylink
    import time
    from PIL import Image  # for preparing the Host backdrop image
    from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
    import subprocess
    # Step 1: Connect to the EyeLink Host PC # The Host IP address, by default, is "100.1.1.1".
    et = pylink.EyeLink("100.1.1.1")
    # Step 2: Open an EDF data file on the Host PC
    edf_fname = 'CGE%s' % subID
    et.openDataFile(edf_fname + '.edf')
    # Step 3: Configure the tracker
    # Put the tracker in offline mode before we change tracking parameters
    et.setOfflineMode()
    # File and Link data control
    file_sample_flags = 'GAZE,GAZERES,AREA,BUTTON,STATUS,INPUT'
    et.sendCommand("file_sample_data = %s" % file_sample_flags)
    # Optional tracking parameters
    # Sample rate, 250, 500, 1000, or 2000, check your tracker specification
    et.sendCommand("sample_rate 1000")
    # Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
    et.sendCommand("calibration_type = HV9")





# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'cgeRDM'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
#expInfo['subID'] = subID
# --- Show participant info dialog --
#dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
#if dlg.OK == False:
#    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
#filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['subID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE\\cgeRDMdraftET.py',
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
    size=[1280, 1024], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.5216,0.5216,0.5216], colorSpace='rgb',
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

# --- Initialize components for Routine "etCameraSetup" ---
etSetupInstText = visual.TextStim(win=win, name='etSetupInstText',
    text='Press any \'Enter" twice to start Camera Setup',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
etSetupInstResp = keyboard.Keyboard()
# Run 'Begin Experiment' code from etCameraSetupCode

### This Begin Experiment tab of the elConnect component gets graphic 
# information from Psychopy, sets the screen_pixel_coords on the Host PC based
# on these values, and logs the screen resolution for Data Viewer via 
# a DISPLAY_COORDS message
if doET:
    # get the native screen resolution used by PsychoPy
    scn_width, scn_height = win.size

    # Pass the display pixel coordinates (left, top, right, bottom) to the tracker
    # see the EyeLink Installation Guide, "Customizing Screen Settings"
    et_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
    et.sendCommand(et_coords)

    # Write a DISPLAY_COORDS message to the EDF file
    # Data Viewer needs this piece of info for proper visualization, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
    et.sendMessage(dv_coords)
    
    
    

# --- Initialize components for Routine "cgeRDMsetup" ---
# Run 'Begin Experiment' code from cgeRDMsetupCode

### Real or Practice
isReal = 0 # 1 will execute the full cgeRDM trials
isHide = 1 # 1 hides the trial number

### Isoluminant Colors Used 
color1 = [0.5216,0.5216,0.5216]
color2 = [-0.0667,0.6392,1]
# BLUE ### Choice Shape; V, N, and OR text
# PsychoPy RGB -1:1 [-0.0667,0.6392,1] # RGB 0:255 [119,209,205]
# GREY ### Background; Choice Line
# psychopy RGB -1:1 [0.5216,0.5216,0.5216] # RGB 0:255 [194,194,194] 

### Text Fonts
instructionsFont = 'Arial'
choiceFont = 'Arial'
choiceValueFont = 'Arial'
fixCrossFont = 'Arial'
NoRespFont = 'Arial'
ocFont = 'Arial'
trialNumFont = 'Arial'

### Text Dimensions
wrap = 1.1
instructionsTextHeight = .05
choiceTextHeight = .05
choiceValuesTextHeight = .1
FixCrossHeight = .05
NoRespTextHeight = .08
ocTextHeight = .1
trialNumHeight = .1

### Instructions Location
instructLoc = [0,0]

### Shapes 'circle' 'rectangle' 'star.7' etc.
leftShape = 'circle'
rightShape = 'circle'
riskShape = 'rectangle'
hideShape = 'rectangle'

### Shape Dimensions
circLeft = [.5,.5]
circRight = [.5,.5]
riskLine = [.5,.01]
riskHide = [.6,.3]

### Fixed Trial Locations
circLeftLoc=[-.35,0]
circRightLoc=[.35,0]
ORtextLoc=[0,0]
VleftLoc=[-.35,-.35]
NrightLoc=[.35,-.35]
fixCrossLoc=[0,0]
trialNumLoc=[0,-.35]

### Number of Trials per Choice Sets
if isReal == 1:
    pracChoices = '0:5'
    statChoices = '0:50'
    dynaChoices = '0:120'
else:
    # 3 trials to choose: A risky, A safe, and A no respond
    pracChoices = '0:3'
    statChoices = '0:3'
    dynaChoices = '0:3'
    
### Trial Number Appearance 
if isHide == 1:
    trialNumColor = [0.5216,0.5216,0.5216]
else:
    trialNumColor = [-0.0667,0.6392,1]

### ITIs
initITIstatic = []
initITIdynamic = []




# --- Initialize components for Routine "cgeRDMstart" ---
cgeRDMstartTxt = visual.TextStim(win=win, name='cgeRDMstartTxt',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nYou may press "V" to select the option on the left and "N" to select the option on the right.\n\nPress "enter" to move on to the next screen.',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cgeRDMstartResp = keyboard.Keyboard()

# --- Initialize components for Routine "etStartRecording" ---

# --- Initialize components for Routine "practiceStart" ---
pracStartTxt = visual.TextStim(win=win, name='pracStartTxt',
    text='There will now be 5 practice trials.\n\nThe structure in the practice round is identical to what you will encounter in the real rounds. The goal of the practice round is to practice timing of decision-making within the four (4) second response window.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pracStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "pracChoices" ---
pracCircLeft = visual.ShapeStim(
    win=win, name='pracCircLeft', vertices=leftShape,
    size=circLeft,
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-1.0, interpolate=True)
pracCircRight = visual.ShapeStim(
    win=win, name='pracCircRight', vertices=rightShape,
    size=circRight,
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
pracRiskLine = visual.ShapeStim(
    win=win, name='pracRiskLine', vertices=riskShape,
    size=riskLine,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-3.0, interpolate=True)
pracORtxt = visual.TextStim(win=win, name='pracORtxt',
    text='OR',
    font=choiceFont,
    pos=ORtextLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
pracTriNum = visual.TextStim(win=win, name='pracTriNum',
    text='',
    font=trialNumFont,
    pos=trialNumLoc, height=trialNumHeight, wrapWidth=wrap, ori=0.0, 
    color=trialNumColor, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
pracLossTxt = visual.TextStim(win=win, name='pracLossTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
pracGainTxt = visual.TextStim(win=win, name='pracGainTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
pracSafeTxt = visual.TextStim(win=win, name='pracSafeTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
pracVleft = visual.TextStim(win=win, name='pracVleft',
    text='V-Left',
    font=choiceFont,
    pos=VleftLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
pracNright = visual.TextStim(win=win, name='pracNright',
    text='N-Right',
    font=choiceFont,
    pos=NrightLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
pracChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "pracISI" ---
isiPracFix = visual.TextStim(win=win, name='isiPracFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pracOutcome" ---
pracNoRespTxt = visual.TextStim(win=win, name='pracNoRespTxt',
    text='You did not respond in time\n',
    font=NoRespFont,
    pos=[0,0], height=NoRespTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pracRiskOC = visual.ShapeStim(
    win=win, name='pracRiskOC', vertices=leftShape,
    size=circLeft,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-2.0, interpolate=True)
pracSafeOC = visual.ShapeStim(
    win=win, name='pracSafeOC', vertices=rightShape,
    size=circRight,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-3.0, interpolate=True)
pracOCtxt = visual.TextStim(win=win, name='pracOCtxt',
    text='',
    font=ocFont,
    pos=[0,0], height=ocTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
pracHideRisk = visual.ShapeStim(
    win=win, name='pracHideRisk', vertices=hideShape,
    size=riskHide,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "pracITI" ---
itiPracFix = visual.TextStim(win=win, name='itiPracFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "staticStart" ---
statStartTxt = visual.TextStim(win=win, name='statStartTxt',
    text='Practice complete.\n\nKeep in mind that responding quickly in this task will not speed up the task. Please take enough time to view and consider each choice option before you make a choice within the 4-second response window.\n\nWhen you are ready to start ROUND 1 of the task, press "V" or "N".\n',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
statStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "realChoices" ---
# Run 'Begin Experiment' code from realChoiceRandLoc

loc = []
staticTrials = []
# primarily for displaying trial number during dynamic trials because this code section gets called before actual dynamic trials
dynamicTrials = [] 



realCircLeft = visual.ShapeStim(
    win=win, name='realCircLeft', vertices=leftShape,
    size=circLeft,
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-1.0, interpolate=True)
realCircRight = visual.ShapeStim(
    win=win, name='realCircRight', vertices=rightShape,
    size=circRight,
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
realRiskLine = visual.ShapeStim(
    win=win, name='realRiskLine', vertices=riskShape,
    size=riskLine,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-3.0, interpolate=True)
realORtxt = visual.TextStim(win=win, name='realORtxt',
    text='OR',
    font=choiceFont,
    pos=ORtextLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
realPracNum = visual.TextStim(win=win, name='realPracNum',
    text='',
    font=trialNumFont,
    pos=trialNumLoc, height=trialNumHeight, wrapWidth=wrap, ori=0.0, 
    color=trialNumColor, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
realLossTxt = visual.TextStim(win=win, name='realLossTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
realGainTxt = visual.TextStim(win=win, name='realGainTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
realSafeTxt = visual.TextStim(win=win, name='realSafeTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
realVleft = visual.TextStim(win=win, name='realVleft',
    text='V-Left',
    font=choiceFont,
    pos=VleftLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realNright = visual.TextStim(win=win, name='realNright',
    text='N-Right',
    font=choiceFont,
    pos=NrightLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
realChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "realISI" ---
isiRealFix = visual.TextStim(win=win, name='isiRealFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "statOutcome" ---
# Run 'Begin Experiment' code from statOCcode

actualITI = []
riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []



statNoRespTxt = visual.TextStim(win=win, name='statNoRespTxt',
    text='You did not respond in time\n',
    font=NoRespFont,
    pos=[0,0], height=NoRespTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
statRiskOC = visual.ShapeStim(
    win=win, name='statRiskOC', vertices=leftShape,
    size=circLeft,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-2.0, interpolate=True)
statSafeOC = visual.ShapeStim(
    win=win, name='statSafeOC', vertices=rightShape,
    size=circRight,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-3.0, interpolate=True)
statOCtxt = visual.TextStim(win=win, name='statOCtxt',
    text='',
    font=ocFont,
    pos=[0,0], height=ocTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
statHideRisk = visual.ShapeStim(
    win=win, name='statHideRisk', vertices=hideShape,
    size=riskHide,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "realITI" ---
itiRealFix = visual.TextStim(win=win, name='itiRealFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "computeBestFit" ---
# Run 'Begin Experiment' code from gridSearchCode

### Computing the Best Fit Pair
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
setupBestFitTxt = visual.TextStim(win=win, name='setupBestFitTxt',
    text='ROUND 1 of the gambling task is complete! \n\nSetting up for the last round of the gambling task.\n\nPlease wait...\n\n\n',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=color2, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "loadingDynamicChoices" ---
loadDynaChoicesTxt = visual.TextStim(win=win, name='loadDynaChoicesTxt',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "dynamicStart" ---
dynaStartTxt = visual.TextStim(win=win, name='dynaStartTxt',
    text='Keep in mind that responding quickly in this task will not speed up the task. Please take enough time to view and consider each choice option before you make a choice within the 4-second response window.\n\nWhen you are ready to start ROUND 2 of the task, press "V" or "N".',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=color2, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dynaStartResp = keyboard.Keyboard()

# --- Initialize components for Routine "realChoices" ---
# Run 'Begin Experiment' code from realChoiceRandLoc

loc = []
staticTrials = []
# primarily for displaying trial number during dynamic trials because this code section gets called before actual dynamic trials
dynamicTrials = [] 



realCircLeft = visual.ShapeStim(
    win=win, name='realCircLeft', vertices=leftShape,
    size=circLeft,
    ori=0, pos=circLeftLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-1.0, interpolate=True)
realCircRight = visual.ShapeStim(
    win=win, name='realCircRight', vertices=rightShape,
    size=circRight,
    ori=0, pos=circRightLoc, anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-2.0, interpolate=True)
realRiskLine = visual.ShapeStim(
    win=win, name='realRiskLine', vertices=riskShape,
    size=riskLine,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-3.0, interpolate=True)
realORtxt = visual.TextStim(win=win, name='realORtxt',
    text='OR',
    font=choiceFont,
    pos=ORtextLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
realPracNum = visual.TextStim(win=win, name='realPracNum',
    text='',
    font=trialNumFont,
    pos=trialNumLoc, height=trialNumHeight, wrapWidth=wrap, ori=0.0, 
    color=trialNumColor, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
realLossTxt = visual.TextStim(win=win, name='realLossTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
realGainTxt = visual.TextStim(win=win, name='realGainTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
realSafeTxt = visual.TextStim(win=win, name='realSafeTxt',
    text='',
    font=choiceValueFont,
    pos=[0,0], height=choiceValuesTextHeight, wrapWidth=None, ori=0, 
    color=color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
realVleft = visual.TextStim(win=win, name='realVleft',
    text='V-Left',
    font=choiceFont,
    pos=VleftLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
realNright = visual.TextStim(win=win, name='realNright',
    text='N-Right',
    font=choiceFont,
    pos=NrightLoc, height=choiceTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
realChoiceResp = keyboard.Keyboard()

# --- Initialize components for Routine "realISI" ---
isiRealFix = visual.TextStim(win=win, name='isiRealFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "dynaOutcome" ---
# Run 'Begin Experiment' code from dynaOCcode

riskygain_values = []
riskyloss_values = []
certain_values = []
choices = []
outcomes = []



dynaNoRespTxt = visual.TextStim(win=win, name='dynaNoRespTxt',
    text='You did not respond in time\n',
    font=NoRespFont,
    pos=[0,0], height=NoRespTextHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
dynaRiskOC = visual.ShapeStim(
    win=win, name='dynaRiskOC', vertices=leftShape,
    size=circLeft,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-2.0, interpolate=True)
dynaSafeOC = visual.ShapeStim(
    win=win, name='dynaSafeOC', vertices=rightShape,
    size=circRight,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color2, fillColor=color2,
    opacity=1, depth=-3.0, interpolate=True)
dynaOCtxt = visual.TextStim(win=win, name='dynaOCtxt',
    text='',
    font=ocFont,
    pos=[0,0], height=ocTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
dynaHideRisk = visual.ShapeStim(
    win=win, name='dynaHideRisk', vertices=hideShape,
    size=riskHide,
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=color1, fillColor=color1,
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "realITI" ---
itiRealFix = visual.TextStim(win=win, name='itiRealFix',
    text='+',
    font=fixCrossFont,
    pos=fixCrossLoc, height=FixCrossHeight, wrapWidth=None, ori=0, 
    color=color2, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "etStopRecording" ---

# --- Initialize components for Routine "cgeRDMend" ---
cgeRDMendTxt = visual.TextStim(win=win, name='cgeRDMendTxt',
    text="You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=color2, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cgeRDMendResp = keyboard.Keyboard()

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this study.\n\nIf you have not already done so, \nplease notify the experimenter with by pressing the white doorbell button.',
    font=instructionsFont,
    pos=instructLoc, height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color=color2, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "etCameraSetup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
etSetupInstResp.keys = []
etSetupInstResp.rt = []
_etSetupInstResp_allKeys = []
# keep track of which components have finished
etCameraSetupComponents = [etSetupInstText, etSetupInstResp]
for thisComponent in etCameraSetupComponents:
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

# --- Run Routine "etCameraSetup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *etSetupInstText* updates
    if etSetupInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etSetupInstText.frameNStart = frameN  # exact frame index
        etSetupInstText.tStart = t  # local t and not account for scr refresh
        etSetupInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etSetupInstText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'etSetupInstText.started')
        etSetupInstText.setAutoDraw(True)
    
    # *etSetupInstResp* updates
    waitOnFlip = False
    if etSetupInstResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etSetupInstResp.frameNStart = frameN  # exact frame index
        etSetupInstResp.tStart = t  # local t and not account for scr refresh
        etSetupInstResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etSetupInstResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'etSetupInstResp.started')
        etSetupInstResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(etSetupInstResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(etSetupInstResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if etSetupInstResp.status == STARTED and not waitOnFlip:
        theseKeys = etSetupInstResp.getKeys(keyList=["return"], waitRelease=False)
        _etSetupInstResp_allKeys.extend(theseKeys)
        if len(_etSetupInstResp_allKeys):
            etSetupInstResp.keys = _etSetupInstResp_allKeys[-1].name  # just the last key pressed
            etSetupInstResp.rt = _etSetupInstResp_allKeys[-1].rt
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
    for thisComponent in etCameraSetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "etCameraSetup" ---
for thisComponent in etCameraSetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if etSetupInstResp.keys in ['', [], None]:  # No response was made
    etSetupInstResp.keys = None
thisExp.addData('etSetupInstResp.keys',etSetupInstResp.keys)
if etSetupInstResp.keys != None:  # we had a response
    thisExp.addData('etSetupInstResp.rt', etSetupInstResp.rt)
thisExp.nextEntry()
# Run 'End Routine' code from etCameraSetupCode

### This End Routine tab sets up graphics options for calibration, and then performs a camera setup
# so that you can set up the eye tracker and calibrate/validate the participant
if doET:
    # Configure a graphics environment (genv) for tracker calibration
    genv = EyeLinkCoreGraphicsPsychoPy(et, win)
    print(genv)  # print out the version number of the CoreGraphics library
    # Set up the calibration target # genv.setTargetType to "circle", "picture", "movie", or "spiral", e.g.,
    genv.setTargetType('circle')
    # Use a picture as the calibration target
    #genv.setTargetType('picture') ### The picture doesn't show the second time around
    #genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp'))
    # Beeps to play during calibration, validation and drift correction # parameters: target, good, error
    # Each parameter could be ''--default sound, 'off'--no sound, or a wav file
    genv.setCalibrationSounds('', '', '')
    # Request Pylink to use the PsychoPy window we opened above for calibration
    pylink.openGraphicsEx(genv)
    et.doTrackerSetup()



# the Routine "etCameraSetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cgeRDMsetup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
cgeRDMsetupComponents = []
for thisComponent in cgeRDMsetupComponents:
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

# --- Run Routine "cgeRDMsetup" ---
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
    for thisComponent in cgeRDMsetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cgeRDMsetup" ---
for thisComponent in cgeRDMsetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from cgeRDMsetupCode

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
initITIstatic = [3, 3.5] * 25 #1, 1.5
initITIdynamic = [3, 3.5] * 60 #1, 1.5

# Shuffle the ITIs using the shuffle function
shuffle(initITIstatic)
shuffle(initITIdynamic)

# Save the ITIs as experiment data
thisExp.addData('initITIstatic', initITIstatic)
thisExp.addData('initITIdynamic', initITIdynamic)



# the Routine "cgeRDMsetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cgeRDMstart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
cgeRDMstartResp.keys = []
cgeRDMstartResp.rt = []
_cgeRDMstartResp_allKeys = []
# keep track of which components have finished
cgeRDMstartComponents = [cgeRDMstartTxt, cgeRDMstartResp]
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
    
    # *cgeRDMstartTxt* updates
    if cgeRDMstartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cgeRDMstartTxt.frameNStart = frameN  # exact frame index
        cgeRDMstartTxt.tStart = t  # local t and not account for scr refresh
        cgeRDMstartTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cgeRDMstartTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cgeRDMstartTxt.started')
        cgeRDMstartTxt.setAutoDraw(True)
    
    # *cgeRDMstartResp* updates
    waitOnFlip = False
    if cgeRDMstartResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        cgeRDMstartResp.frameNStart = frameN  # exact frame index
        cgeRDMstartResp.tStart = t  # local t and not account for scr refresh
        cgeRDMstartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cgeRDMstartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cgeRDMstartResp.started')
        cgeRDMstartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(cgeRDMstartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(cgeRDMstartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if cgeRDMstartResp.status == STARTED and not waitOnFlip:
        theseKeys = cgeRDMstartResp.getKeys(keyList=["return"], waitRelease=False)
        _cgeRDMstartResp_allKeys.extend(theseKeys)
        if len(_cgeRDMstartResp_allKeys):
            cgeRDMstartResp.keys = _cgeRDMstartResp_allKeys[-1].name  # just the last key pressed
            cgeRDMstartResp.rt = _cgeRDMstartResp_allKeys[-1].rt
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
if cgeRDMstartResp.keys in ['', [], None]:  # No response was made
    cgeRDMstartResp.keys = None
thisExp.addData('cgeRDMstartResp.keys',cgeRDMstartResp.keys)
if cgeRDMstartResp.keys != None:  # we had a response
    thisExp.addData('cgeRDMstartResp.rt', cgeRDMstartResp.rt)
thisExp.nextEntry()
# the Routine "cgeRDMstart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "etStartRecording" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from etStartRecCode

#### This Begin Routine tab sets up recording of the eye-tracker

if doET:
    # Put tracker in idle/offline mode before recording
    et.setOfflineMode()
    et.startRecording(1, 0, 0, 0)
    # Allocate some time for the tracker to cache some samples
    et.sendMessage('pre 100 pause')
    pylink.pumpDelay(100)
    # Send message that recording has started
    et.sendMessage('cgeRDM Recording Started')



# keep track of which components have finished
etStartRecordingComponents = []
for thisComponent in etStartRecordingComponents:
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

# --- Run Routine "etStartRecording" ---
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
    for thisComponent in etStartRecordingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "etStartRecording" ---
for thisComponent in etStartRecordingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "etStartRecording" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "practiceStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pracStartResp.keys = []
pracStartResp.rt = []
_pracStartResp_allKeys = []
# keep track of which components have finished
practiceStartComponents = [pracStartTxt, pracStartResp]
for thisComponent in practiceStartComponents:
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

# --- Run Routine "practiceStart" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracStartTxt* updates
    if pracStartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracStartTxt.frameNStart = frameN  # exact frame index
        pracStartTxt.tStart = t  # local t and not account for scr refresh
        pracStartTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracStartTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pracStartTxt.started')
        if doET:
            et.sendMessage('Practice Text Shown') # 10.3.23
        pracStartTxt.setAutoDraw(True)
    
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practiceStart" ---
for thisComponent in practiceStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if pracStartResp.keys in ['', [], None]:  # No response was made
    pracStartResp.keys = None
thisExp.addData('pracStartResp.keys',pracStartResp.keys)
if pracStartResp.keys != None:  # we had a response
    thisExp.addData('pracStartResp.rt', pracStartResp.rt)
thisExp.nextEntry()
# the Routine "practiceStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgeRDMPractice.xlsx', selection=pracChoices),
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pracChoices" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracChoiceRandLoc
    
    # Randomized Practice Trial Locations
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
    
    #riskyLoss = [] ### 10.3.23
    
    # Rounding Presentation of Monetary Values    
    pracLossRounded = '$%.0f' % round(riskyLoss,0)
    pracGainRounded = '$%.2f' % round(riskyGain,2)
    pracSafeRounded = '$%.2f' % round(alternative,2)
    
    pracNum = practiceTrials.thisN + 1
    
    
    
    pracCircRight.setFillColor(color2)
    pracCircRight.setLineColor(color2)
    pracRiskLine.setPos(riskLineLoc)
    pracTriNum.setText(pracNum)
    pracLossTxt.setPos(lossLoc)
    pracLossTxt.setText(pracLossRounded

)
    pracGainTxt.setPos(gainLoc)
    pracGainTxt.setText(pracGainRounded)
    pracSafeTxt.setPos(safeLoc)
    pracSafeTxt.setText(pracSafeRounded)
    pracChoiceResp.keys = []
    pracChoiceResp.rt = []
    _pracChoiceResp_allKeys = []
    # keep track of which components have finished
    pracChoicesComponents = [pracCircLeft, pracCircRight, pracRiskLine, pracORtxt, pracTriNum, pracLossTxt, pracGainTxt, pracSafeTxt, pracVleft, pracNright, pracChoiceResp]
    for thisComponent in pracChoicesComponents:
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
    
    # --- Run Routine "pracChoices" ---
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
        
        # *pracORtxt* updates
        if pracORtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracORtxt.frameNStart = frameN  # exact frame index
            pracORtxt.tStart = t  # local t and not account for scr refresh
            pracORtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracORtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracORtxt.started')
            pracORtxt.setAutoDraw(True)
        if pracORtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracORtxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracORtxt.tStop = t  # not accounting for scr refresh
                pracORtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracORtxt.stopped')
                pracORtxt.setAutoDraw(False)
        
        # *pracTriNum* updates
        if pracTriNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracTriNum.frameNStart = frameN  # exact frame index
            pracTriNum.tStart = t  # local t and not account for scr refresh
            pracTriNum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracTriNum, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracTriNum.started')
            pracTriNum.setAutoDraw(True)
        if pracTriNum.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracTriNum.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                pracTriNum.tStop = t  # not accounting for scr refresh
                pracTriNum.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracTriNum.stopped')
                pracTriNum.setAutoDraw(False)
        
        # *pracLossTxt* updates
        if pracLossTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracLossTxt.frameNStart = frameN  # exact frame index
            pracLossTxt.tStart = t  # local t and not account for scr refresh
            pracLossTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracLossTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracLossTxt.started')
            pracLossTxt.setAutoDraw(True)
        if pracLossTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracLossTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracLossTxt.tStop = t  # not accounting for scr refresh
                pracLossTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracLossTxt.stopped')
                pracLossTxt.setAutoDraw(False)
        
        # *pracGainTxt* updates
        if pracGainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracGainTxt.frameNStart = frameN  # exact frame index
            pracGainTxt.tStart = t  # local t and not account for scr refresh
            pracGainTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracGainTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracGainTxt.started')
            pracGainTxt.setAutoDraw(True)
        if pracGainTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracGainTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracGainTxt.tStop = t  # not accounting for scr refresh
                pracGainTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracGainTxt.stopped')
                pracGainTxt.setAutoDraw(False)
        
        # *pracSafeTxt* updates
        if pracSafeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracSafeTxt.frameNStart = frameN  # exact frame index
            pracSafeTxt.tStart = t  # local t and not account for scr refresh
            pracSafeTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracSafeTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracSafeTxt.started')
            pracSafeTxt.setAutoDraw(True)
        if pracSafeTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracSafeTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracSafeTxt.tStop = t  # not accounting for scr refresh
                pracSafeTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracSafeTxt.stopped')
                pracSafeTxt.setAutoDraw(False)
        
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracChoicesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracChoices" ---
    for thisComponent in pracChoicesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracChoiceResp.keys in ['', [], None]:  # No response was made
        pracChoiceResp.keys = None
    practiceTrials.addData('pracChoiceResp.keys',pracChoiceResp.keys)
    if pracChoiceResp.keys != None:  # we had a response
        practiceTrials.addData('pracChoiceResp.rt', pracChoiceResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "pracISI" ---
    continueRoutine = True
    routineForceEnded = False
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
            routineForceEnded = True
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
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracOCcode
    
    ### Practice Trial Randomized Outcome Presentation
    import random
    import math
    if not pracChoiceResp.keys:
        outcome = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
        extraITI = 0
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
    
    # $iti + extraITI was the original variable version of ITI
    
    if outcome == riskyLoss:
        pracFeedbackRounded = "$%.0f" % round(outcome,0)
    else:
        pracFeedbackRounded = "$%.2f" % round(outcome,2)
        
        
    
    pracNoRespTxt.setPos(noRespLoc)
    pracRiskOC.setPos(ocGambleLoc)
    pracSafeOC.setPos(ocSafeLoc)
    pracOCtxt.setColor(color1, colorSpace='rgb')
    pracOCtxt.setPos(ocLoc)
    pracOCtxt.setText(pracFeedbackRounded)
    pracHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    pracOutcomeComponents = [pracNoRespTxt, pracRiskOC, pracSafeOC, pracOCtxt, pracHideRisk]
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
        
        # *pracNoRespTxt* updates
        if pracNoRespTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracNoRespTxt.frameNStart = frameN  # exact frame index
            pracNoRespTxt.tStart = t  # local t and not account for scr refresh
            pracNoRespTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracNoRespTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracNoRespTxt.started')
            pracNoRespTxt.setAutoDraw(True)
        if pracNoRespTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracNoRespTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracNoRespTxt.tStop = t  # not accounting for scr refresh
                pracNoRespTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracNoRespTxt.stopped')
                pracNoRespTxt.setAutoDraw(False)
        
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
        
        # *pracOCtxt* updates
        if pracOCtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracOCtxt.frameNStart = frameN  # exact frame index
            pracOCtxt.tStart = t  # local t and not account for scr refresh
            pracOCtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracOCtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracOCtxt.started')
            pracOCtxt.setAutoDraw(True)
        if pracOCtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracOCtxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pracOCtxt.tStop = t  # not accounting for scr refresh
                pracOCtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracOCtxt.stopped')
                pracOCtxt.setAutoDraw(False)
        
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
            routineForceEnded = True
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
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "pracITI" ---
    continueRoutine = True
    routineForceEnded = False
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
            if tThisFlipGlobal > itiPracFix.tStartRefresh + iti-frameTolerance:
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
            routineForceEnded = True
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
    
# completed 1 repeats of 'practiceTrials'


# --- Prepare to start Routine "staticStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
statStartResp.keys = []
statStartResp.rt = []
_statStartResp_allKeys = []
# keep track of which components have finished
staticStartComponents = [statStartTxt, statStartResp]
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
    
    # *statStartTxt* updates
    if statStartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        statStartTxt.frameNStart = frameN  # exact frame index
        statStartTxt.tStart = t  # local t and not account for scr refresh
        statStartTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(statStartTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'statStartTxt.started')
        statStartTxt.setAutoDraw(True)
    
    # *statStartResp* updates
    waitOnFlip = False
    if statStartResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        statStartResp.frameNStart = frameN  # exact frame index
        statStartResp.tStart = t  # local t and not account for scr refresh
        statStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(statStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'statStartResp.started')
        statStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(statStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(statStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if statStartResp.status == STARTED and not waitOnFlip:
        theseKeys = statStartResp.getKeys(keyList=['v','n'], waitRelease=False)
        _statStartResp_allKeys.extend(theseKeys)
        if len(_statStartResp_allKeys):
            statStartResp.keys = _statStartResp_allKeys[-1].name  # just the last key pressed
            statStartResp.rt = _statStartResp_allKeys[-1].rt
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
if statStartResp.keys in ['', [], None]:  # No response was made
    statStartResp.keys = None
thisExp.addData('statStartResp.keys',statStartResp.keys)
if statStartResp.keys != None:  # we had a response
    thisExp.addData('statStartResp.rt', statStartResp.rt)
thisExp.nextEntry()
# the Routine "staticStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
staticTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CGT-choice-set.csv', selection=statChoices),
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
    
    # --- Prepare to start Routine "realChoices" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from realChoiceRandLoc
    
    ### Randomized Practice Trial Locations
    import random
    loc = random.choice([1,2])
    
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
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    
    if staticTrials:
        realNum = staticTrials.thisN + 1
        
    if dynamicTrials:
        realNum = dynamicTrials.thisN + 1
        
        
        
    realCircRight.setFillColor(color2)
    realCircRight.setLineColor(color2)
    realRiskLine.setPos(riskLineLoc)
    realPracNum.setText(realNum)
    realLossTxt.setPos(lossLoc)
    realLossTxt.setText(lossRounded)
    realGainTxt.setPos(gainLoc)
    realGainTxt.setText(gainRounded)
    realSafeTxt.setPos(safeLoc)
    realSafeTxt.setText(safeRounded)
    realChoiceResp.keys = []
    realChoiceResp.rt = []
    _realChoiceResp_allKeys = []
    # keep track of which components have finished
    realChoicesComponents = [realCircLeft, realCircRight, realRiskLine, realORtxt, realPracNum, realLossTxt, realGainTxt, realSafeTxt, realVleft, realNright, realChoiceResp]
    for thisComponent in realChoicesComponents:
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
    
    # --- Run Routine "realChoices" ---
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
        
        # *realORtxt* updates
        if realORtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realORtxt.frameNStart = frameN  # exact frame index
            realORtxt.tStart = t  # local t and not account for scr refresh
            realORtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realORtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realORtxt.started')
            realORtxt.setAutoDraw(True)
        if realORtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realORtxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realORtxt.tStop = t  # not accounting for scr refresh
                realORtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realORtxt.stopped')
                realORtxt.setAutoDraw(False)
        
        # *realPracNum* updates
        if realPracNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realPracNum.frameNStart = frameN  # exact frame index
            realPracNum.tStart = t  # local t and not account for scr refresh
            realPracNum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realPracNum, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realPracNum.started')
            realPracNum.setAutoDraw(True)
        if realPracNum.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realPracNum.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                realPracNum.tStop = t  # not accounting for scr refresh
                realPracNum.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realPracNum.stopped')
                realPracNum.setAutoDraw(False)
        
        # *realLossTxt* updates
        if realLossTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realLossTxt.frameNStart = frameN  # exact frame index
            realLossTxt.tStart = t  # local t and not account for scr refresh
            realLossTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realLossTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realLossTxt.started')
            realLossTxt.setAutoDraw(True)
        if realLossTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realLossTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realLossTxt.tStop = t  # not accounting for scr refresh
                realLossTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realLossTxt.stopped')
                realLossTxt.setAutoDraw(False)
        
        # *realGainTxt* updates
        if realGainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realGainTxt.frameNStart = frameN  # exact frame index
            realGainTxt.tStart = t  # local t and not account for scr refresh
            realGainTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realGainTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realGainTxt.started')
            realGainTxt.setAutoDraw(True)
        if realGainTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realGainTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realGainTxt.tStop = t  # not accounting for scr refresh
                realGainTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realGainTxt.stopped')
                realGainTxt.setAutoDraw(False)
        
        # *realSafeTxt* updates
        if realSafeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realSafeTxt.frameNStart = frameN  # exact frame index
            realSafeTxt.tStart = t  # local t and not account for scr refresh
            realSafeTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realSafeTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realSafeTxt.started')
            realSafeTxt.setAutoDraw(True)
        if realSafeTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realSafeTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realSafeTxt.tStop = t  # not accounting for scr refresh
                realSafeTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realSafeTxt.stopped')
                realSafeTxt.setAutoDraw(False)
        
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realChoicesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realChoices" ---
    for thisComponent in realChoicesComponents:
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "realISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    realISIComponents = [isiRealFix]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiRealFix* updates
        if isiRealFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiRealFix.frameNStart = frameN  # exact frame index
            isiRealFix.tStart = t  # local t and not account for scr refresh
            isiRealFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiRealFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiRealFix.started')
            isiRealFix.setAutoDraw(True)
        if isiRealFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiRealFix.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                isiRealFix.tStop = t  # not accounting for scr refresh
                isiRealFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiRealFix.stopped')
                isiRealFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "statOutcome" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from statOCcode
    
    ### Presentation of Real (Static & Dynamic) Outcomes
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
        extraITI = 0
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
    
    actualITI = initITIstatic[staticTrials.thisN] #+ extraITI
    
    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLossReal)
    riskygain_values.append(riskyGainReal)
    certain_values.append(certain)
    
    
    
    statNoRespTxt.setPos(noRespLoc)
    statRiskOC.setPos(ocGambleLoc)
    statSafeOC.setPos(ocSafeLoc)
    statOCtxt.setColor(color1, colorSpace='rgb')
    statOCtxt.setPos(ocLoc)
    statOCtxt.setText(feedbackRounded)
    statHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    statOutcomeComponents = [statNoRespTxt, statRiskOC, statSafeOC, statOCtxt, statHideRisk]
    for thisComponent in statOutcomeComponents:
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
    
    # --- Run Routine "statOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *statNoRespTxt* updates
        if statNoRespTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            statNoRespTxt.frameNStart = frameN  # exact frame index
            statNoRespTxt.tStart = t  # local t and not account for scr refresh
            statNoRespTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(statNoRespTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'statNoRespTxt.started')
            statNoRespTxt.setAutoDraw(True)
        if statNoRespTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > statNoRespTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                statNoRespTxt.tStop = t  # not accounting for scr refresh
                statNoRespTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'statNoRespTxt.stopped')
                statNoRespTxt.setAutoDraw(False)
        
        # *statRiskOC* updates
        if statRiskOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            statRiskOC.frameNStart = frameN  # exact frame index
            statRiskOC.tStart = t  # local t and not account for scr refresh
            statRiskOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(statRiskOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'statRiskOC.started')
            statRiskOC.setAutoDraw(True)
        if statRiskOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > statRiskOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                statRiskOC.tStop = t  # not accounting for scr refresh
                statRiskOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'statRiskOC.stopped')
                statRiskOC.setAutoDraw(False)
        
        # *statSafeOC* updates
        if statSafeOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            statSafeOC.frameNStart = frameN  # exact frame index
            statSafeOC.tStart = t  # local t and not account for scr refresh
            statSafeOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(statSafeOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'statSafeOC.started')
            statSafeOC.setAutoDraw(True)
        if statSafeOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > statSafeOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                statSafeOC.tStop = t  # not accounting for scr refresh
                statSafeOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'statSafeOC.stopped')
                statSafeOC.setAutoDraw(False)
        
        # *statOCtxt* updates
        if statOCtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            statOCtxt.frameNStart = frameN  # exact frame index
            statOCtxt.tStart = t  # local t and not account for scr refresh
            statOCtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(statOCtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'statOCtxt.started')
            statOCtxt.setAutoDraw(True)
        if statOCtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > statOCtxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                statOCtxt.tStop = t  # not accounting for scr refresh
                statOCtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'statOCtxt.stopped')
                statOCtxt.setAutoDraw(False)
        
        # *statHideRisk* updates
        if statHideRisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            statHideRisk.frameNStart = frameN  # exact frame index
            statHideRisk.tStart = t  # local t and not account for scr refresh
            statHideRisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(statHideRisk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'statHideRisk.started')
            statHideRisk.setAutoDraw(True)
        if statHideRisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > statHideRisk.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                statHideRisk.tStop = t  # not accounting for scr refresh
                statHideRisk.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'statHideRisk.stopped')
                statHideRisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in statOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "statOutcome" ---
    for thisComponent in statOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from statOCcode
    
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "realITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    realITIComponents = [itiRealFix]
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
        
        # *itiRealFix* updates
        if itiRealFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiRealFix.frameNStart = frameN  # exact frame index
            itiRealFix.tStart = t  # local t and not account for scr refresh
            itiRealFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiRealFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiRealFix.started')
            itiRealFix.setAutoDraw(True)
        if itiRealFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiRealFix.tStartRefresh + actualITI-frameTolerance:
                # keep track of stop time/frame for later
                itiRealFix.tStop = t  # not accounting for scr refresh
                itiRealFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiRealFix.stopped')
                itiRealFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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
    
    fname.append("../CGE/bespoke_choicesets/bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM))
    dynamicChoiceSetFilename = fname[0]
    
    
    
    dynamicChoiceSet = fname[0]  # Set routine start values for dynamicChoiceSet
    thisExp.addData('dynamicChoiceSet.routineStartVal', dynamicChoiceSet)  # Save exp start value
    bestRho = bestR  # Set routine start values for bestRho
    bestMu = bestM  # Set routine start values for bestMu
    # keep track of which components have finished
    computeBestFitComponents = [setupBestFitTxt]
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
        
        # *setupBestFitTxt* updates
        if setupBestFitTxt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            setupBestFitTxt.frameNStart = frameN  # exact frame index
            setupBestFitTxt.tStart = t  # local t and not account for scr refresh
            setupBestFitTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(setupBestFitTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'setupBestFitTxt.started')
            setupBestFitTxt.setAutoDraw(True)
        if setupBestFitTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > setupBestFitTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                setupBestFitTxt.tStop = t  # not accounting for scr refresh
                setupBestFitTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'setupBestFitTxt.stopped')
                setupBestFitTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
loadingDynamicChoicesComponents = [loadDynaChoicesTxt]
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
    
    # *loadDynaChoicesTxt* updates
    if loadDynaChoicesTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        loadDynaChoicesTxt.frameNStart = frameN  # exact frame index
        loadDynaChoicesTxt.tStart = t  # local t and not account for scr refresh
        loadDynaChoicesTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loadDynaChoicesTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'loadDynaChoicesTxt.started')
        loadDynaChoicesTxt.setAutoDraw(True)
    if loadDynaChoicesTxt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loadDynaChoicesTxt.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            loadDynaChoicesTxt.tStop = t  # not accounting for scr refresh
            loadDynaChoicesTxt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'loadDynaChoicesTxt.stopped')
            loadDynaChoicesTxt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "dynamicStart" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
dynaStartResp.keys = []
dynaStartResp.rt = []
_dynaStartResp_allKeys = []
# keep track of which components have finished
dynamicStartComponents = [dynaStartTxt, dynaStartResp]
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
    
    # *dynaStartTxt* updates
    if dynaStartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dynaStartTxt.frameNStart = frameN  # exact frame index
        dynaStartTxt.tStart = t  # local t and not account for scr refresh
        dynaStartTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dynaStartTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dynaStartTxt.started')
        dynaStartTxt.setAutoDraw(True)
    
    # *dynaStartResp* updates
    waitOnFlip = False
    if dynaStartResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dynaStartResp.frameNStart = frameN  # exact frame index
        dynaStartResp.tStart = t  # local t and not account for scr refresh
        dynaStartResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dynaStartResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dynaStartResp.started')
        dynaStartResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(dynaStartResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(dynaStartResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if dynaStartResp.status == STARTED and not waitOnFlip:
        theseKeys = dynaStartResp.getKeys(keyList=['v', 'n'], waitRelease=False)
        _dynaStartResp_allKeys.extend(theseKeys)
        if len(_dynaStartResp_allKeys):
            dynaStartResp.keys = _dynaStartResp_allKeys[-1].name  # just the last key pressed
            dynaStartResp.rt = _dynaStartResp_allKeys[-1].rt
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
if dynaStartResp.keys in ['', [], None]:  # No response was made
    dynaStartResp.keys = None
thisExp.addData('dynaStartResp.keys',dynaStartResp.keys)
if dynaStartResp.keys != None:  # we had a response
    thisExp.addData('dynaStartResp.rt', dynaStartResp.rt)
thisExp.nextEntry()
# the Routine "dynamicStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
dynamicTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(fname[0], selection=dynaChoices),
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
    
    # --- Prepare to start Routine "realChoices" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from realChoiceRandLoc
    
    ### Randomized Practice Trial Locations
    import random
    loc = random.choice([1,2])
    
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
    
    lossRounded = "$%.0f" % round(riskyoption2,0)
    gainRounded = "$%.2f" % round(riskyoption1,2)
    safeRounded = "$%.2f" % round(safeoption,2)
    
    #lossRounded = ("$" + str(round(riskyoption2, 2)))
    #gainRounded = ("$" + str(round(riskyoption1, 2)))
    #safeRounded = ("$" + str(round(safeoption, 2)))
    
    if staticTrials:
        realNum = staticTrials.thisN + 1
        
    if dynamicTrials:
        realNum = dynamicTrials.thisN + 1
        
        
        
    realCircRight.setFillColor(color2)
    realCircRight.setLineColor(color2)
    realRiskLine.setPos(riskLineLoc)
    realPracNum.setText(realNum)
    realLossTxt.setPos(lossLoc)
    realLossTxt.setText(lossRounded)
    realGainTxt.setPos(gainLoc)
    realGainTxt.setText(gainRounded)
    realSafeTxt.setPos(safeLoc)
    realSafeTxt.setText(safeRounded)
    realChoiceResp.keys = []
    realChoiceResp.rt = []
    _realChoiceResp_allKeys = []
    # keep track of which components have finished
    realChoicesComponents = [realCircLeft, realCircRight, realRiskLine, realORtxt, realPracNum, realLossTxt, realGainTxt, realSafeTxt, realVleft, realNright, realChoiceResp]
    for thisComponent in realChoicesComponents:
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
    
    # --- Run Routine "realChoices" ---
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
        
        # *realORtxt* updates
        if realORtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realORtxt.frameNStart = frameN  # exact frame index
            realORtxt.tStart = t  # local t and not account for scr refresh
            realORtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realORtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realORtxt.started')
            realORtxt.setAutoDraw(True)
        if realORtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realORtxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realORtxt.tStop = t  # not accounting for scr refresh
                realORtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realORtxt.stopped')
                realORtxt.setAutoDraw(False)
        
        # *realPracNum* updates
        if realPracNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realPracNum.frameNStart = frameN  # exact frame index
            realPracNum.tStart = t  # local t and not account for scr refresh
            realPracNum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realPracNum, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realPracNum.started')
            realPracNum.setAutoDraw(True)
        if realPracNum.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realPracNum.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                realPracNum.tStop = t  # not accounting for scr refresh
                realPracNum.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realPracNum.stopped')
                realPracNum.setAutoDraw(False)
        
        # *realLossTxt* updates
        if realLossTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realLossTxt.frameNStart = frameN  # exact frame index
            realLossTxt.tStart = t  # local t and not account for scr refresh
            realLossTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realLossTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realLossTxt.started')
            realLossTxt.setAutoDraw(True)
        if realLossTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realLossTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realLossTxt.tStop = t  # not accounting for scr refresh
                realLossTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realLossTxt.stopped')
                realLossTxt.setAutoDraw(False)
        
        # *realGainTxt* updates
        if realGainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realGainTxt.frameNStart = frameN  # exact frame index
            realGainTxt.tStart = t  # local t and not account for scr refresh
            realGainTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realGainTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realGainTxt.started')
            realGainTxt.setAutoDraw(True)
        if realGainTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realGainTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realGainTxt.tStop = t  # not accounting for scr refresh
                realGainTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realGainTxt.stopped')
                realGainTxt.setAutoDraw(False)
        
        # *realSafeTxt* updates
        if realSafeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            realSafeTxt.frameNStart = frameN  # exact frame index
            realSafeTxt.tStart = t  # local t and not account for scr refresh
            realSafeTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realSafeTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'realSafeTxt.started')
            realSafeTxt.setAutoDraw(True)
        if realSafeTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > realSafeTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                realSafeTxt.tStop = t  # not accounting for scr refresh
                realSafeTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'realSafeTxt.stopped')
                realSafeTxt.setAutoDraw(False)
        
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in realChoicesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "realChoices" ---
    for thisComponent in realChoicesComponents:
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "realISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    realISIComponents = [isiRealFix]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isiRealFix* updates
        if isiRealFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isiRealFix.frameNStart = frameN  # exact frame index
            isiRealFix.tStart = t  # local t and not account for scr refresh
            isiRealFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isiRealFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isiRealFix.started')
            isiRealFix.setAutoDraw(True)
        if isiRealFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiRealFix.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                isiRealFix.tStop = t  # not accounting for scr refresh
                isiRealFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isiRealFix.stopped')
                isiRealFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "dynaOutcome" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from dynaOCcode
    
    ### Dynamic Trials Outcome
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
        extraITI = 0
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
    
    actualITI = initITIdynamic[dynamicTrials.thisN] #+ extraITI
    
    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLossReal)
    riskygain_values.append(riskyGainReal)
    certain_values.append(certain)
    
    
    
    dynaNoRespTxt.setPos(noRespLoc)
    dynaRiskOC.setPos(ocGambleLoc)
    dynaSafeOC.setPos(ocSafeLoc)
    dynaOCtxt.setColor(color1, colorSpace='rgb')
    dynaOCtxt.setPos(ocLoc)
    dynaOCtxt.setText(feedbackRounded)
    dynaHideRisk.setPos(hideGamLoc)
    # keep track of which components have finished
    dynaOutcomeComponents = [dynaNoRespTxt, dynaRiskOC, dynaSafeOC, dynaOCtxt, dynaHideRisk]
    for thisComponent in dynaOutcomeComponents:
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
    
    # --- Run Routine "dynaOutcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dynaNoRespTxt* updates
        if dynaNoRespTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynaNoRespTxt.frameNStart = frameN  # exact frame index
            dynaNoRespTxt.tStart = t  # local t and not account for scr refresh
            dynaNoRespTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynaNoRespTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynaNoRespTxt.started')
            dynaNoRespTxt.setAutoDraw(True)
        if dynaNoRespTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynaNoRespTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynaNoRespTxt.tStop = t  # not accounting for scr refresh
                dynaNoRespTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynaNoRespTxt.stopped')
                dynaNoRespTxt.setAutoDraw(False)
        
        # *dynaRiskOC* updates
        if dynaRiskOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynaRiskOC.frameNStart = frameN  # exact frame index
            dynaRiskOC.tStart = t  # local t and not account for scr refresh
            dynaRiskOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynaRiskOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynaRiskOC.started')
            dynaRiskOC.setAutoDraw(True)
        if dynaRiskOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynaRiskOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynaRiskOC.tStop = t  # not accounting for scr refresh
                dynaRiskOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynaRiskOC.stopped')
                dynaRiskOC.setAutoDraw(False)
        
        # *dynaSafeOC* updates
        if dynaSafeOC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynaSafeOC.frameNStart = frameN  # exact frame index
            dynaSafeOC.tStart = t  # local t and not account for scr refresh
            dynaSafeOC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynaSafeOC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynaSafeOC.started')
            dynaSafeOC.setAutoDraw(True)
        if dynaSafeOC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynaSafeOC.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynaSafeOC.tStop = t  # not accounting for scr refresh
                dynaSafeOC.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynaSafeOC.stopped')
                dynaSafeOC.setAutoDraw(False)
        
        # *dynaOCtxt* updates
        if dynaOCtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynaOCtxt.frameNStart = frameN  # exact frame index
            dynaOCtxt.tStart = t  # local t and not account for scr refresh
            dynaOCtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynaOCtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynaOCtxt.started')
            dynaOCtxt.setAutoDraw(True)
        if dynaOCtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynaOCtxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynaOCtxt.tStop = t  # not accounting for scr refresh
                dynaOCtxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynaOCtxt.stopped')
                dynaOCtxt.setAutoDraw(False)
        
        # *dynaHideRisk* updates
        if dynaHideRisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dynaHideRisk.frameNStart = frameN  # exact frame index
            dynaHideRisk.tStart = t  # local t and not account for scr refresh
            dynaHideRisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dynaHideRisk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dynaHideRisk.started')
            dynaHideRisk.setAutoDraw(True)
        if dynaHideRisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dynaHideRisk.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dynaHideRisk.tStop = t  # not accounting for scr refresh
                dynaHideRisk.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dynaHideRisk.stopped')
                dynaHideRisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dynaOutcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "dynaOutcome" ---
    for thisComponent in dynaOutcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from dynaOCcode
    
    thisExp.addData('outcomes', outcometmp)
    thisExp.addData('choices', choicetmp)
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "realITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    realITIComponents = [itiRealFix]
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
        
        # *itiRealFix* updates
        if itiRealFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            itiRealFix.frameNStart = frameN  # exact frame index
            itiRealFix.tStart = t  # local t and not account for scr refresh
            itiRealFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(itiRealFix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'itiRealFix.started')
            itiRealFix.setAutoDraw(True)
        if itiRealFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiRealFix.tStartRefresh + actualITI-frameTolerance:
                # keep track of stop time/frame for later
                itiRealFix.tStop = t  # not accounting for scr refresh
                itiRealFix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'itiRealFix.stopped')
                itiRealFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
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


# --- Prepare to start Routine "etStopRecording" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
etStopRecordingComponents = []
for thisComponent in etStopRecordingComponents:
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

# --- Run Routine "etStopRecording" ---
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
    for thisComponent in etStopRecordingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "etStopRecording" ---
for thisComponent in etStopRecordingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from etStopRecCode

### This End Routine stops eye tracker recording

# stop recording; add 100 msec to catch final events before stopping
if doET:
    et.sendMessage('cgeRDM Recording Stopped')
    et.sendMessage('post 100 pause')
    pylink.pumpDelay(100)
    et.stopRecording()
    et.closeDataFile()
    time_str = time.strftime("_%Y_%m_%d_%H_%M_%S", time.localtime())
    session_identifier = edf_fname + time_str
    et.receiveDataFile(edf_fname + '.edf', os.path.join('/Users/Display/Desktop/Github/cge/CGE/RawData/' + session_identifier + '.edf'))
    et.close()



# the Routine "etStopRecording" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cgeRDMend" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
cgeRDMendResp.keys = []
cgeRDMendResp.rt = []
_cgeRDMendResp_allKeys = []
# keep track of which components have finished
cgeRDMendComponents = [cgeRDMendTxt, cgeRDMendResp]
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
    
    # *cgeRDMendTxt* updates
    if cgeRDMendTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cgeRDMendTxt.frameNStart = frameN  # exact frame index
        cgeRDMendTxt.tStart = t  # local t and not account for scr refresh
        cgeRDMendTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cgeRDMendTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cgeRDMendTxt.started')
        cgeRDMendTxt.setAutoDraw(True)
    
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
        routineForceEnded = True
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)
# Run 'End Experiment' code from etCameraSetupCode

### Creating ASC file from EDF
if doET:
    subprocess.run(["edf2asc.exe", os.path.join('/Users/Display/Desktop/Github/cge/CGE/RawData/', session_identifier + '.edf')])

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
#core.quit() 10.3.23