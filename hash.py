import random
class Generate_Hash :
	"""Generates a Hash"""
	def __init__(self) :
		pass 

	def generate_id(employee_id) :
		"""generates a random hash with getrandbits"""

		hash_bits = random.getrandbits(128)
		hash_code = "%032x" % hash_bits
		hash = hash_code[:6] + str(employee_id)

		return hash 

