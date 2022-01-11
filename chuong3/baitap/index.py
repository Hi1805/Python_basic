
 # -*- coding: utf-8 -*
# Viết chương trình đọc một số nguyên từ người dùng.
#  Sau đó, chương trình của bạn sẽ hiển thị một 
# thông báo cho biết số nguyên là chẵn hay lẻ.'

def printTypeNumber(number):
    if(int(number) % 2 != 0):
        print("Number is odd Number");
    else:
        print("Number is even Number")
# Viết chương trình đọc một chữ cái từ người dùng.
#  Nếu người dùng nhập a, e, i, o hoặc u thì chương trình 
#  hiển thị thông báo cho biết rằng chữ cái đã nhập là nguyên âm.
#   Nếu người dùng nhập y thì chương trình hiển thị thông báo cho biết 
#   có thể y là nguyên âm hoặc phụ âm. Nếu không, chương trình sẽ hiển 
#   thị thông báo cho biết chữ cái là phụ âm.

#consonant : Phụ âm
#vowel : Nguyên âm
def printTypeCharacter(char):
    vowel = "aeio";
    if(char in vowel):
        print("Character is vowel")
    else:
        if(char == "y"):
            print("Char is consonant or vowel")
        else:
            print("Char is consonant")

# printTypeCharacter(str(input("Please Enter Character : ")))


# Viết chương trình xác định tên của hình dựa trên số cạnh của nó.
#  Ví dụ, nhập số 3 thì là hình tam giác, 4 hình tứ giác ,... 
#  Yêu cầu: Chương trình hỗ trợ các hình dạng từ 3 đến 10 cạnh.
#   Nếu số cạnh vượt ra bên ngoài phạm vi này thì chương trình 
#   sẽ hiển thị thông báo lỗi thích hợp.
#numberEdge : Số cạnh
#conform : Phù hợp, đúng theo 
def printTypeOfShape(numberEdge):
    if(int(numberEdge) < 2 or int(numberEdge) > 10):
        print("Number Edge don't conform shape ")
    switcher ={
        3:"This is Triangle",
        4:"This is Quadrangle",
        5:"This is Pentagon",
        6:"This is Hexagon",
        7:"Hình Thất Giác :v",
        8:"Hình Bát Giác",
        9:"Hình Cửu Giác",
        10:"Hình Thập Giác"
    }
    print(switcher.get(numberEdge))

# printTypeOfShape(5)

#Bai 4  
#Số ngày của một tháng thay đổi từ 28 đến 31 ngày. 
# Viết chương trình đọc tên của một tháng từ người dùng dưới dạng một chuỗi
# . Sau đó, chương trình sẽ hiển thị số ngày trong tháng đó
#  (Chú ý: tháng 2 có 28 hoặc 29 ngày).


def getTotalDayInMonth(month):

    #nghien cuu them
    switcher ={
        "one" or "mot": "31",
        "two" or "hai":"28 or 29 ",
        "three" or "ba":"31",
        "four"or "bon":"30",
        "five"or "nam":"31",
        "six" or "sau":"30",
        "seven"or"bay":"31",
        "eight"or"tam":"31",
        "nine" or "chin":"30",
        "ten" or "muoi":"31",
        "eleven" or "muoi mot":"30",
        "twelve" or "muoi hai":"31"
    }
    return switcher.get(month.strip(),"month is invalid")

print(getTotalDayInMonth("   one   "))


