# Functional MRI tasks of the Human Connectome PHantom (HCPh) study

This repository contains three functional MRI tasks implemented as *Psychopy3* experiments:

* Breath-holding task (BHT): [`task-bht_bold.psyexp`](https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/master/task-bht_bold.psyexp)
* Quality-control task (QCT): [`task-qct_bold.psyexp`](https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/master/task-qct_bold.psyexp)
* Resting-state fMRI (rest): [`task-rest_bold.psyexp`](https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/master/task-rest_bold.psyexp)

## Positive control task
The task contains a visual trial block, an eye-movement trial block, and a finger-tapping trial block.
The task was originally derived from «Version A» of the task proposed by Harvey et al.:

     Harvey J, Demetriou L, McGonigle J, Wall MB. 2018. A short, robust brain activation
     control task optimised for pharmacological fMRI studies. PeerJ 6:e5540
     doi:https://doi.org/10.7717/peerj.5540

The most prominent changes to the original task are:

- Elimination of the auditive block (since we do not plan the parcipant to wear headphones)
- Substitution of the motor task (button pressing) with a simple finger-tapping paradigm
- Enabling eye-tracking with our SR instruments device.

The original implementation of their task is found at [mattwall1103/fMRI-Control-Task](https://github.com/mattwall1103/fMRI-Control-Task). Please cite their paper whenever you use their code.

# License

These tasks are released under the terms of the Apache 2.0, in order to abide by the [NiPreps licensing principles](https://www.nipreps.org/community/licensing/). See ``NOTICE`` file for further details.
