import json


def generate_prompt():
    prompt = input("Enter your prompt: ")

    formatted_json = json.dumps({
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    })

    print(formatted_json)
    return formatted_json
