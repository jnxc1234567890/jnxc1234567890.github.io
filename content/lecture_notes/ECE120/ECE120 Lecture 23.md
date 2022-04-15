---
title: "ECE120 Lecture 23 - From FSM to Computer"
---

## FSM and Code
Theoretically, finite state machines can solve any kinds of problems that computer language codes can solve. (Because computers are also finite state machines!)

Look at the example code below.

```c
int values[10];
int idx;
int min = values[0];
for (idx = 1; 10 > idx; idx = idx + 1) 
{
	if (min > values[idx])
	{
		min = values[idx];
	} 
}
```

How to transform this code into a finite state machine?

## Code Analysis

### Array -> Memory
What does this mean?
```c
int values[10];
```

We created ten 32-bit 2’s complement numbers (ten ints). Such a group is called an array. An **array** is the software analogue of a **memory**.

### Flow Chart
```mermaid
flowchart LR
	start(START)
	init1["min = values[0]"]
	start --> init1
	init2["idx = 1"]
	init1 --> init2
	compare1{"10 > idx?"}
	init2 --> compare1
	compare2{"min > values [idx]?"}
	compare1 -->|TRUE| compare2
	add["idx = idx + 1"]
	compare2 -->|FALSE| add
	add --> compare1
	setmin["min = values[idx]"]
	compare2 -->|TRUE| setmin
	setmin --> add
	done(DONE)
	compare1 -->|FALSE| done
```

