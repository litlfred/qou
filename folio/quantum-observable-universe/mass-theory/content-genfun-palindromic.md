**Proposition (palindromy and bar-even rigidity of the content generating function).**

*For $n \geq 1$ let $f^\lambda$ be the number of standard Young tableaux of shape
$\lambda \vdash n$ and $\mathrm{content}(\lambda) = \sum_{(i,j)\in\lambda}(j-i)$ the
content sum, and set*

$$
C_n(q) \;=\; \sum_{\lambda \vdash n} f^\lambda\, q^{\,\mathrm{content}(\lambda)} .
$$

*Then $C_n$ is **palindromic**,*

$$
C_n(q) \;=\; C_n(q^{-1}),
$$

*and its deviation from the classical value is **bar-even of second order**,*

$$
C_n(q) - C_n(1) \;=\; O\!\big((q-1)^2\big),
\qquad C_n(1) = \sum_{\lambda\vdash n} f^\lambda = I(n),
$$

*where $I(n)$ is the number of involutions of $S_n$.*

By [The balanced dimension sum is the involution generating function for $2\,\mathrm{maj} + \mathrm{content} \circ \mathrm{RSK}$](#prop:binding-period-involution-statistic),
$C_n(q)$ is the content-only face of the binding statistic — the object obtained by
retaining the RSK shape and discarding the descent (major-index) data. The bar-even
$O((q-1)^2)$ deviation is exactly the q-rigidity measured for the level-1/2 alien datum
$\Delta_{\omega_0}$: the content sector carries no linear q-deformation, so it activates
only at second order.

Both statements are instances of a single structural fact — partition conjugation
$\lambda \mapsto \lambda'$ is an anti-invariant involution, $f^{\lambda'} = f^\lambda$
and $\mathrm{content}(\lambda') = -\mathrm{content}(\lambda)$ — which is proved for
every $n$; it gives the palindromy and the vanishing linear term
$\sum_\lambda f^\lambda\,\mathrm{content}(\lambda) = 0$. The
$n=4$ instance is proved directly: $C_4(q) = q^6 + 3q^2 + 2 + 3q^{-2} + q^{-6}$.
