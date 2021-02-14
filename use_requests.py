import requests

url = 'https://kompas.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success Response = {response.status_code}')
        print(f'\nContent = {response.text}')
    else:
        print('Woops, Ada error cuy')
except Exception as e:
    print(f'There as any error code{e}')
print('Program Ended')

