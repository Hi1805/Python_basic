#Bài 4: Viết một chương trình thay thế một từ trong chuỗi. Yêu cầu: 
# Nhập vào một chuỗi 
# Nhập vào một từ cần thay thế và một từ thay thế. 
# Sau đó, hiển thị kết quả ra màn hình.
st1 = input("Nhập chuỗi của bạn: ")
st2 = input("Nhập từ cần thay thế: ")
st3 = input("Nhập từ thay thế: ")

st1 = st1.replace(st2,st3)
print(st1)