from django.db import models


class Browsers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'browsers'


class PC(models.Model):
    id = models.IntegerField(primary_key=True)
    memory = models.IntegerField()
    brand = models.CharField(max_length=20)
    browser_id = models.ForeignKey(Browsers, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pc'