from ollama import chat

PATH = "image.jpg"

def main():


    response2 = chat(
        model='llava-phi3:latest',
        messages=[
            {
                'role': 'user',
                'content': 'What is in this image? Be concise. Також надай відповідь українською.',
                'images': [PATH],
            }
        ],
    )

    print(response2.message.content)

if __name__ == "__main__":
    main()