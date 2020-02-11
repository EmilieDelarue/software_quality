"""changement d'une phrase en liste de mots"""

def change_phrase_on_list():
    phrasing = input('Tapez une phrase :')
    if isinstance(phrasing, str):
        print('Vous avez renseigner une chaine de caractère') 
        word_list = phrasing.split(' ')
        print(word_list)
        print('Vous avez tapez ' + str(len(word_list)) + ' mots')

change_phrase_on_list()

