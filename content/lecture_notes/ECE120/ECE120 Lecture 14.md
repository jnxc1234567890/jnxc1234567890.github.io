---
title: "ECE120 Lecture 14"
---

## Power of Two Checker

How to check whether a number is the power of 2? It's very easy for us human to do that because power of 2 has only one 1 bit in binary.

The same applies for a circuit, we just need to check how many 1 bits are there in a number!
We would still use a bit-sliced design (but in **2**-bit sliced). To represent all the situations, we'll need 2 bits.

| C1  | C0  | meaning             |
| --- | --- | ------------------- |
| 0   | 0   | no 1 bits           |
| 0   | 1   | one 1 bit           |
| 1   | 0   | not used            | 
| 1   | 1   | more than one 1 bit |

It's not hard to derive the truth table for this:

| A   | B   | $C_{1}$ | $C_0$ | $Z_1$ | $Z_0$ |
| --- | --- | ------- | ----- | ----- | ----- |
| 0   | 0   | 0       | 0     | 0     | 1     |
| 0   | 0   | 0       | 1     | 0     | 1     |
| 0   | 0   | 1       | 0     | x     | x     |
| 0   | 0   | 1       | 1     | 1     | 1     |
| 0   | 1   | 0       | 0     | 0     | 1     |
| 0   | 1   | 0       | 1     | 1     | 1     |
| 0   | 1   | 1       | 0     | x     | x     |
| 0   | 1   | 1       | 1     | 1     | 1     |
| 1   | 0   | 0       | 0     | 0     | 1     |
| 1   | 0   | 0       | 1     | 1     | 1     |
| 1   | 0   | 1       | 0     | x     | x     |
| 1   | 0   | 1       | 1     | 1     | 1     |
| 1   | 1   | 0       | 0     | 0     | 1     |
| 1   | 1   | 0       | 1     | 1     | 1     |
| 1   | 1   | 1       | 0     | x     | x     |
| 1   | 1   | 1       | 1     | 1     | 1     | 

The expressions should be:
$$
\begin{align*}
&Z_{1}=(C_{1}+A+B)(C_{0}+A)(C_{0}+B)\\
&Z_{0}=C_{0}+A+B=(C_{0}+A)+(C_{0}+B)
\end{align*}
$$

## Upper-case Checker

The final design is about upper-case checker, that is, a circuit checking whether an ASCII character is an upper-case letter.
We assume the input is 7-bit. $C=C_{6}C_{5}C_{4}C_{3}C_{2}C_{1}C_{0}$.

The common Truth table plus K-Map approach doesn't seem to work perfectly here. We have in total of 7 bits!

