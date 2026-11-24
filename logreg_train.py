import sys
import pandas as pd
import numpy as np


def read_data():
    if len(sys.argv) < 2:
        print("Please select dataset_train.csv")
        sys.exit()

    try:
        df = pd.read_csv(sys.argv[1])
    except Exception:
        print("Ckeck the name of the argument")
        sys.exit()
    return df

def preprocess_data(df): # ESTANDARIZACION
    # We choose these subjects because of their data importance compared to other subjetcs 
    valid_subjects = ["Astronomy", "Herbology", "Divination", "Muggle Studies", "Ancient Runes", "Charms", "Flying"]

    # ********* NASA math incoming ***********
    # Average and standard deviation

    X = df[valid_subjects]
    means = X.mean()
    stds = X.std()

    # Save empty spaces with average
    X = X.fillna(means)
    X_scaled = (X - means) / stds

    # HASTA AHORA HEMOS ESTANDARIZADO LOS VALORES.
    # CENTRAMOS CADA ASIGNATURA Y MEDIMOS CUANTO SE ALEJA CADA ALUMNO DE LA MEDIA
    return X_scaled, means, stds

def sigmoid(z):
    res = 1 / (1 + np.exp(-z))
    return res


def train(X_scaled, df, house, lr=0.1, iterations=1000):
    # Etiquetas binarias (y): es de esa casa o no.
    y = np.where(df["Hogwarts House"] == house, 1, 0)

    # Pesos (w) y sesgo (b)
    weights = np.zeros(X_scaled.shape[1])  # Shape = filas, columnas (1600, 7 asignaturas). En este caso 7 asignaturas
    # Pone a 0 el peso de las 7 asignaturas
    bias = 0
    m = X_scaled.shape[0] # numero total de alumnos

    for _ in range(iterations): # bucle de entrenamiento
        predictions = sigmoid(np.dot(X_scaled, weights)+ bias)
        error = predictions - y # Descenso de gradiente
        dw = (1 / m) * np.dot(X_scaled.T, error) # .T gira la tabla, cambia filas por columnas
        db = (1 / m) * np.sum(error)
        weights = weights - lr * dw
        bias = bias - lr * db
    return weights, bias



def train_all(X_scaled, df):
    models = {}
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    for house in houses:
        weight, bias = train(X_scaled, df, house)
        models[house] = (weight, bias)
    return models


def save_weights(models, means, stds):
    data = {}
    for house, (weights, bias) in models.items(): # recorremos el diccionario de casas y sacamos peso y sesgo
        data[house] = list(weights) + [bias]

    # Cada casa tiene 7 sesgos y 1 peso
    data["means"] = list(means) + [0] # añadimos 0 como relleno para que ambas tablas tngan 8 elementos
    data["stds"] = list(stds) + [0]

    columns = list(means.index) + ["bias"]
    weights_df = pd.DataFrame.from_dict(data, orient="index", columns=columns) # por defecto pandas convierte las claves de un dicc en columnas, aqui indicamos que sean filas
    weights_df.to_csv("weights.csv")

df = read_data()
X_scaled, means, stds = preprocess_data(df)
models = train_all(X_scaled, df)
save_weights(models, means, stds)



