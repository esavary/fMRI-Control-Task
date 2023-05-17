#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.3.0dev6),
    on mer 17 mai 2023 11:50:01
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
import serial



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.3.0dev6'
expName = 'breath_holding_task'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
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
    originPath='/home/esavary/new/HCPh-fMRI-tasks/breath_holding_task.py',
    savePickle=True, saveWideText=True,
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:

# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='breath_holding_task', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "calibration" ---

# --- Initialize components for Routine "intro" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Waiting for trigger. To proceed manually press "t".',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instructions" ---
directions = visual.TextStim(win=win, name='directions',
    text='Breath-holding task\n\nBreathe through your nose during the whole experiment.\n\nDO NO HOLD YOUR BREATH (red color) IN THE FIRST TRIAL. \nA message will let you know when to start holding your breath in red.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "start_et" ---
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)

# --- Initialize components for Routine "breath" ---
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "breath_last" ---
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.4000, 0.4539, -0.4000], fillColor=[-0.4000, 0.4539, -0.4000],
    opacity=None, depth=0.0, interpolate=True)
polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.2500, -1.0000], fillColor=[1.0000, 0.2500, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "hold_test" ---
bh_body = visual.Rect(
    win=win, name='bh_body',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
bh_end = visual.Rect(
    win=win, name='bh_end',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.1200, -0.1200], fillColor=[1.0000, -0.1200, -0.1200],
    opacity=None, depth=-1.0, interpolate=True)
end_trial_msg = visual.TextStim(win=win, name='end_trial_msg',
    text='End of test trial\n\nPlease engage in the task and HOLD YOUR BREATH during the red colored rectangles.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "breath" ---
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "breath_last" ---
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.4000, 0.4539, -0.4000], fillColor=[-0.4000, 0.4539, -0.4000],
    opacity=None, depth=0.0, interpolate=True)
polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.2500, -1.0000], fillColor=[1.0000, 0.2500, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "hold" ---
bh_body_2 = visual.Rect(
    win=win, name='bh_body_2',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
bh_end_2 = visual.Rect(
    win=win, name='bh_end_2',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.1200, -0.1200], fillColor=[1.0000, -0.1200, -0.1200],
    opacity=None, depth=-1.0, interpolate=True)
bh_end_3 = visual.Rect(
    win=win, name='bh_end_3',
    width=(0.5, 0.02)[0], height=(0.5, 0.02)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "done" ---
finished = visual.TextStim(win=win, name='finished',
    text='Finished!\n\nPlease keep breathing at a comfortable pace',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "stop_et" ---
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)
key_resp_2 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='End of the task. Press t.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "calibration" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
calibrationComponents = []
for thisComponent in calibrationComponents:
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

# --- Run Routine "calibration" ---
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
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "calibration" ---
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [text_2, key_resp]
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
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
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
        theseKeys = key_resp.getKeys(keyList=['t','s'], waitRelease=False)
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
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructionsComponents = [directions]
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
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *directions* updates
    
    # if directions is starting this frame...
    if directions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        directions.frameNStart = frameN  # exact frame index
        directions.tStart = t  # local t and not account for scr refresh
        directions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(directions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'directions.started')
        # update status
        directions.status = STARTED
        directions.setAutoDraw(True)
    
    # if directions is active this frame...
    if directions.status == STARTED:
        # update params
        pass
    
    # if directions is stopping this frame...
    if directions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > directions.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            directions.tStop = t  # not accounting for scr refresh
            directions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'directions.stopped')
            # update status
            directions.status = FINISHED
            directions.setAutoDraw(False)
    
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- Prepare to start Routine "start_et" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code
ioServer.getDevice('tracker').sendMessage("hello")

# keep track of which components have finished
start_etComponents = [etRecord]
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
        if tThisFlipGlobal > etRecord.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord.tStop = t  # not accounting for scr refresh
            etRecord.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord.stopped', t)
            # update status
            etRecord.status = FINISHED
    
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
if etRecord.status != FINISHED:
    etRecord.status = FINISHED
# the Routine "start_et" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
normal_respiratory_rate = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='normal_respiratory_rate')
thisExp.addLoop(normal_respiratory_rate)  # add the loop to the experiment
thisNormal_respiratory_rate = normal_respiratory_rate.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNormal_respiratory_rate.rgb)
if thisNormal_respiratory_rate != None:
    for paramName in thisNormal_respiratory_rate:
        exec('{} = thisNormal_respiratory_rate[paramName]'.format(paramName))

