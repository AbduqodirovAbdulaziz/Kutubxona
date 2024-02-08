from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.CharField(max_length=20, choices=[("1-kurs", "1-kurs"), ("2-kurs", "2-kurs"), ("3-kurs", "3-kurs"),
                                                    ("4-kurs", "4-kurs")])
    kitob_soni = models.IntegerField(default=1)

    def __str__(self):
        return f"Talaba: {self.ism} {self.kurs} kitoblar soni {self.kitob_soni}"


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30, choices=[("ayol", "ayol"), ("erkak", "erkak")])
    tugilgan_sana = models.DateField(blank=True, null=True)
    kitoblar_soni = models.IntegerField()
    tirik = models.CharField(max_length=20, choices=[("tirik", "tirik"), ("o'lgan", "o'lgan")])

    def __str__(self):
        return f"Muallif {self.ism} "


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=20)
    sahifa = models.IntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} janr-{self.janr}"


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=20)
    ish_vaqti = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ism} ish vaqti{self.ish_vaqti}"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.CharField(max_length=10, default=False)
    qaytarish_sana = models.DateField()

    def __str__(self):
        return f"{self.talaba} {self.kitob} {self.olingan_sana} {self.qaytarish_sana}"
