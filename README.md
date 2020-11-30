# meeting-scheduler
Meeting scheduler in python on command line 

To Execute main file command : python main.py 

Main file will get the inputs of total number of rooms and employees 
Also gets the option 
1.Book a Meeting
2.Cancel a Meeting
3.Exit 

# How are we storing data ?
The time is converted to minutes and we store the time intervals for each date. 
so that we can room associated with that intervals which inturns optimises the time to 
schedule and cancel a meeting (insert and delete and interval)

The data stored in a map ( dictionary in python ) looks like 
datetime[date] = [ Start Time,End Time,Room ID]

The unique meeting id is created and the employee to meeting ID is data is stored in a meetings dict 

meetings[Employee ID][Meeting ID] = [Interval]
Here, Interval also consists of a date time 

# How to delete data upon cancellation ?
Employee gives his ID and Meeting ID 
so that based on these details we can remove from meetings. 
while deleting we store the datetime and interval from meetings 

And this date time is user to cancel the schedule from datetime

# Features 
book(employee_id, start_time, end_time)
● if success, prints the id of the room and id of the meeting itself
● If given time is beyond 1 month, prints 'Cannot book beyond 1 month from
today'
● If meeting duration is more than 3 hrs, prints 'Cannot book a meeting of more
than 3 hrs duration'
● if this employee has already 2 meetings scheduled at the same time, prints 'you
have exceeded the max limit of bookings at a time'
● Disable Past Dates : User cannot schedule meeting on previous days
● if room not found, prints 'All rooms busy for the given time interval'

● cancel(employee_id, meeting_id)
● if success, prints 'success'
● if this employee id is not the organiser of this meeting id, prints 'you are not the
organizer of this meeting'
● If employee has no meetings prints 'You dont have any meetings scheduled yet ! '
