The **$q$-angular momentum** of a particle is the
$\mathrm{SU}_q(2)$ Casimir eigenvalue of its knot
representation.

**Definition.**
Let $K = \hat{\beta}$ be a knot/link with braid representative
$\beta \in B_n$.  The **$q$-angular momentum** is the eigenvalue of
the $q$-Casimir element $C_q$ (cf. [def:q-casimir](#def:q-casimir))
on the spin-$j$ irreducible of $\mathrm{SU}_q(2)$:

$$
  J_q^2(K) =  [j]_q  [j+1]_q
  =  \frac{q^j - q^{-j}}{q - q^{-1}} \cdot
        \frac{q^{j+1} - q^{-(j+1)}}{q - q^{-1}}
$$

where $j$ is the spin quantum number determined by the
Jones--Wenzl projector $p_n$ acting on the $n$-strand braid:
$j = n/2$ for the highest-weight component.

At $q = 1$: $J_q^2 \to j(j+1)$, the standard Casimir.

**The $q$-deformed angular momentum operators.**

The generators $J_+, J_-, J_z$ of $\mathrm{SU}_q(2)$ satisfy:

$$
  [J_z, J_{\pm}] = \pm J_{\pm}, \qquad
  [J_+, J_-] = [2 J_z]_q
  =  \frac{q^{2J_z} - q^{-2J_z}}{q - q^{-1}}
$$

This differs from the classical $[J_+, J_-] = 2J_z$ by
replacing $2J_z$ with its $q$-number $[2J_z]_q$.  The
asymmetry at $q \neq 1$ is directly connected to parity
violation ([parity violation](#prop:parity-violation-skein)):
the raising and lowering operators are not related by a simple
conjugation.

