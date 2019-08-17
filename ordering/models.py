from pymongo.write_concern import WriteConcern
from bson import ObjectId
from pymodm import MongoModel, fields, connect

# # Connect to MongoDB and call the connection "my-app".
connect("mongodb://db/dev")


class Order(MongoModel):
	_id 			= fields.ObjectIdField(primary_key=True, default=ObjectId)
	name 			= fields.CharField()
	items 			= fields.ListField(field = fields.CharField())
	bill 			= fields.FloatField()
	creation_date 	= fields.DateTimeField()
	destination		= fields.CharField()
	delivery_id 	= fields.CharField()