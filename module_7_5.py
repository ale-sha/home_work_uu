import os
import time

print("Текущая директория:", os.getcwd())  # абсолютный путь до рабочей директории
# os.mkdir('first')  # создание папки в текущей директории. Второй с таким именем не создать
if os.path.exists("first"):  # замена существуещей папки на новую c тем же имeнем
    os.chdir("first")
else:
    os.mkdir('first')
    os.chdir('first')
print("Текущая директория:", os.getcwd())
# os.makedirs('second/third') # создание вложенных директорий в текущей
# print(os.listdir())  # посмотреть, что лежит в папке из текущ.дир.
# for i in os.walk('.'):  # посмотреть, попапочно
#     print(i)
os.chdir('/Users/alenashabalina/Documents/обучение urban/HomeWork/hw_7/hw_7')
print("Текущая директория:", os.getcwd())  # Вернулись к начальной дир.
print(os.listdir())  # Показывает ВСЁ что есть в папке
file = [f for f in os.listdir() if os.path.isfile(f)]  # возвращает True, если это файл
dirs = [d for d in os.listdir() if os.path.isdir(d)]  # возвращает True, если это папка
print(dirs)
print(file)
# os.startfile(file[6])  # открыть конкретный файл
print(os.stat(file[6]))

directory = '/Users/alenashabalina/Documents/обучение urban/HomeWork/hw_7/hw_7'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')
