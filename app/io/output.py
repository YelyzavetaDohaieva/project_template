

def console_output(data):
    """Function that takes data as an argument and outputs it in console.

    Args:
        data (Any): Input value that will be displayed in console.

    Returns:
        obj: None.
    """
    print(data)
    return None


def file_output(data, file_name='output_file.txt'):
    """Function that takes data as an argument and writes it to file specified in the data directory.
    Adds a blank line at the end. Doesn't overwrite data if the specified file is not empty.

    Args:
        data (Any): Input value that will be written to file.
        file_name (str, optional): Name of the file to write to. Defaults to 'output_file.txt'.

    Returns:
        obj: None.
    """
    try:
        with open('D:\\Projects\\PyCharm\\project_template\\data\\' + file_name, 'a') as file_handle:
            file_handle.write(data)
            file_handle.write('\n')
    except FileNotFoundError:
        return None
    return None


def pandas_output(dataframe, file_name='output_file.csv'):
    """Function that takes a pandas.DataFrame as an argument and writes it to csv file specified in the data directory.

    Args:
        dataframe (pandas.DataFrame): Input value that will be written to file.
        file_name (str, optional): Name of the file to write to. Defaults to 'output_file.csv'.

    Returns:
        obj: None.
    """
    try:
        dataframe.to_csv('D:\\Projects\\PyCharm\\project_template\\data\\' + file_name)
    except FileNotFoundError:
        return None
    return None
