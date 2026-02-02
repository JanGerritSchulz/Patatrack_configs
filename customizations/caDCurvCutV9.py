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
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  4.90e-02, outer= 3)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  6.68e-02, outer= 4)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  6.68e-02, outer= 16)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  8.73e-02, outer= 5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  8.73e-02, outer= 17)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.02e-01, outer= 6)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.02e-01, outer= 18)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.06e-01, outer= 7)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.06e-01, outer= 19)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.24e-02, outer= 8)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.24e-02, outer= 20)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.18e-01, outer= 9)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.18e-01, outer= 21)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.12e-01, outer= 10)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.12e-01, outer= 22)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  8.79e-02, outer= 11)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  8.79e-02, outer= 23)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.78e-09, outer= 12)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.78e-09, outer= 24)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.05e-01, outer= 13)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  1.05e-01, outer= 25)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.40e-11, outer= 14)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.40e-11, outer= 26)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.40e-11, outer= 15)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  5.40e-11, outer= 27)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  8.16e-02, outer= 28)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  4.82e-02, outer= 29)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurvCuts",  3.79e-02, outer= 30)
# set the caDCurv0 offsets
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  8.54e-04, outer= 3)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  9.13e-04, outer= 4)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  9.13e-04, outer= 16)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.67e-03, outer= 5)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.67e-03, outer= 17)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  3.65e-03, outer= 6)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  3.65e-03, outer= 18)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.16e-03, outer= 7)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.16e-03, outer= 19)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.87e-03, outer= 8)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.87e-03, outer= 20)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.04e-03, outer= 9)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.04e-03, outer= 21)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.01e-03, outer= 10)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.01e-03, outer= 22)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.15e-03, outer= 11)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.15e-03, outer= 23)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.29e-02, outer= 12)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.29e-02, outer= 24)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.33e-03, outer= 13)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.33e-03, outer= 25)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.09e-02, outer= 14)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.09e-02, outer= 26)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.12e-02, outer= 15)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  1.12e-02, outer= 27)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  8.32e-04, outer= 28)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  4.27e-04, outer= 29)
replaceValue(process.hltPhase2PixelTracksSoA.geometry, "caDCurv0",  2.76e-04, outer= 30)


