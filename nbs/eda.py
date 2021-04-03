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
df['Name'][1].split('(', 1)[0]
df['Name'][1].split('(', 1)[1]

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
df['Name'].str.contains('.')
# %%
