The [classical limit obstruction](#def:classical-limit-obstruction)
sits in a Hochschild tower whose vanishing controls flatness of the
$q \to 1$ deformation; we record the tower, the flatness mechanism,
and its comparison with the Yekutieli characteristic classes.

**The Hochschild tower.**
The Hochschild cohomology groups $HH^n(\mathcal{U}_q, \mathrm{Ad})$
govern the deformation theory of the substrate family
$\{A_q\}_{q \in \mathbb{G}_m}$:

| Degree | Group | Interpretation |
|--------|-------|----------------|
| $HH^0(\mathrm{Ad})$ | $\mathrm{Ad}^G$ | $G$-invariant adjoint vectors (hidden symmetries) |
| $HH^1(\mathrm{Ad})$ | $\mathrm{Der}(\mathcal{U}_q) / \mathrm{Inn}(\mathcal{U}_q)$ | Outer derivations (infinitesimal deformations of the family) |
| $HH^2(\mathrm{Ad})$ | $\mathrm{Obs}(\mathbf{C}, q \to 1)$ | Obstructions to extending deformations across $q = 1$ |
| $HH^3(\mathrm{Ad})$ | $\mathrm{Obs}_2$ | Secondary obstructions (Massey products) |

A property $\mathcal{P}(q)$ that holds for $q \in \mathbb{G}_m^{\mathrm{nt}}$
(generic non-torsion) persists through $q = 1$ if and only if its
**obstruction class** $[\mathcal{P}] \in HH^2(\mathrm{Ad})$ vanishes.

**Why $HH^2$ controls the classical limit.**
The classical limit $q \to 1$ is a deformation-theoretic
specialisation: the family $\{A_q\}_{q \in \mathbb{G}_m}$ is a
flat deformation of $A_1$ over the formal neighborhood of
$q = 1$.  The base of the deformation is
$\mathrm{Spf} R[[q-1]]$, and the obstructions to
**flatness** at each order in $(q-1)$ live in $HH^2$.

Concretely: expanding $A_q = A_1 + (q-1)\phi_1 + (q-1)^2\phi_2 + \cdots$
(the Drinfeld--Jimbo expansion), the first-order deformation
$\phi_1$ is a Hochschild 2-cocycle (defines $[\phi_1] \in HH^2$).
The second-order term $\phi_2$ exists iff $[\phi_1] \cup [\phi_1] = 0$
in $HH^3$.  The obstruction tower continues: $\phi_n$ exists iff
a sequence of Massey products vanishes in $HH^{n+1}$.

The **total** obstruction to the classical limit is the formal sum:

$$
\mathrm{obs}_\infty
= 
\sum_{n \geq 1} (q-1)^n [\phi_n]
 \in 
HH^2(\mathrm{Ad})[[q-1]].
$$

This formal power series converges (is a well-defined formal
obstruction) iff all Massey products vanish through the tower.

**For a general quantum universe**: the obstruction space
$HH^2(\mathrm{Ad})$ has no a priori bound on its dimension.
With $m = \dim HH^0(\mathrm{Ad})$ hidden symmetries, the
space of obstructions can be at least $m$-dimensional
(by the cup product $HH^0 \otimes HH^2 \to HH^2$, the
hidden symmetries act on the obstruction space).  Each
independent obstruction class corresponds to a distinct
way the classical limit can fail.

**Connection to the Yekutieli tower.**
The Hochschild obstruction $[\phi_n] \in HH^2(\mathrm{Ad})$
maps to the quantum characteristic class
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$
([quantum characteristic classes](#def:quantum-characteristic-classes))
under the Hochschild-to-sheaf comparison map:

$$
HH^2(\mathcal{U}_q, \mathrm{Ad})
\xrightarrow{ \mathrm{HKR}}
H^2(\mathcal{S}, \mathcal{B}).
$$

For smooth algebras this is the Hochschild--Kostant--Rosenberg
isomorphism; for the quantum group it is a filtered quasi-isomorphism
\cite{yekutieli2010}.  The upshot: the abstract Hochschild obstruction
is computed concretely by the Euler class $\kappa_0 = e(\xi)$ and its
Kummer filtration.
