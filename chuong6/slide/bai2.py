# Bài 2: Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1
# đến 20 (tính cả 1 và 20). Sau đó thực thi hàm.
# Gợi ý:
# Sử dụng toán tử ** để lấy giá trị bình phương.
# Sử dụng range() cho vòng lặp.
# Sử dụng phương thức append() để thêm giá trị vào danh sách.

def Tao_In_DS():
    ds=list()
    for i in range(1,21):
        ds.append(i**2)
    print(ds)
Tao_In_DS()