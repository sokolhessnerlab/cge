#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Thu Jun 23 14:38:37 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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
psychopyVersion = '2022.1.4'
expName = 'CogCont'  # from the Builder filename that created this script
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
    originPath='/Users/annarini/Downloads/CGT COG CONT/CogCont_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nOnce "V-Left" and "N-Right" appear on the screen, you may press "V" to select the option on the left and "N" to choose the option on the right.\n\nPress "enter" to move on to the next screen.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inst1 = keyboard.Keyboard()

# Initialize components for Routine "pracStart"
pracStartClock = core.Clock()
startPract = visual.TextStim(win=win, name='startPract',
    text='There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startPracResp = keyboard.Keyboard()

# Initialize components for Routine "practiceTask"
practiceTaskClock = core.Clock()
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

# Initialize components for Routine "isiPrac"
isiPracClock = core.Clock()
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
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

# Initialize components for Routine "itiPrac_2"
itiPrac_2Clock = core.Clock()
itiText = visual.TextStim(win=win, name='itiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "postPrac"
postPracClock = core.Clock()
postPracText = visual.TextStim(win=win, name='postPracText',
    text='Practice complete.\n\nWhen you are ready to start the real task, press "V" or "N".\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
postPractResp = keyboard.Keyboard()

# Initialize components for Routine "realTask"
realTaskClock = core.Clock()
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

# Initialize components for Routine "isiReal"
isiRealClock = core.Clock()
isiTextReal = visual.TextStim(win=win, name='isiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedbackReal"
feedbackRealClock = core.Clock()
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

# Initialize components for Routine "itiReal"
itiRealClock = core.Clock()
itiTextReal = visual.TextStim(win=win, name='itiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "selectOutcome"
selectOutcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Task complete!\n\nRandomly selecting outcome...',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
chooseOC = visual.TextStim(win=win, name='chooseOC',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
exitResponse = keyboard.Keyboard()

# Initialize components for Routine "endOfTask"
endOfTaskClock = core.Clock()
endRedirect = visual.TextStim(win=win, name='endRedirect',
    text='This part of the experiment is complete. \n\nYou will be redirected in a few moments\n to the next part of the study.\n\nThank you.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
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
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
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
        Instructions.setAutoDraw(True)
    
    # *inst1* updates
    waitOnFlip = False
    if inst1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        inst1.frameNStart = frameN  # exact frame index
        inst1.tStart = t  # local t and not account for scr refresh
        inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst1, 'tStartRefresh')  # time at next scr refresh
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

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if inst1.keys in ['', [], None]:  # No response was made
    inst1.keys = None
thisExp.addData('inst1.keys',inst1.keys)
if inst1.keys != None:  # we had a response
    thisExp.addData('inst1.rt', inst1.rt)
thisExp.addData('inst1.started', inst1.tStartRefresh)
thisExp.addData('inst1.stopped', inst1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracStart"-------
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
pracStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracStart"-------
while continueRoutine:
    # get current time
    t = pracStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracStartClock)
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
        startPract.setAutoDraw(True)
    
    # *startPracResp* updates
    waitOnFlip = False
    if startPracResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        startPracResp.frameNStart = frameN  # exact frame index
        startPracResp.tStart = t  # local t and not account for scr refresh
        startPracResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startPracResp, 'tStartRefresh')  # time at next scr refresh
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

# -------Ending Routine "pracStart"-------
for thisComponent in pracStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('startPract.started', startPract.tStartRefresh)
thisExp.addData('startPract.stopped', startPract.tStopRefresh)
# check responses
if startPracResp.keys in ['', [], None]:  # No response was made
    startPracResp.keys = None
thisExp.addData('startPracResp.keys',startPracResp.keys)
if startPracResp.keys != None:  # we had a response
    thisExp.addData('startPracResp.rt', startPracResp.rt)
thisExp.addData('startPracResp.started', startPracResp.tStartRefresh)
thisExp.addData('startPracResp.stopped', startPracResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "pracStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../psychopyResources/capPractice.xlsx'),
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
    
    # ------Prepare to start Routine "practiceTask"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
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
    lossTxt.setText(riskyLoss

)
    gainTxt.setPos(gainLoc)
    gainTxt.setText(riskyGain)
    safeTxt.setPos(safeLoc)
    safeTxt.setText(alternative)
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
    practiceTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceTask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceTaskClock)
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
            circleLeft.setAutoDraw(True)
        if circleLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleLeft.tStop = t  # not accounting for scr refresh
                circleLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circleLeft, 'tStopRefresh')  # time at next scr refresh
                circleLeft.setAutoDraw(False)
        
        # *circleRight* updates
        if circleRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circleRight.frameNStart = frameN  # exact frame index
            circleRight.tStart = t  # local t and not account for scr refresh
            circleRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleRight, 'tStartRefresh')  # time at next scr refresh
            circleRight.setAutoDraw(True)
        if circleRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleRight.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleRight.tStop = t  # not accounting for scr refresh
                circleRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circleRight, 'tStopRefresh')  # time at next scr refresh
                circleRight.setAutoDraw(False)
        
        # *lineLeft* updates
        if lineLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lineLeft.frameNStart = frameN  # exact frame index
            lineLeft.tStart = t  # local t and not account for scr refresh
            lineLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lineLeft, 'tStartRefresh')  # time at next scr refresh
            lineLeft.setAutoDraw(True)
        if lineLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lineLeft.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lineLeft.tStop = t  # not accounting for scr refresh
                lineLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lineLeft, 'tStopRefresh')  # time at next scr refresh
                lineLeft.setAutoDraw(False)
        
        # *orText* updates
        if orText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            orText.frameNStart = frameN  # exact frame index
            orText.tStart = t  # local t and not account for scr refresh
            orText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orText, 'tStartRefresh')  # time at next scr refresh
            orText.setAutoDraw(True)
        if orText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > orText.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                orText.tStop = t  # not accounting for scr refresh
                orText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(orText, 'tStopRefresh')  # time at next scr refresh
                orText.setAutoDraw(False)
        
        # *lossTxt* updates
        if lossTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lossTxt.frameNStart = frameN  # exact frame index
            lossTxt.tStart = t  # local t and not account for scr refresh
            lossTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lossTxt, 'tStartRefresh')  # time at next scr refresh
            lossTxt.setAutoDraw(True)
        if lossTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lossTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lossTxt.tStop = t  # not accounting for scr refresh
                lossTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lossTxt, 'tStopRefresh')  # time at next scr refresh
                lossTxt.setAutoDraw(False)
        
        # *gainTxt* updates
        if gainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gainTxt.frameNStart = frameN  # exact frame index
            gainTxt.tStart = t  # local t and not account for scr refresh
            gainTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gainTxt, 'tStartRefresh')  # time at next scr refresh
            gainTxt.setAutoDraw(True)
        if gainTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gainTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                gainTxt.tStop = t  # not accounting for scr refresh
                gainTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gainTxt, 'tStopRefresh')  # time at next scr refresh
                gainTxt.setAutoDraw(False)
        
        # *safeTxt* updates
        if safeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeTxt.frameNStart = frameN  # exact frame index
            safeTxt.tStart = t  # local t and not account for scr refresh
            safeTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeTxt, 'tStartRefresh')  # time at next scr refresh
            safeTxt.setAutoDraw(True)
        if safeTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > safeTxt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                safeTxt.tStop = t  # not accounting for scr refresh
                safeTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(safeTxt, 'tStopRefresh')  # time at next scr refresh
                safeTxt.setAutoDraw(False)
        
        # *vLeft* updates
        if vLeft.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            vLeft.frameNStart = frameN  # exact frame index
            vLeft.tStart = t  # local t and not account for scr refresh
            vLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vLeft, 'tStartRefresh')  # time at next scr refresh
            vLeft.setAutoDraw(True)
        if vLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vLeft.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vLeft.tStop = t  # not accounting for scr refresh
                vLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(vLeft, 'tStopRefresh')  # time at next scr refresh
                vLeft.setAutoDraw(False)
        
        # *nRight* updates
        if nRight.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nRight.frameNStart = frameN  # exact frame index
            nRight.tStart = t  # local t and not account for scr refresh
            nRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nRight, 'tStartRefresh')  # time at next scr refresh
            nRight.setAutoDraw(True)
        if nRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nRight.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                nRight.tStop = t  # not accounting for scr refresh
                nRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nRight, 'tStopRefresh')  # time at next scr refresh
                nRight.setAutoDraw(False)
        
        # *choice1* updates
        waitOnFlip = False
        if choice1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            choice1.frameNStart = frameN  # exact frame index
            choice1.tStart = t  # local t and not account for scr refresh
            choice1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice1, 'tStartRefresh')  # time at next scr refresh
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
                win.timeOnFlip(choice1, 'tStopRefresh')  # time at next scr refresh
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
    
    # -------Ending Routine "practiceTask"-------
    for thisComponent in practiceTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('circleLeft.started', circleLeft.tStartRefresh)
    trials.addData('circleLeft.stopped', circleLeft.tStopRefresh)
    trials.addData('circleRight.started', circleRight.tStartRefresh)
    trials.addData('circleRight.stopped', circleRight.tStopRefresh)
    trials.addData('lineLeft.started', lineLeft.tStartRefresh)
    trials.addData('lineLeft.stopped', lineLeft.tStopRefresh)
    trials.addData('orText.started', orText.tStartRefresh)
    trials.addData('orText.stopped', orText.tStopRefresh)
    trials.addData('lossTxt.started', lossTxt.tStartRefresh)
    trials.addData('lossTxt.stopped', lossTxt.tStopRefresh)
    trials.addData('gainTxt.started', gainTxt.tStartRefresh)
    trials.addData('gainTxt.stopped', gainTxt.tStopRefresh)
    trials.addData('safeTxt.started', safeTxt.tStartRefresh)
    trials.addData('safeTxt.stopped', safeTxt.tStopRefresh)
    trials.addData('vLeft.started', vLeft.tStartRefresh)
    trials.addData('vLeft.stopped', vLeft.tStopRefresh)
    trials.addData('nRight.started', nRight.tStartRefresh)
    trials.addData('nRight.stopped', nRight.tStopRefresh)
    # check responses
    if choice1.keys in ['', [], None]:  # No response was made
        choice1.keys = None
    trials.addData('choice1.keys',choice1.keys)
    if choice1.keys != None:  # we had a response
        trials.addData('choice1.rt', choice1.rt)
    trials.addData('choice1.started', choice1.tStartRefresh)
    trials.addData('choice1.stopped', choice1.tStopRefresh)
    
    # ------Prepare to start Routine "isiPrac"-------
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
    isiPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isiPrac"-------
    while continueRoutine:
        # get current time
        t = isiPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiPracClock)
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
            isiText.setAutoDraw(True)
        if isiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiText.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiText.tStop = t  # not accounting for scr refresh
                isiText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isiText, 'tStopRefresh')  # time at next scr refresh
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
    
    # -------Ending Routine "isiPrac"-------
    for thisComponent in isiPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('isiText.started', isiText.tStartRefresh)
    trials.addData('isiText.stopped', isiText.tStopRefresh)
    # the Routine "isiPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
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
    outcomeText.setText(outcome)
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
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
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
            noRespTxt.setAutoDraw(True)
        if noRespTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noRespTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                noRespTxt.tStop = t  # not accounting for scr refresh
                noRespTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noRespTxt, 'tStopRefresh')  # time at next scr refresh
                noRespTxt.setAutoDraw(False)
        
        # *ocGamble* updates
        if ocGamble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocGamble.frameNStart = frameN  # exact frame index
            ocGamble.tStart = t  # local t and not account for scr refresh
            ocGamble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocGamble, 'tStartRefresh')  # time at next scr refresh
            ocGamble.setAutoDraw(True)
        if ocGamble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocGamble.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocGamble.tStop = t  # not accounting for scr refresh
                ocGamble.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ocGamble, 'tStopRefresh')  # time at next scr refresh
                ocGamble.setAutoDraw(False)
        
        # *ocSafe* updates
        if ocSafe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocSafe.frameNStart = frameN  # exact frame index
            ocSafe.tStart = t  # local t and not account for scr refresh
            ocSafe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocSafe, 'tStartRefresh')  # time at next scr refresh
            ocSafe.setAutoDraw(True)
        if ocSafe.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocSafe.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocSafe.tStop = t  # not accounting for scr refresh
                ocSafe.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ocSafe, 'tStopRefresh')  # time at next scr refresh
                ocSafe.setAutoDraw(False)
        
        # *outcomeText* updates
        if outcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcomeText.frameNStart = frameN  # exact frame index
            outcomeText.tStart = t  # local t and not account for scr refresh
            outcomeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcomeText, 'tStartRefresh')  # time at next scr refresh
            outcomeText.setAutoDraw(True)
        if outcomeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcomeText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                outcomeText.tStop = t  # not accounting for scr refresh
                outcomeText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(outcomeText, 'tStopRefresh')  # time at next scr refresh
                outcomeText.setAutoDraw(False)
        
        # *hideGamble* updates
        if hideGamble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hideGamble.frameNStart = frameN  # exact frame index
            hideGamble.tStart = t  # local t and not account for scr refresh
            hideGamble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hideGamble, 'tStartRefresh')  # time at next scr refresh
            hideGamble.setAutoDraw(True)
        if hideGamble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hideGamble.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hideGamble.tStop = t  # not accounting for scr refresh
                hideGamble.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hideGamble, 'tStopRefresh')  # time at next scr refresh
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
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('outcome', outcome)
    trials.addData('noRespTxt.started', noRespTxt.tStartRefresh)
    trials.addData('noRespTxt.stopped', noRespTxt.tStopRefresh)
    trials.addData('ocGamble.started', ocGamble.tStartRefresh)
    trials.addData('ocGamble.stopped', ocGamble.tStopRefresh)
    trials.addData('ocSafe.started', ocSafe.tStartRefresh)
    trials.addData('ocSafe.stopped', ocSafe.tStopRefresh)
    trials.addData('outcomeText.started', outcomeText.tStartRefresh)
    trials.addData('outcomeText.stopped', outcomeText.tStopRefresh)
    trials.addData('hideGamble.started', hideGamble.tStartRefresh)
    trials.addData('hideGamble.stopped', hideGamble.tStopRefresh)
    
    # ------Prepare to start Routine "itiPrac_2"-------
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
    itiPrac_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "itiPrac_2"-------
    while continueRoutine:
        # get current time
        t = itiPrac_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiPrac_2Clock)
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
            itiText.setAutoDraw(True)
        if itiText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiText.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                itiText.tStop = t  # not accounting for scr refresh
                itiText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(itiText, 'tStopRefresh')  # time at next scr refresh
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
    
    # -------Ending Routine "itiPrac_2"-------
    for thisComponent in itiPrac_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('itiText.started', itiText.tStartRefresh)
    trials.addData('itiText.stopped', itiText.tStopRefresh)
    # the Routine "itiPrac_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "postPrac"-------
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
postPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "postPrac"-------
while continueRoutine:
    # get current time
    t = postPracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=postPracClock)
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
        postPracText.setAutoDraw(True)
    
    # *postPractResp* updates
    waitOnFlip = False
    if postPractResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postPractResp.frameNStart = frameN  # exact frame index
        postPractResp.tStart = t  # local t and not account for scr refresh
        postPractResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postPractResp, 'tStartRefresh')  # time at next scr refresh
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

