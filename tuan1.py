#bai1


#bai2

import math

def tinh_chu_vi_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong
    return chu_vi, dien_tich

def tinh_chu_vi_dien_tich_hinh_tam_giac(canh_a, canh_b, canh_c, chieu_cao):
    chu_vi = canh_a + canh_b + canh_c
    dien_tich = 0.5 * chieu_cao * (canh_a + canh_b)
    return chu_vi, dien_tich

def tinh_chu_vi_dien_tich_hinh_tron(ban_kinh):
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh ** 2
    return chu_vi, dien_tich

def tinh_chu_vi_dien_tich_hinh_vuong(canh):
    chu_vi = 4 * canh
    dien_tich = canh ** 2
    return chu_vi, dien_tich

def tinh_chu_vi_dien_tich_hinh_thang(canh_day_lon, canh_day_nho, chieu_cao):
    chu_vi = canh_day_lon + canh_day_nho + 2 * math.sqrt((canh_day_lon - canh_day_nho) ** 2 + chieu_cao ** 2)
    dien_tich = 0.5 * (canh_day_lon + canh_day_nho) * chieu_cao
    return chu_vi, dien_tich

# Chương trình chính
def main():
    print("Chương trình tính chu vi và diện tích các hình học")
    print("a) Hình chữ nhật")
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)
    print("Chu vi của hình chữ nhật là:", chu_vi)
    print("Diện tích của hình chữ nhật là:", dien_tich)

    print("\nb) Hình tam giác")
    canh_a = float(input("Nhập cạnh a: "))
    canh_b = float(input("Nhập cạnh b: "))
    canh_c = float(input("Nhập cạnh c: "))
    chieu_cao = float(input("Nhập chiều cao: "))
    chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_tam_giac(canh_a, canh_b, canh_c, chieu_cao)
    print("Chu vi của hình tam giác là:", chu_vi)
    print("Diện tích của hình tam giác là:", dien_tich)

    print("\nc) Hình tròn")
    ban_kinh = float(input("Nhập bán kính: "))
    chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_tron(ban_kinh)
    print("Chu vi của hình tròn là:", chu_vi)
    print("Diện tích của hình tròn là:", dien_tich)

    print("\nd) Hình vuông")
    canh = float(input("Nhập cạnh: "))
    chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_vuong(canh)
    print("Chu vi của hình vuông là:", chu_vi)
    print("Diện tích của hình vuông là:", dien_tich)

    print("\ne) Hình thang")
    canh_day_lon = float(input("Nhập chiều dài cạnh đáy lớn: "))
    canh_day_nho = float(input("Nhập chiều dài cạnh đáy nhỏ: "))
    chieu_cao = float(input("Nhập chiều cao: "))
    chu_vi, dien_tich = tinh_chu_vi_dien_tich_hinh_thang(canh_day_lon, canh_day_nho, chieu_cao)
    print("Chu vi của hình thang là:", chu_vi)
    print("Diện tích của hình thang là:", dien_tich)

if __name__ == "__main__":
    main()
