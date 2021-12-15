import pandas as pd


def work_with_csv(file):
    df = pd.read_csv(file)
    print(df)
    column = input()
    row = input()
    df[column] += row
    if df[column] > 1:
        df["Success"] += "+"
    elif df[column] < 1:
        df["Failure"] += "+"
    print(df)
    return df


def main():
    file_name = input()
    work_with_csv(file_name)


if __name__ == "__main__":
    main()
