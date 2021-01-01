from django.db import models
from datetime import datetime
import uuid
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField

# Create your models here.
class Novinky(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=1600, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'novinky'
    

class Oznamy(models.Model):
    body = RichTextField()
    date = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = 'oznamy'

    def __str__(self):
        return str(self.date)

class UradnaTabula(models.Model):
    date = models.DateField(default=datetime.now)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/uradna')
    title1 = models.CharField(blank=True, max_length=200)
    file1 = models.FileField(blank=True, upload_to='files/uradna')
    title2 = models.CharField(blank=True, max_length=200)
    file2 = models.FileField(blank=True, upload_to='files/uradna')
    title3 = models.CharField(blank=True, max_length=200)
    file3 = models.FileField(blank=True, upload_to='files/uradna')
    title4 = models.CharField(blank=True, max_length=200)
    file4 = models.FileField(blank=True, upload_to='files/uradna')
    title5 = models.CharField(blank=True, max_length=200)
    file5 = models.FileField(blank=True, upload_to='files/uradna')

    class Meta:
        verbose_name_plural = 'Uradna Tabula'
    
    def __str__(self):
        return str(self.date)

class Odpad(models.Model):

    PO = 'Pondelok'
    UT = 'Utorok'
    STR = 'Streda'
    STV = 'Stvrtok'
    PIA = 'Piatok'
    SO = 'Sobota'
    NE = 'Nedela'

    WEEK_DAY = [
        ('Podnelok', PO),
        ('Utorok', UT),
        ('Streda', STR),
        ('Štvrtok', STV),
        ('Piatok', PIA),
        ('Sobota', SO),
        ('Nedeľa', NE),
    ]

    JAN = 'Januar'
    FEB = 'Februar'
    MAR = 'Marec'
    APR = 'April'
    MAY = 'Maj'
    JUN = 'Jun'
    JUL = 'Jul'
    AUG = 'August'
    SEPT = 'September'
    OKT = 'Oktober'
    NOV = 'November'
    DEC = 'December'

    MONTH = [
        ('JAN', JAN),
        ('FEB', FEB),
        ('MAR', MAR),
        ('APR', APR),
        ('MÁJ', MAY),
        ('JÚN', JUN),
        ('JÚL', JUL),
        ('AUG', AUG),
        ('SEP', SEPT),
        ('OKT', OKT),
        ('NOV', NOV),
        ('DEC', DEC),
    ]

    KO = 'Komunalny'
    PET = 'Plasty'
    SKL = 'Sklo'
    PAP = 'Papier'
    ELK = 'Elektro'
    NO = 'Nebezpecny'

    DESCRIPTION = [
        ('Komunálny odpad', KO),
        ('Zmiešané plasty, PET fľaše', PET),
        ('Sklo', SKL),
        ('Papier', PAP),
        ('Elektro, VKM, Kovové obaly', ELK),
        ('Nebezpečný odpad', NO),
    ]

    day = models.IntegerField()
    month = models.CharField(max_length=200, choices=MONTH, default='')
    description = models.CharField(max_length=250, choices=DESCRIPTION, default='')
    week_day = models.CharField(max_length=160, choices=WEEK_DAY, default='')
    color = ColorField(default='#FF0000', blank=True)

    class Meta:
        verbose_name_plural = 'Odpady'
    
    def __str__(self):
        return str(self.day)

class Aktuality(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=350)
    date = models.DateField(auto_now=True)
    body = RichTextField()

    class Meta:
        verbose_name_plural = 'aktuality'
    
    def __str__(self):
        return self.title

class Vzn(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/vzn/')
    
    class Meta:
        verbose_name_plural = 'vzn'
    
    def __str__(self):
        return self.title

class FakturyRok(models.Model):
    rok = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Faktury rok'

    def __str__(self):
        return self.rok

class FakturyFiles(models.Model):
    rok = models.ForeignKey(FakturyRok, on_delete=models.CASCADE, related_name='faktury')
    title = models.CharField(max_length=160)
    faktura = models.FileField(upload_to='files/faktury')

    class Meta:
        verbose_name_plural = 'Faktury subory'

    def __str__(self):
        return '%s %s' % (self.title, self.rok)

class ZapisniceObdobie(models.Model):
    obdobie = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Zapisnice obdobie'

    def __str__(self):
        return self.obdobie

class ZapisniceFiles(models.Model):
    obdobie = models.ForeignKey(ZapisniceObdobie, on_delete=models.CASCADE, related_name='zapisnice')
    date = models.DateField(default=datetime.now)
    zapisnica = models.FileField(upload_to='files/zapisnice', blank=True)
    uznesenie = models.FileField(upload_to='files/uznesenia', blank=True)

    class Meta:
        verbose_name_plural = 'Zapisnice subory'
        ordering = ['-date']

    def __str__(self):
        return str(self.date)

class ZmluvyRok(models.Model):
    rok = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Zmluvy rok'

    def __str__(self):
        return self.rok

class ZmluvyFiles(models.Model):
    rok = models.ForeignKey(ZmluvyRok, on_delete=models.CASCADE, related_name='zmluvy')
    cislo = models.CharField(max_length=60, blank=True)
    zmluvne_strany = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=160)  
    zmluva = models.FileField(upload_to='files/zmluvy')

    class Meta:
        verbose_name_plural = 'Zmluvy subory'

    def __str__(self):
        return self.cislo