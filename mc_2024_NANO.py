# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: mc_2024 --mc --era Run3_2024 --step NANO:@PHYS+@Scout --conditions 150X_mcRun3_2024_realistic_v2 --datatier NANOAODSIM --eventcontent NANOAODSIM --fileout file:nano.root --filein file:inMINIAOD.root --no_exec -n -1 --nThreads 2
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2024_cff import Run3_2024

process = cms.Process('NANO',Run3_2024)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('PhysicsTools.NanoAOD.custom_run3scouting_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIII2024Summer24MiniAODv6/HHto2B2G-SChan-h-SChan-interference_Par-Eta-0-M-270-RelWidth-0p01_TuneCP5_13p6TeV_madgraph-pythia8/MINIAODSIM/150X_mcRun3_2024_realistic_v2-v3/2560000/64c89e7a-90bd-4036-a43c-bd028c80ec72.root'),
    #fileNames = cms.untracked.vstring('/store/mc/RunIII2024Summer24MiniAODv6/HHto2B2G-SChan-h-SChan-interference_Par-Eta-0-M-270-RelWidth-0p01_TuneCP5_13p6TeV_madgraph-pythia8/MINIAODSIM/150X_mcRun3_2024_realistic_v2-v3/2560000/0936b2fa-8c01-4ff9-908f-226486ed6e12.root'),
    #fileNames = cms.untracked.vstring('file:inMINIAOD.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('mc_2024 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:nano.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_mcRun3_2024_realistic_v2', '')

# Path and EndPath definitions
process.nanoAOD_step0 = cms.Path(process.nanoSequenceMC)
process.nanoAOD_step1 = cms.Path(process.scoutingNanoSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step0,process.nanoAOD_step1,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 2
process.options.numberOfStreams = 0

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.custom_run3scouting_cff
from PhysicsTools.NanoAOD.custom_run3scouting_cff import customiseScoutingNano 

#call to customisation function customiseScoutingNano imported from PhysicsTools.NanoAOD.custom_run3scouting_cff
process = customiseScoutingNano(process)

# End of customisation functions


# Customisation from command line
process.load("PhysicsTools.NanoAOD.custom_run3scouting_cff")
process.nanoScouting_step = cms.Path(process.nanoSequence)
process.schedule.extend([process.nanoScouting_step])

from NanoTuples.NanoTuples.nanoTuples_cff import nanoTuples_withAK15
nanoTuples_withAK15(process)

from TopQuarkAnalysis.BFragmentationAnalyzer.customizeAddAll import customizeAddWeights
customizeAddWeights(process, addClassicBFragAndDecay=True, addClassicCFragAndDecay=True, addMLBfrag=True, addMLHdamp=True, addMLNNLO=True)

# Run scouting and HLT ParticleNet on shared AK4 jets and save both score
# families in ScoutingPFJetRecluster, plus inclusive scouting SV/V0 tables, using the
# converted scouting primary vertices and the offline beam spot.
# Branch and model details: AK4_PNET_REPORT.pdf.
from PhysicsTools.PatFromScouting.scoutingToMiniAODDerivedCollections_cff import customiseScoutingNanoAK4
process = customiseScoutingNanoAK4(process)


process.source.delayReadingEventProducts = cms.untracked.bool(False)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
