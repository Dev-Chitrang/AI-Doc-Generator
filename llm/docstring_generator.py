from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

# API key for OpenAI and base URL for the API endpoint
base_url = "https://api.aimlapi.com/v1"

# Initialize the OpenAI API client with the provided API key and base URL
api = OpenAI(api_key=api_key, base_url=base_url)

def generate_docstring(file_info):
    """
    Adds or updates docstrings in a given source code file.

    This function takes a dictionary containing file information and uses the OpenAI API to generate
    or update docstrings for all functions and classes in the provided source code. The function
    constructs a prompt for the API to ensure the generated documentation is meaningful and well-formatted.

    Parameters:
    file_info (dict): A dictionary containing the following keys:
        - 'language': The programming language of the source code (e.g., 'python').
        - 'path': The file path of the source code (not used in this function).
        - 'code': The source code as a string for which docstrings need to be generated or updated.

    Returns:
    str: The documented source code with added or updated docstrings.
    """
    # print("IN generate_docstring")

    code = file_info["code"]
    language = file_info["language"]

    # Construct the system and user prompts for the OpenAI API
    system_prompt = f"You are an expert {language} developer who specializes in writing clean, well-documented code."
    user_prompt = f"""
        Add or update docstrings for all functions and classes in the following {language} code.
Preserve the original structure and logic; only insert meaningful, well-formatted documentation.

Code:
        {code}

Documented Code:
        """

    # Call the OpenAI API to generate the docstrings
    response = api.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
        max_tokens=2000
    )

    # Return the content of the response which contains the documented code
    return response.choices[0].message.content
