


def largestelementarray(array):
    maxnumber = array[0]

    for index in range(0,len(array)):
        if maxnumber <= array[index]:
            maxnumber = array[index]

    return maxnumber

anarray = [2,3,4,5,6]
print(largestelementarray(anarray))
