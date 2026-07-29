Einstein's non-symmetric field theory \cite{einstein1925, einstein1946, einstein1955}, pursued in parallel by Schrödinger \cite{schrodinger1950}, sought to unify gravitation and electromagnetism by discarding the symmetry of the metric:

$$
  g_{\mu\nu}
  \;=\;
  g_{(\mu\nu)} + g_{[\mu\nu]},
$$

with the symmetric part $g_{(\mu\nu)}$ carrying gravitation and the antisymmetric part $g_{[\mu\nu]}$ intended to carry the Maxwell field. The programme did not succeed: $g_{[\mu\nu]}$ never reproduced Maxwell's equations, and its modern descendant, Moffat's nonsymmetric gravitational theory \cite{moffat1995}, carries linearisation instabilities and ghost modes in the antisymmetric sector \cite{damour1993}.

**Position of the QOU construction.**
The QOU substrate carries a symmetric–antisymmetric decomposition with the same force assignment Einstein sought, but the decomposition is not carried by a metric. It is the eigenvalue decomposition of the braiding.

By the [Hecke relation](#def:crossing-energy), the braiding $c_{V,V}$ splits $V \otimes V$ into $\mathrm{Sym}^2_q(V) \oplus \Lambda^2_q(V)$ and acts on the two summands by the scalars $q$ and $-q^{-1}$. Writing $\lambda = \ln q$, the [crossing energy decomposition](#prop:crossing-energy-decomposition) resolves these weights into channels that are respectively even and odd under the mirror operation $\sigma$:

$$
  q = \cosh\lambda + \sinh\lambda,
  \qquad
  q^{-1} = \cosh\lambda - \sinh\lambda.
$$

The $\cosh$ channel is $\sigma$-invariant and binds independently of charge; the $\sinh$ channel reverses under $\sigma$ and distinguishes charge ([channel identification](#rem:crossing-energy-interpretation)). The [electromagnetic coupling](#prop:em-coupling-projection) is a multiple of the antisymmetric eigenvalue $q^{-1}$.

**Comparison.**

| | Non-symmetric field theory | QOU |
|---|---|---|
| Carrier of the decomposition | metric $g_{\mu\nu}$ on spacetime | braiding $c_{V,V}$ on $\mathbf{C}$ |
| Symmetric part | gravitation | strong binding, $\cosh\lambda$ |
| Antisymmetric part | electromagnetism (intended) | Coulomb interaction, $\sinh\lambda$ |
| Origin of the decomposition | postulated | forced by the Hecke quadratic |
| Behaviour at $q = 1$ | no analogue | antisymmetric channel vanishes identically |

**Three structural differences.**

1. *The QOU metric is symmetric and emergent.* Gravitation in this framework is the geometry of the [acoustic metric](#rem:madelung-acoustic-metric) of the Madelung brane flow, which is symmetric. No antisymmetric part of a metric appears anywhere in the construction. The asymmetry is located upstream of spacetime, in the braided category; the metric is downstream and emergent.

2. *The instability results do not transfer.* The inconsistency theorems of \cite{damour1993} concern a propagating antisymmetric tensor field with its own field equations. The QOU antisymmetric channel is an eigenvalue of a braiding morphism in a rigid monoidal category and satisfies no field equations, so those results have no target here. The framework is correspondingly not a competing theory of non-symmetric gravitation; it is compared with the canonical quantum-gravity programmes in the [preceding section](#rem:lqg-adm-ashtekar-comparison), not with this one.

3. *The $q$-deformation of the metric is conformal, not antisymmetric.* The parameter $q$ does act on a metric in the [contact deformation](#rem:q-metric-contact-deformation), interpolating the Levi-Civita connection to its Reeb projection. That deformation is conformal and contact-theoretic; it does not add an antisymmetric part.

**Note on terminology.**
The torsion appearing in the [substrate parameter axiom](#rem:substrate-gm-torsion) is the torsion subgroup $\mu_\infty \subset \mathbb{G}_m$ of roots of unity, which the substrate section must avoid. It is unrelated to the torsion tensor of an affine connection used in Einstein--Cartan theory and in nonsymmetric gravitational theory.
