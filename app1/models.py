
from django.db import models

# Create your models here.


class Books_Category(models.Model):
    names=models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.names
    

class Author(models.Model):
    name=models.CharField(max_length=128)
    surname=models.CharField(max_length=128)
    year=models.IntegerField()


    def __str__(self) -> str:
        return self.name

# Asosiy Table Books
class Books(models.Model):
    category=models.ForeignKey(Books_Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    name=models.CharField(max_length=128)
    description=models.CharField(max_length=128)
    price=models.IntegerField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='rasm/',blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.category.names}  {self.author.name}  {self.name}"
    

class Review(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    comment=models.CharField(max_length=128)
    star_given=models.IntegerField()
    user=models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.book.name}  {self.comment} "


