def single_root_words(root_word, *other_words):
    some_words = []
    for i in other_words:
        if root_word in i or i.lower() in root_word.lower():
            some_words.append(i)
    print(some_words)
    return some_words

single_root_words('rich','richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement','Able', 'Mable', 'Disable', 'Bagel')