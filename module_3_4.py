def single_root_words(root_word, *other_words):
    same_words = [i for i in other_words if root_word.lower() in i.lower() or i.lower() in root_word.lower()]
    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel' )
