#This is a program that will perform the CRUD operations into a table of a database of an imaginary enterprise

import pymysql #Import the package pymysql to conect with the database example created before

import random #Import the package random to generate a random number on a field of a table of the database

from os import system #Import the package system to clean the shell

from conect import Conect #Import the class created before to conect to the database

from prettytable import PrettyTable #Import the package prettytable to see the queries as MySQL's tables

class Menu(Conect):

	def search_employee(self, employeeNumber):
		db, dbc = self.conect()

		query = "SELECT * FROM employees WHERE employeeNumber = %s"

		dbc.execute(query, (employeeNumber))
		result = dbc.fetchone() #Fetch the first result that agrees with the query

		return result

		db.close()

	
	def search_office(self, officeCode):
		db, dbc = self.conect()

		query = "SELECT * FROM offices WHERE officeCode = %s"

		dbc.execute(query, (officeCode))
		result = dbc.fetchone()

		return result

		db.close()


	def insert(self):
		print("\n")
		db, dbc = self.conect() #Connect with the database
		#This variable saves a simple SQL query
		query = 'INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
		
		#A "while True" loop to be sure that the data is correctly entered (at least the most)
		while True:
			try:
				employeeNumber = random.randint(1000, 1999) #Generate a random number for the employee's ID
				
				lastName = str(input("Type the employee's last name: "))
				
				print("\n")
				firstName = str(input("Type the employee's name: "))
				
				ex_number = random.randint(1000, 1999)
				extension = "x" + str(number) #Converting a integer into an string
				
				print("\n")
				email = str(input("Type the employee's email: "))
				#Using the split function to change the employee email for the enterprise's email
				username = email.split('@')[0]
				email = username + "@classicmodelcars.com"
				
				print("\n")
				print("Which office will the employee belong?")
				print("1 - San Fransisco")
				print("2 - Boston")
				print("3 - New York")
				print("4 - Paris")
				print("5 - Tokyo")
				print("6 - Sydney")
				print("7 - London")
				try:
					print("\n")
					option = int(input("Type your option: "))

					result = self.search_office(option)

					if result != None:
						officeCode = option

					else:
						print("\n")
						print("The office you're searching for doesn't exist")
						break
				except:
					print("\n")
					print("Error....")
					break
				
				print("\n")
				print("The employee will report to")
				print("1 - President")
				print("2 - VP Sales")
				print("3 - VP Marketing")
				print("4 - Sales Manager (APAC)")
				print("5 - Sales Manager (EMEA)")
				print("6 - Sales Manager (NA)")
				print("\n")
				option = int(input("Type your option: "))
				if option == 1:
					reportsTo = 1002

				elif option == 2:
					reportsTo = 1056

				elif option == 3:
					reportsTo = 1076

				elif option == 4:
					reportsTo = 1088

				elif option == 5:
					reportsTo = 1102

				elif option == 6:
					reportsTo = 1143

				else:
					print("\n")
					print("The typed value is invalid >:|")
					break
				
				print("\n")
				jobTitle = str(input("Type the employee's title: "))

				#Executes the query made early with the data that has been already defined
				dbc.execute(query, (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle))

				#commit method to save changes
				db.commit()
				print("\n")
				print("The data was entered successfully")
				break
			
			except:
				print("\n")
				print("There is inconsistency in the data")
				break

		#It's important to close the connection with the database after perform a query
		db.close()
		input() #To reload the menu tapping Enter

	
	def query(self):
		db, dbc = self.conect()

		query = 'SELECT * FROM employees WHERE employeeNumber = %s'

		try:
			print("\n")
			table = PrettyTable(["employeeNumber","lastName","firstName","extension","email","officeCode","reportsTo","jobTitle"]) #This variable saves the rows of the table
			employeeNumber = input("Type the employee's number you want to visualize: ")
			dbc.execute(query, (employeeNumber))
			result = dbc.fetchall() #Fetch all the results that agrees with the query

			if result != ():
				for i in result:
					table.add_row([i['employeeNumber'], i['lastName'], i['firstName'], i['extension'], i['email'], i['officeCode'], i['reportsTo'], i['jobTitle']])
				print(table) #Print the table and the data in it
			
			else:
				print("\n")
				print("The employee you're searching for doesn't exist :c")
		except:
			print("\n")
			print("Error....")
		
		db.close()
		input()


	def update(self):
		print("\n")
		db, dbc = self.conect()

		query1 = "UPDATE employees SET officeCode = %s WHERE employeeNumber = %s"
		query2 = "UPDATE employees SET reportsTo = %s WHERE employeeNumber = %s"
		query3 = "UPDATE employees SET jobTitle = %s WHERE employeeNumber = %s"

		while True:
			try:
				employeeNumber = input("Type the number of the employee you want to update: ")
				result = self.search_employee(employeeNumber)
				if result != None:
					print("\n")
					print("¿Which field would you like to update?")
					print("1 - Office code")
					print("2 - Reports to")
					print("3 - Job title")
					print("\n")
					option = int(input("Type your option: "))
					
					if option == 1:
						print("\n")
						print("Which office will the employee belong?")
						print("1 - San Fransisco")
						print("2 - Boston")
						print("3 - New York")
						print("4 - Paris")
						print("5 - Tokyo")
						print("6 - Sydney")
						print("7 - London")
						try:
							print("\n")
							value = int(input("Type your option: "))

							result = self.search_office(value)

							if result != None:
								dbc.execute(query1, (value, employeeNumber))
								db.commit()
								print("\n")
								print("The field was updated successfully")
								break

							else:
								print("\n")
								print("The office you're searching for doesn't exist")
								break
						except:
							print("\n")
							print("Error....")
							break

					elif option == 2:
						try:
							print("\n")
							value = int(input("Type the new field's value: "))
							result = self.search_employee(value)
							
							if result != None:
								dbc.execute(query2, (value, employeeNumber))
								db.commit()
								print("\n")
								print("The field was updated successfully")
								break

							else:
								print("\n")
								print("The employee you're searching for doesn't exist")
								break
						except:
							print("\n")
							print("Error...")
							break

					elif option == 3:
						value = str(input("Type the new field's value: "))
						dbc.execute(query3, (value, employeeNumber))
						db.commit()
						print("\n")
						print("The field was updated successfully")
						break

					else:
						print("\n")
						print("The entered value is wrong >:|")
						break

				else:
					print("\n")
					print("The employee you're searching for doesn't exist :(")
					break

			except:
				print("\n")
				print("Error...")
				break

		db.close()
		input()


	def delete(self):
		db, dbc = self.conect()

		query = 'DELETE FROM employees WHERE employeeNumber = %s'

		try:
			print("\n")
			employeeNumber = int(input("Type the employees number you want to delete: "))

			result = self.search_employee(employeeNumber)

			if result != None:
				dbc.execute(query, (employeeNumber))
				db.commit()
				print("\n")
				print("The record was deleted successfully :)")

			else:
				print("\n")
				print("The employee you're searching for doesn't exist :c")
		except:
			print("\n")
			print("Error....")
		
		db.close()
		input()

	
	def show_table(self):
		print("\n")
		db, dbc = self.conect()

		try:
			table = PrettyTable(["employeeNumber","lastName","firstName","extension","email","officeCode","reportsTo","jobTitle"])
			dbc.execute("SELECT * FROM employees")
			result = dbc.fetchall()

			for i in result:
				table.add_row([i['employeeNumber'], i['lastName'], i['firstName'], i['extension'], i['email'], i['officeCode'], i['reportsTo'], i['jobTitle']])
			print(table)
		except:
			print("Error....")
		
		db.close()
		input()
			
	
	def main_menu(self):
		system("cls")
		print ("***********************************")
		print ("***********************************")
		print ("******                      *******")
		print ("******   CRUD  OPERATIONS   *******")
		print ("******                      *******")
		print ("***********************************")
		print ("***********************************")
		print ("***********************************")
		print ("             MAIN MENU             ")
		print ("***********************************")
		print ("***********************************")
		print ("1= Create")
		print ("2= Read")
		print ("3= Update")
		print ("4= Delete")
		print ("5= List")
		print ("6= Exit")
		print ("***********************************")
		print ("***********************************")

	
	def menu(self):
		#print("\n")
		while True:
			self.main_menu()
			try:
				print("\n")
				op = int(input("Type an option: "))

				if op == 1:
					self.insert()

				elif op == 2:
					self.query()

				elif op == 3:
					self.update()

				elif op == 4:
					self.delete()

				elif op == 5:
					self.show_table()
				
				elif op == 6:
					break

				else:
					print("\n")
					print("INVALID OPTION")

			except ValueError:
				print("\n")
				print("THE ENTERED VALUE MUST BE AN INTEGER NUMBER")
				input()


if __name__ == '__main__':
	d = Menu()
	d.menu()