---
title: "ECE120 Lecture 2 - Numerical Representation"
---

## Unsigned [[lecture_notes/ECE120/ECE120 Lecture 1#Definition for representation|Representation]]
In order to represent an integer, the computer uses base-2 numbers from mathematics (aka. binary).
Due to hardware limitations, we cannot create representations that use arbitrary number of bits. Therefore, we use some fixed numbers of bits to represent a certain group of numbers, which introduced leading 0s.
e.g.
$$
\begin{align}
17_{10}=00010001_2 \\
42_{10}=00101010_2 
\end{align}
$$
### Conversion from Binary to Decimal
The conversion from binary to decimal is quite straight forward, because the $i$th bit in binary represents $2^{i-1}$ .
e.g. Convert $01001_2$
$$
01001_2 = (0 \cdot 2^4 + 1 \cdot 2^3+0 \cdot 2^2+0 \cdot 2^1+1 \cdot 2^0)_{10}=9_{10}
$$

### Conversion from Decimal to Binary
It might not seem so straightforward as the previous one, but the core idea is the same.
e.g. Convert $9_{10}$ to a 5-bit binary.
$$
\begin{align}
&\text{Assume } 9_{10} = a_4\cdot 2^4 + a_3\cdot 2^3 + a_2\cdot 2^2+a_1\cdot 2^1+a_0\cdot2^0. \\
&\text{Clearly, the parity of the number determined }a_0. \\
&(9-a_0) \div 2 = a_4\cdot 2^3 + a_3\cdot 2^2 + a_2\cdot 2^1+a_1\cdot 2^0 \\
&\text{Clearly, the parity of the number determined } a_1. \\
&((9-a_0)-a_1) \div 2=a_4\cdot 2^2 + a_3\cdot 2^1 + a_2\cdot 2^0 \\
&\text{ Clearly, the parity of the number determined } a_2. \\
&\cdots
\end{align}
$$

## Addition of Unsigned Representation
Binary addition is almost the same as decimal addition.
e.g. $01001_2+01110_2$
$$
\begin{align}
_1\quad \quad  &\\
01001&\\
+01110&\\
\hline
10111&
\end{align}
$$
However, sometimes things go wrong.
e.g. $01001_2+11110_2$
$$
\begin{align}
_{1\ 1} \quad \quad  &\\
01001&\\
+11110&\\
\hline
①10111&
\end{align}
$$
Note there is a carry out 1. Because of bit limitation, it did not appear in the final result, causing a mismatch. This kind of phenomena is called overflow.

To sum up, the addition result of $N$ bit binary is
$$
S = (A+B)\mod 2^N
$$

## 2's Complement
Here comes the question, how to store negative numbers?

The easiest way is [[Sign-Magnitude]]. But our topic today focuses on 2's complement representation, which is the most widely used representation in computers nowadays.

The key concept of 2's complement representation is to make use of the same addition component as unsigned representation, which is to say,
$$
\begin{align*}
&\text{For a negative number }-k, \text{ we wish to find its reprentation }P_k.\\
&\text{So that }\forall N \in \mathbb{Z}, \text{we have }(-k+N)\equiv(P_{k}+N) \mod 2^{N}.
\end{align*}
$$
It's easy to find that the appropriate $P_{k}$ should be $2^{N}-k$.

The representation of $P_{k}=2^{N}-k$ is called **2' complement** representation. It has the advantage of using the same addition circuit with unsigned representation.

## Sign-Magnitude (optional)
Sign-Magnitude representation is used 