import numpy as np
import pandas as pd
from util import BatchGradientDescent, high_degree_performances, high_degree_validations


# encoding
df = pd.read_csv("insurance.csv")
enc_data = {
    'is_smoker': [1 if i == 'yes' else 0 for i in df['smoker']],
    'is_male': [1 if i == 'male' else 0 for i in df['sex']],
    'southwest': [1 if i == 'southwest' else 0 for i in df['region']],
    'southeast': [1 if i == 'southeast' else 0 for i in df['region']],
    'northwest': [1 if i == 'northwest' else 0 for i in df['region']],
    'northeast': [1 if i == 'northeast' else 0 for i in df['region']],
}
enc_df = df.join(pd.DataFrame(data=enc_data))
enc_df = enc_df.drop(columns=['sex', 'smoker', 'region'])

# scaling
features_to_scale = ['age', 'bmi', 'children', 'charges']
data = {}
min_max_dict = {}
for feature in features_to_scale:
    min_value = min(enc_df[feature])
    max_value = max(enc_df[feature])
    min_max_dict[feature] = {}
    min_max_dict[feature]['min'] = min_value
    min_max_dict[feature]['max'] = max_value
    data[feature] = [(v-min_value)/(max_value-min_value) for v in enc_df[feature]]

scaled_df = enc_df.drop(columns=features_to_scale)
scaled_df = scaled_df.join(pd.DataFrame(data=data))

# create array
X = scaled_df.drop(columns=['charges']).to_numpy()
print(f"X.shape: {X.shape}")
X1 = np.c_[np.ones((X.shape[0], 1)), X]
print(f"X.shape: {X1.shape}")
Y = scaled_df['charges'].to_numpy()
print(f"Y.shape: {Y.shape}")
Y = np.reshape(Y, [Y.shape[0], 1])
print(f"Y.shape: {Y.shape}")


# train model by specifying the total number of iteration
high_degree_performances(X, Y, 5, 0.01, 100)

# train model by auto-decided convergence based on threshold value
# high_degree_performances(X, Y, 4, 0.1)

# 2-fold validation for 1-4 degrees
high_degree_validations(X, Y, 4, 0.1, 2)
