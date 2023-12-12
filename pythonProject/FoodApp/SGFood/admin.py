from django.contrib import admin
from .models import TaiKhoan,LoaiTaiKhoan,KiemDuyet,LoaiThucAn,MonAn,Menu,HoaDon,ThongBao,ThoiDiem,ThoiGianBan
from django.utils.html import mark_safe
# Register your models here.
class TaiKhoanAdmin(admin.ModelAdmin):
    list_display = ['pk','ho_ten']
    search_fields = ['ho_ten']
    list_filter = ['id','ho_ten']
    readonly_fields = ['avatar']

    def avatar(self,TaiKhoan):
        if TaiKhoan:
            return mark_safe('<img src="/static/{url}" width="120"/> '.format(url=TaiKhoan.avatar.name)

            )

    class Media:
        css={
            'all': ('/static/css/style.css',)
        }




admin.site.register(TaiKhoan,TaiKhoanAdmin)
admin.site.register(LoaiTaiKhoan)
admin.site.register(MonAn)
admin.site.register(Menu)
admin.site.register(KiemDuyet)
admin.site.register(HoaDon)
admin.site.register(ThoiDiem)
admin.site.register(ThoiGianBan)
admin.site.register(LoaiThucAn)
admin.site.register(ThongBao)
