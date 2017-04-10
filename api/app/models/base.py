import peewee
import datetime
import os

# variable database linked to DATABASE imported from config file

DATABASE = {
	'host': '54.183.156.10',
	'user': 'airbnb_user_dev',
	'database': 'airbnb_dev',
	'port': 3306,
	'charset': 'utf8',
	'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')
}

database = peewee.MySQLDatabase(database=DATABASE["database"], host=DATABASE["host"], user=DATABASE["user"], port=DATABASE["port"], passwd=DATABASE["password"], charset=DATABASE["charset"])

class BaseModel(peewee.Model):
	id = peewee.PrimaryKeyField(unique=True)
	created_at = peewee.DateTimeField(default=datetime.datetime.now(),formats="%d/%m/%Y %H:%M:%S")
	updated_at = peewee.DateTimeField(default=datetime.datetime.now(),formats="%d/%m/%Y %H:%M:%S")

	# overloads save method of Model to update updated_at before saving
	def save(self, *args, **kwargs):
		self.updated_at = datetime.datetime.now()
		super(BaseModel, self).save(*args, **kwargs)

	class Meta:
		# connects to database
		database = database
		order_by = ("id", )