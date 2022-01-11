# Cho chuỗi biểu diễn:  
#         “minhnhutvh@gmai.com•Sat•Jan•5•09:14:16”
# Rút trích và hiển thị chuỗi “gmail.com”. Đây chính là tên Host
data = 'minhnhutvh@gmail.com Sat Jan  5 09:14:16'
vitribatdau = data.find('@')
vitriketthuc = data.find('•’, vitribatdau')
host = data[vitri +1 : vitriketthuc]
print(host)
