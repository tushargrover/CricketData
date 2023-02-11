#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[3]:


df_players = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\01 WC_players.csv")
df_ground = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\02 Ground_Averages.csv")
df_match = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\03 ODI_Match_Totals.csv")
df_results = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\04 ODI_Match_Results.csv")
df_batsman = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\05 Batsman_Data.csv")
df_bowler = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\06 Bowler_data.csv")


# # FILE 1 - PLAYERS FILE

# In[6]:


df_players.columns


# In[9]:


df_players.isnull().sum()


# In[14]:


df_players=df_players.drop(["ID"], axis=1)
#dropping ID column as same is not important


# In[15]:


df_players.columns


# In[20]:


df_players.groupby(['Country'])['Player'].count()
#grouping by countries to check the number of players


# In[21]:


df_players.to_csv("df_players_cleaned.csv", index=False)


# # FILE 2 - GROUND FILE

# In[140]:


df_ground = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\02 Ground_Averages.csv")


# In[141]:


df_ground.columns


# In[142]:


df_ground.isnull().sum()


# In[143]:


df_ground = df_ground.drop(['Span'], axis=1)


# In[144]:


df = pd.DataFrame(df_ground)
df.max()
#maximum number of matches in a stadium


# In[145]:


maxval = df_ground[['Mat', 'Won','Runs','Wkts' ]].max()
maxval


# In[146]:


df_ground['Ground'] = df_ground['Ground'].str.split(',')


# In[147]:


df_ground1 = pd.DataFrame(df_ground['Ground'].tolist())


# In[148]:


df_ground1.head()


# In[149]:


df_groundew = pd.DataFrame(df_ground['Ground'].tolist()).fillna('').add_prefix('Ground_')


# In[152]:


df_ground = pd.concat([df_ground, df_groundew], axis=1)


# In[153]:


df_ground


# In[155]:


df_ground = df_ground.drop(['Ground'], axis=1)


# In[160]:


df_ground


# In[161]:


df_ground.to_csv("df_ground_cleaned.csv" , index = False)


# # FILE 3 - BATSMAN FILE

# In[233]:



df_batsman = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\05 Batsman_Data.csv")


# In[234]:


df_batsman.columns


# In[235]:


df_batsman.isnull().sum()


# In[236]:


df_batsman.info()


# In[237]:


df_batsman = df_batsman.drop(['Unnamed: 0'], axis=1)
df_batsman = df_batsman.drop(['Match_ID', 'Player_ID'], axis=1)
##dropped the unnecesarry column


# In[238]:


df_batsman.describe()


# In[239]:


df_batsman.Bat1.unique()


# In[243]:


df_batsman.Bat1[df_batsman.Bat1=='DNB'].count()


# In[242]:


df_batsman.drop(df_batsman.index[(df_batsman["Bat1"] =="DNB")], axis=0,inplace=True)
df_batsman.drop(df_batsman.index[(df_batsman["Bat1"] =="absent")], axis=0,inplace=True)
df_batsman.drop(df_batsman.index[(df_batsman["Bat1"] =="sub")], axis=0,inplace=True)
df_batsman.drop(df_batsman.index[(df_batsman["Bat1"] =="TDNB")], axis=0,inplace=True)
##dropped the unnecesarry rows containing DNB, absent, sub, TDNB


# In[244]:


df_batsman.Bat1[df_batsman.SR=='-'].count()


# In[245]:


df_batsman.SR.replace("-","0",inplace = True)
##replaced a particular value in a column


# In[246]:


df_batsman['Start Date'] = pd.to_datetime(df_batsman['Start Date'])
df_batsman['Start Date'] = df_batsman['Start Date'].dt.strftime('%m/%d/%Y')

##formatting of date column in a proper manner


# In[431]:


df_year = df_batsman['Start Date'].apply(lambda x: x[-4:])

## year is splitting from date column


# In[437]:


df_batsman = pd.concat([df_batsman, df_year], axis=1)

##making a new column in a table


