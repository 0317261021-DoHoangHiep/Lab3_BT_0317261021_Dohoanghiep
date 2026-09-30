# bai1_clean_data.py
print("--- HỆ THỐNG CRM: CHUẨN HÓA DỮ LIỆU ---")
# 1. Dữ liệu thô từ hệ thống
raw_name = "  nGuyễn thỊ pHươNg ThẢo  "
print(f"Dữ liệu gốc: '{raw_name}'")
# 2. Làm sạch dữ liệu (Có thể nối các hàm với nhau - Method chaining)
# - strip() xóa khoảng trắng ở 2 đầu
# - title() viết hoa chữ cái đầu mỗi từ
clean_name = raw_name.strip().title()
# 3. Xuất kết quả
print(f"Dữ liệu sạch: '{clean_name}'")
