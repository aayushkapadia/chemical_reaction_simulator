from PyQt4 import QtCore, QtGui

import ReactionMaker.inversion as inversion
import ReactionMaker.duplicate as duplicate
import ReactionMaker.increment as increment
import ReactionMaker.decrement as decrement
import ReactionMaker.multiply as multiply1
import ReactionMaker.logarithm as logarithm
import ReactionMaker.power as power

import Simulator.XMLParser as XMLParser
import Simulator.plot as plot

from ExpressionSolver.solver import *

def getHistoryFileName(xmlFileName):
	y = xmlFileName[:-3]
	return 'history_' + y + 'txt'

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.addWidgets()

    def addWidgets(self):
		mainMenu=self.menuBar()
		mainMenu.setNativeMenuBar(False)

		# Creating main menus of GUI
		examples=mainMenu.addMenu('Examples')
		simulate= mainMenu.addMenu('Simulate')

		# Creating sub menus of examples menu
		examples.addAction("Basic Examples")
		examples.addAction("Advanced Examples")
		examples.triggered[QtGui.QAction].connect(self.exampletrigger)

		# Creating sub menus of simulate menu
		simulate.addAction("Import XML")
		simulate.addAction("Import txt")
		simulate.addAction("Expression Solver")
		simulate.triggered[QtGui.QAction].connect(self.simulatetrigger)


		# Adding main welcome widget to the screen 
		welcome_widget = WelcomeScreen(self)
		self.central_widget.addWidget(welcome_widget)
		self.central_widget.setCurrentWidget(welcome_widget)

 	# Function for executuing any sub menu choosen from examples menu
    def exampletrigger(self,q):
	    if q.text() == "Basic Examples":
			print q.text()
			basic_widget = BasicWidget(self)
			self.central_widget.addWidget(basic_widget)
			self.central_widget.setCurrentWidget(basic_widget)
	    else:
			print q.text()
			advanced_widget = AdvancedWidget(self)
			self.central_widget.addWidget(advanced_widget)
			self.central_widget.setCurrentWidget(advanced_widget)		

	# Function for executuing any sub menu choosen from simulate menu
    def simulatetrigger(self,q):
		if q.text() =="Expression Solver":

			expression, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Expression :')
		    
			if ok:
				expression=str(expression)
				expression=expression.replace(" ","")
				op_out = []    #This holds the operators that are found in the string (left to right)
				num_out = []   #this holds the non-operators that are found in the string (left to right)
				operators = set('+-*/')
				buff = []
				for c in expression:  #examine 1 character at a time
				    if c in operators:  
				        #found an operator.  Everything we've accumulated in `buff` is 
				        #a single "number". Join it together and put it in `num_out`.
				        num_out.append(''.join(buff))
				        buff = []
				        op_out.append(c)
				    else:
				        #not an operator.  Just accumulate this character in buff.
				        buff.append(c)
				num_out.append(''.join(buff))   
				af=[]
				for i in range(0,len(num_out)):
					af.append(num_out[i])
					if i==len(num_out)-1:
						break   
					af.append(op_out[i])
				for i in range(0,len(af)):
				    if i==0:
				        solver = Solver(int(af[i]))
				    else:
				        if af[i]=="+":
				            solver.add(int(af[i+1]))
				        elif af[i]=="*":
				            solver.multiply(int(af[i+1]))

				solver.printTxt('expression.txt')
				print 'Expression.txt created'
			else:
				return

		if q.text() == "Import XML":
			fname = QtGui.QFileDialog.getOpenFileName(self, 'Select XML to Import','/home')
			print fname
		elif q.text() == "Import txt":
			fname = QtGui.QFileDialog.getOpenFileName(self, 'Select Text file to simulate','/home')
			print fname
		else:
			fname = "expression.txt"

		if q.text() != "Expression Solver":
			simulationtime, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Simulation time:')
		else:
			simulationtime = solver.getEstimatedTimeForCompletion()
			ok = True

		if ok:
			print simulationtime
		else:
			return

		if q.text() != "Expression Solver":
			reactantslist, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Reactants to be plotted seperated by , for eg A,B,C')
			if ok:
				if "," in str(reactantslist):
					reactantslist = str(reactantslist)
					reactantslist = reactantslist.split(",")
					print reactantslist
				else:
					c=[]
					c.append(str(reactantslist))
					reactantslist = c 
					print reactantslist
			else:
				return	    
		else:
			reactantslist = solver.getListOfReactionsToPlot()

		if q.text() == "Import XML":
			print "Plotting From XML File"	
			plot.plotFromXML(fname,int(simulationtime),reactantslist)
		else:
			print "Plotting From Text File"
			plot.plotFromTxt(fname,int(simulationtime),reactantslist)
	    		
