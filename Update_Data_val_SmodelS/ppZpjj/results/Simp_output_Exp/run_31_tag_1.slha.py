smodelsOutput = {
'OutputStatus' : {
    'sigmacut' : 0.001,
    'minmassgap' : 50,
    'maxcond' : 0.2,
    'ncpus' : 1,
    'model' : 'smodels.share.models.ppZpjj',
    'checkinput' : True,
    'doinvisible' : True,
    'docompress' : True,
    'computestatistics' : True,
    'testcoverage' : True,
    'combinesrs' : False,
    'file status' : 1,
    'decomposition status' : 1,
    'warnings' : 'Input file ok',
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Exp/run_31_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 11.62423,
        'upper limit (fb)' : 52.6596,
        'expected upper limit (fb)' : 19.6427,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 4800.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.2207428,
        'r_expected' : 0.5917835,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 11.624226404147999}
    }
],
'Total xsec for missing topologies (fb)' : 8.01846,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.906057,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.906027,
        'SMS' : 'PV > (t,t)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.206376,
        'SMS' : 'PV > (MET)'
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 19.64269,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 11.62423,
        'SMS' : 'PV > (jet,jet)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.906057,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.906027,
        'SMS' : 'PV > (t,t)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.206376,
        'SMS' : 'PV > (MET)'
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}