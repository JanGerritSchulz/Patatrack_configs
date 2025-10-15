# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2 --procModifiers alpaka,ngtScouting,phase2CAExtension -s L1P2GT,HLT:75e33,VALIDATION:@hltValidation --conditions auto:phase2_realistic_T33 --datatier DQMIO -n -1 --eventcontent DQMIO --geometry ExtendedRun4D110 --era Phase2C17I13M9 --filein file:step1.root --fileout file:step2_VALIDATION.root --process HLTX --inputCommands=keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT --no_exec
CONFIGNAME = "PatatrackBase"
INPUTFILEPATH = "/eos/user/j/jaschulz/cms-ngt/data"

import FWCore.ParameterSet.Config as cms
# argument parsing
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Produce and analyze HLT tracks.")
    parser.add_argument("-d", "--dataset", type=str, default="TTbar_relval", help="Dataset to be used. Most have a corresponding directory (default TTbar_relval).")
    parser.add_argument("-n", "--nevents", default=-1, type=int,  help="Number of events (default -1).")
    parser.add_argument("-s", "--skipevents", default=0, type=int,  help="Number of events to skip at the beginning (default 0).")
    parser.add_argument("--multipleFiles", default=False, action="store_true",  help="Enables processing of multiple files for TTbar + 200 PU (default False).")
    args = parser.parse_args()

    # create output directory if not there yet
    from pathlib import Path
    DATASET = args.dataset
    OUTDIR = "./results/%s/%s" % (DATASET, CONFIGNAME)
    Path(OUTDIR).mkdir(parents=True, exist_ok=True)
    NEVENTS = args.nevents
    SKIPEVENTS = args.skipevents

    if args.multipleFiles:
        INPUTFILES = cms.untracked.vstring(["file:%s/%s/step2.root" % (INPUTFILEPATH, DATASET)] +
                                           ["file:%s/%s/step2_%i.root" % (INPUTFILEPATH, DATASET, i) for i in range(9)])
    else:
        INPUTFILES = cms.untracked.vstring("file:%s/%s/step2.root" % (INPUTFILEPATH, DATASET))

else:
    DATASET = "TTbar_relval"
    OUTDIR = "."
    NEVENTS = -1
    SKIPEVENTS = 0
    INPUTFILES = cms.untracked.vstring("file:%s/%s/step2.root" % (INPUTFILEPATH, DATASET)

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
from Configuration.ProcessModifiers.alpaka_cff import alpaka
#from Configuration.ProcessModifiers.phase2CAExtension_cff import phase2CAExtension

process = cms.Process('HLTX',Phase2C17I13M9,alpaka)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtendedRun4D110Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimPhase2L1GlobalTriggerEmulator_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.step1_2024.l1tGTMenu_cff')
process.load('HLTrigger.Configuration.HLT_75e33_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


### load the new EDProducer "SimDoubletsProducerPhase2"
process.load("SimTracker.TrackerHitAssociation.simDoubletsProducerPhase2_cfi")
### load the new DQM EDAnalyzer "SimDoubletsAnalyzerPhase2"
process.load("Validation.TrackingMCTruth.simDoubletsAnalyzerPhase2_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(NEVENTS),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = INPUTFILES,
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_hlt*_*_HLT',
        'drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT'
    ),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents=cms.untracked.uint32(SKIPEVENTS)
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:%s/fullSimPixelTracks_DQMIO.root' % OUTDIR),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.Applications.ConfigBuilder import ConfigBuilder
process.hltvalidation.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "HLTX", whitelist = ("subSystemFolder",), verbose = False))
process.prevalidation.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "HLTX", whitelist = ("subSystemFolder",), verbose = False))
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T33', '')

