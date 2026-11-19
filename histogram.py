import pandas as pd
import matplotlib.pyplot as plt
import sys

def read_data():
    if len(sys.argv) < 2:
        print("Please select dataset_train.csv")
        sys.exit()

    try:
        df = pd.read_csv(sys.argv[1])
    except Exception:
        print("Ckeck the name of the argument")
        sys.exit()
    # filter all houses
    # from house == gryffindor, filter subject care of magical creatures.
    # dropna means don´t show blank values
    gryffindor_grades = df[df["Hogwarts House"] == "Gryffindor"]["Care of Magical Creatures"].dropna()
    slitheryn_grades = df[df["Hogwarts House"] == "Slytherin"]["Care of Magical Creatures"].dropna()
    hufflepuff_grades = df[df["Hogwarts House"] == "Hufflepuff"]["Care of Magical Creatures"].dropna()
    ravenclaw_grades = df[df["Hogwarts House"] == "Ravenclaw"]["Care of Magical Creatures"].dropna()

    plt.hist(gryffindor_grades, alpha= 0.5, label="Gryffindor", bins=30, color= "red")
    plt.hist(slitheryn_grades, alpha= 0.5, label="Slytherin", bins=30, color="green")
    plt.hist(hufflepuff_grades, alpha= 0.5, label="Hufflepuff", bins=30, color="gold")
    plt.hist(ravenclaw_grades, alpha= 0.5, label="Ravenclaw", bins=30, color="blue")

    plt.legend()
    plt.title("Care of Magical Creatures")
    plt.show()






read_data()

