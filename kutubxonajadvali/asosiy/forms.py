from django import forms
from .models import *


class TalabaForm(forms.Form):
    ism = forms.CharField(label='Ism')
    kurs = forms.CharField(label='Kurs')
    kitob_soni = forms.IntegerField(label='Kitoblar soni', min_value=1, max_value=1000)


class KutubxonachiForm(forms.Form):
    ism = forms.CharField(max_length=30, label="Ism:")
    ish_vaqti = forms.CharField(label="Ish vaqti:")


class MuallifForm(forms.Form):
    ism = forms.CharField(max_length=30, label="Ism: ")
    jins = forms.CharField(max_length=10, label="Jins(erkak,ayol)")
    tugilgan_sana = forms.DateField()
    kitoblar_soni = forms.IntegerField(min_value=1)
    tirik = forms.CharField(max_length=10, label="tirik/o'lgan")

#-------xato variyanti----------
# class RecordForm(forms.Form):
#     talaba = forms.CharField(max_length=30, label="Talaba: ")
#     kitob = forms.CharField(max_length=30, label="Kitob")
#     kutubxonachi = forms.CharField(max_length=30, label="Kutubxonachi")
#     olingan_sana = forms.DateField()
#     qaytardi = forms.CharField(label="qaytardi/qaytarmadi")
#     qaytarish_sana = forms.DateField()
#--------------------------

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
