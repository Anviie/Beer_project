from django.db import models


class Beer(models.Model):
    name = models.CharField('Название', max_length=100)
    taste = models.IntegerField(
        'Вкус',
        default=0,
        choices=[(i, f"{i} звездочек") for i in range(1, 11)])
    price = models.IntegerField(
        'Вкус',
        default=0,
        choices=[(i, f"{i} звездочек") for i in range(1, 11)])
    comment = models.TextField(
        'Накиньте пару слов об этом пивке',
        blank=True,
        null=True)
    total_rate = models.FloatField(default=0)
    image = models.ImageField('Фото', upload_to='beer_images', blank=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_rate = (self.taste + self.price) / 2
        super(Beer, self).save(*args, **kwargs)
