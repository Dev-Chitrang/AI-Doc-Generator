def scan_java_file(file_path):
    """
    Reads a Java file from the specified path and returns its contents along with metadata.

    Args:
        file_path (str): The path to the Java file to be read.

    Returns:
        dict: A dictionary containing the following keys:
            - 'language': A string indicating the programming language ('java').
            - 'path': The path to the Java file.
            - 'code': The contents of the Java file as a string.
    """
    with open(file_path, "r") as f:
        code = f.read()
    # print("IN JAVA SCANNER")
    return {
        "language": "java",
        "path": file_path,
        "code": code
    }
