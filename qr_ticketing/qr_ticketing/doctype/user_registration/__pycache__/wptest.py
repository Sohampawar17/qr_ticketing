# import requests

# url = "https://graph.facebook.com/v17.0/120708414452334/messages"

# headers = {
#     "Authorization": "Bearer EAACJ0v07SIkBOyLvgz49vEPYv4ZBadufcZBqSyAkiaYf7GtPMIoZBrrsqTxZAJ7HV2iPxofv1EEFvnNs0pzflWCbdX1ZA4nzxp1vcUslrBwHrrvzU9w4e2FhnHAOyiWYCbrhnIpZCmDZBYvdBXKNx1HhZA7FJyzWJ3tJ4feOmPZBxMG7cXEqKrFdNxZBHzUJQ3ZAHOgN9hZBwfTGCZAygAg2RFXHlOdlTXH63zwZDZD",
#     "Content-Type": "application/json"
# }

# payload = {
#     "messaging_product": "whatsapp",
#     "to": "917058517648",
#     "type": "template",
#     "template": {
#         "name": "hello_world",
#         "language": {
#             "code": "en_US"
#         }
#     }
# }

# response = requests.post(url, headers=headers, json=payload)

# print(response.status_code)
# print(response.text)


import requests

access_token = "EAACJ0v07SIkBOyLvgz49vEPYv4ZBadufcZBqSyAkiaYf7GtPMIoZBrrsqTxZAJ7HV2iPxofv1EEFvnNs0pzflWCbdX1ZA4nzxp1vcUslrBwHrrvzU9w4e2FhnHAOyiWYCbrhnIpZCmDZBYvdBXKNx1HhZA7FJyzWJ3tJ4feOmPZBxMG7cXEqKrFdNxZBHzUJQ3ZAHOgN9hZBwfTGCZAygAg2RFXHlOdlTXH63zwZDZD"
phone_id = "120708414452334"
whatsapp_id = "122676764253733"
custom_phone_number = "7775837874"  # Replace this with the desired custom phone number
custom_message = "hello Sourabh"

url = f"https://graph.facebook.com/v17.0/{phone_id}/messages"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

message_data = {
    "messaging_product": "whatsapp",
    "to": f"91{custom_phone_number}",  # Include the country code in the phone number
    "type": "text",
    "text": {
        "body": custom_message
    }
}

response = requests.post(url, headers=headers, json=message_data)

if response.status_code == 200:
    print("Custom message sent successfully!")
else:
    print(f"Failed to send custom message. Status code: {response.status_code}")
    print(response.text)








