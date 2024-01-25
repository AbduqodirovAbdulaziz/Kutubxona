from django.shortcuts import render, redirect

from .models import *

def hamma_kitoblar(request):
    natija=Kitob.objects.all()
    kiritilgan_kitob = request.GET.get("nom")
    if kiritilgan_kitob is not None:
        natija = Kitob.objects.filter(nom__contains=kiritilgan_kitob)
    data={
        "books": natija
    }
    return render(request, 'kitoblar.html', data)

def hamma_talabalar(request):
    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ism")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)
    data={
        "talaba": natija
    }
    return render(request, 'talabalar.html', data)

def bitiruvchilar(request):
    data={
        "talaba": Talaba.objects.filter(kurs="4-kurs")
    }
    return render(request, 'talabalar.html', data)

def kitobiborlar(request):
    data={
        "talaba": Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request, 'talabalar.html', data)

def bitta_talaba(request,pk):
    data={
        "student": Talaba.objects.get(id=pk)
    }
    return  render(request, 'bitta_talaba.html', data)

def ismidaA(request,harf):
    data={
        "talaba": Talaba.objects.filter(ism__contains=harf)
    }
    return  render(request, 'talabalar.html', data)

def erkakMuallif(requst):
    data={
        "Muallif": Muallif.objects.filter(jins="erkak")
    }
    return render(requst, 'muallif.html', data)

def hammamuallif(requsts):
    data={
        "Muallif": Muallif.objects.all()
    }
    return render(requsts, 'muallif.html', data)

def tanlanganMuallif(requests,son):
    data={
        "muallif": Muallif.objects.get(id=son)
    }
    return render(requests, 'bitta_muallif.html', data)

def tanlanganKitob(requests,son):
    data={
        "Kitob" : Kitob.objects.get(id=son)
    }
    return render(requests, 'bitta_kitob.html', data)

def hammaRecord(requests):
    data = {
        "Record": Record.objects.all()
    }
    return render(requests,'Record.html',data)

def tirikmualliflar(requsts):
    data={
        "Muallif": Muallif.objects.filter(tirik="tirik")
    }
    return render(requsts, 'muallif.html', data)
def sahifasikatta(requests):
    data={
        "Kitob": Kitob.objects.order_by("-sahifa")[0:3]
    }
    return render(requests, 'bitta_kitob.html', data)

def kitobikop(requests):
    data = {
        "Muallif": Muallif.objects.order_by("-kitoblar_soni")[0:3]
    }
    return render(requests,"muallif.html",data)

def Recordsana(requests):
    data = {
        "Record": Record.objects.order_by("-olingan_sana")[0:3]
    }
    return render(requests,'Record.html',data)

#--------------------------------
def tirikmuallifkitoblari(requests):
    tirik_muallif = Muallif.objects.filter(tirik="tirik")
    data={
        "Kitob": Kitob.objects.filter(muallif=tirik_muallif)
    }
    return render(requests, 'kitoblar.html', data)
#--------------------------------

def badiykitob(requests):
    data={
        "Badiy": Kitob.objects.filter(janr="badiy")
    }
    return render(requests,'bitta_kitob.html',data)

def yoshikattamuallif(requsts):
    data={
        "Muallif": Muallif.objects.order_by("tugilgan_sana")[0:3]
    }
    return render(requsts, 'bitta_muallif.html', data)

def ontadankamkitob(requests):
    data={
        "Muallif": Muallif.objects.filter(kitoblar_soni__lt=10)
    }
    return render(requests, 'muallif.html',data)

def idrecordchiqar(requests,son):
    data={
        "Record": Record.objects.get(id=son)
    }
    return render(requests, 'Record.html',data)

def bitiruvchirecord(requests):
    talaba_4_kurs=Talaba.objects.filter(kurs="4-kurs")
    data={
        "Record" Record.objects.filter(talaba__in=talaba_4_kurs)
    }
    return render(requests, 'Record.html',data)















def talaba_ochir(requests,pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/hammatalaba/")

def kitob_ochir(requests,pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/hammakitob/")


