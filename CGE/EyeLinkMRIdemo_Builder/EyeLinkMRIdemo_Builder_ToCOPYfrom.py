#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on May 09, 2023, at 13:28
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

# Run 'Before Experiment' code from elConnect
# DESCRIPTION:
# This is a basic example illustrating how to do continuous eye tracker 
# recording through a block of trials (e.g., in an MRI setup), and how to 
# synchronize the presentation of trials with a sync signal from the MRI. With 
# a long recording, we start and stop recording at the beginning and end of a 
# testing session (block/run), rather than at the beginning and end of each 
# experimental trial. We still send the TRIALID and TRIAL_RESULT messages to 
# the tracker, and Data Viewer will still be able to segment the long recording 
# into small segments (trials).

# The code components in the eyelinkSetup, eyelinkStartRecording, trial, and 
# eyelinkStopRecording routines handle communication with the Host PC/EyeLink
# system.  All the code components are set to Code Type Py, and each code 
# component may have code in the various tabs (e.g., Before Experiment, Begin
# Experiment, etc.)

# Last updated: March 7 2023

# This Before Experiment tab of the elConnect component imports some
# modules we need, manages data filenames, allows for dummy mode configuration
# (for testing), connects to the Host PC, configures some tracker settings,
# and defines some helper function definitions (which are called later)

import pylink
import time
import platform
from PIL import Image  # for preparing the Host backdrop image
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from string import ascii_letters, digits

# Switch to the script folder
script_path = os.path.dirname(sys.argv[0])
if len(script_path) != 0:
    os.chdir(script_path)


# Set this variable to True if you use the built-in retina screen as your
# primary display device on macOS. If have an external monitor, set this
# variable True if you choose to "Optimize for Built-in Retina Display"
# in the Displays preference settings.
use_retina = False

# Set this variable to True to run the script in "Dummy Mode"
dummy_mode = False

# Prompt user to specify an EDF data filename
# before we open a fullscreen window
dlg_title = 'Enter EDF File Name'
dlg_prompt = 'Please enter a file name with 8 or fewer characters\n' + \
             '[letters, numbers, and underscore].'


# Set up EDF data file name and local data folder
#
# The EDF data filename should not exceed 8 alphanumeric characters
# use ONLY number 0-9, letters, & _ (underscore) in the filename
edf_fname = 'TEST'

# Prompt user to specify an EDF data filename
# before we open a fullscreen window
dlg_title = 'Enter EDF File Name'
dlg_prompt = 'Please enter a file name with 8 or fewer characters\n' + \
             '[letters, numbers, and underscore].'

# loop until we get a valid filename
while True:
    dlg = gui.Dlg(dlg_title)
    dlg.addText(dlg_prompt)
    dlg.addField('File Name:', edf_fname)
    # show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:  # if ok_data is not None
        print('EDF data filename: {}'.format(ok_data[0]))
    else:
        print('user cancelled')
        core.quit()
        sys.exit()

    # get the string entered by the experimenter
    tmp_str = dlg.data[0]
    # strip trailing characters, ignore the ".edf" extension
    edf_fname = tmp_str.rstrip().split('.')[0]

    # check if the filename is valid (length <= 8 & no special char)
    allowed_char = ascii_letters + digits + '_'
    if not all([c in allowed_char for c in edf_fname]):
        print('ERROR: Invalid EDF filename')
    elif len(edf_fname) > 8:
        print('ERROR: EDF filename should not exceed 8 characters')
    else:
        break
        
# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = edf_fname + time_str

# create a folder for the current testing session in the "results" folder
session_folder = os.path.join(results_folder, session_identifier)
if not os.path.exists(session_folder):
    os.makedirs(session_folder)

# For macOS users check if they have a retina screen
if 'Darwin' in platform.system():
        dlg = gui.Dlg("Retina Screen?", labelButtonOK='Yes', labelButtonCancel='No')
        dlg.addText("Does your Mac have a Retina screen?")
        # show dialog and wait for OK or Cancel
        ok_data = dlg.show()
        if dlg.OK:  # if ok_data is not None
            use_retina = True
        else:
            use_retina = False
    
