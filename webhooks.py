import requests

url = "https://webexapis.com/v1/webhooks"

payload = '''{
    "name": "Arcor Webhook",
    "targetUrl": "https://6c71-181-170-125-94.ngrok-free.app/v1/arcor",
    "resource": "messages",
    "event": "created"
}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer 9643-417f-9974-ad72cae0e10f"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

payload = '''{
    "name": "My Attachment Action Webhook",
    "targetUrl": "https://6c71-181-170-125-94.ngrok-free.app/v1/arcor",
    "resource": "attachmentActions",
    "event": "created"
}'''

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))