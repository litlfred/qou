The [classical limit obstruction](#def:classical-limit-obstruction) occupies a Hochschild tower. Its vanishing controls the flatness of the $q \to 1$ deformation. We record the tower, the flatness mechanism, and the comparison with the Yekutieli characteristic classes.

**The Hochschild tower.** The Hochschild cohomology groups $HH^n(\mathcal{U}_q, \mathrm{Ad})$ govern the deformation theory of the substrate family $\{A_q\}_{q \in \mathbb{G}_m}$:

| Degree | Group | Interpretation |
|--------|-------|----------------|
| $HH^0(\mathrm{Ad})$ | $\mathrm{Ad}^G$ | $G$-invariant adjoint vectors (hidden symmetries). |
| $HH^1(\mathrm{Ad})$ | $\mathrm{Der}(\mathcal{U}_q) / \mathrm{Inn}(\mathcal{U}_q)$ | Outer derivations (infinitesimal deformations of the family). |
| $HH^2(\mathrm{Ad})$ | $\mathrm{Obs}(\mathbf{C}, q \to 1)$ | Obstructions to extending deformations across $q = 1$. |
| $HH^3(\mathrm{Ad})$ | $\mathrm{Obs}_2$ | Secondary obstructions (Massey products). |

A property $\mathcal{P}(q)$ holding for $q \in \mathbb{G}_m^{\mathrm{nt}}$ (generic non-torsion) persists through $q = 1$ if and only if its **obstruction class** $[\mathcal{P}] \in HH^2(\mathrm{Ad})$ vanishes.

**Control of the classical limit by $HH^2$.** The classical limit $q \to 1$ operates as a deformation-theoretic specialisation. The family $\{A_q\}_{q \in \mathbb{G}_m}$ forms a flat deformation of $A_1$ over the formal neighborhood of $q = 1$. The base of the deformation is $\mathrm{Spf} R[[q-1]]$. The obstructions to **flatness** at each order in $(q-1)$ reside in $HH^2$.

Expanding $A_q = A_1 + (q-1)\phi_1 + (q-1)^2\phi_2 + \cdots$ yields the Drinfeld--Jimbo expansion. The first-order deformation $\phi_1$ acts as a Hochschild 2-cocycle, defining $[\phi_1] \in HH^2$. The second-order term $\phi_2$ exists if and only if $[\phi_1] \cup [\phi_1] = 0$ in $HH^3$. The obstruction tower continues: $\phi_n$ exists if and only if a sequence of Massey products vanishes in $HH^{n+1}$.

The **total** obstruction to the classical limit forms the sum:

$$
\mathrm{obs}_\infty
= 
\sum_{n \geq 1} (q-1)^n [\phi_n]
 \in 
HH^2(\mathrm{Ad})[[q-1]].
$$

This formal power series converges (yielding a well-defined formal obstruction) if and only if all Massey products vanish throughout the tower.

**For a general quantum universe:** The obstruction space $HH^2(\mathrm{Ad})$ admits no a priori dimension bound. Given $m = \dim HH^0(\mathrm{Ad})$ hidden symmetries, the obstruction space can be at least $m$-dimensional. The cup product $HH^0 \otimes HH^2 \to HH^2$ dictates that hidden symmetries act on the obstruction space. Each independent obstruction class isolates a distinct failure mode for the classical limit.

**Connection to the Yekutieli tower.** The Hochschild obstruction $[\phi_n] \in HH^2(\mathrm{Ad})$ maps to the quantum characteristic class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) via the Hochschild-to-sheaf comparison map:

$$
HH^2(\mathcal{U}_q, \mathrm{Ad})
\xrightarrow{ \mathrm{HKR}}
H^2(\mathcal{S}, \mathcal{B}).
$$

For smooth algebras, this provides the Hochschild--Kostant--Rosenberg isomorphism. For the quantum group, it serves as a filtered quasi-isomorphism \cite{yekutieli2010}. The abstract Hochschild obstruction is therefore computed concretely by the Euler class $\kappa_0 = e(\xi)$ and its Kummer filtration.
