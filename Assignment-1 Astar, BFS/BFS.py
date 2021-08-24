# Best First Search (BFS) Algorithm

# Import Required Functionalities 
from puzzle import Puzzle, heuristicFuncList
from heapq import heappush, heappop
from time import time

class BFS:
	# Cost Function f(n) = h(n)
	def __init__(self,heuristic,heuristicFunc,puzzle):
		self.heuristic = heuristic
		self.heuristicFunc = heuristicFunc
		self.puzzle = puzzle
		self.distance = {}
		self.exploredStates = 0

	class Node:
		# value is f(n) as per problem statement, will be used in minHeap
		# puzzle is the puzzle configuration
		# parent is the parent node, used to find the path
		def __init__(self, value, puzzle, parent=None):
			self.puzzle = puzzle
			self.parent = parent
			self.value = value

		def __lt__(self, other):
			return self.value < other.value

	def run(self):

		start_time = time()
		pq = []
		f_n = self.heuristicFunc(self.puzzle)
		self.distance[self.puzzle] = 0
		node = self.Node(f_n, self.puzzle)
		heappush(pq, node)

		curr_node = None
		while pq:
			vertex = heappop(pq)
			if vertex.parent == None:
				g_n = 0
			else :
				g_n = self.distance[vertex.parent.puzzle] + 1

			# Skip to next Node(state) if current selection is suboptimal
			if self.distance[vertex.puzzle] < g_n:
				continue

			# Goal State Reached
			if vertex.puzzle.isGoal():
				curr_node = vertex
				break

			# Increment count of Explored States
			self.exploredStates += 1

			#explore adjacent nodes
			#find blank cell
			blankX, blankY = Puzzle.findCell(vertex.puzzle.puzzleConfig, 0)

			swap_pos = [(-1,0),(1,0),(0,1),(0,-1)]
			for dx, dy in swap_pos:
				newX = dx + blankX
				newY = dy + blankY

				if(newX < 0 or newY < 0 or newX == 3 or newY == 3):
					continue

				newPuzzle = vertex.puzzle.newConfig(blankX,blankY,newX,newY)
				
				if newPuzzle in self.distance:
					continue

				if newPuzzle not in self.distance:
					self.distance[newPuzzle] = g_n+1
					f_n = self.heuristicFunc(newPuzzle)
					node = self.Node(f_n,newPuzzle,vertex)
					heappush(pq, node)

		# Store path from START_STATE to GOAL_STATE if exists
		path = []
		while curr_node:
			path.append(curr_node.puzzle)
			curr_node = curr_node.parent

		# Calculate execution time
		exec_time = time()-start_time
		
		return exec_time, path
