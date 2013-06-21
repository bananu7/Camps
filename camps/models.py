from django.db import models
from datetime import datetime

class Camp(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField('date added', default=datetime.now, blank=True)
    date_expiry = models.DateField('date of effective expiration')
    description = models.TextField()
    rooms_count = models.IntegerField()
    link = models.URLField(max_length=200)
    price = models.IntegerField()
    address = models.CharField(max_length=100)

    CategoryChoices = (
        (0, 'Mieszkanie'),
        (1, 'M. 2-poziomowe'),
        (2, 'Dom'),
    )
    category = models.IntegerField(default=0, choices=CategoryChoices)

    def __unicode__(self):
        return self.name

