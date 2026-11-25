import sys
import pandas as pd
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

df_test = pd.read_csv(sys.argv[1])
weights_df = pd.read_csv(sys.argv[2], index_col=0)

valid_subjects = ["Astronomy", "Herbology", "Divination", "Muggle Studies", "Ancient Runes", "Charms", "Flying"]
X_test = df_test[valid_subjects]

# Ignoramos columna de bias y sacamos media y stds
means = weights_df.loc["means", valid_subjects]
stds = weights_df.loc["stds", valid_subjects]

# Limpiar y escalar
X_test = X_test.fillna(means)
X_test_scaled = (X_test - means) / stds


houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
probabilities = {}
for house in houses:
    weights = weights_df.loc[house, valid_subjects]
    bias = weights_df.loc[house, "bias"]
    probabilities[house] = sigmoid(np.dot(X_test_scaled, weights) + bias)
probs_df = pd.DataFrame(probabilities)
predictions = probs_df.idxmax(axis=1)

output_df = pd.DataFrame({"Index": df_test["Index"], "Hogwarts House": predictions})
output_df.to_csv("houses.csv", index=False)