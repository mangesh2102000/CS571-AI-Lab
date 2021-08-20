from puzzle import Puzzle, heuristicFuncList
from heapq import heappush, heappop

class BFS:
	#f(n) = h(n)
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
		f_n = self.heuristicFunc(self.puzzle)
		self.distance[self.puzzle] = 0
		node = self.Node(f_n, self.puzzle)
		heappush(pq, node)

		curr_node = None
		while pq:
			vertex = heappop(pq)
			# g_n = vertex.value - self.heuristicFunc(vertex.puzzle)
			if vertex.parent == None:
				g_n = 0
			else :
				g_n = self.distance[vertex.parent.puzzle] + 1

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
					# f_n = g_n+1+self.heuristicFunc(newPuzzle)
					f_n = self.heuristicFunc(newPuzzle)
					node = self.Node(f_n,newPuzzle,vertex)
					heappush(pq, node)

				elif g_n+1 < self.distance[newPuzzle]:
					self.distance[newPuzzle] = g_n+1
					# f_n = g_n+1+self.heuristicFunc(newPuzzle)
					f_n = self.heuristicFunc(newPuzzle)
					node = self.Node(f_n,newPuzzle,vertex)
					heappush(pq, node)

		path = []
		while curr_node:
			path.append(curr_node.puzzle)
			curr_node = curr_node.parent

		return path



a = [[8,3,5],[4,1,6],[2,7,0]]
p = Puzzle(a)

BFSs = []
for heuristic, heuristicFunc in heuristicFuncList.items():
	BFSs.append(BFS(heuristic,heuristicFunc,p))

paths = [BFS.run() for BFS in BFSs]

for idx, path in enumerate(paths):
	print(BFSs[idx].heuristic,"heuristics' explored states:",BFSs[idx].exploredStates)
	path.reverse()
	if not path:
		print("No path available")
	for step in path:
		print(step)
	print("------------------------------")
