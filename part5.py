'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''

FILENAME = "task5.txt"

NUMBERS = "12 7 87 935 0 32 71"

summ = 0

try:
    with open(FILENAME, 'w') as fhs:
        fhs.write(NUMBERS)

    with open(FILENAME, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        summ += float(item)
except IOError as e:
    print(e)
except ValueError:
    print("Error")

print(summ)