for thisNormal_respiratory_rate in normal_respiratory_rate:
    currentLoop = normal_respiratory_rate
    # abbreviate parameter names if possible (e.g. rgb = thisNormal_respiratory_rate.rgb)
    if thisNormal_respiratory_rate != None:
        for paramName in thisNormal_respiratory_rate:
            exec('{} = thisNormal_respiratory_rate[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "breath" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    breathComponents = [polygon_4, polygon_5]
    for thisComponent in breathComponents:
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
    
    # --- Run Routine "breath" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        
        # if polygon_4 is starting this frame...
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            # update status
            polygon_4.status = STARTED
            polygon_4.setAutoDraw(True)
        
        # if polygon_4 is active this frame...
        if polygon_4.status == STARTED:
            # update params
            pass
        
        # if polygon_4 is stopping this frame...
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 2.7-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                # update status
                polygon_4.status = FINISHED
                polygon_4.setAutoDraw(False)
        
        # *polygon_5* updates
        
        # if polygon_5 is starting this frame...
        if polygon_5.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            # update status
            polygon_5.status = STARTED
            polygon_5.setAutoDraw(True)
        
        # if polygon_5 is active this frame...
        if polygon_5.status == STARTED:
            # update params
            pass
        
        # if polygon_5 is stopping this frame...
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + 2.3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                # update status
                polygon_5.status = FINISHED
                polygon_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breath" ---
    for thisComponent in breathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'normal_respiratory_rate'

# get names of stimulus parameters
if normal_respiratory_rate.trialList in ([], [None], None):
    params = []
else:
    params = normal_respiratory_rate.trialList[0].keys()
# save data for this loop
normal_respiratory_rate.saveAsText(filename + 'normal_respiratory_rate.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "breath_last" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
breath_lastComponents = [polygon_6, polygon_7]
for thisComponent in breath_lastComponents:
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

# --- Run Routine "breath_last" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_6* updates
    
    # if polygon_6 is starting this frame...
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'polygon_6.started')
        # update status
        polygon_6.status = STARTED
        polygon_6.setAutoDraw(True)
    
    # if polygon_6 is active this frame...
    if polygon_6.status == STARTED:
        # update params
        pass
    
    # if polygon_6 is stopping this frame...
    if polygon_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_6.tStartRefresh + 2.7-frameTolerance:
            # keep track of stop time/frame for later
            polygon_6.tStop = t  # not accounting for scr refresh
            polygon_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_6.stopped')
            # update status
            polygon_6.status = FINISHED
            polygon_6.setAutoDraw(False)
    
    # *polygon_7* updates
    
    # if polygon_7 is starting this frame...
    if polygon_7.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
        # keep track of start time/frame for later
        polygon_7.frameNStart = frameN  # exact frame index
        polygon_7.tStart = t  # local t and not account for scr refresh
        polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'polygon_7.started')
        # update status
        polygon_7.status = STARTED
        polygon_7.setAutoDraw(True)
    
    # if polygon_7 is active this frame...
    if polygon_7.status == STARTED:
        # update params
        pass
    
    # if polygon_7 is stopping this frame...
    if polygon_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_7.tStartRefresh + 2.3-frameTolerance:
            # keep track of stop time/frame for later
            polygon_7.tStop = t  # not accounting for scr refresh
            polygon_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_7.stopped')
            # update status
            polygon_7.status = FINISHED
            polygon_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in breath_lastComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "breath_last" ---
