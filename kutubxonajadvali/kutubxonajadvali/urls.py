from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hammakitob/', hamma_kitoblar),
    path('hammatalaba/', hamma_talabalar),
    path('bitiruvchi/', bitiruvchilar),
    path('kitobiborlar/', kitobiborlar),
    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('ismida/<str:harf>/', ismidaA),
    path('erkakMuallif/', erkakMuallif),
    path('hammamuallif/', hammamuallif),
    path('tanlanganmuallif/<int:son>/', tanlanganMuallif),
    path('tanlangankitob/<int:son>/', tanlanganKitob),
    path('hammacecord', hammaRecord),
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
]
