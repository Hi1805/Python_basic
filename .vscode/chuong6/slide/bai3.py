# Bài 3: Định nghĩa một hàm có thể tạo danh sách chứa các giá trị bình phương của các số từ 1
# đến 20 (bao gồm cả 1 và 20) và in 5 phần tử đầu tiên cùng với 5 phần tử cuối cùng trong danh
# sách.
#
# Gợi ý:
#
# Sử dụng toán tử ** để lấy giá trị bình phương.
#
# Sử dụng range() cho vòng lặp.
#
# Sử dụng phương thức append() để thêm giá trị vào danh sách.
#
# Sử dụng [n1:n2] để trích danh sách và in

def Tao_In_DS():
    ds=list()
    for i in range(1,21):
        ds.append(i**2)
    print(ds[:5]+ds[len(ds)-5:])

Tao_In_DS()