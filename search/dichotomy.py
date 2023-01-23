#fenix

#Ce programme implemente la recherche par dichotomie sur un tableau trie.
#Il retourne 1 si la valeur est trouve et 0 si la valeur n'est pas trouve.

def dichotomy_search(array,nbreSearch):
    low = 0
    high = len(array) - 1
    while(low <= high):
        middle = (low + high) // 2
        if(array[middle] == nbreSearch):
            return 1
        elif(array[middle] < nbreSearch):
            low = middle + 1
        else:
            high = middle - 1
    return 0

table = [1,2,3,4,5,6,7,8,9,10,11,14,20]
nbreSearch=int(input("Donnez le nombre a rechecher : "))
result = dichotomy_search(table,nbreSearch)

print(result)
