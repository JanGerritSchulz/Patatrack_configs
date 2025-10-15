#!/usr/bin/env bash

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

# change directory, so that the output file is at the right place
cd "results/$dataset/$cutconfig"

# run the harvesting
cmsRun ../../../config/fullPixels_HARVESTING.py

# rename the output file
mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root DQM_FullPixels_${cutconfig}.root

cd -
