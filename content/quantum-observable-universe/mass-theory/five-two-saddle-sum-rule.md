## The $5_2$ saddle sum rule

The $5_2$ saddle cubic is

$$
  y^3 - 2y^2 + 3y - 1 \;=\; 0 ,
$$

with discriminant $-23$. It has one real root $t \in (0,1)$ and a conjugate pair $a, \bar a$ with $\mathrm{Im} a > 0$. The sum rule states that the dilogarithm values at the three roots combine into a closed form involving only $\pi$, $\log t$, and $\arg a$.

**Theorem.**
*There exist $t \in (0,1)$ real and $a \in \mathbb{C}$ with $\mathrm{Im} a > 0$, both roots of the saddle cubic together with $\bar a$, such that*

$$
  \mathrm{Li}_2(a) + \mathrm{Li}_2(\bar a) + \mathrm{Li}_2(t)
  \;=\;
  -\frac{\pi^2}{6} \;-\; \frac{(\log t)^2}{2} \;+\; \frac{2}{3}\bigl(\arg a - \pi\bigr)^2 ,
$$

*where $\mathrm{Li}_2$ is the corpus's integral continuation of the dilogarithm to $\mathbb{C} \setminus [1,\infty)$.*

## What changed, and what did not

This statement was previously carried as an open conjecture class, with the comment *"No instance is provided: the statement is open."* It is now a theorem. The route is algebraic: the complex five-term identity evaluated at $(y_3, y_1)$ and $(y_3, y_2)$, the anharmonic evaluations, the branch equations from $y^2 = (1-y)^3$, and the root data — every step sorry-free.

**It is not the volume conjecture.** Three statements are distinct and must not be conflated:

1. the sum rule above, which is now proved;
2. $\mathrm{Vol}(S^3 \setminus 5_2) = 3\,D(y_1)$, which is a statement about a hyperbolic manifold and is not formalised here;
3. $\lim_{N} \frac{2\pi}{N}\log\langle 5_2\rangle_N = \mathrm{Vol}(S^3 \setminus 5_2)$, the volume conjecture for $5_2$ — Ohtsuki's theorem, untouched.

The sum rule is an identity among dilogarithm values at algebraic points. Nothing about a metric, a manifold, or an asymptotic follows from it.

## Why the shape field is $\mathbb{Q}(\sqrt{-23})$ and not something smaller

The cubic is irreducible over $\mathbb{Q}$ with discriminant $-23$, so its splitting field has the imaginary quadratic subfield $\mathbb{Q}(\sqrt{-23})$. Contrast the figure-eight knot, whose shape field is the Eisenstein field $\mathbb{Q}(\sqrt{-3})$ and whose tetrahedra are regular. The extra arithmetic complexity of $5_2$ is exactly why its analysis does not reduce to the $4_1$ argument: the $4_1$ squeeze relies on positivity of $\langle 4_1\rangle_N$, which $\langle 5_2\rangle_N$ does not have.
