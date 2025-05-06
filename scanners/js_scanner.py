
def scan_js_file(file_path):
    """
    Reads a JavaScript file from the given file path and returns a dictionary containing
    the language type, file path, and the file's content.

    Args:
        file_path (str): The path to the JavaScript file to be scanned.

    Returns:
        dict: A dictionary with the following keys:
            - 'language': A string indicating the language type ('javascript').
            - 'path': The path to the JavaScript file.
            - 'code': The content of the JavaScript file as a string.
    """
    with open(file_path, "r") as f:
        code = f.read()
    print("IN JS SCANNER")
    return {
        "language": "javascript",
        "path": file_path,
        "code": code
    }
