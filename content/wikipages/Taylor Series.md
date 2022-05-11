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
&&&\text{converges if }\left| x-a \right| <R \text{ and diverges if }\left| x-a \right| >R. \\
&&&(R\text{ is called the radius of convergence of }\sum a_{n}.)
\end{align*}$$

## Derivative and Integral of Power Series
>**THEOREM**:
>If the power series $\sum c_n (x-a)^n$ has radius of convergence $R>0$, then the function defined by
>$$
f(x)=\sum^\infty_{n=0}c_{n}(x-a)^n$$
>is differentiable (and therefore continuous) on the interval $(a-R,a+R)$ and
>$$
\begin{align*}
\text{(i)}&&f'(x)&=\sum^\infty_{n=1}nc_{n}(x-a)^{n-1}\tag{1} \\
\text{(ii)}&&\int f(x) \, dx&=C+\sum^\infty_{n=0} c_{n}\frac{(x-a)^{n+1}}{n+1} \tag{2}
\end{align*}$$

## Taylor Series
Taylor series is a power series used to represent a function.
Assume we have $f(x)=\sum\limits^\infty_{n=0}c_{n}(x-a)^n$.
Then according to Equation (1), we should have
$$
f'(x)=\sum^\infty_{n=1} nc_{n}(x-a)^{n-1}
$$
Continue applying this step
$$
f''(x)=\sum^\infty_{n=2}n(n-1)c_{n}(x-a)^{n-2}
$$
Using mathematical induction, we can get
$$
f^{(i)}(x)=\sum^\infty_{n=i} \frac{n!}{(n-i)!}c_{n}(x-a)^{n-i}
$$
Apply substitution $x=a$ to the expression,
$$
\begin{align*}
f^{(i)}(a)&=\frac{i!}{(i-i)!}c_{i}(a-a)^0+\sum^\infty_{n=i+1} \frac{n!}{(n-i)!}c_{n}(a-a)^{n-i} \\
&=i!\cdot c_{i}\cdot 1+0=i!\cdot c_{i} \\
\end{align*}
$$
Therefore, we have
$$
c_{n}=\frac{f^{(n)}(a)}{n!}
$$

>**THEOREM** (*Taylor Series*):
>If $f$ has a power series representation at $a$, i.e. $f(x)=\sum^\infty_{n=0}c_{n}(x-a)^n$, then the power series must be
>$$
\begin{align*}
\sum^\infty_{n=0} \frac{f^{(n)}(a)}{n!}(x-a)^n&&\text{for }\left| x-a \right| <R\tag{3}
\end{align*}$$
>The series in Equation (3) is called the **Taylor series** of  the function $f$ at $a$.

>**Example** (*Maclaurin Series*):
>By setting $a=0$ to Taylor series, we get the **Maclaurin series**:
>$$
\sum^\infty_{n=0} \frac{f^{(n)}(0)}{n!}x^n\tag{4}$$

## Taylor Polynomial
It is not easy to compute infinite order polynomial (power series) in application. So normally we choose Taylor polynomials.

>**DEFINITION**:
>A $n$th-degree Taylor polynomial is the partial sum of Taylor series.
>$$
T_{n}(x)=\sum^n_{i=0} \frac{f^{(i)}(a)}{i!}x^i$$

Obviously, as $n\to \infty$, $T_{n}(x)$ would become the Taylor series.

## Remainder and Condition of Taylor Series
### Remainder of Taylor Series
The remainder of Taylor series is a bit different from other series because the goal of Taylor series is to approximate a function, not a series.

>**DEFINITION**:
>The **remainder of Taylor series** is the difference of $f(x)$ and $T_{n}(x)$.
>$$
R_{n}(x)=f(x)-T_{n}(x)$$

As $n\to \infty$,
$$
\lim_{ n \to \infty } T_{n}(x)=\lim_{ n \to \infty } [f(x)-R_{n}(x)]=f(x)-\lim_{ n \to \infty } R_{n}(x)
$$
If $\lim_{ n \to \infty } R_{n}(x)=0$, then it is very clear that the Taylor series equals the original function. Therefore, we have the following theorem:
>**THEOREM**:
>If $f(x)=T_{n}(x)+R_{n}(x)$, where $T_{n}$ is the $n$th-degree Taylor polynomial of $f$ at $a$ and
>$$
\begin{aligned}
\lim_{ n \to \infty } R_{n}=0&&\text{for }\left| x-a \right|<R 
\end{aligned}$$
>then $f$ equals to the sum of its Taylor series on the intverval $(x-R,x+R)$.

### Condition of Taylor Series
Note that convergence of a Taylor series does not imply the Taylor series equals the original function. (Contrarily however, if Taylor series equals the original function, then it must be convergent)

A canonical example is as follows
>**Example**:$$
f(x)=\begin{cases}
e^{-\frac{1}{x^2}} &\text{if }x\neq 0 \\
0 &\text{if }x=0
\end{cases}$$
>For this function, the Taylor series is convergent and is constant $0$, which is obviously not the original function.

To summarize, we have to go through these following steps before saying that $f$ equals its Taylor series:
1. The function $f$ must be infinitely differentiable.
2. The Taylor series must be convergent.
3. $\lim_{ n \to \infty } R_{n}(x)=0$

