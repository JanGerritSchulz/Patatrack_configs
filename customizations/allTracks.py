# set the chi2/ndof selection cut for pixel tracks at the end of Patatrack to a higher value of 7
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxChi2TripletsOrQuadruplets = 7
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxChi2Quintuplets = 7
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxChi2 = 7
# disable the selection of only non-skipping quadruplets
process.hltPhase2PixelTracksCAExtension.requireQuadsFromConsecutiveLayers = False