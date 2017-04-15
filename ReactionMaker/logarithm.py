from ExtraModules import EasyCRNMaker as maker

def execute(input1):
	crn = maker()

	crn.addReaction('b -> b + a',1)
	crn.addReaction('xdash -> x',2)
	crn.addReaction('a + 2x -> c + xdash + a',5)
	crn.addReaction('c -> y',3)
	crn.addReaction('a -> ',4)
	crn.addReaction('2c -> c',6)

	crn.addInitConcentration('x->'+str(input1))
	crn.addInitConcentration('b->1')

	outputFileName = "logarithm_"+str(input1)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName,['x','y']