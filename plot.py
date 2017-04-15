from Simulator import *
import XMLParser
import textToXML

def plotFromXML(fileName,simulationTime,chemicalList):
	sim =  XMLParser.getSimulator(fileName)
	sim.simulate(int(simulationTime))
	sim.plot(chemicalList)

def plotFromTxt(fileName,simulationTime,chemicalList):
	xmlFile = textToXML.getXMLFromTxt(fileName)
	plotFromXML(xmlFile,simulationTime,chemicalList)
