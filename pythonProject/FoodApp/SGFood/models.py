from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


# Create your models here.
class TaiKhoan(models.Model):
    ho_ten=models.CharField(max_length=50,null=False)
    username=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    ngay_sinh=models.DateTimeField(auto_now_add=True)
    gioi_tinh=models.BooleanField(default=False)
    email=models.EmailField(max_length=254,null=False)
    sdt=models.CharField(max_length=50,null=False)
    avatar=models.ImageField(upload_to='sgfood/%y/%m/%d',null=True,blank=True)
    dia_chi=models.CharField(max_length=50,null=False)
    kinh_do=models.FloatField(null=False)
    vi_do=models.FloatField(null=False)
    id_loai_tai_khoan=models.ForeignKey('LoaiTaiKhoan',on_delete=models.CASCADE)
    id_kiem_duyet=models.ForeignKey('KiemDuyet',on_delete=models.CASCADE)


    def __str__(self):
        return self.ho_ten


class LoaiTaiKhoan(models.Model):
    ten_loai_tai_khoan=models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.ten_loai_tai_khoan


class KiemDuyet(models.Model):
    ten_loai_kiem_duyet=models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.ten_loai_kiem_duyet


class ThongBao(models.Model):
    noi_dung=models.CharField(max_length=50,null=False)
    id_nguoi_dung=models.ForeignKey('TaiKhoan',on_delete=models.CASCADE)

    def __str__(self):
        return self.noi_dung


class Follow(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan',on_delete=models.CASCADE,related_name='nguoi_dung_follow')
    id_cua_hang=models.ForeignKey('TaiKhoan',on_delete=models.CASCADE,related_name='cua_hang_follow')

    def __str__(self):
        return self.id_nguoi_dung


class TimKiem(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan', on_delete=models.CASCADE)
    ten_mon_an=models.CharField(max_length=50,null=True,default=' ')
    gia=models.IntegerField(null=True,default=' ')
    ten_loai_thuc_an=models.CharField(max_length=50,null=True,default=' ')
    ten_cua_hang=models.CharField(max_length=50,null=True,default=' ')

    def __str__(self):
        return self.id_nguoi_dung


class BinhLuan(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan', on_delete=models.CASCADE)
    # id_mon_an=models.ForeignKey('MonAn',on_delete=models.CASCADE)
    id_binh_luan_cha=models.ForeignKey('BinhLuan',on_delete=models.CASCADE)

    def __str__(self):
        return self.id_nguoi_dung


class DanhGia(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan', on_delete=models.CASCADE,related_name='danh_gia_cua_nguoi_dung')
    # id_mon_an=models.ForeignKey('MonAn',on_delete=models.CASCADE)
    diem=models.IntegerField(null=False)
    id_cua_hang=models.ForeignKey('TaiKhoan',on_delete=models.CASCADE,related_name='cua_hang_duoc_danh_gia')

    def __str__(self):
        return self.id_nguoi_dung


class MonAn(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan', on_delete=models.CASCADE)
    ten_mon_an=models.CharField(max_length=50,null=True)
    gia=models.IntegerField(null=True)
    id_loai_thuc_an=models.ForeignKey('LoaiThucAn',on_delete=models.CASCADE)
    trai_thai=models.BooleanField(default=False)
    hinh_anh=models.ImageField(upload_to='monan/%Y/%m/%d')
    id_don_hang=models.ForeignKey('HoaDon',on_delete=models.CASCADE)
    id_gio_hang=models.ForeignKey('GioHang',on_delete=models.CASCADE)
    so_luong=models.IntegerField(null=False)

    def __str__(self):
        return self.ten_mon_an


class Menu(models.Model):
    id_nguoi_dung=models.ForeignKey('TaiKhoan', on_delete=models.CASCADE)
    ngay_tao=models.DateTimeField(auto_now_add=True)
    danh_sach_mon_an=models.ManyToManyField(MonAn,through='ChiTietMenu')

    def __str__(self):
        return self.id_nguoi_dung


class ChiTietMenu(models.Model):
    id_mon_an=models.ForeignKey('MonAn',on_delete=models.CASCADE)
    id_menu=models.ForeignKey('Menu',on_delete=models.CASCADE)
    so_luong=models.IntegerField(null=False)

    def __str__(self):
        return self.id_menu

class LoaiThucAn(models.Model):
    ten_loai_thuc_an=models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.ten_loai_thuc_an


class ThoiDiem(models.Model):
    thoi_gian=models.CharField(max_length=50,null=False)
    mon_an=models.ManyToManyField(MonAn,through='ThoiGianBan')

    def __str__(self):
        return self.thoi_gian


class ThoiGianBan(models.Model):
    id_mon_an=models.ForeignKey('MonAn',on_delete=models.CASCADE)
    id_thoi_diem=models.ForeignKey('ThoiDiem',on_delete=models.CASCADE)

    def __str__(self):
        return self.id_mon_an


class HoaDon(models.Model):
    ngayTao=models.DateTimeField(auto_now_add=True)
    id_nguoi_dung=models.ForeignKey('TaiKhoan',on_delete=models.CASCADE)
    mon_an=models.ManyToManyField(MonAn,through='ChiTietHoaDon')

    def __str__(self):
        return self.id_nguoi_dung


class ChiTietHoaDon(models.Model):
    id_mon_an=models.ForeignKey('MonAn',on_delete=models.CASCADE)
    id_hoa_don=models.ForeignKey('HoaDon',on_delete=models.CASCADE)
    so_luong=models.IntegerField(null=False)
    don_gia=models.IntegerField(null=False)

    def __str__(self):
        return self.id_hoa_don


class GioHang(models.Model):
    so_luong_san_pham=models.IntegerField(null=False)

    def __str__(self):
        return self.so_luong_san_pham

