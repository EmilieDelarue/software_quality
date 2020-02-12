



"""Création d'une liste vide"""
numberList = []

"""Récupération du fichier contenant un string de chiffres à trier"""
numbers = open("/Users/milou/Documents/Cours/2019.2020/SoftwareQuality/numberList.txt", "r")
numberString = numbers.read()

"""Création de split() pour séparer chaque string de chiffre et transformation en int"""
def my_split(string):
    temp_string = ""
    for ch in string: #parcours chaque caratère du string
        if ch == " ":
            if temp_string:
               yield int(temp_string)  #permet de retourner un object générateur pour pouvoir itérer dessus au moment venu
               temp_string = ""
        else:
            temp_string += ch #creation string temporaire
    if temp_string:
        yield int(temp_string) #permet de retourner un object générateur pour pouvoir itérer dessus au moment venu

"""itération sur le string avec utilisation de my_split() pour insertion dans la liste numberList"""
for i in my_split(numberString):
    numberList.append(i)

newList = []


"""fonction bubbleSort : échange à plusieurs reprises les éléments adjacents s'ils sont dans le mauvais ordre en deux boucles"""
def bubbleSort(l):
    #première boucle
    for x in range(len(l)-1, 0, -1):
        #deuxième boucle 
        for y in range(x):
            #tri et échange si cela doit etre fait
            if l[y] < l[y + 1]:
               l[y], l[y + 1] = l[y + 1], l[y]
    return l
#newList = bubbleSort(numberList)
#print(newList)

"""fonction quickSort : partitionne la liste - choisi une valeur de la liste qui sera à sa place triée. 
Cette valeur est appelée pivot. Tous les éléments plus petits que le pivot sont déplacés vers sa gauche. 
Tous les éléments plus grands sont déplacés vers sa droite."""
def partition(l,low,high): #fonction qui partitionne le tableau
    i = ( low-1 )    #défini le plus petit nombre (en principe 0)    
    pivot = l[high]  #défini le nombre pivot (en principe la longueur de la liste)    
    for j in range(low , high): #tri chaque chiffre entre le plus petit nombre et le nombre pivot
        if   l[j] <= pivot: 
            i = i+1 
            l[i],l[j] = l[j],l[i] 
    l[i+1],l[high] = l[high],l[i+1] 
    return ( i+1 ) 

def quickSort(l,low,high): #tri en fonction du tableau partionné
    if low < high: 
        pi = partition(l,low,high) #place le chiffre en fonction du nombre pivot
        quickSort(l, low, pi-1) 
        quickSort(l, pi+1, high)
    return l
#n = len(numberList) 
#newList = quickSort(numberList,0,n-1) 
#print(newList)

"""fonction de tri par insertion : déplace les éléments de la liste qui sont supérieur à la clé définie, à une position 
d'avance à leur position actuelle"""
def insertionSort(l): 
    for i in range(1, len(l)): 
        key = l[i] #définition de la clé
        j = i-1
        while j >=0 and key < l[j] : #continue tant que la clé défini est plus petite que l'élément actuel
                l[j+1] = l[j] #tri en fonction de la clé
                j -= 1
        l[j+1] = key #définition de la nouvelle clé
    return l
#newList = insertionSort(numberList)
#print(newList)

"""tris par tas : On recherche le père du dernier nœud de l’arbre et on le tamise : le père d’un noeud dans un arbre binaire 
corresponds à l’arrondi inférieur de (i-1)/2 avec i la position du noeud dans le tableau qui stocke l’arbre.
Le tamisage d’un noeud consiste à visiter son fils droit et son fils gauche et permuter la racine avec le plus grand des deux.
On tamise l’arbre jusqu’à arriver à la racine, le plus grand nombre de l’arbre se retrouve alors en position de racine au début du tableau.
On permute la racine qui est le plus grand nombre avec la dernière feuille (soit la position n du tableau qui stocke l’arbre de taille n).
On considère alors que ce nombre est bien ordonné (càd il est en dernière position et c’est le plus grand)
On réitère l’opération de tamisage et permutation en considérant le sous arbre qui va de la racine à n-1 
(pour ne pas déplacer le nombre qui a été correctement ordonné) jusqu’à ce qu’on arrive au fils gauche de la racine"""


"""tri par fusion : Consiste à séparer la liste en deux, la fusion consiste à rassembler dans un seul tableau
trié les valeurs contenues dans les deux tableaux triés fournis en paramètre  """
def mergeSort(l):
    if len(l)>1: #verification s'il y a + d'un élément dans la liste 
        mid = len(l)//2 #division de la liste en 2
        lefthalf = l[:mid] #liste de gauche
        righthalf = l[mid:] #liste de droite
        mergeSort(lefthalf) #redivision de la liste gauche jusqu'a ce qu'il ne reste plus qu'un élément
        mergeSort(righthalf) #redivision de la liste droite jusqu'a ce qu'il ne reste plus qu'un élément
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]: #tri des nombres entre la liste de gauche et la liste de droite
                l[k]=lefthalf[i]
                i=i+1
            else:
                l[k]=righthalf[j] 
                j=j+1
            k=k+1

        while i < len(lefthalf): #tri liste de gauche
            l[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf): #tri liste de droite
            l[k]=righthalf[j]
            j=j+1
            k=k+1
    return l
#newList = mergeSort(numberList)
#print(newList)