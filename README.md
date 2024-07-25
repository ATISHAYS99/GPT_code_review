﻿GPT_code_review review system
By Atishay Sharma


Setting Up the Project
Clone the Repository:

    git clone https://github.com/ATISHAYS99/GPT_code_review.git
    cd project_directory

Install Dependencies:
Ensure you have Python installed. Create a virtual environment and install the required packages.

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install requirements.txt

Create a .env File:

Create a .env file in the project directory and add your OpenAI API key.

    echo "OPEN_AI_KEY="openai_api_key" > .env

    To use the code review tool, follow these steps:

Run the Main Script:
Use the following command to run the main.py script.

    python main.py <file_path> --language <language>

Some sample code are provided in the Codes folder in the repo, that can be used for submission and generating reviews.
