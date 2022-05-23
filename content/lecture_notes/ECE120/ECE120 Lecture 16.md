---
title: "ECE120 Lecture 16 - Storing a Bit"
---
## Sequential Logic
**Combinational logic** allows us to solve the following type of problem:
- given a set of bits as input
- how can we combine them to produce other sets of bits (Boolean expressions)?

**Sequential logic**:
- stores bits as state
- its behavior depends on the state (the values of the stored bits)

## R'-S' Latch
The **R'-S' latch** is a widely used sequential logic circuit used for storing a bit.

The diagram is as follows:
![[lecture_notes/ECE120/images/Pasted image 20220505001852.png]]

The behavior of an R'-S' latch:

| $\overline{R}$ | $\overline{S}$ | Effect           |
| -------------- | -------------- | ---------------- |
| 1              | 1              | Keep current bit |
| 1              | 0              | Set Q = 1        |
| 0              | 1              | Set P = 1        |
| 0              | 0              | not used         | 

## Gated D Latch
A more common version is called **gated D latch**. D stands for data, WE stands for write enable.

![[lecture_notes/ECE120/images/Pasted image 20220505002704.png]]

| D   | WE  | $\overline{S}$ | $\overline{R}$ | behavior         |
| --- | --- | -------------- | -------------- | ---------------- |
| x   | 0   | 1              | 1              | Keep current bit |
| 1   | 1   | 0              | 1              | Set Q = 1        |
| 0   | 1   | 1              | 0              | Set Q = 0        | 

## Clock Signal
In complex sequential logic circuits, a **clock signal** is usually used to drive the WE inputs of the latches.

## D Flip-flop
We need a circuit that holds its value during an entire clock cycle and only changes its value between two cycles (edges). Clearly, latches won't do the job because when WE=1, they'll alter their value.

The common circuit that serves this purpose is (positive-edge-triggered) **D flip-flop**. The most popular implementation is called *master-slave implementation*,which consists of two D latches.
![[lecture_notes/ECE120/images/Pasted image 20220505004530.png]]

The positive-edge-triggered means that it only changes value on positive (rising) edges, shown in the diagram below.
![[lecture_notes/ECE120/images/Pasted image 20220505004557.png]]

