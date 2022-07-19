## Get the value of x0 from user input, it will ask user to input again if the input is illegal
#
#  @param difficulty - it will decide the range of the input that is acceptable
#
#  @return x0 - the user input
def get_x0(difficulty = 1):
	while(1):
		while(1):
			try:
				x0 = float(input("Please enter the value of x0: "))
			except:
				print("x0 must be a float, please enter again.\n")
			else:
				break
		if(x0 >= 0 and x0 <= difficulty * 100):
			break
		print("The range of x0 is [0, {:.0f}], please enter again.\n".format(difficulty * 100))
	return x0

## Get the value of v0 from user input, it will ask user to input again if the input is illegal
#
#  @param difficulty - it will decide the range of the input that is acceptable
#
#  @return v0 - the user input
def get_v0(difficulty = 1):
	while(1):
		while(1):
			try:
				v0 = float(input("Please enter the value of v0: "))
			except:
				print("v0 must be a float, please enter again.\n")
			else:
				break
		if(v0 >= 0 and v0 <= difficulty * 100):
			break
		print("The range of v0 is [0, {:.0f}], please enter again.\n".format(difficulty * 100))
	return v0

## Get the value of x0 from user input, it will ask user to input again if the input is illegal
#
#  @param case - it will decide the range of the input that is acceptable, in scene A case 0 will be used, and in scene B case 1 will be used
#
#  @return theta - the user input
def get_theta(case = 0):
	while(1):
		while(1):
			try:
				theta = float(input("Please enter the value of theta: "))
			except:
				print("theta must be a float, please enter again.\n")
			else:
				break
		if(case):
			if(theta >= 0 and theta <= 180):
				break
			print("The range of theta is [0, 180], please enter again.\n")
		else:
			if(theta >= 0 and theta <= 90):
				break
			print("The range of theta is [0, 90], please enter again.\n")
	return theta

if __name__ == "__main__":
	while(1):
		#a = get_x0()
		#a = get_v0()
		#a = get_theta()
		a = get_theta(1)
		print(a)