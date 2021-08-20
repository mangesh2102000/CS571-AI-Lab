from puzzle import Puzzle, heuristicFuncList
from heapq import heappush, heappop

class Astar:
	#f(n) = g(n)+h(n)
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
		pq = []
		f_n = 0 + self.heuristicFunc(self.puzzle)
		self.distance[self.puzzle] = 0
		node = self.Node(f_n, self.puzzle)
		heappush(pq, node)

		curr_node = None
		while pq:
			vertex = heappop(pq)
			g_n = vertex.value - self.heuristicFunc(vertex.puzzle)
			if self.distance[vertex.puzzle] < g_n:
				continue
			self.exploredStates += 1

			if vertex.puzzle.isGoal():
				curr_node = vertex
				break

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
				if newPuzzle not in self.distance:
					self.distance[newPuzzle] = g_n+1
					f_n = g_n+1+self.heuristicFunc(newPuzzle)
					node = self.Node(f_n,newPuzzle,vertex)
					heappush(pq, node)

				elif g_n+1 < self.distance[newPuzzle]:
					self.distance[newPuzzle] = g_n+1
					f_n = g_n+1+self.heuristicFunc(newPuzzle)
					node = self.Node(f_n,newPuzzle,vertex)
					heappush(pq, node)

		path = []
		while curr_node:
			path.append(curr_node.puzzle)
			curr_node = curr_node.parent

		return path



a = [[1,2,3],[4,5,6],[7,0,8]]
p = Puzzle(a)

astars = []
for heuristic, heuristicFunc in heuristicFuncList.items():
	astars.append(Astar(heuristic,heuristicFunc,p))

paths = [astar.run() for astar in astars]

for idx, path in enumerate(paths):
	print(astars[idx].heuristic,"heuristics' explored states:",astars[idx].exploredStates)
	path.reverse()
	if not path:
		print("No path available")
	for step in path:
		print(step)
	print("------------------------------")