# -------Ending Routine "postPrac"-------
for thisComponent in postPracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('postPracText.started', postPracText.tStartRefresh)
thisExp.addData('postPracText.stopped', postPracText.tStopRefresh)
# check responses
if postPractResp.keys in ['', [], None]:  # No response was made
    postPractResp.keys = None
thisExp.addData('postPractResp.keys',postPractResp.keys)
if postPractResp.keys != None:  # we had a response
    thisExp.addData('postPractResp.rt', postPractResp.rt)
thisExp.addData('postPractResp.started', postPractResp.tStartRefresh)
thisExp.addData('postPractResp.stopped', postPractResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "postPrac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
realTrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('capChoiceSets/1.csv', selection='0:6'),
    seed=None, name='realTrials')
thisExp.addLoop(realTrials)  # add the loop to the experiment
thisRealTrial = realTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRealTrial.rgb)
if thisRealTrial != None:
    for paramName in thisRealTrial:
        exec('{} = thisRealTrial[paramName]'.format(paramName))

for thisRealTrial in realTrials:
    currentLoop = realTrials
    # abbreviate parameter names if possible (e.g. rgb = thisRealTrial.rgb)
    if thisRealTrial != None:
        for paramName in thisRealTrial:
            exec('{} = thisRealTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "realTask"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
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
    lossTxtReal.setText(riskyLoss)
    gainTxtReal.setPos(gainLoc)
    gainTxtReal.setText(riskyGain)
    safeTxtReal.setPos(safeLoc)
    safeTxtReal.setText(alternative)
    realChoice.keys = []
    realChoice.rt = []
    _realChoice_allKeys = []
    # keep track of which components have finished
    realTaskComponents = [circleLeftReal, circleRightReal, lineLeftReal, orTextReal, lossTxtReal, gainTxtReal, safeTxtReal, vLeftReal, nRightReal, realChoice]
    for thisComponent in realTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    realTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "realTask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = realTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=realTaskClock)
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
            circleLeftReal.setAutoDraw(True)
        if circleLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleLeftReal.tStop = t  # not accounting for scr refresh
                circleLeftReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circleLeftReal, 'tStopRefresh')  # time at next scr refresh
                circleLeftReal.setAutoDraw(False)
        
        # *circleRightReal* updates
        if circleRightReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circleRightReal.frameNStart = frameN  # exact frame index
            circleRightReal.tStart = t  # local t and not account for scr refresh
            circleRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circleRightReal, 'tStartRefresh')  # time at next scr refresh
            circleRightReal.setAutoDraw(True)
        if circleRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circleRightReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                circleRightReal.tStop = t  # not accounting for scr refresh
                circleRightReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(circleRightReal, 'tStopRefresh')  # time at next scr refresh
                circleRightReal.setAutoDraw(False)
        
        # *lineLeftReal* updates
        if lineLeftReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lineLeftReal.frameNStart = frameN  # exact frame index
            lineLeftReal.tStart = t  # local t and not account for scr refresh
            lineLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lineLeftReal, 'tStartRefresh')  # time at next scr refresh
            lineLeftReal.setAutoDraw(True)
        if lineLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lineLeftReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lineLeftReal.tStop = t  # not accounting for scr refresh
                lineLeftReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lineLeftReal, 'tStopRefresh')  # time at next scr refresh
                lineLeftReal.setAutoDraw(False)
        
        # *orTextReal* updates
        if orTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            orTextReal.frameNStart = frameN  # exact frame index
            orTextReal.tStart = t  # local t and not account for scr refresh
            orTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orTextReal, 'tStartRefresh')  # time at next scr refresh
            orTextReal.setAutoDraw(True)
        if orTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > orTextReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                orTextReal.tStop = t  # not accounting for scr refresh
                orTextReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(orTextReal, 'tStopRefresh')  # time at next scr refresh
                orTextReal.setAutoDraw(False)
        
        # *lossTxtReal* updates
        if lossTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lossTxtReal.frameNStart = frameN  # exact frame index
            lossTxtReal.tStart = t  # local t and not account for scr refresh
            lossTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lossTxtReal, 'tStartRefresh')  # time at next scr refresh
            lossTxtReal.setAutoDraw(True)
        if lossTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lossTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                lossTxtReal.tStop = t  # not accounting for scr refresh
                lossTxtReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lossTxtReal, 'tStopRefresh')  # time at next scr refresh
                lossTxtReal.setAutoDraw(False)
        
        # *gainTxtReal* updates
        if gainTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gainTxtReal.frameNStart = frameN  # exact frame index
            gainTxtReal.tStart = t  # local t and not account for scr refresh
            gainTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gainTxtReal, 'tStartRefresh')  # time at next scr refresh
            gainTxtReal.setAutoDraw(True)
        if gainTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gainTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                gainTxtReal.tStop = t  # not accounting for scr refresh
                gainTxtReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gainTxtReal, 'tStopRefresh')  # time at next scr refresh
                gainTxtReal.setAutoDraw(False)
        
        # *safeTxtReal* updates
        if safeTxtReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            safeTxtReal.frameNStart = frameN  # exact frame index
            safeTxtReal.tStart = t  # local t and not account for scr refresh
            safeTxtReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(safeTxtReal, 'tStartRefresh')  # time at next scr refresh
            safeTxtReal.setAutoDraw(True)
        if safeTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > safeTxtReal.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                safeTxtReal.tStop = t  # not accounting for scr refresh
                safeTxtReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(safeTxtReal, 'tStopRefresh')  # time at next scr refresh
                safeTxtReal.setAutoDraw(False)
        
        # *vLeftReal* updates
        if vLeftReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            vLeftReal.frameNStart = frameN  # exact frame index
            vLeftReal.tStart = t  # local t and not account for scr refresh
            vLeftReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vLeftReal, 'tStartRefresh')  # time at next scr refresh
            vLeftReal.setAutoDraw(True)
        if vLeftReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vLeftReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vLeftReal.tStop = t  # not accounting for scr refresh
                vLeftReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(vLeftReal, 'tStopRefresh')  # time at next scr refresh
                vLeftReal.setAutoDraw(False)
        
        # *nRightReal* updates
        if nRightReal.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            nRightReal.frameNStart = frameN  # exact frame index
            nRightReal.tStart = t  # local t and not account for scr refresh
            nRightReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nRightReal, 'tStartRefresh')  # time at next scr refresh
            nRightReal.setAutoDraw(True)
        if nRightReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nRightReal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                nRightReal.tStop = t  # not accounting for scr refresh
                nRightReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nRightReal, 'tStopRefresh')  # time at next scr refresh
                nRightReal.setAutoDraw(False)
        
        # *realChoice* updates
        waitOnFlip = False
        if realChoice.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            realChoice.frameNStart = frameN  # exact frame index
            realChoice.tStart = t  # local t and not account for scr refresh
            realChoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(realChoice, 'tStartRefresh')  # time at next scr refresh
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
                win.timeOnFlip(realChoice, 'tStopRefresh')  # time at next scr refresh
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
        for thisComponent in realTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "realTask"-------
    for thisComponent in realTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    realTrials.addData('circleLeftReal.started', circleLeftReal.tStartRefresh)
    realTrials.addData('circleLeftReal.stopped', circleLeftReal.tStopRefresh)
    realTrials.addData('circleRightReal.started', circleRightReal.tStartRefresh)
    realTrials.addData('circleRightReal.stopped', circleRightReal.tStopRefresh)
    realTrials.addData('lineLeftReal.started', lineLeftReal.tStartRefresh)
    realTrials.addData('lineLeftReal.stopped', lineLeftReal.tStopRefresh)
    realTrials.addData('orTextReal.started', orTextReal.tStartRefresh)
    realTrials.addData('orTextReal.stopped', orTextReal.tStopRefresh)
    realTrials.addData('lossTxtReal.started', lossTxtReal.tStartRefresh)
    realTrials.addData('lossTxtReal.stopped', lossTxtReal.tStopRefresh)
    realTrials.addData('gainTxtReal.started', gainTxtReal.tStartRefresh)
    realTrials.addData('gainTxtReal.stopped', gainTxtReal.tStopRefresh)
    realTrials.addData('safeTxtReal.started', safeTxtReal.tStartRefresh)
    realTrials.addData('safeTxtReal.stopped', safeTxtReal.tStopRefresh)
    realTrials.addData('vLeftReal.started', vLeftReal.tStartRefresh)
    realTrials.addData('vLeftReal.stopped', vLeftReal.tStopRefresh)
    realTrials.addData('nRightReal.started', nRightReal.tStartRefresh)
    realTrials.addData('nRightReal.stopped', nRightReal.tStopRefresh)
    # check responses
    if realChoice.keys in ['', [], None]:  # No response was made
        realChoice.keys = None
    realTrials.addData('realChoice.keys',realChoice.keys)
    if realChoice.keys != None:  # we had a response
        realTrials.addData('realChoice.rt', realChoice.rt)
    realTrials.addData('realChoice.started', realChoice.tStartRefresh)
    realTrials.addData('realChoice.stopped', realChoice.tStopRefresh)
    
    # ------Prepare to start Routine "isiReal"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isiRealComponents = [isiTextReal]
    for thisComponent in isiRealComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiRealClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isiReal"-------
    while continueRoutine:
        # get current time
        t = isiRealClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiRealClock)
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
            isiTextReal.setAutoDraw(True)
        if isiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isiTextReal.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isiTextReal.tStop = t  # not accounting for scr refresh
                isiTextReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isiTextReal, 'tStopRefresh')  # time at next scr refresh
                isiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiRealComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isiReal"-------
    for thisComponent in isiRealComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    realTrials.addData('isiTextReal.started', isiTextReal.tStartRefresh)
    realTrials.addData('isiTextReal.stopped', isiTextReal.tStopRefresh)
    # the Routine "isiReal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackReal"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    import random
    if not realChoice.keys:
        realOutcome = " "
        noRespLoc = [0,0]
        ocLoc = [5,5]
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 1:
        realOutcome = random.choice([riskyGain, riskyLoss])
        if realOutcome == riskyGain:
            ocLoc = [-.4,.1]
            ocGambleLoc = [-.4,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.4,-.125]
        elif realOutcome == riskyLoss:
             ocLoc = [-.4,-.1]
             ocGambleLoc = [-.4,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.4,.125]
             noRespLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 2:
        realOutcome = alternative
        ocLoc = [-.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==1:
        realOutcome = alternative
        ocLoc = [.4,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif realChoice.keys == 'n' and loc ==2:
        realOutcome = random.choice([riskyGain, riskyLoss])
        if realOutcome == riskyGain:
            ocLoc = [.4,.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,-.125]
            noRespLoc = [5,5]
        elif realOutcome == riskyLoss:
            ocLoc = [.4,-.1]
            ocGambleLoc = [.4,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.4,.125]
            noRespLoc = [5,5]
    
    
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    outcomeTextReal.setColor('black', colorSpace='rgb')
    outcomeTextReal.setPos(ocLoc)
    outcomeTextReal.setText(realOutcome)
    hideGambleReal.setPos(hideGamLoc)
    # keep track of which components have finished
    feedbackRealComponents = [noRespTxtReal, ocGambleReal, ocSafeReal, outcomeTextReal, hideGambleReal]
    for thisComponent in feedbackRealComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackRealClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackReal"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackRealClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackRealClock)
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
            noRespTxtReal.setAutoDraw(True)
        if noRespTxtReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noRespTxtReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                noRespTxtReal.tStop = t  # not accounting for scr refresh
                noRespTxtReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noRespTxtReal, 'tStopRefresh')  # time at next scr refresh
                noRespTxtReal.setAutoDraw(False)
        
        # *ocGambleReal* updates
        if ocGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocGambleReal.frameNStart = frameN  # exact frame index
            ocGambleReal.tStart = t  # local t and not account for scr refresh
            ocGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocGambleReal, 'tStartRefresh')  # time at next scr refresh
            ocGambleReal.setAutoDraw(True)
        if ocGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocGambleReal.tStop = t  # not accounting for scr refresh
                ocGambleReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ocGambleReal, 'tStopRefresh')  # time at next scr refresh
                ocGambleReal.setAutoDraw(False)
        
        # *ocSafeReal* updates
        if ocSafeReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ocSafeReal.frameNStart = frameN  # exact frame index
            ocSafeReal.tStart = t  # local t and not account for scr refresh
            ocSafeReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ocSafeReal, 'tStartRefresh')  # time at next scr refresh
            ocSafeReal.setAutoDraw(True)
        if ocSafeReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ocSafeReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ocSafeReal.tStop = t  # not accounting for scr refresh
                ocSafeReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ocSafeReal, 'tStopRefresh')  # time at next scr refresh
                ocSafeReal.setAutoDraw(False)
        
        # *outcomeTextReal* updates
        if outcomeTextReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcomeTextReal.frameNStart = frameN  # exact frame index
            outcomeTextReal.tStart = t  # local t and not account for scr refresh
            outcomeTextReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcomeTextReal, 'tStartRefresh')  # time at next scr refresh
            outcomeTextReal.setAutoDraw(True)
        if outcomeTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcomeTextReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                outcomeTextReal.tStop = t  # not accounting for scr refresh
                outcomeTextReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(outcomeTextReal, 'tStopRefresh')  # time at next scr refresh
                outcomeTextReal.setAutoDraw(False)
        
        # *hideGambleReal* updates
        if hideGambleReal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hideGambleReal.frameNStart = frameN  # exact frame index
            hideGambleReal.tStart = t  # local t and not account for scr refresh
            hideGambleReal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hideGambleReal, 'tStartRefresh')  # time at next scr refresh
            hideGambleReal.setAutoDraw(True)
        if hideGambleReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hideGambleReal.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                hideGambleReal.tStop = t  # not accounting for scr refresh
                hideGambleReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hideGambleReal, 'tStopRefresh')  # time at next scr refresh
                hideGambleReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackRealComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackReal"-------
    for thisComponent in feedbackRealComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('realOutcome', realOutcome)
    realTrials.addData('noRespTxtReal.started', noRespTxtReal.tStartRefresh)
    realTrials.addData('noRespTxtReal.stopped', noRespTxtReal.tStopRefresh)
    realTrials.addData('ocGambleReal.started', ocGambleReal.tStartRefresh)
    realTrials.addData('ocGambleReal.stopped', ocGambleReal.tStopRefresh)
    realTrials.addData('ocSafeReal.started', ocSafeReal.tStartRefresh)
    realTrials.addData('ocSafeReal.stopped', ocSafeReal.tStopRefresh)
    realTrials.addData('outcomeTextReal.started', outcomeTextReal.tStartRefresh)
    realTrials.addData('outcomeTextReal.stopped', outcomeTextReal.tStopRefresh)
    realTrials.addData('hideGambleReal.started', hideGambleReal.tStartRefresh)
    realTrials.addData('hideGambleReal.stopped', hideGambleReal.tStopRefresh)
    
    # ------Prepare to start Routine "itiReal"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiRealComponents = [itiTextReal]
    for thisComponent in itiRealComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiRealClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "itiReal"-------
    while continueRoutine:
        # get current time
        t = itiRealClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiRealClock)
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
            itiTextReal.setAutoDraw(True)
        if itiTextReal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > itiTextReal.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                itiTextReal.tStop = t  # not accounting for scr refresh
                itiTextReal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(itiTextReal, 'tStopRefresh')  # time at next scr refresh
                itiTextReal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiRealComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "itiReal"-------
    for thisComponent in itiRealComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    realTrials.addData('itiTextReal.started', itiTextReal.tStartRefresh)
    realTrials.addData('itiTextReal.stopped', itiTextReal.tStopRefresh)
    # the Routine "itiReal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'realTrials'


