from ollama import chat

PATH = "image.jpg"

#gen_model = 'llava-phi3:latest'

gen_model = 'minicpm-v'

messages = []


while True:
    user_input = input("You: ")

    messages.append({
        'role': 'user',
        'content': user_input
    })

    response = chat(
        model=gen_model,
        messages=messages
    )

    answer = response['message']['content']
    print(answer)

    messages.append({
        'role': 'assistant',
        'content': answer
    })




