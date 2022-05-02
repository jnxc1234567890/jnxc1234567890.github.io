---
title: "Integrals"
---
## Definition of Definite Integral
$$
\boxed{
\begin{align*}
&\mathrm{ If\ } f\ \mathrm{is\ a\ function\ defined\ for\ }a < x < b, \mathrm{we\ divide\ the\ interval\ } [a, b]\\
&\mathrm{into\ } n\ \mathrm{subintervals\ of\ equal\ width\ } \Delta x = (b-a)/n.\\
&\mathrm{We\ let}\ x_{0}(=a), x_{1}, x_{2}, \cdots , x_{n} (=b) \mathrm{be\ the\ endpoints\ of\ these\ }\\
& \mathrm{subintervals\ and\ we\ let}\ x_{1}^{*}, x_{2}^{*},\cdots, x_{n}^{*}\ \mathrm{be\ any\ sample\ points\ in}\\\
& \mathrm{these\ subintervals\ ,\\
so}\ x_{i}^{*}\ \mathrm{lies\ in\ the\ }  i \mathrm{th\ subinterval}\ [x_{i-1}, x_{i}].\\
& \mathrm{Then\ the\ definite\ integral\ of}\ f\ \mathrm{from}\ a\ \mathrm{to}\ b\ \mathrm{is}\\
&\int_{a}^{b}{f(x) \mathrm{d}x}=\lim_{n\to\infty}\sum\limits_{i=1}^{n}f(x_{i}^{*})\Delta x\\
&\mathrm{provided\ that\ this\ limit\ exists\ and\ gives\ the\ same\ value\ for\ all\ } \\
&\mathrm{possible\ choices\ of\ sample\ points.} \\
&\mathrm{If\ it\ does\ exist\, we\ say\ that\ } f\ \mathrm{ is\ integrable\ on\ } [a, b].
\end{align*}
}
$$
## Definition of Indefinite Integral

## Fundamental Rules of Calculus


## Improper Integral
### How improper integral happens?
Recall the definition of [[wikipages/Integrals#Definition of Definite Integral|definite integrals]]. There're some cases that make a definite integral incomputable:
1. The first case is when $a$ or $b$ becomes an infinite number. e.g. $\int^{\infty}_{a}f(x)\mathrm{d}x$
2. The second case is when there is a point $x_{0}\in[a,b]$ that $f(x_{0})$ is not integrable. e.g. $\int^{1}_{0}\frac{1}{x-0.5}\mathrm{d}x$

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
