from Simulator import *
import XMLParser
import textToXML

def getHistoryFileName(xmlFileName):
	y = xmlFileName[:-3]
	return 'history_' + y + 'txt'

def plotFromXML(fileName,simulationTime,chemicalList):
	historyFile = getHistoryFileName(fileName)
	sim =  XMLParser.getSimulator(fileName)
	sim.simulate(int(simulationTime),historyFile)
	sim.plot(chemicalList)

def plotFromTxt(fileName,simulationTime,chemicalList):
	xmlFile = textToXML.getXMLFromTxt(fileName)
	plotFromXML(xmlFile,simulationTime,chemicalList)
