---
title: "Integrals"
---
## Definition of Definite Integral
>**DEFINITION**:
>If $f$ is a function defined for $a<x<b$, we divide the interval $[a,b]$ into $n$ subintervals of euqal width $\Delta x=(b-a)/n$.
>We let $x_0(=a),x_1,x_2,\cdots,x_n(=b)$ be the endpoints of these subintervals and we let $x_1^*,x_2^*,\cdots,x_n^*$ be any sample points in these subintervals, meaning $x_i^*$ lies in the $i$th subinterval $[x_{i-1},x_i]$.
>Then the **definite integral** of $f$ from $a$ to $b$ is
>$$
\int^{b}_{a} f(x) \, dx=\lim_{ n \to \infty } \sum^\infty_{i=1}f(x_{i}^*)\Delta x $$
>provided that this limit exists and gives the same value for all possible choices of sample points.
>If it does exist we say that $f$ is integrable on $[a,b]$.

## The Fundamental Theorem of Calculus
>**THEOREM** (*The Fundamental Theorem of Calculus*):
>**Part I**: If $f$ is continous on $[a,b]$, then the function $g$ defined by
>$$
\begin{align*}
&g(x)=\int ^x_{a}f(t) \, dt &&a\leq x\leq b
\end{align*}$$
>is continous on $[a,b]$ and differentiable on $(a,b)$, and $g'(x)=f(x)$.
>**Part II**: If $f$ is continous on $[a,b]$, then
>$$
\int ^b_{a}f(x) \, dx=F(b)-F(a) $$
>where $F$ is any antiderivative of $f$, i.e. $F'(x)=f(x)$.

## Definition of Indefinite Integral
>**DEFINITION**:
>The **indefinite integral** of a function $f$ is the notation for the *antiderivative* of $f$.
>Thus:
>$$F(x)=\int f(x) \, dx \iff F'(x)=f(x)$$

## Improper Integral
### How improper integral happens?
Recall the definition of [[wikipages/Integrals#Definition of Definite Integral|definite integrals]]. There're some cases that make a definite integral incomputable:
1. The first case is when $a$ or $b$ becomes an infinite number. e.g. $\int^{\infty}_{a}f(x)\mathrm{d}x$
2. The second case is when there is a point $x_{0}\in[a,b]$ that $f(x_{0})$ is not integrable. e.g. $\int^{1}_{0}\frac{1}{x-0.5}\mathrm{d}x$.

### Types of Improper Integrals
#### Type I: Infinite Integrals
##### Case 1: $\int^{\infty}_{a}f(x)\mathrm{d}x$
$$
\begin{align*}
\int^{\infty}_{a}f(x)\mathrm{d}x &= \lim_{t\to\infty} \int^{t}_{a}f(x)\mathrm{d}x
\end{align*}
$$
##### Case 2: $\int^{b}_{-\infty}f(x)\mathrm{d}x$
$$
\int^{b}_{-\infty}f(x)\mathrm{d}x=\lim_{t\to- \infty}\int^{b}_{t}f(x)\mathrm{d}x
$$
##### Case 3: $\int^{\infty}_{-\infty}f(x)\mathrm{d}x$
$$
\begin{align*}
&\int^{\infty}_{-\infty}f(x)\mathrm{d}x=\int^{a}_{-\infty}f(x)\mathrm{d}x+\int^{\infty}_{a}f(x)\mathrm{d}x\\
&\mathrm{The\ left\ integral\ converges\ if\ all\ right\ integrals\ converge.}
\end{align*}
$$

#### Type II: Discontinuous Integral
##### Case 1: $f$ is continuous on $\left[a,b\right)$ and discontinuous at $b$
$$
\int^{b}_{a}{f(x)\mathrm{d}x}=\lim_{t\to b^{-}}{\int^{t}_{a}}{f(x)\mathrm{d}x}
$$

##### Case 2: $f$ is continuous on $(a,b]$ and discontinuous at $a$
$$
\int^{b}_{a}{f(x)\mathrm{d}x}=\lim_{t\to a^{+}}{\int^{b}_{t}}{f(x)\mathrm{d}x}
$$

##### Case 3: $f$ has discontinuity at $c$ and $c \in (a,b)$
$$
\int^{b}_{a}{f(x)\mathrm{d}x}=\int^{c}_{a}{f(x)\mathrm{d}x}+\int^{b}_{c}{f(x)\mathrm{d}x}
$$
