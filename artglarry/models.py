from django.db import models


class register(models.Model):

    username=models.CharField(max_length=15)
    email=models.CharField(max_length=15)
    password=models.IntegerField()

    def __str__(self):
        return self.username

class artist_register(models.Model):
    
    artist_username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.CharField(max_length=20)

    def __str__(self):
        return self.artist_username

class art(models.Model):

    artist_name=models.ForeignKey(artist_register,on_delete=models.CASCADE)
    art=models.ImageField(upload_to='img/')
    art_name=models.CharField(max_length=20)
    date=models.DateField()
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.art_name+' BY '+self.artist_name.artist_username

class user_bid(models.Model):
    
    user_name=models.ForeignKey(register,on_delete=models.CASCADE)
    artist_art=models.ForeignKey(art,on_delete=models.CASCADE)
    bid_price=models.IntegerField()

    def __str__(self):
        return self.user_name.username

class sold(models.Model):

    buyer=models.ForeignKey(register,on_delete=models.DO_NOTHING)
    art=models.ForeignKey(art,on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=15,null=True)
    city=models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.buyer.username

class contact(models.Model):

    name=models.CharField(max_length=15)
    mobile=models.IntegerField()
    massege=models.CharField(max_length=200)

    def __str__(self):
        return self.name