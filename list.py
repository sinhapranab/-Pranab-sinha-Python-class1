#Question 1-------------------------------------------------------
# list=[1,2,3,6,2,1,8,6]
# unique=[]
# for item in list:
#     if item not in unique:
#         unique.append(item)
#
# print("Unique elements: ",unique)

#Question 2---------------------------------------------------------
# numbers=[1,2,3,4,5,6,7,8,9]
# even_numbers=[n for n in numbers if n%2==0]
# print("even numbers: ",even_numbers)

#Question 3---------------------------------------------------------
# list=[78,90,45,50,65]
# largest=-1
# sec_largest=-1
# for num in list:
#     if num>largest:
#         sec_largest=largest
#         largest=num
#     elif num>sec_largest and num!=largest:
#         sec_largest=num
#
# print("second largest element: ",sec_largest)

#Question 4-------------------------------------------------------------
# nested_list=[[1,2,3],[4,5,6],[7,8,9]]
# for inner in nested_list:
#     print("sum: ",sum(inner))

#Question 5--------------------------------------------------------------
import copy
original=[[1,2],[3,4]]
shallow=copy.copy(original)
deep=copy.deepcopy(original)

original[0][0]=100
print("original: ",original)
print("shallow copy: ",shallow)
print("deep copy: ",deep)
