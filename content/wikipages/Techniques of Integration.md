---
title: "Techniques of Integration"
---
## Substitution Rule
The most widely known integration technique must be the substitution rule.
### Chain Rule to Substitution Rule
We all well know about [[Chain Rule]] in differentiation:
$$
\begin{align}
\frac{d}{dx}f(\varphi(x)) &=f'(\varphi(x))\cdot \varphi'(x) &(1)
\end{align}
$$
The chain rule, after some modification, would become substitution rule.
$$
\begin{align*}
&\text{Assume }F'(x)=f(x),\\
&\begin{aligned}
\frac{d}{dx}F(\varphi(x))&=f(\varphi(x))\varphi'(x)\\
\int \frac{d}{dx}F(\varphi(x))\ dx&=\int f(\varphi(x))\varphi'(x)\ dx\\
F(\varphi(x))&=\int f(\varphi(x))\varphi'(x)\ dx\\
\int f(\varphi(x))\varphi'(x)\ dx&=\int f(\varphi(x))\ d\varphi(x) 
\end{aligned}
\end{align*}
$$
Finally, we can conclude that:
$$
\begin{align}
&\int f(\varphi(x))\varphi'(x)\ dx \xlongequal{u=\varphi(x)} \int f(u) \ du &(2)
\end{align}
$$

### Useful Techniques
#### Forward Substitution
The most direct substitution is to find possible $\varphi'(x)$ and substitute using $u=\varphi(x)$.
Examples:
1. 
$$
\int f(ax+b)\ dx\xlongequal{u=ax+b}\frac{1}{a}\int f(u)\ du
$$
2. 
$$

$$
#### Backward Substitution

## Integration by Parts

## Trigonometric Integrals

## Trigonometric Substitution

## Partial Fraction