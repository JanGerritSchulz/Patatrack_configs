# define function to exclude layers from the pixel tracking config
def _exclude_OT_layers(geometry, layers_to_exclude = [28, 29, 30]):
    keep_indices = []
    num_pairs = len(geometry.pairGraph) // 2
    startingPairs = []
    i_new = 0
    for i in range(num_pairs):
        a = geometry.pairGraph[2*i]
        b = geometry.pairGraph[2*i + 1]
        if a not in layers_to_exclude and b not in layers_to_exclude:
            keep_indices.append(i)
            if i in geometry.startingPairs:
                startingPairs.append(i_new)
            i_new += 1
    # Now update in place
    # For pairGraph, build the new flat list from kept pairs
    new_pairGraph = []
    for i in keep_indices:
        new_pairGraph.extend([geometry.pairGraph[2*i], geometry.pairGraph[2*i+1]])
    geometry.pairGraph[:] = new_pairGraph
    # Update all other lists in place
    for p in geometry.parameterNames_():
        if (num_pairs == len(getattr(geometry, p))) and (p != "startingPairs"):
            setattr(geometry, p, [getattr(geometry, p)[k] for k in keep_indices])
    geometry.startingPairs[:] = startingPairs
    
# exclude the OT layers
_exclude_OT_layers(process.hltPhase2PixelTracksSoA.geometry, [28, 29, 30])

