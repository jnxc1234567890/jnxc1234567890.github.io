---
title: "Infinite Sequence and Series"
---
## Sequence
An infinite sequence is a list of numbers in a definite order. Rigorously speaking, an infinite sequence is a function $f : \mathbb{N}\to\mathbb{R}$. Thus its definition of limit is the same as function's limit and theorems concerning functions apply to it as well (e.g. The Squeeze Theorem).

> **NOTATION**:
> A sequence is usually denoted by:
> $$
\begin{align*}
&\{ a_{1},a_{2},\dots \}&\text{or}&&\{ a_{n} \} &&\text{or}&& \{ a_{n} \}^{\infty}_{n=1}
\end{align*}$$

### Convergence of Sequence

>**DEFINITION**:
>A sequence $\{ a_{n} \}$ is said to be **convergent** if and only if
>$$
\lim_{ n \to \infty } a_{n} = L$$
>In other cases, we say the sequence **diverges**.

### Absolute Value and Convergence to 0
>**THEOREM**:
>$$
\begin{align*}
\lim_{ n \to \infty } \left| a_{n} \right| =0 \implies \lim_{ n \to \infty } a_{n}=0\tag{1}
\end{align*}$$

**PROOF**:
Consider $b_{n}=\left| a_n \right|,\ c_{n}=-\left| a_n \right|$.
Clearly,
$$
c_{n}\leq a_{n}\leq b_{n},\lim_{ n \to \infty } c_{n}=-\lim_{ n \to \infty } b_{n}=0=\lim_{ n \to \infty } b_{n}
$$
By [[The Squeeze Theorem]],
$$
\lim_{ n \to \infty } a_{n}=\lim_{ n \to \infty } c_{n}=\lim_{ n \to \infty } b_{n} = 0
$$
### Convergence of $\{ r^{n} \}$
With some simple calculation, we'll find:
>**Example**:
>The sequence $\{ r^n \}$ is convergent if $-1<r\leq 1$ and divergent for all other values of $r$.
>i.e.
>$$
\lim_{ n \to \infty } r^{n} = \begin{cases}
0 &\text{ if }&-1<r<1 \\
1 &\text{ if }&r=1
\end{cases}$$

### Bounded Sequence
> **DEFINITION**:
> A sequence $\{ a_{n} \}$ is **bounded above** if there is a  number $M$ such that
> $$
\begin{align*}
&a_{n}\leq M &\text{for all }n\geq 1 \\
\end{align*}$$
>It's bounded below if there is a number $m$ such that
>$$
\begin{align*}
&a_{n}\geq  m &\text{for all }n\geq 1 \\
\end{align*}$$
>If it's bounded both above and below, it's a **bounded sequence**.

### Monotonic Sequence Theorem
>**THEOREM**:
>$$
\begin{align*}
\text{Every bounded, monotonic sequence is convergent.}\tag{2}
\end{align*}$$

## Series
An infinite series is the sum of all terms in an infinite sequence.

>**NOTATION**:
>The usual notation for series is Sigma Notation:
>$$
\begin{align*}
&\sum^\infty_{n=1}a_{n} && \text{or} && \sum a_{n}
\end{align*}$$


### Partial Sum and Convergence of Series
>**DEFINITION**:
>The **partial sum** of a series $\sum a_{n}$ is defined by:
>$$
s_{n}=\sum^n_{i=1}a_{i}$$
>If $\{ s_{n} \}$ is convergent, i.e. $\lim_{ n \to \infty } s_{n}=s$, the series $\sum a_{n}$ is called **convergent** and we have
>$$
\sum^\infty_{n=1}a_{n}=s$$
>If $\{ s_{n} \}$ is divergent, the series is divergent.

### Geometric Series
>**Example**:
>The **geometric series**
>$$
\sum^\infty_{n=1}ar^{n-1}=a+ar+ar^2+\dots $$
>is convergent if and only if $\left| r \right| <1$ and and its sum is
>$$
\sum^\infty_{n=1}ar^{n-1}=\frac{a}{1-r}$$

### Harmonic Series

### Test for Divergence
>**THEOREM**:
>$$
\begin{align*}
\sum^\infty_{n=1}a_{n}=s \implies \lim_{ n \to \infty } a_{n}=0\tag{3}
\end{align*}$$

**PROOF**:
Assume $s_{n}=\sum^n_{i=1}a_{i}$, then $a_{n}=s_{n}-s_{n-1}$.
We have:
$$
\lim_{ n \to \infty } a_{n}=\lim_{ n \to \infty } (s_{n}-s_{n-1})=\lim_{ n \to \infty } s_{n}-\lim_{ n \to \infty } s_{n-1}=s-s=0
$$

The contrapositive of [[wikipages/Infinite Sequence and Series#Test for Divergence|(3)]] is called **test for divergence**.

>**THEOREM** (*Test for Divergence*):
>$$
\begin{align*}
\lim_{ n \to \infty } a_{n}\neq 0 \text{ or DNE}\tag{4} \implies \sum^\infty_{n=1}a_{n}\text{ is divergent}
\end{align*}$$

### Absolute Convergence
>**DEFINITION**:
>A series $\sum a_{n}$ is called **absolutely convergent** if $\sum |a_{n}|$ is convergent.
>If $\sum a_{n}$ is convergent and $\sum |a_{n}|$  is divergent we call the series **conditionally convergent**.

Similar to sequence [[wikipages/Infinite Sequence and Series#Absolute Value and Convergence to 0|above]], the absolute value of  series also implies somthing about convergence.
>**THEOREM**:
>$$
\begin{align*}
\sum \left| a_{n} \right| \text{ is convergent}\implies \sum  a_{n}  \text{ is convergent}\tag{5}
\end{align*}$$

**PROOF**:
Obviously, we could have:
$$
0\leq a_{n}+\left| a_{n} \right| \leq 2|a_{n}|
$$
According to [[wikipages/Series Convergence Tests#Comparison Test and Limit Comparison Test|Comparison Test]],
$$
\sum 2|a_{n}| \text{ is convergent}\implies \sum (a_{n}+|a_{n}|) \text{ is convergent}
$$
Notice that
$$\sum a_{n}=\sum (a_{n}+|a_{n}|)-|a_{n}|=\sum (a_{n}+|a_{n}|)-\sum |a_{n}|$$
$\sum a_{n}$ is the difference of two convergent series therefore converges.

### Remainder Estimation