# if __name__ == "__main__":
#     from parameterSets.Patatrack import hltPhase2PixelTracksSoA
# else:
#     import importlib
#     spec = importlib.util.spec_from_file_location("hltPhase2PixelTracksSoA", "/data/jaschulz/work/NGT-LST-measurements/config/parameterSets/Patatrack.py")
#     paramSet = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(paramSet)
#     hltPhase2PixelTracksSoA = paramSet.hltPhase2PixelTracksSoA
# process.hltPhase2PixelTracksSoA.trackQualityCuts = hltPhase2PixelTracksSoA.trackQualityCuts
# process.hltPhase2PixelTracksSoA.geometry = hltPhase2PixelTracksSoA.geometry
# process.hltPhase2PixelTracksSoA.minYsizeB1 = hltPhase2PixelTracksSoA.minYsizeB1
# process.hltPhase2PixelTracksSoA.minYsizeB2 = hltPhase2PixelTracksSoA.minYsizeB2
# process.hltPhase2PixelTracksSoA.maxDYsize12 = hltPhase2PixelTracksSoA.maxDYsize12
# process.hltPhase2PixelTracksSoA.maxDYsize = hltPhase2PixelTracksSoA.maxDYsize
# process.hltPhase2PixelTracksSoA.maxDYPred = hltPhase2PixelTracksSoA.maxDYPred
# process.hltPhase2PixelTracksSoA.cellZ0Cut = hltPhase2PixelTracksSoA.cellZ0Cut
# process.hltPhase2PixelTracksSoA.cellPtCut = hltPhase2PixelTracksSoA.cellPtCut
# process.hltPhase2PixelTracksSoA.ptmin = hltPhase2PixelTracksSoA.ptmin
# process.hltPhase2PixelTracksSoA.hardCurvCut = hltPhase2PixelTracksSoA.hardCurvCut
# process.hltPhase2PixelTracksSoA.minHitsPerNtuplet = hltPhase2PixelTracksSoA.minHitsPerNtuplet
# process.hltPhase2PixelTracks.requireQuadsFromConsecutiveLayers = False


# enable extension
# process.simDoubletsProducerPhase2.numLayersOT = 0
# process.simDoubletsAnalyzerPhase2.numLayersOT = 0

# Change the CA parameters in the SimPixelTracks
# process.simDoubletsAnalyzerPhase2.geometry = hltPhase2PixelTracksSoA.geometry
# process.simDoubletsAnalyzerPhase2.minYsizeB1 = hltPhase2PixelTracksSoA.minYsizeB1
# process.simDoubletsAnalyzerPhase2.minYsizeB2 = hltPhase2PixelTracksSoA.minYsizeB2
# process.simDoubletsAnalyzerPhase2.maxDYsize12 = hltPhase2PixelTracksSoA.maxDYsize12
# process.simDoubletsAnalyzerPhase2.maxDYsize = hltPhase2PixelTracksSoA.maxDYsize
# process.simDoubletsAnalyzerPhase2.maxDYPred = hltPhase2PixelTracksSoA.maxDYPred
# process.simDoubletsAnalyzerPhase2.cellZ0Cut = hltPhase2PixelTracksSoA.cellZ0Cut
# process.simDoubletsAnalyzerPhase2.ptmin = hltPhase2PixelTracksSoA.ptmin
# process.simDoubletsAnalyzerPhase2.hardCurvCut = hltPhase2PixelTracksSoA.hardCurvCut
# process.simDoubletsAnalyzerPhase2.minHitsPerNtuplet = hltPhase2PixelTracksSoA.minHitsPerNtuplet

