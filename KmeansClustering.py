import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('house-prices.csv')
print(df.head())

df.dropna()
x = df[['SqFt','Bedrooms']]
scaler = StandardScaler()
xscaled = scaler.fit_transform(x)

model = KMeans(n_clusters=3, random_state=42)
model.fit(xscaled)
labels = model.labels_
centroids = model.cluster_centers_
df['Cluster'] = labels
print(df.head())
