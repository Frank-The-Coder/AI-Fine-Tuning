import openai

    openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(user_message):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ]
    )

    return response.choices[0].message['content']

while True:
    user_input = input("Ask something (or type 'n' to exit): ")
    
    if user_input.strip().lower() == 'n':
        break

    print(get_response(user_input))
