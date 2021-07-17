# Bài 7: Viết Chương trình nhập các số từ bàn phím, 
# các giá trị này lưu vào danh sách. Sau đó,
# in ra giá trị trung bình.

numlist = list()

while (True):
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Giá trị Trung bình:", average)

print(numlist)