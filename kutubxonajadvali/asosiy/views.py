from django.shortcuts import render, redirect
from .forms import *
from datetime import datetime


def hamma_kitoblar(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get("nom"),
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id=request.POST.get("m")),
        )
    natija = Kitob.objects.all()
    kiritilgan_kitob = request.GET.get("nom")
    if kiritilgan_kitob is not None:
        natija = Kitob.objects.filter(nom__contains=kiritilgan_kitob)
    data = {
        "books": natija,
        "mualliflar": Muallif.objects.all()
    }
    return render(request, 'kitoblar.html', data)

#--------------------------------------------------------
def hamma_talabalar(request):
    if request.method == "POST":
        data = TalabaForm(request.POST)
        if data.is_valid():
            Talaba.objects.create(
                ism=data.cleaned_data['ism'],
                kurs=data.cleaned_data['kurs'],
                kitob_soni=data.cleaned_data['kitob_soni'],
            )
        # Talaba.objects.create(
        #     ism=request.POST.get("ismi"),
        #     kurs=request.POST.get("k"),
        #     kitob_soni=request.POST.get("k_s"),
        # )
        return redirect("/hammatalaba/")

    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ism")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)
    data = {
        "talaba": natija,
        "form": TalabaForm()

    }
    return render(request, 'talabalar.html', data)

#---------------------------------------------------------------
def kutubxonachi_add(request):
    if request.method=="POST":
        context=KutubxonachiForm(request.POST)
        if context.is_valid():
            Kutubxonachi.objects.create(
                ism=context.cleaned_data["ism"],
                ish_vaqti=context.cleaned_data["ish_vaqti"],
            )
        return redirect("/kutubxonachi_add/")

    context={
        "kutubxonachilar": Kutubxonachi.objects.all(),
        "form": KutubxonachiForm
    }
    return render(request,"kutubxonachilar.html",context)
#-------------------------------------------------------
def muallif_add(request):
    if request.method=="POST":
        context=MuallifForm(request.POST)
        if context.is_valid():
            Muallif.objects.create(
                ism=context.cleaned_data["ism"],
                jins=context.cleaned_data["jins"],
                tugilgan_sana=context.cleaned_data["tugilgan_sana"],
                kitoblar_soni=context.cleaned_data["kitoblar_soni"],
                tirik=context.cleaned_data["tirik"],
            )
        return redirect("/muallif_add/")



    context={
        "Muallif": Muallif.objects.all(),
        "form": MuallifForm
    }
    return render(request,"muallif.html",context)



#------------------------------------------------------
def record_add(request):
    if request.method=="POST":
        data=RecordForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("/record_add/")
    context={
        "recordlar": Record.objects.all(),
        "form": RecordForm()
    }
    return render(request,'Record.html',context)

#------------------------------------------------------

#------------------------------------------------------

def bitiruvchilar(request):
    data = {
        "talaba": Talaba.objects.filter(kurs="4-kurs")
    }
    return render(request, 'talabalar.html', data)


def kitobiborlar(request):
    data = {
        "talaba": Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request, 'talabalar.html', data)


def bitta_talaba(request, pk):
    data = {
        "student": Talaba.objects.get(id=pk)
    }
    return render(request, 'bitta_talaba.html', data)


def ismidaA(request, harf):
    data = {
        "talaba": Talaba.objects.filter(ism__contains=harf)
    }
    return render(request, 'talabalar.html', data)


def erkakMuallif(requst):
    data = {
        "Muallif": Muallif.objects.filter(jins="erkak")
    }
    return render(requst, 'muallif.html', data)


def hammamuallif(request):
    # if request.method == "POST":
    #     Muallif.objects.create(
    #         ism=request.POST.get("ismi"),
    #         jins=request.POST.get("jins"),
    #         tugilgan_sana=request.POST.get("t_sana"),
    #         kitoblar_soni=request.POST.get("k_soni"),
    #         tirik=request.POST.get("tirik"),
    #     )
    #     return redirect("/hammamuallif/")
    data = {
        "Muallif": Muallif.objects.all()

    }
    return render(request, 'muallif.html', data)


# --------------------------------------
def muallif_tahrirlash(request, id):
    if request.method == "POST":
        muallif = Muallif.objects.get(id=id)
        muallif.ism = request.POST["ism"]
        muallif.jins = request.POST["jins"]
        muallif.tugilgan_sana = request.POST["tugilgan_sana"]
        muallif.kitoblar_soni = request.POST["kitoblar_soni"]
        muallif.tirik = request.POST["tirik"] == 'on'
        muallif.save()

        return redirect('/hammamuallif/')
    contex = {
        'muallif': Muallif.objects.get(id=id)
    }
    return render(request, 'muallif_tahrirlash.html', contex)


