import xml.etree.ElementTree as ET
from Reaction import *
from Simulator import *

def getSimulator(xmlFile):
	tree = ET.parse(xmlFile)
	crn_tag = tree.getroot()

	crn = ReactionNetwork()

	reactions_tag = crn_tag.find('reactions')
	init_tag = crn_tag.find('init')

	for reaction_tag in reactions_tag: # Traverse over all reactions
		rate_constant = int(reaction_tag.attrib.get('rate_constant',1))
		reaction = Reaction(rate_constant)

		for reaction_chemical_tag in reaction_tag:
			chemical_name = reaction_chemical_tag.attrib.get('name')
			chemical_coeff = int(reaction_chemical_tag.attrib.get('coeff'))
			absense_name = reaction_chemical_tag.attrib.get('absense_name')
			recChemical = ReactionChemical(chemical_name,chemical_coeff,absense_name)

			if reaction_chemical_tag.tag=='reactant':
				reaction.addReactant(recChemical)
			else:
				reaction.addProduct(recChemical)

		crn.addReaction(reaction)

	for chemical_tag in init_tag:
		chemical_name = chemical_tag.attrib.get('name')
		init_conc = int(chemical_tag.attrib.get('val'))
		crn.addInitConcentration(chemical_name,init_conc)

	return Simulator(crn)




				

