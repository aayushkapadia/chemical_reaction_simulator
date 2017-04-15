from ExtraModules import EasyCRNMaker as maker

def execute(input1):
	crn = maker()

	crn.addAbsence('x-ab -> x')
	crn.addAbsence('gdash-ab -> g')
	crn.addAbsence('xrx-ab -> xrx')

	crn.addReaction('x + g -> xdash + g',1)
	crn.addReaction('x-ab + g -> ',2)
	crn.addReaction('2xdash + gdash-ab -> xdash + x + xrx',5)
	crn.addReaction('xrx -> ',3)
	crn.addReaction('xdash + gdash-ab + xrx-ab -> ',4)

	crn.addInitConcentration('x->'+str(input1))
	crn.addInitConcentration('g->1')

	outputFileName = "decrement_"+str(input1)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName,['x']