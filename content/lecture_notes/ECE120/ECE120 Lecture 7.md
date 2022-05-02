---
title: "ECE120 Lecture 7"
---
## Program Analysis
Being able to read code is a necessary skill.

In the real world, codes are often poorly commented (few people are interested in commenting their codes). Therefore, it would be nice if we could interpret others' codes without comments.
```c
/* Adapted from V. Kindratenko's notes on 30 August 2016. */
#include <stdio.h> /* needed for printf and scanf */
int main()
{
 int A;
 char B;
 int C;
 int D;
 printf ("Enter two numbers separated by a character: ");
 if (3 != scanf ("%d %c %d", &A, &B, &C)) {
 printf ("Please try again.\n");
 /* Program failed. */
 return 3;
 }
 if ('+' == B) {
 D = A + C;
 } else if ('-' == B) {
 D = A - C;
 } else if ('/' == B) {
 D = A / C;
 } else if ('*' == B) {
 D = A * C;
 } else {
 printf ("Invalid choice '%c'\n", B);
 /* Program failed. */
 return 2;
 }
 printf ("answer: %d\n", D); 
 /* End the program successfully. */
 return 0;
}
```

## Testing Programs
In the world of programming, it's a wise choice to test your programs before true submission.
__Brooks' Rule of Thumb__:
- 1/3 planning and design 
- 1/6 writing the program 
- 1/2 testing

It's really no kidding. Programmers often make small mistakes in programming and it will take a long testing period to find out those mistakes.


## Floating Points are Tricky!
As we have shown [[Lectures/ECE120/Lecture 4#Danger in floating point numbers|before]], floating point numbers are tricky to handle.
Here is an example in C Programming:

Suppose we wish to find $\int^{1}_{-1}{(x^{2}+2x+3)} \mathrm{d}x$ by using C Programming.
We could use an approximation of [[Riemann Sum]]
```c
#include <stdio.h>

int main()
{
 int n = 100; /* hardcoded number of Riemann sum terms */
 float a = -1.0f; /* hardcoded [a,b] */
 float b = 1.0f;
 float s = 0.0f; /* computed integral value */
 int i; /* loop counter */
 float x; /* x and y=f(x) */
 float y;
 float dx = (b - a) / n; /* width of rectangles */
 /* Sum n rectangles. */
 for (i = 0; n > i; i = i + 1) {
 /* x values are equally spaced from a to b. */
 x = a + dx * i;
 /* y values are f(x). */
 y = x * x + 2 * x + 3;
 /* Rectangle is y high and dx wide. */
 s = s + y * dx;
 }
 printf ("%f\n", s);
 return 0;
}
```
Theoretically, as ```n``` gets larger, the result will become more accurate.

![[Bin/Photos/ECE120Lec07Img1.png]]
This is also how things develop when $\mathrm{n} < 10^{6}$. 

However, when $\mathrm{n}> 10^{6}$ , things becomes wired.
![[Bin/Photos/ECE120Lec07Img2.png]]

Why? Note an important part of the code above
```c
s = s + y * dx;
```
As ```n``` gets larger, ```y * dx``` gets smaller and smaller, and as we've already mentioned earlier, a super-large number adding a super-small number causes errors in floating point.

## Bit-wise Calculation
As we have learnt previously in Boolean Operations, C supports multiple bit-wise operations. We can use this interesting property to do efficient truth table printing:
```c
#include <stdint.h>
#include <stdio.h>
int main ()
{
 /*
 * The input variables A, B, and C are 8-bit unsigned values.
 * We use each bit to represent a possible combination of the
 * three variables.  Bit 7 of each is set to a 1, for example.
 * Bit 4 of A is set to 1, while bits 4 of B and C are set to 0.
 * In this way, we cover all entries of the truth table for
 * F(A,B,C).
 */
 uint8_t A = 0xF0; /* input variable A                   */
 uint8_t B = 0xCC; /* input variable B                   */
 uint8_t C = 0xAA; /* input variable C                   */
 uint8_t F; /* the function F                     */
 int32_t i; /* truth table row iteration variable */
 /*
 * Compute all possible values of function F using one statement.
 *    F(A,B,C) = (A+B)(A'+C')
 */
 F = ((A | B) & ((~A) | (~C)));
 /* Print a truth table for F. */
 printf ("A B C | F\n");
 printf ("------+---\n");
 for (i = 0; 8 > i; i = i + 1) {
 printf ("%c %c %c | %c\n",
 '0' + (0 != (i & 4)), /* A        */
 '0' + (0 != (i & 2)), /* B        */
 '0' + (0 != (i & 1)), /* C        */
 '0' + (0 != (F & (1 << i)))); /* F(A,B,C) */
 }
 /* Return success. */
 return 0;
}
```

How does this program come into effect?

Let's first analyze the final result we wish to have:
$$
F = (A+B)(\overline{A}+\overline{C})
$$
| A | B | C | F |
|---|---|---|---|
|0|0|0|x|
|0|0|1|x|
|0|1|0|x|
|0|1|1|x|
|1|0|0|x|
|1|0|1|x|
|1|1|0|x|
|1|1|1|x|

It's not hard to comprehend why we choose ```0xF0, 0xCC, 0xAA``` for```A, B, C```
If we rewrite them in binary, they'll be:
$$
\begin{align*}
A&=11110000_2\\
B&=11001100_2\\
C&=10101010_2
\end{align*}
$$
If we do bit-wise calculations on them, the corresponding ```F``` will be the result for each row of the truth table.

But what does ```(0 != (i & 4))``` means?
Well, let's first analyze what ```i & 4``` does.

We've known that $4_{10}=0\cdots 0100_{2}$
Notice there's only one bit $1$ in $4_{10}$. Therefore, when we do the calculation of ```i & 4```, for those $0$ bits, the result must be $0$, but for the 2nd bit (from behind), it will result in $1$ if the 2nd bit of ```i``` is $1$.

It becomes very interesting that from $0$ to $7$ ($0\cdots 0000_{2}$ to $0\cdots 0111_{2}$), the 2nd bit changes every 4 times.

For ```i & 2```, the 1st bit changes every 2 times, for ```i & 1```, the 0th bit changes every time! This is exactly what we want for ```A, B, C```.
