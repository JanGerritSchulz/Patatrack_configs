# disable the EarlyFishbone in the CA
process.hltPhase2PixelTracksSoA.earlyFishbone = False
process.hltPhase2PixelTracksSoA.maxNumberOfTuples = cms.string(str(40*60*1024))
process.hltPhase2PixelTracksSoA.avgTracksPerCell = 0.5