# import math
# def cockroach_speed(s):

#     # Good Luck!
#     result = s *1000/3600
#     return math.floor(result)
     

# print(cockroach_speed(-384.47))

# def invert(lst):
#     return [x and -x for x in lst]

# print(invert([1,-2,3,4,5]))

# def digitize(n):
#     return 

# def digitize(n):
#     n = str(n)
#     result = []

#     for i in n:
#         result.append(int(i))
#     return list(reversed(result))
# print(digitize(35231))

# def greet(name):
#     #Good Luck (like you need it)
#     return "Hello, {} how are you doing today?".format(name)

# def summation(num):
#     result = []
#     x = range(1, num +1)
#     for i in x:
#         result.append(i)
#     print(sum(result))
# 
#         

# def func(**kwargs):
#     print(kwargs['zero'])

# func(a =0, zero = 8)

# def binary_array_to_number(arr):
#     total = 0
#     i = 1
#     for num in arr[::-1]:
#         total += (i*num)
#         i *= 2
#     return total


# binary_array_to_number([0, 0, 0, 1])
# # Testing: [0, 0, 1, 0]
# # Testing: [0, 1, 0, 1]
# # Testing: [1, 0, 0, 1]
# # Testing: [0, 0, 1, 0]
# # Testing: [0, 1, 1, 0]
# # Testing: [1, 1, 1, 1]
# # Testing: [1, 0, 1, 1]

# def smash(words):
#     list_1 = ''
#     for i in words:
#         list_1 += i + ' '
#     return list_1.strip()
    
# smash(['hello', 'world', 'this', 'is', 'great'])

# Regex validate PIN code

# def validate_pin(pin):
#     #return true or false
#     if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
#         return True
#     else:
#         return False


# Grasshopper - Grade book
def get_grade(s1, s2, s3):
    
    score = (s1 + s2 + s3) / 3 
    if score >= 90 and score <=100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'F'



