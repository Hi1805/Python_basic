
 # -*- coding: utf-8 -*
# Bài 1: Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với
#  n là số nguyên được nhập
# vào (n> 0).

n=int(input("Please Enter Number >  0: "))

sum=0.0

for i in range(1,n+1):

    sum += float(float(i)/(i+1))

print(sum)

# Bài 2: Viết một chương trình chấp nhận đầu vào là một câu, đếm số ký tự hoa, số ký tự
# thường. Giả sử đầu vào là: Quản Trị Mạng

# Thì đầu ra là: Chữ hoa: 3

# Chữ thường: 8

st = input("Please Enter sentences: ")

tong_so_ky_tu_hoa = 0

tong_so_ky_tu_thuong = 0

for c in st:

    if c.isupper():

        tong_so_ky_tu_hoa +=1

    elif c.islower():

        tong_so_ky_tu_thuong +=1

    else:

        pass # bỏ qua, không thực hiện

print("Char Upper:", tong_so_ky_tu_hoa)
print("Char Lower:", tong_so_ky_tu_thuong)

# Bài 3: Một số được gọi là số Amstrong bậc N, nếu nó là số nguyên dương và tổng bậc N của
# các các chữ số cấu thành, bằng chính số đó.Ví dụ:

# Số Amstrong bậc 4: abcd = a4 + b4 + c4 + d4

# Số Amstrong bậc N: abc….d = aN + bN + cN + ….+ dN

# Cụ thể: 153 = 1*1*1 + 5*5*5 + 3*3*3 nên 153 số Amstrong.

# Viết chương trình nhập vào 1 số, cho biết số đó có phải là số Amstrong hay không?

num = int(input("Enter a number: "))
bac = int(input("level: "))
sum = 0
temp = num

while temp > 0:

    digit = temp % 10

    sum += digit ** bac

    temp //= 10

if num == sum:
    print(num, "is Number Amstrong, level: " + str(bac))

else:
    print(num, "This isn't Amstrong")


# Bài 4: Viết chương trình loại bỏ các ký tự không phải là ký tự CHỮ CÁI và SỐ trong một chuỗi.

# Ví dụ: Từ st1 = "He is very handsome@%^&%^"

# Trích thành chuỗi st2 = "He is very handsome"

# Định nghĩa chuỗi các ký tự cần loại bỏ

st1 = """!()-[]{};:""\,<>./?@#$%^&*_~"""

my_str = "Hello!!!, he said ---and went."

# Nếu muốn người dung nhập chuỗi vào thì dung lệnh sau

# my_str = input("Nhập vào một chuỗi: ")

# Loại bỏ ký tự cần loại bỏ

st2 = ""

for char in my_str:

    if char not in st1:

        st2 = st2 + char

# Hiển thị chuỗi sau khi loại bỏ

print(st2)