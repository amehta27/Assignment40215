

def smallestelement(array):
    smallestelement = array[0]

    for index in range(0,len(array)):
        if smallestelement >= array[index]:
            smallestelement = array[index]

    return smallestelement


arrayelement = [2,3,4,5,6]

print(smallestelement(arrayelement))
