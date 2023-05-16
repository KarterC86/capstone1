import requests
import json 
#try to import this iinto ,my tkinter app.

def chatgpt(input_text):

    keyFile = open('capstone1\key.txt','r')

    key = keyFile.readline()

    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {key}'
    }

    data = { 
        'prompt' : input_text,
        'max_tokens' : 50, 
        'temperature' : 0.5
    }

    response = requests.post(
        'https://api.openai.com/v1/engines/text-davinci-003/completions',
        headers = headers, 
        json = data 
    )

    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data['choices'][0]['text']
    else:
        return 'Error: ' + str(response.status_code)


