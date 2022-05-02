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

### Convergence to 0 and Absolute Value
>**THEOREM**:
>$$
\lim_{ n \to \infty } \left| a_{n} \right| =0 \implies \lim_{ n \to \infty } a_{n}=0$$

**Proof**:
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
The sequence $\{ r^n \}$ is convergent if $-1<r\leq 1$ and divergent for all other values of $r$.
i.e.
$$
\lim_{ n \to \infty } r^{n} = \begin{cases}
0 &\text{ if }&-1<r<1 \\
1 &\text{ if }&r=1
\end{cases}
$$

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
>Every bounded, monotonic sequence is convergent.

## Series
An infinite series is the sum of all terms in an infinite sequence.

>**NOTATION**:
>The usual notation for series is Sigma Notation:
>$$

$$
