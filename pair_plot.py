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
