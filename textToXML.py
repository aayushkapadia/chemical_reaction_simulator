import sys

openFile = None

def take_input():
		global openFile
		inputString = openFile.readline()
		return inputString.strip()

def getXMLFromTxt(file_name):
	global openFile
	
	sys.path.insert(0, 'ReactionMaker')
	from ExtraModules import EasyCRNMaker as maker

	openFile = open(file_name)
	inputString = ''
	crn = maker()

	while True:
		inputString = take_input()
		if inputString == "Absence:" :
			break

	while True:
		inputString = take_input()
		if inputString=="":
			break
		crn.addAbsence(inputString)

	while True:
		inputString = take_input()
		if inputString == "Reactions:" :
			break

	while True:
		inputString = take_input()
		if inputString=="":
			continue
		if inputString == "Concentrations:":
			break
		i = inputString.index('{')
		j = inputString.index('}')
		crn.addReaction(inputString[:i],inputString[i+1:j])

	while True:
		inputString = take_input()
		if inputString=="" or inputString is None:
			break
		crn.addInitConcentration(inputString)

	file_name = "temp.xml"
	crn.writeXMLToFile(file_name)

	print 'successfully written '+file_name
	return file_name