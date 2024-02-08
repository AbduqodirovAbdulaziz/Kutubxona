from django.contrib import admin

from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ["id","ism","kurs","kitob_soni"]
    list_display_links = ["id","ism"]
    list_editable = ["kurs","kitob_soni"]
    list_filter = ["kurs"]
    search_fields = ["ism","id"]
    search_help_text = "Id va ism bo'yicha qidiring"
    list_per_page = 5

# class MuallifAdmin(admin.ModelAdmin):
    # list_display = ["ism","jins","tugilgan_sana","kitoblar_soni","tirik"]
    # list_display_links = ["ism"]
    # list_editable = ["kitoblar_soni"]
    # search_fields = ["ism","id","tugilgan_sana"]
    # search_help_text = "Ism id va tug'ilgan yil bo'yicha qidiring"
    # list_filter = ["tirik"]
    # date_hierarchy = "tugilgan_sana"

class KitobAdmin(admin.ModelAdmin):
    list_display = ["id","nom","janr","sahifa","muallif"]
    list_display_links = ["nom"]
    list_editable = ["sahifa"]
    search_fields = ["nom","id","muallif__ism"]
    search_help_text = "Nom Id va Muallifning Ismi orqali"
    list_filter = ["janr","muallif"]
    autocomplete_fields = ["muallif"]

class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["ism","ish_vaqti"]
    list_filter = ["ish_vaqti"]
    search_fields = ["ism"]
    search_help_text = "Ismi bo'yicha qidirish"

class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id","ism", "jins", "tugilgan_sana", "kitoblar_soni", "tirik"]
    list_display_links = ["ism","id"]
    list_editable = ["kitoblar_soni","tirik"]
    search_fields = ["ism"]
    search_help_text = "Ism bo'yicha qidiring"
    list_filter = ["tirik"]

class RecordAdmin(admin.ModelAdmin):
    list_display = ["talaba","kitob","kutubxonachi","olingan_sana","qaytardi","qaytarish_sana"]
    search_fields = ["talaba","kitob"]
    search_help_text = "Talaba va kitob ma'lumotlarini kiritish orqali qidiring"
    autocomplete_fields = ["talaba","kitob","kutubxonachi"]


admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Muallif,MuallifAdmin)
admin.site.register(Kitob,KitobAdmin)
admin.site.register(Kutubxonachi,KutubxonachiAdmin)
admin.site.register(Record,RecordAdmin)
