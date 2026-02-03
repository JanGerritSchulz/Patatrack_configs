##### Adjust the CA parameters for optimal efficiency

## scalars
# lower the cuts YsizeB1 and YsizeB2
process.hltPhase2PixelTracksSoA.minYsizeB1 = 15
process.hltPhase2PixelTracksSoA.minYsizeB2 = 14
# increase DYsize cuts
process.hltPhase2PixelTracksSoA.maxDYsize = 20  # !!!
process.hltPhase2PixelTracksSoA.maxDYsize12 = 15
# hardCurvCut
process.hltPhase2PixelTracksSoA.hardCurvCut = 0.02
# update z0 cut
process.hltPhase2PixelTracksSoA.cellZ0Cut = 13

## vector values
def replaceValue(geometry, cut, inner, outer, newValue):
    """
    Replaces a specific value of a specified vector cut
    
    :param geometry: the geometry parameter set
    :param cut: name of the vector cut
    :param inner: inner layer ID
    :param outer: outer layer ID
    :param newValue: the new value for this cut and layer pair
    """
    for i in range(len(geometry.phiCuts)):
        iLayer = geometry.pairGraph[2*i]
        oLayer = geometry.pairGraph[2*i + 1]
        if (iLayer == inner) and (oLayer == outer):
            setattr(geometry, cut, [(getattr(geometry, cut)[k] if i!=k else newValue) for k in range(len(geometry.phiCuts))])
# update the pt cuts
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "ptCuts",  0,  1, 0.7)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "ptCuts",  0,  2, 0.8)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "ptCuts",  0,  4, 0.6)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "ptCuts",  0, 16, 0.6)
# update inner/outer cuts
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "minInner",  0,  4,  3.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxInner",  0, 16, -3.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxOuter",  0,  4, 12.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxOuter",  0, 16, 12.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "minOuter", 17, 28,-80.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxDR",  0,  4, 8.5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxDR",  0, 16, 8.5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxDR",  1,  4, 8.5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxDR",  1, 16, 8.5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "minDZ",  1,  3,-17.0)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "maxDZ",  1,  3, 17.0)
# update the connection cuts
process.hltPhase2PixelTracksSoA.geometry.caDCACuts[12] = 0.4
process.hltPhase2PixelTracksSoA.geometry.caDCACuts[13] = 0.4
process.hltPhase2PixelTracksSoA.geometry.caDCACuts[24] = 0.4
process.hltPhase2PixelTracksSoA.geometry.caDCACuts[25] = 0.4
process.hltPhase2PixelTracksSoA.geometry.caDCACuts[28] = 0.5
process.hltPhase2PixelTracksSoA.geometry.caThetaCuts[28] = 5e-3
process.hltPhase2PixelTracksSoA.geometry.caThetaCuts[29] = 5e-3

## starting pairs
def removeStartingPair(geometry, inner, outer):
    """
    Removes the layer pair (inner, outer) from the set of starting pairs
    
    :param geometry: the geometry parameter set
    :param inner: inner layer ID
    :param outer: outer layer ID
    """
    for i in range(len(geometry.phiCuts)):
        iLayer = geometry.pairGraph[2*i]
        oLayer = geometry.pairGraph[2*i + 1]
        if (iLayer == inner) and (oLayer == outer):
            newStartingPairs = []
            newStartingPairMaxInnerR = []
            for ik, k in enumerate(geometry.startingPairs):
                if k != i:
                    newStartingPairs.append(k)
                    if hasattr(geometry, "startingPairMaxInnerR"):
                        newStartingPairMaxInnerR.append(geometry.startingPairMaxInnerR[ik])
            geometry.startingPairs = newStartingPairs
            if hasattr(geometry, "startingPairMaxInnerR"):
                geometry.startingPairMaxInnerR = newStartingPairMaxInnerR
            break
# remove (2,3)
removeStartingPair(process.hltPhase2PixelTracksSoA.geometry, 2, 3)

## number of doublets and Ntuplets
process.hltPhase2PixelTracksSoA.maxNumberOfDoublets = cms.string(str(6e6))  # 12*512*1024
process.hltPhase2PixelTracksSoA.maxNumberOfTuples = cms.string(str(200e3))       # 2*60*1024
process.hltPhase2PixelTracksSoA.avgCellsPerHit = cms.double(20)