process.hltPhase2PixelTracksSoA.pixelRecHitSrc = cms.InputTag('hltPhase2SiPixelRecHitsSoA')
process.hltPhase2PixelTracksSoA.ptmin = cms.double(0.9)
process.hltPhase2PixelTracksSoA.hardCurvCut = cms.double(0.0328407225)
process.hltPhase2PixelTracksSoA.minHitsPerNtuplet = cms.uint32(4)
process.hltPhase2PixelTracksSoA.maxNumberOfDoublets = cms.string(str(5*512*1024))
process.hltPhase2PixelTracksSoA.maxNumberOfTuples = cms.string(str(32*1024))
process.hltPhase2PixelTracksSoA.cellZ0Cut = cms.double(7.5)
process.hltPhase2PixelTracksSoA.minYsizeB1 = cms.int32(25)
process.hltPhase2PixelTracksSoA.minYsizeB2 = cms.int32(15)
process.hltPhase2PixelTracksSoA.maxDYsize12 = cms.int32(12)
process.hltPhase2PixelTracksSoA.maxDYsize = cms.int32(10)
process.hltPhase2PixelTracksSoA.maxDYPred = cms.int32(20)
process.hltPhase2PixelTracksSoA.avgHitsPerTrack = cms.double(7.0)
process.hltPhase2PixelTracksSoA.avgCellsPerHit = cms.double(6)
process.hltPhase2PixelTracksSoA.avgCellsPerCell = cms.double(0.151)
process.hltPhase2PixelTracksSoA.avgTracksPerCell = cms.double(0.040)
process.hltPhase2PixelTracksSoA.minHitsForSharingCut = cms.uint32(10)
process.hltPhase2PixelTracksSoA.fitNas4 = cms.bool(False)
process.hltPhase2PixelTracksSoA.useRiemannFit = cms.bool(False)
process.hltPhase2PixelTracksSoA.doSharedHitCut = cms.bool(True)
process.hltPhase2PixelTracksSoA.dupPassThrough = cms.bool(False)
process.hltPhase2PixelTracksSoA.useSimpleTripletCleaner = cms.bool(True)
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxChi2 = cms.double(5.0)
process.hltPhase2PixelTracksSoA.trackQualityCuts.minPt   = cms.double(0.9)
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxTip  = cms.double(0.3)
process.hltPhase2PixelTracksSoA.trackQualityCuts.maxZip  = cms.double(12.)
process.hltPhase2PixelTracksSoA.geometry.caDCACuts = cms.vdouble(0.15, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25)
process.hltPhase2PixelTracksSoA.geometry.caThetaCuts = cms.vdouble(0.002, 0.002, 0.002, 0.002, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003)
process.hltPhase2PixelTracksSoA.geometry.startingPairs = cms.vuint32(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
process.hltPhase2PixelTracksSoA.geometry.pairGraph = cms.vuint32(0, 1, 0, 4, 0, 16, 1, 2, 1, 4, 1, 16, 2, 3, 2, 4, 2, 16, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 0, 2, 0, 5, 0, 17, 0, 6, 0, 18, 1, 3, 1, 5, 1, 17, 1, 6, 1, 18, 11, 12, 12, 13, 13, 14, 14, 15, 23, 24, 24, 25, 25, 26, 26, 27, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 16, 18, 17, 19, 18, 20, 19, 21, 20, 22, 21, 23, 22, 24)
process.hltPhase2PixelTracksSoA.geometry.phiCuts = cms.vint32(522, 522, 522, 626, 730, 730, 626, 730, 730, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 522, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 522, 522, 522, 522, 522, 522, 522, 522)
process.hltPhase2PixelTracksSoA.geometry.minInner = cms.vdouble(-16, 4, -22, -17, 6, -22, -18, 11, -22, 23, 30, 39, 50, 65, 82, 109, -28, -35, -44, -55, -70, -87, -113, -16, 7, -22, 11, -22, -17, 9, -22, 13, -22, 137, 173, 199, 229, -142, -177, -203, -233, 23, 30, 39, 50, 65, 82, 109, -28, -35, -44, -55, -70, -87, -113)
process.hltPhase2PixelTracksSoA.geometry.maxInner = cms.vdouble(17, 22, -4, 17, 22, -6, 18, 22, -11, 28, 35, 44, 55, 70, 87, 113, -23, -30, -39, -50, -65, -82, -109, 17, 22, -7, 22, -10, 17, 22, -9, 22, -13, 142, 177, 203, 233, -137, -173, -199, -229, 28, 35, 44, 55, 70, 87, 113, -23, -30, -39, -50, -65, -82, -109)
process.hltPhase2PixelTracksSoA.geometry.maxDR = cms.vdouble(5, 5, 5, 7, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 6, 5, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 8, 6, 5, 5, 5, 6, 5, 5, 5, 9, 9, 9, 8, 8, 8, 11, 9, 9, 9, 8, 8, 8, 11)
nPairs = len(process.hltPhase2PixelTracksSoA.geometry.phiCuts)
process.hltPhase2PixelTracksSoA.geometry.minOuter = cms.vdouble([-10000] * nPairs)
process.hltPhase2PixelTracksSoA.geometry.maxOuter = cms.vdouble([ 10000] * nPairs)
process.hltPhase2PixelTracksSoA.geometry.minDZ = cms.vdouble([-10000] * nPairs)
process.hltPhase2PixelTracksSoA.geometry.maxDZ = cms.vdouble([ 10000] * nPairs)
process.hltPhase2PixelTracksSoA.geometry.ptCuts = cms.vdouble([0.85] * nPairs)
process.hltPhase2PixelTracksSoA.geometry.skipsLayers = cms.vuint32([False] * nPairs)
# fix the min and max inner for inner layer == endcap
for p in range(nPairs):
    if process.hltPhase2PixelTracksSoA.geometry.pairGraph[2*p] > 3:
        process.hltPhase2PixelTracksSoA.geometry.minInner[p] =  0.0
        process.hltPhase2PixelTracksSoA.geometry.maxInner[p] = 99.0

nLayers = len(process.hltPhase2PixelTracksSoA.geometry.caDCACuts)
if hasattr(process.hltPhase2PixelTracksSoA.geometry, "startMaxInnerR"):
    process.hltPhase2PixelTracksSoA.geometry.startMaxInnerR = cms.vdouble([99.0]    * nLayers)
if hasattr(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts"):
    process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts    = cms.vdouble([99.0]    * nLayers)
if hasattr(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0"):
    process.hltPhase2PixelTracksSoA.geometry.caDCurv0       = cms.vdouble([99.0]    * nLayers)
if hasattr(process.hltPhase2PixelTracksSoA.geometry, "fishboneCuts"):
    process.hltPhase2PixelTracksSoA.geometry.fishboneCuts   = cms.vdouble([0.99999] * nLayers)
