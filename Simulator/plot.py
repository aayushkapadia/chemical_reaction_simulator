from Simulator import *
import XMLParser
import textToXML


def getHistoryFileName(xmlFileName):
	y = xmlFileName[:-3]
	y = y + 'txt'

	i = len(y) - 1
	while i>=0 :
		if y[i]=='\\' or y[i]=='/' :
			break
		i-=1

	if i>=0 :
		return y[:i+1] + 'history_' + y[i+1:]
	else:
		return 'history_' + y
	

def plotFromXML(fileName,simulationTime,chemicalList):
	historyFile = getHistoryFileName(fileName)
	sim =  XMLParser.getSimulator(fileName)
	sim.simulate(int(simulationTime),historyFile)
	sim.plot(chemicalList)

def plotFromTxt(fileName,simulationTime,chemicalList):
	xmlFile = textToXML.getXMLFromTxt(fileName)
	plotFromXML(xmlFile,simulationTime,chemicalList)
