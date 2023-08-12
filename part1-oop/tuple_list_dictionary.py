# tuple
thang_nam_sinh = ("Tháng 5", 1990)
diem_so = (8, 9, 7, 10)

print(thang_nam_sinh[0])


#list
danh_sach_so = [1, 2, 3, 4, 5]
danh_sach_ten = ["An", "Bình", "Cường"]

print(danh_sach_ten[0])

danh_sach_so.append(10)
print(danh_sach_so)

danh_sach_so.remove(4)
print(danh_sach_so)
del(danh_sach_so[2])
print(danh_sach_so)


#dictionary
thong_tin_sinh_vien = {"ten": "Nguyễn Văn A", "tuoi": 20, "lop": "12A"}
diem_so = {"Toan": 9, "Van": 8, "Anh": 7}

print(thong_tin_sinh_vien["ten"])