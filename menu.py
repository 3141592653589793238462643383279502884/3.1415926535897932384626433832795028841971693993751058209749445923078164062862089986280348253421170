from sys import exit
from game import game

def menu():
	print("Welcome to shoot game!\n")
	while(1):
		print("0: Play\n1: Exit\n")
		case = input()
		if(case == "0"):
			game()
			return
		if(case == "1"):
			print("Goodbye.\n")
			exit(0)
		else:
			print("Invalid input. Please enter again.\n")

if __name__ == "__main__":
	menu()