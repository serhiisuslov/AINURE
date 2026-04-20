from ollama import generate

PATH = "image.jpg"

def main():

    #gen_model = 'llava-phi3:latest'

    gen_model = 'minicpm-v'

    response = generate(gen_model, 'What is the definition of AI?')

    print(response['response'])

if __name__ == "__main__":
    main()