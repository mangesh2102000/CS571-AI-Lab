#This File contains Puzzle class and heuristic function definitions
#For helping the implementation of A-star and BFS algorithms
from copy import deepcopy

class Puzzle:
	#Blank tile is considered to be 0.
	#Matrix size should always be 3x3

	GOAL_STATE = [[1,2,3],[4,5,6],[7,8,0]]

	def __init__(self,puzzleConfig):
		self.puzzleConfig = puzzleConfig

	def __eq__(self, puzzle):
		return self.puzzleConfig == puzzle.puzzleConfig

	def __hash__(self):
		hashValue = 0
		for i in range(3):
			for j in range(3):
				hashValue = hashValue*10 + self.puzzleConfig[i][j]
		return hashValue

	def __str__(self):
		return str(self.puzzleConfig)

	def newConfig(self, X, Y, nX, nY):
		newPuzzle = deepcopy(self)
		newPuzzle.puzzleConfig[X][Y], newPuzzle.puzzleConfig[nX][nY] = newPuzzle.puzzleConfig[nX][nY], newPuzzle.puzzleConfig[X][Y]

		return newPuzzle

	def isGoal(self):
		return Puzzle.GOAL_STATE == self.puzzleConfig

	@staticmethod
	def findCell(puzzleConfig, num):
		for i in range(3):
			for j in range(3):
				if(puzzleConfig[i][j] == num):
					return (i,j)
		return (-1,-1)
	
	@staticmethod
	def legitPuzzle(puzzleConfig):
		count = [0]*9
		for i in range(3):
			for j in range(3):
				if puzzleConfig[i][j] < 0 or puzzleConfig[i][j] > 8:
					return False
				count[puzzleConfig[i][j]] += 1
		for c in count:
			if c != 1:
				return False
		return True

def displaceCost(puzzle: Puzzle):
	num_of_displaced_tiles = 0
	for i in range(3):
		for j in range(3):
			if puzzle.puzzleConfig[i][j] != puzzle.GOAL_STATE[i][j]:
				num_of_displaced_tiles += 1

	return num_of_displaced_tiles

def manhattanCost(puzzle: Puzzle):
	total_cost = 0
	for i in range(1,9):
		x1, y1 = Puzzle.findCell(puzzle.puzzleConfig, i)
		x2, y2 = Puzzle.findCell(puzzle.GOAL_STATE, i)

		total_cost += abs(x1-x2)+abs(y1-y2)
	return total_cost

heuristicFuncList = {
	"displaceCost": displaceCost,
	"manhattanCost": manhattanCost
}

