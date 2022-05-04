---
title: "Series Convergence Tests"
---
## Integral Test
>**THEOREM** (*Integral Test*):
>Suppose $f$ is a continous, positive, decreasing function on $[1,\infty)$ and we have $a_{n}=f(n)$. Then the following statements are true:
>$$
\begin{align*}
&(\text{i}) & &\text{If }\int_{1}^{\infty} f(x) \, dx \text{ is convergent, then }\sum ^\infty_{n=1}a_{n} \text{ is convergent}. \\
&(\text{ii}) & &\text{If }\int_{1}^{\infty} f(x) \, dx \text{ is divergent, then }\sum ^\infty_{n=1}a_{n} \text{ is divergent}. \\
\end{align*}$$

## Comparison Test and Limit Comparison Test
>**THEOREM** (*Comparison Test*):
>Suppose $\sum a_{n}$ and $\sum b_{n}$ are series with positive terms.
>$$
\begin{align*}
&\text{(i)} &&\text{If }\sum  b_{n} \text{ is convergent and }a_{n}\leq  b_{n} \text{ for all }n, \\
&&& \text{then }\sum a_{n} \text{ is also convergent.} \\
&\text{(ii)} &&\text{If }\sum  b_{n} \text{ is divergent and }a_{n}\geq b_{n} \text{ for all }n, \\
&&& \text{then }\sum a_{n} \text{ is also divergent.} \\
\end{align*}$$

While Comparison Test applies to many situations where the difference of two series remains positive (resp. negative). Sometimes we have the feeling that two series looks very similar, and that would be Limit Comparison Test.

>**THEOREM** (*Limit Comparison Test*):
>Suppose $\sum a_{n}$ and $\sum b_{n}$ are series with positive terms and
>$$
\lim_{ n \to \infty } \frac{a_{n}}{b_{n}}=c$$
>then either both series converge or both diverge.

## Alternating Series Test
>**THEOREM** (*Alternating Series Test*):
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
>then the series is convergent.

## Ratio and Root Test
>**THEOREM** (*Ratio Test*):
>$$
\begin{align*}
\text{(i)}&&&\text{If $\lim_{ n \to \infty } \left| \frac{a_{n+1}}{a_{n}} \right| =L<1$, then the series $\sum ^\infty _{n=1}a_{n}$}\\
&&&\text{is absolutely convergent (and therefore convergent).} \\
\text{(ii)}&&&\text{If $\lim_{ n \to \infty } \left| \frac{a_{n+1}}{a_{n}} \right| =L>1$, then the series $\sum ^\infty _{n=1}a_{n}$}\\
&&&\text{is divergent.} \\
\text{(iii)}&&&\text{If $\lim_{ n \to \infty } \left| \frac{a_{n+1}}{a_{n}} \right| =1$, the Ratio Test is inconclusive.}\\
\end{align*}$$

>**THEOREM** (*Root Test*):
>$$
\begin{align*}
\text{(i)}&&&\text{If $\lim_{ n \to \infty }  \sqrt[n]{ \left|a_{n}\right| }  =L<1$, then the series $\sum ^\infty _{n=1}a_{n}$}\\
&&&\text{is absolutely convergent (and therefore convergent).} \\
\text{(ii)}&&&\text{If $\lim_{ n \to \infty } \sqrt[n]{ \left|a_{n}\right| } =L>1$, then the series $\sum ^\infty _{n=1}a_{n}$}\\
&&&\text{is divergent.} \\
\text{(iii)}&&&\text{If $\lim_{ n \to \infty } \sqrt[n]{ \left|a_{n}\right| } =1$, the Ratio Test is inconclusive.}\\
\end{align*}$$

## Proofs
