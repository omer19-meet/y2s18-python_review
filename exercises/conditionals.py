# Write your solution for 1.2 here!
a = 0
x=0
# for i in range(101):

# 	if i%2 == 0:
# 		a = a+i
# 		print(a)
# 		# x  =+1 

big = 2
for i in range(1000):
	if i%6==2 and i**3%5==3 :
		if i > big :
			big = i 

		
	# 	print(".")
print(big)