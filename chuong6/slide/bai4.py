
# def tuDienSinhVien():
#     danhsachtudien = []
#
#     while(1):
#         tudien = {};
#         mssv = str(input("vui long nhap mssv : ,nhap 000 de thoat" ))
#         if(mssv=="000"):
#             break;
#         ten = str(input("vui long nhap ho ten"))
#         tudien[mssv] = ten
#         danhsachtudien.append(tudien)
#     return danhsachtudien
# print(tuDienSinhVien())

# def danhSachSoChan():
#     DS_so_chan =[];
#     i = 2;
#     while(i != 100):
#         DS_so_chan .append(i)
#         i = i + 2
#     print(DS_so_chan [0:4])
#
# danhSachSoChan()
from os.path import join


# def taoDanhSachChuoi():
#     Danh_Sach_Chuoi = []
#     while(1):
#         str = input("vui long nhap chuoi, hoac nhap exit de thoat :")
#         if(str.strip() == "exit"):
#             break
#         Danh_Sach_Chuoi.append(str)
#     return  " ".join(Danh_Sach_Chuoi)
#
# print(taoDanhSachChuoi())

# def tongTupple():
#     tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     sum = 0
#     for i in range(0,5):
#         sum = sum + tp[i]**2
#     return sum
# print(tongTupple())
#
# def replaceName():
#     oldFullName = input("vui long nhap ho va ten cua ban: ")
#     name = input("nhap ten thay the : ")
#     newName = input("vui long nhap ten thay the:")
#
#
#     print(oldFullName.replace(name,newName).title())
#
# replaceName()


def findMaxAndMinArray():
    arr = []
    while(1):
        n = int(input("vui long nhap so : "))
        arr.append(n)
        check = input("nhap done neu ban muon dung : ")
        if (check.strip() == "done"):
            break
    print("max la : ", max(arr))
    print("min la : ", min(arr))

findMaxAndMinArray()





