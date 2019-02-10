data = ["red","green","red","red","green"]

def freq(arr, item):
    counter = 0
    for i in range(0, len(arr)):
        if (arr[i] == item):
            counter += 1
    return counter

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

        print(left)
        print(right)

        if (left == right):
            return left
        elif (right == -1):
            return left
        elif (left == -1):
            return right
        
        leftCount = freq(arr, left)
        rightCount = freq(arr, right)

        print(rightCount)
        print(leftCount)

        if(leftCount == rightCount):
            print("none")
            return -1
        elif(leftCount > rightCount):
            print("left")
            return left
        else:
            print("right")
            return right

print(findMajorityElementDivAndConq(data))