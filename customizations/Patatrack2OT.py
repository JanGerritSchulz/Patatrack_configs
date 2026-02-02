# define function to exclude layers from the pixel tracking config
def _exclude_OT_layers(hltPhase2PixelTracksSoA, layers_to_exclude = [28, 29, 30]):
    keep_indices = []
    num_pairs = len(hltPhase2PixelTracksSoA.geometry.pairGraph) // 2
    startingPairs = []
    i_new = 0
    for i in range(num_pairs):
        a = hltPhase2PixelTracksSoA.geometry.pairGraph[2*i]
        b = hltPhase2PixelTracksSoA.geometry.pairGraph[2*i + 1]
        if a not in layers_to_exclude and b not in layers_to_exclude:
            keep_indices.append(i)
            if i in hltPhase2PixelTracksSoA.geometry.startingPairs:
                startingPairs.append(i_new)
            i_new += 1
    # Now update in place
    # For pairGraph, build the new flat list from kept pairs
    new_pairGraph = []
    for i in keep_indices:
        new_pairGraph.extend([hltPhase2PixelTracksSoA.geometry.pairGraph[2*i], hltPhase2PixelTracksSoA.geometry.pairGraph[2*i+1]])
    hltPhase2PixelTracksSoA.geometry.pairGraph[:] = new_pairGraph
    # Update all other lists in place
    hltPhase2PixelTracksSoA.geometry.startingPairs[:] = startingPairs
    hltPhase2PixelTracksSoA.geometry.phiCuts[:] = [hltPhase2PixelTracksSoA.geometry.phiCuts[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.minInner[:] = [hltPhase2PixelTracksSoA.geometry.minInner[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.maxInner[:] = [hltPhase2PixelTracksSoA.geometry.maxInner[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.minOuter[:] = [hltPhase2PixelTracksSoA.geometry.minOuter[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.maxOuter[:] = [hltPhase2PixelTracksSoA.geometry.maxOuter[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.maxDR[:] = [hltPhase2PixelTracksSoA.geometry.maxDR[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.minDZ[:] = [hltPhase2PixelTracksSoA.geometry.minDZ[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.maxDZ[:] = [hltPhase2PixelTracksSoA.geometry.maxDZ[i] for i in keep_indices]
    hltPhase2PixelTracksSoA.geometry.ptCuts[:] = [hltPhase2PixelTracksSoA.geometry.ptCuts[i] for i in keep_indices]
# exclude the outer OT layer
_exclude_OT_layers(process.hltPhase2PixelTracksSoA, [30])