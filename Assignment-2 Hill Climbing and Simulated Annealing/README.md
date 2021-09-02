
# CS561 - ARTIFICIAL INTELLIGENCE LAB  
## ASSIGNMENT-2: Hill Climbling and Simulated Annealing  

### Group Information  
----------------------
|HEADER|INFORMATION|
|------|-----------|
|GroupID | 1801cs12_1801cs16_1801cs22 | 
|Date | 02/09/2021  |
|1801CS12 | Bablu Kumar  |
|1801CS16 | Mangesh Chandrawanshi|  
|1801CS22 | Hrishabh Raj  |
  
### Contents 

* Hill Climbing Algorithm
	* main.py : driver code
	* puzzle.py : puzzle Class, heuristic functions
	* Utils.py : complementory functions for input/output
	* HillClimb.py : HillClimbing algorithm Class
	* StartState : Input file for start state
	* GoalState : Input file for goal state

* Simulated Annealing Algorithm
	* main.py : driver code
	* puzzle.py : puzzle Class, heuristic functions
	* Utils.py : complementory functions for input/output
	* SimulatedAnnealing.py : SimulatedAnnealing algorithm Class
	* StartState : Input file for start state
	* GoalState : Input file for goal state

### Usage 

Sample Input :
* Hill Climbing
	```
	StartState 
	T8 T3 T5 
	T4 T1 T6 
	T2 T7 B

	GoalState
	T1 T2 T3 
	T8 B T4 
	T7 T6 T5
	
	Note: Avoid extra whitespaces/newlines while providing input throught these files
	```
* Simulated Annealing
	```
	StartState 
	T8 T3 T5 
	T4 T1 T6 
	T2 T7 B

	GoalState
	T1 T2 T3 
	T8 B T4 
	T7 T6 T5
	
	Note: Avoid extra whitespaces/newlines while providing input throught these files
	```

### Execution :
```
python main.py
```
* Hill Climbing
	(Outputs to console)
* Simulated Annealing
	(Outputs to output.txt)

Sample Output :
* Hill Climbing -
	Check test_output.txt in the same folder.
* Simulated Annealing -
	Check output.txt in the same folder.
	

Thank You
