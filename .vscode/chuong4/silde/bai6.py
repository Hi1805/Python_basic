 # -*- coding: utf-8 -*
# Bài 6: Viết Chương trình nhập các số từ bàn phím. In ra giá trị trung bình
total = 0
count = 0
while (True):
    inp = input("Enter a number: ")
    if inp == "done":
         break

value = float(inp)
total = total + value
count = count + 1
average = total / count
print("average is:", average)