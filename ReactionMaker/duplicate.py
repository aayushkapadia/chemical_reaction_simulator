from ExtraModules import EasyCRNMaker as maker

def execute(input1):
	crn = maker()

	crn.addAbsence('y-ab -> y')
	crn.addAbsence('g-ab -> g')

	crn.addReaction('y + g -> ydash + g',1)
	crn.addReaction('g + y-ab -> ',2)
	crn.addReaction('g-ab + ydash -> y + z',3)
	crn.addReaction('xrx -> ',3)
	crn.addReaction('xdash + gdash-ab + xrx-ab -> ',4)

	crn.addInitConcentration('y->'+str(input1))
	crn.addInitConcentration('g->1')

	outputFileName = "duplicate_"+str(input1)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName