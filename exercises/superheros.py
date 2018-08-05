# Write your solutions for 1.5 here!
class superhero(object):
	"""docstring for superhero"""
	def __init__(self, name ,power ,strengh):
		# super(superhero, self).__init__()
		self.name = name
		self.power = power
		self.strengh = strengh
	def name_superp(self):
		print(self.name)
		print(self.power)

	def save_sivilian(self , work):
		if work	<self.strengh:
			self.strengh =  self.strengh - work
			print(self.strengh)
		else:
			print("super hero is actually not such soper..... )-: ")


	






omer = superhero("omer", "invisibal", 8)
# print(omer.strengh)
omer.name_superp()
omer.save_sivilian(7)
