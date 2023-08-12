# Định nghĩa lớp
class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def gioi_thieu(self):
        print(f"Xin chào, tôi là {self.ten}, {self.tuoi} tuổi.")

# Tạo đối tượng

sv1 = SinhVien("Nguyễn Văn A", 20)
sv2 = SinhVien("Trần Thị B", 22)

sv1.gioi_thieu()  
sv2.gioi_thieu()  