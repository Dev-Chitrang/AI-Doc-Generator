def scan_python_file(file_path):
    """
    Reads a Python file and returns its content along with metadata.

    This function opens a Python file specified by the `file_path`, reads its content,
    and returns a dictionary containing the programming language, the file path, and the code itself.

    Args:
        file_path (str): The path to the Python file to be read.

    Returns:
        dict: A dictionary containing the following keys:
            - 'language': A string indicating the programming language ('python').
            - 'path': The path to the file.
            - 'code': The content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    print("IN PYTHON SCANNER")
    return {
        "language": "python",
        "path": file_path,
        "code": code
    }
