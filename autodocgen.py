import os
from scanners import scan_codebase  # from __init__.py in scanners
from llm import docstring_generator
from generator import readme_generator

def process_project(directory):
    """
    Processes a project by scanning its codebase, generating docstrings for each file,
    and creating a README.md file.

    Args:
        directory (str): The path to the project directory to be processed.

    This function performs the following steps:
    1. Scans the project directory to identify all code files.
    2. For each code file, generates and inserts docstrings using the `docstring_generator`.
    3. Writes the updated code back to the respective files.
    4. Generates a README.md file summarizing the project using the `readme_generator`.

    It prints the progress and any errors encountered during the process.
    """
    print("🔎 Scanning project files...\n")

    all_files = scan_codebase(directory)
    print(f"✅ Found {len(all_files)} code files to process.\n")

    for file_info in all_files:
        lang = file_info["language"].upper()
        path = file_info["path"]
        print(f"✍️  Generating docstrings for {lang} file: {path}")
        try:
            updated_code = docstring_generator.generate_docstring(file_info)
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated_code)
            print(f"✅ Updated {path}\n")
        except Exception as e:
            print(f"❌ Failed to update {path}: {str(e)}\n")

    print("📄 Generating README.md ...\n")
    try:
        readme_generator.generate(all_files)
    except Exception as e:
        print(f"❌ Failed to generate README.md: {str(e)}")

if __name__ == "__main__":
    project_dir = os.path.abspath(".")
    process_project(project_dir)
