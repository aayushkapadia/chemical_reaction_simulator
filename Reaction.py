import operator 

class ReactionChemical:
	def __init__(self,name,coeff,absense_name = None):
		self.name = name
		self.coeff = coeff
		self.absense_name = absense_name 
		if absense_name != None:
			self.coeff = 1

	def isAbsenseIndicator(self):
		if self.absense_name==None:
			return False
		else:
			return True

class Reaction:
	# higher the k more fast the reaction will be
	def __init__(self,k):
		self.reactants = []
		self.products = []
		self.k = k

	def addReactant(self,reactant):
		self.reactants.append(reactant)

	def addProduct(self,product):
		self.products.append(product)

	def satisfies(self,concentrations):
		for reactant in self.reactants:
			concentration = concentrations.get(reactant.name)
			if concentration==None:
				return False
			else:
				if concentration<reactant.coeff:
					return False
		return True

class ReactionNetwork:
	def __init__(self):
		self.reactions = []
		self.concentrations = dict()

	# Adds new reaction to the chemical network
	# Also adds any new chemical if found
	def addReaction(self,reaction):
		self.reactions.append(reaction)

		for reactant in reaction.reactants:
			chemical_name = None
			if reactant.isAbsenseIndicator():
				chemical_name = reactant.absense_name
			else:
				chemical_name = reactant.name

			self.concentrations[chemical_name] = 0

		for product in reaction.products:
			chemical_name = None
			if product.isAbsenseIndicator():
				chemical_name = product.absense_name
			else:
				chemical_name = product.name

			self.concentrations[chemical_name] = 0

	# Returns false if no such chemical present in the network
	# Returns true if initial concentration is updated
	def addInitConcentration(self,chemical_name,initConcentration):
		if self.concentrations.get(chemical_name)==None:
			return False
		self.concentrations[chemical_name] = initConcentration
		return True

	# Sort the reactions according to rate constant
	def prepare(self):
		self.reactions = sorted(self.reactions, key=operator.attrgetter('k'))

	# Returns the fastest reaction which satisfies min concentration
	def getFastestReaction(self):
		for reaction in reversed(self.reactions):
			if reaction.satisfies(self.concentrations):
				return reaction
		return None

	def doReaction(self,reaction):
		for reactant in reaction.reactants:
			self.concentrations[reactant.name] -= reactant.coeff
		for product in reaction.products:
			self.concentrations[product.name] += product.coeff