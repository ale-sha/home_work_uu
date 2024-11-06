from datetime import  datetime
import threading
import time
from time import sleep, thread_time

start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        for i in range(word_count):
            file.write('Какое-то слово № '+ str(i +1) + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = datetime.now()
time_result = end - start
print(f'Работа потоков {time_result}')


start = datetime.now()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end = datetime.now()
time_result = end - start
print(f'Работа потоков {time_result}')
