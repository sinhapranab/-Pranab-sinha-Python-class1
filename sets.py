#Question 1----------------------------------------------------
# set1={1,2,3,4}
# set2={3,4,5,6,7}
# print("Union: ",set1 | set2)
# print("Intersection: ",set1 & set2)
# print("difference: ",set1 - set2)
# print("symmetric_difference: ",set1 ^ set2)

#Question 2-------------------------------------------------------
# set1={1,2,3,4}
# set2={3,4,5,6,7}
# common = set1 & set2
# set1 = set1 - common
# set2 = set2 - common
# print("set1 after removing common element: ",set1)
# print("set2 after removing common element: ",set2)

#Question 3------------------------------------------------------------
# set1={1,2}
# set2={1,2,3,4,5}
# if set1.issubset(set2):
#     print("set1 is a subset of set2")
# else:
#     print("set1 is not a subset of set2")

#Question 4-----------------------------------------------------------------
# set={89,67,54,32,28,98}
# num=50
# for item in set:
#     if item>num:
#         print(item)

#Question 5---------------------------------------------------------
lst=[1,2,3,2,4,5,6,2,8,2,9,4,5,6]
unique_list=list(set(lst))
print("Unique elements: ",unique_list)
