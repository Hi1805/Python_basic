 # -*- coding: utf-8 -*
 #Tạo ra một tự điển, có n phần tử, 
 # các khóa là từ 1 đến n và giá trị tương ứng là bình phương
# của khóa. Sau đó in từ điển ra màn hình
n=int(input("Please Enter Number "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)