# change the requirement for efficient, true tracks to 100% hits being correct
process.quickTrackAssociatorByHits.Cut_RecoToSim = cms.double(0.99)
process.quickTrackAssociatorByHits.PixelHitWeight = cms.double(10000.)