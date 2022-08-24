giolv=float(input("Nhập số giờ làm việc : "))
luonggio=float(input("Nhập mức lương / giờ : "))
if giolv>40 :
    print('Tiền lương làm thêm giờ : ',luonggio*(giolv+(giolv-40)*1.5))
else:
    print('Tiền lương thường : ',luonggio*giolv)
