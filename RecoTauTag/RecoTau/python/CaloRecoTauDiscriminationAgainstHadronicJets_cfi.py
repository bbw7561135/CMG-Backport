import FWCore.ParameterSet.Config as cms
from TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff import *
from RecoTauTag.RecoTau.TCTauAlgoParameters_cfi import *
from RecoTauTag.RecoTau.TauDiscriminatorTools import noPrediscriminants

caloRecoTauDiscriminationAgainstHadronicJets = cms.EDProducer("CaloRecoTauDiscriminationAgainstHadronicJets",
	tcTauAlgoParameters,
	CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
	Prediscriminants = noPrediscriminants
)
