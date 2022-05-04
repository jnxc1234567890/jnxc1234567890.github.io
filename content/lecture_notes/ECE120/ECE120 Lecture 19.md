---
title: "ECE120 Lecture 19 - FSM and Binary Counter"
---

## FSM
### Definition of FSM
A **Finite State Machine** consists of five parts:
1. Finite set of states
2. Set of inputs
3. Set of outputs(only dependent on state)
4. Set of transition rules
5. Methods for calculating outputs

### Digital FSM
We implement FSM in digital system as sequential logic circuits.

### Keyless Entry Example
#### State Table

| meaning              | state    | driver’s door | other doors | alarm on? |
| -------------------- | -------- | ------------- | ----------- | --------- |
| vehicle locked       | LOCKED   | locked        | locked      | no        |
| driver door unlocked | DRIVER   | unlocked      | locked      | no        |
| all doors unlocked   | UNLOCKED | unlocked      | unlocked    | no        |
| alarm sounding       | ALARM    | locked        | locked      | yes       |

#### Next-State Table

| state  | action/input  | next state |
| ------ | ------------- | ---------- |
| LOCKED | push “unlock” | DRIVER     |
| DRIVER | push “unlock” | UNLOCKED   |
| (any)  | push “lock”   | LOCKED     |
| (any)  | push “panic”  | ALARM      |

#### Abstract State Transition Diagram
![[lecture_notes/ECE120/images/Pasted image 20220414174205.png]]

#### From Abstract to Digital
##### Bit Representation
There're 4 states here, so we only need 2 bits to represent state: $S_{1},S_{0}$
There're three bits required for outputs: $D,R,A$
Similarly, we need 3 bits for inputs as well: $U,L,P$

##### Listing Truth Table for State Table

| meaning              | state    | S1S0 | D   | R   | A   |
| -------------------- | -------- | ---- | --- | --- | --- |
| vehicle locked       | LOCKED   | 00   | 0   | 0   | 0   |
| driver door unlocked | DRIVER   | 10   | 1   | 0   | 0   |
| all doors unlocked   | UNLOCKED | 11   | 1   | 1   | 0   |
| alarm sounding       | ALARM    | 01   | 0   | 0   | 1   |          |          |      |     |     |     |

##### $S_{1}^{+}S_{0}^{+}$ for the Next State
When we're trying to express the next state, we'll use the notation of $S_{1}^{+}S_{0}^{+}$ to represent values in the next clock cycle.
Therefore, our current objective becomes finding the truth table for $S_{1}^{+}S_{0}^{+}$ according to $S_{1},S_{0},U,L,P$.

##### Prioritizing the Buttons

Wait! We encountered a huge problem in filling in this table! Because the table requires us to think about the situations of multiple buttons being pressed.
Don't worry, a simple way to solve this is to list priorities of the buttons.

Our rules:
- Panic has priority! 
- Lock has second priority. 
- Unlock only matters when neither of the others is pressed.

##### Truth Table for $S_{1}^{+}S_{0}^{+}$

Step 1: Panic button

| $S_{1}S_{0}$\\ $ULP$ | 000 | 001 | 011 | 010 | 110 | 111 | 101 | 100 |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| **00**               | -   | 01  | 01  | -   | -   | 01  | 01  | -   |
| **01**               | -   | 01  | 01  | -   | -   | 01  | 01  | -   |
| **11**               | -   | 01  | 01  | -   | -   | 01  | 01  | -   |
| **10**               | -   | 01  | 01  | -   | -   | 01  | 01  | -   |

Step 2: Lock button

| $S_{1}S_{0}$\\ $ULP$ | 000 | 001 | 011 | 010 | 110 | 111 | 101 | 100 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| **00**           | -  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **01**           | -  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **11**           | -  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **10**           | -  | 01  | 01  | 00  | 00  | 01  | 01  | -  |

Step 3: No button

| $S_{1}S_{0}$\\ $ULP$ | 000 | 001 | 011 | 010 | 110 | 111 | 101 | 100 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| **00**           | 00  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **01**           | 01  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **11**           | 11  | 01  | 01  | 00  | 00  | 01  | 01  | -  |
| **10**           | 10  | 01  | 01  | 00  | 00  | 01  | 01  | -  |

Step 4: Unlock button

| $S_{1}S_{0}$\\ $ULP$ | 000 | 001 | 011 | 010 | 110 | 111 | 101 | 100 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| **00**           | 00  | 01  | 01  | 00  | 00  | 01  | 01  | 10  |
| **01**           | 01  | 01  | 01  | 00  | 00  | 01  | 01  | 01  |
| **11**           | 11  | 01  | 01  | 00  | 00  | 01  | 01  | 11  |
| **10**           | 10  | 01  | 01  | 00  | 00  | 01  | 01  | 11  |

Note that when car is fully unlocked, it remains the state. When car is on alarm, pushing unlock button doesn't work.

##### State Transition Diagram
![[lecture_notes/ECE120/images/Pasted image 20220414174502.png]]

## Binary Counter

A FSM without inputs is **counter**. The normal operation of a counter is a loop of states.

### State Transition Diagram for Binary Counter
![[lecture_notes/ECE120/images/Pasted image 20220414174556.png]]

Above is the state transition diagram for a 3-bit binary counter. It starts from 000 to 001 and the loop goes back to 000 from 111.

### Next-state Truth Table

| $S_{2}$ | $S_{1}$ | $S_{0}$ | $S_{2}^{+}$ | $S_{1}^{+}$ | $S_{0}^{+}$ |
| ------- | ------- | ------- | ----------- | ----------- | ----------- |
| 0       | 0       | 0       | 0           | 0           | 1           |
| 0       | 0       | 1       | 0           | 1           | 0           |
| 0       | 1       | 0       | 0           | 1           | 1           |
| 0       | 1       | 1       | 1           | 0           | 0           |
| 1       | 0       | 0       | 1           | 0           | 1           |
| 1       | 0       | 1       | 1           | 1           | 0           |
| 1       | 1       | 0       | 1           | 1           | 1           |
| 1       | 1       | 1       | 0           | 0           | 0            |

From K-Map, we can easily derive that
$$
\begin{align*}
&S_{0}^{+}=S_{0}'=S_{0} \oplus 1\\
&S_{1}^{+}=S_{1}S_{0}'+S_{1}'S_{0}=S_{1}\oplus S_{0}\\
&S_{2}^{+}=S_{2}S_{1}'+S_{2}S_{0}'+S_{2}'S_{1}S_{0}=S_{2}(S_{1}'+S_{0}')+S_{2}'S_{1}S_{0}=S_{2}\oplus (S_{1}S_{0})
\end{align*}
$$

### Synchronous Counters
Now we've got the Boolean expressions, it's time to design the counters.

#### Serial Gating
![[lecture_notes/ECE120/images/Pasted image 20220414174759.png]]
Smaller Area, More Delay

#### Parallel Gating
![[lecture_notes/ECE120/images/Pasted image 20220414174739.png]]
More Area, Smaller Delay

### Ripple Counter
Apart from clocked synchronous sequential circuit, we can also implement counter using ripple design.

![[lecture_notes/ECE120/images/Pasted image 20220414174950.png]]

#### How it works?
![[lecture_notes/ECE120/images/Pasted image 20220414175019.png]]