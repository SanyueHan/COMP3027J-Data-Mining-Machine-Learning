import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv("../kc_house_data.csv")
print(df.head())

df.info()

df.hist(bins=50, figsize=(20, 15))

attributes = ['sqft_living', 'bedrooms', 'bathrooms', 'price']
scatter_matrix(df[attributes], figsize=(12, 8))

cols = ['sqft_living', 'price']
df_simple = df.loc[df['zipcode'] == 98074, cols].head(50)
df_simple['price'] = df_simple['price'].div(1000.0)
print(df_simple.head())

df_simple.info()

ax1 = df_simple.plot.scatter(x='sqft_living', y='price', c='DarkBlue', ylim=[0, 1000])

matrix = df_simple.to_numpy()
X = matrix[:, 0]
Y = matrix[:, 1]

plt.scatter(X, Y)
plt.ylim(0, 1000)
plt.ylabel("Property Price ($1000)")
plt.xlabel("Overall Living Area (sq. Feet)")
plt.show()



