### Unify (2, 28)
def removeLayerPair(geometry, inner, outer):
    """
    Removes the layer pair (inner, outer) from the set of layer pairs
    
    :param geometry: the geometry parameter set
    :param inner: inner layer ID
    :param outer: outer layer ID
    """
    lpFullyRemoved = False
    nLp = len(geometry.phiCuts)

    while not lpFullyRemoved:
        lpFullyRemoved = True
        for i in range(nLp):
            iLayer = geometry.pairGraph[2*i]
            oLayer = geometry.pairGraph[2*i + 1]
            if (iLayer == inner) and (oLayer == outer):
                lpFullyRemoved = False
                # fix starting pair indices
                geometry.startingPairs = [(k - (k>i)) for k in geometry.startingPairs if (k != i)]
                
                # remove the layer pair
                for p in geometry.parameterNames_():
                    if (nLp == len(getattr(geometry, p))) and (p != "startingPairs"):
                        setattr(geometry, p, [getattr(geometry, p)[k] for k in range(nLp) if (k != i)])
                geometry.pairGraph = [geometry.pairGraph[k] for k in range(2*nLp) if ((k != 2*i) and (k != 2*i+1))]
                nLp -= 1
                break
            
# remove the initial layer pairs (2, 28)
removeLayerPair(process.hltPhase2PixelTracksSoA.geometry, 2, 28)

# add back the layer pair with new values
newLayerPairs = [
    #  0,  1,     2,      3,      4,      5,       6,       7,     8,      9,     10,     11
    #  i,  o, start, phiCut,  minIn,  maxIn,  minOut,  maxOut, maxDR,  minDZ,  maxDZ, ptCuts
    [  2, 28, False,   1200,    -20,     20,   -50.0,    50.0, 10000,  -35.0,   35.0,  0.85],
]

for lp in newLayerPairs:
    process.hltPhase2PixelTracksSoA.geometry.pairGraph.extend([lp[0], lp[1]])
    if lp[2]:
        process.hltPhase2PixelTracksSoA.geometry.startingPairs.extend([len(process.hltPhase2PixelTracksSoA.geometry.phiCuts)])
    for i, p in enumerate([ "phiCuts", "minInner", "maxInner", "minOuter", "maxOuter", "maxDR", "minDZ", "maxDZ", "ptCuts"], start=3):
        if hasattr(process.hltPhase2PixelTracksSoA.geometry, p):
            getattr(process.hltPhase2PixelTracksSoA.geometry, p).extend([lp[i]])