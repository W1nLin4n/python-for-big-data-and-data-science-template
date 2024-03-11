def console_out(text):
    """
    Write text to console
    :param text: text to write
    """
    print(text)


def std_file_out(file, text):
    """
    Write text to file using standard python methods
    :param file: target file
    :param text: text to write
    """
    with open(file, mode="w") as f:
        f.write(str(text))
