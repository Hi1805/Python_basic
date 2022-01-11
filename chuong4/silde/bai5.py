# Bài 5: Viết chương trình tách từ thành 1 danh sách và sắp xếp các từ theo alphabe.
# my_str = "Hello this Is an Example With cased letters"
# Nếu muốn người dung nhập vào thì thay bằng lệnh sau
my_str = input("Enter a string: ")
# Tách từ trong chuỗi và lưu vào danh sách ds_tu
ds_tu = my_str.split()
# Sắp xếp các phần tử (từ) trong danh sách từ ds_tu
ds_tu.sort()
# Hiển thị từ từ trong danh sách
print("Các từ đã được tách và sắp xếp theo Alphabe")
for tu in ds_tu:

    print(tu)