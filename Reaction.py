import operator 

class ReactionChemical:
	'''
	Describes a particular chemical of reaction along with its coefficients. It can either be on reactant side or product side.
	eg. 2A,10B,3C ... 

	Attributes: 
		name : name of the chemical 
		coeff : Coeffient that is to be used for the chemical in the reaction
		absense_name : the chemical it is indicating absense of. None if it is not a absense indicator chemical.
	'''

	def __init__(self,name,coeff,absense_name = None):
		'''
			Initialize object with given parameters. Also it normalizes the coeff of absense indicator chemicals to 1.
		'''
		self.name = name
		self.coeff = coeff
		self.absense_name = absense_name 

		if self.isAbsenseIndicator(): # There is no meaning of coeffecient with absense indicator chemicals so normalizing coeff to 1
			self.coeff = 1

	def isAbsenseIndicator(self):
		'''
			Return True if the chemical is an absense indicator chemical else returns False
		'''
		if self.absense_name==None:
			return False
		else:
			return True

class Reaction:
	'''
		Describes any chemical reaction. 
		eg. 2A + 3B -> 6C

		Attributes: 
			reactants : List Of ReactionChemical that are present on the reactant side of the reaction
			products : List Of ReactionChemical that are present on the product side of the reaction
			k : Rate constant for the reaction. Higher the rate constant, it will be more faster.
	'''

	def __init__(self,k):
		'''
		Initalize the reaction with given rate constant and empty set of reactants and products
		'''
		self.reactants = []
		self.products = []
		self.k = k

	def addReactant(self,reactant):
		'''
		Add ReactionChemical 'reactant' to the reactant side of the reaction
		'''
		self.reactants.append(reactant)

	def addProduct(self,product):
		'''
		Add ReactionChemical 'product' to the product side of the reaction

		Precondition :
			product should not be absense indicator chemical.
		'''
		self.products.append(product)

	def satisfies(self,concentrations):
		'''
			Returns True if this reaction can be performed given the concentration of the different chemicals in the network else returns False

			Parameters:
				concentrations : Dictionary object mapping chemical_name to its concentration in the network
		'''

		for reactant in self.reactants:
			if reactant.isAbsenseIndicator():	
				if concentrations.get(reactant.absense_name)>0: # The chemical which this is representing absense of is still present . So cannot perform this reaction
					return False
			else:
				if concentrations.get(reactant.name)<reactant.coeff: # Cannot perform the reaction because concentration of this chemical is less than what is required for this reaction to perform. 
					return False
		return True # All ReactionChemical on the reactant side satisfies the criteria for reaction performance

class ReactionNetwork:
	'''
		Describes a ideal chemical reaction network. See definition of ideal in README

		States of the system :
			Constructing stage : You are still adding reactions to the network. (Initial Stage)
			Running stage : Now you are allowed to execute any reaction. And you can no longer add any new reaction to the network.

		Attributes:
			reactions: List of all possible reactions that can happen in this network at each time step.
			concentrations : Dictionary mapping chemical_name to its current concentrations in the network. Absense indicator chemicals are not there in dictionary.
	'''
	def __init__(self):
		'''
			Initialize the network with no reactions and no chemicals.
		'''
		self.reactions = []
		self.concentrations = dict()

	def addReaction(self,reaction):
		'''
			Adds a new reaction to the network.
			If reaction contains any chemical which is not yet registered in the network, it automatically registers the chemical with 0 current concentration.
			Same holds for absense indicator chemical. If the chemical it indicates absense of is not yet registered, it registers it with 0 concentration.
		'''
		self.reactions.append(reaction)

		for reactant in reaction.reactants: # Finding any new chemical on reactant side
			if reactant.isAbsenseIndicator():
				self.concentrations[reactant.absense_name] = 0
			else:
				self.concentrations[reactant.name] = 0
			

		for product in reaction.products: # Finding any new chemical on product side
			if product.isAbsenseIndicator():
				self.concentrations[prodcut.absense_name] = 0
			else:
				self.concentrations[prodcut.name] = 0

	
	def addInitConcentration(self,chemical_name,initConcentration):
		'''
			Modify initial concentration of the chemical with given initial concentration.
			Preconditions:
				Network is in constructing stage.
				The chemical is already registered in the network.
		'''
		self.concentrations[chemical_name] = initConcentration

	def prepare(self):
		'''
		Transfering of state from constructing to running. 
		Sorts all reaction according to their rate constants.
		'''
		self.reactions = sorted(self.reactions, key=operator.attrgetter('k'))

	def getFastestReaction(self):
		'''
			Returns the fastest reaction among all possible reactions.
			Returns None if none of them can be performed.

			Preconditions:
				Network is in running stage
		'''
		for reaction in reversed(self.reactions): # Iterating the reactions in decreasing rate constants order
			if reaction.satisfies(self.concentrations):
				return reaction
		return None # No reaction possible

	def doReaction(self,reaction):
		'''
			Performs the given reaction in the system.

			Prequisite :
				The reaction should be present in the network.
		'''
		for reactant in reaction.reactants:
			if reactant.isAbsenseIndicator():
				pass
			else:
				self.concentrations[reactant.name] -= reactant.coeff

		for product in reaction.products: # There are no absense indicators on product side of reaction
			self.concentrations[product.name] += product.coeff