
# CS561 - ARTIFICIAL INTELLIGENCE LAB  
## ASSIGNMENT-5: Parser & Prolog  

### Group Information  
----------------------
|HEADER|INFORMATION|
|------|-----------|
|GroupID | 1801cs12_1801cs16_1801cs22 | 
|Date | 26/10/2021  |
|1801CS12 | Bablu Kumar  |
|1801CS16 | Mangesh Chandrawanshi|  
|1801CS22 | Hrishabh Raj  |
---------------------------

```
Q1)=>

	> python Q1.py
	Enter a Query: (P=>Q)=>((~Q=>P)=>Q)
	Theorem

	> python Q1.py
	Enter a Query: (P)=>(PvQ)
	Theorem

	> python Q1.py
	Enter a Query: (P^Q)=>(PvR)
	Theorem

	> python Q1.py
	Enter a Query: (~P)=>(PvQ)
	Not Theorem
```

```
Q2)=>
	# prolog

	?- ['Q2.pl']

	?- g(M).
	M = b.

	?- halt.
```
