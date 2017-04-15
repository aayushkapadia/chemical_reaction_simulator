from ExtraModules import EasyCRNMaker as maker

def execute(input1,input2):
	crn = maker()

	slowest = 1
	slower = 2
	slow = 3
	medium = 4
	fast = 5
	faster = 6
	fastest = 7

	crn.addReaction('c + 2y -> c + y',fast)
	crn.addReaction('c -> ',medium)
	crn.addReaction('p -> a',slowest)
	crn.addReaction('a + x -> b + a + xdash',medium)
	crn.addReaction('b + y -> ydash + d + b',fastest)
	crn.addReaction('b -> ',faster)
	crn.addReaction('ydash -> y',fast)
	crn.addReaction('a -> e',slow)
	crn.addReaction('e + y -> e',faster)
	crn.addReaction('e + xdash -> e + x',faster)
	crn.addReaction('e -> ',fast)
	crn.addReaction('d -> y',slower)


	crn.addInitConcentration('x->'+str(input1))
	crn.addInitConcentration('p->'+str(input2))
	crn.addInitConcentration('y->1')

	outputFileName = "power_"+str(input1)+"_"+str(input2)+".xml"

	crn.writeXMLToFile(outputFileName)

	return outputFileName,['x','p','y']