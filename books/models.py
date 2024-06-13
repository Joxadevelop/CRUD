from django.db import models

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='nomi')
    description = models.TextField(verbose_name='category haqida')
    
    
    def __str__(self):
        return self.name



class Books(models.Model):
    STATUSES = (
        ("sotuvda", "Sotuvda",),
        ("qolmagan", "qolmagan")
    )
    
    name = models.CharField(max_length=200, verbose_name='kitob nomi')
    slug = models.TextField(verbose_name='kitob haqida')
    picture = models.ImageField(verbose_name='rasmi')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='narxi')
    quantitiy = models.IntegerField(verbose_name='qancha bor')
    status = models.CharField(max_length=50, choices=STATUSES, verbose_name='holati') 
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    
    
    def __str__(self):
        return self.name  
    
