import requests

URL = 'https://github.com/ale-sha/home_work_uu'
page = requests.get(URL)
print(page)
print(page.text)

image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('new_image.png', 'wb') as f:
    f.write(image.content)

url = 'https://webhook.site/0c29052d-8a01-4930-bfe5-92b8e3e934ec'
with open('test.txt', 'w') as f:
    f.write('текст для проверки загрузки файла')
    with open('test.txt', 'rb') as f:
        r = requests.post(url, {'files': f})
        print(r)
