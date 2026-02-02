#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Produce and analyze HLT tracks.")
parser.add_argument("CONFIGFILE", type=str, help="CMSSW config file to be customized.")
parser.add_argument("CONFIGNAME", type=str, help="Name of the CMSSW config.")
parser.add_argument("-c", "--CUSTOMIZATION", type=str, default="NONE", help="Customization of the configuration.")
parser.add_argument("-p", "--PATH", type=str, default=".", help="Global path to the Patatrack_configs repo.")
args = parser.parse_args()

CONFIGFILE = args.CONFIGFILE
CONFIGNAME = args.CONFIGNAME
OUTPUTCONFIG = "timing/%s_cfg.py" % CONFIGNAME
PATH = args.PATH

# load optional customizations
if args.CUSTOMIZATION == "NONE":
    CUSTOMIZATION = ""
else:
    with open(args.CUSTOMIZATION, "r") as f:
        CUSTOMIZATION = f.read()

# dictionary of input lines to the desired list of output lines
inOutLines = {
    "    fileNames = cms.untracked.vstring('REPLACEDINPUTFILES')," : [
        "    fileNames = INPUTFILES,"
    ],
    "import FWCore.ParameterSet.Config as cms" : [
        'import FWCore.ParameterSet.Config as cms',
        '# get the input files',
        'import glob',
        'INPUTFILES = cms.untracked.vstring()',
        'INPUTFILES.extend(["file:%s" % f for f in glob.glob("' + PATH + '/data/%s/step2*.root" % DATASET)])',
    ],
    "# customisation of the process." : [
        "# customisation of the process.",
        CUSTOMIZATION
    ]
}

# open input file
with open(CONFIGFILE,"r") as inFile:
    # open output file
    with open(OUTPUTCONFIG, "w") as outFile:
        # loop through input lines and eventually replace them in the output file
        for line in inFile:
            if line.rstrip('\n') in inOutLines.keys():
                for newLine in inOutLines[line.rstrip('\n')]:
                    outFile.write(newLine + "\n")
            else:
                outFile.write(line)
