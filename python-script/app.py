import requests

from prompt_formatter import generate_prompt


def post_data():
    url = "http://127.0.0.1:8080/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = generate_prompt()
    try:
        response = requests.post(url, headers=headers, data=data)
        print(response.json())
    except Exception as e:
        print("Error occured: ", e)


while True:
    post_data()