# --------------------------------------
def tanlanganMuallif(requests, son):
    data = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(requests, 'bitta_muallif.html', data)


def tanlanganKitob(requests, son):
    data = {
        "Kitob": Kitob.objects.get(id=son)
    }
    return render(requests, 'bitta_kitob.html', data)


def hammaRecord(requests):
    if requests.method == "POST":
        Record.objects.create(
            talba=requests.POST.get("talaba"),
            kitob=requests.POST.get("kitob"),
            kutubxonachi=requests.POST.get("k_xonachi"),
            olingan_sana=requests.POST.get("o_sana"),
            qaytardi=requests.POST.get("q") == 'on',
            qaytarish_sana=requests.POST.get("q_sana"),

        )
        return redirect("/hammatalaba/")
    data = {
        "Record": Record.objects.all(),
        "talabalar": Talaba.objects.all(),
        "kitoblar": Kitob.objects.all(),
        "kutubxonachi": Kutubxonachi.objects.all()
    }
    return render(requests, 'Record.html', data)


def tirikmualliflar(requsts):
    data = {
        "Muallif": Muallif.objects.filter(tirik="tirik")
    }
    return render(requsts, 'muallif.html', data)


def sahifasikatta(requests):
    data = {
        "Kitob": Kitob.objects.order_by("-sahifa")[0:3]
    }
    return render(requests, 'bitta_kitob.html', data)


def kitobikop(requests):
    data = {
        "Muallif": Muallif.objects.order_by("-kitoblar_soni")[0:3]
    }
    return render(requests, "muallif.html", data)


def Recordsana(requests):
    data = {
        "Record": Record.objects.order_by("-olingan_sana")[0:3]
    }
    return render(requests, 'Record.html', data)


# --------------------------------
def tirikmuallifkitoblari(requests):
    tirik_muallif = Muallif.objects.filter(tirik="tirik")
    data = {
        "Kitob": Kitob.objects.filter(muallif=tirik_muallif)
    }
    return render(requests, 'kitoblar.html', data)


# --------------------------------

def badiykitob(requests):
    data = {
        "Badiy": Kitob.objects.filter(janr="badiy")
    }
    return render(requests, 'bitta_kitob.html', data)


def yoshikattamuallif(requsts):
    data = {
        "Muallif": Muallif.objects.order_by("tugilgan_sana")[0:3]
    }
    return render(requsts, 'bitta_muallif.html', data)


def ontadankamkitob(requests):
    data = {
        "Muallif": Muallif.objects.filter(kitoblar_soni__lt=10)
    }
    return render(requests, 'muallif.html', data)


def idrecordchiqar(requests, son):
    data = {
        "Record": Record.objects.get(id=son)
    }
    return render(requests, 'Record.html', data)


def bitiruvchirecord(requests):
    data = {
        "Record": Record.objects.filter(talaba__kurs="4-kurs")
    }
    return render(requests, 'Record.html', data)


def talaba_tahrirlash(request, id):
    if request.method == "POST":
        talaba = Talaba.objects.get(id=id)
        talaba.ism = request.POST["ism"]
        talaba.kurs = request.POST["kurs"]
        talaba.kitob_soni = request.POST["kitob_soni"]
        talaba.save()
        return redirect('/hammatalaba/')
    contex = {
        'talaba': Talaba.objects.get(id=id)
    }
    return render(request, 'talaba_tahrirlash.html', contex)


def recordlar(request):
    context = {
        "recordlar": Record.objects.all()
    }
    return render(request, 'Record.html', context)


def record_edit(request, id):
    if request.method == "POST":
        record = Record.objects.get(id=id),
        record.qaytardi = request.POST["qaytardi", False] == 'on',
        record.qaytarish_sana = request.POST["q_sanasi"],
        record.save()

        return redirect("/recordlar/")
    context = {
        "record": Record.objects.get(id=id)
    }
    return render(request, 'Record_edit.html', context)


def kutubxonachilar(request):
    context={
        "kutubxonachilar": Kutubxonachi.objects.all()
    }
    return render(request,'kutubxonachilar.html',context)

def kutubxonachilar_edit(request,id):
    if request.method =="POST":
        kutubxonachi=Kutubxonachi.objects.get(id=id)
        kutubxonachi.ism=request.POST['ism']
        kutubxonachi.ish_vaqti=request.POST['ish_vaqti']
        kutubxonachi.save()
        return redirect("/kutubxonachilar/")
    context={
        "kutubxonachi" : Kutubxonachi.objects.get(id=id)
    }
    return render(request,'kutubxonachi_edit.html',context)












def talaba_ochir(requests, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/hammatalaba/")


def kitob_ochir(requests, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/hammakitob/")
