#!/bin/bash

### get arguments:
#   -d dataset
#   -c cutconfig
while getopts d:c: flag
do
    case "${flag}" in
        d) dataset=${OPTARG};;
        c) cutconfig=${OPTARG};;
    esac
done

# save path of current directory
theDir="${PWD}"

# change directory, so that the output file is at the right place
cd "results/$cutconfig/$dataset"

# run the harvesting
cmsRun "$theDir/config/HARVESTING_Tracking.py"

# rename the output file
mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root DQM_Tracking_${cutconfig##*/}.root

cd -
