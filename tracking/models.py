from pymodm import MongoModel, fields, connect
from datetime import datetime, timedelta
from bson import ObjectId


connect('mongodb://db/dev')


class Delivery(MongoModel):
	_id 			= fields.ObjectIdField(primary_key=True, default=ObjectId)
	creation_date 	= fields.DateTimeField(default=datetime.now)
	delivery_date 	= fields.DateTimeField(default=lambda: datetime.now() + timedelta(days=7))
	status			= fields.CharField(default='processing')
	current_location= fields.CharField(default='Depot')
	destination		= fields.CharField(required=True)
	order_id		= fields.CharField(required=True)