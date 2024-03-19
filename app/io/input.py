import pandas as pd


def console_input(message='Enter:'):
    """Function that takes input from console and returns it.

    Args:
        message (str, optional): Message to be displayed. Defaults to 'Enter:'.

    Returns:
        str: User input from console.
    """
    user_input = input(message)
    return user_input


def file_input(file_name):
    """Function that takes input from file in the data directory and returns it.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        str: Data from file. None if file not found.
    """
    try:
        with open('D:\\Projects\\PyCharm\\project_template\\data\\' + file_name, 'r') as file_handle:
            result = file_handle.read()
    except FileNotFoundError:
        return None
    return result


def pandas_input(file_name, column_index=0):
    """Function that takes input from csv file in the data directory and returns it.

    Args:
        file_name (str): Name of the csv file to be read.
        column_index (int, optional): Index of the column with row labels.

    Returns:
        str: Data from file converted to string. None if file not found or empty.
    """
    try:
        result = pd.read_csv('D:\\Projects\\PyCharm\\project_template\\data\\' + file_name, index_col=column_index)
    except FileNotFoundError:
        return None
    return result.to_string()
