# 1. Arrays — Sum of all elements
arr = [1, 2, 3, 4]
total = sum(arr)
print(total) 
#------------------------

# 2. Loops — Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()
#------------------------

# 3. Strings — Reverse a string
s = "hello"
reversed_s = s[::-1]
print(reversed_s) 
#------------------------

# 4. Math — Even or Odd
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#------------------------

# 5. Lists — Add element to end
lst = [1, 2, 3]
lst.append(4)
print(lst) 
#------------------------

# 6. Conditions — Positive, Negative, or Zero
num = -10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#------------------------

# 7. While Loops — Print 5 to 1
i = 5
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
#------------------------

# 8. Count Occurrences — How many times number appears
lst = [1, 2, 3, 2, 4, 2]
count = lst.count(2)
print(count)  
#------------------------

# 9. String Length
s = "apple"
length = len(s)
print(length)  
#------------------------

# 10. Max Number — Largest number in list
lst = [3, 5, 2, 8, 1]
max_num = max(lst)
print(max_num)  
#------------------------
