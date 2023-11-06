# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки)

domains_file = "Lesson 10 Units/domains.txt"

def domains_into_list(domains_file):
    with open (domains_file, 'r') as file:
        domains = [line.strip() for line in file]
        return [domain.replace('.', '') for domain in domains]


domains_list = domains_into_list(domains_file)
print(domains_list)

# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

names_file = 'Lesson 10 Units/names.txt'

def names_into_list(names_file):
    with open (names_file, 'r') as file:
        last_names = [line.strip().split('\t') for line in file]

    return last_names


last_names = names_into_list(names_file)
print(last_names)

# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

authors_file = 'Lesson 10 Units/autors.txt'


def data_dictionary(authors_file):
    with open (authors_file, 'r') as file:
        date_dict = [line.strip().split('-')[0].strip() for line in file if '-' in line]
        date_dict = [{"date":date} for date in date_dict]
    return date_dict

dictionary = data_dictionary(authors_file)
print(dictionary)
