 # -*- coding: utf-8 -*

# Bài 1. Viết chương trình nhập vào một chuỗi
# In ra màn hình chuỗi ký tự hoa
# In ra màn hình chuỗi ký tự có ký tự đầu là ký tự hoa
# In ra màn hình chuỗi ký tự thường

st = input("Nhập vào chuỗi ký tự của bạn:")
chuoi_hoa = st.upper()
chuoi_thuong = st.lower()
chuoi_kt_dau_tu_hoa = st.title()

print("Chuỗi ký tự hoa là: " + chuoi_hoa)
print("Chuỗi ký tự thường là: "+ chuoi_thuong)
print("“Chuỗi kt đầu từ hoa là: “" + chuoi_kt_dau_tu_hoa)
