import numpy as np
import pandas as pd
from model_0 import BatchGradientDescent, k_fold_validation
from utils import *


data_frames = []
for name in sorted(os.listdir(PRE)):
    data_frames.append(pd.read_csv(PRE+name))
df = pd.concat(data_frames)


# create array
X = df.drop(columns=['target']).to_numpy()
print(f"X.shape: {X.shape}")
X = np.c_[np.ones((X.shape[0], 1)), X]
print(f"X.shape: {X.shape}")
Y = df['target'].to_numpy()
print(f"Y.shape: {Y.shape}")
Y = np.reshape(Y, [Y.shape[0], 1])
print(f"Y.shape: {Y.shape}")


model = BatchGradientDescent(X, Y, 0.01)
model.train()
model.plot_loss_history()


# 2-fold validation for 1-4 degrees
k_fold_validation(X, Y, 2, 0.01, 100)
