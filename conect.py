#Import the package pymysql to conect with the database classicmodels created before
import pymysql

#Create the class Conect
class Conect(object):
	#Create the function conect
	def conect(self):
		_db_host = 'localhost'
		_db_user = 'root'
		_db_password = '12345'
		_db_name = 'classicmodels'
		try:
			_connection = pymysql.connect(host = _db_host, user = _db_user, password = _db_password, db = _db_name, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

			return _connection, _connection.cursor()
		except pymysql.InternalError as error:
			code, message = error.args
			print("ERROR: ", code, message)