# 1. Nhập Họ Tên đầy đủ
full_name = input("Nhập họ và tên đầy đủ: ").strip()

# 2. Nhập Năm sinh
birth_year = input("Nhập năm sinh: ").strip()

# Lấy từ cuối cùng trong họ tên làm "Tên" (VD: "Lê Văn Mẹo" -> "Mẹo")
name = full_name.split()[-1]

# 3. Lấy tối đa 3 ký tự đầu của Tên và chuyển thành chữ viết hoa
name_prefix = name[:3].upper()

# Tạo mã ưu đãi theo quy tắc: [3 chữ cái đầu Tên viết hoa]-[Năm sinh]-[VIP]
promo_code = f"{name_prefix}-{birth_year}-VIP"

# In kết quả
print("Mã ưu đãi của bạn là:", promo_code)
