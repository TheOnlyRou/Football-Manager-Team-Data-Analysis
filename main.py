import pandas as pd
import matplotlib.pyplot as plt


def main():
    # fortuna = pd.read_csv("Fortuna2029.csv", encoding="utf8")
    # print(fortuna)
    # print(fortuna.info())
    df = pd.read_csv("data/scoringTimeSeries/premscorers2022.csv", encoding="utf8")
    print(df.info())
    pass


if __name__ == '__main__':
    main()