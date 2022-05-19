---
title: "Techniques of Integration"
---
## Substitution Rule
The most widely known integration technique must be the substitution rule.
### Chain Rule to Substitution Rule
We all well know about [[Chain Rule]] in differentiation:
$$
\begin{align*}
\frac{d}{dx}f(\varphi(x)) &=f'(\varphi(x))\cdot \varphi'(x) \tag{1}
\end{align*}
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
>**THEOREM** (*Substitution Rule*):
>$$
\begin{align*}
&\int f(\varphi(x))\varphi'(x)\ dx \xlongequal{u=\varphi(x)} \int f(u) \ du \tag{2}
\end{align*}$$

## Integration by Parts
From the Product Rule, we know that
$$
\frac{d}{dx}(uv)=\frac{du}{dx}v+u\frac{dv}{dx}
$$
Integrating both parts and we get
$$
\begin{align*}
\int \frac{d}{dx}(uv) \, dx&=\int v \frac{du}{dx} \, dx+\int u \frac{dv}{dx} \, dx\\
uv&=\int v \, du+\int u \, dv  
\end{align*}
$$
>**THEOREM** (*Integration by Parts*):
>$$
\int v \, du=uv-\int u \, dv  $$
>Definite form:
>$$
\int _{a}^b f(x)g'(x) \, dx=f(x)g(x) ]^b_{a} -\int _{a}^b g(x)f'(x) \, dx $$

## Trigonometric Integrals
We usually meet trigonometric forms like $\int \sin^m(x)\cos^n(x) \, dx$. In fact, we have a strategy for such integrals.

>**Strategy**:
>1. If the power of cosine is odd ($n=2k+1$), substitute one cosine.
>$$
\begin{align*}
\int \sin^mx\cos^{2k+1}x \, dx&=\int \sin^m x\cos^{2k}x\cdot \cos x \, dx\\
&=\int \sin^m x \cos^{2k}x \, d\sin x\\
&=\int \sin^m x(\cos^2x)^k \, d\sin x\\
&=\int \sin^m x(1-\sin^2 x)^k \, d\sin x 
\end{align*}$$
>2. If the power of sine is odd ($m=2k+1$), substitute one sine.
>$$
\begin{align*}
\int \sin^{2k+1}x\cos^nx \, dx&=\int \sin^{2k} x\cos^nx\cdot \sin x \, dx\\
&=-\int \sin^{2k} x \cos^nx \, d\cos x\\
&=-\int (\sin^2 x)^k\cos^nx \, d\cos x\\
&=-\int (1-\cos^2x)^k \cos^nx \, d\cos x 
\end{align*}$$
>3. If both powers are even, consider half-angle identities
>$$
\begin{align*}
\sin^2x=\frac{1}{2}(1-\cos 2x)&&\cos^2x=\frac{1}{2}(1+\cos2x)
\end{align*}$$

One of the important reasons why we can do this is because $\sin^2$ and $\cos^2$ can be transformed from each other. A similar senerio happens on $\tan$ and $\sec$:
$$
\sec^2x=1+\tan^2x
$$
Thus, we have the following strategy for evaluating $\int \tan^mx\sec^nx \, dx$.

>**Strategy**:
>1. If the power of secant is even ($n=2k,k\geq 2$), substitute $\sec^2$ and use identity.
>$$
\begin{align*}
\int \tan^mx\sec^{2k}x \, dx&=\int \tan^mx\sec^{2k-2}x\sec^2x \, dx\\
&=\int \tan^mx(\sec^2x)^{k-1} \, d\tan x\\
&=\int \tan^mx(1+\tan^2x)^{k-1} \, d\tan x 
\end{align*}$$
>2. If the power of tangent is odd ($m=2k+1$), substitute $\sec\tan$ and use identity.
>$$
\begin{align*}
\int \tan^{2k+1}x\sec^{n}x \, dx&=\int \tan^{2k}x\sec^{n}x\sec x\tan x \, dx\\
&=\int (\tan^2x)^k\sec^n x \, d\sec x\\
&=\int (\sec^2x-1)^k\sec^nx \, d\sec x 
\end{align*}$$
>3. For other situations, the guideline is not clear.

## Trigonometric Substitution
If we write out the expression of $y=f(x)$ for a circle $\mathcal{C}: x^2+y^2=r^2$, we'll get $y=\sqrt{ r^2-x^2 }$, this reveals the connection between $\sqrt{ r^2-x^2 }$ and trigonometric functions.

If we substitute $x$ with $r\sin\theta$, $\sqrt{ r^2-x^2 }=r \cos\theta$, $dx=r\cos\theta d\theta$. The integral $\int \sqrt{ r^2-x^2 } \, dx$ becomes
$$
\int r\cos\theta \, d(r\sin\theta)=\int r^2\cos^2\theta \, d\theta
$$

This technique is extremely important in solving radical integrals. And we can conclude a more general case:

>**Strategy**:
>1. $\sqrt{ a^2-x^2 }$: $x=a\sin\theta$
>2. $\sqrt{ a^2+x^2 }$: $x=a\tan\theta$
>3. $\sqrt{ x^2-a^2 }$: $x=a\sec\theta$

## Partial Fraction
Partial fraction is derived