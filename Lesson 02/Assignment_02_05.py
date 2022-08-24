
yn='y'
while yn=='y':
    luong=float(input("Nhập mức lương : "))
    tlhh=float(input("Nhập tỷ lệ hoa hồng % : "))
    tienhh=luong*tlhh/100
    print('Hoa hồng được hưởng là :', tienhh)
    yn=input('Bạn có muốn tiếp tục không (y/n)')