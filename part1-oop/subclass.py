# Định nghĩa lớp và lớp con
class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong
    
    def gioi_thieu(self):
        print(f"Tôi là {self.ten}, lương {self.luong}")
        
class GiamDoc(NhanVien):
    # pass

    def gioi_thieu(self): # hàm ghi đè
        print(f"Tôi là giám đốc {self.ten}, lương {self.luong}")

# Sử dụng
nhan_vien1 = NhanVien("Nguyễn Văn A", 5000)
nhan_vien2 = GiamDoc("Trần Thị B", 10000)

nhan_vien1.gioi_thieu()  
nhan_vien2.gioi_thieu()  

