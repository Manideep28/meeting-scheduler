class operationsUtils :
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
