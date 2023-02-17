import openai
import json
import openpyxl
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('API_KEY')

def get_answer(question, extra_prompt):
    """
    Use the OpenAI API to generate a response to a question.

    Parameters:
    - question: The question to generate a response for.
      (type: str)
    - extra_prompt: The extra prompt to add to the question.
      (type: str)

    Returns:
    - A string containing the response to the question.
      (type: str)
    """
    try:
        prompt = f'{extra_prompt}\n"{question.strip()}"'
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
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

# Ask user for extra prompts
extra_prompts = []
while True:
    prompt = input("Enter an extra prompt (or type 'done' to continue): ")
    if prompt == "done":
        break
    extra_prompts.append(prompt)

# Create an empty list to store the results
results = []

# Iterate over the questions and call the get_answer() function for each question with all the extra prompts, storing the results in the results list
for question in questions:
    for extra_prompt in extra_prompts:
        result = get_answer(question.strip(), extra_prompt).lstrip()
        if result != "ERROR":
            print('parsing .... ' + question)
        else:
            print('SOMETHING WRONG WITH .... ' + question)
        results.append([extra_prompt, question.strip(), result])

# Open the Excel file in write mode and create a new worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Write the headers to the worksheet
ws.append(["Extra Prompt", "Keyword", "Result"])

# Append the new results to the worksheet
for result in results:
    ws.append(result[0:2] + [result[2].strip()])

# Save the Excel file
wb.save('results.xlsx')

print("Done")
