luong=float(input("Nhập mức lương : "))
namlv=int(input("Nhập số năm làm việc : "))

if luong>=30000 :
    if namlv >=2 :
        print('Khách hàng đủ điều kiện cho khoản vay')
    else:    
                print('Khách hàng không đủ điều kiện cho khoản vay')
else:
    print('Khách hàng không đủ điều kiện cho khoản vay')
                
