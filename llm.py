import ollama

response = ollama.chat(
    model='gemma3',
    messages=[
        {"role": "user", "content": "hello."}
    ]
)

print(response['message']['content'])