from django.db import models

# Create your models here.
class category(models.Model):
    age=(
        ('kids','kids'),
        ('adults','adults'),
    )
    cat_id=models.CharField(max_length=10, primary_key=True)
    cat_name=models.CharField(max_length=20)
    agegroup=models.CharField(max_length=7, choices=age)
    special_off=models.CharField(max_length=50)
    def __str__(self):
        return self.cat_id
    

class flipkart(models.Model):
    fid=models.CharField(max_length=10,primary_key=True)
    pname=models.CharField(max_length=25)
    price=models.CharField(max_length=10)
    discount=models.CharField(max_length=10)
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.fid
    

class myntra(models.Model):
    mid=models.CharField(max_length=10,primary_key=True)
    pname=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    discount=models.CharField(max_length=10)
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.mid
    

class customer(models.Model):
    cid=models.CharField(max_length=10,primary_key=True)
    cname=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    address=models.TextField()
    fid=models.ForeignKey(flipkart, on_delete=models.CASCADE)
    mid=models.ForeignKey(myntra, on_delete=models.CASCADE)
    def __str__(self):
        return self.cid
    
