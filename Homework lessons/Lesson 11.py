import os
test_directory = "Homework lessons"


def dict_of_dir_and_files(directory):
    result_dict = {'dirnames': [], 'filenames': []}
    if os.path.isdir(directory):
      items = os.listdir(directory)

      for item in items:
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path):
            result_dict['filenames'].append(item)
        elif os.path.isdir(full_path):
            result_dict['dirnames'].append(item)
    return result_dict


result = dict_of_dir_and_files(test_directory)
print(result)

# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.

def sorted_dir_and_files_dir(dictionary,):
    dictionary['filenames'] = sorted(dictionary['filenames'], reverse = False)
    dictionary['dirnames'] = sorted(dictionary['dirnames'], reverse = False)
    return dictionary

sorted_result = sorted_dir_and_files_dir(result)
print(sorted_result)

# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.

def add_item_in_dict(directory_dict, item_name):
    if '.' in item_name:
        directory_dict['filenames'].append(item_name)
    else:
        directory_dict['dirnames'].append(item_name)
    return directory_dict

add_item = "new_folder"
updated_dict = add_item_in_dict(result, add_item)
print(updated_dict)
