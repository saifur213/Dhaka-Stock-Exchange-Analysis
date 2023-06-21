from django.db import models

# Create your models here.
class company_details(models.Model):
    ID = models.IntegerField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    TradingCode = models.CharField(max_length=50)
    ScripCode = models.CharField(max_length=5)
    Sector = models.CharField(max_length=100)

    def __str__(self):
        return self.CompanyName

class company_other_info(models.Model):
    ID = models.IntegerField()
    TradingCode = models.CharField(max_length=50)
    Date = models.CharField(max_length=30)
    SponsorDirector = models.FloatField()
    Govt = models.FloatField()
    Institute = models.FloatField()
    ForeignNum = models.FloatField()
    Public = models.FloatField()