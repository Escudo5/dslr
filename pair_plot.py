import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data():
    if len(sys.argv) < 2:
        print("Please select dataset_train.csv")
        sys.exit()

    try:
        df = pd.read_csv(sys.argv[1])
    except Exception:
        print("Ckeck the name of the argument")
        sys.exit()

# quitamos index y columnas innecesarias
    column = ["Hogwarts House","Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    clean_data = df[column].dropna()
    sns.pairplot(clean_data, hue="Hogwarts House")
    plt.show()

read_data()