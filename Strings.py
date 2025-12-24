#question 1-----------------------------------------------
# str=input("Enter a string:")
# vowels=0
# consonants=0
# digits=0
# special_char=0
#
# for ch in str:
#     if ch.lower() in 'aeiou':
#         vowels+=1
#     elif ch.isalpha():
#         consonants+=1
#     elif ch.isdigit():
#         digits+=1
#     else:
#         special_char+=1
#
#
#
# print("vowels:",vowels)
# print("consonants:",consonants)
# print("digits:",digits)
# print("special_char:",special_char)

#Question2-------------------------------------------------------
# str=input("Enter a string: ")
#
# words = str.split()
# reversed_words = []
#
# for word in words:
#     reversed_words.append(word[::-1])
#
# result = " ".join(reversed_words)
# print(result)

#Question 3-------------------------------------------------------------
#
# str=input("Enter a string: ")
# if str == str[::-1]:
#      print("str is palindrome")
# else:
#      print("str is not palindrome")

#Question 4-------------------------------------------------------------

# str=input("Enter a string: ")
# freq={}
# for char in str:
#     if char in freq:
#         freq[char]+=1
#     else:
#         freq[char]=1
# print("character frequency: ")
# for key,value in freq.items():
#     print(key,":",value)

#Question 5-------------------------------------------------------------
s="Python"
try:
 s[0]="J"
except TypeError as e:
    print("Error",e)



