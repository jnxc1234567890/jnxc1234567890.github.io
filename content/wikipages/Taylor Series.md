---
title: "Taylor Series"
---
## Power Series
>**DEFINITION**:
>A **powe series** is an infinite order polynomial, i.e.
>$$
\sum^\infty_{n=0} c_{n}(x-a)^n=c_{0}+c_{1}(x-a)+c_{2}(x-a)^2+\dots $$
>where $x$ is a variable and $c_{n}$ are constants called coefficients.

## Convergence of Power Series
>**THEOREM**:
>For a given power series $\sum^\infty_{n=0}c_{n}(x-a)^n$, there are only three possibilities:
>$$
\begin{align*}
\text{(i)}&&&\text{The series converges only when }x=a. \\
\text{(ii)}&&&\text{The series converges for all }x. \\
\text{(iii)}&&&\text{There is a positive number }R\text{ such that the series} \\
&&&\text{converges if }\left| x-a \right| <R \text{ and diverges if }\left| x-a \right| >R.
\end{align*}$$

## Derivative and Integral of Power Series
>**THEOREM**:
>If the power series $\sum c_n (x-a)^n$ has radius of convergence $R>0$, then the function defined by
>$$
f(x)=\sum^\infty_{n=0}c_{n}(x-a)^n$$
>is differentiable (and therefore continuous) on the interval $(a-R,a+R)$ and
>$$
\begin{align*}
\text{(i)}&&f'(x)&=\sum^\infty_{n=1}nc_{n}(x-a)^{n-1} \\
\text{(ii)}&&\int f(x) \, dx&=C+\sum^\infty_{n=0} c_{n}\frac{(x-a)^{n+1}}{n+1}
\end{align*}$$

## Taylor Series
Taylor series is a power series used to represent a function.
Assume we have $f(x)=\sum\limits^\infty_{n=0}c_{n}(x-a)^n$.
