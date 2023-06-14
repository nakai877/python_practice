from django.contrib import admin
from .models import StaffInformation, Staff, Department ,Book # 追加

admin.site.register(StaffInformation)
admin.site.register(Staff) # 追加
admin.site.register(Department)
admin.site.register(Book)