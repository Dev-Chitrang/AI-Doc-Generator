def scan_jsx_file(file_path):
    """
    Scans a JSX file and returns its content along with metadata.

    This function opens a file specified by the given path, reads its content,
    and returns a dictionary containing the language type, file path, and the
    code itself. It also prints a message indicating that the JSX scanner is active.

    Args:
        file_path (str): The path to the JSX file to be scanned.

    Returns:
        dict: A dictionary containing:
            - 'language' (str): The language type, which is 'jsx'.
            - 'path' (str): The path to the JSX file.
            - 'code' (str): The content of the JSX file.
    """
    with open(file_path, "r") as f:
        code = f.read()
    print("IN JSX SCANNER")
    return {
        "language": "jsx",
        "path": file_path,
        "code": code
    }
