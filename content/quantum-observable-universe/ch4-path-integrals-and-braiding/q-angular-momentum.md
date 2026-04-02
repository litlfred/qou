The **$q$-angular momentum** of a particle is the
$\mathrm{SU}_q(2)$ Casimir eigenvalue of its knot
representation.

**Definition.**
Let $K = \hat{\beta}$ be a knot/link with braid representative
$\beta \in B_n$.  The **$q$-angular momentum** is defined by the
$q$-Casimir operator $C_q$ of $\mathrm{SU}_q(2)$:

$$
  J_q^2(K) \;=\; [j]_q \, [j+1]_q
  \;=\; \frac{q^j - q^{-j}}{q - q^{-1}} \cdot
        \frac{q^{j+1} - q^{-(j+1)}}{q - q^{-1}}

$$

where $j$ is the spin quantum number determined by the
Jones-Wenzl projector $p_n$ acting on the $n$-strand braid:
$j = n/2$ for the highest-weight component.

At $q = 1$: $J_q^2 \to j(j+1)$, the standard Casimir.

**The $q$-deformed angular momentum operators.**

The generators $J_+, J_-, J_z$ of $\mathrm{SU}_q(2)$ satisfy:

$$
  [J_z, J_{\pm}] = \pm J_{\pm}, \qquad
  [J_+, J_-] = [2 J_z]_q
  \;=\; \frac{q^{2J_z} - q^{-2J_z}}{q - q^{-1}}

$$

This differs from the classical $[J_+, J_-] = 2J_z$ by
replacing $2J_z$ with its $q$-number $[2J_z]_q$.  The
asymmetry at $q \neq 1$ is directly connected to parity
violation ([parity violation](#prop:parity-violation-skein)):
the raising and lowering operators are not related by a simple
conjugation.

**Connection to the Jones polynomial.**

The Jones polynomial $J_K(q)$ of a knot $K$ is the quantum
trace over the spin-$\tfrac{1}{2}$ representation:

$$
  J_K(q) \;=\; \mathrm{tr}_{V_{1/2}}(\rho(\beta))

$$

The colored Jones polynomial $J_K^{(j)}(q)$ uses the
spin-$j$ representation.  The $q$-angular momentum is
encoded in the **recursion** between colored Jones
polynomials:

$$
  J_K^{(j+1/2)}(q) \;=\; [2j+1]_q \cdot J_K^{(j)}(q)
  \;+\; \text{(lower-order terms)}

$$

**Building block values.**

| Knot | $n$ (strands) | $j$ | $J_q^2$ at the substrate parameter $q$ | Classical $j(j+1)$ |
|------|:---:|:---:|:---:|:---:|
| $0_1$ (unknot) | $1$ | $0$ | $0$ | $0$ |
| $3_1$ (trefoil) | $2$ | $\frac{1}{2}$ | $[1/2]_q [3/2]_q = 0.818$ | $0.75$ |
| $4_1$ (figure-eight) | $2$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |
| $5_1$ (cinquefoil) | $2$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |
| $\mathcal{B}_3$ (Borromean) | $3$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |

All single-component knots in $B_2$ carry spin $j = \tfrac{1}{2}$.
The nuclear spin depends on coupling: $A$ nucleons
(each $j = 1/2$) couple to total $J$ via $q$-Clebsch-Gordan
coefficients, with $J$ parity determined by $A \bmod 2$
([nuclear spin parity](#prop:nuclear-spin-parity)).

**Nuclear $q$-angular momentum.**

For a nucleus $\mathcal{N}(Z, N)$ with $A = Z + N$:

$$
  J_q^2(\mathcal{N}) \;=\; [J]_q \, [J+1]_q

$$

where $J$ is the ground-state spin determined by the nuclear
link's embedding in the Temperley-Lieb algebra $TL_A(\delta)$
with $\delta = -(q^{1/2} + q^{-1/2})$.
