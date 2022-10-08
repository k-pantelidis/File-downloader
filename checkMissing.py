import pandas as pd
import os

df = pd.read_csv('filesList.csv')
df2 = pd.DataFrame(columns=['filename'])
count = 0

for i in range(len(df)):
    file_name = df.at[i, 'url']
    if os.path.exists('data/' + file_name) == False:
        df2.loc[len(df2)] = file_name
        print(file_name)
        count += 1
        print(count)

df.to_csv('missing.csv', index=False)
