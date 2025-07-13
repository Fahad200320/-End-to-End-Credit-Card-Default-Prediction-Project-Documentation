import pandas as pd
df = pd.read_csv(r'C:\Users\sk abdul fahad\OneDrive\ml project\Data\rawdata\rawdata.csv')
df.head()
df.info()
df.isnull().sum()
import os 
os.makedirs(r'C:\Users\sk abdul fahad\OneDrive\ml project\Data\cleaneddata',exist_ok= True)
df.to_csv(r'C:\Users\sk abdul fahad\OneDrive\ml project\Data\cleaneddata\cleaned.csv',index=False)