import pegSolitaireUtils
import config
import Pegsolitaire
import copy

def RecursiveDLS(fro, pegSolitaireObject, d):
	while len(fro) != 0:
		PegSolitaire1 = copy.deepcopy(pegSolitaireObject)
		cnt=0
		
		
		for i in range(7):
			for j in range(7):
				if PegSolitaire1.gameState[i][j] == PegSolitaire1.goldHolder[i][j]:
					cnt=cnt+1
		
		if cnt == 49:
				return PegSolitaire1	
		pos = list()
		npos = list()
		cpos = list()
		x = fro.pop(0)
		y = fro.pop(0)
		pos.append(x)
		pos.append(y)
		npos.append(x)
		npos.append(y)
		#x = pos [0]
		#y = pos [1]
		
		#fro.append(x+1)
		#fro.append(y)
		if PegSolitaire1.is_validMove(pos, 'E'):
			cpos = PegSolitaire1.getNextPosition(pos, 'E')
			fro.append(cpos[0])
			fro.append(cpos[1])

		if PegSolitaire1.is_validMove(pos, 'N'):
			cpos = PegSolitaire1.getNextPosition(pos, 'N')
			fro.append(cpos[0])
			fro.append(cpos[1])
		if PegSolitaire1.is_validMove(pos, 'W'):
			cpos = PegSolitaire1.getNextPosition(pos, 'W')
			fro.append(cpos[0])
			fro.append(cpos[1])
		if PegSolitaire1.is_validMove(pos, 'S'):
			cpos = PegSolitaire1.getNextPosition(pos, 'S')
			fro.append(cpos[0])
			fro.append(cpos[1])

		#	RecursiveDLS(fro, PegSolitaire1, d - 1)
		if PegSolitaire1.is_validMove(pos, 'E'):
	
						npos = PegSolitaire1.getNextPosition(pos, 'E')
						RecursiveDLS(npos, PegSolitaire1, d - 1)
						PegSolitaire1 = copy.deepcopy(PegSolitaire1.getNextState(pos, 'E'))
						
						
		elif PegSolitaire1.is_validMove(pos, 'N'):
	
						npos = PegSolitaire1.getNextPosition(pos, 'N')
						RecursiveDLS(npos, PegSolitaire1, d - 1)
						PegSolitaire1 = copy.deepcopy(PegSolitaire1.getNextState(pos, 'N'))
						
						
		elif PegSolitaire1.is_validMove(pos, 'W'):
	
						npos = PegSolitaire1.getNextPosition(pos, 'W')
						RecursiveDLS(npos, PegSolitaire1, d - 1)
						PegSolitaire1 = copy.deepcopy(PegSolitaire1.getNextState(pos, 'W'))
						
						
		elif PegSolitaire1.is_validMove(pos, 'S'):
	
						npos = PegSolitaire1.getNextPosition(pos, 'S')
						RecursiveDLS(npos, PegSolitaire1, d - 1)
						PegSolitaire1 = copy.deepcopy(PegSolitaire1.getNextState(pos, 'S'))
						
			
		RecursiveDLS(fro, PegSolitaire1, d - 1)
		cnt=0				
		for i in range(7):
			for j in range(7):
				if PegSolitaire1.gameState[i][j] == PegSolitaire1.goldHolder[i][j]:
					cnt=cnt+1
		if cnt == 49:
			return PegSolitaire1
	

    	    		   
def DepthLimitedSearch(pegSolitaireObject,d):
	# pick some valid start position here 
	PegSolitaire1 = pegSolitaireObject
	depth = d
	fronti = list()
	#for i in range(7):
	#	for j in range(7):
	#		fronti.append(i)
	#		fronti.append(j)
	fronti.append(0)
	fronti.append(0)
	fronti.append(0)
	fronti.append(1)
	posoutcomes= RecursiveDLS(fronti, PegSolitaire1, d)
	return posoutcomes	  

	
def ItrDeepSearch(pegSolitaireObject):

	# code the goal check condition here
	for d in range(7):
	    result_state = DepthLimitedSearch(pegSolitaireObject, 7)
	if (result_state == pegSolitaireObject.goldHolder):
		print ("goal")
		return
	return
	
	#else:
	#	continue #goal is found
		#else continue for further depth






def aStarOne(pegSolitaireObject):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        #
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you
	# reach goal using A-Star searching with first Heuristic
	# you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################
	return True

def aStarTwo(pegSolitaireObject):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        #
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you
        # reach goal using A-Star searching with second Heuristic
        # you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################
	return True
