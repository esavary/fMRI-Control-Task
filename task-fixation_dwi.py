#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.3.0dev6),
    on jeu 12 oct 2023 13:35:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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

# Run 'Before Experiment' code from channel2_start
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
ename = 'fixation_'+data.getDateStr(format="%Y-%m-%d")

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
expName = 'fixation'  # from the Builder filename that created this script
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
    originPath='/home/common/workspace/HCPh-fMRI-tasks/task-fixation_dwi.py',
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
ioServer = io.launchHubServer(window=win, experiment_code='fixation', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "triggerwait" ---
key_resp = keyboard.Keyboard()
et_desc = visual.TextStim(win=win, name='et_desc',
    text="We're beginning the DWI task. Please keep your eyes on the central dot.",
    font='Arial',
    pos=(0, -0.4), height=0.12, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
fixation_out = visual.ShapeStim(
    win=win, name='fixation_out',
    size=[0.075, 0.1], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[0,0,0],
    opacity=1, depth=0.0, interpolate=True)
fixation_in = visual.ShapeStim(
    win=win, name='fixation_in',
    size=[0.035, 0.047], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,1,-1],
    opacity=1, depth=-1.0, interpolate=True)
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
fixation_out_2 = visual.ShapeStim(
    win=win, name='fixation_out_2',
    size=[0.075, 0.1], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[0,0,0],
    opacity=1, depth=-3.0, interpolate=True)
fixation_in_2 = visual.ShapeStim(
    win=win, name='fixation_in_2',
    size=[0.035, 0.047], vertices='circle',
    ori=0, pos=[0, 0], anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,1,-1],
    opacity=1, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.075, fillColor=[-1,-1,-1,-1], borderColor='black', lineWidth=2.0,
    innerRadius=0.035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "triggerwait" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
triggerwaitComponents = [key_resp, et_desc]
for thisComponent in triggerwaitComponents:
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

# --- Run Routine "triggerwait" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['t', 's'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerwaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "triggerwait" ---
for thisComponent in triggerwaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "triggerwait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "fixation" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from channel2_start
send_message((signals.RUN | signals.ET_START_AND_STOP).to_bytes())
ioServer.getDevice('tracker').sendMessage("hello fixation")
# keep track of which components have finished
fixationComponents = [fixation_out, fixation_in, etRecord, fixation_out_2, fixation_in_2]
for thisComponent in fixationComponents:
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

# --- Run Routine "fixation" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1800.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_out* updates
    
    # if fixation_out is starting this frame...
    if fixation_out.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        fixation_out.frameNStart = frameN  # exact frame index
        fixation_out.tStart = t  # local t and not account for scr refresh
        fixation_out.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_out, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_out.started')
        # update status
        fixation_out.status = STARTED
        fixation_out.setAutoDraw(True)
    
    # if fixation_out is active this frame...
    if fixation_out.status == STARTED:
        # update params
        pass
    
    # if fixation_out is stopping this frame...
    if fixation_out.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_out.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            fixation_out.tStop = t  # not accounting for scr refresh
            fixation_out.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_out.stopped')
            # update status
            fixation_out.status = FINISHED
            fixation_out.setAutoDraw(False)
    
    # *fixation_in* updates
    
    # if fixation_in is starting this frame...
    if fixation_in.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_in.frameNStart = frameN  # exact frame index
        fixation_in.tStart = t  # local t and not account for scr refresh
        fixation_in.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_in, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_in.started')
        # update status
        fixation_in.status = STARTED
        fixation_in.setAutoDraw(True)
    
    # if fixation_in is active this frame...
    if fixation_in.status == STARTED:
        # update params
        pass
    
    # if fixation_in is stopping this frame...
    if fixation_in.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_in.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            fixation_in.tStop = t  # not accounting for scr refresh
            fixation_in.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_in.stopped')
            # update status
            fixation_in.status = FINISHED
            fixation_in.setAutoDraw(False)
    # *etRecord* updates
    
    # if etRecord is starting this frame...
    if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etRecord.frameNStart = frameN  # exact frame index
        etRecord.tStart = t  # local t and not account for scr refresh
        etRecord.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('etRecord.started', t)
        # update status
        etRecord.status = STARTED
    
    # if etRecord is stopping this frame...
    if etRecord.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord.tStartRefresh + 1800.0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord.tStop = t  # not accounting for scr refresh
            etRecord.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord.stopped', t)
            # update status
            etRecord.status = FINISHED
    
    # *fixation_out_2* updates
    
    # if fixation_out_2 is starting this frame...
    if fixation_out_2.status == NOT_STARTED and tThisFlip >= 1770-frameTolerance:
        # keep track of start time/frame for later
        fixation_out_2.frameNStart = frameN  # exact frame index
        fixation_out_2.tStart = t  # local t and not account for scr refresh
        fixation_out_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_out_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_out_2.started')
        # update status
        fixation_out_2.status = STARTED
        fixation_out_2.setAutoDraw(True)
    
    # if fixation_out_2 is active this frame...
    if fixation_out_2.status == STARTED:
        # update params
        pass
    
    # if fixation_out_2 is stopping this frame...
    if fixation_out_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_out_2.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            fixation_out_2.tStop = t  # not accounting for scr refresh
            fixation_out_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_out_2.stopped')
            # update status
            fixation_out_2.status = FINISHED
            fixation_out_2.setAutoDraw(False)
    
    # *fixation_in_2* updates
    
    # if fixation_in_2 is starting this frame...
    if fixation_in_2.status == NOT_STARTED and tThisFlip >= 1770-frameTolerance:
        # keep track of start time/frame for later
        fixation_in_2.frameNStart = frameN  # exact frame index
        fixation_in_2.tStart = t  # local t and not account for scr refresh
        fixation_in_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_in_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_in_2.started')
        # update status
        fixation_in_2.status = STARTED
        fixation_in_2.setAutoDraw(True)
    
    # if fixation_in_2 is active this frame...
    if fixation_in_2.status == STARTED:
        # update params
        pass
    
    # if fixation_in_2 is stopping this frame...
    if fixation_in_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_in_2.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            fixation_in_2.tStop = t  # not accounting for scr refresh
            fixation_in_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_in_2.stopped')
            # update status
            fixation_in_2.status = FINISHED
            fixation_in_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation" ---
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord.status != FINISHED:
    etRecord.status = FINISHED
# Run 'End Routine' code from channel2_start
send_message(signals.ET_START_AND_STOP.to_bytes())
ioServer.getDevice('tracker').sendMessage("bye fixation")
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1800.000000)

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
