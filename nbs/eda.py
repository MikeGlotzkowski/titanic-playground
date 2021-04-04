# %%
import numpy as np
import pandas as pd
df = pd.read_csv('../data/train.csv')
df
# %%
df.head()
# %%
df.shape
# %%
df.columns
# %%
# (mrs) | florence briggs thayer | man name
# get Mr., Mrs., Mr off name
mrs = 'Mrs.|the Countess.'
miss = 'Miss.|Mme.|Mlle.|Ms'
mr = 'Mr.|Master.|Rev.|Dr.|Major.|Don.|Col. Oberst|Col.|Capt.|Jonkheer.'
df['Mrs'] = df['Name'].str.contains(mrs)
df['Miss'] = df['Name'].str.contains(miss)
df['Mr'] = df['Name'].str.contains(mr)
not_mrs = df['Mrs'] == False
not_miss = df['Miss'] == False
not_mr = df['Mr'] == False
missed = df[not_mrs & not_miss & not_mr]
missed

# %%
df.head()

# %%
# cut name by given name, surname, name of husband, nickname
df['Name'] = df['Name'].str.replace(f'{mrs}|{miss}|{mr}', '')
df.head()
# %%
maiden_name = df['Name'].str.split('(', n=1, expand=True)
maiden_name
# %%
maiden_name[1] = maiden_name[1].str.replace(')', '')
maiden_name
# %%
maiden_name[1]

# %%
maiden_name[1] = maiden_name[1].fillna(maiden_name[0])
maiden_name = maiden_name.rename(columns={0: 'HusbandName', 1: 'OwnName'})
maiden_name

# %%
maiden_name['HusbandName'] = np.where(maiden_name['HusbandName'] == maiden_name['OwnName'], None, maiden_name['HusbandName'])
maiden_name
# %%
df["OwnName"]= maiden_name['OwnName']
df['HusbandName']= maiden_name['HusbandName']
df.drop(columns =["Name"], inplace = True)
df
# %%
# Spouse = husband, wife (mistresses and fiancés were ignored)
df['married'] = np.where((df['SibSp'] == 1) & (pd.notna(df['HusbandName'])), True, False)
df
# %%
df['SibSp'].unique()

# %%
o = df['OwnName'].str.replace(' ', '')
o
# %%
h = pd.Series(df['HusbandName'].unique()).str.replace(' ', '')
h
# %%
o.isin(h).unique()
# %%
df[0:14]
df['married']
# %%
cond = df['OwnName'].str.replace(' ', '').isin(pd.Series(df['HusbandName'].unique()).str.replace(' ', ''))
husbands = df[cond]
df['married'] = np.where((df['married']) | (cond), True, False)
df[0:14]
# %%
