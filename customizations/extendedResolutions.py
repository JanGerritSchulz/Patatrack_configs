# extend the bin range for dz and pt to ensure a good resolution estimate
# even when the Gaussian distribution is wide
process.hltTrackValidator.histoProducerAlgoBlock.dzRes_nbin = 600
process.hltTrackValidator.histoProducerAlgoBlock.dzRes_rangeMax = 0.3
process.hltTrackValidator.histoProducerAlgoBlock.dzRes_rangeMin = -0.3
process.hltTrackValidator.histoProducerAlgoBlock.ptRes_nbin = 200
process.hltTrackValidator.histoProducerAlgoBlock.ptRes_rangeMax = 0.2
process.hltTrackValidator.histoProducerAlgoBlock.ptRes_rangeMin = -0.2