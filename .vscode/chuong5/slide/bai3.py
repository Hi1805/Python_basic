 # -*- coding: utf-8 -*
#Sử dụng cấu trúc từ điển, viết một chương trình nhập một câu, 
# in số chữ cái và chữ số
# trong câu đó. Giả sử đầu vào chuỗi: hello world! 123
# Thì đầu ra sẽ là:
# - Số chữ cái là: 10
# - Số chữ số là: 3
# Gợi ý: giả sử ch là một ký tự. Thì:
# - ch.isalpha() = True nếu ch là ký tự chữ cái
# - ch.isdigit() = True nếu ch là ký tự số

chuoi = str(input("Please Enter sentences :"))
d= {"chu_cai":0 , "chu_so": 0}
for ch in chuoi:
    if ch.isalpha() == True:
        d[chu_cai] +=1
    elif ch.isdigit()  == True:
        d[chu_so] +=1
    else:
      pass

print("Số chữ cái là:",d["chu_cai"])
print("Số chữ số là:", d["chu_so"])