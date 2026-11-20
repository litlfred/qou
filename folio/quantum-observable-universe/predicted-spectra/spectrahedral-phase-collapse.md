# Spectrahedral Phase Collapse

**Theorem (convention C).**
*In the pre-Archimedean $q$-regime, write $u = \sqrt{q}$ and let $G(u)$ be the Gram matrix of the Frobenius bilinear form on the Gröbner–Shirshov normal-form basis of $\mathbf{H}_3(q)$, taken with the convention-C Markov weight $z = u/(u^2+1)$. Then on $u > 0$ the form degenerates at exactly two points,*

$$
  u = 1/\psi \approx 0.68233, \qquad \psi^3 - \psi^2 - 1 = 0,
$$

*where $\psi$ is the Supergolden Ratio, and*

$$
  u = 1, \qquad \textit{i.e. } q = 1 .
$$

*The supergolden zero has multiplicity $5$ and the classical zero multiplicity $1$. At each, $G$ acquires a kernel and the formal solution space collapses from the higher-dimensional bulk onto a strictly lower-dimensional face of the Hecke spectrahedron.*

The supergolden threshold is the inverse of the first Super Metallic Mean. The substrate sits above both zeros, at $u_0 = \sqrt{q_0} \approx 1.0536$, inside the region $u > 1$ on which $G$ is non-singular — so neither degeneracy is reached by the physical anchor, and the collapse remains distinct from the aeon instantiation at the boundary $q \to 1^+$.

## Scope: this is a convention-C statement, and the reading does not survive convention D

The exact factorisation, over $\mathbb{Q}(u)$, is

$$
  \det G(u) = -\,\frac{(u-1)(u+1)\,(u^3+u-1)^5\,(u^3+u^2+1)^5\,S_1(u)\,S_2(u)}{u^{10}\,(u^2+1)^{12}},
$$

with $S_1, S_2$ the two sextic factors, both without real roots. The factor $(u^3+u^2+1)^5$ contributes the real root $u = -\psi$, which is negative and therefore outside the regime; the two positive zeros above are all there are.

Under the canonical Convention-D trace ($z_D = q^3/(q^2+1)$), the $6 \times 6$ Gram determinant on $H_3(q)$ is **identically zero for every $q$** — convention D is a root of the determinant as a polynomial in $z$, which is `QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero` (with the null direction exhibited explicitly as the three-strand $q$-antisymmetriser). A hypothesis singling out $u = 1/\psi$ therefore does no work canonically: the Gram is degenerate there because it is degenerate everywhere.

So the theorem above is true, non-vacuous and permanent **as a convention-C result** — but the phase-transition *reading* of it is frame-dependent and must not be restated as a property of the canonical Gram. This is a scope-limited negative in the sense of the (a)/(b) discipline: it rules out this determinant route to a canonical phase transition, not a canonical phase transition by some other route.