# Path and EndPath definitions
process.Phase2L1GTProducer = cms.Path(process.l1tGTProducerSequence)
process.Phase2L1GTAlgoBlockProducer = cms.Path(process.l1tGTAlgoBlockProducerSequence)
process.pDoubleEGEle37_24 = cms.Path(process.DoubleEGEle3724)
process.pDoubleIsoTkPho22_12 = cms.Path(process.DoubleIsoTkPho2212)
process.pDoublePuppiJet112_112 = cms.Path(process.DoublePuppiJet112112)
process.pDoublePuppiJet160_35_mass620 = cms.Path(process.DoublePuppiJet16035Mass620)
process.pDoublePuppiTau52_52 = cms.Path(process.DoublePuppiTau5252)
process.pDoubleTkEle25_12 = cms.Path(process.DoubleTkEle2512)
process.pDoubleTkElePuppiHT_8_8_390 = cms.Path(process.DoubleTkElePuppiHT)
process.pDoubleTkMuPuppiHT_3_3_300 = cms.Path(process.DoubleTkMuPuppiHT)
process.pDoubleTkMuPuppiJetPuppiMet_3_3_60_130 = cms.Path(process.DoubleTkMuPuppiJetPuppiMet)
process.pDoubleTkMuon15_7 = cms.Path(process.DoubleTkMuon157)
process.pDoubleTkMuonTkEle5_5_9 = cms.Path(process.DoubleTkMuonTkEle559)
process.pDoubleTkMuon_4_4_OS_Dr1p2 = cms.Path(process.DoubleTkMuon44OSDr1p2)
process.pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18 = cms.Path(process.DoubleTkMuon4p5OSEr2Mass7to18)
process.pDoubleTkMuon_OS_Er1p5_Dr1p4 = cms.Path(process.DoubleTkMuonOSEr1p5Dr1p4)
process.pIsoTkEleEGEle22_12 = cms.Path(process.IsoTkEleEGEle2212)
process.pNNPuppiTauPuppiMet_55_190 = cms.Path(process.NNPuppiTauPuppiMet)
process.pPuppiHT400 = cms.Path(process.PuppiHT400)
process.pPuppiHT450 = cms.Path(process.PuppiHT450)
process.pPuppiMET200 = cms.Path(process.PuppiMET200)
process.pPuppiMHT140 = cms.Path(process.PuppiMHT140)
process.pPuppiTauTkIsoEle45_22 = cms.Path(process.PuppiTauTkIsoEle4522)
process.pPuppiTauTkMuon42_18 = cms.Path(process.PuppiTauTkMuon4218)
process.pQuadJet70_55_40_40 = cms.Path(process.QuadJet70554040)
process.pSingleEGEle51 = cms.Path(process.SingleEGEle51)
process.pSingleIsoTkEle28 = cms.Path(process.SingleIsoTkEle28)
process.pSingleIsoTkPho36 = cms.Path(process.SingleIsoTkPho36)
process.pSinglePuppiJet230 = cms.Path(process.SinglePuppiJet230)
process.pSingleTkEle36 = cms.Path(process.SingleTkEle36)
process.pSingleTkMuon22 = cms.Path(process.SingleTkMuon22)
process.pTkEleIsoPuppiHT_26_190 = cms.Path(process.TkEleIsoPuppiHT)
process.pTkElePuppiJet_28_40_MinDR = cms.Path(process.TkElePuppiJetMinDR)
process.pTkEleTkMuon10_20 = cms.Path(process.TkEleTkMuon1020)
process.pTkMuPuppiJetPuppiMet_3_110_120 = cms.Path(process.TkMuPuppiJetPuppiMet)
process.pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax = cms.Path(process.TkMuTriPuppiJetdRMaxDoubleJetdEtaMax)
process.pTkMuonDoubleTkEle6_17_17 = cms.Path(process.TkMuonDoubleTkEle61717)
process.pTkMuonPuppiHT6_320 = cms.Path(process.TkMuonPuppiHT6320)
process.pTkMuonTkEle7_23 = cms.Path(process.TkMuonTkEle723)
process.pTkMuonTkIsoEle7_20 = cms.Path(process.TkMuonTkIsoEle720)
process.pTripleTkMuon5_3_3 = cms.Path(process.TripleTkMuon533)
process.pTripleTkMuon_5_3_0_DoubleTkMuon_5_3_OS_MassTo9 = cms.Path(process.TripleTkMuon530OSMassMax9)
process.pTripleTkMuon_5_3p5_2p5_OS_Mass5to17 = cms.Path(process.TripleTkMuon53p52p5OSMass5to17)
process.prevalidation_step = cms.Path(process.prevalidation)
process.validation_step = cms.EndPath(process.hltvalidation)

process.load('Validation.RecoTrack.simPixelTrackFromRecoTrackProducerPhase2_cfi')
process.simPixelTracksFromFakePixelTracks = process.simPixelTrackFromRecoTrackProducerPhase2.clone(includeTrueTracks = cms.bool(False))
process.fakePixelTrackAnalyzer = process.simDoubletsAnalyzerPhase2.clone(folder = cms.string('Tracking/TrackingMCTruth/FakePixelTracks'),
                                                                        simDoubletsSrc = cms.InputTag('simPixelTracksFromFakePixelTracks'),
                                                                        inputIsRecoTracks = cms.bool(True))
process.simPixelTracksFromTruePixelTracks = process.simPixelTrackFromRecoTrackProducerPhase2.clone(includeFakeTracks = cms.bool(False))
process.truePixelTrackAnalyzer = process.simDoubletsAnalyzerPhase2.clone(folder = cms.string('Tracking/TrackingMCTruth/TruePixelTracks'),
                                                                        simDoubletsSrc = cms.InputTag('simPixelTracksFromTruePixelTracks'),
                                                                        inputIsRecoTracks = cms.bool(True))
