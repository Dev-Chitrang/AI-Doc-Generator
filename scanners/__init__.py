from scanners.python_scanner import scan_python_file
from scanners.js_scanner import scan_js_file
from scanners.java_scanner import scan_java_file
from scanners.jsx_scanner import scan_jsx_file
from pathlib import Path

EXCLUDE_DIRS = {"node_modules", "__pycache__", ".git", ".venv", "venv", ".mypy_cache", "env"}

def scan_codebase(project_path):
    """
    Scans the codebase located at the given project path for files with specific extensions
    and processes them using the appropriate scanner function.

    Supported file types are:
    - Python (.py)
    - JavaScript (.js)
    - JSX (.jsx)
    - Java (.java)

    Files located in directories specified in EXCLUDE_DIRS are ignored.

    Args:
        project_path (str or Path): The path to the project directory to scan.

    Returns:
        list: A list containing the results of scanning each file, as returned by the respective scanner functions.
    """
    # print("IN __INIT__ FILE")
    files_info = []
    for file_path in Path(project_path).rglob("*.*"):
        if any(excl in file_path.parts for excl in EXCLUDE_DIRS):
            continue
        if file_path.suffix == ".py":
            files_info.append(scan_python_file(file_path))
            # print("PYTHON CASE")
        elif file_path.suffix == ".js":
            files_info.append(scan_js_file(file_path))
            # print("JS CASE")
        elif file_path.suffix == ".jsx":
            files_info.append(scan_jsx_file(file_path))
            # print("JSX CASE")
        elif file_path.suffix == ".java":
            files_info.append(scan_java_file(file_path))
            # print("JAVA CASE")
    return files_info
