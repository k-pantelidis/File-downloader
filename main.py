import pandas as pd
import os.path
import time
from datetime import datetime
import requests

pd.set_option('display.max_colwidth', None)


def check(filez, st, completeName):
    if os.path.exists('saveFolderHere/' + file_name) == False and st == 0:
        response = requests.get(URL)
        open(completeName, "wb").write(response.content)
        check(filez=filez, st=1, completeName=completeName)
    elif os.path.exists('saveFolderHere/' + file_name) == False and st == 1:
        print('Downloading...', file_name , datetime.now())
        time.sleep(5)
        check(filez=filez, st=1, completeName=completeName)
    elif os.path.exists('saveFolderHere/' + file_name) == True:
        print('Download complete for: ', file_name)


df = pd.read_csv('YOUR-CSV-LIST-GOES-HERE.csv')
save_path = 'saveFolderHere'
mainPath = 'https://addPathOfSite/'

for i in range(len(df)):
    try:
        file_name = df.at[i, 'url']
        URL = mainPath + df.at[i, 'url']
        completeName = os.path.join(save_path, file_name)
        print("Next file to download is: ", file_name, " ", datetime.now())
        check(filez=file_name, st=0, completeName=completeName)
    except:
        pass
