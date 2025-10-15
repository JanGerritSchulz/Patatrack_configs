# Instructions for producing `SimPixelTrack` DQM files in Phase-2

Clone the configuration repo:
```bash
git clone https://github.com/JanGerritSchulz/Patatrack_configs.git
cd Patatrack_confgis
```

Setup CMSSW:
```bash
# default setup
cmsrel CMSSW_16_0_0_pre1
cd CMSSW_16_0_0_pre1/src
cmsenv
git cms-init

# adding SimPixelTracks
git cms-merge-topic JanGerritSchulz:jgs_SimPixelTracks_16_0_0_pre1
scram b -j 8
cd -
```

Run CMSSW SimPixelTracks (`-n` sets number of events, `-d` the dataset). **Note**, if you are not me, you'll have to change the input files!
```bash
cmsRun -n 0 config/fullSimPixelTracks_PatatrackBase.py -n 1000 -d TTbar_200PU
```

Harvest:
```bash
bash config/harvest.sh -d TTbar_200PU -c PatatrackBase
```