from tortoise import models, fields


class Second(models.Model):
    id = fields.IntField(pk=True)
    created_time = fields.DatetimeField(auto_now=True)
    name = fields.CharField(max_length=40)
    