import openai

    openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat...")
        break
    
    prompt = f"【中文聊天机器人】\n{user_input}\n"

    response = openai.Completion.create(
      model="gpt-4",
      prompt=prompt,
      max_tokens=150
    )
    
    print(f"Bot: {response.choices[0].text.strip()}")
