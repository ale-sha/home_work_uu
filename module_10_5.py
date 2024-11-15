from datetime import  datetime
from multiprocessing.pool import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line.strip())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    start = datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.now()
    result_time = end - start
    print(f'Линейный вызов: {result_time}')


    start = datetime.now()
    with Pool(4) as pool:
        result = pool.map(read_info, filenames)
    end = datetime.now()
    result_time = end - start
    print(f'Многопроцессный вызов: {result_time}')
