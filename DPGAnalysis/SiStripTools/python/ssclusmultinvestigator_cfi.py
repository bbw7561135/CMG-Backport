import FWCore.ParameterSet.Config as cms

ssclusmultinvestigator = cms.EDAnalyzer('MultiplicityInvestigator',
                                        vertexCollection = cms.InputTag(""),
                                        wantInvestHist = cms.bool(True),
                                        wantVtxCorrHist = cms.bool(False),
                                        wantLumiCorrHist = cms.bool(False),
                                        wantPileupCorrHist = cms.bool(False),
                                        digiVtxCorrConfig = cms.PSet(),
                                        digiLumiCorrConfig = cms.PSet(lumiProducer=cms.InputTag("")),
                                        digiPileupCorrConfig = cms.PSet(
                                                                        pileupSummaryCollection=cms.InputTag(""),
                                                                        useVisibleVertices = cms.bool(False)
                                                                        ),
                            wantedSubDets = cms.untracked.VPSet(    
                              cms.PSet(detSelection = cms.uint32(0),detLabel = cms.string("TK"),  binMax = cms.int32(9523712/64)),
                              cms.PSet(detSelection = cms.uint32(3),detLabel = cms.string("TIB"), binMax = cms.int32(1787904/64)),
                              cms.PSet(detSelection = cms.uint32(4),detLabel = cms.string("TID"), binMax = cms.int32( 565248/64)),
                              cms.PSet(detSelection = cms.uint32(5),detLabel = cms.string("TOB"), binMax = cms.int32(3303936/64)),
                              cms.PSet(detSelection = cms.uint32(6),detLabel = cms.string("TEC"), binMax = cms.int32(3866624/64))
                            ),
                                         hitName = cms.untracked.string("cluster"),
                                         multiplicityMap = cms.InputTag("ssclustermultprod"),
                                         numberOfBins = cms.untracked.int32(500),   
                                         orbitNbin = cms.untracked.int32(1800),   
                                         scaleFactor = cms.untracked.int32(10)
                                      )

