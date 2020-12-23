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
    file = models.FileField(upload_to='files/')
    title1 = models.CharField(blank=True, max_length=200)
    file1 = models.FileField(blank=True, upload_to='files/')
    title2 = models.CharField(blank=True, max_length=200)
    file2 = models.FileField(blank=True, upload_to='files/')
    title3 = models.CharField(blank=True, max_length=200)
    file3 = models.FileField(blank=True, upload_to='files/')
    title4 = models.CharField(blank=True, max_length=200)
    file4 = models.FileField(blank=True, upload_to='files/')
    title5 = models.CharField(blank=True, max_length=200)
    file5 = models.FileField(blank=True, upload_to='files/')

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