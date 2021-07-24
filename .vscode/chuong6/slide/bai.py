# Viết một chương trình tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320

def factorial(n):
    if(n == 0):
        return 0
    result = 1;
    for i in range(2,n+1):
        result = result*i
    return result

print(factorial(8))