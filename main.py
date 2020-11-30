import datetime 
from collections import defaultdict

from utils.hash import Generate_Hash 

from utils.datetime_utils import datetimeUtils
from utils.input_utils import inputUtils 
from utils.operations_utils import operationsUtils 

print('*********Welcome to FlyFin Meetings********** ')

while True :
	try :
		max_rooms = int(input("Enter total number of meeting rooms :")) 
		if max_rooms <= 0 :
			raise Exception("")
		else :
			break
	except :
		print("Invalid number of meeting rooms")

while True :
	try :
		total_employees = int(input("Enter total number of employees :"))	
		if total_employees <= 0 :
			raise Exception("")
		else :
			break
	except :
		print("Invalid number of Employees")

print("Success! Meeting room(s) has/have been created") 

#dictionary (map) to store intervals with roomid 
#key = datetime and value = intevals with roomid 
date_intervals = defaultdict(list)
#meetings has empid as key ,meetingid as inner dict (map) key, value as interval with date_time
meetings = defaultdict(lambda : defaultdict(list)) 


def insert( employee_id, newInterval, date_time) : 
		"""Inserts a new interval and assigns room id"""
		intervals = date_intervals[date_time] 
		unavailable_rooms = set() 
		not_overlapped = False 
		stack = [] 

		i = 0 

		#check the overlapping intervals with the newInterval 
		new_room_id = 1 
		while i < len(intervals) : 
			start,end,room_id = intervals[i] 
			
			if newInterval[0] < end : 
				if newInterval[1] < start : 
					not_overlapped = True 
					break 
				unavailable_rooms.add(room_id) 

			i += 1 

		#Assign room available at this interval 
		if not_overlapped and len(unavailable_rooms) == 0:
			new_room_id = 1 
		elif len(unavailable_rooms) == max_rooms :
			print("No Rooms available at this Time Slot ") 
			return False
		else :
			new_room_id = operationsUtils.get_room(unavailable_rooms,max_rooms)

		newInterval[2] = new_room_id	
		stack += intervals[:i]
		stack += newInterval,
		stack += intervals[i:]
		
		date_intervals[date_time] = stack 

		#generate new meeting id 
		meeting_id = Generate_Hash.generate_id(employee_id) 

		interval_date = newInterval + [date_time]
		print()

		#store the meetings of all employees with there intervals in meetings dictionary
		meetings[employee_id][meeting_id].append(interval_date)

		

		print('You have succesfully scheduled a meeting.\nDetails :') 
		print('Room ID :', new_room_id) 
		print('meeting ID :', meeting_id) 
		
		return True 



def book(employee_id,date_time,start_time,end_time) : 
	"""Books a meeting room for a given time interval"""
	if date_time not in date_intervals : 
		room_id = 1 
		newInterval = [start_time,end_time,room_id]
		date_intervals[date_time].append(newInterval) 
		
		meeting_id = Generate_Hash.generate_id(employee_id) 
		interval_date = newInterval + [date_time]
		meetings[employee_id][meeting_id].append(interval_date)
		

		print('You have succesfully scheduled a meeting.\nDetails :') 
		print('Room ID :', room_id) 
		print('meeting ID :', meeting_id) 
		return 

	#check if the employee can handle this meeting in parallel 
	if is_burden(employee_id,start_time,end_time,date_time) :
		print('you have exceeded the max limit of bookings at a time')
		return 

        #initially 0 because no room has been allocated yet
	interval = [start_time,end_time,0] 
	insert( employee_id, interval, date_time) 


def cancel(employee_id, meeting_id) :
	"""Cancels the scheduled Meeting of an employee"""
	if employee_id not in meetings :
		print("You dont have any meetings scheduled yet !")
		return
	if meeting_id not in meetings[employee_id] :
		print("Sorry! You are not the organizer of this meeting") 
		return 

	#get the meeting of an employee to cancel 
	start_time,end_time,room_id,date_time = meetings[employee_id][meeting_id][0]
	interval = [start_time,end_time,room_id]
	date_intervals[date_time].remove(interval)

	del meetings[employee_id][meeting_id] 

	#if employee has no more meetings remove emp from map
	if len(meetings[employee_id]) == 0 :
		del meetings[employee_id]

	print("Meeting with the following details has been cancelled succesfully ! ")
	print("Room ID :", room_id)
	print("Meeting ID : ", meeting_id)
	




def is_burden(employee_id,start_time,end_time,date_time) : 
	"""Checks if employee has 2 meeting at a same time"""
	if employee_id not in meetings :
		return False 
	count = 0 
	for meet_id in meetings[employee_id] :
		for start,end,room_id,dt_time in meetings[employee_id][meet_id] :
			#if dates were same and interval overlap add it to the count
			if dt_time == date_time :
				if operationsUtils.is_interval_overlap(start,end,start_time,end_time) :
					count += 1 
					#Employee cant handle more than 2 at a time so it's a burden 
					if count == 2 :
						return True 

	return False 


while True : 
	print()
	print("###Schedule a Meeting###")
	print('1. Book a Meeting') 
	print('2. Cancel a Meeting') 
	print('3. Exit ')

	option = inputUtils.get_option()
	if option == 1 : 
		employee_id = inputUtils.get_employee()

		date_time = datetimeUtils.get_date()
		
		while True :
			
			start_hh,start_mins = datetimeUtils.get_time('start')
			
			end_hh,end_mins = datetimeUtils.get_time('end')

			start_time = start_hh*60 + start_mins 
			end_time = end_hh*60 + end_mins 
			
			#End time should be greater than start time 
			if end_time - start_time <= 0 :
				print('Invalid Time End time should be greater than start time')
				continue

			#check if the duration is less than 3 hours 
			if datetimeUtils.is_valid_time_frame(start_time,end_time) :
				break


		book(employee_id,date_time,start_time,end_time) 

	elif option == 2 :
		employee_id = inputUtils.get_employee() 
		meeting_id = input("Enter Meeting ID :")
		
		cancel(employee_id, meeting_id) 
		
	elif option == 3 :
		exit() 
	else :
		print('Invalid Option')

