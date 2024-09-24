# openai_cli.py
import sys
sys.path.append('C:/Users/Owner/PycharmProjects/pythonProject/venv/Scripts')

import openai
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Query OpenAI's GPT model.")
    parser.add_argument('prompt', type=str, help='The prompt you want to send to the model.')
    args = parser.parse_args()

    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Completion.create(
        model="gpt-4",
        prompt=args.prompt,
        max_tokens=150
    )

    print(response.choices[0].text.strip())

if __name__ == '__main__':
    main()

