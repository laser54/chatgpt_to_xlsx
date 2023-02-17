# Chatgpt to xlsx
This project is a simple command-line client for interacting with the OpenAI API. It reads in a list of questions from an input file, generates responses for each question using the OpenAI API, and writes the results to an Excel file.

## Prerequisites
You will need to have a valid OpenAI API key. You can sign up for an API key at the OpenAI website.

This project uses the openai and openpyxl libraries, which can be installed using pip:

Copy code 
``` 
pip install -r requirements.txt
```
## Usage
Save your OpenAI API key in a file called .env in the root directory of this project. The file should contain a single line with the following format:
Copy code
```
API_KEY="your-api-key-here"
```
Create an input file called input.txt in the root directory of this project. This file should contain a list of questions, with one question per line.

## Run the script:

Copy code
```
python main.py
```
The script will read in the list of questions from the input file, generate responses for each question using the OpenAI API, and write the results to an Excel file called results.xlsx.
You can add additional prompts before calling the program. You can enter multiple prompts, with each prompt being linked to each keyword and added to the final file separately.