for thisComponent in breath_lastComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "hold_test" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
hold_testComponents = [bh_body, bh_end, end_trial_msg]
for thisComponent in hold_testComponents:
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

# --- Run Routine "hold_test" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 20.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bh_body* updates
    
    # if bh_body is starting this frame...
    if bh_body.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bh_body.frameNStart = frameN  # exact frame index
        bh_body.tStart = t  # local t and not account for scr refresh
        bh_body.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bh_body, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bh_body.started')
        # update status
        bh_body.status = STARTED
        bh_body.setAutoDraw(True)
    
    # if bh_body is active this frame...
    if bh_body.status == STARTED:
        # update params
        pass
    
    # if bh_body is stopping this frame...
    if bh_body.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bh_body.tStartRefresh + 13-frameTolerance:
            # keep track of stop time/frame for later
            bh_body.tStop = t  # not accounting for scr refresh
            bh_body.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bh_body.stopped')
            # update status
            bh_body.status = FINISHED
            bh_body.setAutoDraw(False)
    
    # *bh_end* updates
    
    # if bh_end is starting this frame...
    if bh_end.status == NOT_STARTED and tThisFlip >= 13-frameTolerance:
        # keep track of start time/frame for later
        bh_end.frameNStart = frameN  # exact frame index
        bh_end.tStart = t  # local t and not account for scr refresh
        bh_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bh_end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'bh_end.started')
        # update status
        bh_end.status = STARTED
        bh_end.setAutoDraw(True)
    
    # if bh_end is active this frame...
    if bh_end.status == STARTED:
        # update params
        pass
    
    # if bh_end is stopping this frame...
    if bh_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bh_end.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            bh_end.tStop = t  # not accounting for scr refresh
            bh_end.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bh_end.stopped')
            # update status
            bh_end.status = FINISHED
            bh_end.setAutoDraw(False)
    
    # *end_trial_msg* updates
    
    # if end_trial_msg is starting this frame...
    if end_trial_msg.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        end_trial_msg.frameNStart = frameN  # exact frame index
        end_trial_msg.tStart = t  # local t and not account for scr refresh
        end_trial_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_trial_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_trial_msg.started')
        # update status
        end_trial_msg.status = STARTED
        end_trial_msg.setAutoDraw(True)
    
    # if end_trial_msg is active this frame...
    if end_trial_msg.status == STARTED:
        # update params
        pass
    
    # if end_trial_msg is stopping this frame...
    if end_trial_msg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_trial_msg.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_trial_msg.tStop = t  # not accounting for scr refresh
            end_trial_msg.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_trial_msg.stopped')
            # update status
            end_trial_msg.status = FINISHED
            end_trial_msg.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hold_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "hold_test" ---
