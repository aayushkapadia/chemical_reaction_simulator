from Reaction import *

class Simulator:
	def __init__(self,crn):
		self.crn = crn

	def simulate(self,timeSteps):
		print self.crn.concentrations
		for i in range(timeSteps):
			reaction = self.crn.getFastestReaction()
			if reaction != None:
				self.crn.doReaction(reaction)
			print self.crn.concentrations
				



