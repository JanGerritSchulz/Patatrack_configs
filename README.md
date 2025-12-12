# Patatrack configuration repository
This repository aims for providing an easy to use workflow for Patatrack Pixel Tracking and an archieve for used configurations (for both HLT Pixel Tracking and SimPixelTracks). Below you can find instructions on how to produce and run the HLT Tracking or SimPixelTracks easily while conserving the configs at one place.

## Setup of the repo and CMSSW

First, clone this configuration repo:
```bash
git clone https://github.com/JanGerritSchulz/Patatrack_configs.git
cd Patatrack_configs
```

Then (if you don't have a CMSSW version installed yet), setup CMSSW:
```bash
# default setup
cmsrel CMSSW_16_0_0_pre1
cd CMSSW_16_0_0_pre1/src
cmsenv
git cms-init

# ------------------------------------------------------------------------
# adding SimPixelTracks (can be skipped if you don't need SimPixelTracks)
git cms-merge-topic JanGerritSchulz:jgs_SimPixelTracks_16_0_0_pre1
scram b -j 8
# ------------------------------------------------------------------------

cd -
```

Create a symbolic link `data` in the main directory of the repo that points to the directory where you store your `step2*root` input files. It expects to see a file structure like this:

```
.
├── config
├── customizations
├── data
│   ├── DATASET1
│   │   ├── step2*.root
│   │   ├── step2*.root
│   │   ├── ...
│   │   └── step2*.root
│   ├── DATASET2
│   │   ├── step2*.root
│   │   ├── step2*.root
│   │   ├── ...
│   │   └── step2*.root
│   ├── ...
│   └── DATASETX
│       ├── step2*.root
│       ├── step2*.root
│       ├── ...
│       └── step2*.root
├── scripts
├── ...
└── README.md
```

You can create the symbolic link using this command:

```bash
ln -s /path/to/your/actual/data data
```

The dataset names, `DATASET1` and so on in the tree, could be e.g. `TTbar_200PU`. The repo and config files are setup in such a way that you only need to specify the dataset when running the actual reconstruction. meaning you you can run the same config on different datasets just by changing a flag when running. More on this in the following section.


## Instructions for producing `HLT Tracking` DQM files in Phase-2

As mentioned, the idea is to easily create flexible config files for CMSSW that you can run on different datasets, different number of events, and even varying the skipping events at the beginning. This is achieved by creating the config files for HLT Tracking using the `makeTrackingConfig.sh` script. You can run it from the command line as follows:

```bash
./makeTrackingConfig.sh "PatatrackIT+3OT" --procMods phase2CAExtension,singleIterPatatrack --custom extendedResolutions addNonHPPixelTracksToMTV
```

The first argument `PatatrackIT+3OT` will be the unique name of your configuration. Optional arguments include a list of process modifiers for CMSSW (`--procMods`) and process customizations (`--custom`). While the process modifiers just need to be present in the respective CMSSW release, the customizations are part of this repo. You can find a couple useful ones in `customizations/` already, however feel free to add new ones too. The file name identifies the customization for `makeTrackingConfig.sh`.

The command will produce a config file `config/PatatrackIT+3OT_cfg.py` for HLT Tracking including the specifications you passed. 

It can be run on a given dataset via:

```bash
cmsRun -n 56 config/PatatrackIT+3OT_cfg.py -d TTbar_200PU [-n $NEVENTS] [-s SKIPPEDEVENTS]
```

Hereby, `56` is the number of threads, `TTbar_200PU` is the dataset (so, there should be some files `step2*.root` in `data/TTbar_200PU` for it to work), and optionally, you can specify the number of events to process/skip.

The CMSSW job will create a DQMIO file in the (newly created) directory `results/PatatrackIT+3OT/TTbar_200PU`. To harvest, simply run:

```bash
./runTrackingHarvesting.sh -d TTbar_200PU -c PatatrackIT+3OT
```

This will create the final output file `results/PatatrackIT+3OT/TTbar_200PU/DQM_Tracking_PatatrackIT+3OT.root` that contains all relevant histograms.


## Instructions for producing `SimPixelTrack` DQM files in Phase-2

To run the SimPixelTracks in Phase-2, the procedure is analogous to the HLT tracking in the descripted previous section.

First, create the flexible CMSSW config:

```bash
./makeSimPixelTrackConfig.sh "PatatrackIT+3OT" --procMods phase2CAExtension
```

Note, that again you can specify `--procMods` and `--custom`, but typically less are needed than in the tracking config. **Note**, the Patatrack parameters are read automatically from the `hltPhase2PixelTracksSoA` module. That means, if you modify it using either `procMods` or `custom`izations, the changes will automatically propagated to the SimPixelTracks. The command will produce a config file `config/PatatrackIT+3OT_SIM_cfg.py` (note the additional `_SIM` compared to the tracking config) for SimPixelTracks including the specifications you passed. 

Run the config on the dataset of your choice:

```bash
cmsRun -n 56 config/PatatrackIT+3OT_SIM_cfg.py -d TTbar_200PU [-n $NEVENTS] [-s SKIPPEDEVENTS]
```
