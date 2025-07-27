import ollama


messages = [
    {"role": "system", "content": "You are a financial analysis assistant. Your task is to analyze text and assess confidence in a specific stock's performance. Based on the content, provide a score from 0 to 100, where:\n\n- 0 = Strong Sell\n- 50 = Hold\n- 100 = Strong Buy\n\nInclude a brief explanation of your reasoning. Output format:\n\nIn-depth Analysis: [Your explanation]\n[Stock Name]: [Score]"},
    {"role": "user", "content": "test"}
]

response = ollama.chat(model='gemma3', messages=messages)

print(response['message']['content'])