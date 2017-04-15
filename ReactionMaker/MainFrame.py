import inversion
import duplicate
import increment
import decrement
import multiply
import logarithm
import power

def printWelcomeMessage():
	print "Welcome to the Chemical Computer world!!"

def executeInversion():
	var = raw_input("Enter the value you want to invert: ")
	return inversion.execute(var)

def executeDuplicate():
	var = raw_input("Enter the value you want to duplicate: ")
	return duplicate.execute(var)

def executeDecrement():
	var = raw_input("Enter the value you want to decrement: ")
	return decrement.execute(var)


def executeIncrement():
	var = raw_input("Enter the value you want to increment: ")
	return increment.execute(var)

def executeMultiply():
	input1 = raw_input("Enter the value of input 1: ")
	input2 = raw_input("Enter the value of input 2: ")
	return multiply.execute(input1,input2)

def executeLogarithm():
	var = raw_input("Enter the value you want to take logarithm of: ")
	return logarithm.execute(var)

def executePower():
	input1 = raw_input("Enter the value of base: ")
	input2 = raw_input("Enter the value of exponent: ")
	return power.execute(input1,input2)

def showMainMenu():
	print "Enter your choice here: "
	print "1: Basic Functions"
	print "2: Advanced Functions"
	print "3: Exit"

def showBasicFunctionsMenu():
	print "Select any one of the below basic function"
	print "1: Inversion"
	print "2: Duplication/Copy"
	print "3: Decrementation"		
	print "4: Incrementation"
	
def showAdvancedFunctionsMenu():
	print "Select any one of the below advanced function"
	print "1: Multiplication"
	print "2: Logarithm"
	print "3: Power"

def showInvalidMessageAndQuit():
	print "Please select only one of the given choice"
	print "Quitting the Chemical World ..."
	quit()

def executeBasicFunction(userChoice):
	outputFileName = ''

	if userChoice == 1:
		outputFileName = executeInversion()
	elif userChoice == 2:
		outputFileName = executeDuplicate()
	elif userChoice == 3:
		outputFileName = executeDecrement()
	elif userChoice == 4:
		outputFileName = executeIncrement()
	else:
		showInvalidMessageAndQuit()

	print 'Result File ' + outputFileName + ' Created'

def executeAdvancedFunction(userChoice):
	outputFileName = ''

	if userChoice == 1:
		outputFileName = executeMultiply()
	elif userChoice == 2:
		outputFileName = executeLogarithm()
	elif userChoice == 3:
		outputFileName = executePower()
	else:
		showInvalidMessageAndQuit()

	print 'Result File ' + outputFileName + ' Created'

def executeUserChoice(userChoice):
	if userChoice == 1:
		showBasicFunctionsMenu()
		userChoice = int(input())
		executeBasicFunction(userChoice)
	elif userChoice == 2:
		showAdvancedFunctionsMenu()
		userChoice = int(input())
		executeAdvancedFunction(userChoice)
	elif userChoice == 3:
		print "Quitting the Chemical World ..."
		quit()
	else:
		showInvalidMessageAndQuit()

def main():
	printWelcomeMessage()
	while True:
		print ""
		showMainMenu()
		userChoice = int(input())
		executeUserChoice(userChoice)

main()