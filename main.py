import pandas as pd
import matplotlib.pyplot as plt


def main():
    fortuna = pd.read_csv("Fortuna2029.csv", encoding="windows-1252")
    print(fortuna)
    print(fortuna.info())
    pass


if __name__ == '__main__':
    main()