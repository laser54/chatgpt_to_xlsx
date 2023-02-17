import openai
import json
import openpyxl
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

openai.api_key = os.getenv('API_KEY')

def generate_response(question, extra_prompt):
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
        return data["choices"][0]["text"].lstrip()
    except Exception as e:
        print(f"Error generating response for '{question}': {e}")
        return "ERROR"

def main():
    # Read the input file and get the questions
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

    # Iterate over the questions and extra prompts, and call the generate_response() function for each combination
    for i, question in enumerate(tqdm(questions, desc="Generating responses", total=len(questions))):
        for extra_prompt in extra_prompts:
            response = generate_response(question, extra_prompt)
            results.append([extra_prompt, question.strip(), response])

    # Write the results to an Excel file
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the headers to the worksheet
    ws.append(["Extra Prompt", "Keyword", "Result"])

    # Write the results to the worksheet
    for result in results:
        ws.append([result[0], result[1], result[2]])

    # Save the Excel file
    wb.save('results.xlsx')

    print("Done")

if __name__ == '__main__':
    main()
