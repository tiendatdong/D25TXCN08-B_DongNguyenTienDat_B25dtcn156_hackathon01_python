import csv
ds = []
while True:
    print("\n------------ MENU ------------")
    print("1. Hiển thị danh sách")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách")
    print("7. Thống kê điểm TB")
    print("8. Liệt kê SV cao nhất/thấp nhất")
    print("9. Phân loại học lực")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")
    if chon == "1":
        print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
            "Mã SV","Tên","Toán","Lý","Hóa","TB","Xếp loại"))
        for sv in ds:
            print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
                sv["ma_sv"], sv["ten"], sv["toan"], sv["ly"], sv["hoa"], sv["diem_tb"], sv["xep_loai"]))
    elif chon == "2":
        ma = input("Nhập mã SV: ")
        if any(sv["ma_sv"] == ma for sv in ds):
            print("Mã SV đã tồn tại!")
            continue
        ten = input("Nhập tên: ")
        toan = float(input("Điểm Toán: "))
        ly = float(input("Điểm Lý: "))
        hoa = float(input("Điểm Hóa: "))
        if not (0 <= toan <= 10 and 0 <= ly <= 10 and 0 <= hoa <= 10):
            print("Điểm phải trong khoảng 0-10")
            continue
        tb = round((toan+ly+hoa)/3,2)
        if tb < 5: loai="Yếu"
        elif tb < 7: loai="Trung Bình"
        elif tb < 8: loai="Khá"
        else: loai="Giỏi"
        ds.append({"ma_sv":ma,"ten":ten,"toan":toan,"ly":ly,"hoa":hoa,"diem_tb":tb,"xep_loai":loai})
        print("Đã thêm sinh viên.")
    elif chon == "3":
        ma = input("Nhập mã SV cần sửa: ")
        found = False
        for sv in ds:
            if sv["ma_sv"] == ma:
                toan = float(input("Điểm Toán mới: "))
                ly = float(input("Điểm Lý mới: "))
                hoa = float(input("Điểm Hóa mới: "))
                sv["toan"], sv["ly"], sv["hoa"] = toan, ly, hoa
                sv["diem_tb"] = round((toan+ly+hoa)/3,2)
                if sv["diem_tb"] < 5: sv["xep_loai"]="Yếu"
                elif sv["diem_tb"] < 7: sv["xep_loai"]="Trung Bình"
                elif sv["diem_tb"] < 8: sv["xep_loai"]="Khá"
                else: sv["xep_loai"]="Giỏi"
                print("Đã cập nhật.")
                found = True
                break
        if not found: print("Không tìm thấy SV.")
    elif chon == "4":
        ma = input("Nhập mã SV cần xóa: ")
        for sv in ds:
            if sv["ma_sv"] == ma:
                confirm = input("Bạn có chắc muốn xóa? (y/n): ")
                if confirm.lower()=="y":
                    ds.remove(sv)
                    print("Đã xóa.")
                break
        else:
            print("Không tìm thấy SV.")
    elif chon == "5":
        key = input("Nhập tên hoặc mã SV cần tìm: ")
        ket_qua = [sv for sv in ds if key.lower() in sv["ten"].lower() or sv["ma_sv"]==key]
        for sv in ket_qua:
            print(sv)
    elif chon == "6":
        print("1. Sắp xếp theo điểm TB giảm dần")
        print("2. Sắp xếp theo tên A-Z")
        c = input("Chọn: ")
        if c == "1":
            for i in range(len(ds)-1):
                for j in range(len(ds)-i-1):
                    if ds[j]["diem_tb"] < ds[j+1]["diem_tb"]:
                        ds[j], ds[j+1] = ds[j+1], ds[j]
            print("Danh sách sau khi sắp xếp theo điểm TB giảm dần:")
        elif c == "2":
            for i in range(len(ds)-1):
                for j in range(len(ds)-i-1):
                    if ds[j]["ten"].lower() > ds[j+1]["ten"].lower():
                        ds[j], ds[j+1] = ds[j+1], ds[j]
            print("Danh sách sau khi sắp xếp theo tên A-Z:")
        else:
            print("Lựa chọn không hợp lệ!")
            continue
        print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
            "Mã SV","Tên","Toán","Lý","Hóa","TB","Xếp loại"))
        for sv in ds:
            print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
                sv["ma_sv"], sv["ten"], sv["toan"], sv["ly"], sv["hoa"], sv["diem_tb"], sv["xep_loai"]))
    elif chon == "7":
        thongke={"Giỏi":0,"Khá":0,"Trung Bình":0,"Yếu":0}
        for sv in ds:
            thongke[sv["xep_loai"]] += 1
        print(thongke)
    elif chon == "8":
        if ds:
            max_sv = ds[0]
            min_sv = ds[0]
            for i in range(1, len(ds)):
                if ds[i]["diem_tb"] > max_sv["diem_tb"]:
                    max_sv = ds[i]
                if ds[i]["diem_tb"] < min_sv["diem_tb"]:
                    min_sv = ds[i]
            print("SV có điểm TB cao nhất:")
            print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
                "Mã SV","Tên","Toán","Lý","Hóa","TB","Xếp loại"))
            print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
                max_sv["ma_sv"], max_sv["ten"], max_sv["toan"], max_sv["ly"], max_sv["hoa"], max_sv["diem_tb"], max_sv["xep_loai"]))

            print("SV có điểm TB thấp nhất:")
            print("{:<10}{:<20}{:<6}{:<6}{:<6}{:<6}{:<10}".format(
                min_sv["ma_sv"], min_sv["ten"], min_sv["toan"], min_sv["ly"], min_sv["hoa"], min_sv["diem_tb"], min_sv["xep_loai"]))
    elif chon == "9":
        for sv in ds:
            print(sv["ten"], ":", sv["xep_loai"])
    elif chon == "0":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ!")