process.validation_step = cms.EndPath(
    process.hltSiPhase2RecHits +        # produce the OT RecHits
    #process.hltHighPtTripletStepSeedTracks +
    #process.hltMergedPixelTracksHighPtTripletSeeds +
    process.hltMultiTrackValidation +
    # produce and analyze doublets/Ntuplets of fake RecoTracks
    process.simPixelTracksFromFakePixelTracks +
    process.fakePixelTrackAnalyzer +
    # produce and analyze doublets/Ntuplets of true RecoTracks
    process.simPixelTracksFromTruePixelTracks +
    process.truePixelTrackAnalyzer +
    # produce and analyze true doublets/Ntuplets
    process.simDoubletsProducerPhase2 +
    process.simDoubletsAnalyzerPhase2
    )

process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.Phase2L1GTProducer)
process.schedule.insert(1, process.Phase2L1GTAlgoBlockProducer)
process.schedule.insert(2, process.pDoubleEGEle37_24)
process.schedule.insert(3, process.pDoubleIsoTkPho22_12)
process.schedule.insert(4, process.pDoublePuppiJet112_112)
process.schedule.insert(5, process.pDoublePuppiJet160_35_mass620)
process.schedule.insert(6, process.pDoublePuppiTau52_52)
process.schedule.insert(7, process.pDoubleTkEle25_12)
process.schedule.insert(8, process.pDoubleTkElePuppiHT_8_8_390)
process.schedule.insert(9, process.pDoubleTkMuPuppiHT_3_3_300)
process.schedule.insert(10, process.pDoubleTkMuPuppiJetPuppiMet_3_3_60_130)
process.schedule.insert(11, process.pDoubleTkMuon15_7)
process.schedule.insert(12, process.pDoubleTkMuonTkEle5_5_9)
process.schedule.insert(13, process.pDoubleTkMuon_4_4_OS_Dr1p2)
process.schedule.insert(14, process.pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18)
process.schedule.insert(15, process.pDoubleTkMuon_OS_Er1p5_Dr1p4)
process.schedule.insert(16, process.pIsoTkEleEGEle22_12)
process.schedule.insert(17, process.pNNPuppiTauPuppiMet_55_190)
process.schedule.insert(18, process.pPuppiHT400)
process.schedule.insert(19, process.pPuppiHT450)
process.schedule.insert(20, process.pPuppiMET200)
process.schedule.insert(21, process.pPuppiMHT140)
process.schedule.insert(22, process.pPuppiTauTkIsoEle45_22)
process.schedule.insert(23, process.pPuppiTauTkMuon42_18)
process.schedule.insert(24, process.pQuadJet70_55_40_40)
process.schedule.insert(25, process.pSingleEGEle51)
process.schedule.insert(26, process.pSingleIsoTkEle28)
process.schedule.insert(27, process.pSingleIsoTkPho36)
process.schedule.insert(28, process.pSinglePuppiJet230)
process.schedule.insert(29, process.pSingleTkEle36)
process.schedule.insert(30, process.pSingleTkMuon22)
process.schedule.insert(31, process.pTkEleIsoPuppiHT_26_190)
process.schedule.insert(32, process.pTkElePuppiJet_28_40_MinDR)
process.schedule.insert(33, process.pTkEleTkMuon10_20)
process.schedule.insert(34, process.pTkMuPuppiJetPuppiMet_3_110_120)
process.schedule.insert(35, process.pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax)
process.schedule.insert(36, process.pTkMuonDoubleTkEle6_17_17)
process.schedule.insert(37, process.pTkMuonPuppiHT6_320)
process.schedule.insert(38, process.pTkMuonTkEle7_23)
process.schedule.insert(39, process.pTkMuonTkIsoEle7_20)
process.schedule.insert(40, process.pTripleTkMuon5_3_3)
process.schedule.insert(41, process.pTripleTkMuon_5_3_0_DoubleTkMuon_5_3_OS_MassTo9)
process.schedule.insert(42, process.pTripleTkMuon_5_3p5_2p5_OS_Mass5to17)
process.schedule.extend([process.prevalidation_step,process.validation_step,process.DQMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
