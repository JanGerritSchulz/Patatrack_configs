#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="Produce and analyze SimPixelTracks from truth and recoTracks.")
parser.add_argument("CONFIGFILE", type=str, help="CMSSW config file to be customized.")
parser.add_argument("CONFIGNAME", type=str, help="Name of the CMSSW config.")
parser.add_argument("-c", "--CUSTOMIZATION", type=str, default="NONE", help="Customization of the configuration.")
args = parser.parse_args()

CONFIGFILE = args.CONFIGFILE
CONFIGNAME = args.CONFIGNAME
OUTPUTCONFIG = "config/%s_FULL_cfg.py" % CONFIGNAME
OUTPUTDIR = OUTPUTCONFIG.rsplit('/', 1)[0]
os.makedirs(OUTPUTDIR, exist_ok=True)

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
        'process.load("Validation.RecoTrack.simPixelTrackFromRecoTrackProducerPhase2_cfi")',
        'process.simPixelTracksFromFakePixelTracks = process.simPixelTrackFromRecoTrackProducerPhase2.clone(includeTrueTracks = cms.bool(False))',
        'process.fakePixelTrackAnalyzer = process.simPixelTrackAnalyzerPhase2.clone(folder = cms.string("Tracking/TrackingMCTruth/FakePixelTracks"),',
        '                                                                        simPixelTrackSrc = cms.InputTag("simPixelTracksFromFakePixelTracks"),',
        '                                                                        inputIsRecoTracks = cms.bool(True))',
        'process.simPixelTracksFromTruePixelTracks = process.simPixelTrackFromRecoTrackProducerPhase2.clone(includeFakeTracks = cms.bool(False))',
        'process.truePixelTrackAnalyzer = process.simPixelTrackAnalyzerPhase2.clone(folder = cms.string("Tracking/TrackingMCTruth/TruePixelTracks"),',
        '                                                                        simPixelTrackSrc = cms.InputTag("simPixelTracksFromTruePixelTracks"),',
        '                                                                        inputIsRecoTracks = cms.bool(True))',
        '# additional Path definitions',
        'process.simPixelTrack_step = cms.Path(',
        '    process.HLTBeamSpotSequence +       # beamspot',
        '    process.HLTItLocalRecoSequence +    # local tracker reconstruction',
        '    process.hltSiPixelRecHits +         # reproduce the SiPixelRecHits',
        '    process.hltSiPhase2RecHits +        # produce the OT RecHits',
        '    process.hltTPClusterProducer +      # run the cluster to TrackingParticle association',
        '    process.simPixelTrackProducerPhase2 # produce the SimPixelTracks',
        ')',
        'process.validation_step = cms.EndPath(',
        '    process.hltvalidation +',
        '    process.simPixelTrackAnalyzerPhase2 +',
        '    process.simPixelTracksFromFakePixelTracks +',
        '    process.fakePixelTrackAnalyzer +',
        '    process.simPixelTracksFromTruePixelTracks +',
        '    process.truePixelTrackAnalyzer',
        ')',
        'process.schedule.insert(len(process.schedule)-2, process.simPixelTrack_step)',
        CUSTOMIZATION
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
    'for module in ["simPixelTrackAnalyzerPhase2","fakePixelTrackAnalyzer","truePixelTrackAnalyzer"]:',
    '    if hasattr(process, module):',
    '        module = getattr(process, module)',
    '        # Change the CA parameters in the SimPixelTracks',
    '        module.geometry = process.hltPhase2PixelTracksSoA.geometry',
    '        module.minYsizeB1 = process.hltPhase2PixelTracksSoA.minYsizeB1',
    '        module.minYsizeB2 = process.hltPhase2PixelTracksSoA.minYsizeB2',
    '        module.maxDYsize12 = process.hltPhase2PixelTracksSoA.maxDYsize12',
    '        module.maxDYsize = process.hltPhase2PixelTracksSoA.maxDYsize',
    '        module.maxDYPred = process.hltPhase2PixelTracksSoA.maxDYPred',
    '        module.cellZ0Cut = process.hltPhase2PixelTracksSoA.cellZ0Cut',
    '        module.ptmin = process.hltPhase2PixelTracksSoA.ptmin',
    '        module.hardCurvCut = process.hltPhase2PixelTracksSoA.hardCurvCut',
    '        module.minHitsPerNtuplet = process.hltPhase2PixelTracksSoA.minHitsPerNtuplet',
    '',
    '# enable extension in SimPixelTracks',
    'from Configuration.ProcessModifiers.phase2CAExtension_cff import phase2CAExtension',
    'for module in ["simPixelTrackAnalyzerPhase2", "simPixelTrackProducerPhase2",',
    '               "fakePixelTrackAnalyzer", "truePixelTrackAnalyzer"]:',
    '    if hasattr(process, module):',
    '        module = getattr(process, module)',
    '        phase2CAExtension.toModify(module, includeOTBarrel = True)  #, includeOTDisks = True',
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
