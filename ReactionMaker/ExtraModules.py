import xml.etree.cElementTree as ET
from xml.dom import minidom

def getTag(tagname):
		return ET.Element(tagname)

def getNameAndCoeff(chemical):
		i = 0
		while i<len(chemical):
			if chemical[i]<'0' or chemical[i]>'9':
				break
			i = i + 1
		if i == 0:
			return chemical,"1"
		else:
			return chemical[i:],chemical[0:i]

class EasyCRNMaker():
	def __init__(self):
		self.absenseDictionary = dict()
		self.crnTag = getTag("crn")
		self.reactionsTag = getTag("reactions")
		self.initTag = getTag("init")

	def getDictionary(self,reactantString):
		newDict = dict()
		if reactantString == "":
			return newDict
		splitData = reactantString.split("+")
		for reactant in splitData:
			reac = reactant.strip()
			name,coeff = getNameAndCoeff(reac)
			if name in self.absenseDictionary:
				newDict[name]=coeff,True
			else:
				newDict[name]=coeff,False
		return newDict


	def getReactantDictionary(self,reactionString):
		splitData = reactionString.split("->")
		return self.getDictionary(splitData[0].strip())

	def getProductDictionary(self,reactionString):
		splitData = reactionString.split("->")
		return self.getDictionary(splitData[1].strip())

	def addAbsence(self,absenseString):
		splitData = absenseString.split("->")
		chemical_name = splitData[0].strip()
		absense_chemical_name = splitData[1].strip()
		self.absenseDictionary[chemical_name] = absense_chemical_name

	def addReaction(self,reactionString,rateConstant):
		reactDict = self.getReactantDictionary(reactionString)
		prodDict = self.getProductDictionary(reactionString)

		reactionTag = ET.SubElement(self.reactionsTag,"reaction",rate_constant=str(rateConstant))

		for reactant in reactDict:
			coefficient,isAbsense = reactDict[reactant]
			if isAbsense:
				ET.SubElement(reactionTag,"reactant",name=reactant,coeff=coefficient,absense_name=self.absenseDictionary[reactant])
			else:
				ET.SubElement(reactionTag,"reactant",name=reactant,coeff=coefficient)

		for prod in prodDict:
			coefficient,isAbsense = prodDict[prod]
			ET.SubElement(reactionTag,"product",name=prod,coeff=coefficient)

	def writeXMLToFile(self,filePath):
		self.crnTag.append(self.reactionsTag)
		self.crnTag.append(self.initTag)
		tree = ET.ElementTree(self.crnTag)
		tree.write(filePath)

	def addInitConcentration(self,initString):
		splitData = initString.split("->")
		chemical_name = splitData[0].strip()
		initConcentration = splitData[1].strip()
		ET.SubElement(self.initTag,"chemical",name=chemical_name,val=initConcentration)