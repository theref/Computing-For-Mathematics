import Tickable1

jlist = Tickable1.jumbledlist(30, 20)
print jlist

def insertionsort(data):
    """
    """
    firstUnsorted = 0
    while firstUnsorted < len(data) - 1: # you've sorted the entire list
        indexOfSmallest = firstUnsorted # because you start at the beginning
        index = firstUnsorted + 1 # moves along one so you have things to compare
        while index <= len(data) - 1: # not at the end of the list
            if data[index] < data[indexOfSmallest]: # checks which is smallest
                indexOfSmallest = index # changes the index values
            index += 1 # moves index along one
        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
        # moves the smallest unsorted element the beginning of unsorted block, thus making it sortedrew3w3wwaaaa`p
        firstUnsorted += 1 # moves first unsorted along one
    return data

print insertionsort(jlist)