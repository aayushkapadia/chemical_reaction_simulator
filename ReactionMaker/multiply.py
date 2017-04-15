from ExtraModules import EasyCRNMaker as maker

def execute(input1,input2):
	crn = maker()

	crn.addReaction('x -> i',1)
	crn.addReaction('ydash -> y',2)
	crn.addReaction('i + y -> i + ydash + z',4)
	crn.addReaction('i -> ',3)

	crn.addInitConcentration('x->'+str(input1))
	crn.addInitConcentration('y->'+str(input2))

	outputFileName = "multiply_"+str(input1)+"_"+str(input2)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName