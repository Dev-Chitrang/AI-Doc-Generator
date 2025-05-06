from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
base_url = "https://api.aimlapi.com/v1"

# Initialize the OpenAI API client
api = OpenAI(api_key=api_key, base_url=base_url)

def generate(scanned_files):
    """
    Generates a professional README.md file based on the provided scanned code.

    This function takes a list of scanned files, each represented as a dictionary
    containing 'language', 'path', and 'code'. It extracts code snippets from the
    first three files and uses the OpenAI API to generate a README.md file with
    sections such as Project Title, Description, Features, Technologies Used, How
    to Run, and Example Usage.

    Args:
        scanned_files (list): A list of dictionaries, where each dictionary contains
                              'language', 'path', and 'code' keys representing the
                              details of the scanned files.

    Returns:
        None: The function writes the generated README content to a file named
              'README.md' in the current directory.
    """
    # print("IN generate()")

    # Define the path for the README file
    readme_path = "README.md"

    # Create code samples from the first three scanned files
    code_sample = "\n\n".join([f"// File: {f['path']}\n{f['code']}" for f in scanned_files[:3]])

    # Define the system and user prompts for the OpenAI API
    system_prompt = "You are a helpful assistant that creates professional documentation for software projects."
    user_prompt = f"""
Given the following source code snippets, generate a professional README.md file.
Include:
- Project Title
- Description
- Features
- Technologies Used
- How to Run
- Example Usage

Code Snippets:
{code_sample}

README:
"""

    # Call the OpenAI API to generate the README content
    response = api.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=1500,
    )

    # Extract the generated README content from the API response
    readme_content = response.choices[0].message.content

    # Write the generated README content to the README.md file
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md generated.")
