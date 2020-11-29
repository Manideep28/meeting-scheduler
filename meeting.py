import datetime 
from collections import defaultdict

from hash import Generate_Hash 

from operations import Operations

print('*********Welcome to FlyFin Meetings********** ')
m = int(input("Enter Total number of meeting rooms :")) 
n = int(input("Enter Total number of Employees :"))		
print("Success Meeting rooms have been created") 

#dictionary (map) to store intervals with roomid 
#key = datetime and value = intevals with roomid 
d = defaultdict(list)
#meetings has empid as key ,meetingid as inner dict (map) key, value as interval with date_time
meetings = defaultdict(lambda : defaultdict(list)) 


def insert( employee_id, newInterval, date_time) : 
		"""Inserts a new interval and assigns room id"""
		intervals = d[date_time] 
		unavailable_rooms = set() 
		not_overlapped = False 
		stack = [] 

		i = 0 

		#check the overlapping intervals with the newInterval 
		new_room_id = 1 
		while i < len(intervals) : 
			s,e,room_id = intervals[i] 
			
			if newInterval[0] < e : 
				if newInterval[1] < s : 
					not_overlapped = True 
					break 
				unavailable_rooms.add(room_id) 

			i += 1 

		#Assign room available at this interval 
		if not_overlapped :
			new_room_id = 1 
		elif len(unavailable_rooms) == m :
			print("No Rooms available at this Time Slot ") 
			return False
		else :
			new_room_id = Operations.get_room(unavailable_rooms,m)

		newInterval[2] = new_room_id	
		stack += intervals[:i]
		stack += newInterval,
		stack += intervals[i:]
		
		d[date_time] = stack 

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
	if date_time not in d : 
		room_id = 1 
		newInterval = [start_time,end_time,room_id]
		d[date_time].append(newInterval) 
		
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

	interval = [start_time,end_time,0] 
	insert( employee_id, interval, date_time) 


def Cancel(employee_id, meeting_id) :
	"""Cancels the scheduled Meeting of an employee"""
	if employee_id not in meetings :
		print("You dont have any meetings scheduled yet !")
		return
	if meeting_id not in meetings[employee_id] :
		print("you are not the organizer of this meeting") 
		return 

	#get the meeting of an employee to cancel 
	start_time,end_time,room_id,date_time = meetings[employee_id][meeting_id][0]
	interval = [start_time,end_time,room_id]
	d[date_time].remove(interval)

	del meetings[employee_id][meeting_id] 

	#if employee has no more meetings remove emp from map
	if len(meetings[employee_id]) == 0 :
		del meetings[employee_id]

	print("Meeting with the following details have succesfully Cancelled ! ")
	print("Room ID :", room_id)
	print("Meeting ID : ", meeting_id)
	




def is_burden(employee_id,start_time,end_time,date_time) : 
	"""Checks if employee has 2 meeting at a same time"""
	if employee_id not in meetings :
		return False 
	count = 0 
	for meet_id in meetings[employee_id] :
		for mst,met,rm_id,dt_time in meetings[employee_id][meet_id] :
			#if dates were same and interval overlap add it to the count
			if dt_time == date_time :
				if Operations.is_interval_overlap(mst,met,start_time,end_time) :
					count += 1 
					#Employee cant handle more than 2 at a time so it's a burden 
					if count == 2 :
						return True 

	return False 


while True : 
	print("###Schedule a Meeting###")
	print('1. Book a Meeting') 
	print('2. Cancel a Meeting') 
	print('3. Exit ')
	option = int(input("Enter your input :")) 
	if option == 1 : 
		employee_id = int(input("Enter Employee ID :")) 

		date_time = Operations.get_date()
		
		while True :
			
			start_hh,start_mins = Operations.get_time('start')
			
			end_hh,end_mins = Operations.get_time('end')

			start_time = start_hh*60 + start_mins 
			end_time = end_hh*60 + end_mins 
			
			if end_time - start_time <= 0 :
				print('Invalid Time End time should be greater than start time')
				continue

			if Operations.is_valid_time_frame(start_time,end_time) :
				break


		book(employee_id,date_time,start_time,end_time) 

	elif option == 2 :
		employee_id = int(input("Enter Employee ID : "))
		meeting_id = input("Enter Meeting ID :")
		
		Cancel(employee_id, meeting_id)
	elif option == 3 :
		exit()
	else :
		print('Invalid Input ')

