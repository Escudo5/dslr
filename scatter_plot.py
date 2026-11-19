import sys
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    if len(sys.argv) < 2:
        print("Please select dataset_train.csv")
        sys.exit()

    try:
        df = pd.read_csv(sys.argv[1])
    except Exception:
        print("Ckeck the name of the argument")
        sys.exit()

    clean_data = df[["Astronomy", "Defense Against the Dark Arts"]].dropna()
    # We use clean data because some values are missing, to avoid matplotlib mistakes, we select 2 columns before cleaning with dropna.
    plt.scatter(clean_data["Astronomy"], clean_data["Defense Against the Dark Arts"], alpha=0.5)
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")
    plt.title("Astronomy vs Defense Against the Dark Arts")
    plt.show()


read_data()