from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'CSCEff2022B_9'
config.General.workArea = ''
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'create_ntuple_crab_Run3Data_2022B.py'
config.JobType.maxMemoryMB = 2500 
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/SingleMuon/Run2022B-ZMu-PromptReco-v1/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/Era/Prompt/Cert_320394-325273_13TeV_PromptReco_Collisions18_JSON_eraD.txt'
#config.Data.runRange = '320394-325273' # '316998-319312 320394-325273 320394-321500 322348-322355'
config.Data.publication = True
config.Data.outputDatasetTag = 'CSCEff2022B_20220725_9'

config.Site.storageSite = 'T2_US_Wisconsin' 
