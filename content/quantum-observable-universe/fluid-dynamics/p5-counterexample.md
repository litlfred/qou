We consider the $q \to 1$ limit of solutions to the [q-NS equation](#def:q-navier-stokes). We use the [Yekutieli tower](#def:recursive-brane-tower) to identify the homological stratum where blowup occurs.

**The initial data.**

We construct an initial velocity field $v_0$ from two anti-parallel vortex filaments. They have equal circulation $\Gamma$, are separated by distance $d$, and align with the $z$-direction:

$$
  v_0(x)
  = 
  \frac{\Gamma}{2\pi}
  \left(
    \frac{(x - d/2)^\perp}{|x - d/2|^2}
    -
    \frac{(x + d/2)^\perp}{|x + d/2|^2}
  \right)
  * \phi_\sigma,
$$

where $x^\perp = (-x_2, x_1, 0)$ and $\phi_\sigma$ is a Gaussian mollifier of width $\sigma \ll d$ ensuring smoothness. These counter-rotating vortex tubes approach each other by mutual induction.

In the q-deformed setting, $\Gamma$ is quantised: $\Gamma_q = [j]_q[j+1]_q$ with fundamental mode $j = 1/2$. The separation $d$ is measured in units of the Planck length $\ell_q = (q-1)/q$.

**Phase 1: q-deformed evolution ($q > 1$).**

For $q > 1$, [q-NS well-posedness](#thm:q-ns-wellposedness) guarantees a unique smooth global solution. The two filaments approach, interact, and the [Hecke relation](#rem:braid-fluid) determines the outcome:

* With probability amplitude $q/(q+q^{-1})$: **pass-through** (symmetric channel). The filaments continue past each other.
* With probability amplitude $q^{-1}/(q+q^{-1})$: **reconnection** (antisymmetric channel). The filaments break and rejoin in a new topology.

In either case, the quantum pressure $Q_q$ prevents the cores from overlapping. The minimum separation is $d_{\min} \sim \ell_q = (q-1)/q > 0$.

**Phase 2: the $q \to 1$ limit.**

As $q \to 1^+ = 1 + \varepsilon$:

* $\ell_q \to 0$: the minimum separation vanishes.
* $\nu_q \to 0$: viscous damping vanishes.
* $Q_q \to 0$: quantum pressure vanishes.
* $\Gamma_q = [1/2]_q[3/2]_q \to 1 \cdot 2 / 4 = 3/4$: circulation approaches the classical value.

The filaments approach with velocity $v_{\mathrm{ind}} \sim \Gamma/(2\pi d)$, which diverges as $d \to 0$. Without quantum pressure to arrest the approach:

$$
  d(t) \sim \sqrt{d_0^2 - c\Gamma t},
  \qquad
  T^* = d_0^2/(c\Gamma) < \infty.
$$

At $t = T^*$, the filaments collide and $d(T^*) = 0$.

**Phase 3: the blowup — homological diagnosis.**

At the collision time $T^*$, the vorticity $\omega = \nabla \times v$ concentrates on the collision locus $\Sigma$, which is the line segment where the two filament cores intersect.

**Claim 1 (Hausdorff dimension).** We have $d_H(\Sigma) = 1$ (filament blowup, not sheet or point).
The two filaments are curves in $\mathbb{R}^3$. Their mutual induction causes approach perpendicular to both axes. The collision locus is their intersection curve, which is one-dimensional.

**Claim 2 (Obstruction level).** We have $n^* = 2$. The blowup occurs at the second level of the [brane tower](#def:recursive-brane-tower).
Yekutieli analysis determines $n^*$ by the Sobolev regularity at blowup. Anti-parallel vortex collision produces a velocity field with bounded $L^2$ norm but unbounded vorticity. This places it in $H^s$ with $1 \leq s < 2$. The obstruction appears at level $n^* = 2$.

**Claim 3 (Obstruction class).** The obstruction class $\kappa_2 \in H^2(\Sigma, \mathcal{B})$ at the collision locus is

$$
  \kappa_2
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot [\mathcal{B}]
   \in 
  H^2(\Sigma, \mathcal{O}^{\times}_M),
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ is the integer linking number of the two filaments and $[\mathcal{B}]$ is the fundamental class of the band sheaf.
The [:refterm[descent]{#descent} condition](#prop:descent-condition) fails at $\Sigma$ because the transition functions $g_{ij}^{(2)}$ of the second jet prolongation acquire a discontinuity proportional to the linking number. This linking number is a topological invariant. It depends only on the knot type of the filament pair, not on the approach geometry.

**Claim 4 (Local cohomology).** The [local cohomology](#def:local-cohomology-group) at the collision point $p \in \Sigma$ satisfies

$$
  H^1_{\mathfrak{m}_1}(A_p)
   \cong 
  V_{1/2} \oplus V_{1/2},
$$

where $V_{1/2}$ is the fundamental representation of $\mathrm{SU}_q(2)$. This four-dimensional space (two spin-$1/2$ copies) reflects the two filaments meeting at $p$.
Each filament carries the fundamental vortex representation $j = 1/2$. At the collision point, the local cohomology group is the direct sum of their contributions. The non-vanishing of this group proves algebraically that the velocity field cannot be extended smoothly across $p$.

**The complete homological address of the counter-example.**

$$
  \boxed{
    \bigl(
      v_0^{\mathrm{anti-par}},
      T^* = d_0^2/(c\Gamma),
      \Sigma = \text{line segment},
      n^* = 2,
      \kappa_2 = \mathrm{lk} \cdot [\mathcal{B}]
    \bigr)
  }
$$

This structure lives at:

* **Brane tower level**: $n = 2$ (second jet prolongation).
* **Gerbe**: $\mathfrak{G}_2$ (the gerbe of 2-jets of $\mathrm{SU}(2)$ connections).
* **Obstruction**: $\kappa_2 \in H^2(\Sigma, \mathcal{O}_M^\times)$ with value equal to the linking number.
* **Local cohomology**: $H^1_{\mathfrak{m}_1} \cong V_{1/2}^{\oplus 2}$ at each point of $\Sigma$.
* **:refterm[Descent]{#descent} failure**: the twisted 2-cocycle $d(g_{ijk}^{(2)}) \neq a_{ij}^{(2)} \cdot g_{ijk}^{(2)} \cdot (a_{jk}^{(2)})^{-1}$ fails on any triple intersection meeting $\Sigma$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
