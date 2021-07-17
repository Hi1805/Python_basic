 # -*- coding: utf-8 -*
#bai 1: Viết một chương trình nhập vào một số nguyên dương. Nếu nó là số chẵn thì in ra
#chuỗi “Đây là số chẵn”, ngược lại thì in ra chuỗi “Đây là số lẻ”:
number = input("Please Enter Number: ")

if int(number)%2 == 0:
    print("Đây là số chẵn!")
else:
    print("Đây là số lẻ!")

#bai 2. Viết một chương trình kiểm tra một chuỗi nhập vào từ bàn phím: Chuỗi hoa; Chuỗi
#thường; Chuỗi chứa ký tự hoa và ký tự thường.: 
c = input("Nhập câu của bạn: ")

if c.isupper():

    print("Đây là chuỗi hoa")

elif c.islower():

     print("Đây là chuỗi thường")
else:
    print("Đây là chuỗi chứa ký tự hoa và ký tự thường")

# Bài 3. Viết một chương trình kiểm tra một chuỗi có trong chuỗi khác. Yêu cầu:

# Nhập vào một chuỗi st

# Nhập vào chuỗi cần tìm st_search

# Nếu có thì in ra màn hình “Đã tìm thấy chuỗi cần tìm, tại vị trí: …”.

st = input("Nhập vào chuỗi st: ")

st_search = input("Nhập vào chuỗi cần tìm:")

if st_search in st:

    print("Đã tìm thấy chuỗi cần tìm, tại vị trí: " +str(st.find(st_search)))
    
else:
    print("Không tìm thấy")

#Bài 4. Viết chương trình in số lớn nhất của 3 số

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):

    largest = num1

elif (num2 >= num1) and (num2 >= num3):

    largest = num2

else:

    largest = num3

print("The largest number between", num1, ",", num2, "and", num3,"is", largest)