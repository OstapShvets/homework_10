# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).
#
# def read_domains(file_name):
#     with open(file_name, 'r') as f:
#         domains = f.readlines()
#     domains = [d.strip() for d in domains]
#     return [d.replace('.', '') for d in domains]
# domains = read_domains('domains.txt')
# print(domains)


#  Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

# def read_surnames(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#     surnames = []
#     for line in lines:
#         parts = line.strip().split('\t')
#         surnames.append(parts[1])
#     return surnames


# #####Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

