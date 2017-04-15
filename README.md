# chemical_reaction_simulator
It is a ideal simulator for simulating chemical reactions in chemical reaction network. 

Assumptions of Ideal Simulator :
* At every time step it will make a list of possible reactions that can occur.
* Out of this possible reactions, it will pick the fastest one means one which has the highest rate constant.
* If there are no reactions in step 2 , then simulation will terminate.

It accepts the input of chemical reaction network as a xml file.

To run the Chemical World type command "python ReactionMaker/MainFrame.py"