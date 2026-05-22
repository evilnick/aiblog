import requests

url = "http://localhost:5000/translate"
mytext = input("Enter the text to translate: ")
payload = {"q": mytext,
           "source": "en",
           "target": "de",
           "format": "text"}
response = requests.post(url, json=payload)

print(f"That translates to German as: {response.json()['translatedText']}")
