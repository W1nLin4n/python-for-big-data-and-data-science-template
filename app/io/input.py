import pandas as pd


def console_in():
    """
    Read text from console.
    :returns: text from console
    """
    return input()


def std_file_in(file):
    """
    Read text from file using standard python methods.
    :param file: source file
    :returns: text from file
    """
    with open(file) as f:
        return f.read()


def pd_file_in(file):
    """
    Read csv file using pandas
    :param file: source file
    :returns: dataframe built from csv file
    """
    return pd.read_csv(file)
