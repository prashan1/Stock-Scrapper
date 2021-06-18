from django.db import models

# Create your models here.
class StockMarket(models.Model):
    
    ceopenInterest = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    cechangeinOpenInterest  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    cetotalTradedVolume  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    ceimpliedVolatility  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    celastPrice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    cechange  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    cebidQty  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    cebidprice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    ceaskPrice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    ceaskQty  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    strikePrice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    pebidQty  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    pebidprice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    peaskPrice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    peaskQty  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    pechange  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    pelastPrice  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    peimpliedVolatility  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    petotalTradedVolume  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    pechangeinOpenInterest  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    peopenInterest  = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)

    CEtotOI = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    CEtotVoi = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    PEtotOI = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)
    PEtotVoi = models.DecimalField(max_digits=11,decimal_places=2,default=0,null=True,blank=True)



    class Meta:
        ordering = ['strikePrice']