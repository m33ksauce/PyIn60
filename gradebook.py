gradebook = []

def main():
	print("Welcome to the Gradebook")
	print("========================")
	print("Type the option you want")
	print("1) Print the Gradebook")
	print("2) Add a grade")
	print("3) Remove a grade")
	print("4) Quit")

	while True:
		# Get the command input
		command = input("Option: ")

		if command == "1":
			print("\nGrades")
			print("======")
			for asgn, grade in gradebook:
				print("{} - {}".format(asgn, grade))
		elif command == "2":
			assignment = input("Assignment: ")
			grade = input("Grade: ")
			# Append as tuple
			gradebook.append((assignment, grade))
			print(gradebook)
			print("Added {} with grade {}"
				.format(assignment, grade))
		elif command == "3":
			print("You want to remove a grade")
		elif command == "4":
			print("You want to quit")
			return
	

if __name__ == "__main__":
	main()