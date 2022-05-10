# # Program1
# # def factorial(n):
# #      assert n>=0 and int(n) == n, 'The number be positive integer only'
# #      if n in[0,1]:
# #          return 1
# #      else:
# #          return n*factorial(n-1)    
# # print(factorial(14))         



# # Program2
# # def fibonacci(n):
# #     assert n >=0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer.'
# #     if n in [0,1]:
# #           return n
# #     else:
# #           return fibonacci(n-1) + fibonacci(n-2)
# # print(fibonacci(10))



# # program3 | sum of digits
# # def sumofdigits(n):
# #     assert n >= 0 and int(n) == n, 'The no should be positive integer'
# #     if n == 0:
# #         return 0
# #     else:
# #         return n%10 + sumofdigits(n//10)
# # print(sumofdigits(555))            



# # program4 | power
# # def power(base,exp):
# #     assert exp >= 0 and int(exp) == exp, 'The exponent should be positive integer only.'
# #     if exp == 0:
# #         return 0
# #     if exp == 1:
# #         return base
# #     else:
# #         return base * power(base,exp-1)
# # print(power(2,10))       



# # program5 | greatest common factor
# # def gcd(a,b):
# #     assert int(a) == a and int(b) == b, 'The no must be interger only'
# #     if a < 0:
# #         a = -1*a
# #     if b < 0:
# #         b = -1*b
# #     if b == 0:
# #         return a
# #     else:
# #         return gcd(b,a%b)
# # print(gcd(18,48))                    



# # program5 | decimal to binary
# # def decimaltobinary(n):
# #     assert int(n) == n, 'The no must be integer'
# #     if n == 0:
# #         return 0
# #     else:
# #         return n%2 + 10*(decimaltobinary(int(n/2)))
# # print(decimaltobinary(13))         



# # all about one dimentional array

# # from array import *

# # arr1 = array('i' , [1,2,3,4,5,6])

# # print(arr1)

# # arr1.insert(6,7)
# # print(arr1)

# # def traverseArray(array):
# #     for i in array:
# #         print(i)

# # traverseArray(arr1)

# # def accessElement(array, index):
# #     if index >= len(array):
# #         print("There is no element at this extention")
# #     else:
# #         print(array[index])   

# # accessElement(arr1,2)   


# # def searchInArray(array, value):
# #      for i in array:
# #           if i== value:
# #                 return array.index(value)
# #      return "The elenent does not exist in this array"
# # print(searchInArray(arr1,4))
   

# # arr1.remove(4)
# # print(arr1)   



# #  2 dimentional array

# # import numpy as np

# # twoDArray = np.array([[11,15,10,6] , [10,14,11,5] , [12,17,12,8] , [15,18,14,9]])
# # print(twoDArray)

# # newtwoDArray = np.insert(twoDArray,00,[1,2,3,4], axis=1)
# # print(newtwoDArray)

# # newtwoDArray = np.append(twoDArray, [[1,2,3,4]] , axis=0)
# # print(newtwoDArray)

# # def searchTbarray(array, value):
# #      for i in range(len(array)):
# #           for j in range(len(array[0])):
# #                 if array[i][j] == value:
# #                      return 'The valu is located at index '+str[i]+" "+str[j]
# #      return 'The eleent is not found'
# # print(searchTbarray(twoDArray, 14)


# # newTDarray = np.delete(twoDArray, 0, axis=1)
# # print(newTDarray)




# # LIST

# # mylist = [1,2,3,4,5,6,7]
# # print(mylist)

# # mylist.insert(0,11)

# # mylist.append(8)

# # newlist = [11,12,13,14]
# # mylist.extend(newlist)
# # print(mylist)





# # average temp of days
# #  code without list
# # numDays = int(input("How many days temperature."))
# # total = 0
# # for i in range(1,numDays+1):
# #     nextday = int(input("Day " + str(i) + "'s high temperature"))
# #     total += nextday
    
# # avg = round(total/numDays,2) 
# # print("\nAverage = "+str(avg)) 




# # code with list
# # numDays = int(input("How many days temperature."))
# # total = 0
# # temp = []
# # for i in range(numDays):
# #     nextday = int(input("Day " + str(i+1) + "'s high temperature"))
# #     temp.append(nextday)
# #     total += temp[i]
    
# # avg = round(total/numDays,2) 
# # print("\nAverage = "+str(avg)) 

# # above = 0
# # for i in temp:
# #     if i > avg:
# #         above += 1
# # print(str(above)+ "days above average")




# # DICTIONARIES

# myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

# # def traversedict(dict):
# #     for key in dict:
# #         print(key,dict[key])
# # traversedict(myDict)        

# def searchDict(dict,value):
#     for key in dict:
#         if dict[key] == value:
#             return key,value
#     return "the value doesnot exist"

# print(searchDict(myDict,27)) 




# TUPLES

# newTuple = ('a',' b', 'c', 'd', 'e') 

# def searchTuple(pTuple, element):
#      for i in pTuple:
#           if i == element:
#                 return pTuple.index(i)
#      return 'The element does not exist'
# print(searchTuple(newTuple, 'c'))




# # STACK
# import queue
# stack = queue.LifoQueue(3)
# stack.put(10)
# stack.put(20) 
# stack.put(30)
# stack.put(40,timeout=1)
# print(stack)


