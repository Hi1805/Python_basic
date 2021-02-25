# Cho trước 3 số nguyên x, y, z được từ bàn phím. Bạn hãy viết chương trình hiển thị ra màn hình theo yêu cầu sau:

# Nếu x là số chẵn, kiểm tra xem y có lớn hơn hoặc bằng 20 hay không. Nếu y >= 20, in ra dòng chữ y is greater than or equal to 20; ngược lại, in ra dòng chữ y is less than 20.
# Nếu x là số lẻ, kiểm tra xem z có lớn hơn hoặc bằng 30 hay không. Nếu z >= 30, in ra dòng chữ z is greater than or equal to 30; ngược lại, in ra dòng chữ z is less than 30.
# Ví dụ:

# Với x = 20, y = 33, z = 15 thì in ra màn hình y is greater than 20. Vì x % 2 == 0 và y > 20
# Với x = 15, y = 23, z = 20 thì in ra màn hình z is less than 30.
# Vì x % 2 != 0 và z < 30   
x = int(input());
y = int(input());
z = int(input());
if (x % 2 == 0):
    if y >= 20 :
        print("y is greater than or equal to 20");
    else : print("y is less than 20");
