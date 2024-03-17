import math
import pandas as pd
from sklearn import tree
import numpy as np

df = pd.read_csv('1127/data.csv')

df = pd.concat([pd.get_dummies(df.Temperature), df], axis=1)
df = df.drop('Temperature', axis=1)

df = pd.concat([pd.get_dummies(df.Outlook), df], axis=1)
df = df.drop('Outlook', axis=1)

df['Humidity'] = df['Humidity'].map({'High': True, 'Normal': False})
df['Wind'] = df['Wind'].map({'Strong': True, 'Weak': False})
df['PlayTennis'] = df['PlayTennis'].map({'Yes': True, 'No': False})
df.replace('True', True)
df.replace('False', False)

print(df)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(df.iloc[:, :-1], df.iloc[:, -1])

tree.plot_tree(clf)

# ent = [((df[c] == True) &).sum() for c in df.columns[:-1]]
tt = np.array([((df[c] == True) & (df['PlayTennis'] == True)).sum() for c in df.columns[:-1]])
tf = np.array([((df[c] == True) & (df['PlayTennis'] == False)).sum() for c in df.columns[:-1]])
ft = np.array([((df[c] == False) & (df['PlayTennis'] == True)).sum() for c in df.columns[:-1]])
ff = np.array([((df[c] == False) & (df['PlayTennis'] == False)).sum() for c in df.columns[:-1]])

entt = np.where((tf != 0) & (tt != 0), ((tt + tf) / 14) * (-1 * (tt / (tt + tf)) * np.log2((tt / (tt + tf))) - (tf / (tt + tf)) * np.log2((tf / (tt + tf)))), 0)
entf = np.where((ff != 0) & (ft != 0), ((ft + ff) / 14) * (-1 * (ft / (ft + ff)) * np.log2((ft / (ft + ff))) - (ff / (ft + ff)) * np.log2((ff / (ft + ff)))), 0)
ent = entt + entf
print(ent)
print(df.columns[ent.argmin()], ent.min())
