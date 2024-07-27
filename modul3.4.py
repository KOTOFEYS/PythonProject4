def single_root_words(root_word, *other_words):
    some_words = []
    for i in other_words:
        if root_word in i:
            some_words.append(i)

            continue
        else:
            continue

        return some_words
    print(some_words)
single_root_words('rich', 'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('able', 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel')