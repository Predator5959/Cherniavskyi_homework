import os



test_dir = "Lesson 10 Units"
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
