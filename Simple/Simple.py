#Eynes Test - Federico Wagner

#Simple
import random

def listGenerator():
    """Returns an array of ten dictionaries, in which everyone has two keys: "id" and "age"
    >>> listGenerator()
    [{'id': 1, 'age': 25}, {'id': 2, 'age': 61}, {'id': 3, 'age': 53}, ...
    """

    dict = [ {"id": id, "age": random.randint(0, 100)} 
            for id in range(1,11) ]
    print (dict)
    return dict
        
def sortingFunction(array):
    """Returns the given array sorted by the key "age"
    >>> sortingFunction([{'id': 1, 'age': 25}, {'id': 2, 'age': 61}, {'id': 3, 'age': 53}])
    [{'id': 1, 'age': 25}, {'id': 3, 'age': 53}, {'id': 2, 'age': 61}]
    """
    sortedArray = sorted(array, key=lambda x: x['age']) 
    print("Youngest:", sortedArray[0])
    print("Oldest:", sortedArray[-1])
    return sortedArray


#sortingFunction(listGenerator())  #TEST