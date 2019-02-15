# def getMissingNo(A):
#     n = len(A)
#     total = (n+1)*(n+2)/2
#     sum_of_A = sum(A)
#     return total - sum_of_A

# def getmissingno(array):
#     arraylength = len(array)
#     total = (arraylength+1)*(arraylength+2)/2
#     sumarray = sum(array)
#     return total - sumarray

def getmissingno(anarray):
    for index in range(0,len(anarray)-1):
        element = anarray[index]
        if (element + 1 != anarray[index+1]):
            print(element+1)






anarray = [1,2,3,4,5,6,7,9]
getmissingno(anarray)
