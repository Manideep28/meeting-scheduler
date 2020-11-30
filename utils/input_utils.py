class inputUtils :
	def __init__(self) :
		pass 

	def get_employee() :
		while True :
			try :
				employee_id = int(input("Enter Employee ID :")) 
				return employee_id
			except Exception as e:
				print("Invalid Employee ID")

	def get_option() :
		while True :
			try :
				option = int(input("Enter your input :")) 
				return option
			except :
				print("Choose a valid option ")

	