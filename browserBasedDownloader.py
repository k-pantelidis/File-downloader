import webbrowser
import pandas as pd
import os
import time
from datetime import datetime

opera_path = "Opera_Path_Here"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))


pd.set_option('display.max_colwidth', None)

def check(filez, st, completeName):
    if os.path.exists('Path_here' + file_name) == False and st == 0:
        webbrowser.get(using='opera').open_new_tab(URL)
        time.sleep(10)
        check(filez=filez, st=1, completeName=completeName)
    elif os.path.exists('Path_here' + file_name + '.suffix') == True and st == 1:
        print('Downloading...', file_name , datetime.now())
        time.sleep(10)
        check(filez=filez, st=1, completeName=completeName)
    elif os.path.exists('Path_here' + file_name) == True:
        print('Download complete for: ', file_name)


df = pd.read_csv('filesList.csv')
save_path = 'save_path'
mainPath = 'http path of file here'

for i in range(len(df)):
    file_name = df.at[i, 'url']
    URL = mainPath + df.at[i, 'url']
    completeName = os.path.join(save_path, file_name)
    print("Next file to download is: ", file_name)
    check(filez=file_name, st=0, completeName=completeName)
