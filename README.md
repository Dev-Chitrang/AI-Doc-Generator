```markdown
# AI Doc Generator

## Description
AI Doc Generator is a powerful tool designed to automate the creation of professional documentation for software projects. By analyzing the codebase, it generates comprehensive docstrings for functions and classes, and constructs a detailed `README.md` file to accompany the project. This tool is particularly useful for developers seeking to enhance their project documentation with minimal manual effort.

## Features
- **Automated Codebase Scanning**: Identifies and processes all code files within a project directory.
- **Docstring Generation**: Utilizes AI to add or update docstrings for functions and classes in various programming languages.
- **README.md Generation**: Leverages AI to create a professional and informative README file, summarizing the project's key aspects.
- **Error Handling**: Provides feedback on any files that fail to process, ensuring transparency and ease of debugging.

## Technologies Used
- **Python**: The core programming language for implementing the tool.
- **OpenAI API**: Utilized for AI-driven docstring and README generation.
- **GPT-4o Model**: Powers the natural language processing capabilities for generating documentation content.

## How to Run
1. **Set Up Environment**: Ensure Python is installed and the OpenAI API key is correctly configured in the environment.
2. **Execute the Script**: Run the `autodocgen.py` script from the command line.
   ```sh
   python autodocgen.py
   ```
3. **Monitor Output**: The script will provide console outputs indicating the progress of file processing and any errors encountered.

## Example Usage
Suppose you have a project directory located at `D:\Projects\MyProject`. To generate documentation, navigate to the directory containing `autodocgen.py`, and execute the following command:

```sh
python autodocgen.py
```

The tool will scan all code files within the directory, generate docstrings, and create a `README.md` file summarizing the project's details. This process greatly reduces the time and effort required to produce high-quality project documentation.

```markdown
// Example output in console:

🔎 Scanning project files...

✅ Found 10 code files to process.

✍️  Generating docstrings for PYTHON file: D:\Projects\MyProject\example.py
✅ Updated D:\Projects\MyProject\example.py

📄 Generating README.md ...

✅ README.md generated.
```

By automating the documentation process, AI Doc Generator allows developers to focus on coding while ensuring their projects are well-documented and accessible to collaborators and users.
```