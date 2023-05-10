#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on November 02, 2022, at 13:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

##### Start of Original CGE Imports #####

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

##### End of Original CGE Imports #####



##### eyelinkSetuo - From MRIdemo_Builder - START of elConnect 'Before Experiment' Code #####
""" 
    PLACE 
        AFTER 'Import packages'
        BEFORE DIRECTORY AND WINDOW SETUP
"""
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
""" 
    PLACE 
        AFTER 'Import packages'
        BEFORE DIRECTORY AND WINDOW SETUP
"""
##### eyelinkSetuo - From MRIdemo_Builder - END of elConnect 'Before Experiment' Code #####

##### Original CGE #####

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
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE\\CGE_draft_version.py',
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
    size=[1280, 1024], fullscr=True, screen=0,
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

##### Original CGE #####

### COMPONENTS: Setting up the components (shapes, texts, colors, etc.) to use to run the routines (Instructions, Choicesets, Outcome, ITI, etc.)

##### eyelinkSetuo - From MRIdemo_Builder - START of 'eyelinkSetup' Routine components #####
""" 
    PLACE 
        AFTER setting up window and keyboard
        BEFORE START of elConnect 'Begin Experiment' Code
"""
# --- Initialize components for Routine "eyelinkSetup" ---
instructionsTextHeight = 0.04;
letterTextHeight = 0.1;
wrap = .5
elInstructions = visual.TextStim(win=win, name='elInstructions',
    text='Press any key to start Camera Setup',
    font='Open Sans',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
""" 
    PLACE 
        AFTER setting up window and keyboard
        BEFORE START of elConnect 'Begin Experiment' Code
""" # Included with the elConnect Code because they are all part of the same routine
##### eyelinkSetuo -  From MRIdemo_Builder - END of 'eyelinkSetup' Routine components #####

##### eyelinkSetuo - From MRIDemo_Builder - START of elConnect 'Begin Experiment' Code #####
""" 
    PLACE 
        AFTER 'Intialize components for Routine "eyelinkSetup"'
        BEFORE 'Initialize components for Routine "instruct"'
"""
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
""" 
    PLACE 
        AFTER 'Intialize components for Routine "eyelinkSetup"'
        BEFORE 'Initialize components for Routine "instruct"'
"""
##### eyelinkSetuo - From MRIDemo_Builder - END of elConnect 'Begin Experiment' Code #####

### Orgiginal CGE

### Practice Choiceset

# --- Initialize components for Routine "instructions" --- Practice Choiceset Start Part 1
# Run 'Begin Experiment' code from code
# instructionsTextHeight = 0.04;
# letterTextHeight = 0.1;
# wrap = .5
Instructions = visual.TextStim(win=win, name='Instructions',
    text='As discussed in the instructions, you will choose between a gamble and a guaranteed alternative.\n\nOnce "V-Left" and "N-Right" appear on the screen, you may press "V" to select the option on the left and "N" to choose the option on the right.\n\nPress "enter" to move on to the next screen.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
inst1 = keyboard.Keyboard()

### Orginal CGE

### eyelinkStartRecording - From MRIdemo_Builder - START of elStartRecord 'Begin Experiment' Code ###
"""
    PLACE
        AFTER instructions
        BEFORE next Routine run
"""
# --- Initialize components for Routine "eyelinkStartRecording" ---
# Run 'Begin Experiment' code from elStartRecord
# This Begin Experiment tab of the elStartRecord component initializes some 
# variables that are used to keep track of the current trial and block 
# numbers

trial_index = 1
block_index = 0
"""
    PLACE
        AFTER instructions
        BEFORE next Routine run
"""
### eyelinkStartRecording - From MRIdemo_Builder - END of elStartRecord 'Begin Experiment' Code ###

### Original CGE

# --- Initialize components for Routine "pracStart" --- Practice Choiceset Start Part 2
startPract = visual.TextStim(win=win, name='startPract',
    text='There will now be 5 practice trials.\n\nWhen you are ready to begin the practice, press "V" or "N".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
startPracResp = keyboard.Keyboard()

# --- Initialize components for Routine "practiceTask" --- Practice Choiceset Components
# Run 'Begin Experiment' code from randLoc
textHeight = 0.05;
circleLeft = visual.Rect(
    win=win, name='circleLeft',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-1.0, interpolate=True)
    # Original line color: [-0.0667,0.6392,1]
    # Original silver color: 0.5216,0.5216,0.5216
circleRight = visual.Rect(
    win=win, name='circleRight',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
lineLeft = visual.Rect(
    win=win, name='lineLeft',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-3.0, interpolate=True)
orText = visual.TextStim(win=win, name='orText',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
lossTxt = visual.TextStim(win=win, name='lossTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-5.0);
gainTxt = visual.TextStim(win=win, name='gainTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-6.0);
safeTxt = visual.TextStim(win=win, name='safeTxt',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-7.0);
vLeft = visual.TextStim(win=win, name='vLeft',
    text='V-Left',
    font='Arial',
    pos=(-.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-8.0);
nRight = visual.TextStim(win=win, name='nRight',
    text='N-Right',
    font='Arial',
    pos=(.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-9.0);
choice1 = keyboard.Keyboard()

# --- Initialize components for Routine "isiPrac" --- Practice Choiceset ISI
isiText = visual.TextStim(win=win, name='isiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback" --- Practice Choiceset Outcome
noRespTxt = visual.TextStim(win=win, name='noRespTxt',
    text='You did not respond in time\n',
    font='Arial',
    pos=[0,0], height=textHeight, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
ocGamble = visual.Rect(
    win=win, name='ocGamble',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafe = visual.Rect(
    win=win, name='ocSafe',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeText = visual.TextStim(win=win, name='outcomeText',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
hideGamble = visual.Rect(
    win=win, name='hideGamble',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "itiPrac_2" --- Practice Choiceset ITI
itiText = visual.TextStim(win=win, name='itiText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

### Static Choiceset

# --- Initialize components for Routine "postPrac" --- Static Choiceset Start
postPracText = visual.TextStim(win=win, name='postPracText',
    text='Practice complete.\n\nWhen you are ready to start the real task, press "V" or "N".\n',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
postPractResp = keyboard.Keyboard()

# --- Initialize components for Routine "choiceWindow" --- Static Choiceset Components
# Run 'Begin Experiment' code from randLoc_2
loc = [];
circleLeftReal = visual.Rect(
    win=win, name='circleLeftReal',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-1.0, interpolate=True)
    # Blue [-0.0667,0.6392,1]
    # Silver [0.5216,0.5216,0.5216]
circleRightReal = visual.Rect(
    win=win, name='circleRightReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
lineLeftReal = visual.Rect(
    win=win, name='lineLeftReal',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-3.0, interpolate=True)
orTextReal = visual.TextStim(win=win, name='orTextReal',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
lossTxtReal = visual.TextStim(win=win, name='lossTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-5.0);
gainTxtReal = visual.TextStim(win=win, name='gainTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-6.0);
safeTxtReal = visual.TextStim(win=win, name='safeTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-7.0);
vLeftReal = visual.TextStim(win=win, name='vLeftReal',
    text='V-Left',
    font='Arial',
    pos=(-.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-8.0);
nRightReal = visual.TextStim(win=win, name='nRightReal',
    text='N-Right',
    font='Arial',
    pos=(.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-9.0);
realChoice = keyboard.Keyboard()

# --- Initialize components for Routine "isi" --- Static Choiceset ISI
isiTextReal = visual.TextStim(win=win, name='isiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "showOutcome" --- Static Choiceset Outcome
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
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
ocGambleReal = visual.Rect(
    win=win, name='ocGambleReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafeReal = visual.Rect(
    win=win, name='ocSafeReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeTextReal = visual.TextStim(win=win, name='outcomeTextReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
hideGambleReal = visual.Rect(
    win=win, name='hideGambleReal',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "iti" --- Static Choiceset ITI
itiTextReal = visual.TextStim(win=win, name='itiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

### Risk Preference Calculations

# --- Initialize components for Routine "computeEstimates" ---
# Run 'Begin Experiment' code from gridSearchCode
import math

### Function Definitions --- Calculating Risk Preferences from Static Choiceset to tailor Dynamic Choiceset

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
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0.0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=-4.0);

### Dynamic Choiceset

# --- Initialize components for Routine "loadDynamicChoiceset" --- Loading Calculated Dynamic Choiceset
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
staticLoadChoiceset = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='staticLoadChoiceset')

# --- Initialize components for Routine "startDynamicTask" --- Dynamic Choiceset Start
moveToRDMpart2 = visual.TextStim(win=win, name='moveToRDMpart2',
    text='When you are ready to begin the next round of the gambling task, press "enter".',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0.0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "choiceWindow" --- Dynamic Choiceset Components
# Run 'Begin Experiment' code from randLoc_2
loc = [];
circleLeftReal = visual.Rect(
    win=win, name='circleLeftReal',
    width=(.5, .5)[0], height=(.5, .5)[1],
    ori=0, pos=(-.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-1.0, interpolate=True)
    # Silver [0.5216,0.5216,0.5216]
    # Blue [-0.0667,0.6392,1]
circleRightReal = visual.Rect(
    win=win, name='circleRightReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(.35,0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
lineLeftReal = visual.Rect(
    win=win, name='lineLeftReal',
    width=(0.5, 0.01)[0], height=(0.5, 0.01)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=3,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-3.0, interpolate=True)
orTextReal = visual.TextStim(win=win, name='orTextReal',
    text='OR',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
lossTxtReal = visual.TextStim(win=win, name='lossTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-5.0);
gainTxtReal = visual.TextStim(win=win, name='gainTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-6.0);
safeTxtReal = visual.TextStim(win=win, name='safeTxtReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-7.0);
vLeftReal = visual.TextStim(win=win, name='vLeftReal',
    text='V-Left',
    font='Arial',
    pos=(-.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-8.0);
nRightReal = visual.TextStim(win=win, name='nRightReal',
    text='N-Right',
    font='Arial',
    pos=(.35, -.35), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-9.0);
realChoice = keyboard.Keyboard()

# --- Initialize components for Routine "isi" --- Dynamic Choiceset ISI
isiTextReal = visual.TextStim(win=win, name='isiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "showOutcome" --- Dynamic Choiceset Outcome
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
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
ocGambleReal = visual.Rect(
    win=win, name='ocGambleReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-2.0, interpolate=True)
ocSafeReal = visual.Rect(
    win=win, name='ocSafeReal',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-0.0667,0.6392,1], fillColor=[-0.0667,0.6392,1],
    opacity=1, depth=-3.0, interpolate=True)
outcomeTextReal = visual.TextStim(win=win, name='outcomeTextReal',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0,
    color=[0.5216,0.5216,0.5216], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
hideGambleReal = visual.Rect(
    win=win, name='hideGambleReal',
    width=(0.6, 0.3)[0], height=(0.6, 0.3)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[0.5216,0.5216,0.5216], fillColor=[0.5216,0.5216,0.5216],
    opacity=1, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "iti" --- Dynamic Choiceset ITI
itiTextReal = visual.TextStim(win=win, name='itiTextReal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

### Redirect to Working Memory Span (Originally Digit Span in CGT)

# --- Initialize components for Routine "rdmToSpanTransition" ---
breaktxt = visual.TextStim(win=win, name='breaktxt',
    text="You have sucessfully completed the first task in this experiment!\n\nPlease take a brief 1 minute break. \n\nYou are welcome to take a longer break, but keep in mind this study should take no longer than 1 hour to complete. \n\nWhen you are ready to move on, press 'enter' to continue.\n",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0.0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);
stopBreak = keyboard.Keyboard()

### End of CGE (Orignally Redirected to Qualtrics in CGT)

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to the next portion.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0.0,
    color=[-0.0667,0.6392,1], colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);

### Original CGE ###
### Setting up the clock to be used for running the routines

# Create some handy timers ---- Is this the timestamps that I need?
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine

### Original CGE ###

### Script for running the routines (Instructions, Choicesets, Outcome, etc.)

##### eyelinkSetuo - From MRIdemo_Builder - START of 'eyelinkSetup' Routine #####
"""
    PLACE
        AFTER 'Create some handy timers'
        BEFORE elConnect 'End Routine' Code
""" 
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
"""
    PLACE
        AFTER 'Create some handy timers'
        BEFORE elConnect 'End Routine' Code
""" # Included with the elConnect Code because they are all part of the same routine
##### From MRIdemo_Builder - START of 'eyelinkSetup' Routine #####

##### From MRIdemo_Builder - START of elConnect 'End Routine' Code #####
"""
    PLACE
        AFTER 'Ending Routine "eyelinkSetup"' (Included as part of "eyelinkSetup" routine)
        BEFORE 'Prepare to start Routine "instruct"' OR my version of instruction routine
"""
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
routineTimer.reset() ### Not part of the code but PsychoPy Coder AutoAdds for end of a routine
"""
    PLACE
        AFTER 'Ending Routine "eyelinkSetup"' (Included as part of "eyelinkSetup" routine)
        BEFORE 'Prepare to start Routine "instruct"' OR my version of instruction routine
"""
##### From MRIdemo_Builder - END of elConnect 'End Routine' Code #####

### Original CGE ###

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

### Practice Choiceset Routine

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

### Original CGE 

### eyelinkStartRecording - From MRIdemo_Builder - START of 'eyelinkStartRecording' Routine ###
"""
    PLACE
        AFTER (in this case) after 'set up handler to look after randomisation of conditions etc' for block OR after instructions Routine
        BEFORE elStartRecord 'Begin Routine'
""" # elStartRecord is within

# --- Prepare to start Routine "eyelinkStartRecording" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat

### eyelinkStartRecording - From MRIdemo_Builder - START of elStartRecord 'Begin Routine' Code ###
"""
    PLACE
        AFTER 'Prepare to start Routine "eyelinkStartRecording"'
        BEFORE 'keep track of which components have finished'
"""
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
"""
    PLACE
        AFTER 'Prepare to start Routine "eyelinkStartRecording"'
        BEFORE 'keep track of which components have finished'
""" # Still withing the 'Prepare to start Routine "eyelinkStartRecording"'
### eyelinkStartRecording - From MRIdemo_Builder - END of elStartRecord 'Begin Routine' Code ###

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
"""
    PLACE
        AFTER (in this case) after 'set up handler to look after randomisation of conditions etc' for block OR after instructions Routine
        BEFORE elStartRecord 'Begin Routine'
""" # elStartRecord is within
### eyelinkStartRecording - From MRIdemo_Builder - END of 'eyelinkStartRecording' Routine ###

### Original CGE ###

### Practice Choiceset Location Function

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cgtRDMPractice.xlsx', selection='0:4'), ### Practice Choiceset (5) Trials
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
        targetPos=[-.35,0]
    else:
        targetPos=[.35,0]

    if loc==1:
        lossLoc=[-.35,-.1]
        gainLoc=[-.35,.1]
        safeLoc=[.35,0]
    else:
        lossLoc=[.35,-.1]
        gainLoc=[.35,.1]
        safeLoc=[-.35,0]


    pracLossRounded = '$%.0f' % round(riskyLoss,0)
    pracGainRounded = '$%.2f' % round(riskyGain,2)
    pracSafeRounded = '$%.2f' % round(alternative,2)
    #circleRight.setFillColor([-0.0667,0.6392,1])
    #circleRight.setLineColor([0.5216,0.5216,0.5216])
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

    # --- Prepare to start Routine "feedback" --- Practice Choiceset Outcome Locations
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedback
    import random
    import math
    if not choice1.keys:
        outcome = math.nan
        noRespLoc = [0,0]
        ocLoc = [5,5] # What is the 5,5 referring to? Is it saying that it is happening offscreen?
        ocGambleLoc = [5,5]
        ocSafeLoc = [5,5]
        hideGamLoc = [5,5]
    elif choice1.keys == 'v' and loc == 1:
        outcome = random.choice([riskyGain, riskyLoss])
        if outcome == riskyGain:
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.125]
        elif outcome == riskyLoss:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.125]
             noRespLoc = [5,5]
    elif choice1.keys == 'v' and loc == 2:
        outcome = alternative
        ocLoc = [-.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif choice1.keys == 'n' and loc ==1:
        outcome = alternative
        ocLoc = [.35,0]
        ocGambleLoc = [5,5]
        ocSafeLoc = ocLoc
        hideGamLoc = ocGambleLoc
        noRespLoc = [5,5]
    elif choice1.keys == 'n' and loc ==2:
        outcome = random.choice([riskyGain, riskyLoss])
        if outcome == riskyGain:
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.125]
            noRespLoc = [5,5]
        elif outcome == riskyLoss:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.125]
            noRespLoc = [5,5]

    if outcome == riskyLoss:
        pracFeedbackRounded = "$%.0f" % round(outcome,0)
    else:
        pracFeedbackRounded = "$%.2f" % round(outcome,2)
    noRespTxt.setPos(noRespLoc)
    ocGamble.setPos(ocGambleLoc)
    ocSafe.setPos(ocSafeLoc)
    #outcomeText.setColor([0.5216,0.5216,0.5216], colorSpace='rgb')
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

### Static Choiceset Routine

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

### Static Choiceset Location Function

# set up handler to look after randomisation of conditions etc
staticRDM = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CGT-choice-set.csv', selection='0:4'), #### Static Choiceset (50) Trials
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
        targetPos=[-.35,0]
    else:
        targetPos=[.35,0]

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
    #circleRightReal.setFillColor([0.5216,0.5216,0.5216])
    #circleRightReal.setLineColor([-0.0667,0.6392,1])
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

    # --- Prepare to start Routine "showOutcome" --- Static Choiceset Outcome Locations
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
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.125]
        elif outcometmp == riskyoption2:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.125]
             noRespLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [-.35,0]
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
        ocLoc = [.35,0]
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
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.125]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.125]
            noRespLoc = [5,5]


    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)

    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLoss)
    riskygain_values.append(riskyGain)
    certain_values.append(certain)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    #outcomeTextReal.setColor([-0.0667,0.6392,1], colorSpace='rgb')
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

### Risk Preference Calculation Routine

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

fname.append("../CGE/bespoke_choicesets/bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM))
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

### Dynamic Choiceset Routine

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

### Dynamic Choiceset Location Function

# set up handler to look after randomisation of conditions etc
dynamicRDM = data.TrialHandler(nReps=1.0, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(fname[0], selection='0:4'), ### Dynamic Choiceset (60 Easy + 60 Hard = 120) Trials
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
        targetPos=[-.35,0]
    else:
        targetPos=[.35,0]

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
    #circleRightReal.setFillColor([0.5216,0.5216,0.5216])
    #circleRightReal.setLineColor([-0.0667,0.6392,1])
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

    # --- Prepare to start Routine "showOutcome" --- Dynamic Choiceset Outcome Locations
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
            ocLoc = [-.35,.1]
            ocGambleLoc = [-.35,0]
            ocSafeLoc = [5,5]
            noRespLoc = [5,5]
            hideGamLoc = [-.35,-.125]
        elif outcometmp == riskyoption2:
             ocLoc = [-.35,-.1]
             ocGambleLoc = [-.35,0]
             ocSafeLoc = [5,5]
             hideGamLoc = [-.35,.125]
             noRespLoc = [5,5]
    elif realChoice.keys == 'v' and loc == 2:
        outcometmp = safeoption
        choicetmp = 0
        riskyLoss = riskyoption2
        riskyGain = riskyoption1
        certain = safeoption
        ocLoc = [-.35,0]
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
        ocLoc = [.35,0]
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
            ocLoc = [.35,.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,-.125]
            noRespLoc = [5,5]
        elif outcometmp == riskyoption2:
            ocLoc = [.35,-.1]
            ocGambleLoc = [.35,0]
            ocSafeLoc = [5,5]
            hideGamLoc = [.35,.125]
            noRespLoc = [5,5]


    if outcometmp == riskyoption2:
        feedbackRounded = "$%.0f" % round(outcometmp,0)
    else:
        feedbackRounded = "$%.2f" % round(outcometmp,2)


    # print('gain:',riskyGain, 'riskyLoss', riskyLoss, 'certain:', certain ,'outcome:', outcometmp, 'choice:', choicetmp, 'feedback text:', feedbackRounded, 'choice keys:', realChoice.keys)
    
    outcomes.append(outcometmp)
    choices.append(choicetmp)
    riskyloss_values.append(riskyLoss)
    riskygain_values.append(riskyGain)
    certain_values.append(certain)
    noRespTxtReal.setPos(noRespLoc)
    ocGambleReal.setPos(ocGambleLoc)
    ocSafeReal.setPos(ocSafeLoc)
    #outcomeTextReal.setColor([-0.0667,0.6392,1], colorSpace='rgb')
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

### Transition to Working Memory Span (Originally Digit Span in CGT) Now Ospan and Sspan

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

### Original CGE ###

### eyelinkStopRecording - From MRIdemo_Builder - START of 'eyelinkStopRecording' Routine ###
""" 
    PLACE
        AFTER (in this case) the trial routine code
        BEFORE elStopRecord 'End Routine'
""" # elStopRecord code is within
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
        
### eyelinkStopRecording - From MRIdemo_Builder - START of elStopRecord 'End Routine' Code ###
"""
    PLACE
        AFTER 'Ending Routine "eyelinkStopRecording"'
        BEFORE next Routine
"""
# Run 'End Routine' code from elStopRecord
# This End Routine tab of the elStopRecord component stops eye tracker recording

# stop recording; add 100 msec to catch final events before stopping
pylink.pumpDelay(100)
el_tracker.stopRecording()
# the Routine "eyelinkStopRecording" was not non-slip safe, so reset the non-slip timer
routineTimer.reset() ### Not part of the eyetrack code but autoadd to end of routine
# completed 2.0 repeats of 'block'
"""
    PLACE
        AFTER 'Ending Routine "eyelinkStopRecording"'
        BEFORE next Routine
"""
### eyelinkStopRecording - From MRIdemo_Builder - END of elStopRecord 'End Routine' Code ###
""" 
    PLACE
        AFTER (in this case) the trial routine code
        BEFORE elStopRecord 'End Routine'
""" # elStopRecord code is within
### eyelinkStopRecording - From MRIdemo_Builder - START of 'eyelinkStopRecording' Routine ###

### Original CGE ###

### End Study Redirect to Qualtrics - Not Working Properly so Commented Out 

# # THE CODE BELOW DOESN'T EXIT GRACEFULLY; NO KEY RESPONSE QUITS?
# # --- Prepare to start Routine "END" ---
# continueRoutine = True
# routineForceEnded = False
# # update component parameters for each repeat
# # keep track of which components have finished
# ENDComponents = [ThankYou]
# for thisComponent in ENDComponents:
#     thisComponent.tStart = None
#     thisComponent.tStop = None
#     thisComponent.tStartRefresh = None
#     thisComponent.tStopRefresh = None
#     if hasattr(thisComponent, 'status'):
#         thisComponent.status = NOT_STARTED
# # reset timers
# t = 0
# _timeToFirstFrame = win.getFutureFlipTime(clock="now")
# frameN = -1
#
# # --- Run Routine "END" ---
# while continueRoutine:
#     # get current time
#     t = routineTimer.getTime()
#     tThisFlip = win.getFutureFlipTime(clock=routineTimer)
#     tThisFlipGlobal = win.getFutureFlipTime(clock=None)
#     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#     # update/draw components on each frame
#
#     # *ThankYou* updates
#     if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
#         # keep track of start time/frame for later
#         ThankYou.frameNStart = frameN  # exact frame index
#         ThankYou.tStart = t  # local t and not account for scr refresh
#         ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
#         win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
#         # add timestamp to datafile
#         thisExp.timestampOnFlip(win, 'ThankYou.started')
#         ThankYou.setAutoDraw(True)
#
#     # check for quit (typically the Esc key)
#     if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
#         core.quit()
#
#     # check if all components have finished
#     if not continueRoutine:  # a component has requested a forced-end of Routine
#         routineForceEnded = True
#         break
#     continueRoutine = False  # will revert to True if at least one component still running
#     for thisComponent in ENDComponents:
#         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#             continueRoutine = True
#             break  # at least one component has not yet finished
#
#     # refresh the screen
#     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#         win.flip()
#
# # --- Ending Routine "END" ---
# for thisComponent in ENDComponents:
#     if hasattr(thisComponent, "setAutoDraw"):
#         thisComponent.setAutoDraw(False)
# # the Routine "END" was not non-slip safe, so reset the non-slip timer
# routineTimer.reset()

### Original CGE ###

##### From MRIdemo_Builder - START of elConnect 'End Experiment' Code #####
"""
    PLACE
        AFTER last run routine script
        BEFORE 'End experiment'
"""
# Run 'End Experiment' code from elConnect
# This End Experiment tab of the elConnect component calls the 
# terminate_task helper function to get the EDF file and close the connection
# to the Host PC

# Disconnect, download the EDF file, then terminate the task
terminate_task()
"""
    PLACE
        AFTER last run routine script
        BEFORE 'End of experiment'
"""
##### From MRIdemo_Builder - END of elConnect 'End Experiment' Code #####

### Original CGE ###

### End of Experiment

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
