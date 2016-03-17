import readGame
import copy
#######################################################
# These are some Helper functions which you have to use
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_corner(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################
class game:

	def __init__(self, filePath):
		self.gameState = readGame.readGameState(filePath)
		self.nodesExpanded = 0
		self.trace = []
		self.goldHolder = [[-1,-1, 0, 0, 0,-1,-1], [-1,-1, 0, 0, 0,-1,-1], [ 0, 0, 0, 0, 0, 0, 0], [ 0, 0, 0, 1, 0, 0, 0], [ 0, 0, 0, 0, 0, 0, 0], [-1,-1, 0, 0, 0,-1,-1], [-1,-1, 0, 0, 0,-1,-1]]

	# pos, newPos and oldPos pass are list and not tuples !
	def is_corner(self, pos):
		# if position is out of board, we term it as corner ! The term corner is little abused here !
		if(pos[0] < 0 or pos[0] > 6 or pos[1] < 0 or pos[1] > 6):
			return True
		elif(self.gameState[pos[0]][pos[1]] == -1):
			return True
		else:
			return False

	def getNextPosition(self, oldPos, direction):
		#########################################
		# YOU HAVE TO MAKE CHANGES HERE
		# See DIRECTION dictionary in config.py and add
		# this to oldPos to get new position of the peg if moved
		# in given direction , you can remove next line
		
		newPos = [oldPos[0],oldPos[1]];
		
		if(direction == 'E'):
			newPos[1] = oldPos[1] + 1
		elif(direction == 'W'):
			newPos[1] = oldPos[1] - 1
		elif(direction == 'N'):
			newPos[0] = oldPos[0] - 1
		elif(direction == 'S'):
			newPos[0] = oldPos[0] + 1
		

		return newPos 
	
	
	def is_validMove(self, oldPos, direction):
		#########################################
		# DONT change Things in here
		# In this we have got the next peg position and
		# below lines check for if the new move is a corner
		
		newPos = self.getNextPosition(oldPos, direction)
		newPos = self.getNextPosition(newPos, direction)
		if self.is_corner(newPos):
			
			return False
		elif(direction == 'E'):
			if(self.gameState[oldPos[0]][oldPos[1] + 1] == 1 and self.gameState[oldPos[0]][oldPos[1] + 2] == 0):
				return True
			else:
				
				return False
		elif(direction == 'W'):
			if(self.gameState[oldPos[0]][oldPos[1] - 1] == 1 and self.gameState[oldPos[0]][oldPos[1] - 2] == 0):
				return True
			else:
				
				return False
		elif(direction == 'N'):
			if(self.gameState[oldPos[0] - 1][oldPos[1]] == 1 and self.gameState[oldPos[0] - 2][oldPos[1]] == 0):
				return True
			else:
				
				return False
		elif(direction == 'S'):
			if(self.gameState[oldPos[0] + 1][oldPos[1]] == 1 and self.gameState[oldPos[0] + 2][oldPos[1]] == 0):
				return True
			else:
				
				return False
		else: 
			return False

	def getNextState(self, oldPos, direction):
		###############################################
		# DONT Change Things in here
		self.nodesExpanded += 1
		if not self.is_validMove(oldPos, direction):
			print ("Error, You are not checking for valid move")
			exit(0)
		###############################################
		else: # it is valid move, proceed for state update
			if(direction == 'E'):
		
				self.gameState[oldPos[0]][oldPos[1]    ] = 0
				self.gameState[oldPos[0]][oldPos[1] + 1] = 0
				self.gameState[oldPos[0]][oldPos[1] + 2] = 1
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1])
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1] + 2)
		
			if(direction == 'W'):
		
				self.gameState[oldPos[0]][oldPos[1]    ] = 0
				self.gameState[oldPos[0]][oldPos[1] - 1] = 0
				self.gameState[oldPos[0]][oldPos[1] - 2] = 1
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1])
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1] - 2)
		
			if(direction == 'N'):
		
				self.gameState[oldPos[0]    ][oldPos[1]] = 0
				self.gameState[oldPos[0] - 1][oldPos[1]] = 0
				self.gameState[oldPos[0] - 2][oldPos[1]] = 1
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1])
				self.trace.append(oldPos[0] - 2)
				self.trace.append(oldPos[1])
		
			if(direction == 'S'):
		
				self.gameState[oldPos[0]    ][oldPos[1]] = 0
				self.gameState[oldPos[0] + 1][oldPos[1]] = 0
				self.gameState[oldPos[0] + 2][oldPos[1]] = 1
				self.trace.append(oldPos[0])
				self.trace.append(oldPos[1])
				self.trace.append(oldPos[0] + 2)
				self.trace.append(oldPos[1])
		
		return self