# In[433]:


df_batsman


# In[434]:


df_batsman.columns


# In[435]:


df_batsman.columns = ['Bat1', 'Runs', 'BF', 'SR', '4s', '6s', 'Opposition', 'Ground',
       'Start Date', 'Batsman', 'Year']

##Renaming the columns


# In[436]:


df_batsman.columns


# In[247]:


df_batsman['Opposition'] = df_batsman['Opposition'].apply(lambda x: x[2:])

## removed the vs from the opposition column


# In[248]:


df_batsman['Bat2'] = df_batsman['Bat1'].apply(lambda x: x[-1:])


# In[266]:


df_batsman['Runs'] = df_batsman['Runs'].astype(int)


# In[267]:


df_batsman['Runs']


# In[272]:


mnmn = df_batsman['Runs'].max()
mnmn


# In[274]:


df_batsman['4s'] = df_batsman['4s'].astype(int)


# In[275]:


mnmnw = df_batsman['4s'].max()
mnmnw


# In[277]:



df_batsman['BF'] = df_batsman['BF'].astype(int)
df_batsman['SR'] = df_batsman['SR'].astype(float)
df_batsman['6s'] = df_batsman['6s'].astype(int)


# In[278]:


df_batsman.info()


# In[279]:


df_batsman = df_batsman.drop('Bat2',axis=1)


# In[280]:


df_batsman


# In[438]:


df_batsman.to_csv("df_batsman_cleaned.csv" , index = False)


# # FILE 4 - BOWLER FILE

# In[4]:


df_bowler = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\03 World Cup\\06 Bowler_data.csv")


# In[5]:


df_bowler.columns


# In[6]:


df_bowler = df_bowler = df_bowler.drop(["Unnamed: 0"], axis=1)


# In[7]:


df_bowler = df_bowler.drop(["Match_ID"], axis=1)


# In[8]:


df_bowler = df_bowler = df_bowler.drop(["Player_ID"], axis=1)


# In[9]:


df_bowler.columns


# In[10]:


df_bowler['Opposition'] = df_bowler['Opposition'].apply(lambda x: x[2:])


# In[11]:


df_bowler.drop(df_bowler.index[(df_bowler['Overs'] == '-')], axis=0,inplace= True)


# In[12]:


df_bowler['Ave'] = df_bowler['Ave'].replace("-", "0", inplace=False)


# In[13]:


df_bowler['SR'] = df_bowler['SR'].replace("-", "0", inplace=False)


# In[14]:


df_bowler['Start Date'] = pd.to_datetime(df_bowler['Start Date'])
df_bowler['Start Date'] = df_bowler['Start Date'].dt.strftime('%m/%d/%Y')


# In[15]:


df_yearbi = df_bowler['Start Date'].apply(lambda x: x[-4:])


# In[16]:


df_bowler = pd.concat([df_bowler, df_yearbi], axis=1)


# In[17]:


df_bowler


# In[ ]:





# In[18]:


df_bowler.columns


# In[19]:


df_bowler.Wkts.unique()


# In[20]:


df_bowler['Wkts'] = df_bowler['Wkts'].astype(int)


# In[21]:


df2 = len(df_bowler[(df_bowler['Bowler']=="Kemar Roach") & (df_bowler['Wkts']>=5)])
df2


# In[22]:


df_bowler['Bowler'] = df_bowler['Bowler'].astype(str)


# In[23]:


df_bowler.info()


# In[24]:


df_bowler['Overs'] = df_bowler['Overs'].astype(float)


# In[25]:


df_bowler['Mdns'] = df_bowler['Overs'].astype(int)


# In[26]:


df_bowler['Runs'] = df_bowler['Overs'].astype(int)


# In[27]:


df_bowler['Ave'] = df_bowler['Ave'].astype(float)


# In[28]:


df_bowler['SR'] = df_bowler['SR'].astype(float)


# In[29]:


df_bowler['Opposition'] = df_bowler['Opposition'].astype(str)


# In[30]:


