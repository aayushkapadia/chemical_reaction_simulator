from Reaction import *


class Simulator:
	def __init__(self,crn):
		self.crn = crn
		self.simulationData = dict()
		self.crn.prepare()

		for chemical_name in self.crn.concentrations:
			self.simulationData[chemical_name] = []

	def addInSimulationData(self,concentrations):
		for chemical_name in concentrations:
			self.simulationData[chemical_name].append(concentrations[chemical_name])

	def simulate(self,timeSteps):
		print self.crn.concentrations
		self.addInSimulationData(self.crn.concentrations)
		for i in range(timeSteps):
			reaction = self.crn.getFastestReaction()
			if reaction != None:
				self.crn.doReaction(reaction)
			self.addInSimulationData(self.crn.concentrations)
			print self.crn.concentrations

		#for chemical_name in self.simulationData:
		#	print chemical_name,'-> ',self.simulationData[chemical_name]

		
				



