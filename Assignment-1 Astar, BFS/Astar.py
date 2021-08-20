from puzzle import Puzzle, heuristicFuncList

class Astar:
	def __init__(self,heuristic,heuristicFunc,puzzle):
		self.heuristic = heuristic
		self.heuristicFunc = heuristicFunc
		self.puzzle = puzzle

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

	


# a = [[1,4,3],[2,5,6],[8,7,0]]
# p = Puzzle(a)

# for heuristic, heuristicFunc in heuristicFuncList.items():
# 	print(f"{heuristic}:", heuristicFunc(p))