# ------Prepare to start Routine "selectOutcome"-------
continueRoutine = True
# update component parameters for each repeat
finiteOutcomes = 9
outcome2payFull = 9999;
outcome2payScaled = 1234;

wrapUpText = "Randomly selected outcome: ${} \n\nYou will be paid an additional: ${} \n\nPress the 'space' bar when you are ready to proceed".format(outcome2payFull, outcome2payScaled);

chooseOC.setText(wrapUpText)
exitResponse.keys = []
exitResponse.rt = []
_exitResponse_allKeys = []
# keep track of which components have finished
selectOutcomeComponents = [text, chooseOC, exitResponse]
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
selectOutcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "selectOutcome"-------
while continueRoutine:
    # get current time
    t = selectOutcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=selectOutcomeClock)
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
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *chooseOC* updates
    if chooseOC.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        chooseOC.frameNStart = frameN  # exact frame index
        chooseOC.tStart = t  # local t and not account for scr refresh
        chooseOC.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(chooseOC, 'tStartRefresh')  # time at next scr refresh
        chooseOC.setAutoDraw(True)
    
    # *exitResponse* updates
    waitOnFlip = False
    if exitResponse.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        exitResponse.frameNStart = frameN  # exact frame index
        exitResponse.tStart = t  # local t and not account for scr refresh
        exitResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exitResponse, 'tStartRefresh')  # time at next scr refresh
        exitResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exitResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exitResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exitResponse.status == STARTED and not waitOnFlip:
        theseKeys = exitResponse.getKeys(keyList=['space'], waitRelease=False)
        _exitResponse_allKeys.extend(theseKeys)
        if len(_exitResponse_allKeys):
            exitResponse.keys = _exitResponse_allKeys[-1].name  # just the last key pressed
            exitResponse.rt = _exitResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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

