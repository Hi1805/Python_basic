# Viết một chương trình nhập vào 1 chuỗi. Sau đó, in ra màn hình: 
# 5 ký tự cuối cùng
# 5 ký tự đầu tiên. 
# 4 chuỗi trên một dòng cách 1 khoảng trắng.
# 4 chuỗi trên 4 dòng.

st = input("Nhập chuỗi của bạn: ")
chuoi_5_kt_dau = st[:5]
chuoi_5_kt_cuoi = st[len(st)-4:]
Bon_chuoi_1_dong = 4 * (st + " ")
Bon_chuoi_4_dong = 4 * (st + "\n")
print("“Năm ký tự đầu là: “ "+ chuoi_5_kt_dau)
print("“Năm ký tự cuối là: “" + chuoi_5_kt_cuoi)
print("Bốn chuỗi trên một dòng là: “" + Bon_chuoi_1_dong)
print("“Bốn chuỗi trên bốn dòng là: \n“" + Bon_chuoi_4_dong)

