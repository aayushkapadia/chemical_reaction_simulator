from ExtraModules import EasyCRNMaker as maker

def execute(input1):
	crn = maker()

	crn.addReaction(' -> a-ab',1)
	crn.addReaction('a + a-ab -> a',2)
	crn.addReaction('2a-ab -> a-ab',3)

	crn.addInitConcentration('a->'+str(input1))

	outputFileName = "inversion_"+str(input1)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName,['a','a-ab']