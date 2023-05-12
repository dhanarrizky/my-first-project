from django.contrib import admin

# Register your models here.
from .models import Members #import database

#register your models here

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','joined_date',) #memberika tampilan display paling atas, atau keterangan table

admin.site.register(Members,MemberAdmin) #memasukkan database kedalam halaman admin