df_bowler.info()


# In[32]:


df_bowler.to_csv("df_bowler_cleanednew.csv" , index = False)


# # FILE 5 - RESULTS FILE

# In[344]:


df_results


# In[345]:


df_results.columns


# In[346]:


df_results.info()


# In[348]:


df_results = df_results.drop(["Unnamed: 0"], axis=1)


# In[350]:


df_results = df_results.drop(["Match_ID", "Country_ID"], axis=1)


# In[351]:


df_results = df_results.drop(["BR"], axis=1)


# In[352]:


df_results['Start Date'] =pd.to_datetime(df_results['Start Date'])
df_results['Start Date'] =df_results['Start Date'].dt.strftime('%m/%d/%Y')


# In[353]:


df_results['Result'].unique()


# In[355]:


df_results.drop(df_results.index[(df_results['Result'] == 'n/r')], axis=0,inplace= True)


# In[356]:


df_results.drop(df_results.index[(df_results['Result'] == 'aban')], axis=0,inplace= True)


# In[357]:


df_results.drop(df_results.index[(df_results['Result'] == 'canc')], axis=0,inplace= True)


# In[358]:


df_results.drop(df_results.index[(df_results['Result'] == '-')], axis=0,inplace= True)


# In[359]:


df_results['Result'].unique()


# In[361]:


df4 = len(df_results[(df_results['Toss']=="won") & (df_results['Bat']=="1st") & (df_results['Result']=="won")])
df4


# In[363]:


df3 = len(df_results[(df_results['Toss']=="won") & (df_results['Bat']=="2nd") & (df_results['Result']=="won")])
df3


# In[368]:


df6 = len(df_results[(df_results['Toss']=="lost") & (df_results['Bat']=="1st") & (df_results['Result']=="won")])
df6


# In[365]:


df7 = len(df_results[(df_results['Toss']=="lost") & (df_results['Bat']=="2nd") & (df_results['Result']=="won")])
df7


# In[367]:


df9 = len(df_results[(df_results['Toss']=="won") & (df_results['Bat']=="1st") & (df_results['Result']=="lost")])
df9


# In[369]:


df10 = len(df_results[(df_results['Toss']=="won") & (df_results['Bat']=="2nd") & (df_results['Result']=="lost")])
df10


# In[371]:


df_results['Opposition'] = df_results['Opposition'].apply(lambda x: x[2:])


# In[372]:


df_results


# In[381]:


df_results['Result'].value_counts(normalize=True)


# In[396]:


de =df_results.groupby(['Country','Result','Bat'])['Result'].count()
de


# In[397]:


df_results.to_csv("df_results_cleaned.csv" , index = False)


# # FILE 6 - MATCH FILE

# In[398]:


df_match.columns


# In[400]:


df_match = df_match.drop(['Unnamed: 0'], axis=1)


# In[408]:


df_match = df_match.drop(['RPO'], axis=1)


# In[401]:


df_match = df_match.drop(['Match_ID'], axis=1)


# In[402]:


df_match = df_match.drop(['Country_ID'], axis=1)


# In[409]:


df_match.columns


# In[407]:


df_match['Start Date'] = pd.to_datetime(df_match['Start Date'])
df_match['Start Date'] = df_match['Start Date'].dt.strftime('%m/%d/%Y')


# In[410]:


df_match['Opposition'] =df_match['Opposition'].apply(lambda x:x[2:])


# In[412]:


df_match.Result.unique()


# In[413]:


df_match.drop(df_match.index[(df_match['Result'] =='n/r')], axis=0,inplace= True)


# In[414]:


df_match.drop(df_match.index[(df_match['Result'] =='-')], axis=0,inplace= True)


# In[415]:


df_match.Result.unique()


# In[416]:


df_match.columns


# In[425]:


df_match.to_csv("df_match_cleaned.csv" , index = False)


# In[426]:


df_match


# In[430]:


de = df_match.groupby(['Country','Opposition', 'Result'])['Opposition'].count()
de

