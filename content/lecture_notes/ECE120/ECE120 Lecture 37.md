---
title: "ECE120 Lecture 37 - Microprogrammed Control Unit Design"
---
## Microprogrammed Design
We have discussed the possibilities of using hardwired design for LC-3 in [[lecture_notes/ECE120/ECE120 Lecture 36|the previous lecture]]. But there's a simpler design other than hardwiring.

Notice the 3 FETCH states are always the same for all the instructions. Besides, many instructions clearly have the same operations. Therefore, we can assign state IDs to these states and ignoring interrupts and privilege, we only need 5 bits.



## Patt and Patel Control Unit


## Extending LC-3 ISA
