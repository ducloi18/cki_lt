# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:13:54 2024

@author: NGUYEN DUC LOI
"""

from datetime import datetime
import math
import random
def lab_1(num_a, num_b, num_c, num_d : int):   
    numbers = (num_a, num_b, num_c, num_d)
    average = sum(numbers) / len(numbers)
    return average
def lab_2(a, b: int):
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = round(a / b, 3)
    return tong, hieu, tich, thuong, round(a / b, 2)
def lab_3(a,b):
    kq_chia_nguyen = a // b
    kq_chia_du = a % b
    return kq_chia_nguyen, kq_chia_du
def lab_4(N):
    chu_so_hang_chuc = N // 10
    chu_so_hang_don_vi = N % 10
    tong_hai_chu_so_cua_N = chu_so_hang_chuc + chu_so_hang_don_vi
    if 10 <= N <= 99:
        return tong_hai_chu_so_cua_N
    return None
def lab_5(thoi_gian: int):
    gio, phut, giay = map(int, thoi_gian.split(":"))
    tong_giay = gio * 3600 + phut * 60 + giay
    return tong_giay
def lab_6(nam_sinh):
    nam_hien_tai = datetime.now().year
    tuoi_cua_ban = nam_hien_tai - nam_sinh
    return tuoi_cua_ban
def lab_7(r):
    C = 2*r*math.pi
    S = r*r*math.pi
    return round(C, 2)
    return round(S, 2)
def lab_8(cannang, chieucao):
    BMI = cannang / pow(chieucao, 2)
    return round(BMI, 1)
def lab_9(khach_chon: int):
    print("============ MENU ============")
    print("1. Hu tieu")
    print("2. Chao long")
    print("3. Banh canh")
    print("4. Bun rieu")
    print("5. Pho bo")
    print("==============================")
    menu = {
        1: "Hu tieu",
        2: "Chao long",
        3: "Banh canh",
        4: "Bun rieu",
        5: "Pho bo"
        }
    if khach_chon in menu:
        return (menu[khach_chon])
    return None
def lab_10(car_number: int):
    chu_so_hang_nghin = car_number // 1000
    chu_so_hang_tram = (car_number % 1000) // 100
    chu_so_hang_chuc = ((car_number % 1000) % 100) // 10
    chu_so_hang_don_vi = (car_number % 10)
    chu_so_xe = (chu_so_hang_nghin, chu_so_hang_tram, chu_so_hang_chuc, chu_so_hang_don_vi)
    so_nut = sum(chu_so_xe)
    if 0 <= so_nut <= 9:
        return f"Số nút của bạn là {so_nut} nút"
    else:
        a = so_nut // 10
        b = so_nut % 10
        so_nut_moi = a + b
        return so_nut_moi
def lab_11(chu_thuong):
    if len(chu_thuong) == 1 and chu_thuong.islower():
        chu_hoa = chu_thuong.upper()
        return chu_hoa
    return False
def lab_12():
    so_nguyen_ngau_nhien_a = random.randint(0, 100)
    so_nguyen_ngau_nhien_b = random.randint(50, 99)
    so_nguyen_ngau_nhien_c = random.randint(-39, 79)
    so_nguyen_ngau_nhien_d = random.randint(-79, -39)
    return "So nguyen ngau nhien la: ", so_nguyen_ngau_nhien_a, so_nguyen_ngau_nhien_b, so_nguyen_ngau_nhien_c, so_nguyen_ngau_nhien_d
    so_thuc_ngau_nhien_a = random.uniform(0, 100)
    so_thuc_ngau_nhien_b = random.uniform(50, 99)
    so_thuc_ngau_nhien_c = random.uniform(-39, 79)
    so_thuc_ngau_nhien_d = random.uniform(-79, -39)
    return "So thuc ngau nhien la: ", so_thuc_ngau_nhien_a, so_thuc_ngau_nhien_b, so_thuc_ngau_nhien_c, so_thuc_ngau_nhien_d
def lab_13_a(day, month, year: int):
    format_a = f"{day}/{month}/{year}"
    format_b = f"{day}/{month}/{str(year)[2:]}"
    format_c = f"{year}/{month}/{day}"
    return format_a, format_b, format_c
def lab_13_b():
    input_a = input("Nhập theo định dạng Ngày/Tháng/Năm: ")
    input_b = input("Nhập theo định dạng Ngày/Tháng/2 số cuối của Năm: ")
    input_c = input("Nhập theo định dạng Năm/Tháng/Ngày: ")
    day_a, month_a, year_a = map(int, input_a.split('/'))
    day_b, month_b, year_b = map(int, input_b.split('/'))
    year_b += 1900 if year_b > 50 else 2000
    year_c, month_c, day_c = map(int, input_c.split('/'))
    return day_a, month_a, year_a
    return day_b, month_b, year_b
    return day_c, month_c, year_c
def lab_14():
    A = (32 ** 0.2) - ((1/64) ** -0.25) + ((8/27) ** (1/3))
    return round(A, 3)
def lab_15(a, b):
    A = ((a+b)/(pow(a, 1/3) + pow(b, 1/3)) - pow(a*b, 1/3))  / pow((pow(a, 1/3) - pow(b, 1/3)), 2)
    return A
def lab_16(thoi_gian):
    so_thoi_gian = ""
    for i in thoi_gian:
        if i.isalpha():
            so_thoi_gian += ":"
        else:
            so_thoi_gian += i
    thoi_gian_dung = so_thoi_gian[:-1]
    hh, pp, ss = map(int, thoi_gian_dung.split(":"))
    so_giay = hh * 3600 + pp * 60 + ss
    return so_giay
def lab_17(a,b,c: int):
    so_lon_nhat = max(a, b, c)
    so_nho_nhat = min(a, b, c)
    return so_lon_nhat, so_nho_nhat
def lab_18(thoi_gian_1, thoi_gian_2: str):
    hh, mm, ss = map(int, thoi_gian_1.split(":"))
    h, m, s = map(int, thoi_gian_2.split(":"))
    tong_giay_1 = hh * 3600 + mm * 60 + ss
    tong_giay_2 = h * 3600 + m * 60 + s
    hieu_thoi_gian = tong_giay_1 - tong_giay_2
    if hieu_thoi_gian > 0:
        h1 = hieu_thoi_gian // 3600
        m1 = (hieu_thoi_gian % 3600) // 60
        s1 = hieu_thoi_gian % 60
        return f"Hiệu của 2 thời gian là: {h1}:{m1}:{s1}"
    else:
        return "Thời gian nhỏ hơn!"
    tong_thoi_gian = tong_giay_1 + tong_giay_2
    h2 = tong_thoi_gian // 3600
    m2 = (tong_thoi_gian % 3600) // 60
    s2 = tong_thoi_gian % 60
    return f"Tổng của 2 thời gian là: {h2}:{m2}:{s2}"
def lab_19(a,b,c,d: int):
    min_value = a
    if b < a:
        min_value = b
    if c < a:
        min_value = c
    if d < a:
        min_value = d
    return min_value
def lab_20(a,b,c: int):
    max_value = a
    if max_value < b:
        max_value = b
    if a < c:
        max_value = c
    return max_value
def lab_21(nhap):
    nhap = int(nhap)
    dinh_dang = {
    0: "Không",
    1: "Một",
    2: "Hai",
    3: "Ba",
    4: "Bốn",
    5: "Năm",
    6: "Sáu",
    7: "Bảy",
    8: "Tám",
    9: "Chín"
    }
    if nhap in dinh_dang:
        return dinh_dang[nhap]
    return None
def lab_22(a,b):
    if a == 0 and b == 0:
        return " pt có vô số nghiệm"
    elif a == 0 and b != 0:
        return " pt vô nghiệm"
    return " pt có 1 nghiệm x=", -b/a
def lab_23(a,b,c: int):
    denta = b*b - (4*a*c)
    if a == 0:
        return " pt có 1 nghiệm duy nhất x=", -b/c
    elif a != 0 and denta < 0:
        return " pt vô nghiệm"
    elif a != 0 and denta == 0:
        return "pt có nghiệm kép x1=x2 = ", -b/(2*a)
    elif a != 0 and b*b-(4*a*c) > 0:
        return "pt có 2 nghiệm pb x1 = ", (-b + math.sqrt(denta))/(2*a)
        return "pt có 2 nghiệm pb x2 = ", (-b - math.sqrt(denta))/(2*a)
    return None
def lab_24(gio, phut, giay: int):
    if gio > 24 or (phut and giay) > 60:
        return "Thời gian nhập vào không hợp lệ!"
    return f"Thời gian hợp lệ {gio}/{phut}/{giay}"
def lab_25(nhap: str):
    if len(nhap) == 1:
        if nhap.lower:
            return nhap.upper()
        elif nhap.upper():
            return nhap.lower()
        return "Không nhận diện được"
    return "Khong dung"
def lab_26_a(a,b,c: int):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c
def lab_26_b(N):
    danh_sach = list(N)
    sap_xep = danh_sach.sort()
    sap_xep_danh_sach = "".join(danh_sach)
    return sap_xep_danh_sach
def lab_27(hinh, pheptinh, *args, **kwargs):
    hinh_name = ["v", "n","t"]
    pheptinh = ["chuvi", "dientich"]
    if hinh in hinh_name:
        if hinh == "v":
            canh = args[0]
            return canh * 4 if pheptinh == "chuvi" else pow(canh, 2)
        elif hinh == "n":
            dai = args[0]
            rong = args[1]
            return (dai + rong) * 2 if pheptinh == "chuvi" else dai * rong
        elif hinh == "t":
            r = args[0]
            return math.pi * 2 * r if pheptinh == "chuvi" else math.pi * r * r
    return None
def lab_28(N: int):
    while N < 0:
        return "Nhap lai"
    uoc = []
    for i in range(1, N+1):
        if N % i == 0:
            uoc += [i]
    return uoc
def lab_29(N: int):
    tong_cac_chu_so = 0
    while N < 0:
        return False
    for i in str(N):
        tong_cac_chu_so += int(i)
    return "Tổng các chữ số của N là: ", tong_cac_chu_so
def lab_30(chuoi: str):
    ngay, thang, nam = map(int, chuoi.split("/"))
    def nam_nhuan(nam):
        nam = str(nam)
        duoi = nam[2:]
        if duoi == "00":
            if int(nam) % 400 == 0:
                return "Năm nhuận"
            return "Không phải năm nhuận"
        else:
            if int(nam) % 4 == 0 and int(nam) % 100 != 0:
                return "Năm nhuận"
            return "Không phải năm nhuận"
        if 1 > ngay or ngay > 31:
            return False
        if 1 < thang or thang > 12:
            return False
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay = 31
        return f"Số ngày của tháng {thang} là {so_ngay}"
    elif thang in [4, 6, 9, 11]:
        so_ngay = 30
        return f"Số ngày của tháng {thang} là {so_ngay}"
    else:
        if nam_nhuan(nam):
            so_ngay = 29
            return f"Số ngày của tháng {thang} là {so_ngay}"
        else:
            so_ngay = 28
            return f"Số ngày của tháng {thang} là {so_ngay}"
def lab_31(a,b,c: int):
    dinh_dang = {
        (True, False, False) : "cân tại đỉnh C",
        (False, True, False) : "cân tại đỉnh B",
        (False, False, True) : "cân tại đỉnh A"}
    def tam_giac(a,b,c):
        if a + b > c and a + c > b and b + c > a:
            return f"{a},{b},{c} tạo thành 1 tam giác"
    if tam_giac(a,b,c):
        if a == b == c:
            return f"{a},{b},{c} tạo thành 1 tam giác đều"
        elif a == b != c or a == c != b or b == c != a:
            return f"{a},{b},{c} tạo thành một tam giác {dinh_dang[(a == b, a == c, b == c)]}"
        elif pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2):
            return f"{a},{b},{c} tạo thành 1 tam giác vuông"
        elif (pow(a, 2) + pow(b, 2) == pow(c, 2) and a == b != c) or \
             (pow(a, 2) + pow(c, 2) == pow(b, 2) and a == c != b) or \
             (pow(b, 2) + pow(c, 2) == pow(a, 2) and b == c != a):
                 return f"{a},{b},{c} tạo thành 1 tam giác vuông cân"
    return f"{a},{b},{c} không tạo thành 1 tam giác"
def lab_32(d):
    tien = 0
    if d < 1:
        tien += d * 150000
    if 2 <= d < 6:
        tien += 15000 + ((d - 1) * 13500)
    if 6 <= d:
        tien += 15000 + 67500 + ((d - 6) * 11000)
    if d > 120:
        tien *= 0.9
        tien = float(tien)
    return f"Số tiền bạn cần trả là: {tien} VNĐ"
def lab_33_socp(so):
    so_cp = math.sqrt(so)
    so_cp = int(so_cp)
    if so_cp * so_cp == so:
        return True
    return False
def lab_34_songuyento(so):
    if so < 2:
        return False
    kiemtra = math.sqrt(so)
    for i in range(2, kiemtra + 1):
        if so % i == 0:
            return False
        return True
def lab_35(n):
    tong = 0
    for i in range (1, n + 1):
        tong += i
    return tong
def lab_36(n):
    tong = 0
    for i in range(1, n + 1):
        tong += pow(i,2)
    return tong
def lab_37(n):
    tong = 0
    for i in range(2, n + 1, 2):
        tong += i
    return tong
def lab_38(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich
def lab_39(n):
    tong = 0
    for i in range(1, n + 1):
        tong += (1/i)
    return tong
def lab_40(n):
    tong = 0
    for i in range(2, n + 1, 2):
        tong += (1/i)
    return tong
def lab_41(n):
    tong = 0
    for i in range(1, n + 1, 2):
        tong += (1/i)
    return tong
def lab_42(n):
    tong = 0
    for i in range(1, n + 1):
        tong *= 1/ (i * (i + 1))
    return tong
def lab_43(n):
    tong = 0
    for i in range(1, n + 1):
        tong += (i / (i + 1))
        tong = float(tong)
    return tong
def lab_44(n):
    tong = 0 
    for i in range(1, n + 1, 2):
        tong += i / (i + 1)
    return tong
def lab_45(x, n):
    S = 0
    s = 0
    for i in range(1, n + 1):
        s += i
        S += pow(x, i) / s
        S = float(S)
    return S
def lab_46():
    print("Cho phương trình:", "\n", "2x + 7y + 9z = 979 với (x, y, z > 0)")
    bo_nghiem = []
    for x in range(1, int(979 / 2) + 1):
        for y in range(1, int((979 - (2 * x)) / 7) + 1):
            for z in range(1, int((979 - (2 * x) - (7 * y)) / 9) + 1):
                if (2 * x) + (7 * y) + (9 * z) == 979:
                    bo_nghiem.append((x, y, z))
    if bo_nghiem:
        return f"Các bộ nghiệm nguyên của phương trình là: {bo_nghiem}"
    else:
        return "Không có bộ nghiệm nguyên nào thỏa mãn."
def lab_47():
    print("Cho phương trình:", "\n", "2x + 7y + 9z = 979 với (x, y, z > 0)")
    bo_nghiem = []
    for x in range(1, int(979 / 2) + 1):
        for y in range(1, int((979 - (2 * x)) / 7) + 1):
            for z in range(1, int((979 - (2 * x) - (7 * y)) / 9) + 1):
                if (2 * x) + (7 * y) + (9 * z) == 979:
                    bo_nghiem.append((x, y, z))
    max_bo_nghiem = bo_nghiem[0]
    max_tong = sum(max_bo_nghiem)
    for nghiem in bo_nghiem:
        tong = sum(nghiem)
        if tong > max_tong:
            max_tong = tong
            max_bo_nghiem = nghiem
    return f"Bộ nghiệm có tổng lớn nhất là: {max_bo_nghiem}, với tổng là: {max_tong}"
def lab_48():
    print("Cho phương trình:", "\n", "2x + 7y + 9z = 979 với (x, y, z > 0)")
    bo_nghiem = []
    for x in range(1, int(979 / 2) + 1):
        for y in range(1, int((979 - (2 * x)) / 7) + 1):
            for z in range(1, int((979 - (2 * x) - (7 * y)) / 9) + 1):
                if (2 * x) + (7 * y) + (9 * z) == 979:
                    bo_nghiem.append((x, y, z))
    min_bo_nghiem = bo_nghiem[0]
    min_tong = sum(min_bo_nghiem)
    for nghiem in bo_nghiem:
        tong = sum(nghiem)
        if tong < min_tong:
            min_tong = tong
            min_bo_nghiem = nghiem
    return f"Bộ nghiệm có tổng lớn nhất là: {min_bo_nghiem}, với tổng là: {min_tong}"
def lab_49(so): 
    if so % 2 == 0 and so < 0:
        return True
    else:
        return False
def lab_50(so):
    if so < 0 and so % 2 == 1:
        return -1
    elif so > 0 and so % 2 == 0:
        return 1
    else:
        return 0
def lab_51(so):
    while so not in range(-89, 91):
        so = float(input("Nhập lại giá trị của số = "))
    return "Giá trị đã đúng", so
def lab_52(so):
    def can_bac_n(so, n):
        return so ** (1/n)
    def so_dao(so):
        dao = 0
        while so > 0:
            chu_so = so % 10
            dao = dao * 10 + chu_so
            so //= 10
        return dao
    def sodao(so):
        return str(so)[::-1]
    def so_chinh_phuong(so):
        so_cp = math.sqrt(so)
        so_cp = int(so_cp)
        if so_cp * so_cp == so:
            return True
        return False
    def so_nguyen_to(so):
        if so < 2:
            return False
        for i in range(2, int(math.sqrt(so)) + 1):
            if so % i == 0:
                return False
        return True
    def tich_so_le(so):
        tich = 1
        for i in range(1, so + 1, 2):
            tich *= i
        return tich
    def tong_cac_so_nguyen_to(so):
        tong = 0
        for i in range(2, so):
            if so_nguyen_to(i):
                tong += i
        return tong
    def tong_cac_so_chinh_phuong(so):
        tong = 0
        for i in range(2, so):
            if so_chinh_phuong(i):
                tong += i
        return tong
    def tong_cac_uoc_so_duong(so):
        tong = 0
        for i in range(1, so + 1):
            if so % i == 0:
                tong += i
        return tong
def lab_53(n: int):
    def lab_53_a(n):
        tong = 0
        for i in range(1, n + 1):
            tong += i
        return tong
    def lab_53_b(n):
        tong = 0
        for i in range(1, n + 1):
            tong += pow(i, 2)
        return tong
    def lab_53_c(n):
        tong = 0 
        for i in range(1, n + 1):
            tong += 1/i
        return tong
    def lab_53_d(n):
        def giai_thua(n):
            tong_n = 0
            tong = 0
            for i in range(1, n +1):
                tong += i
                tong_n += tong
            return tong_n
    def lab_53_e(n):
        tich = 1 
        for i in range(1, n + 1):
            tich *= i
        return tich
def lab_54(n):
    ds = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    while a < n:
        ds.append(a)
        a, b = b, a + b
    return ds
pheptinh = ["chuvi", "dientich"]
def lab_55():
    def chuvi_dientich(pheptinh, *args, **kwargs):
        dai = args[0]
        rong = args[1]
        if pheptinh == "chuvi":
            return (dai + rong) * 2
        elif pheptinh == "dientich":
            return dai * rong
        else:
            return "Tham số không hợp lệ!"
        def vehcn(rong, cao):
            hinh = ""
            for i in range(cao):
                hinh += "*" * rong + "\n"
            return hinh
def lab_56(*args, **kwargs):
    hinh_name = ["vuong", "chu_nhat", "tron"]
    pheptinh = ["cv", "dt"]
    hinh = kwargs.get("hình")
    tinh_toan = kwargs.get('tinh')
    if hinh not in hinh_name:
        return "Không hợp lệ"
    if tinh_toan not in pheptinh:
        return "Không hợp lệ"
    if hinh == 'vuong':
        canh = args[0]
        return canh * 4 if tinh_toan == "cv" else canh ** 2

    elif hinh == 'chu_nhat':
        dai, rong = args
        return 2 * (dai + rong) if tinh_toan == 'cv' else dai * rong
    elif hinh == 'tron':
        ban_kinh = args[0]
        return 2 * math.pi * ban_kinh if tinh_toan == 'cv' else math.pi * (ban_kinh ** 2)
    return "Thông số không hợp lệ"