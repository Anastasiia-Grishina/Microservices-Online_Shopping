from bson import ObjectId
from flask.json import JSONEncoder
from datetime import datetime
from pymodm import MongoModel, queryset



# Custom encoder
class CustomJSONEncoder(JSONEncoder):
	def default(self, obj):
		try:
			if isinstance(obj, ObjectId):
				return str(obj)
			elif isinstance(obj, datetime):
				return round(obj.timestamp())
		except TypeError:
			pass

		return JSONEncoder.default(self, obj)


def pretty(obj):
	if isinstance(obj, MongoModel):
		return obj._data._python_data
	elif isinstance(obj, queryset.QuerySet):
		return list(obj.values())
	else:
		return obj