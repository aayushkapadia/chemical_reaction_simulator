from Reaction import *
import matplotlib.pyplot as plt


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

	def simulate(self,timeSteps,filePath):
		historyFile = open(filePath,'w')
		historyFile.write(str(self.crn.concentrations))
		historyFile.write('\n')
		self.addInSimulationData(self.crn.concentrations)
		for i in range(timeSteps):
			reaction = self.crn.getFastestReaction()
			if reaction != None:
				self.crn.doReaction(reaction)
			self.addInSimulationData(self.crn.concentrations)
			historyFile.write(str(self.crn.concentrations))
			historyFile.write('\n')
		print 'History file ' + filePath + ' created'

	def plot(self,listOfChemicals):
		for chemical in listOfChemicals:
			initString = 'init = '+str(self.simulationData[chemical][0])
			endString = 'end = '+ str(self.simulationData[chemical][-1])
			plt.plot(self.simulationData[chemical],label=chemical + '(' + initString +',' + endString + ')')
		plt.ylabel('Concentration')
		plt.xlabel('Time (unit time)')
		plt.legend()
		plt.show()



		
				