class WelcomeScreen(QtGui.QWidget):
    def __init__(self,parent=None):
		super(WelcomeScreen,self).__init__(parent)
		layout=QtGui.QHBoxLayout()
		self.label=QtGui.QLabel('WELCOME!')
		layout.addWidget(self.label)
		self.setLayout(layout)

class BasicWidget(QtGui.QWidget):
    def __init__(self, parent=None):
		super(BasicWidget, self).__init__(parent)
		layout = QtGui.QHBoxLayout()

		self.inversion = QtGui.QPushButton('1) Inversion')
		layout.addWidget(self.inversion)

		self.duplication = QtGui.QPushButton('2) Duplication/Copy')
		layout.addWidget(self.duplication)

		self.decrementation = QtGui.QPushButton('3) Decrementation')
		layout.addWidget(self.decrementation)

		self.incrementation = QtGui.QPushButton('4) Incrementation')
		layout.addWidget(self.incrementation)

		self.setLayout(layout)

		self.inversion.clicked.connect(self.dinversion)
		self.duplication.clicked.connect(self.dduplication)
		self.decrementation.clicked.connect(self.ddecrementation)
		self.incrementation.clicked.connect(self.dincrementation)


    def dinversion(self):
		print "Inversion"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value you want to invert')

		if ok:
			print X
		else:
			return

		outputFileName,chemicalList = inversion.execute(X)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)
		
    def dduplication(self):
		print "Duplicate"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value you want to duplicate')

		if ok:
			print X
		else:
			return

		outputFileName,chemicalList = duplicate.execute(X)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

    def ddecrementation(self):
		print "Decrement"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value you want to decrement 1 from')

		if ok:
			print X
		else:
			return

		outputFileName,chemicalList = decrement.execute(X)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

    def dincrementation(self):
		print "Increment"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value you want to increment 1 to')

		if ok:
			print X
		else:
			return

		outputFileName,chemicalList = increment.execute(X)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

class AdvancedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
		super(AdvancedWidget, self).__init__(parent)
		layout = QtGui.QHBoxLayout()

		self.multiplication = QtGui.QPushButton('1) Multiplication')
		layout.addWidget(self.multiplication)

		self.logarithm = QtGui.QPushButton('2) Logarithm')
		layout.addWidget(self.logarithm)

		self.power = QtGui.QPushButton('3) Power')
		layout.addWidget(self.power)

		self.setLayout(layout)

		self.multiplication.clicked.connect(self.dmultiplication)
		self.logarithm.clicked.connect(self.dlogarithm)
		self.power.clicked.connect(self.dpower)
 
    def dmultiplication(self):
		print "Multiplication"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter first value you want to multiply')

		if ok:
			print X
		else:
			return

		Y, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter second value you want to multiply')

		if ok:
			print Y
		else:
			return

		outputFileName,chemicalList = multiply1.execute(X,Y)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

    def dlogarithm(self):
		print "Ceiling of logarithm"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value you want to take ceiling logarithm of')

		if ok:
			print X
		else:
			return

		outputFileName,chemicalList = logarithm.execute(X)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

    def dpower(self):
		print "Power"

		X, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter value of base')

		if ok:
			print X
		else:
			return

		Y, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter vaue of exponent')

		if ok:
			print Y
		else:
			return

		outputFileName,chemicalList = power.execute(X,Y)

		print 'Result File ' + outputFileName + ' Created'

		timeOfSimulation, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter Time Of Simulation')

		if ok:
			print timeOfSimulation
		else:
			return

		sim = XMLParser.getSimulator(outputFileName)
		sim.simulate(int(timeOfSimulation),getHistoryFileName(outputFileName))
		sim.plot(chemicalList)

app = QtGui.QApplication([])
window = MainWindow()
window.show()
app.exec_()