# Step 1: Connect to the EyeLink Host PC
#
# The Host IP address, by default, is "100.1.1.1".
# the "el_tracker" objected created here can be accessed through the Pylink
# Set the Host PC address to "None" (without quotes) to run the script
# in "Dummy Mode"
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except RuntimeError as error:
        dlg = gui.Dlg("Dummy Mode?")
        dlg.addText("Couldn't connect to tracker at 100.1.1.1 -- continue in Dummy Mode?")
        # show dialog and wait for OK or Cancel
        ok_data = dlg.show()
        if dlg.OK:  # if ok_data is not None
            #print('EDF data filename: {}'.format(ok_data[0]))
            dummy_mode = True
            el_tracker = pylink.EyeLink(None)
        else:
            print('user cancelled')
            core.quit()
            sys.exit()

# Step 2: Open an EDF data file on the Host PC
edf_file = edf_fname + ".EDF"
try:
    el_tracker.openDataFile(edf_file)
except RuntimeError as err:
    print('ERROR:', err)
    # close the link if we have one open
    if el_tracker.isConnected():
        el_tracker.close()
    core.quit()
    sys.exit()

# Add a header text to the EDF file to identify the current experiment name
# This is OPTIONAL. If your text starts with "RECORDED BY " it will be
# available in DataViewer's Inspector window by clicking
# the EDF session node in the top panel and looking for the "Recorded By:"
# field in the bottom panel of the Inspector.
preamble_text = 'RECORDED BY %s' % os.path.basename(__file__)
el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)

# Step 3: Configure the tracker
#
# Put the tracker in offline mode before we change tracking parameters
el_tracker.setOfflineMode()

# Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
# 5-EyeLink 1000 Plus, 6-Portable DUO
eyelink_ver = 0  # set version to 0, in case running in Dummy mode
if not dummy_mode:
    vstr = el_tracker.getTrackerVersionString()
    eyelink_ver = int(vstr.split()[-1].split('.')[0])
    # print out some version info in the shell
    print('Running experiment on %s, version %d' % (vstr, eyelink_ver))

# File and Link data control
# what eye events to save in the EDF file, include everything by default
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# what eye events to make available over the link, include everything by default
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
# what sample data to save in the EDF data file and to make available
# over the link, include the 'HTARGET' flag to save head target sticker
# data for supported eye trackers
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)

# Optional tracking parameters
# Sample rate, 250, 500, 1000, or 2000, check your tracker specification
# if eyelink_ver > 2:
#     el_tracker.sendCommand("sample_rate 1000")
# Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
el_tracker.sendCommand("calibration_type = HV9")
# Set a gamepad button to accept calibration/drift check target
# You need a supported gamepad/button box that is connected to the Host PC
el_tracker.sendCommand("button_function 5 'accept_target_fixation'")

def clear_screen(win):
    """ clear up the PsychoPy window"""
    win.fillColor = genv.getBackgroundColor()
    win.flip()

def show_msg(win, text, wait_for_keypress=True):
    """ Show task instructions on screen"""

    msg = visual.TextStim(win, text,
                          color=genv.getForegroundColor(),
                          wrapWidth=scn_width/2)
    clear_screen(win)
    msg.draw()
    win.flip()

    # wait indefinitely, terminates upon any key press
    if wait_for_keypress:
        event.waitKeys()
        clear_screen(win)

def terminate_task():
    """ Terminate the task gracefully and retrieve the EDF data file
    """
    el_tracker = pylink.getEYELINK()

    if el_tracker.isConnected():
        # Terminate the current trial first if the task terminated prematurely
        error = el_tracker.isRecording()
        if error == pylink.TRIAL_OK:
            abort_trial()

        # Put tracker in Offline mode
        el_tracker.setOfflineMode()

        # Clear the Host PC screen and wait for 500 ms
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)

        # Close the edf data file on the Host
        el_tracker.closeDataFile()

        # Show a file transfer message on the screen
        msg = 'EDF data is transferring from EyeLink Host PC...'
        show_msg(win, msg, wait_for_keypress=False)

        # Download the EDF data file from the Host PC to a local data folder
        # parameters: source_file_on_the_host, destination_file_on_local_drive
        local_edf = os.path.join(session_folder, session_identifier + '.EDF')
        try:
            el_tracker.receiveDataFile(edf_file, local_edf)
        except RuntimeError as error:
            print('ERROR:', error)

        # Close the link to the tracker.
        el_tracker.close()

    # close the PsychoPy window
    win.close()

    # quit PsychoPy
    core.quit()
    sys.exit()


