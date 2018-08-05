# Write your solution for 1.4 here!

def is_prime(x):
		# mod = x
		for i in range(x-1, 1, -1):
			if x % i == 0 :
				return False
		return True


		# else:
		# 	return True

# is_prime(8)
print(is_prime(5191))

