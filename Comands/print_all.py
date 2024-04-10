import pandas as pd


def print_all_note():
    df = pd.read_csv('notes.csv', sep = ',')
    print(df)
