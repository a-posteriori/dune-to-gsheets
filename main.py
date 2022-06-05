#### @pipko

from getpass import getuser
from duneanalytics import DuneAnalytics

# import gspread
# import df2gspread as d2g



#------------------------------------------------------------------------

# standard modules
import json
from pathlib import Path
import os, sys
#sys.path.append((os.path.realpath(__file__)))#

import pandas as pd

# custom modules
from utils import ROOT_DIR


#------------------------------------------------------------------------



def getConfigs():
    configFile = Path(ROOT_DIR) / 'config.json'
    with open(configFile) as json_data_file:
        configs = json.load(json_data_file)

    return configs

def getUsername():
    configs = getConfigs()
    u = configs['duneanalytics']['username']
    return u

def getPassword():
    configs = getConfigs()
    p = configs['duneanalytics']['password']
    return p


def getQueryInDataFrame():
    # initialize client
    user = getUsername()
    pw = getPassword()

    if user == 'username' or pw == 'password':
        raise Exception("Username / password entry is invalid. Please update config.json")

    dune = DuneAnalytics(getUsername(), getPassword())

    # try to login
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # fetch query result id using query id
    # query id for any query can be found from the url of the query:
    # for example: 
    # https://duneanalytics.com/queries/4494/8769 => 4494
    # https://duneanalytics.com/queries/3705/7192 => 3705
    # https://duneanalytics.com/queries/3751/7276 => 3751

    result_id = dune.query_result_id(query_id=17338)

    # fetch query result & parse
    x = dune.query_result(result_id)
    d = x['data']['get_result_by_result_id']

    n = 0
    y = {}
    for a in d:
        y[n] = a['data']
        n+=1
    
    df = pd.DataFrame.from_dict(y, orient = 'index')
    return df

if __name__ == '__main__':
    df = getQueryInDataFrame()
    print(df)



