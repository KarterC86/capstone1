import requests
import json 

headers = {
    'content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

input_text = input('enter whatever youd like: ')
data = { 
    'prompt' : input_text,
    'max_tokens' : 500, 
    'temperature' : 0.5
}

response = requests.post(
    'https://api.openai.com/v1/engines/text-davinci-003/completions',
    headers = headers, 
    json = data 
)
print(response.status_code)
if response.status_code == 200:
    response_data = json.loads(response.text)
    print(response_data['choices'][0]['text'])
else:
    print('Error: ' + str(response.status_code))