for thisComponent in hold_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-20.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # set up handler to look after randomisation of conditions etc
    normal_respiratory_rate_2 = data.TrialHandler(nReps=4.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='normal_respiratory_rate_2')
    thisExp.addLoop(normal_respiratory_rate_2)  # add the loop to the experiment
    thisNormal_respiratory_rate_2 = normal_respiratory_rate_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNormal_respiratory_rate_2.rgb)
    if thisNormal_respiratory_rate_2 != None:
        for paramName in thisNormal_respiratory_rate_2:
            exec('{} = thisNormal_respiratory_rate_2[paramName]'.format(paramName))
    
    for thisNormal_respiratory_rate_2 in normal_respiratory_rate_2:
        currentLoop = normal_respiratory_rate_2
        # abbreviate parameter names if possible (e.g. rgb = thisNormal_respiratory_rate_2.rgb)
        if thisNormal_respiratory_rate_2 != None:
            for paramName in thisNormal_respiratory_rate_2:
                exec('{} = thisNormal_respiratory_rate_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "breath" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        breathComponents = [polygon_4, polygon_5]
        for thisComponent in breathComponents:
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
        
        # --- Run Routine "breath" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_4* updates
            
            # if polygon_4 is starting this frame...
            if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.started')
                # update status
                polygon_4.status = STARTED
                polygon_4.setAutoDraw(True)
            
            # if polygon_4 is active this frame...
            if polygon_4.status == STARTED:
                # update params
                pass
            
            # if polygon_4 is stopping this frame...
            if polygon_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_4.tStartRefresh + 2.7-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_4.tStop = t  # not accounting for scr refresh
                    polygon_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                    # update status
                    polygon_4.status = FINISHED
                    polygon_4.setAutoDraw(False)
            
            # *polygon_5* updates
            
            # if polygon_5 is starting this frame...
            if polygon_5.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.tStart = t  # local t and not account for scr refresh
                polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.started')
                # update status
                polygon_5.status = STARTED
                polygon_5.setAutoDraw(True)
            
            # if polygon_5 is active this frame...
            if polygon_5.status == STARTED:
                # update params
                pass
            
            # if polygon_5 is stopping this frame...
            if polygon_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_5.tStartRefresh + 2.3-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_5.tStop = t  # not accounting for scr refresh
                    polygon_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                    # update status
                    polygon_5.status = FINISHED
                    polygon_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breathComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breath" ---
        for thisComponent in breathComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'normal_respiratory_rate_2'
    
    # get names of stimulus parameters
    if normal_respiratory_rate_2.trialList in ([], [None], None):
        params = []
    else:
        params = normal_respiratory_rate_2.trialList[0].keys()
    # save data for this loop
    normal_respiratory_rate_2.saveAsText(filename + 'normal_respiratory_rate_2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "breath_last" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    breath_lastComponents = [polygon_6, polygon_7]
    for thisComponent in breath_lastComponents:
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
    
    # --- Run Routine "breath_last" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_6* updates
        
        # if polygon_6 is starting this frame...
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_6.started')
            # update status
            polygon_6.status = STARTED
            polygon_6.setAutoDraw(True)
        
        # if polygon_6 is active this frame...
        if polygon_6.status == STARTED:
            # update params
            pass
        
        # if polygon_6 is stopping this frame...
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 2.7-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                # update status
                polygon_6.status = FINISHED
                polygon_6.setAutoDraw(False)
        
        # *polygon_7* updates
        
        # if polygon_7 is starting this frame...
        if polygon_7.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_7.started')
            # update status
            polygon_7.status = STARTED
            polygon_7.setAutoDraw(True)
        
        # if polygon_7 is active this frame...
        if polygon_7.status == STARTED:
            # update params
            pass
        
        # if polygon_7 is stopping this frame...
        if polygon_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_7.tStartRefresh + 2.3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_7.tStop = t  # not accounting for scr refresh
                polygon_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                # update status
                polygon_7.status = FINISHED
                polygon_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breath_lastComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breath_last" ---
    for thisComponent in breath_lastComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "hold" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    holdComponents = [bh_body_2, bh_end_2, bh_end_3]
    for thisComponent in holdComponents:
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
    
    # --- Run Routine "hold" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 25.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bh_body_2* updates
        
        # if bh_body_2 is starting this frame...
        if bh_body_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bh_body_2.frameNStart = frameN  # exact frame index
            bh_body_2.tStart = t  # local t and not account for scr refresh
            bh_body_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bh_body_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bh_body_2.started')
            # update status
            bh_body_2.status = STARTED
            bh_body_2.setAutoDraw(True)
        
        # if bh_body_2 is active this frame...
        if bh_body_2.status == STARTED:
            # update params
            pass
        
        # if bh_body_2 is stopping this frame...
        if bh_body_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bh_body_2.tStartRefresh + 13-frameTolerance:
                # keep track of stop time/frame for later
                bh_body_2.tStop = t  # not accounting for scr refresh
                bh_body_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bh_body_2.stopped')
                # update status
                bh_body_2.status = FINISHED
                bh_body_2.setAutoDraw(False)
        
        # *bh_end_2* updates
        
        # if bh_end_2 is starting this frame...
        if bh_end_2.status == NOT_STARTED and tThisFlip >= 13-frameTolerance:
            # keep track of start time/frame for later
            bh_end_2.frameNStart = frameN  # exact frame index
            bh_end_2.tStart = t  # local t and not account for scr refresh
            bh_end_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bh_end_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bh_end_2.started')
            # update status
            bh_end_2.status = STARTED
            bh_end_2.setAutoDraw(True)
        
        # if bh_end_2 is active this frame...
        if bh_end_2.status == STARTED:
            # update params
            pass
        
        # if bh_end_2 is stopping this frame...
        if bh_end_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bh_end_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                bh_end_2.tStop = t  # not accounting for scr refresh
                bh_end_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bh_end_2.stopped')
                # update status
                bh_end_2.status = FINISHED
                bh_end_2.setAutoDraw(False)
        
        # *bh_end_3* updates
        
        # if bh_end_3 is starting this frame...
        if bh_end_3.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            bh_end_3.frameNStart = frameN  # exact frame index
            bh_end_3.tStart = t  # local t and not account for scr refresh
            bh_end_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bh_end_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bh_end_3.started')
            # update status
            bh_end_3.status = STARTED
            bh_end_3.setAutoDraw(True)
        
        # if bh_end_3 is active this frame...
        if bh_end_3.status == STARTED:
            # update params
            pass
        
        # if bh_end_3 is stopping this frame...
        if bh_end_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bh_end_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                bh_end_3.tStop = t  # not accounting for scr refresh
                bh_end_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bh_end_3.stopped')
                # update status
                bh_end_3.status = FINISHED
                bh_end_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in holdComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "hold" ---
    for thisComponent in holdComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-25.000000)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "done" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [finished]
for thisComponent in doneComponents:
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

# --- Run Routine "done" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 25.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finished* updates
    
    # if finished is starting this frame...
    if finished.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished.frameNStart = frameN  # exact frame index
        finished.tStart = t  # local t and not account for scr refresh
        finished.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finished.started')
        # update status
        finished.status = STARTED
        finished.setAutoDraw(True)
    
    # if finished is active this frame...
    if finished.status == STARTED:
        # update params
        pass
    
    # if finished is stopping this frame...
    if finished.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished.tStartRefresh + 25.0-frameTolerance:
            # keep track of stop time/frame for later
            finished.tStop = t  # not accounting for scr refresh
            finished.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finished.stopped')
            # update status
            finished.status = FINISHED
            finished.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "done" ---
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-25.000000)

# --- Prepare to start Routine "stop_et" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_2
ioServer.getDevice('tracker').sendMessage("bye")

key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
stop_etComponents = [etRecord_2, key_resp_2, text_5]
for thisComponent in stop_etComponents:
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

# --- Run Routine "stop_et" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *etRecord_2* updates
    
    # if etRecord_2 is stopping this frame...
    if etRecord_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord_2.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord_2.tStop = t  # not accounting for scr refresh
            etRecord_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord_2.stopped', t)
            # update status
            etRecord_2.status = FINISHED
    
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
        theseKeys = key_resp_2.getKeys(keyList=['s','t'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_5* updates
    
    # if text_5 is starting this frame...
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        # update status
        text_5.status = STARTED
        text_5.setAutoDraw(True)
    
    # if text_5 is active this frame...
    if text_5.status == STARTED:
        # update params
        pass
    
    # if text_5 is stopping this frame...
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.stopped')
            # update status
            text_5.status = FINISHED
            text_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stop_etComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "stop_et" ---
for thisComponent in stop_etComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord_2.status != FINISHED:
    etRecord_2.status = FINISHED
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "stop_et" was not non-slip safe, so reset the non-slip timer
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
