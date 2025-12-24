#Question 1------------------------------------------------------------
# tup=(8,5,78,56,1,3)
# print("maximum: ",max(tup))
# print("minimum: ",min(tup))

#Question 2----------------------------------------------------------
# list=[("Pranab",101),("subham",102),("rohan",103)]
# d=dict(list)
# print("Dictionary: ",d)

#Question 3-------------------------------------------------------
# tup=(2,6,9,5,4,3,2,1,2,8)
# element=2
# count=0
#
# for el in tup:
#     if el==element:
#         count+=1
#
# print("count: ",count)

#Question 4--------------------------------------------------------------
# tup=([1,2,3],[4,5,6])
# tup[0][0]=9
# print("new tuple:",tup)

#Question 5------------------------------------------------------------
t1=(1,2,3)
t2=(4,5,6)
t1, t2 = t2, t1
print("t1: ",t1)
print("t2: ",t2)