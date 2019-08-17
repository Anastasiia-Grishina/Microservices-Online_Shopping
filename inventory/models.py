from pymodm import MongoModel, fields, connect
from datetime import datetime
from bson import ObjectId


connect('mongodb://db/dev')


class Item(MongoModel):
	_id = fields.ObjectIdField(primary_key=True, default=ObjectId)
	name = fields.CharField(required=True)
	category = fields.CharField(required=True)
	price = fields.FloatField(required=True)
	availability = fields.IntegerField(default=0)
	updated_on = fields.DateTimeField(required=True)
