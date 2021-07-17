chuoi = input("Nhập vào một số:")
d= {"chu_hoa":0 , "chu_thuong": 0}
for ch in chuoi:
    if ch.isupper() == True:
        d[chu_hoa] +=1
    elif ch.islower() == True:
         d[chu_thuong] +1
    else:
      pass

print("Số chữ hoa là:", d["chu_hoa"])
print("Số chữ thường là:", d["chu_thường"])