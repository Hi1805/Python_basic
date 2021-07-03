# Bài 2. Cho chuỗi biểu diễn địa chỉ email:   “•minhnhutvh@gmail.com”
# Rút trích và hiển thị chuỗi “gmail.com”. Đây chính là  tên Host
data = "minhnhutvh@gmail.com"
vitri = data.find('@')              
host = data[vitri +1 :]
print(host)