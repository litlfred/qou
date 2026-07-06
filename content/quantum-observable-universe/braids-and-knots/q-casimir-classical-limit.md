The generic $q$-Casimir eigenvalue of [def:q-casimir](#def:q-casimir),
$[j]_q\,[j+1]_q$ with $[n]_q = (q^n - q^{-n})/(q - q^{-1})$, is defined
over an abstract coefficient field. Its **classical limit** is the
archimedean specialisation to $\mathbb{R}$ at $q \to 1$.

**Proposition (classical limit of the $q$-Casimir eigenvalue).**
*Specialising the coefficient field to $\mathbb{R}$, as $q \to 1$ the
symmetric $q$-number converges to its undeformed value,*

$$
  \lim_{q \to 1} [n]_q  =  n,
$$

*and consequently the $q$-Casimir eigenvalue converges to the classical
$\mathfrak{su}(2)$ Casimir eigenvalue,*

$$
  \lim_{q \to 1} [j]_q\,[j+1]_q  =  j\,(j+1).
$$

The limits are taken over the punctured neighbourhood $q \to 1$,
$q \neq 1$, in the order topology of $\mathbb{R}$. The value $j(j+1)$
is the eigenvalue of the usual Casimir
$C = FE + \tfrac{1}{2}H(\tfrac{1}{2}H + 1)$ on the spin-$j$
representation, recovering the classical angular-momentum-squared
spectrum.

**Archimedean specialisation (§7c).** This block sits on the
archimedean side of the substrate wall: the generic algebraic
construction of the $q$-Casimir stays coefficient-field-free in
[def:q-casimir](#def:q-casimir), while the real-analytic $q \to 1$
limit — a `Tendsto` statement over $\mathbb{R}$ — is separated here and
consumes that generic eigenvalue at $K := \mathbb{R}$.