# -------Ending Routine "selectOutcome"-------
for thisComponent in selectOutcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('finiteOutcomes', finiteOutcomes);
thisExp.addData('outcome2payFull', outcome2payFull);
thisExp.addData('outcome2payScaled', outcome2payScaled);

thisExp.addData('chooseOC.started', chooseOC.tStartRefresh)
thisExp.addData('chooseOC.stopped', chooseOC.tStopRefresh)
# check responses
if exitResponse.keys in ['', [], None]:  # No response was made
    exitResponse.keys = None
thisExp.addData('exitResponse.keys',exitResponse.keys)
if exitResponse.keys != None:  # we had a response
    thisExp.addData('exitResponse.rt', exitResponse.rt)
thisExp.addData('exitResponse.started', exitResponse.tStartRefresh)
thisExp.addData('exitResponse.stopped', exitResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "selectOutcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "endOfTask"-------
continueRoutine = True
routineTimer.add(10.000000)
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
endOfTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endOfTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endOfTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endOfTaskClock)
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
        endRedirect.setAutoDraw(True)
    if endRedirect.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endRedirect.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            endRedirect.tStop = t  # not accounting for scr refresh
            endRedirect.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endRedirect, 'tStopRefresh')  # time at next scr refresh
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

# -------Ending Routine "endOfTask"-------
for thisComponent in endOfTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endRedirect.started', endRedirect.tStartRefresh)
thisExp.addData('endRedirect.stopped', endRedirect.tStopRefresh)

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
