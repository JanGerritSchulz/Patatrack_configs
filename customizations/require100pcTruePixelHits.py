# change the requirement for efficient, true tracks to 100% hits being correct
process.hltTrackAssociatorByHits.Purity_SimToReco = cms.double(0.99)
process.hltTrackAssociatorByHits.PixelHitWeight = cms.double(10000.)