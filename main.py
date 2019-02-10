data = ["red","red","blue","red","blue"]

def freq(arr, item):
    counter = 0
    for i in range(0, len(arr)):
        if (arr[i] == item):
            counter += 1
    return counter

def findMajority(arr):
    result = findMajorityElementDivAndConq(arr)
    counter = freq(arr, result)
    if (counter > len(arr) / 2):
        return result
    else:
        return "NO MAJORITY"

def findMajorityElementDivAndConq(arr):

    if(len(arr) == 1):
        return arr[0]
    else:

        leftArr = []
        rightArr = []


        for i in range(0,len(arr)):
            if (i < len(arr) / 2):
                leftArr.append(arr[i])
            else:
                rightArr.append(arr[i])


        left = findMajorityElementDivAndConq(leftArr)
        right = findMajorityElementDivAndConq(rightArr)

        if (left == right):
            return left
        
        leftCount = freq(arr, left)
        rightCount = freq(arr, right)

        if(leftCount == rightCount):
            return -1
        elif(leftCount > rightCount):
            return left
        else:
            return right


result = findMajority(data)
print("----")
print(result)