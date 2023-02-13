"""Python_lesson_5"""

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# my_f = open('task_1.txt', 'w', encoding='utf-8')
# line = input('Введите текст \n')
# while line:
#     my_f.writelines(line)
#     line = input('Введите текст \n')
#     if not line:
#         break
#
# my_f.close()
# my_f = open('test.txt', 'r', encoding='utf-8')
# content = my_f.readlines()
# print(content)
# my_f.close()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# def count_info() -> object:
#     try:
#         with open('task_2.txt', 'r', encoding="utf-8") as file:
#             my_list = file.readlines()
#             for i in range(len(my_list)):
#                 new_l = my_list[i].split()
#                 print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
#     except FileNotFoundError:
#         return 'Файл не найден.'
#
#
# count_info()

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

# def workers_statistics():
#     try:
#         with open("task_3.txt", encoding="utf-8") as read_file:
#             f_average_salary = 0
#             all_read_lines = read_file.readlines()
#             for line in all_read_lines:
#                 s_name, salary = line.split()
#                 salary = float(salary)
#                 f_average_salary += salary
#                 if salary < 20000:
#                     print(f"\t{s_name} {salary}")
#             if len(all_read_lines) > 0:
#                 f_average_salary /= len(all_read_lines)
#                 print(f"\tСредняя зарплата: {f_average_salary:.2f}\n")
#     except IOError:
#         print("\tОшибка открытия файла!\n")
#
#
# workers_statistics()

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

# def rewrite_file():
#     try:
#         with open("task_4.txt", encoding="utf-8") as read_file:
#             with open("new_task_4.txt", "w", encoding="utf-8") as write_file:
#                 number_words_list = ["Один", "Два", "Три", "Четыре"]
#                 all_read_lines = read_file.readlines()
#                 for num, line in enumerate(all_read_lines):
#                     if len(line):
#                         words = line.split()
#                         print(f"{number_words_list[num]} {words[1]} {words[2]}", file=write_file)
#                 print("\tГотово\n")
#     except IOError:
#         print("\tОшибка открытия файла!\n")
#
#
# rewrite_file()

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. 
"""

#
# def summary():
#     try:
#         with open('task_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
#
#
# summary()

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и 
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# def count_subjects():
#     try:
#         # Информатика: 100(л) 50(пр) 20(лаб).
#         mydict = {}
#         with open("task_6.txt", encoding='utf-8') as fobj:
#             for line in fobj:
#                 name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
#                 name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
#                 """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры
#                         и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', '0'])
#                  2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет
#                         получившееся: _100_50_20  (где _ это пробел)
#                  3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()
#                         - делит по пробелам методом .split(): ['100', '50', '20']
#                  4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split())
#                         - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int
#                  5. с помощью sum(['100', '50', '20']) суммирует все элементы списка """
#                 mydict[name] = name_sum
#             print(f"{mydict}")  # вывод:{'Информатика': 170}
#     except FileNotFoundError:
#         return 'Файл не найден.'
#
#
# count_subjects()

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

# import json
#
#
# def get_statistics():
#     try:
#         with open('task_7.txt', 'r+', encoding='utf-8') as file:
#             statistics = []
#             profit = {}
#             average_profit = {}
#             av = 0
#             prof = 0
#             i = 3
#             for line in file:
#                 name, firm, earning, damage = line.split()
#                 total = int(earning) - int(damage)
#                 if total >= 0:
#                     prof = prof + total
#                 else:
#                     i -= 1
#                 profit[name] = total
#             statistics.append(profit)
#             if i != 0:
#                 (av) = prof / i
#                 average_profit['average_profit'] = round(av)
#                 statistics.append(average_profit)
#             else:
#                 print('Все компании работают в убыток')
#             print(statistics)
#         with open('file.json', 'a+', encoding='utf-8') as json_file:
#             json.dump(statistics, json_file)
#     except FileNotFoundError:
#         return 'Файл не найден.'
#
#
# get_statistics()
