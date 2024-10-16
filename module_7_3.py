class WordsFinder:
    def __init__(self, *file_names):
        names_files = []
        for file_name in file_names:
            names_files.append(file_name)
        self.file_name = names_files

    def get_all_words(self):
        diction = {}
        for name_file in self.file_name:
            with open(name_file, encoding='utf-8') as file:
                words_list = []
                for line in file:
                    import string
                    line = line.lower().translate(str.maketrans('', '', string.punctuation))
                    words_list.extend(line.split())
            diction[name_file] = words_list
        return diction

    def find(self, word):
        find_dict = self.get_all_words()
        diction = {}
        word = word.lower()
        word_order = 1
        for name_file, words in find_dict.items():
            for i in words:
                if i == word:
                    diction[name_file] = word_order
                    break
                word_order += 1
        return diction

    def count(self, word):
        find_dict = self.get_all_words()
        diction = {}
        word = word.lower()
        word_count = 1
        for name_file, words in find_dict.items():
            for i in words:
                if i == word:
                    diction[name_file] = word_count
                    word_count += 1
        return diction


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('На'))
print(finder2.count('нА'))

