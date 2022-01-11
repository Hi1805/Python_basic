import os
TenFile =str(input("Nhap vao ten File: "))
print(TenFile)

st = open("vd.txt")

tuDienTu = dict()
for dong in st:
    tachTuTrongMotDong = dong.split()
    for tu in tachTuTrongMotDong:
        if tu not in tuDienTu:
              tuDienTu[tu] = 1
        else:
              tuDienTu[tu] += 1

print(tuDienTu)

