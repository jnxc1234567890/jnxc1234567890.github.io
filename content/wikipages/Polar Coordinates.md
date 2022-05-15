---
title: "Polar Coordinates"
---
## Polar Coordinates
>**DEFINITION**:
>We choose a point in the plane that is called the **pole** (or origin) and is labeled $O$. Then we draw a ray (half-line) starting at $O$ called the **polar axis**.
>If $P$ is any other point in the plane, let $r$ be the distance from $O$ to $P$ and let $\theta$ be the angle (usually measured in radians) between the polar axis and the line $OP$.
>The point $P$ is represented by the ordered  pair $(r,\theta)$,called **polar coordinates** of P.

## Transformation of Polar and Cartesian Coordinates
>**THEOREM**:
>Suppose a polar coordinate $(r,\theta)$ and a Cartesian coordinate $(x,y)$ have the same origin (pole) and the polar axis is the x-axis.
>Then the transformation from polar coordinates to Cartesian coordinates is:
>$$
\begin{align*}
x=r\cos\theta&&y=r\sin\theta\tag{1}
\end{align*}$$
>The transformation from Cartesian coordinates to polar coordinates is:
>$$
\begin{align*}
r^2=x^2+y^2 &&\tan\theta= \frac{y}{x}\tag{2}
\end{align*}$$
>Remind that the two equations give four $(r,\theta)$ but only two of them are valid.

## Symmetry of Polar Curves
Suppose we have a polar curve equation $F(r,\theta)=0$.

1. If $F(r,-\theta)=0$ or $F(-r,\pi-\theta)=0$, the curve is symmetric about the polar axis.
2. If $F(-r,\theta)=0$ or $F(r,\theta+\pi)=0$, the curve is symmetric about the pole.
3. If $F(r,\pi-\theta)=0$ or $F(-r,-\theta)=0$, the curve is symmetric about the vertical line $\theta=\frac{\pi}{2}$.

## Tangents to Polar Curves
>**THEOREM**:
>The tangent to a point $P$ in a polar curve is given by:
>$$
\frac{dy}{dx}=\frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}}=\frac{ \frac{dr}{d\theta}\sin\theta+r\cos\theta }{\frac{dr}{d\theta}\cos\theta-r\sin\theta}$$

## Area in Polar Curves
Remind we have the following formula for the area of a sector
$$
A=\frac{1}{2}r^2\theta
$$
Therefore, by applying the concept of [[wikipages/Integrals#Definition of Definite Integral|Riemann Sum]], we have
$$
A=\lim_{ n \to \infty } \frac{1}{2}[f(\theta^*_{i})]^2\Delta\theta=\int ^b_{a}\frac{1}{2}[f(\theta)]^2 \, d\theta 
$$
>**THEOREM**:
>For $a<\theta<b$, the area bounded by the polar equation $r=f(\theta)$ is
>$$
A=\int _{a}^b \frac{1}{2}r^2 \, d\theta $$

## Arc Length in Polar Curves
Intuitively, the difference of arc length of a given polar curve for an infinitely small segment $\Delta\theta$ should be $\sqrt{ (r\Delta\theta)^2+\Delta r^2 }$. Therefore, we will have:
$$
L=\int _{a}^b \sqrt{ (r\cdot  d\theta)^2+(dr)^2 }=\int _{a}^b \sqrt{ r^2+\left( \frac{dr}{d\theta} \right)^2 } \, d\theta  
$$

>**THEOREM**:
>For $a<\theta<b$, the arc length of the polar euqation $r=f(\theta)$ is
>$$
L=\int _{a}^b \sqrt{ r^2+\left( \frac{dr}{d\theta} \right)^2 } \, d\theta $$
