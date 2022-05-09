## Tangent in Parametric Curves
From Chain Rule, we have:
$$
\frac{ dy }{ dt } =\frac{ dy }{ dx } \frac{ dx }{ dt } 
$$
If $dx/dt\neq 0$, we have
>**THEOREM**:
>The derivative can be given by:
>$$
\begin{align*}
\frac{ dy }{ dx } =\frac{\displaystyle\frac{ dy }{ dt }}{\displaystyle\frac{ dx }{ dt } }&&\text{if }\frac{ dx }{ dt } \neq 0 \tag{1}
\end{align*}$$

It's also easy to observe that when $\frac{ dx }{ dt } =0$, the curve has a vertical tangent. When $\frac{ dy }{ dt } =0$, it has a horizontal tangent.

>**THEOREM**:
>The second derivative can be given by:
>$$
\frac{ d^{2}y }{ dx^{2} } =\frac{d}{dx} \left( \frac{ dy }{ dx }  \right)=\frac{\displaystyle\frac{d}{dt} \left( \frac{ dy }{ dx }  \right)}{\displaystyle\frac{ dx }{ dt } }$$

## Areas in Parametric Curves
The area under a curve $y=F(x)$ from $a$ to $b$ is $A=\int ^b_{a}F(x) \, dx$.

>**THEOREM**:
>If $x=f(x)$ and $y=g(t)$, the area under the curve $y=F(x)$ is given by:
>$$
A=\int ^b_{a}y \, dx=\int ^\beta_{\alpha}g(t)f'(t) \, dt  $$

## Arc Length in Parametric Curves
The arc length of a curve $y=F(x)$ in an interval $a\leq x\leq b$ is $L=\int ^b_a\sqrt{ 1+\left( \frac{ dy }{ dx }  \right)^2 } \, dx$ if $F'$ is continuous.

Using (1) to replace $\frac{dy}{dx}$, we get
>**THEOREM**:
>If a curve $C$ is described by the parametric equations $x=f(t),y=g(t)$, $\alpha\leq t\leq \beta$, where $f'$ and $g'$ are continuous on $[\alpha,\beta]$ and $C$ is traversed exactly once as $t$ increases from $\alpha$ to $\beta$, then the length of $C$ is
>$$
\begin{align*}
L&=\int ^b_{a}\sqrt{ 1+\left( \frac{ dy }{ dx }  \right)^2 } \, dx=\int _{\alpha}^\beta \sqrt{ 1+\left( \frac{\frac{dy}{dt}}{\frac{dx}{dt}} \right)^2 } \frac{dx}{dt} \, dt\\
&=\int _{\alpha}^\beta \sqrt{ \left( \frac{ dx }{ dt }  \right)^2+\left( \frac{ dy }{ dt }  \right)^2 } \, dt \tag{4}
\end{align*}$$

Note that even if $y=F(x)$ is not a function, (4) still holds because the equation can also be derived from polygonal approximation.

## Surface Area of Revolution in Parametric Curves
Similar to arc length, we can also have a parametric version of surface area of revolution.

