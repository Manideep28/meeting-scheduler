import datetime

class Operations :
	def __init__(self) :
		pass

	def get_room(unavailable_rooms,max_rooms) :
		"""Returns the Available room"""

		for room in range(1,max_rooms+1) :
			if room not in unavailable_rooms :
				return room 

	def is_interval_overlap(mst,met,start_time,end_time) :
		"""Checks if the current time overlaps with other"""
		if start_time <= mst <= end_time or start_time <= met <= end_time :
			return True 
		return False 

	def get_date() :
		"""Gets Date from the user"""
		while True :
			try :
				date = input("Enter Meeting Date in dd/mm/yyyy Format :") 
				dd,mm,yyyy = map(int, date.split('/'))
				date = datetime.date(yyyy,mm,dd) 

				now = datetime.date.today() 
				date_diff = date - now
				if date_diff.days < 0 :
					print("Cannot Schedule meeting on previous days")
					raise Exception('')
				elif date_diff.days > 30 :
					print("Cannot book beyond 1 month from today")
					raise Exception('')
				return date
			except :
				print("Invalid Date ")

	def get_time(state) :
		"""Gets time from the user"""
		while True :
			try :
				print('Enter ',state , end = "")
				time = input(" time in 24 hours hh:mm Format :").format(state)
				hh,mins = map(int,time.split(':'))
				if hh < 0 or hh >= 24 or mins < 0 or mins >= 60 :
					print("Invalid Time ")
				else :	
					return hh,mins
			except :
				print("Invalid Time") 

	def is_valid_time_frame(start_time,end_time) :
		"""Checks if the duration is more than 3 hours"""
		time_difference = (end_time - start_time) / 60 
		if time_difference > 3.0 :
			print("Invalid Time Frame - Cannot book a meeting of more than 3 hrs duration.")
			return False 
		return True 

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
