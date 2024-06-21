import random


def sortEstimatedValueErrors(errorArray, errorIndexArray):
    n = len(errorArray)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if errorArray[j] > errorArray[j + 1]:
                errorArray[j], errorArray[j + 1] = errorArray[j + 1], errorArray[j]
                errorIndexArray[j], errorIndexArray[j + 1] = errorIndexArray[j + 1], errorIndexArray[j]


errorArrayOutside = []
errorIndexArrayOutside = []

for i in range(0, 200):
    errorArrayOutside.append(random.random())
    errorIndexArrayOutside.append(i)

sortEstimatedValueErrors(errorArrayOutside, errorIndexArrayOutside)
for i in range(0, 200):
    print(errorArrayOutside[i], errorIndexArrayOutside[i])