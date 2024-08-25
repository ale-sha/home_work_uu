def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().__contains__(root_word.lower()) or root_word.lower().__contains__(i.lower()):
            same_words.append(i)
    return same_words


print(single_root_words("доМ", "дОмашний", "слон", "домик"))
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
