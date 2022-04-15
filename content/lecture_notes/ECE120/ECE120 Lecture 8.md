---
title: "ECE120 Lecture 8"
---

## MOSFET

All the digital electronics today use MOSFETs.

There're two kinds, named after the charge carrier.

- n(egative)-type
- p(ositive)-type

![[lecture_notes/ECE120/images/Pasted image 20220415113217.png|300]]

<img src="images/Pasted image 20220415113217.png" />

An n-type MOSFET turns on if the Gate voltage exceeds threshold while the p-type do the opposite.

We only need two kinds of voltages to represent binary:

- $0V$ , binary 0
- $V_{dd}$ , binary 1

## CMOS Logic Gate
Gates are mostly based on Complementary MOS (CMOS), which is the **complementary structure** of p-type and n-type MOSFETs.

#### NOT Gate
![[lecture_notes/ECE120/images/Pasted image 20220415113412.png]]
#### NOR Gate
![[lecture_notes/ECE120/images/Pasted image 20220415113358.png]]
#### NAND Gate
![[lecture_notes/ECE120/images/Pasted image 20220415113425.png]]

## Optimization of Boolean Expressions

### What's the best way to write F?
Suppose we have:
$$
F = AB’C + ABC’ + ABC
$$
The function $F$ can also be written in many other ways:
$$
\begin{align*}
&F = AB + AC\\
&F = A (B + C)\\
&\cdots
\end{align*}
$$
How to determine the best way?

As a matter of fact, this is not a valid question. Because when evaluating a method, the metric is important. There're mainly 4 metrics used in logic gate construction.

- area / size / cost
- performance / speed
- power / energy consumption
- complexity / reliability

### Area Heuristics
1. Count literals (A, A’, B, B’, C, C’)
2. Add the number of operations (not including complements for literals).

### Delay(Speed) Heuristics
- Find the maximum number of gates between any input and any output.

### Power and Complexity
These two metrics are beyond our class’ scope. You’ll see power in ECE385.

One heuristic for power uses the fact that current flows when a transistor switches on/off and uses simulation to estimate the number of times that happens. 

Complexity is hard to measure, and is usually based on experience.

### Answer the question above

| From of $F$ | Lits | Ops | Area | Delay |
|    ---    | ---  | --- | ---   | ---  |
| $AB’C + ABC’ + ABC$ | 9 | 4 | 13 | 2 |
| $AB + AC$ | 4 | 3 | 7 | 2 |
| $A (B + C)$ | 3 | 2 | 5 | 2 |

In general, $A (B + C)$ is the winner among all designs!