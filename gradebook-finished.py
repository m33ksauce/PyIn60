gradebook = []
gradebookFileName = "mygradebook.csv"

def main():
	command = None

	print("Welcome to the gradebook!\n")

	loadGradebook()
	

	while True:
		printMenu()
		command = input("Option: ")

		if (command == "1"):
			printSummary()
		elif (command == "2"):
			addGrade()
		elif (command == "3"):
			removeGrade()
		elif (command == "4"):
			saveGradebook()
		elif (command == "5"):
			return

		print("\n")

def printMenu():
	print("Select an option below:")
	print("=======================\n")
	print("1) Print grade summary")
	print("2) Add a grade")
	print("3) Remove a grade")
	print("4) Save")
	print("5) Quit")

def printSummary():
	total_grades = 0
	avg = 100
	print("Grades\n======")
	for (asgn, grade) in gradebook:
		print("{} - {}".format(asgn, grade))
		total_grades += int(grade)

	if len(gradebook) > 0:
		avg = total_grades/len(gradebook)

	print("\nAverage: {:.2f}".format(avg))

def addGrade():
	assignment = input("Assignment name: ")
	grade = input("Grade: ")

	gradebook.append((assignment,grade))
	print("You added a grade of {} for assignment {}".format(grade, assignment))

	return (assignment, grade)

def removeGrade():
	asgn_to_remove = input("Assignment to remove: ")

	removeAt = None

	for idx, (asgn, grade) in enumerate(gradebook):
		if asgn == asgn_to_remove:
			gradebook.pop(idx)
			print("Removed {} from gradebook".format(asgn_to_remove))
			return

	print("Could not find assignment!")

def loadGradebook():
	try:
		gbFile = open(gradebookFileName, "rt")

		for line in gbFile:
			(a, g) = line.split(",")
			gradebook.append((a,g))

		gbFile.close()
	except:
		print("No existing gradebook")

def saveGradebook():
	print("Saving...")
	gbFile = open(gradebookFileName, "wt")
	for (assignment, grade) in gradebook:
		nxt = formatGradeLine(assignment, grade)
		writeNextLine(gbFile, nxt)
	gbFile.close()

def formatGradeLine(assignment, grade):
	return "{},{}\n".format(assignment, grade)

def writeNextLine(outFile, nextLine):
	outFile.write(nextLine)

if __name__ == "__main__":
	main()