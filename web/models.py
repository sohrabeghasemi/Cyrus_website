from django.db import models

# Create your models here.


class personel(models.Model):

	MADRAK_CHOICES = {
		'ci': 'سیکل',
		'dp': 'دیپلم',
		'fd': 'فوق دیپلم',
		'li': 'لیسانس',
		'fl': 'فوق لیسانس',
		'dr': 'دکترا',
	}

	F_name = models.CharField(max_length=200)
	L_name = models.CharField(max_length=250)


