#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Produce and analyze HLT tracks.")
parser.add_argument("CONFIGFILE", type=str, help="CMSSW config file to be customized.")
parser.add_argument("CONFIGNAME", type=str, help="Name of the CMSSW config.")
parser.add_argument("-c", "--CUSTOMIZATION", type=str, default="NONE", help="Customization of the configuration.")
args = parser.parse_args()

CONFIGFILE = args.CONFIGFILE
CONFIGNAME = args.CONFIGNAME
OUTPUTCONFIG = "config/%s_cfg.py" % CONFIGNAME

# load optional customizations
if args.CUSTOMIZATION == "NONE":
    CUSTOMIZATION = ""
else:
    with open(args.CUSTOMIZATION, "r") as f:
        CUSTOMIZATION = f.read()

# dictionary of input lines to the desired list of output lines
inOutLines = {
    "    input = cms.untracked.int32(-1)," : [
        "    input = cms.untracked.int32(NEVENTS),"
    ],
    "    fileNames = cms.untracked.vstring('REPLACEDINPUTFILES')," : [
        "    fileNames = INPUTFILES,"
    ],
    "    secondaryFileNames = cms.untracked.vstring()" : [
        "    secondaryFileNames = cms.untracked.vstring(),",
        "    skipEvents=cms.untracked.uint32(SKIPEVENTS)"
    ],
    "    fileName = cms.untracked.string('Tracking_DQMIO.root')," : [
        "    fileName = cms.untracked.string('file:%s/Tracking_DQMIO.root' % OUTDIR),"
    ],
    "import FWCore.ParameterSet.Config as cms" : [
        'CONFIGNAME = "%s"' % CONFIGNAME,
        '',
        'import FWCore.ParameterSet.Config as cms',
        '# argument parsing',
        'if __name__ == "__main__":',
        '    import argparse',
        '    parser = argparse.ArgumentParser(description="Produce and analyze HLT tracks.")',
        '    parser.add_argument("-d", "--dataset", type=str, default="TTbar_relval", help="Dataset to be used. Most have a corresponding directory (default TTbar_relval).")',
        '    parser.add_argument("-n", "--nevents", default=-1, type=int,  help="Number of events (default -1).")',
        '    parser.add_argument("-s", "--skipevents", default=0, type=int,  help="Number of events to skip at the beginning (default 0).")',
        '    args = parser.parse_args()',
        '',
        '    # create output directory if not there yet',
        '    from pathlib import Path',
        '    DATASET = args.dataset',
        '    OUTDIR = "./results/%s/%s" % (CONFIGNAME, DATASET)',
        '    Path(OUTDIR).mkdir(parents=True, exist_ok=True)',
        '    NEVENTS = args.nevents',
        '    SKIPEVENTS = args.skipevents',
        '',
        '    import glob',
        '    INPUTFILES = cms.untracked.vstring()',
        '    INPUTFILES.extend(["file:%s" % f for f in glob.glob("data/%s/step2*.root" % DATASET)])',
        '',
        'else:',
        '    DATASET = "TTbar_relval"',
        '    OUTDIR = "."',
        '    NEVENTS = -1',
        '    SKIPEVENTS = 0',
        '    INPUTFILES = cms.untracked.vstring("file:/shared/work/NGT-LST-measurement/data/%s/step2.root" % (DATASET))'
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
