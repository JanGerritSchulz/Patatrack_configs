## dCurv cut for quadruplets
def replaceValue(geometry, cut, newValue, inner=None, outer=None):
    """
    Replaces a specific value of a specified vector cut
    
    :param geometry: the geometry parameter set
    :param cut: name of the vector cut
    :param newValue: the new value for this cut and layer pair
    :param inner: inner layer ID
    :param outer: outer layer ID
    """
    for i in range(len(geometry.phiCuts)):
        iLayer = geometry.pairGraph[2*i]
        oLayer = geometry.pairGraph[2*i + 1]
        if ((inner is None) or (iLayer == inner)) and ((outer is None) or (oLayer == outer)):
            setattr(geometry, cut, [(getattr(geometry, cut)[k] if i!=k else newValue) for k in range(len(geometry.phiCuts))])

# set the caDCurv cuts
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[3] =  4.90e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[4] =  6.68e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[16] =  6.68e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[5] =  8.73e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[17] =  8.73e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[6] =  1.02e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[18] =  1.02e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[7] =  1.06e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[19] =  1.06e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[8] =  5.24e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[20] =  5.24e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[9] =  1.18e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[21] =  1.18e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[10] =  1.12e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[22] =  1.12e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[11] =  8.79e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[23] =  8.79e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[12] =  1.78e-09
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[24] =  1.78e-09
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[13] =  1.05e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[25] =  1.05e-01
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[14] =  5.40e-11
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[26] =  5.40e-11
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[15] =  5.40e-11
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[27] =  5.40e-11
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[28] =  8.16e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[29] =  4.82e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurvCuts[30] =  3.79e-02
# set the caDCurv0 offsets
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[3] = 8.54e-04
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[4] = 9.13e-04
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[16] = 9.13e-04
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[5] = 1.67e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[17] = 1.67e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[6] = 3.65e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[18] = 3.65e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[7] = 4.16e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[19] = 4.16e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[8] = 4.87e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[20] = 4.87e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[9] = 4.04e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[21] = 4.04e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[10] = 4.01e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[22] = 4.01e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[11] = 4.15e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[23] = 4.15e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[12] = 1.29e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[24] = 1.29e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[13] = 4.33e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[25] = 4.33e-03
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[14] = 1.09e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[26] = 1.09e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[15] = 1.12e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[27] = 1.12e-02
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[28] = 8.32e-04
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[29] = 4.27e-04
process.hltPhase2PixelTracksSoA.geometry.caDCurv0[30] = 2.76e-04

