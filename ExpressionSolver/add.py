def getAbsense(chemical):
	absenseChemical = chemical+'-ab'
	return absenseChemical

def registerAbsense(chemical,absenseChemical,absenseDict):
	absenseDict[absenseChemical] = chemical


def getListOfReactions(input1,input2,output,absenseDict,stepNumber):
	reactions = []
	fast = '100'
	slow = '1'

	# generating input and output indicators
	inputIndicator = 'g'+str(stepNumber)
	outputIndicator = 'g'+str(stepNumber+1)

	# generating absense molecules
	outputIndicatorAbs = getAbsense(outputIndicator)
	input1Abs = getAbsense(input1)
	input2Abs = getAbsense(input2)

	# registering absense molecules in the dictionary
	registerAbsense(input1,input1Abs,absenseDict)
	registerAbsense(input2,input2Abs,absenseDict)
	registerAbsense(outputIndicator,outputIndicatorAbs,absenseDict)

	# Generating the reactions

	# x -> z
	reaction1 = input1 + ' + ' + inputIndicator + ' -> ' + output + ' + ' + inputIndicator
	reactions.append(reaction1 + '{' + fast + '}')
	
	# y -> z
	reaction2 = input2 + ' + ' + inputIndicator + ' -> ' + output + ' + ' + inputIndicator
	reactions.append(reaction2 + '{' + fast + '}')

	# generating output signal and disabling input signal on completion of both the above reactions
	reaction3 = input1Abs + ' + ' + input2Abs + ' + ' + inputIndicator + ' + ' + outputIndicatorAbs + ' -> '  + outputIndicator
	reactions.append(reaction3 + '{' + fast + '}')

	return reactions

'''absenseDict = dict()
list1 = getListOfReactions('x','y','z',absenseDict,1)
for x in list1:
	print x
print absenseDict'''


