import requests

url = 'https://api.whatsapp.com/send'
data = {
    'phone': 'numero',
    'message': 'Hola, este es un mensaje automático.'
}
response = requests.post(url, json=data)
if response.status_code == 200:
    print('Mensaje enviado con éxito')
else:
    print('Error al enviar el mensaje')
