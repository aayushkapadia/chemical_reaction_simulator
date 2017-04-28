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

	# generating add and decrement indicators 
	addIndicator = 'gdash'+str(stepNumber)
	decrementIndicator = 'gdoubledash'+str(stepNumber)
	loopIndicator = 'gtripledash'+str(stepNumber)

	# generating intermediate molecules
	input1Copy = input1+'dash'
	input2Copy = input2+'dash'

	# generating absense molecules
	outputIndicatorAbs = getAbsense(outputIndicator)
	input1Abs = getAbsense(input1)
	input2Abs = getAbsense(input2)
	addIndicatorAbs = getAbsense(addIndicator)
	decrementIndicatorAbs = getAbsense(decrementIndicator)
	input1CopyAbs = getAbsense(input1Copy)
	input2CopyAbs = getAbsense(input2Copy)

	# registering absense molecules in the dictionary
	registerAbsense(input1,input1Abs,absenseDict)
	registerAbsense(input2,input2Abs,absenseDict)
	registerAbsense(outputIndicator,outputIndicatorAbs,absenseDict)
	registerAbsense(addIndicator,addIndicatorAbs,absenseDict)
	registerAbsense(decrementIndicator,decrementIndicatorAbs,absenseDict)
	registerAbsense(input1Copy,input1CopyAbs,absenseDict)
	registerAbsense(input2Copy,input2CopyAbs,absenseDict)

	# Generating the reactions

	# generating add and decrement indicators so that they can progress parallely
	reaction1 = inputIndicator  + ' -> ' + addIndicator + ' + ' + decrementIndicator + ' + ' + loopIndicator
	reactions.append(reaction1 + '{' + fast + '}')
	
	# doing add operation z+= y with y maintained and not destroyed

	# y + gdash -> ydash + gdash
	reaction2 = input2 + ' + ' + addIndicator + ' -> ' + input2Copy + ' + ' + addIndicator
	reactions.append(reaction2 + '{' + fast + '}')

	# y-ab + gdash -> null
	reaction3 = input2Abs + ' + ' + addIndicator + ' -> '
	reactions.append(reaction3 + '{' + fast + '}')

	# ydash + gdash-ab -> y + z
	reaction4 = input2Copy + ' + ' + addIndicatorAbs + ' -> ' + input2 + ' + ' + output
	reactions.append(reaction4 + '{' + fast + '}')

	# doing decrement operation x--

	# x + gdoubledash -> xdash + gdoubledash
	reaction5 = input1 + ' + ' + decrementIndicator + ' -> ' + input1Copy + ' + ' + decrementIndicator
	reactions.append(reaction5 + '{' + fast + '}')

	# x-ab + gdoubledash -> null
	reaction6 = input1Abs + ' + ' + decrementIndicator + ' -> '
	reactions.append(reaction6 + '{' + fast + '}')

	# 2xdash + gdoubledash-abs -> xdash + x
	reaction7 = '2' + input1Copy + ' + ' + decrementIndicatorAbs + ' -> ' + input1Copy + ' + ' + input1
	reactions.append(reaction7 + '{' + fast + '}')

	# xdash -> null
	reaction8 = input1Copy + ' -> '
	reactions.append(reaction8 + '{' + slow + '}')	


	# Looping reaction when both addition and decrement is complete

	# xdash-ab + ydash-ab + gdash-ab + gdoubledash-ab + x + gtripledash -> x + g  
	reaction9 = input1CopyAbs + ' + ' + input2CopyAbs + ' + ' + addIndicatorAbs + ' + ' + decrementIndicatorAbs + ' + ' + input1 + ' + ' + loopIndicator + ' -> ' + input1 + ' + ' + inputIndicator
	reactions.append(reaction9 + '{' + fast + '}')	

	# Breaking out of loop and completing the reaction

	# xdash-ab + ydash-ab + gdash-ab + gdoubledash-ab + x-ab + goutAbs  + gtripledash -> gOut  
	reaction9 = input1CopyAbs + ' + ' + input2CopyAbs + ' + ' + addIndicatorAbs + ' + ' + decrementIndicatorAbs + ' + ' + input1Abs + ' + ' + loopIndicator + ' + ' + outputIndicatorAbs + ' -> ' + outputIndicator
	reactions.append(reaction9 + '{' + fast + '}')	

	return reactions

'''absenseDict = dict()
list1 = getListOfReactions('x','y','z',absenseDict,1)
for x in list1:
	print x
print absenseDict'''


