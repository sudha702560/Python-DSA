def PassCode(strCode, li):
    strList = list(strCode)
    result = []
    myStore = {}
    for i in range(len(li)):
        strList[li[i][0]] , strList[li[i][1]] = strList[li[i][1]] , strList[li[i][0]]
        index = strList[0]
        result.append(ord(index))
        myStore[index] = strList
    
    result.sort()
    key = result[0]

    return ''.join(myStore[chr(key)])
# ord -- to get ASCII values using char A , B , ,, : 
# chr -- ASCII to character conversion

li = [[5,3],[1,2],[0,4]]
# print(len(li))
print(PassCode("dcabfe",li))


# x, y = y, x 