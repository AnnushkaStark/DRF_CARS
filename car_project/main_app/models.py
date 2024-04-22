from django.db import models


class Country(models.Model):
    """
    Страна
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Manufacturer(models.Model):
    """
    Производитель
    """

    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    """
    Автомобиль
    """

    name = models.CharField(max_length=100, unique=True)
    year_of_release = models.DateField()
    year_of_graduation = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.year_of_release} {self.year_of_graduation} {self.manufacturer}"


class Comments(models.Model):
    """
    Комментарии
    """

    author_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    text_comment = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author_email} {self.created_at} {self.text_comment} {self.car}"
