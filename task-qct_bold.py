﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.3.0dev6),
    on jeu 12 oct 2023 13:36:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.3.0dev6')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
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

# Run 'Before Experiment' code from channel_2
import socket
from hcphsignals import signals
from datetime import datetime
def send_message(message, addr="localhost", port=2023):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((addr, port))
    client_socket.sendall(message)
    client_socket.close()
folder_path = os.path.dirname('/home/common/workspace/HCPh-data/Psychopy/session-'+data.getDateStr(format="%Y-%m-%d")+'/')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

ename = 'qct_'+data.getDateStr(format="%Y-%m-%d")
trial = 0
for file in os.listdir(folder_path):
    filename_hour = datetime.strptime(file.split('_')[2],'%Hh%M.%S.%f')
    current_time = datetime.now()

    filename_hour_components = (filename_hour.hour, filename_hour.minute)
    current_time_components = (current_time.hour, current_time.minute)
    hour_difference = abs((current_time_components[0] - filename_hour_components[0]) +
                     (current_time_components[1] - filename_hour_components[1]) / 60.0)

    if ename in file and '.log' in file and hour_difference <1.5:
        trial += 1




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.3.0dev6'
expName = 'qct'  # from the Builder filename that created this script
expInfo = {
    'trial': trial,
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'../HCPh-data/Psychopy/session-'+data.getDateStr(format="%Y-%m-%d")+'/%s_%s_%s' %(expName, expInfo['date'],expInfo['trial'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/common/workspace/HCPh-fMRI-tasks/task-qct_bold.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.INFO)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.sr_research.eyelink.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'EYELINK 1000 DESKTOP',
    'simulation_mode': False,
    'network_settings': '100.1.1.1',
    'default_native_data_file_name': 'EXPFILE',
    'runtime_settings': {
        'sampling_rate': 1000.0,
        'track_eyes': 'RIGHT_EYE',
        'sample_filtering': {
            'sample_filtering': 'FILTER_LEVEL_2',
            'elLiveFiltering': 'FILTER_LEVEL_OFF',
        },
        'vog_settings': {
            'pupil_measure_types': 'PUPIL_AREA',
            'tracking_mode': 'PUPIL_CR_TRACKING',
            'pupil_center_algorithm': 'ELLIPSE_FIT',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='qct', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
wait_trigger = visual.TextStim(win=win, name='wait_trigger',
    text='The program is ready for the scanner trigger. Press t to proceed manually.',
    font='Arial',
    pos=[0, -0.9], height=0.07, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
fix_desc = visual.TextStim(win=win, name='fix_desc',
    text='This task is composed of several blocks of stimuli. Whenever you see a green circle like the one below, please fix your gaze on it. If the circle moves, follow it with your eyes.',
    font='Arial',
    pos=(0.0, 0.6), height=0.12, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
fixation_example = visual.ShapeStim(
    win=win, name='fixation_example',
    size=(0.075, 0.1), vertices='circle',
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
et_desc = visual.TextStim(win=win, name='et_desc',
    text=' If you see "RIGHT" or "LEFT", sequentially tap your thumb with your other fingers of the corresponding hand.\nPlease leave the alarm button somewhere you can retrieve it when the task is concluded.',
    font='Arial',
    pos=(0, -0.4), height=0.12, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
fixation_example_inner = visual.ShapeStim(
    win=win, name='fixation_example_inner',
    size=(0.035, 0.047), vertices='circle',
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "start_et" ---
et_start = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)
# Run 'Begin Experiment' code from channel_2



# --- Initialize components for Routine "trialSelection" ---
# Run 'Begin Experiment' code from code_4
nRepsvis=0
nRepsmot=0
nRepscog=0
nRepsblank=0

# --- Initialize components for Routine "vis" ---
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask='gauss', anchor='center',
    ori=0, pos=[0, 0], size=[1.3, 1.6], sf=12, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1, contrast=1.0, blendmode='avg',
    texRes=128, interpolate=True, depth=-1.0)
fixation_inner_circle = visual.ShapeStim(
    win=win, name='fixation_inner_circle',
    size=[0.035, 0.045], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,1,-1],
    opacity=1, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "cog" ---
eye_movement_fixation = visual.ShapeStim(
    win=win, name='eye_movement_fixation',
    size=[0.075, 0.1], vertices='circle',
    ori=0, pos=[0,0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[0,0,0],
    opacity=1, depth=0.0, interpolate=True)
eye_movement_fixation_inner = visual.ShapeStim(
    win=win, name='eye_movement_fixation_inner',
    size=[0.035, 0.045], vertices='circle',
    ori=0, pos=[0,0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,1,-1],
    opacity=1, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "mot" ---
ft_hand = visual.TextStim(win=win, name='ft_hand',
    text='',
    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank" ---
fixation = visual.ShapeStim(
    win=win, name='fixation',
    size=[0.075, 0.1], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[0,0,0],
    opacity=1, depth=0.0, interpolate=True)
fixation_inner = visual.ShapeStim(
    win=win, name='fixation_inner',
    size=[0.035, 0.047], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,1,-1],
    opacity=1, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end" ---
et_stop = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.075, fillColor=[-1.0000, -1.0000, -1.0000], borderColor='black', lineWidth=2.0,
    innerRadius=0.035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='NINE_POINTS', randomisePos=False, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introComponents = [wait_trigger, key_resp_2, fix_desc, fixation_example, et_desc, fixation_example_inner]
for thisComponent in introComponents:
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

# --- Run Routine "intro" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_trigger* updates
    
    # if wait_trigger is starting this frame...
    if wait_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_trigger.frameNStart = frameN  # exact frame index
        wait_trigger.tStart = t  # local t and not account for scr refresh
        wait_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_trigger, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'wait_trigger.started')
        # update status
        wait_trigger.status = STARTED
        wait_trigger.setAutoDraw(True)
    
    # if wait_trigger is active this frame...
    if wait_trigger.status == STARTED:
        # update params
        pass
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['t', 's'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *fix_desc* updates
    
    # if fix_desc is starting this frame...
    if fix_desc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix_desc.frameNStart = frameN  # exact frame index
        fix_desc.tStart = t  # local t and not account for scr refresh
        fix_desc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix_desc, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fix_desc.started')
        # update status
        fix_desc.status = STARTED
        fix_desc.setAutoDraw(True)
    
    # if fix_desc is active this frame...
    if fix_desc.status == STARTED:
        # update params
        pass
    
    # *fixation_example* updates
    
    # if fixation_example is starting this frame...
    if fixation_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_example.frameNStart = frameN  # exact frame index
        fixation_example.tStart = t  # local t and not account for scr refresh
        fixation_example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_example, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_example.started')
        # update status
        fixation_example.status = STARTED
        fixation_example.setAutoDraw(True)
    
    # if fixation_example is active this frame...
    if fixation_example.status == STARTED:
        # update params
        pass
    
    # *et_desc* updates
    
    # if et_desc is starting this frame...
    if et_desc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        et_desc.frameNStart = frameN  # exact frame index
        et_desc.tStart = t  # local t and not account for scr refresh
        et_desc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(et_desc, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'et_desc.started')
        # update status
        et_desc.status = STARTED
        et_desc.setAutoDraw(True)
    
    # if et_desc is active this frame...
    if et_desc.status == STARTED:
        # update params
        pass
    
    # *fixation_example_inner* updates
    
    # if fixation_example_inner is starting this frame...
    if fixation_example_inner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_example_inner.frameNStart = frameN  # exact frame index
        fixation_example_inner.tStart = t  # local t and not account for scr refresh
        fixation_example_inner.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_example_inner, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_example_inner.started')
        # update status
        fixation_example_inner.status = STARTED
        fixation_example_inner.setAutoDraw(True)
    
    # if fixation_example_inner is active this frame...
    if fixation_example_inner.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "start_et" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from channel_2
send_message((signals.RUN | signals.ET_START_AND_STOP).to_bytes())
ioServer.getDevice('tracker').sendMessage("hello qct")

# keep track of which components have finished
start_etComponents = [et_start]
for thisComponent in start_etComponents:
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

# --- Run Routine "start_et" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *et_start* updates
    
    # if et_start is starting this frame...
    if et_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        et_start.frameNStart = frameN  # exact frame index
        et_start.tStart = t  # local t and not account for scr refresh
        et_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(et_start, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'et_start.started')
        # update status
        et_start.status = STARTED
    
    # if et_start is stopping this frame...
    if et_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > et_start.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            et_start.tStop = t  # not accounting for scr refresh
            et_start.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'et_start.stopped')
            # update status
            et_start.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_etComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_et" ---
for thisComponent in start_etComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if et_start.status != FINISHED:
    et_start.status = FINISHED
# the Routine "start_et" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialSelectLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_select.csv'),
    seed=None, name='trialSelectLoop')
thisExp.addLoop(trialSelectLoop)  # add the loop to the experiment
thisTrialSelectLoop = trialSelectLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialSelectLoop.rgb)
if thisTrialSelectLoop != None:
    for paramName in thisTrialSelectLoop:
        exec('{} = thisTrialSelectLoop[paramName]'.format(paramName))

for thisTrialSelectLoop in trialSelectLoop:
    currentLoop = trialSelectLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialSelectLoop.rgb)
    if thisTrialSelectLoop != None:
        for paramName in thisTrialSelectLoop:
            exec('{} = thisTrialSelectLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trialSelection" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    if trialSelect ==1:
        nRepsvis=1
        nRepsmot=0
        nRepscog=0
        nRepsblank=0
    if trialSelect ==2:
        nRepsvis=0
        nRepsmot=1
        nRepscog=0
        nRepsblank=0
    if trialSelect ==3:
        nRepsvis=0
        nRepsmot=0
        nRepscog=1
        nRepsblank=0
    if trialSelect ==4:
        nRepsvis=0
        nRepsmot=0
        nRepscog=0
        nRepsblank=1
    print(trialSelect)
    
    # keep track of which components have finished
    trialSelectionComponents = []
    for thisComponent in trialSelectionComponents:
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
    
    # --- Run Routine "trialSelection" ---
    routineForceEnded = not continueRoutine
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
        for thisComponent in trialSelectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trialSelection" ---
    for thisComponent in trialSelectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trialSelection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    visLoop = data.TrialHandler(nReps=nRepsvis, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='visLoop')
    thisExp.addLoop(visLoop)  # add the loop to the experiment
    thisVisLoop = visLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVisLoop.rgb)
    if thisVisLoop != None:
        for paramName in thisVisLoop:
            exec('{} = thisVisLoop[paramName]'.format(paramName))
    
    for thisVisLoop in visLoop:
        currentLoop = visLoop
        # abbreviate parameter names if possible (e.g. rgb = thisVisLoop.rgb)
        if thisVisLoop != None:
            for paramName in thisVisLoop:
                exec('{} = thisVisLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "vis" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        gratingPhase=0
        frameCounter=0
        
        
        # Run 'Begin Routine' code from channel_4
        send_message(signals.QCT_VIS.to_bytes())
        ioServer.getDevice('tracker').sendMessage("start vis loop")
        
        # keep track of which components have finished
        visComponents = [grating, fixation_inner_circle]
        for thisComponent in visComponents:
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
        
        # --- Run Routine "vis" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            frameCounter=frameCounter+1
            
            if frameCounter<30:  # Change this number (30) to make the grating switch direction more/less often
                gratingPhase=gratingPhase+0.1 # Change this number (0.1) to speed up or slow down the grating
            
            if frameCounter>=30: # Change this number (30) to make the grating switch direction more/less of
                gratingPhase=gratingPhase-0.1 # Change this number (0.1) to speed up or slow down the grating
            
            if frameCounter==60: 
                frameCounter=0
            
            
            # *grating* updates
            
            # if grating is starting this frame...
            if grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grating.frameNStart = frameN  # exact frame index
                grating.tStart = t  # local t and not account for scr refresh
                grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating.started')
                # update status
                grating.status = STARTED
                grating.setAutoDraw(True)
            
            # if grating is active this frame...
            if grating.status == STARTED:
                # update params
                grating.setPhase(gratingPhase, log=False)
            
            # if grating is stopping this frame...
            if grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grating.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    grating.tStop = t  # not accounting for scr refresh
                    grating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grating.stopped')
                    # update status
                    grating.status = FINISHED
                    grating.setAutoDraw(False)
            
            # *fixation_inner_circle* updates
            
            # if fixation_inner_circle is starting this frame...
            if fixation_inner_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_inner_circle.frameNStart = frameN  # exact frame index
                fixation_inner_circle.tStart = t  # local t and not account for scr refresh
                fixation_inner_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_inner_circle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_inner_circle.started')
                # update status
                fixation_inner_circle.status = STARTED
                fixation_inner_circle.setAutoDraw(True)
            
            # if fixation_inner_circle is active this frame...
            if fixation_inner_circle.status == STARTED:
                # update params
                pass
            
            # if fixation_inner_circle is stopping this frame...
            if fixation_inner_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_inner_circle.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_inner_circle.tStop = t  # not accounting for scr refresh
                    fixation_inner_circle.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_inner_circle.stopped')
                    # update status
                    fixation_inner_circle.status = FINISHED
                    fixation_inner_circle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in visComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "vis" ---
        for thisComponent in visComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_2
        gratingPhase=0
        # Run 'End Routine' code from channel_4
        ioServer.getDevice('tracker').sendMessage("stop vis loop")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed nRepsvis repeats of 'visLoop'
    
    # get names of stimulus parameters
    if visLoop.trialList in ([], [None], None):
        params = []
    else:
        params = visLoop.trialList[0].keys()
    # save data for this loop
    visLoop.saveAsExcel(filename + '.xlsx', sheetName='visLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    visLoop.saveAsText(filename + 'visLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    cogLoop = data.TrialHandler(nReps=nRepscog, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('xpos_ypos.csv'),
        seed=None, name='cogLoop')
    thisExp.addLoop(cogLoop)  # add the loop to the experiment
    thisCogLoop = cogLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCogLoop.rgb)
    if thisCogLoop != None:
        for paramName in thisCogLoop:
            exec('{} = thisCogLoop[paramName]'.format(paramName))
    
    for thisCogLoop in cogLoop:
        currentLoop = cogLoop
        # abbreviate parameter names if possible (e.g. rgb = thisCogLoop.rgb)
        if thisCogLoop != None:
            for paramName in thisCogLoop:
                exec('{} = thisCogLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "cog" ---
        continueRoutine = True
        # update component parameters for each repeat
        eye_movement_fixation.setPos([xpos, ypos])
        eye_movement_fixation_inner.setPos([xpos, ypos])
        # Run 'Begin Routine' code from channel_8
        send_message(signals.QCT_COG.to_bytes())
        ioServer.getDevice('tracker').sendMessage("start cog loop")
        # keep track of which components have finished
        cogComponents = [eye_movement_fixation, eye_movement_fixation_inner]
        for thisComponent in cogComponents:
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
        
        # --- Run Routine "cog" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *eye_movement_fixation* updates
            
            # if eye_movement_fixation is starting this frame...
            if eye_movement_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eye_movement_fixation.frameNStart = frameN  # exact frame index
                eye_movement_fixation.tStart = t  # local t and not account for scr refresh
                eye_movement_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eye_movement_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eye_movement_fixation.started')
                # update status
                eye_movement_fixation.status = STARTED
                eye_movement_fixation.setAutoDraw(True)
            
            # if eye_movement_fixation is active this frame...
            if eye_movement_fixation.status == STARTED:
                # update params
                pass
            
            # if eye_movement_fixation is stopping this frame...
            if eye_movement_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eye_movement_fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    eye_movement_fixation.tStop = t  # not accounting for scr refresh
                    eye_movement_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'eye_movement_fixation.stopped')
                    # update status
                    eye_movement_fixation.status = FINISHED
                    eye_movement_fixation.setAutoDraw(False)
            
            # *eye_movement_fixation_inner* updates
            
            # if eye_movement_fixation_inner is starting this frame...
            if eye_movement_fixation_inner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eye_movement_fixation_inner.frameNStart = frameN  # exact frame index
                eye_movement_fixation_inner.tStart = t  # local t and not account for scr refresh
                eye_movement_fixation_inner.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eye_movement_fixation_inner, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eye_movement_fixation_inner.started')
                # update status
                eye_movement_fixation_inner.status = STARTED
                eye_movement_fixation_inner.setAutoDraw(True)
            
            # if eye_movement_fixation_inner is active this frame...
            if eye_movement_fixation_inner.status == STARTED:
                # update params
                pass
            
            # if eye_movement_fixation_inner is stopping this frame...
            if eye_movement_fixation_inner.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eye_movement_fixation_inner.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    eye_movement_fixation_inner.tStop = t  # not accounting for scr refresh
                    eye_movement_fixation_inner.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'eye_movement_fixation_inner.stopped')
                    # update status
                    eye_movement_fixation_inner.status = FINISHED
                    eye_movement_fixation_inner.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cogComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cog" ---
        for thisComponent in cogComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from channel_8
        ioServer.getDevice('tracker').sendMessage("stop cog loop")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed nRepscog repeats of 'cogLoop'
    
    # get names of stimulus parameters
    if cogLoop.trialList in ([], [None], None):
        params = []
    else:
        params = cogLoop.trialList[0].keys()
    # save data for this loop
    cogLoop.saveAsExcel(filename + '.xlsx', sheetName='cogLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    cogLoop.saveAsText(filename + 'cogLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    ftLoop = data.TrialHandler(nReps=nRepsmot, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('fingertapping.csv'),
        seed=None, name='ftLoop')
    thisExp.addLoop(ftLoop)  # add the loop to the experiment
    thisFtLoop = ftLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFtLoop.rgb)
    if thisFtLoop != None:
        for paramName in thisFtLoop:
            exec('{} = thisFtLoop[paramName]'.format(paramName))
    
    for thisFtLoop in ftLoop:
        currentLoop = ftLoop
        # abbreviate parameter names if possible (e.g. rgb = thisFtLoop.rgb)
        if thisFtLoop != None:
            for paramName in thisFtLoop:
                exec('{} = thisFtLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mot" ---
        continueRoutine = True
        # update component parameters for each repeat
        ft_hand.setPos([ft_xpos, 0])
        ft_hand.setText(hand)
        # Run 'Begin Routine' code from channel_10
        send_message(signals.QCT_MOT.to_bytes())
        ioServer.getDevice('tracker').sendMessage("start mot loop")
        # keep track of which components have finished
        motComponents = [ft_hand]
        for thisComponent in motComponents:
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
        
        # --- Run Routine "mot" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ft_hand* updates
            
            # if ft_hand is starting this frame...
            if ft_hand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ft_hand.frameNStart = frameN  # exact frame index
                ft_hand.tStart = t  # local t and not account for scr refresh
                ft_hand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ft_hand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ft_hand.started')
                # update status
                ft_hand.status = STARTED
                ft_hand.setAutoDraw(True)
            
            # if ft_hand is active this frame...
            if ft_hand.status == STARTED:
                # update params
                pass
            
            # if ft_hand is stopping this frame...
            if ft_hand.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ft_hand.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ft_hand.tStop = t  # not accounting for scr refresh
                    ft_hand.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ft_hand.stopped')
                    # update status
                    ft_hand.status = FINISHED
                    ft_hand.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in motComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mot" ---
        for thisComponent in motComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from channel_10
        ioServer.getDevice('tracker').sendMessage("stop mot loop")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed nRepsmot repeats of 'ftLoop'
    
    # get names of stimulus parameters
    if ftLoop.trialList in ([], [None], None):
        params = []
    else:
        params = ftLoop.trialList[0].keys()
    # save data for this loop
    ftLoop.saveAsExcel(filename + '.xlsx', sheetName='ftLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    ftLoop.saveAsText(filename + 'ftLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    blankLoop = data.TrialHandler(nReps=nRepsblank, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blankLoop')
    thisExp.addLoop(blankLoop)  # add the loop to the experiment
    thisBlankLoop = blankLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlankLoop.rgb)
    if thisBlankLoop != None:
        for paramName in thisBlankLoop:
            exec('{} = thisBlankLoop[paramName]'.format(paramName))
    
    for thisBlankLoop in blankLoop:
        currentLoop = blankLoop
        # abbreviate parameter names if possible (e.g. rgb = thisBlankLoop.rgb)
        if thisBlankLoop != None:
            for paramName in thisBlankLoop:
                exec('{} = thisBlankLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "blank" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from channel_20
        send_message(signals.QCT_BLANK.to_bytes())
        ioServer.getDevice('tracker').sendMessage("start blank loop")
        # keep track of which components have finished
        blankComponents = [fixation, fixation_inner]
        for thisComponent in blankComponents:
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
        
        # --- Run Routine "blank" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *fixation_inner* updates
            
            # if fixation_inner is starting this frame...
            if fixation_inner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_inner.frameNStart = frameN  # exact frame index
                fixation_inner.tStart = t  # local t and not account for scr refresh
                fixation_inner.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_inner, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_inner.started')
                # update status
                fixation_inner.status = STARTED
                fixation_inner.setAutoDraw(True)
            
            # if fixation_inner is active this frame...
            if fixation_inner.status == STARTED:
                # update params
                pass
            
            # if fixation_inner is stopping this frame...
            if fixation_inner.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_inner.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_inner.tStop = t  # not accounting for scr refresh
                    fixation_inner.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_inner.stopped')
                    # update status
                    fixation_inner.status = FINISHED
                    fixation_inner.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from channel_20
        ioServer.getDevice('tracker').sendMessage("stop blank loop")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed nRepsblank repeats of 'blankLoop'
    
    # get names of stimulus parameters
    if blankLoop.trialList in ([], [None], None):
        params = []
    else:
        params = blankLoop.trialList[0].keys()
    # save data for this loop
    blankLoop.saveAsExcel(filename + '.xlsx', sheetName='blankLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    blankLoop.saveAsText(filename + 'blankLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialSelectLoop'

# get names of stimulus parameters
if trialSelectLoop.trialList in ([], [None], None):
    params = []
else:
    params = trialSelectLoop.trialList[0].keys()
# save data for this loop
trialSelectLoop.saveAsExcel(filename + '.xlsx', sheetName='trialSelectLoop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trialSelectLoop.saveAsText(filename + 'trialSelectLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "end" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from channel_2_2
send_message(signals.ET_START_AND_STOP.to_bytes())
ioServer.getDevice('tracker').sendMessage("bye qct")

# keep track of which components have finished
endComponents = [et_stop]
for thisComponent in endComponents:
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

# --- Run Routine "end" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *et_stop* updates
    
    # if et_stop is stopping this frame...
    if et_stop.status == STARTED:
        if bool(True):
            # keep track of stop time/frame for later
            et_stop.tStop = t  # not accounting for scr refresh
            et_stop.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'et_stop.stopped')
            # update status
            et_stop.status = FINISHED
    # Run 'Each Frame' code from channel_2_2
    if et_stop.status == NOT_STARTED:
        et_stop.status = STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if et_stop.status != FINISHED:
    et_stop.status = FINISHED
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()