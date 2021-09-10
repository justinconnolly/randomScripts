list1 = [1,2,3]
list2 = [4,5,6]



for i in range(len(list1)):
    for j in range(len(list2)):
        print("<",end="")
        print(list1[i], end = ", ")                 # first number
        print(list2[(j+1)%len(list2)],end = "")     # this will start with the SECOND entry of list1 then use modular arithmetic to wrap around without a key error
        print(">")
