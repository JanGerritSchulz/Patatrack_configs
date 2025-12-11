#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Produce and analyze SimPixelTracks.")
parser.add_argument("CONFIGFILE", type=str, help="CMSSW config file to be customized.")
parser.add_argument("CONFIGNAME", type=str, help="Name of the CMSSW config.")
args = parser.parse_args()

CONFIGFILE = args.CONFIGFILE
CONFIGNAME = args.CONFIGNAME
OUTPUTCONFIG = "config/%s_SIM_cfg.py" % CONFIGNAME

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
        "    fileName = cms.untracked.string('file:%s/SimPixelTracks_DQMIO.root' % OUTDIR),"
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
        '# customisation of the process.',
        '',
        '### load SimPixelTrackProducerPhase2, SimPixelTrackAnalyzerPhase2 and SimPixelTrackFromRecoPixelTrack',
        'process.load("SimTracker.TrackerHitAssociation.simPixelTrackProducerPhase2_cfi")',
        'process.load("Validation.TrackingMCTruth.simPixelTrackAnalyzerPhase2_cfi")',
        '# additional Path definitions',
        'process.simPixelTrack_step = cms.Path(',
        '    process.HLTBeamSpotSequence +       # beamspot',
        '    process.HLTItLocalRecoSequence +    # local tracker reconstruction',
        '    process.hltSiPixelRecHits +         # reproduce the SiPixelRecHits',
        '    process.hltSiPhase2RecHits +        # produce the OT RecHits',
        '    process.hltTPClusterProducer +      # run the cluster to TrackingParticle association',
        '    process.simPixelTrackProducerPhase2 # produce the SimPixelTracks',
        ')',
        'process.validation_step = cms.Path(',
        '    process.simPixelTrackAnalyzerPhase2',
        ')',
        'process.schedule.insert(len(process.schedule)-1, process.simPixelTrack_step)',
        'process.schedule.insert(len(process.schedule)-1, process.validation_step)'
    ],
    "# import of standard configurations" : [
        '# import of standard configurations',
        '# load HLT to be able to access the Patatrack settings (and apply them to SimPixelTracks at the end of the config)',
        '# and for beamspot, hits, ...',
        'process.load("HLTrigger.Configuration.HLT_75e33_trackingOnly_cff")',
        'process.load("Configuration.StandardSequences.Validation_cff")'
    ]
}

endlines = [
    '# additional end lines',
    '',
    '# apply (potentially updated) Patatrack settings to SimPixelTracks',
    'for module in [process.simPixelTrackAnalyzerPhase2]:',
    '    # Change the CA parameters in the SimPixelTracks',
    '    module.geometry = process.hltPhase2PixelTracksSoA.geometry',
    '    module.minYsizeB1 = process.hltPhase2PixelTracksSoA.minYsizeB1',
    '    module.minYsizeB2 = process.hltPhase2PixelTracksSoA.minYsizeB2',
    '    module.maxDYsize12 = process.hltPhase2PixelTracksSoA.maxDYsize12',
    '    module.maxDYsize = process.hltPhase2PixelTracksSoA.maxDYsize',
    '    module.maxDYPred = process.hltPhase2PixelTracksSoA.maxDYPred',
    '    module.cellZ0Cut = process.hltPhase2PixelTracksSoA.cellZ0Cut',
    '    module.ptmin = process.hltPhase2PixelTracksSoA.ptmin',
    '    module.hardCurvCut = process.hltPhase2PixelTracksSoA.hardCurvCut',
    '    module.minHitsPerNtuplet = process.hltPhase2PixelTracksSoA.minHitsPerNtuplet',
    '',
    '# enable extension in SimPixelTracks',
    'from Configuration.ProcessModifiers.phase2CAExtension_cff import phase2CAExtension',
    'for module in [process.simPixelTrackAnalyzerPhase2, process.simPixelTrackProducerPhase2]:',
    '    phase2CAExtension.toModify(module, includeOTBarrel = True, includeOTDisks = True)',
]

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
        
        for line in endlines:
            outFile.write(line + '\n')