def abort_trial():
    """Ends recording """
    el_tracker = pylink.getEYELINK()

    # Stop recording
    if el_tracker.isRecording():
        # add 100 ms to catch final trial events
        pylink.pumpDelay(100)
        el_tracker.stopRecording()

    # clear the screen
    clear_screen(win)
    # Send a message to clear the Data Viewer screen
    bgcolor_RGB = (116, 116, 116)
    el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)

    # send a message to mark trial end
    el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)

    return pylink.TRIAL_ERROR


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'EyeLinkMRI_demoBuilder'  # from the Builder filename that created this script
expInfo = {
    'session': '01',
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
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE\\EyeLinkMRIdemo_Builder\\EyeLinkMRIdemo_Builder.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='[0,0,0]', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
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

# --- Initialize components for Routine "eyelinkSetup" ---
elInstructions = visual.TextStim(win=win, name='elInstructions',
    text='Press any key to start Camera Setup',
    font='Open Sans',
    pos=(0, 0), height=50.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from elConnect
# This Begin Experiment tab of the elConnect component gets graphic 
# information from Psychopy, sets the screen_pixel_coords on the Host PC based
# on these values, and logs the screen resolution for Data Viewer via 
# a DISPLAY_COORDS message

# get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size

# resolution fix for Mac retina displays
if 'Darwin' in platform.system():
    if use_retina:
        scn_width = int(scn_width/2.0)
        scn_height = int(scn_height/2.0)

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
# see the EyeLink Installation Guide, "Customizing Screen Settings"
el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendCommand(el_coords)

# Write a DISPLAY_COORDS message to the EDF file
# Data Viewer needs this piece of info for proper visualization, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendMessage(dv_coords)

# --- Initialize components for Routine "instruct" ---
taskInstructions = visual.TextStim(win=win, name='taskInstructions',
    text='OK. Ready for the experiment?\n\nPress z if there is a picture of a train or m if there is a picture of canoes.\n\nPress any key to continue',
    font='Open Sans',
    pos=(0, 0), height=50.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ready = keyboard.Keyboard()

# --- Initialize components for Routine "eyelinkStartRecording" ---
# Run 'Begin Experiment' code from elStartRecord
# This Begin Experiment tab of the elStartRecord component initializes some 
# variables that are used to keep track of the current trial and block 
# numbers

trial_index = 1
block_index = 0

# --- Initialize components for Routine "waitForScannerPulse" ---
waitTriggerText = visual.TextStim(win=win, name='waitTriggerText',
    text='Waiting for scanner pulse\n(keyboard t press)',
    font='Open Sans',
    pos=(0, 0), height=50.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyTrigger = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=50.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
resp = keyboard.Keyboard()

# --- Initialize components for Routine "eyelinkStopRecording" ---

# --- Initialize components for Routine "thanks" ---
endScreen = visual.TextStim(win=win, name='endScreen',
    text='This is the end of the experiment.\n\nThanks!',
    font='Open Sans',
    pos=(0, 0), height=50.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "eyelinkSetup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
eyelinkSetupComponents = [elInstructions, key_resp]
for thisComponent in eyelinkSetupComponents:
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

# --- Run Routine "eyelinkSetup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *elInstructions* updates
    if elInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        elInstructions.frameNStart = frameN  # exact frame index
        elInstructions.tStart = t  # local t and not account for scr refresh
        elInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(elInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'elInstructions.started')
        elInstructions.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eyelinkSetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "eyelinkSetup" ---
for thisComponent in eyelinkSetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# Run 'End Routine' code from elConnect
# This End Routine tab of the elConnect component configures some
# graphics options for calibration, and then performs a camera setup
# so that you can set up the eye tracker and calibrate/validate the participant

# Configure a graphics environment (genv) for tracker calibration
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
print(genv)  # print out the version number of the CoreGraphics library

# Set background and foreground colors for the calibration target
# in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
foreground_color = (-1, -1, -1)
background_color = tuple(win.color)
genv.setCalibrationColors(foreground_color, background_color)

# Set up the calibration target
#
# The target could be a "circle" (default), a "picture", a "movie" clip,
# or a rotating "spiral". To configure the type of calibration target, set
# genv.setTargetType to "circle", "picture", "movie", or "spiral", e.g.,
# genv.setTargetType('picture')
#
# Use genv.setMovieTarget() to set a "movie" target
# genv.setMovieTarget(os.path.join('videos', 'calibVid.mov'))

# Use a picture as the calibration target
genv.setTargetType('picture')
genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp'))

# Configure the size of the calibration target (in pixels)
# this option applies only to "circle" and "spiral" targets
# genv.setTargetSize(24)

# Beeps to play during calibration, validation and drift correction
# parameters: target, good, error
#     target -- sound to play when target moves
#     good -- sound to play on successful operation
#     error -- sound to play on failure or interruption
# Each parameter could be ''--default sound, 'off'--no sound, or a wav file
genv.setCalibrationSounds('', '', '')

# resolution fix for macOS retina display issues
if use_retina:
    genv.fixMacRetinaDisplay()

#clear the screen before we begin Camera Setup mode
clear_screen(win)

# Request Pylink to use the PsychoPy window we opened above for calibration
pylink.openGraphicsEx(genv)

# skip this step if running the script in Dummy Mode
if not dummy_mode:
    try:
        el_tracker.doTrackerSetup()
    except RuntimeError as err:
        print('ERROR:', err)
        el_tracker.exitCalibration()
# the Routine "eyelinkSetup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ready.keys = []
ready.rt = []
_ready_allKeys = []
# keep track of which components have finished
instructComponents = [taskInstructions, ready]
for thisComponent in instructComponents:
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

# --- Run Routine "instruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *taskInstructions* updates
    if taskInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        taskInstructions.frameNStart = frameN  # exact frame index
        taskInstructions.tStart = t  # local t and not account for scr refresh
        taskInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(taskInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'taskInstructions.started')
        taskInstructions.setAutoDraw(True)
    
    # *ready* updates
    waitOnFlip = False
    if ready.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ready.started')
        ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=None, waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # just the last key pressed
            ready.rt = _ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruct" ---
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "eyelinkStartRecording" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from elStartRecord
    # This Begin Routine tab of the elStartRecord component updates some 
    # variables that are used to keep track of the current trial and block 
    # numbers, draws some feedback graphics (a simple shape) on the 
    # Host PC, sends a trial start messages to the EDF, performs a 
    # drift check/drift correct, and starts eye tracker recording
    
    # these keep track of the current trial number within the block/run and
    # the block/run number
    trial_in_block = 1
    block_index = block_index + 1
    
    # get a reference to the currently active EyeLink connection
    el_tracker = pylink.getEYELINK()
    
    # put the tracker in the offline mode first
    el_tracker.setOfflineMode()
    
    # clear the host screen before we draw the backdrop
    el_tracker.sendCommand('clear_screen 0')
    
    # OPTIONAL: draw landmarks and texts on the Host screen
    # In addition to backdrop image, You may draw simples on the Host PC to use
    # as landmarks. For illustration purpose, here we draw some texts and a box
    # For a list of supported draw commands, see the "COMMANDS.INI" file on the
    # Host PC (under /elcl/exe)
    left = int(scn_width/2.0) - 60
    top = int(scn_height/2.0) - 60
    right = int(scn_width/2.0) + 60
    bottom = int(scn_height/2.0) + 60
    draw_cmd = 'draw_filled_box %d %d %d %d 1' % (left, top, right, bottom)
    el_tracker.sendCommand(draw_cmd)
    
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('TRIALID %d' % trial_index)
    
    # record_status_message : show some info on the Host PC
    # here we show how many trial has been tested
    status_msg = 'Block number %d' % block_index
    el_tracker.sendCommand("record_status_message '%s'" % status_msg)
    
    # drift check
    # we recommend drift-check at the beginning of each trial
    # the doDriftCorrect() function requires target position in integers
    # the last two arguments:
    # draw_target (1-default, 0-draw the target then call doDriftCorrect)
    # allow_setup (1-press ESCAPE to recalibrate, 0-not allowed)
    #
    # Skip drift-check if running the script in Dummy Mode
    while not dummy_mode:
        # terminate the task if no longer connected to the tracker or
        # user pressed Ctrl-C to terminate the task
        if (not el_tracker.isConnected()) or el_tracker.breakPressed():
            terminate_task()
        # drift-check and re-do camera setup if ESCAPE is pressed
        try:
            error = el_tracker.doDriftCorrect(int(scn_width/2.0),
                                              int(scn_height/2.0), 1, 1)
            # break following a success drift-check
            if error is not pylink.ESC_KEY:
                break
        except:
            pass
    
    # put tracker in idle/offline mode before recording
    el_tracker.setOfflineMode()
    
    # Start recording
    # arguments: sample_to_file, events_to_file, sample_over_link,
    # event_over_link (1-yes, 0-no)
    try:
        el_tracker.startRecording(1, 1, 1, 1)
    except RuntimeError as error:
        print("ERROR:", error)
        abort_trial()
    
    el_tracker.sendMessage('pre 100 pause')
    
    # Allocate some time for the tracker to cache some samples
    pylink.pumpDelay(100)
    # keep track of which components have finished
    eyelinkStartRecordingComponents = []
    for thisComponent in eyelinkStartRecordingComponents:
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
    
    # --- Run Routine "eyelinkStartRecording" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkStartRecordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyelinkStartRecording" ---
    for thisComponent in eyelinkStartRecordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eyelinkStartRecording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "waitForScannerPulse" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyTrigger.keys = []
    keyTrigger.rt = []
    _keyTrigger_allKeys = []
    # keep track of which components have finished
    waitForScannerPulseComponents = [waitTriggerText, keyTrigger]
    for thisComponent in waitForScannerPulseComponents:
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
    
    # --- Run Routine "waitForScannerPulse" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitTriggerText* updates
        if waitTriggerText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waitTriggerText.frameNStart = frameN  # exact frame index
            waitTriggerText.tStart = t  # local t and not account for scr refresh
            waitTriggerText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitTriggerText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waitTriggerText.started')
            waitTriggerText.setAutoDraw(True)
        
        # *keyTrigger* updates
        waitOnFlip = False
        if keyTrigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyTrigger.frameNStart = frameN  # exact frame index
            keyTrigger.tStart = t  # local t and not account for scr refresh
            keyTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyTrigger, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyTrigger.started')
            keyTrigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyTrigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyTrigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyTrigger.status == STARTED and not waitOnFlip:
            theseKeys = keyTrigger.getKeys(keyList=['t'], waitRelease=False)
            _keyTrigger_allKeys.extend(theseKeys)
            if len(_keyTrigger_allKeys):
                keyTrigger.keys = _keyTrigger_allKeys[-1].name  # just the last key pressed
                keyTrigger.rt = _keyTrigger_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitForScannerPulseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waitForScannerPulse" ---
    for thisComponent in waitForScannerPulseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyTrigger.keys in ['', [], None]:  # No response was made
        keyTrigger.keys = None
    block.addData('keyTrigger.keys',keyTrigger.keys)
    if keyTrigger.keys != None:  # we had a response
        block.addData('keyTrigger.rt', keyTrigger.rt)
    # Run 'End Routine' code from logTriggerTime
    # This End Routine tab of the logTriggerTime component sends an event
    # marking message for the trigger pulse signal and, importantly, logs the pulse
    # time so that we can later write make it a trial variable (via TRIAL_VAR
    # messages to the EDF on each trial)
    
    # If a key was presssed, calculate the difference between the current time 
    # and the time of the key press onset. This offset value will be sent at the 
    # beginning of the message and will automatically be subtracted by Data Viewer 
    # from the timestamp of the message to position the message at the correct point 
    # in time. Then send a message marking the event
    if not isinstance(keyTrigger.rt,list):
        
        offsetValue = int(round((core.getTime() - \
            (waitTriggerText.tStartRefresh + keyTrigger.rt))*1000))
        scanPulseTime = int(round((waitTriggerText.tStartRefresh + keyTrigger.rt)*1000))
        el_tracker.sendMessage('%i SCAN_PULSE_RECEIVED' % offsetValue)
    # the Routine "waitForScannerPulse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialData.csv'),
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
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from elTrial
        # This Begin Routine tab of the elTrial component resets some 
        # variables that are used to keep track of whether certain trial events have
        # happened and sends trial variable messages to the EDF to mark condition
        # information
        
        # these variables keep track of whether the fixation presentation, image 
        # presentation, and trial response have occured yet (0 = no, 1 = yes).
        # They later help us to ensure that each event marking message only gets
        # sent once, at the time of each event
        sentResponseMessage = 0
        sentFixationMessage = 0
        sentImageMessage = 0
        
        # send a "TRIALID" message to mark the start of a trial, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        # Skip this message for the first trial
        if trial_in_block > 1:
            el_tracker.sendMessage('TRIALID %d' % trial_index)
            
        # record trial variables to the EDF data file, for details, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        el_tracker.sendMessage('!V TRIAL_VAR scanPulseTime %s' % scanPulseTime)
        el_tracker.sendMessage('!V TRIAL_VAR condition %s' % condition)
        el_tracker.sendMessage('!V TRIAL_VAR identifier %s' % identifier)
        el_tracker.sendMessage('!V TRIAL_VAR image %s' % trialImage)
        
        # if sending many messages in a row, add a 1 msec pause between after 
        # every 5 messages or so
        time.sleep(0.001)
        el_tracker.sendMessage('!V TRIAL_VAR corrAns %s' % corrAns)
        image.setImage(trialImage)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, image, resp]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from elTrial
            # This Each Frame tab of the elTrial component handles the marking
            # of experimental events via messages to the EDF, sends additional messages
            # to allow visualization of trial stimuli in Data Viewer, logs trial variable
            # information associated with responses and stimulus timing, and checks whether
            # the eye tracker is still properly recording (and aborts the trial if not)
            
            # if a key was presssed, calculate the difference between the current time 
            # and the time of the key press onset. 
            # This offset value will be sent at the beginning of the message
            # and will automatically be subtracted by Data Viewer from the timestamp
            # of the message to position the message at the correct point in time
            # then send a message marking the event
            if not isinstance(resp.rt,list) and sentResponseMessage == 0:
                offsetValue = int(round((core.getTime() - \
                    (image.tStartRefresh + resp.rt))*1000))
                el_tracker.sendMessage('%i KEY_PRESSED' % offsetValue)
            
                # after every few messages, include a 1 msec delay to ensure
                # that no messages are missed 
                time.sleep(0.001)
                el_tracker.sendMessage('!V TRIAL_VAR accuracy %i' % resp.corr)
                el_tracker.sendMessage('!V TRIAL_VAR keyPressed %s' % resp.keys)
            
                # log that the response message has been written so that we don't 
                # write it again on future frames
                sentResponseMessage = 1
            
            # if the trial fixaton target onset just occurred then mark its occurence
            # and send some draw command messages to the EDF
            if fixation.tStartRefresh is not None and sentFixationMessage == 0:
                # calculate the difference between the current time and the time of the 
                # fixation onset. This offset value will be sent at the beginning of the message
                # and will automatically be subtracted by Data Viewer from the timestamp
                # of the message to position the message at the correct point in time
                # then send a message marking the event
                offsetValue = int(round((core.getTime() - fixation.tStartRefresh)*1000))
                el_tracker.sendMessage('%i FIXATION_ONSET' % offsetValue)
                
                # send some Data Viewer drawing commands so that you can see a representation
                # of the fixation cross in Data Viewer's various visualizations
                # For more information on this, see section "Protocol for EyeLink Data to 
                # Viewer Integration" section of the Data Viewer User Manual (Help -> Contents)
                el_tracker.sendMessage('%i !V CLEAR 128 128 128' % offsetValue)
                el_tracker.sendMessage('%i !V DRAWLINE 255 255 255 %i %i %i %i' % \
                    (offsetValue,scn_width/2 - 25,scn_height/2,scn_width/2 + 25,\
                    scn_height/2))  
                el_tracker.sendMessage('%i !V DRAWLINE 255 255 255 %i %i %i %i' % \
                    (offsetValue,scn_width/2,scn_height/2 - 25,scn_width/2,\
                    scn_height/2 + 25)) 
                
                # after every few messages, include a 1 msec delay to ensure
                # that no messages are missed 
                time.sleep(0.001)
                
                # log the fixation onset time (in Display PC time) as a Trial Variable
                fixationTime = fixation.tStartRefresh*1000
                el_tracker.sendMessage('!V TRIAL_VAR fixationTime %i' % fixationTime)
                
                # log that the fixation onset message has been written so that we don't 
                # write it again on future frames
                sentFixationMessage = 1
                
            # if the trial image onset just occurred then mark its occurence
            # and send an image load message to the EDF
            if image.tStartRefresh is not None and sentImageMessage == 0:
            
                # calculate the difference between the current time and the time of the 
                # image onset. This offset value will be sent at the beginning of the message
                # and will automatically be subtracted by Data Viewer from the timestamp
                # of the message to position the message at the correct point in time
                # then send a message marking the event
                offsetValue = int(round((core.getTime()-image.tStartRefresh)*1000))
                el_tracker.sendMessage(str(offsetValue) + ' IMAGE_ONSET')  
            
                # send some Data Viewer drawing commands so that you can see the trial image
                # in Data Viewer's various visualizations
                # For more information on this, see section "Protocol for EyeLink Data to 
                # Viewer Integration" section of the Data Viewer User Manual (Help -> Contents)
                el_tracker.sendMessage('%i !V CLEAR 128 128 128' % offsetValue)
                el_tracker.sendMessage('%i !V IMGLOAD CENTER ../../%s %i %i' % \
                    (offsetValue,trialImage,scn_width/2,scn_height/2)) 
                    
                #log the fixation onset time (in Display PC time) as a Trial Variable
                imageTime = image.tStartRefresh*1000
                el_tracker.sendMessage('!V TRIAL_VAR imageTime %i' % imageTime)
                
                # log that the image onset message has been written so that we don't 
                # write it again on future frames
                sentImageMessage = 1
            
            # abort the current trial if the tracker is no longer recording
            error = el_tracker.isRecording()
            if error is not pylink.TRIAL_OK:
                el_tracker.sendMessage('tracker_disconnected')
                abort_trial()
            
            # check keyboard events
            for keycode, modifier in event.getKeys(modifiers=True):
            
            # Abort a trial if "ESCAPE" is pressed
                if keycode == 'escape':
                    el_tracker.sendMessage('trial_skipped_by_user')
                    # clear the screen
                    clear_screen(win)
                    # abort trial
                    abort_trial()
                    contineRoutine = False
                    
                # Terminate the task if Ctrl-c
                if keycode == 'c' and (modifier['ctrl'] is True):
                    el_tracker.sendMessage('terminated_by_user')
                    terminate_task()
                    
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    image.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp.started')
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.stopped')
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=["z","m"], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from elTrial
        # This End Routine tab of the elTrial component clears the screen and logs
        # an additional message to mark the end of the trial
        
        # clear the screen
        clear_screen(win)
        el_tracker.sendMessage('blank_screen')
        # send a message to clear the Data Viewer screen as well
        el_tracker.sendMessage('!V CLEAR 128 128 128')
            
        # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        el_tracker.sendMessage('TRIAL_RESULT %d' % 0)
        
        # update the trial counter for the next trial
        trial_index = trial_index + 1
        trial_in_block = trial_in_block + 1
        
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "eyelinkStopRecording" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    eyelinkStopRecordingComponents = []
    for thisComponent in eyelinkStopRecordingComponents:
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
    
    # --- Run Routine "eyelinkStopRecording" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkStopRecordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyelinkStopRecording" ---
    for thisComponent in eyelinkStopRecordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from elStopRecord
    # This End Routine tab of the elStopRecord component stops eye tracker recording
    
    # stop recording; add 100 msec to catch final events before stopping
    pylink.pumpDelay(100)
    el_tracker.stopRecording()
    # the Routine "eyelinkStopRecording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'block'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [endScreen]
for thisComponent in thanksComponents:
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

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endScreen* updates
    if endScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endScreen.frameNStart = frameN  # exact frame index
        endScreen.tStart = t  # local t and not account for scr refresh
        endScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endScreen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endScreen.started')
        endScreen.setAutoDraw(True)
    if endScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endScreen.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            endScreen.tStop = t  # not accounting for scr refresh
            endScreen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endScreen.stopped')
            endScreen.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)
# Run 'End Experiment' code from elConnect
# This End Experiment tab of the elConnect component calls the 
# terminate_task helper function to get the EDF file and close the connection
# to the Host PC

# Disconnect, download the EDF file, then terminate the task
terminate_task()

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
