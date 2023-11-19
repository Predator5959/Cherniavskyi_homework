class DomainsListProcess:
    def __init__(self, domains_file):
        self.domains_file = domains_file
        self.domains_list = self.read_domains()

    def read_domains(self):
        with open(self.domains_file, 'r') as file:
            return [line.strip() for line in file]
    def remove_dots(self):
        return [domain.replace('.','') for domain in self.domains_list]

domains_path = "Lesson 10 Units/domains.txt"
domain_processor = DomainsListProcess(domains_path)
updated_domains = domain_processor.remove_dots()

print(updated_domains)

class NamesListProcess:
    def __init__(self, names_file):
        self.names_file = names_file
        self.nameslist = self.read_names()
    def read_names(self):
        with open(self.names_file, 'r') as file:
            return [line.strip().split('\t') for line in file]
    def get_names_list(self):
        return self.nameslist

names_path = 'Lesson 10 Units/names.txt'
name_process = NamesListProcess(names_path)

names_in_list = name_process.get_names_list()
print(names_in_list)

class AuthorsDictList:

    def __init__(self, autors_file):
        self.autors_file = autors_file
        self.autors_dict = self.read_autors_file()

    def read_autors_file(self):
        # autors_list = []
        with open(self.autors_file, 'r') as file:
            date_dict = [line.strip().split('-')[0].strip() for line in file if '-' in line]
            date_dict = [{"date": date} for date in date_dict]
        return date_dict

    def get_autors_dict(self):
        return self.autors_dict

autors_path = 'Lesson 10 Units/autors.txt'
autors_process = AuthorsDictList(autors_path)

autors_dict = autors_process.get_autors_dict()
print(autors_dict)