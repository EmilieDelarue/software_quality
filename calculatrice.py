play = True

"""debut de la boucle pour rejouer"""
while play:

    x = float(input("Entrer un nombre : ")) 
    operator = input("Entrer un opérateur : ")
    y = float(input("Entrer un nombre : "))
    result = float

"""récupération de l'opérateur en string pour l'appliquer - result défini pour l'inscrire dans le fichier"""
    if operator == '+':
        result = (x+y)
       print(x+y)
    elif operator == '-':
        result = (x-y)
        print(x-y)
    elif operator == '/' or ':':
        if x == 0:
            print('On ne peut pas diviser par 0')
        else:
            result = (x/y)
            print(x/y)
    elif operator == '*' or 'x' or 'X':
        result = (x*y)
        print(x*y)
    else:
        print('Votre opérateur n\'est pas valide')


"""input pour le nom du fichier texte à enregistrer"""
    message = input("Entrez le nom du fichier sur lequel vous souahitez enregistrer l'opération : ")

"""inscription dans le fichier"""
    mon_fichier = open(message + ".txt", "a")
    mon_fichier.write(str(x) + operator + str(y) + "=" + str(result))
    mon_fichier.close

"""demande pour rejouer"""
    if input("Jouer encore (O/N ?) ") == "N":
        play = False

