from django.db import models

# Create your models here.
class Point(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25)
    box_budget = models.FloatField()

    class Meta: 
        verbose_name = 'Point'
        verbose_name_plural = 'Points'

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length=250)
    amount = models.IntegerField()
    price = models.FloatField()


    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Distributor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25)
    address=models.CharField(max_length=50)
    nit = models.CharField(max_length= 15)
    description = models.TextField(max_length=250)
    phone=models.CharField(max_length=13)

    Item=models.ManyToManyField(Item)

    class Meta:
        verbose_name = 'Distributor'
        verbose_name_plural = 'Distributors'

    def __str__(self):
        return self.name


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    type_invoice = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.TextField(max_length=250)
    cost = models.FloatField()
    iva = models.FloatField()

    point=models.ForeignKey(Point, null=True, blank=True, on_delete=models.CASCADE)
    distributor=models.ForeignKey(Distributor, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __srt__(self):
        return self.id


class Detail_invoice(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()

    
    invoice=models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Detail_invoice'
        verbose_name_plural = 'Details_invoice'

    def __str__(self):
        return self.id + self.invoice


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 16)
    cc = models.CharField(max_length= 15)
    first_name=models.CharField(max_length = 15)
    last_name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)

    
    point=models.OneToOneField(Point, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name


