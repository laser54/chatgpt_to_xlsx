import openai
import json
import openpyxl
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('API_KEY')

def get_answer(question):
    """
    Use the OpenAI API to generate a response to a question.

    Parameters:
    - question: The question to generate a response for.
      (type: str)

    Returns:
    - A string containing the response to the question.
      (type: str)
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=2048,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        json_string = json.dumps(response)
        data = json.loads(json_string)
        return data["choices"][0]["text"]
    except Exception as e:
        return "ERROR"


with open('input.txt', 'r') as input_file:
    questions = input_file.readlines()

# Create an empty list to store the results
results = []

# Iterate over the questions and call the some_func() function for each question, storing the results in the results list
for question in questions:
    result = get_answer(question).lstrip()
    if result != "ERROR":
        print('parsing .... ' + question)
    else:
        print('SOMETHING WRONG WITH .... ' + question)
    results.append([question, result])

    # Open the Excel file in write mode and create a new worksheet
    wb = openpyxl.load_workbook('results.xlsx')
    ws = wb.active

    # Append the new result to the worksheet
    ws.append([question, result])

    # Save the Excel file
    wb.save('results.xlsx')

print("Done")



