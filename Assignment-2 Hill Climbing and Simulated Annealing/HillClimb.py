# Simulated Annealing Algorithm

# Import Required Functionalities 
from puzzle import Puzzle, heuristicFuncList
from heapq import heappush, heappop
from time import time

class HillClimbing:
	# Cost Function = h(n)
	def __init__(self,heuristic,heuristicFunc,puzzle):
		self.heuristic = heuristic
		self.heuristicFunc = heuristicFunc
		self.puzzle = puzzle
		self.distance = {}
		self.exploredStates = 0

	class Node:
		# value is h(n) as per problem statement, will be used to compare nodes
		# puzzle is the puzzle configuration
		# parent is the parent node, used to find the path
		def __init__(self, value, puzzle, parent=None):
			self.puzzle = puzzle
			self.parent = parent
			self.value = value

		def __lt__(self, other):
			return self.value < other.value

		def findNeighbours(self):
			blankX, blankY = Puzzle.findCell(self.puzzle.puzzleConfig, 0)
			swap_pos = [(-1,0),(1,0),(0,1),(0,-1)]

			neighbours = []
			for dx, dy in swap_pos:
				newX = dx + blankX
				newY = dy + blankY

				if(newX < 0 or newY < 0 or newX == 3 or newY == 3):
					continue

				newPuzzle = currNode.puzzle.newConfig(blankX,blankY,newX,newY)
				neighbours.append(newPuzzle)

			return neighbours



	def run(self):

		start_time = time()
		h_n = self.heuristicFunc(self.puzzle)
		self.distance[self.puzzle] = 0
		currNode = self.Node(h_n, self.puzzle)

		while currNode:			
			# Goal State Reached
			if currNode.puzzle.isGoal():
				break

			# Increment count of Explored States
			self.exploredStates += 1
			g_n = self.distance[currNode.puzzle]

			#explore adjacent nodes
			neighbours = currNode.findNeighbours()

			bestNode = None
			for newPuzzle in neighbours:
				if newPuzzle in self.distance:
					continue
				h_n = self.heuristicFunc(newPuzzle)
				newNode = self.Node(h_n, newPuzzle, currNode)

				if bestNode and newNode <= bestNode:
					bestNode = newNode

				elif not bestNode and newNode <= currNode:
					bestNode = newNode

			currNode = bestNode
			if currNode:
				self.distance[currNode.puzzle] = g_n + 1


		# Store path from START_STATE to GOAL_STATE if exists
		path = []
		while currNode:
			path.append(currNode.puzzle)
			currNode = currNode.parent

		# Calculate execution time
		exec_time = time()-start_time

		return exec_time, path
