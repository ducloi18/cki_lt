# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:47:08 2024

@author: NGUYEN DUC LOI
"""

import math
import random
import string
def question_1(n: int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#n = int(input("Nhập vào giá trị nguyên n: "))
#print(question_1(n))
def question_2():
    tong = 0
    ds = []
    for i in range(random.randint(1, 10)):
        n = random.randint(1, 100)
        ds += [n]
        tong += n
    trungbinh = tong / len(ds)
    print("Danh sách các số ngẫu nhiên là: ", ds, len(ds))
    return tong, trungbinh
#print(question_2())
def question_3(chuoi: str):
    dem_chu_thuong = 0
    dem_chu_hoa = 0
    for i in chuoi:
        if 'a' <= i <= 'z':
            dem_chu_thuong += 1
        elif 'A' <= i <= 'Z':
            dem_chu_hoa += 1
    return dem_chu_hoa, dem_chu_thuong
#chuoi = input("Nhập vào chuỗi: ")
#print(question_3(chuoi))
def question_4(n : int):
    if n % 2 == 0:
        return True
    return False
#n = int(input("Nhập số nguyên n: "))
#print(question_4(n))
def question_5(ds: list, x):
    if x in ds:
        return f"Giá trị {x} có vị trí là {ds.index(x)}" 
    return f"Giá trị {x} có vị trí là None"
#ds = [5, 10, 20, 15, 30, 21]
ds = ["c", 4, 5, "h", 9, "l"]
#x = input("Nhập giá trị x cần tìm: ")
#if x.isdigit():
    #x = int(x)
#print(question_5(ds))
def question_6(n: int):
    giaithua = 1
    for i in range(1, n + 1):
        giaithua *= i
    return giaithua
#n = int(input("Nhập vào số n: "))
#while n < 0:
    #n = int(input("Nhập lại n duong: "))
#print(question_6(n))
def question_7():
    ds = []
    for i in range(random.randint(1, 10)):
        n = random.uniform(0, 1)
        ds += [n]
    print("Danh sách các số thực là: ", ds)
    solonnhat = max(ds)
    sobenhat = min(ds)
    return solonnhat, sobenhat
#print(question_7())
def question_8(chuoi: str):
    chuoi = chuoi[::-1]
    return chuoi
#chuoi = input("Nhập vào chuỗi: ")
#print(question_8(chuoi))
def question_9(chuoi: str):
    chuoi = ''.join(char.lower() for char in chuoi if char.isalpha())
    if chuoi == chuoi[::-1]:
        return True
    return False
#chuoi = input("Nhập vào chuỗi: ")
#print(question_9(chuoi))
def question_10():
    nhap = input("Nhập vào các số nguyên trong danh sách, cách bởi dấu phẩy: ")
    ds = [int(num.strip()) for num in nhap.split(",") if num.strip()]
    if len(ds) == 0:
        return None
    return ds
#print(question_10())
def question_11(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
#n = int(input("Nhập số nguyên n của dãy fibonacy: "))
#print(f"Số Fibonacci thứ {n} là: {question_11(n)}")
def question_12(n: int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = random.randint(1, 1000)
#print(n)
#print(question_12(n))
def question_13(chuoi: str):
    tu = chuoi.split()
    print(tu)
    sotu = len(tu)
    return sotu
#chuoi = input("Nhập vào chuỗi: ")
#print(question_13(chuoi))
def question_14(chuoi: str):
    if chuoi.replace("-", "", 1). replace(".", "", 1).isdigit():
        return True
    return False
#chuoi = input("Nhập vào chuỗi: ")
#print(question_14(chuoi))
def question_15(bien):
    return bien is None
#bien = input("Nhập vào giá trị biến: ")
#if bien == "":
    #bien = None
#print(question_15(bien))
def question_16(*args: float):
    if len(args) == 0:
        return None
    trungbinhcong = sum(args) / len(args)
    return trungbinhcong
#so = (input("Nhập vào các tham số bất kỳ, cách nhau bởi dấu phẩy: "))
#ds = [float(num.strip()) for num in so.split(",") if num.strip()]
#ketqua = question_16(*ds)
#print(ketqua)
def question_17(n: int):
    ds = []
    for i in range(random.randint(1, 10)):
        n = random.randint(1, 100)
        ds += [n]
    print(ds)
    ds = sorted(ds, reverse= True)
    return ds
#print(question_17(n))
def question_18(chuoi: str):
    chuoi = chuoi.strip()
    chuoi = " ".join(chuoi.split())
    return chuoi
#chuoi = input("Nhập vào chuỗi: ")
#print(question_18(chuoi))
def question_19(so: int):
    sochotruoc = random.randint(1, 100)
    print(sochotruoc)
    if so < sochotruoc:
        return False
    return True
#so = int(input("Nhập vào số nguyên cần kiểm tra: "))
#print(question_19(so))
def question_20(giatri):
    if giatri == "":
        return None
    return giatri
#giatri = input("Nhập vào giá trị: ")
#print(question_20(giatri))
def question_21():
    def tim_cap_so(ds: list, tong: int):
        da_kiem_tra = set()
        cac_cap = []
        for so in ds:
            can_tim = tong - so
            if can_tim in da_kiem_tra:
                cac_cap.append((can_tim, so))
            da_kiem_tra.add(so)
        return cac_cap if cac_cap else None
    so = input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ")
    ds = [int(num.strip()) for num in so.split(",") if num.strip()]
    sochotruoc = int(input("Nhập vào số cho trước: "))
    cac_cap = tim_cap_so(ds, sochotruoc)

    if cac_cap:
        return f"Các cặp số có tổng bằng {sochotruoc} là: {cac_cap}"
    return f"Không tìm thấy cặp số nào có tổng bằng {sochotruoc}."
#if __name__ == "__main__":
    #print(question_21())
def question_22(so):
    index = 0
    for sokt in so:
        if sokt != 0:
            so[index] = sokt
            index += 1
    for i in range(index, len(so)):
        so[i] = 0
#so = input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#question_22(ds)
#print(ds)
def question_23(so):
    lap = set()
    for sokt in so:
        if sokt in lap:
            return True
        lap.add(sokt)
    return False
#so = input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(ds)
#print(question_23(so))
def question_24(ds):
   kiemtra = None
   dem = 0
   for sokt in ds:
       if dem == 0:
           kiemtra = sokt
           dem = 1
       elif sokt == kiemtra:
           dem += 1
       else:
           dem -= 1   
   return kiemtra
#so = input("Nhập vào dãy số danh sách, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(question_24(ds))
def question_25(ds):
    ds_moi = []
    for i in ds:
        i = pow(i, 2)
        ds_moi += [i]
    ds_moi = sorted(ds_moi, reverse= False)
    return ds_moi
#so = input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(question_25(ds))
def question_26_m(chuoi):
    dem = {}
    for char in chuoi:
        dem[char] = dem.get(char, 0) + 1
    do_dai = 0
    kt_le = False
    for i in dem.values():
        if i % 2 == 0:
            do_dai += i
        else:
            do_dai += i - 1
            kt_le = True
    if kt_le:
       do_dai += 1
    return do_dai
chuoi = "abccccdd"
#print("Độ dài của chuỗi palindrome dài nhất có thể:", question_26_m(chuoi))
def question_27_m(chuois):
    if not chuois:
        return ""
    tien_to = chuois[0]
    for chuoi in chuois[1:]:
        i = 0
        while i < len(tien_to) and i < len(chuoi) and tien_to[i] == chuoi[i]:
            i += 1 
        tien_to = tien_to[:i]
        if not tien_to:
            return ""
    return tien_to
#chuois = input("Nhập vào các chuỗi, cách nhau bởi dấu phẩy: ")
#ds = [str(s.strip()) for s in chuois.split(",") if s.strip()]
#print(question_27_m(ds))
def question_28_m(chuoi):
    dem = {}
    for char in chuoi:
        if char in dem:
            dem[char] += 1
        else:
            dem[char] = 1
    return dem
#chuoi = input("Nhập chuỗi: ")
#print(question_28_m(chuoi))
def question_29_m(ds):
    ds_moi = sorted(ds, reverse= False)
    print(ds_moi)
    trungvi = ds_moi[len(ds_moi) // 2]
    if len(ds_moi) % 2 == 0:
        trungvi = sum(ds) / len(ds)
        return trungvi
    return trungvi
#so = input("Nhập vào giá trị của chuỗi, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(question_29_m(ds))
def question_30_m(doan):
    doan = doan.lower()
    xoa = ""
    for  char in doan:
      if char not in string.punctuation:
          xoa += char
    so_tu = xoa.split()
    dem = {}
    for tu in so_tu:
        if tu in dem:
            dem[tu] += 1
        else:
            dem[tu] = 1
    return dem
#doan = input("Nhập vào đoạn văn: ")
#print(question_30_m(doan))
def question_31_m(doan):
    doan = doan.lower()
    xoa = ""
    for char in doan:
        if char not in string.punctuation:
            xoa += char
    so_tu = xoa.split()
    dem_tu = {}
    tong_tu = len(so_tu)
    for tu in so_tu:
        if tu in dem_tu:
            dem_tu[tu] += 1
        else:
            dem_tu[tu] = 1
    n = 0
    for tu, dem in  dem_tu.items():
        phantram = dem / tong_tu
        if phantram > 0.2:
            n += 1
    return n
#doan = input("Nhập đoạn: ")
#print(question_31_m(doan))
def question_32_m(ds):
    ds_moi = sorted(ds, reverse= False)
    chan = []
    le = []
    for i in ds_moi:
        if i % 2 == 0:
            chan.append(i)
        else:
            le.append(i)
    capchan = tuple(chan)
    capchan = sorted(capchan, reverse= True)
    caple = tuple(le)
    caple = sorted(caple, reverse= False)
    return capchan, caple
#so = input("Nhập vào danh sách các số, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(question_32_m(ds))
def question_33_m(so):
    ds_moi = list(set(ds))
    ds_moi.sort()
    print(ds_moi)
    if len(ds_moi) < 2:
        so_lon_thu_2 = None
    else:
        so_lon_thu_2 = ds_moi[-2]
    if len(ds_moi) < 5:
        so_be_thu_5 = None
    else:
        so_be_thu_5 = ds_moi[4]
    return so_lon_thu_2, so_be_thu_5
#so = input("Nhập vào các số, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in so.split(",") if num.strip()]
#print(question_33_m(ds))
def question_34_m(chuoi):
    chuoi_con_dai_nhat = ""
    ds_kt = []
    for char in chuoi:
        if char in ds_kt:
            while ds_kt and ds_kt[0] != char:
                del ds_kt[0]
            del ds_kt[0]
        ds_kt.append(char)
        if len(ds_kt) > len(chuoi_con_dai_nhat):
            chuoi_con_dai_nhat = "".join(ds_kt)
    return chuoi_con_dai_nhat
chuoi = "abcabcbb"
#ketqua = question_34_m(chuoi)
#print("Chuỗi con dài nhất không chứa ký tự lặp lại là:", ketqua)
def question_35_m(chuoi):
    chuoi_con_dai_nhat = ""
    n = len(chuoi)
    for i in range(1, n // 2 + 1):
        chuoi_con_da_gap = set()
        for m in range(n - i + 1):
            chuoi_con = chuoi[m:m + i]
            if chuoi_con in chuoi_con_da_gap:
                if len(chuoi_con) > len(chuoi_con_dai_nhat):
                    chuoi_con_dai_nhat = chuoi_con
            else:
                chuoi_con_da_gap.add(chuoi_con)
    return chuoi_con_dai_nhat
chuoi = "aabcdeaabcd"
#ketqua = question_35_m(chuoi)
#print("Chuỗi con lặp lại dài nhất là:", ketqua)
def question_36_m(so):
    def tao_hoanvi(hientai, dao):
        if not dao:
            ketqua.append(hientai)
        for i in range(len(dao)):
            tao_hoanvi(hientai + [dao[i]], dao[:i] + dao[i + 1:])
    ketqua = []
    tao_hoanvi([], nums)
    return ketqua
nums = [1, 2, 3]
#if __name__ == "__main__":
    #ham = question_36_m(nums)
    #print("Tất cả các hoán vị có thể của mảng là:", ham)
#hientai + [dao[i]]: thêm phần tử hiện tại vào hoán vị "hientai".
#dao[:i] + dao[i + 1:]: loại bỏ phần tử hiện tại ra khỏi dao.    
def question_37(chuoi: str):
    chuoi_kt = []
    cap = {')': '(', '}': '{', ']': '['}
    for char in chuoi:
        if char in cap:
           if not chuoi_kt:
               return False
           kt_dau = chuoi_kt[-1]
           if cap[char] != kt_dau:
               return False
           chuoi_kt = chuoi_kt[:-1]
        else:
           chuoi_kt.append(char)
    return not chuoi_kt
#chuoi = input("Nhập vào chuỗi kí tự: ")
#print(question_37(chuoi))
def question_38_m(n):
    if n == 0 or n == 1:
        return 1
    bien_0 = 1
    bien_1 = 1
    for i in range(2, n +1):
        cach = bien_0 + bien_1
        bien_0 = bien_1
        bien_1 = cach
    return bien_1
n = random.randint(0, 20)
#print("Số bậc thang là: ",n)
#print(question_38_m(n))
def question_39_m(*gia):
    if not gia:
        return 0
    min_gia = float("inf")
    max_loinhuan = 0
    for i in gia:
        if i < min_gia:
            min_gia = i
        loi_nhuan = i - min_gia
        if loi_nhuan > max_loinhuan:
            max_loinhuan = loi_nhuan
    return max_loinhuan
#gia = input("Nhập vào các giá, cách nhau bởi dấu phẩy: ")
#ds = [int(num.strip()) for num in gia.split(",") if num.strip()]
#result = question_39_m(*ds)
#print("Lợi nhuận lớn nhất có thể đạt được:", result)