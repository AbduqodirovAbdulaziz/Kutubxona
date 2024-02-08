from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hammakitob/', hamma_kitoblar),

    path('hammatalaba/', hamma_talabalar),
    path('talaba/<int:id>/tahrirlash/', talaba_tahrirlash),

    path('bitiruvchi/', bitiruvchilar),
    path('kitobiborlar/', kitobiborlar),
    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('ismida/<str:harf>/', ismidaA),
    path('erkakMuallif/', erkakMuallif),

    path('hammamuallif/', hammamuallif),
    path('muallif/<int:id>/tahrirlash/', muallif_tahrirlash),

    path('tanlanganmuallif/<int:son>/', tanlanganMuallif),
    path('tanlangankitob/<int:son>/', tanlanganKitob),
    path('hammarecord/', hammaRecord),
    path('tirikmualliflar/', tirikmualliflar),
    path('sahifasikatta/', sahifasikatta),
    path('kitobikop/', kitobikop),
    path('Recordsana/', Recordsana),
    path('talaba_ochir/<int:pk>/', talaba_ochir),
    path('kitob_ochir/<int:pk>/', kitob_ochir),
    path('tirikmuallifkitoblari/', tirikmuallifkitoblari),
    path('badiykitob/', badiykitob),
    path('yoshikattamuallif/', yoshikattamuallif),
    path('ontadankamkitob/', ontadankamkitob),
    path('idrecordchiqar/<int:son>/', idrecordchiqar),
    path('bitiruvchirecord/', bitiruvchirecord),

    path('recordlar/', recordlar),
    path('recordlar/<int:id>/tahrirlash/', record_edit),

    path('kutubxonachilar/', kutubxonachilar),
    path('kutubxonachi/<int:id>/tahrirlash/', kutubxonachilar_edit),
# forms bilan qo'shish
    path('kutubxonachi_add/', kutubxonachi_add),

    path('muallif_add/', muallif_add),

    path('record_add/', record_add),



]
