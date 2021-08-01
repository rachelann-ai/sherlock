#!/usr/bin/env python3

from datetime import datetime

# Pandas for managing datasets
import pandas as pd

# Matplotlib for additional customization
from matplotlib import pyplot as plt

# Seaborn for plotting and styling
import seaborn as sns


class FF:
    def __init__(self, fis):
        self.fis = fis
        for fi in self.fis:
            fi.check_sanity_of_config()

    def get_data(self):
        pass


def display_data():
    # Read dataset
    df = pd.read_csv(r'D:\dataset\crime\garda_stations.csv', encoding="ISO-8859-1", index_col=0, header=0)

    # Display first 5 observations
    print(df[['Station', 'Divisions']].head())


def main():
    print('started at: ', datetime.now().strftime("%d/%m/%y %H:%M:%S"))

    display_data()

    print('finished at: ', datetime.now().strftime("%d/%m/%y %H:%M:%S"))


if __name__ == '__main__':
    main()
