email = input("Nhập địa chỉ email: ")
username, domain = email.split("@")
first_3_chars = username [0:3]
masked_email = first_3_chars + "***@" + domain
print("Email bảo mật:", masked_email)
