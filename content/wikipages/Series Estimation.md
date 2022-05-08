---
title: "Series Estimation"
---
## Integral Test Remainder Estimation
>**THEOREM**:
>Suppose $f(k)=a_k$, where $f$ is a continuous, positive, decreasing function for $x\geq n$ and $\sum a_{n}=s$ is convergent. If $R_n=s-s_n$, where $s_n$ is the partial sum, then
>$$
\int _{n+1}^\infty f(x) \, dx \leq R_{n}\leq \int ^\infty_{n}f(x) \, dx $$

With this theorem, we got a better way to evaluate $\sum a_{n}$ compared with $\sum ^n_{i=0}a_{i}$:
$$
\sum^n_{i=0}a_{i}+\int _{n+1}^\infty f(x) \, dx\leq \sum a_{n}\leq \sum^n_{i=0}a_{i}+\int ^\infty_{n}f(x) \, dx  
$$

## Alternating Series Remainder Estimation
>**THEOREM**:
>If the alternating series
>$$
\begin{align*}
&\sum^\infty_{n=1}(-1)^{n-1}b_{n}=b_{1}-b_{2}+b_{3}-b_{4}+\dots&&b_{n}>0 
\end{align*}$$
>satisfies
>$$
\begin{align*}
\text{(i)}&&&b_{n+1}\leq b_{n}&&\text{for all }n \\
\text{(ii)}&&&\lim_{ n \to \infty } b_{n}=0&&
\end{align*}$$
>then
>$$
\left| R_{n} \right| =\left| s-s_{n} \right| \leq b_{n+1}$$

## 