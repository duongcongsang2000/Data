import json

# Mở file JSON để đọc
with open('Data.json', 'r', encoding='utf-8') as file:
    # Sử dụng json.load để đọc nội dung từ file và chuyển đổi thành Python data structure
    data = json.load(file)

# In ra nội dung đã đọc
print(data)
