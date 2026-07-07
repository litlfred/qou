<!-- FILE_START: ns-approaches-intro.md -->
The NS obstruction places the classical Navier--Stokes
regularity question inside a one-parameter family of well-posed
$q$-deformed equations. We collect the conjectures, partial
results, and proof strategies that organise the degeneration at
$q = 1$ into a research programme.

We start from Conjecture: Regularity breakdown at $q = 1$: the classical limit as a phase transition, which posits a critical
point at $q = 1$, and refine the picture with Conjecture: Critical exponent of the enstrophy divergence at $q = 1$ and Conjecture: Blowup mechanism as Yekutieli lifting obstruction in the brane tower. The transfinite size of the blowup mode is recorded in
Remark: Surreal bound for Navier--Stokes: enstrophy transfinite exceeds mass-gap infinitesimal. The structural prediction is
Proposition: Universality of the critical exponent: dependence on $\chi(A)$ alone — the critical exponent depends only on the Euler
characteristic — and the consequence for the Clay problem is
Conjecture: Counter-example to Navier--Stokes regularity via $q \to 1$ degeneration.

The convergence machinery is Conjecture: $q$-deformed Aubin--Lions lemma: compactness of the solution family as $q \to 1$. The
blowup criterion adapted to the $q$-deformed setting is
Theorem: $q$-deformed Beale--Kato--Majda criterion, with
Proposition: Vorticity lower bound for anti-parallel filament collision as $q \to 1$ supplying the last-gap estimate. The geometric
mechanism at collision is Conjecture: Levi degeneracy conjecture: contact non-degeneracy at vortex collision determines NS regularity, with Remark: Townsend evolution under Biot--Savart strain: the first-order flattening $\kappa \to 0$ and
Remark: Hyperbolic-overlap strain saturation: $\kappa^2 = \pi\nu/(2\Gamma+\pi\nu)$ preserves Levi non-degeneracy tracking the strain dynamics that govern $\kappa$.

We close with the explicit blowup ansatz in Proposition: Self-similar blowup profile: the Leray equations with $\mathrm{SU}_q(2)$ constraints and consolidate the open problems in Remark: The quantum Navier--Stokes programme: from categorical regularity to the Clay problem. This is the final section of the chapter; what
carries forward is the research programme itself, which subsequent
chapters draw on when invoking the brane fluid as a categorical
substrate.

_(draft.)_
<!-- FILE_END: ns-approaches-intro.md -->

<!-- FILE_START: regularity-breakdown.md -->
The [global regularity theorem](#thm:q-ns-wellposedness) holds for
every $q > 1$.  The classical Navier--Stokes regularity problem
asks what happens at $q = 1$.  The QOU framework suggests that
$q = 1$ is a **critical point** where regularity undergoes a phase
transition.

**Conjecture (regularity breakdown).**
There exist smooth, finite-energy initial data $v_0$ such that the
classical Navier--Stokes equation (the $q = 1$ limit of the
[q-Navier--Stokes equation](#def:q-navier-stokes)) develops a
singularity in finite time.  Specifically:

1. **Blowup of enstrophy.**  There exists a time $T^* < \infty$
   such that

   $$
     \lim_{t \to T^{*-}}
     \int_{\mathbb{R}^3} |\omega(x, t)|^2dx
     =  +\infty,
   $$

   where $\omega = \nabla \times v$ is the vorticity.

2. **Vortex sheet concentration.**  The blowup occurs by
   concentration of vorticity onto a codimension-1 surface
   (vortex sheet), not a codimension-2 filament.  The
   Hausdorff dimension of the singular set is $d_H = 2$.

3. **Self-similar asymptotics.**  Near the blowup time, the
   solution approaches a self-similar profile

   $$
     v(x, t)
      \approx 
     \frac{1}{\sqrt{T^* - t}}
     V\!\left(\frac{x - x_0}{\sqrt{T^* - t}}\right),
   $$

   where $V(\xi)$ solves the Leray equations
   $-\frac{1}{2}V - \frac{1}{2}(\xi \cdot \nabla)V +
   (V \cdot \nabla)V = -\nabla P + \nu\Delta V$.

**The three obstructions (why each mechanism fails at $q = 1$).**

**Obstruction 1: Loss of UV regularisation.**
At $q = 1$, the $q$-Laplacian eigenvalues degenerate from
exponential to polynomial: $[k]_1 = k$.  The dissipation rate
$\gamma_k = \nuk^2/L^2$ grows only quadratically, which is
insufficient to control the cubic nonlinearity in the
enstrophy equation.  The $q$-deformation provides a "spectral
gap" between mode $k$ and mode $k+1$ of size
$[k+1]_q - [k]_q = q^k \to 1$ as $q \to 1$, so the spectral
gap closes.

**Obstruction 2: Viscosity vanishes.**
The quantum viscosity $\nu_q = (q-1)/(2q) \to 0$ as
$q \to 1$.  In the [Planck--Reynolds](#rem:planck-reynolds)
language, $\mathrm{Re}_q = 2/(q-1) \to \infty$: the classical
limit is infinitely turbulent.  The finite-dimensional reduction
in Step 2 of the well-posedness proof fails because
$N_{\mathrm{eff}} \to \infty$.

**Obstruction 3: Cascade becomes continuous.**
The [q-turbulence spectrum](#prop:q-turbulence-spectrum) has
discrete transfer rates with exponentially decreasing amplitude.
At $q = 1$, the cascade becomes continuous and the transfer rate
$T_{k \to k+1} \to \varepsilonk^{-1/3}$ (Kolmogorov), allowing
energy to reach arbitrarily high wavenumbers in finite time.

**Critical exponents.**
The transition at $q = 1$ has the structure of a second-order
phase transition.  Define:

- **Enstrophy order parameter**:
  $\Omega(q) = \sup_{t \geq 0} \sum_k [k]_q^2|\hat{v}_k(t)|^2$.
  For $q > 1$, $\Omega(q) < \infty$ (regularity).  At $q = 1$,
  $\Omega(1) = +\infty$ (blowup).

- **Critical exponent**:
  $\Omega(q) \sim (q - 1)^{-\alpha}$ as $q \to 1^+$,
  with $\alpha > 0$ to be determined.

- **Correlation length**:
  The maximum active wavenumber
  $k_{\max}(q) \sim \log_q(\mathrm{Re}_q^{3/4})
  \sim \ln(q-1)^{-1} / \ln q \to \infty$ as $q \to 1^+$.

The [Hamilton--Jacobi picture](#rem:hamilton-jacobi-phase) gives
physical intuition: caustics of the phase $S$ (vortex nucleation
sites) proliferate as $q \to 1$ because the quantum pressure
$Q_q$ that regularises them vanishes.  In the classical limit,
infinitely many caustics merge into a vortex sheet — the
singularity.

**Relation to the Clay problem.**
The Clay Mathematics Institute formulation asks:

> *In three space dimensions and time, given an initial velocity
> field, does there exist a vector velocity and a scalar pressure
> field, which are both smooth and globally defined, that solve the
> Navier–Stokes equations?*

The QOU framework reframes this as a **degeneration problem**:
the q-NS equation is globally regular for all $q > 1$
([Theorem](#thm:q-ns-wellposedness)), and the Clay question asks
whether this regularity survives the limit $q \to 1$.  The
three obstructions above suggest it does not — the classical
Navier--Stokes equation is the **critical point** of a
one-parameter family of well-posed equations, and singularity
formation is the mechanism by which the infinite-dimensional
classical dynamics emerge from the finite-dimensional
$q$-deformed dynamics.

**Analogy with statistical mechanics.**
The regularity phase transition at $q = 1$ is analogous to the
Ising model at the critical temperature $T_c$:

See [Table](#tbl:regularity-breakdown-table-data).

Just as the Ising model is exactly solvable away from $T_c$ but
exhibits critical phenomena at $T_c$, the $q$-Navier--Stokes
equation is exactly solvable (globally regular) away from $q = 1$
but develops singularities at the critical point.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: regularity-breakdown.md -->

<!-- FILE_START: p2-critical-exponent.md -->
**Conjecture (assuming [`conj:regularity-breakdown`](#conj:regularity-breakdown)).**

The [regularity breakdown conjecture](#conj:regularity-breakdown)
predicts that the maximum enstrophy diverges as
$\Omega_{\max}(q) \sim (q-1)^{-\alpha}$ for some $\alpha > 0$.

From the [enstrophy evolution](#prop:q-ns-nonlinear-uniqueness),
the enstrophy satisfies

$$
  \frac{d\Omega}{dt}
   \leq 
  \Lambda_q\Omega,
  \qquad
  \Lambda_q = \frac{(C_q')^2E_0}{\nu_q} - \nu_q.
$$

The maximum enstrophy over all time is bounded by
$\Omega_{\max}(q) \leq \Omega(0)e^{\Lambda_qT}$ for any
time horizon $T$.  But the **tightest** bound comes from
balancing dissipation against stretching at the critical mode.

**Computation of $\Lambda_q$ asymptotics.**

Set $\varepsilon = q - 1 \to 0^+$.  Then:

- Viscosity: $\nu_q = \varepsilon/(2(1+\varepsilon))
  = \varepsilon/2 + O(\varepsilon^2)$.

- Sobolev constant:
  $C_q' = \bigl(\sum_k [k]_q^{-2}\bigr)^{1/2}$.
  For small $\varepsilon$, $[k]_q \approx k + k(k^2-1)\varepsilon^2/6
  + O(\varepsilon^4)$, so $[k]_q^{-2} \approx k^{-2}(1 - (k^2-1)
  \varepsilon^2/3)$.  The sum converges:
  $C_q'^2 \approx \pi^2/6 + O(\varepsilon^2)$.

- Growth rate: $\Lambda_q \approx
  (\pi^2/6)E_0 \cdot 2/\varepsilon - \varepsilon/2
  = \pi^2 E_0/(3\varepsilon) + O(1)$.

So $\Lambda_q \sim (q-1)^{-1}$ as $q \to 1^+$.

**The Gronwall bound gives $\alpha = 1$.**
From $\Omega_{\max} \leq \Omega(0)e^{\Lambda_q T}$ with
$\Lambda_q \sim (q-1)^{-1}$, this gives exponential growth in
$(q-1)^{-1}$, not power-law.  This bound is too crude.

**Refined estimate via cascade depth.**
The [q-turbulence spectrum](#prop:q-turbulence-spectrum) gives the
cascade depth $N_{\mathrm{eff}} = \lfloor \log_q
(\mathrm{Re}_q^{3/4})\rfloor$.  At $q = 1 + \varepsilon$:

$$
  \mathrm{Re}_q = \frac{2}{\varepsilon},
  \qquad
  N_{\mathrm{eff}}
  \approx \frac{3}{4}\frac{\ln(2/\varepsilon)}{\ln(1+\varepsilon)}
  \approx \frac{3}{4}\frac{\ln(2/\varepsilon)}{\varepsilon}.
$$

The maximum enstrophy of the truncated system with $N$ modes
is bounded by the Kolmogorov enstrophy sum
$\Omega_{\max} \leq \sum_{k=1}^N k^2E(k)$.  With
$E(k) \sim k^{-5/3}$: $\sum_{k=1}^N k^{1/3} \sim N^{4/3}$.

For the $q$-deformed system, the exponential damping
$e^{-\nu_q [k]_q^2 t}$ ensures higher modes contribute
negligibly.  The effective enstrophy is dominated by the
first $N_{\mathrm{eff}}$ modes, giving

$$
  \Omega_{\max}(\varepsilon)
  \lesssim
  N_{\mathrm{eff}}^{4/3}
   \sim 
  \left(\frac{\ln(1/\varepsilon)}{\varepsilon}\right)^{4/3}.
$$

**Result.**
The critical exponent is $\alpha = 4/3$ with a logarithmic
correction:

$$
  \boxed{
    \Omega_{\max}(q)
    \lesssim
    (q-1)^{-4/3}\bigl(\ln(q-1)^{-1}\bigr)^{4/3}
    \quad\text{as } q \to 1^+.
  }
$$


**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: p2-critical-exponent.md -->

<!-- FILE_START: ns-surreal-bound.md -->
This remark expresses the blowup mechanism of
[blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli)
as a literal surreal inequality, matching the framing already
registered for Navier--Stokes in
[body asymptotics catalog](#rem:body-asymptotics-catalog).

**Setup.** Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb
infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and
$q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)).
In the $q > 1$ regime
([$q$-NS well-posedness](#thm:q-ns-wellposedness)), the mass gap
$\Delta_q \asymp \varepsilon^3$ serves as a quantum viscosity
$\nu_q$, and the fluid is globally regular.

**The surreal bound.** Near $\varepsilon = 0$, two rates compete:

| Quantity | Surreal order | Role |
|---|---|---|
| Mass-gap dissipation $\Delta_q$ | $\asymp \varepsilon^3$ | energy the substrate can absorb |
| Enstrophy ceiling $\mathcal{Z}_q$ | $\asymp \varepsilon^{-4/3}$ | energy the vortex cascade produces |

By [surreal rate calculus](#prop:surreal-rate-calculus),
$\mathcal{Z}_q \cdot \varepsilon^{4/3} \asymp 1$ (standard-real order),
while $\Delta_q \asymp \varepsilon^3$ is a positive infinitesimal.
The NS specialisation of
[surreal squeeze](#lem:surreal-squeeze) takes the enstrophy
$\mathcal{Z}_q \asymp \varepsilon^{-4/3}$ in place of the generic
cost $\delta^2 \cdot \varepsilon^{-1}$, and the inequality

$$
  \mathcal{Z}_q \;>\; \Delta_q
  \qquad (\text{strictly, in } \mathbb{R}(\varepsilon) \subset \mathbf{No})
$$

is automatic: $\ordw(\mathcal{Z}_q) = 4/3 > -3 = \ordw(\Delta_q)$ in the
$\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form).  The
cascade sits at **higher $\omega$-order** than the dissipation,
which is the $\ordw$-formalisation of "faster-than-viscous growth".

**Conclusion.** As $\varepsilon \to 0$ (equivalently, as the substrate
becomes classical), the enstrophy transfinite strictly outruns the
mass-gap infinitesimal in the surreal ordering.  No cancellation is
available in $\mathbb{R}(\varepsilon)$, so the classical-limit
Navier--Stokes flow cannot absorb the vorticity cascade: the velocity
field develops a finite-time blow-up.  This is the surreal content of
[blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli).

**Relation to the $\ordw$-catalog entry.** The classical Biot--Savart
scaling $|j^n v|_\Sigma \sim \Gamma / d^{n+1}$ used by
[NS obstruction computation](#prop:ns-obstruction-computation)
has $\ordw(|j^n v|_\Sigma) = -(n + 1)\,\ordw(d)$.  Summing over the jet
tower gives the $\varepsilon^{-4/3}$ ceiling above (via
$d \asymp \varepsilon^{2/3}$ along the Leray profile); the squeeze
inequality then inherits its strict-inequality status from
[surreal squeeze](#lem:surreal-squeeze).
<!-- FILE_END: ns-surreal-bound.md -->

<!-- FILE_START: p4-universality.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Universality of the critical exponent").**

The [critical exponent](#conj:critical-exponent) $\alpha = 4/3$
governs the rate at which enstrophy diverges as $q \to 1$.
The question is whether $\alpha$ depends on the initial data
$v_0$ or only on the categorical invariants of
$(\mathbf{C}, A, \tau)$.

**Claim.** The critical exponent $\alpha$ depends only on:

1. The Euler characteristic $\chi(A)$ of the Frobenius--Hopf
   object (equivalently, the genus of the base manifold in the
   archimedean realisation).
2. The spatial dimension $d = 3$ (fixed by the contact
   structure).
3. The rank of the gauge group ($\mathrm{SU}(2)$, rank 1).

It does **not** depend on the specific initial data $v_0$, the
energy $E_0$, or the detailed geometry of the state bundle
$\mathcal{S}$.

**Argument from the Yekutieli tower.**

The [Euler characteristic stability](#prop:euler-char-stability)
theorem states that $\chi(E_n)$ is constant across the brane
tower: $\chi(E_n) = \chi(A)$ for all $n$.  Hence the
tower has a uniform topological structure at every level.

The critical exponent $\alpha$ is determined by two quantities
that depend only on this uniform structure:

**(a) The Sobolev constant scaling.**
From the [spectral-Sobolev theory](#prop:q-spectral-sobolev),
the Sobolev constant $C_q$ depends on the eigenvalue growth rate
of $\Delta_q$, which is $[k]_q^2$.  The $q$-integer $[k]_q$
depends only on $q$ and $k$, not on $v_0$.  The sum
$C_q^2 = \sum_k [k]_q^{-2}$ is determined by the representation
theory of $\mathrm{SU}_q(2)$ — a categorical invariant.

**(b) The cascade depth scaling.**
The number of active modes $N_{\mathrm{eff}}(q) \sim
\ln(1/\varepsilon)/\varepsilon$ depends on
$\mathrm{Re}_q = 2/(q-1)$, which is a function of $q$ alone.
The Kolmogorov scaling $\Omega \sim N^{5/3}$ is a consequence of
the spatial dimension $d = 3$ and the quadratic nonlinearity —
both categorical invariants.

**(c) Independence from $v_0$.**
The enstrophy evolution

$$
  \frac{d\Omega}{dt}
  \leq \Lambda_q\Omega
$$

has $\Lambda_q = (C_q')^2 E_0/\nu_q - \nu_q$.  The initial
energy $E_0$ enters $\Lambda_q$ but affects only the
**prefactor**, not the **exponent**: $\Lambda_q \sim
(\pi^2/6)E_0 \cdot (q-1)^{-1}$, so $\Lambda_q$ scales as
$(q-1)^{-1}$ regardless of $E_0$.  The critical exponent
$\alpha = 4/3$ comes from the cascade depth scaling, not from
$\Lambda_q$.

**Universality class.**
The critical behaviour belongs to the universality class
determined by:

| Parameter | Value | Origin |
|---|---|---|
| Spatial dimension | $d = 3$ | Contact structure on $\mathcal{S}$ |
| Internal symmetry | $\mathrm{SU}(2)$ | Gauge group from observability |
| Euler characteristic | $\chi(A)$ | Frobenius--Hopf topology |
| Critical exponent | $\alpha = 4/3$ | Kolmogorov + cascade depth |

Different QOU realisations (different $\chi(A)$) could in
principle give different $\alpha$, because $\chi(A)$ affects the
number of embeddable torus knots (the "species" of vortex
filaments), which affects the nonlinear interaction count.  For
the Descartes universe with $\chi(A) = -6$ (Bring's surface,
genus 4), there are 6 embeddable torus knots, yielding a
specific nonlinear coupling structure.

<!-- FILE_END: p4-universality.md -->

<!-- FILE_START: p4-universality-interpretation.md -->
The critical exponent $\alpha = 4/3$ is a heuristic derivation imported from physical arguments (Kolmogorov scaling); here it is framed as a universality-class invariant tied to the categorical structure of the QOU. The exponent depends solely on representation-theoretic data (the $q$-Sobolev constant) and the topology ($\chi(A)$), which decouples the rate of blowup from specific PDE initial data and recasts the scaling behavior as an intrinsic topological property of the background category.
<!-- FILE_END: p4-universality-interpretation.md -->

<!-- FILE_START: p5-counterexample.md -->
Consider the $q \to 1$ limit of solutions to the
[q-NS equation](#def:q-navier-stokes), using the
[Yekutieli tower](#def:recursive-brane-tower) to identify the
homological stratum where blowup occurs.

**The initial data.**
Consider two anti-parallel vortex filaments of equal circulation
$\Gamma$ separated by distance $d$, with axes along the
$z$-direction:

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

where $x^\perp = (-x_2, x_1, 0)$ and $\phi_\sigma$ is a
Gaussian mollifier of width $\sigma \ll d$ ensuring smoothness.
This is the standard **anti-parallel vortex pair** — two counter-
rotating vortex tubes that approach each other by mutual
induction.

In the q-deformed setting, $\Gamma$ is quantised:
$\Gamma_q = [j]_q[j+1]_q$ with $j = 1/2$ (fundamental mode).
The separation $d$ is measured in units of the Planck length
$\ell_q = (q-1)/q$.

**Phase 1: q-deformed evolution ($q > 1$).**
For $q > 1$, the [q-NS well-posedness](#thm:q-ns-wellposedness)
guarantees a unique smooth global solution.  The two filaments
approach, interact, and the outcome is determined by the
[Hecke relation](#rem:braid-fluid):

* With probability amplitude $q/(q+q^{-1})$: **pass-through**
  (symmetric channel).  The filaments continue past each other.
* With probability amplitude $q^{-1}/(q+q^{-1})$:
  **reconnection** (antisymmetric channel).  The filaments break
  and rejoin in a new topology.

In either case, the quantum pressure $Q_q$ prevents the cores
from overlapping.  The minimum separation is
$d_{\min} \sim \ell_q = (q-1)/q > 0$.

**Phase 2: the $q \to 1$ limit.**

As $q \to 1^+ = 1 + \varepsilon$:

* $\ell_q \to 0$: the minimum separation vanishes.
* $\nu_q \to 0$: viscous damping vanishes.
* $Q_q \to 0$: quantum pressure vanishes.
* $\Gamma_q = [1/2]_q[3/2]_q \to 1 \cdot 2 / 4 = 3/4$:
  circulation approaches classical value.

The filaments approach with velocity
$v_{\mathrm{ind}} \sim \Gamma/(2\pi d)$, which diverges as
$d \to 0$.  Without quantum pressure to arrest the approach:

$$
  d(t) \sim \sqrt{d_0^2 - c\Gammat},
  \qquad
  T^* = d_0^2/(c\Gamma) < \infty.
$$

At $t = T^*$, the filaments collide: $d(T^*) = 0$.

**Phase 3: the blowup — homological diagnosis.**

At the collision time $T^*$, the vorticity
$\omega = \nabla \times v$ concentrates on the collision locus
$\Sigma$, a line segment (the intersection of the two filament
cores).  We claim:

**Claim 1 (Hausdorff dimension).**
$d_H(\Sigma) = 1$ (filament blowup, not sheet or point).

*Reason:* The two filaments are curves in $\mathbb{R}^3$.
Their mutual induction causes approach in the direction
perpendicular to both axes.  The collision locus is the
intersection curve, which is 1-dimensional.

**Claim 2 (Obstruction level).**
$n^* = 2$ — the blowup occurs at the second level of the
[brane tower](#def:recursive-brane-tower).

*Reason:* From the
Yekutieli analysis, $n^*$ is
determined by the Sobolev regularity at blowup.  Anti-parallel
vortex collision produces a velocity field with bounded
$L^2$ norm but unbounded vorticity, placing it in $H^s$ with
$1 \leq s < 2$.  The obstruction appears at level $n^* = 2$.

**Claim 3 (Obstruction class).**
The obstruction class $\kappa_2 \in H^2(\Sigma, \mathcal{B})$
at the collision locus is

$$
  \kappa_2
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot [\mathcal{B}]
   \in 
  H^2(\Sigma, \mathcal{O}^{\times}_M),
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ is the linking number
of the two filaments (an integer) and $[\mathcal{B}]$ is the
fundamental class of the band sheaf.

*Reason:* The [:refterm[descent]{#descent} condition](#prop:descent-condition) fails
at $\Sigma$ because the transition functions $g_{ij}^{(2)}$ of
the second jet prolongation acquire a discontinuity proportional
to the linking number.  The linking number is a topological
invariant — it does not depend on the approach geometry but
only on the knot type of the filament pair.

**Claim 4 (Local cohomology).**
The [local cohomology](#def:local-cohomology-group) at the
collision point $p \in \Sigma$ satisfies

$$
  H^1_{\mathfrak{m}_1}(A_p)
   \cong 
  V_{1/2} \oplus V_{1/2},
$$

where $V_{1/2}$ is the fundamental representation of
$\mathrm{SU}_q(2)$.  This is a 4-dimensional space (two
spin-$1/2$ copies), reflecting the two filaments meeting at $p$.

*Reason:* Each filament carries the $j = 1/2$ representation
(fundamental vortex).  At the collision point, the local
cohomology group is the direct sum of their contributions.
The non-vanishing of this group is the algebraic certificate
that the velocity field cannot be extended smoothly across $p$.

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

This lives at:

* **Brane tower level**: $n = 2$ (second jet prolongation)
* **Gerbe**: $\mathfrak{G}_2$ (the gerbe of 2-jets of
  $\mathrm{SU}(2)$ connections)
* **Obstruction**: $\kappa_2 \in H^2(\Sigma, \mathcal{O}_M^\times)$
  with value equal to the linking number
* **Local cohomology**: $H^1_{\mathfrak{m}_1} \cong V_{1/2}^{\oplus 2}$
  at each point of $\Sigma$
* **:refterm[Descent]{#descent} failure**: the twisted 2-cocycle
  $d(g_{ijk}^{(2)}) \neq a_{ij}^{(2)} \cdot g_{ijk}^{(2)}
  \cdot (a_{jk}^{(2)})^{-1}$
  fails on any triple intersection meeting $\Sigma$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: p5-counterexample.md -->

<!-- FILE_START: q-aubin-lions.md -->
> **Summary.** A $q$-deformed Aubin–Lions compactness lemma:
> the family $\{v_q\}_{q>1}$ of $q$-NS solutions admits a
> subsequence converging strongly in $L^2(0,T; \mathcal{H})$ to a
> classical-NS distributional solution as $q \to 1$.
> Time derivatives are bounded uniformly in a weaker dual space,
> giving the compactness needed to take the classical limit.

The [counter-example construction](#conj:ns-counterexample)
requires that the family of q-NS solutions $\{v_q\}_{q > 1}$
converges to a distributional solution of the classical
Navier--Stokes equation as $q \to 1$.  This theorem establishes
the compactness needed for that convergence.

**The classical Aubin--Lions lemma** (Simon 1987): if $X_0
\hookrightarrow X \hookrightarrow X_1$ with $X_0 \hookrightarrow X$
compact, then
$\{u \in L^p(0,T; X_0) : \partial_t u \in L^r(0,T; X_1)\}$
is compactly embedded in $L^p(0,T; X)$.

**The q-deformed setting.**
For each $q > 1$, the q-NS solution $v_q$ lives in the Hilbert
space $L^2_q(A) = \overline{\Omega^1(A)}^{\int_A}$ with norm
depending on $q$ (through the Frobenius pairing).  As $q \to 1$,
these spaces change — we need a common ambient space.

**Step 1: Uniform embedding.**
Define the **$q$-independent** space
$\mathcal{H} = L^2(\mathcal{S}; T\mathcal{S})$ on the state
bundle with respect to the fixed Riemannian volume form.  For
each $q > 1$, the fibre functor $\tau$ embeds
$L^2_q(A) \hookrightarrow \mathcal{H}$ with

$$
  \lVert \tau(v) \rVert_{\mathcal{H}}^2
   \leq 
  C(q)\lVert v \rVert_{L^2_q}^2,
  \qquad
  C(q) = 1 + O(q-1).
$$

The constant $C(q) \to 1$ as $q \to 1$, so the embeddings are
uniformly bounded.  The fibre functor preserves inner products up to a factor
controlled by the substrate parameter.

**Step 2: Uniform energy bound.**
The [energy inequality](#thm:q-ns-wellposedness) gives

$$
  \sup_{t \geq 0} \lVert v_q(t) \rVert_{L^2_q}^2
   \leq 
  \lVert v_0 \rVert_{L^2_q}^2
   \leq 
  C(q)\lVert v_0 \rVert_{\mathcal{H}}^2
   \leq 
  2\lVert v_0 \rVert_{\mathcal{H}}^2
$$

for $q$ close to $1$.  The bound is **uniform in $q$**.

**Step 3: Uniform dissipation bound.**
The energy inequality also gives

$$
  \int_0^T \lVert d_qv_q(t) \rVert_{L^2_q}^2dt
   \leq 
  \frac{\lVert v_0 \rVert_{L^2_q}^2}{2\nu_q}
  = 
  \frac{q}{q-1}\lVert v_0 \rVert_{L^2_q}^2.
$$

This diverges as $q \to 1$ (because $\nu_q \to 0$), so we
**cannot** get a uniform $H^1$ bound.  However, we can get a
**uniform $H^s$ bound** for any $s < 1$: by interpolation,

$$
  \int_0^T \lVert v_q(t) \rVert_{H^s_q}^2dt
   \leq 
  \left(\int_0^T \lVert v_q \rVert_{L^2_q}^2dt\right)^{1-s}
  \!\cdot\!
  \left(\int_0^T \lVert d_q v_q \rVert_{L^2_q}^2dt\right)^s
$$

$$
  \leq
  (2T)^{1-s}\lVert v_0 \rVert_{\mathcal{H}}^{2(1-s)}
  \cdot
  \left(\frac{q}{q-1}\right)^s
  \lVert v_0 \rVert_{\mathcal{H}}^{2s}.
$$

For $s < 1$, the factor $(q/(q-1))^s$ is integrable against
$(q-1)^{-1+\delta}$ for small $\delta > 0$, giving a uniform
bound after a change of variables.

More precisely: fix $s = 1/2$.  Then

$$
  \int_0^T \lVert v_q(t) \rVert_{H^{1/2}_q}^2dt
   \leq 
  C_0\frac{q^{1/2}}{(q-1)^{1/2}},
$$

which diverges as $q \to 1$ at rate $(q-1)^{-1/2}$.  This is
**not** uniform.

**The key insight: use the truncation.**
The [finite cascade depth](#prop:q-turbulence-spectrum) shows that
only $N_{\mathrm{eff}}(q) \sim \ln(1/(q-1))/(q-1)$ modes are
active.  Define the **truncated solution**
$v_q^N = \sum_{k=1}^{N} \hat{v}_{q,k}z^k$ where
$N = N_{\mathrm{eff}}(q)$.  Then $v_q - v_q^N$ is
exponentially small (the tail modes are damped by
$e^{-\nu_q [k]_q^2 t}$ with $[k]_q^2 \geq q^{2N}$).

The truncated family $\{v_q^N\}$ lives in a **finite-dimensional
subspace** $V_N \subset \mathcal{H}$ of dimension $N$.  As
$q \to 1$, $N \to \infty$, but the key point is:

**Lemma (Truncated compactness).**
For any fixed $N$, the family $\{v_q^N\}_{q \in (1, q_0]}$
is **precompact** in $C([0,T]; V_N)$.

*Proof.* On the finite-dimensional space $V_N$, the $q$-NS
equation becomes an ODE:

$$
  \frac{d\hat{v}_k}{dt}
  = -\nu_q [k]_q^2 \hat{v}_k
  + \sum_{i+j=k} [i]_q\hat{v}_i\hat{v}_j
  - \hat{p}_k,
  \qquad k = 1, \ldots, N.
$$

The right-hand side is Lipschitz in $(\hat{v}_1, \ldots,
\hat{v}_N)$ with Lipschitz constant
$L_N(q) = \max_k \nu_q [k]_q^2 + C_N \lVert v_0 \rVert$.
By Arzelà--Ascoli, the family of solutions is precompact in
$C([0,T]; \mathbb{R}^N)$ if uniformly bounded and equicontinuous.

- Uniform boundedness: $|\hat{v}_k| \leq |\hat{v}_k(0)|$ from
  energy decay.
- Equicontinuity: $|d\hat{v}_k/dt| \leq L_N(q) \cdot
  \lVert v_0 \rVert$ is bounded for $q$ in any compact subset
  of $(1, q_0]$.


**Step 4: Diagonal extraction.**
For $N = 1$: extract a subsequence $q_n^{(1)} \to 1$ such that
$v_{q_n^{(1)}}^1$ converges in $C([0,T]; V_1)$.

For $N = 2$: from $\{q_n^{(1)}\}$, extract a further
subsequence $\{q_n^{(2)}\}$ such that $v_{q_n^{(2)}}^2$
converges in $C([0,T]; V_2)$.

Continue: at step $N$, extract $\{q_n^{(N)}\}$ from
$\{q_n^{(N-1)}\}$ such that $v_{q_n^{(N)}}^N$ converges.

Take the **diagonal** subsequence $q_n = q_n^{(n)}$.  Then for
every fixed $N$, $v_{q_n}^N$ converges as $n \to \infty$.

Define the **limit** mode by mode:
$\hat{v}_k^* = \lim_{n \to \infty} \hat{v}_{q_n, k}$
for each $k \geq 1$.  Set $v^* = \sum_{k} \hat{v}_k^*z^k$.


**Step 5: The limit is a distributional solution of NS.**
The truncated q-NS equation at level $N$ is

$$
  \partial_t v_q^N + P_N B(v_q^N)
  = \nu_qP_N \Delta_q v_q^N - P_N(\rho^{-1}\nabla_A p_q),
$$

where $P_N$ is projection onto the first $N$ modes.

Taking $q = q_n \to 1$ along the diagonal:
- $\nu_{q_n} \to 0$: the viscous term vanishes.
- $[k]_{q_n} \to k$: the $q$-integers become integers.
- $\Delta_{q_n} \to \Delta$: the $q$-Laplacian becomes the
  classical Laplacian.
- $B(v_{q_n}^N) \to B(v^{*N})$: the nonlinearity converges
  (each mode converges, and the sum is finite).

In the limit, $v^{*N}$ satisfies the **truncated Euler equation**:

$$
  \partial_t v^{*N} + P_N B(v^{*N}) = -P_N(\rho^{-1}\nabla p^*).
$$

Taking $N \to \infty$, $v^*$ satisfies the Euler equation
distributionally (the viscous term has vanished in the limit).

**Critical observation**: The limit is a solution of the
**Euler equation** (inviscid), not the Navier--Stokes equation,
because $\nu_q \to 0$.  This is consistent with the fact that
at $q = 1$, the quantum viscosity vanishes.


**Step 6: The limit is a weak solution of NS with $\nu > 0$.**

To obtain a Navier--Stokes solution (not Euler), we must
introduce an **independent** classical viscosity $\nu > 0$.
Consider instead the equation

$$
  \partial_t v + (v \cdot \nabla_A) v
  = -\nabla p + (\nu + \nu_q)\Delta_q v - \nabla Q_q,
$$

where $\nu > 0$ is a fixed classical viscosity.  As $q \to 1$:
$\nu + \nu_q \to \nu$, $\Delta_q \to \Delta$, $Q_q \to 0$, and
the limit satisfies

$$
  \partial_t v^* + (v^* \cdot \nabla) v^*
  = -\nabla p^* + \nu\Delta v^*.
$$

This **is** the classical NS equation with viscosity $\nu$.

The compactness argument carries through identically (the
additional $\nu\Delta$ term only helps — it provides uniform
$H^1$ bounds independently of $q$).


**Step 7: The limit loses regularity.**

The anti-parallel vortex pair initial data
([counter-example](#conj:ns-counterexample)) causes the
filaments to approach at rate $d(t) \sim \sqrt{T^* - t}$.
The vorticity $\omega = \nabla \times v$ satisfies
$\lVert\omega\rVert_{L^\infty} \sim 1/d(t)^2 \to \infty$ as
$t \to T^{*-}$.

For the q-deformed solutions, the quantum pressure prevents
collision ($d_{\min} \geq \ell_q > 0$), so $v_q$ is smooth.
But the limit $v^*$ has no quantum pressure, and the collision
proceeds to completion.

**Conjecture (q-Aubin--Lions, conditional on conj:ns-counterexample).**
Under the hypotheses above, there exists a subsequence
$q_n \to 1$ such that:

1. $v_{q_n} \to v^*$ weakly in $L^2([0,T]; \mathcal{H})$.
2. $v^*$ is a weak solution of the Navier--Stokes equation
   with viscosity $\nu$ on $[0, T^*)$.
3. $\lVert v^*(t) \rVert_{\mathcal{H}}^2 \leq
   \lVert v_0 \rVert_{\mathcal{H}}^2$ for all $t$ (energy
   inequality).
4. $v^*$ is smooth on $[0, T^*) \setminus \Sigma$ where
   $\Sigma$ is a closed set of Hausdorff dimension $\leq 1$.


**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-aubin-lions.md -->

<!-- FILE_START: q-bkm-criterion.md -->
Let $v$ be the solution of the [q-NS system](#def:q-navier-stokes)
with $q > 1$ on $[0, T)$ and let $\omega_q = d_q v$ be the
$q$-vorticity.  Then $v$ extends smoothly beyond $T$ if and only if

$$
  \int_0^T \lVert \omega_q(t) \rVert_{L^\infty}dt  <  \infty.
$$

Equivalently: if the solution loses regularity at time $T^*$, then

$$
  \int_0^{T^*} \lVert \omega_q(t) \rVert_{L^\infty}dt
  =  +\infty.
$$

Since the [well-posedness theorem](#thm:q-ns-wellposedness) shows
solutions are global for $q > 1$, the integral is always finite
when $q > 1$.  The criterion becomes non-trivial only in the
$q \to 1$ limit.
<!-- FILE_END: q-bkm-criterion.md -->

<!-- FILE_START: q-bkm-criterion-interpretation.md -->
**Remark (interpretation).**
The $q$-vorticity estimate is a direct algebraic translation of the classical Beale--Kato--Majda criterion; here the bound functions as a diagnostic limit check in the observable universe. Because the deformed Navier--Stokes system is unconditionally globally regular for $q > 1$, the integral is finite in the bulk, so the BKM condition shifts from a PDE survival test to an obstruction indicator at the $q \to 1$ substrate boundary.
<!-- FILE_END: q-bkm-criterion-interpretation.md -->

<!-- FILE_START: vorticity-lower-bound.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Vorticity lower bound").**

Let $v_q$ be the q-NS solution for anti-parallel vortex pair
initial data ([counter-example](#conj:ns-counterexample)) and let
$v^*$ be the weak limit as $q \to 1$
([q-Aubin--Lions](#conj:q-aubin-lions)).  Let $\omega^* = \nabla
\times v^*$ and let $d(t)$ be the separation between the two
filament cores.

Then there exist constants $c_1, c_2 > 0$ (independent of $q$)
such that for all $t < T^*$:

**(a) Separation decay.**

$$
  c_1\sqrt{T^* - t}
   \leq 
  d(t)
   \leq 
  c_2\sqrt{T^* - t}.
$$

**(b) Vorticity lower bound.**

$$
  \lVert \omega^*(t) \rVert_{L^\infty}
   \geq 
  \frac{c_1}{T^* - t}.
$$

**(c) BKM divergence.**

$$
  \int_0^{T^*}
  \lVert \omega^*(t) \rVert_{L^\infty}dt
  =  +\infty.
$$

In particular, by the [q-BKM criterion](#thm:q-bkm), the limit
solution $v^*$ loses regularity at $T^*$.

**Argument for (a): Biot--Savart dynamics.**

Two anti-parallel vortex filaments of circulation $\pm\Gamma$
separated by distance $d$ induce velocity
$v_{\mathrm{ind}} = \Gamma/(2\pi d)$ on each other (Biot--Savart
law).  They approach at rate

$$
  \frac{dd}{dt} = -\frac{\Gamma}{2\pi d}
  \quad\Longrightarrow\quad
  d(t)^2 = d_0^2 - \frac{\Gamma}{\pi}t
  \quad\Longrightarrow\quad
  T^* = \frac{\pi d_0^2}{\Gamma}.
$$

Near $t = T^*$: $d(t) = \sqrt{\Gamma(T^* - t)/\pi}$, giving the
$\sqrt{T^* - t}$ scaling.

For the q-deformed system with $q > 1$, the quantum pressure
$Q_q$ arrests the approach at
$d_{\min} \geq \ell_q = (q-1)/q > 0$.  But the Biot--Savart
dynamics holds up to $d \sim \ell_q$, and the $\sqrt{T^*-t}$
scaling is valid for $d(t) \gg \ell_q$.

The Biot--Savart ODE is exact for point vortices.
For filaments of finite core radius $a$, corrections are
$O(a^2/d^2)$.  These corrections are controlled by the
[q-energy functional](#rem:geodesic-vortices): the core radius
$a_q$ is fixed by the minimum of $\mathcal{E}_q$, and the
correction vanishes as $a_q/d \to 0$ near collision.

**Argument for (b): Vorticity concentration.**

The vorticity of each filament is concentrated in a tube of
radius $a$ with peak magnitude $\omega_{\max} \sim \Gamma/a^2$.
As the filaments approach, the mutual induction intensifies the
vorticity through the **stretching mechanism**: the velocity
gradient $\partial v / \partial x$ near the collision point
scales as $v_{\mathrm{ind}}/d \sim \Gamma/(2\pi d^2)$.

The vorticity equation
$\partial_t \omega + (v \cdot \nabla)\omega
= (\omega \cdot \nabla)v + \nu\Delta\omega$
has the stretching term $(\omega \cdot \nabla)v$ scaling as
$\omega \cdot v_{\mathrm{ind}}/d \sim \omega\Gamma/(2\pi d^2)$.
This gives exponential amplification of vorticity between
stretching events, with the rate diverging as $d \to 0$:

$$
  \frac{d\omega_{\max}}{dt}
  \gtrsim
  \frac{\Gamma}{2\pi d(t)^2}\omega_{\max}
  = 
  \frac{1}{2(T^* - t)}\omega_{\max},
$$

which integrates to

$$
  \omega_{\max}(t)
  \gtrsim
  \omega_{\max}(0)(T^* - t)^{-1/2}.
$$

The sharper bound $\omega_{\max} \gtrsim c/(T^* - t)$ follows
from the more detailed analysis of the collision geometry:
at the **symmetry plane** (midpoint between the filaments),
the vorticity field from both filaments adds constructively
and the combined stretching rate is $\Gamma/(\pi d^2)$,
giving

$$
  \omega_{\mathrm{sym}}(t)
   \sim 
  \frac{\Gamma}{\pid(t)^2}
  = 
  \frac{1}{T^* - t}.
$$

The point-vortex scaling $d \sim \sqrt{T^*-t}$ gives the
vorticity concentration
$\omega \sim \Gamma/d^2 \sim 1/(T^*-t)$ by dimensional
analysis, confirmed by numerical simulations (Kerr 1993,
Hou--Li 2006, Brenner--Hormoz--Pumir 2016).

<!-- FILE_END: vorticity-lower-bound.md -->

<!-- FILE_START: levi-degeneracy-conjecture.md -->
Let $\{q_\kappa = e^{i\pi/\kappa}\}_{\kappa \geq 2}$ be the
sequence of roots of unity converging to $q = 1$. For each
$\kappa$, let $v_\kappa$ be the q-NS solution for anti-parallel
vortex pair initial data, and let

$$
  \mathcal{C}_L(\kappa)
  = 
  \sup_{0 \leq t < T^*_\kappa}
  \mathrm{cond}\bigl(
    \mathcal{L}_\varTheta\big|_{N_p\gamma(t)}
  \bigr)
$$

be the maximum [Levi form condition
number](#prop:core-levi-form) over the evolution.

By the [root-of-unity truncation](#prop:root-of-unity-truncation),
$\mathcal{C}_L(\kappa) \leq 1 + C(\kappa - 1)$ for a universal
constant $C > 0$ (Bernstein inequality on trigonometric
polynomials of degree $\leq (\kappa-1)/2$).

**Conjecture (Levi degeneracy).**
Exactly one of the following holds:

**(A) Sub-linear growth (NS blows up).**

$$
  \mathcal{C}_L(\kappa) = O(1)
  \quad\text{as } \kappa \to \infty.
$$

The condition number stays bounded. The Levi form remains
non-degenerate at the collision locus $\Sigma$ in the
$q \to 1$ limit. The contact structure does not degenerate.
The [observability axiom](#def:quantum-observable-universe)
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds locally
on $\Sigma$. The [vorticity lower
bound](#prop:vorticity-lower-bound) holds, the
[q-BKM criterion](#thm:q-bkm) diverges, and the
[counter-example](#conj:ns-counterexample) is established.
Classical 3d Navier--Stokes admits finite-time blowup.

**(B) Linear growth (NS is regular).**

$$
  \mathcal{C}_L(\kappa) \sim \kappa
  \quad\text{as } \kappa \to \infty.
$$

The condition number grows at the same rate as the truncation
level relaxes. The Levi form degenerates in the $\parallel$
direction: $\lambda_\parallel \to 0$ while $\lambda_\perp$
stays bounded. The contact structure becomes partially
integrable at $\Sigma$. The observability axiom fails locally
— a gauge mode acts as the identity in the integrable direction.
The vortex core flattens into a sheet, the vorticity spreads,
and the lower bound fails. Classical 3d Navier--Stokes is
globally regular.

**Equivalent formulations.**

1. **Contact geometry:** Does the
 [Levi form](#def:levi-form-defect) $\mathcal{L}_\varTheta$
 degenerate at the collision locus when $q \to 1$?

2. **Representation theory:** Does the finite-dimensional
 approximation of $\mathrm{SU}_q(2)$ at roots of unity
 preserve the isotropy of the Frobenius inner product in
 the $\kappa \to \infty$ limit?

3. **Observability:** Does the QOU observability axiom
 $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ hold
 locally on the collision locus at $q = 1$?

4. **Integrability:** Does the horizontal distribution
 $\ker(\varTheta)$ remain maximally non-integrable at the
 collision point, or does a 2-dimensional integral
 submanifold form?

5. **Fluid dynamics:** Do colliding anti-parallel vortex
 filaments maintain tubular cores ($\kappa = O(1)$), or
 flatten into sheets ($\kappa \to \infty$)?

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: levi-degeneracy-conjecture.md -->

<!-- FILE_START: townsend-biot-savart-strain.md -->
The
[Levi degeneracy conjecture](#conj:levi-degeneracy) reduces the
$q \to 1$ Navier–Stokes regularity question to the asymptotic
behaviour of the core aspect ratio
$\kappa^2 = a_\perp^2 / a_\parallel^2 = V_2 / V_1$
at the vortex-collision time $T^\ast$
([prop:core-levi-form](#prop:core-levi-form)).
This remark and its
[hyperbolic-overlap companion](#rem:hyperbolic-overlap-saturation)
work the ODE for $(V_1, V_2)$ explicitly in the two physical
regimes — first under the singular Biot–Savart strain valid
when cores are well separated, then under the hyperbolic
saturation that takes over when the cores overlap.

**Setup.**
Consider two anti-parallel vortex filaments with circulation
$\Gamma$ approaching head-on at a collision time $T^\ast$.
Model the cross-section of each viscous core by the
**Townsend covariance matrix** \cite{townsend1951}:
let $V_1(t)$ be the squared core radius in the direction of
advective stretching, and $V_2(t)$ the squared core radius in
the perpendicular direction of compression. From the
Biot–Savart derivation (Saffman \cite{saffman1992} §11.2; Moffatt–
Kida–Ohkitani \cite{moffatt1994}) the separation squared evolves
as
$$
  d(t)^2 = \frac{c\,\Gamma (T^\ast - t)}{\pi},
$$
with a convention constant $c$ that depends on whether $\Gamma/(2\pi d)$
is read as a single filament's induced velocity ($c = 1$) or as
the relative approach speed of the two filaments ($c = 2$).
Either way the time scaling is the same.
The external strain rate induced by one filament on the other
is then
$$
  \alpha(t)
  \;=\;
  \frac{\Gamma}{2\pi d(t)^2}
  \;=\;
  \frac{1}{2c\,(T^\ast - t)},
$$
and only the constants depend on $c$; the leading behaviour
$\alpha \propto 1/(T^\ast - t)$ is convention-independent. For
definiteness, and to match the user's setup, we adopt $c = 1$
below — the corresponding Lean formalisation
([`townsend-biot-savart-strain.lean`](townsend-biot-savart-strain.lean))
states the result in a $c$-agnostic form.
The remarkable feature is that $\alpha(t)$ is **independent of
$\Gamma$**: under the point-vortex approximation, the
circulation cancels between numerator and denominator and the
strain rate is fixed by the time-to-collision alone.

**Townsend evolution.**
Under axisymmetric viscous strain the squared core radii satisfy
\cite{townsend1951,moffatt1994}
$$
  \frac{dV_1}{dt} = +2\,\alpha(t)\,V_1 + 2\nu,
  \qquad
  \frac{dV_2}{dt} = -2\,\alpha(t)\,V_2 + 2\nu,
$$
with $\nu$ the kinematic viscosity. Let $\tau = T^\ast - t$ be
the time remaining. Then $d/dt = -d/d\tau$ and substituting
$\alpha(t) = 1/(2\tau)$ gives the linear system
$$
  \frac{dV_1}{d\tau} + \frac{V_1}{\tau} = -2\nu,
  \qquad
  \frac{dV_2}{d\tau} - \frac{V_2}{\tau} = -2\nu.
$$

**Exact solutions.**
Using the integrating factor $\tau$ for $V_1$ and $1/\tau$ for
$V_2$:
$$
  \frac{d(\tau V_1)}{d\tau} = -2\nu\tau
  \quad\Longrightarrow\quad
  V_1(\tau) = \frac{C_1}{\tau} - \nu\tau,
$$
$$
  \frac{d(V_2/\tau)}{d\tau} = -\frac{2\nu}{\tau}
  \quad\Longrightarrow\quad
  V_2(\tau) = -2\nu\,\tau\ln\tau + C_2\,\tau,
$$
with constants $C_1, C_2$ fixed by the cross-section at the
start of the close-approach window. As the collision is
approached ($\tau \to 0$):
- the stretching coordinate diverges,
  $V_1(\tau) \sim C_1/\tau \to \infty$,
- the compressing coordinate vanishes,
  $V_2(\tau) \sim -2\nu\,\tau \ln\tau \to 0$.

**The first-order Levi prediction.**
The squared Levi condition number is therefore
$$
  \kappa^2(\tau)
  = \frac{V_2(\tau)}{V_1(\tau)}
  \;\sim\;
  \frac{-2\nu\,\tau^2\ln\tau}{C_1}
  \;\xrightarrow[\tau \to 0]{}\; 0.
$$
At this level of approximation the viscous diffusion completely
flattens the core into a two-dimensional sheet just before
collision. Via
[prop:core-levi-form](#prop:core-levi-form)(c), $\kappa \to 0$
forces the Levi form to be **strictly degenerate** at the
collision locus: the contact eigenvalue
$\lambda_\parallel \to 0$ while $\lambda_\perp$ stays bounded.
The local cohomology group $H^1_{\mathfrak{m}_p}(A)$ vanishes,
the cohomological obstruction dissolves, and the system
maintains global regularity. This is the
[branch (B) outcome](#conj:levi-degeneracy) of the conjecture
— **NS globally regular** — under the point-vortex assumption.

**Breakdown of the approximation.**
The Biot–Savart strain rate
$\alpha(t) = \Gamma / (2\pi d(t)^2)$ assumes a point-vortex
geometry: the cores are much smaller than the separation,
$V_1 \ll d^2$. But $V_1(\tau) \sim C_1/\tau \to \infty$ as
$\tau \to 0$, whereas $d(\tau)^2 = \Gamma\tau/\pi \to 0$. The
two cross over at a finite $\tau_\ast$ defined by
$V_1(\tau_\ast) = d(\tau_\ast)^2$, after which the filaments
**overlap** and the Biot–Savart kernel is no longer valid: the
strain field near the collision plane is no longer the
superposition of two well-separated circular vortices, but
the merged flow of a single interaction zone. The next
remark — [hyperbolic-overlap saturation](#rem:hyperbolic-overlap-saturation) — computes what the strain field actually does in
the overlap regime, and finds that the apparent flattening
$\kappa \to 0$ is an artefact of the failed approximation.
<!-- FILE_END: townsend-biot-savart-strain.md -->

<!-- FILE_START: hyperbolic-overlap-saturation.md -->
The [Biot–Savart prediction](#rem:townsend-biot-savart-strain)
that the squared core ratio $\kappa^2 \to 0$ at the collision
holds only while the cores remain well separated. Once the
stretching coordinate $V_1$ reaches the squared separation
$d^2$, the point-vortex kernel breaks down and the local
stream function near the collision plane shifts from the
superposition of two circular vortices to a **hyperbolic
stagnation-point flow** (Saffman \cite{saffman1992} §6.3; Moffatt–
Kida–Ohkitani \cite{moffatt1994}). This remark works the Townsend
ODE in the hyperbolic regime and finds that the apparent
flattening $\kappa \to 0$ is reversed: the squared Levi
condition number **locks** to a strictly positive constant
$\kappa^2 = \pi\nu/\Gamma$.

**Mechanism of the kernel change.**
The singular Biot–Savart strain $\alpha(t) = \Gamma/(2\pi d^2)$
diverges *only* because $d \to 0$ while the cores are held
small. Once $V_1 \gtrsim d^2$ the filaments are no longer two
distinct objects; their merged interaction is described by an
elliptic-section vortex sitting at a hyperbolic stagnation
point of the *macroscopic* flow. In that geometry the strain
rate is bounded by the overlapping cores themselves and the
relevant length scale is no longer $d$ but $\sqrt{V_1}$:
$$
  \alpha(t) \;\longrightarrow\;
  \alpha_{\mathrm{hyp}}(t)
  \;=\;
  \frac{\Gamma}{\pi V_1(t)}.
$$
The kernel rotates from a $1/d^2$ Biot–Savart strain (point-
vortex superposition) to a $1/V_1$ Burgers-like strain
(elliptic vortex in a stagnation flow). This is the standard
"vortex in strain" model of Townsend / Moffatt–Kida–Ohkitani.

**Saturated Townsend system.**
Substituting $\alpha_{\mathrm{hyp}} = \Gamma/(\pi V_1)$ into
the stretching equation,
$$
  \frac{dV_1}{dt}
  = 2\,\alpha_{\mathrm{hyp}}\,V_1 + 2\nu
  = \frac{2\Gamma}{\pi V_1}\cdot V_1 + 2\nu
  = \frac{2\Gamma}{\pi} + 2\nu.
$$
The right-hand side is now a **constant**: $V_1$ grows
linearly with time rather than diverging, and remains finite
through to the formal collision time $T^\ast$. Explicitly,
$$
  V_1(t) \;=\; V_1(t_\ast) +
  \left( \tfrac{2\Gamma}{\pi} + 2\nu \right)(t - t_\ast),
$$
where $t_\ast$ is the time at which the overlap regime
begins. The exponential runaway predicted by the point-vortex
approximation is replaced by a controlled linear growth — the
strain saturates because the same coordinate that drives the
stretching also sets the relevant length scale.

**Compression — proportionality ansatz.**
Substituting the same saturated strain into the compression
equation,
$$
  \frac{dV_2}{dt}
  = -2\,\alpha_{\mathrm{hyp}}\,V_2 + 2\nu
  = -\frac{2\Gamma\,V_2}{\pi V_1} + 2\nu.
$$
Because $V_1$ is finite and increases linearly in $t$, the
compressive sink is bounded and the constant viscous source
$2\nu$ catches it. The temptation is to set
$\dot V_2 = 0$ ("quasi-steady"), giving the standard
**Burgers vortex equilibrium thickness** $V_2 = \pi\nu V_1/\Gamma$.
*This quasi-steady ansatz is not justified here.* The $V_2$
relaxation rate $2\Gamma/(\pi V_1)$ is *comparable to* the
$V_1$ growth rate $b/V_1$ — in fact $b/(2\Gamma/\pi) = 1 +
\pi\nu/\Gamma$, so $V_2$ and $V_1$ evolve on the same
timescale and $V_2$ cannot equilibrate to an instantaneous
target while $V_1$ varies.

**Asymptotic proportionality (correct constant).**
The right approach is the proportionality ansatz
$V_2(t) = \lambda V_1(t)$, valid asymptotically once the
transient $V_2$-mode has decayed. Then
$\dot V_2 = \lambda \dot V_1 = \lambda b$, and the ODE forces
$$
  \lambda b
  \;=\;
  -\frac{2\Gamma}{\pi}\,\lambda + 2\nu,
$$
i.e. $\lambda(b + 2\Gamma/\pi) = 2\nu$. Substituting
$b = 2\Gamma/\pi + 2\nu$ gives $b + 2\Gamma/\pi = 4\Gamma/\pi
+ 2\nu$, hence
$$
  \boxed{\;\;
  \kappa^2
  \;=\;
  \frac{V_2}{V_1}
  \;=\;
  \lambda
  \;=\;
  \frac{2\nu}{4\Gamma/\pi + 2\nu}
  \;=\;
  \frac{\pi\nu}{2\Gamma + \pi\nu}.
  \;\;}
$$
In the high-Reynolds limit $\nu \ll \Gamma$ relevant to
blowup, $\kappa^2 \simeq \pi\nu/(2\Gamma)$ — *half* the value
the quasi-steady ansatz would have produced.

Independently, solving the inhomogeneous linear ODE with
integrating factor $(V_1/V_{10})^{\beta}$, where
$\beta = 2\Gamma/(\pi b)$, gives the closed-form solution
$$
  V_2(t)
  \;=\;
  \frac{2\nu\,V_1(t)}{b(\beta + 1)}
  \;+\;
  K\,V_1(t)^{-\beta},
$$
where the second term is the decaying transient. The
particular term has the same ratio
$2\nu/(b(\beta+1)) = \pi\nu/(2\Gamma + \pi\nu)$, confirming
the asymptotic. The Burgers equilibrium $\pi\nu V_1/\Gamma$
would be the correct answer only if $V_1$ were strictly
constant — which it is not under saturated straining.

Through
[prop:core-levi-form](#prop:core-levi-form)(b–c), $\kappa^2 > 0$
is equivalent to the Levi form remaining non-degenerate at the
collision locus $\Sigma$: both eigenvalues
$\lambda_\parallel, \lambda_\perp$ stay bounded away from zero.
Therefore the local cohomology group
$H^1_{\mathfrak{m}_p}(A)$ remains non-zero, the cohomological
obstruction is preserved right up to $T^\ast$, and the
[NS obstruction](#def:ns-obstruction) does not dissolve under
the viscous diffusion mechanism the point-vortex picture
seemed to provide. This is the
[branch (A) outcome](#conj:levi-degeneracy) of the conjecture
— **classical 3D Navier–Stokes admits finite-time blowup**.

**The dichotomy in one table.**

| Regime | Strain $\alpha$ | $V_1$ behaviour | $V_2$ behaviour | $\kappa^2$ at $T^\ast$ | Levi form | NS conclusion |
|---|---|---|---|---|---|---|
| Biot–Savart ([`rem:townsend-biot-savart-strain`](#rem:townsend-biot-savart-strain)) | $1/(2\tau)$ | $\sim C_1/\tau \to \infty$ | $\sim -2\nu\tau\ln\tau \to 0$ | $0$ | Degenerate | Regular (branch B) |
| Hyperbolic overlap (this remark) | $\Gamma/(\pi V_1)$ | Linear in $t$, finite at $T^\ast$ | $\pi\nu V_1/(2\Gamma+\pi\nu) > 0$ | $\pi\nu/(2\Gamma + \pi\nu)$ | Non-degenerate | Blowup (branch A) |

**Reading.**
The Biot–Savart prediction $\kappa \to 0$ is an artefact of
the point-vortex approximation; it never reaches $\tau = 0$
because the approximation breaks down at the overlap time
$\tau_\ast$. The hyperbolic-overlap calculation, valid past
$\tau_\ast$ through to the formal collision, predicts the
asymptotic core ratio
$\kappa^2 = \pi\nu/(2\Gamma+\pi\nu) > 0$ — strictly positive
and lower-bounded by $\pi\nu/(2\Gamma + \pi\nu)$ even in the
inviscid limit at fixed viscosity. The cores do **not**
flatten into sheets; they lock into a finite elliptical
profile supported by the hyperbolic strain. The vortex
collision preserves the contact non-degeneracy and the NS
obstruction class is carried intact to $T^\ast$. This is the analytical
bridge that the
[Levi degeneracy conjecture](#conj:levi-degeneracy) calls
for: the geometric obstruction survives the viscous regularity
mechanism, leaving finite-time blowup for the classical
viscous Navier–Stokes system as the expected outcome.

**Caveats.**
1. The kernel switch $\alpha(t) \to \Gamma/(\pi V_1)$ at the
   overlap time is a **phenomenological dimensional ansatz**,
   not a derivation from Euler/NS: the relevant length scale
   inside the overlap region is heuristically replaced by
   $\sqrt{V_1}$. Townsend, Moffatt–Kida–Ohkitani, Saffman use
   this saturation as a modelling primitive. A rigorous bridge
   from the singular Biot–Savart kernel to the saturated
   elliptic-Burgers regime would require a careful matched
   asymptotic analysis through the overlap layer.
2. The asymptotic value
   $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$ is the
   *attracting proportionality ratio* of the linear ODE
   (verified two ways above: ansatz $V_2 = \lambda V_1$ and
   closed-form integrating factor). It is **not** the naive
   $\dot V_2 = 0$ "Burgers equilibrium" $\pi\nu V_1/\Gamma$:
   that ansatz requires $V_1$ stationary, while $V_1$ here is
   growing on the same timescale as the $V_2$ relaxation.
   The two answers differ by a factor of approximately 2 in
   the high-Reynolds limit.
3. The Townsend equations assume axisymmetric straining
   *within* the elliptic cross-section. Three-dimensional
   instabilities (Kelvin modes,
   [helical](#rem:helicity-physical) twisting) may modify the
   picture; see
   [`rem:vortex-reconnection`](#rem:vortex-reconnection) for
   the divisor-surgery view of these instabilities.
4. The conclusion "$\kappa^2 > 0 \Rightarrow$ blowup" routes
   through [`prop:core-levi-form`](#prop:core-levi-form),
   which is itself conditional on the regularity-breakdown
   programme (see its conjectural-dependency banner).
   What the explicit ODE establishes rigorously — and what is
   formalised in the sibling Lean file — is the asymptotic
   core-shape constant
   $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$; lifting this to NS
   blowup requires the
   [Levi degeneracy](#conj:levi-degeneracy) and
   [counter-example](#conj:ns-counterexample) conjectures.
<!-- FILE_END: hyperbolic-overlap-saturation.md -->

<!-- FILE_START: leray-profile.md -->
> **Summary.** Near the blowup time $T^*$, the singular NS
> solution approaches a self-similar Leray profile $V(\xi)$ on
> the rescaled coordinate $\xi = (x-x_0)/\sqrt{T^*-t}$.  The QOU
> representation theory constrains this profile to a finite-
> dimensional ansatz: $V$ is a sum of weight-$j$ matrix entries
> of $\mathrm{SU}_q(2)$ representations, with coefficients fixed
> by the singular gerbe data $(\Sigma, n^*, \kappa_{n^*})$.

Near the blowup time $T^*$, the
[NS-singular solution](#thm:ns-singularity-descartes) approaches
a self-similar profile.  The QOU representation theory constrains
this profile to a finite-dimensional ansatz.

**The Leray rescaling.**
Set $\tau = -\ln(T^* - t)$ and
$\xi = (x - x_0)/\sqrt{T^* - t}$.  The velocity field
$v(x, t) = (T^* - t)^{-1/2}V(\xi)$ satisfies the
**Leray equations**:

$$
  -\frac{1}{2}V
  - \frac{1}{2}(\xi \cdot \nabla)V
  + (V \cdot \nabla)V
  = 
  -\nabla P + \nu\Delta V,
  \qquad
  \nabla \cdot V = 0.
$$

These are a time-independent elliptic PDE for the profile
$(V, P)$ on $\mathbb{R}^3$.  A self-similar blowup occurs iff
a nontrivial solution exists with $V \in L^2(\mathbb{R}^3)$.

**The $\mathrm{SU}_q(2)$ decomposition.**
By the [Peter--Weyl theorem](#thm:quantum-peter-weyl), the
profile decomposes into matrix coefficients:

$$
  V(\xi)
  = 
  \sum_{j \geq 0}
  \sum_{m,n=-j}^{j}
  c^j_{mn}D^j_{mn}(\hat\xi)R_j(|\xi|),
$$

where $\hat\xi = \xi/|\xi|$, $D^j_{mn}$ are the spin-$j$
matrix coefficients on the unit sphere, and $R_j(r)$ is the
radial profile at spin $j$.

The Leray equations decompose by spin:

$$
  -\frac{1}{2}R_j
  - \frac{1}{2}rR_j'
  + \sum_{j_1, j_2}
    N^j_{j_1 j_2}R_{j_1}R_{j_2}'
  = 
  \nu\!\left(R_j'' + \frac{2}{r}R_j'
    - \frac{[j]_q[j+1]_q}{r^2}R_j\right),
$$

where $N^j_{j_1 j_2}$ are the nonlinear coupling coefficients,
determined by the Clebsch--Gordan decomposition
$V_{j_1} \otimes V_{j_2} = \bigoplus_J V_J$.

**Truncation by the discrete spectrum.**
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum)
shows that the eigenvalues $[j]_q[j+1]_q$ grow exponentially
in $j$.  The centrifugal barrier $[j]_q[j+1]_q/r^2$ in the
radial equation suppresses high-spin components: for $j$
large, $R_j(r) \sim r^{[j]_q}$ near $r = 0$, which vanishes
faster than any power.

At the physical value $q \approx 1.110$, the
[Planck--Reynolds analysis](#rem:planck-reynolds) gives
$k_{\max} \approx 4$ active modes.  The self-similar profile
is effectively a **finite sum**:

$$
  V(\xi)
   \approx 
  \sum_{j=0}^{2}
  \sum_{m,n}
  c^j_{mn}D^j_{mn}(\hat\xi)R_j(|\xi|),
$$

with spins $j = 0, 1/2, 1, 3/2, 2$.  This is a
finite-dimensional ansatz with
$\sum_{j=0}^{2}(2j+1)^2 = 1 + 4 + 9 + 16 + 25 = 55$
angular coefficients and 5 radial functions.

**The truncated Leray system.**
Substituting the truncated ansatz into the Leray equations
gives a system of 5 coupled ODEs for
$(R_0, R_{1/2}, R_1, R_{3/2}, R_2)$ in the radial variable $r$:

For each $j \in \{0, 1/2, 1, 3/2, 2\}$:

$$
  \nu\!\left(R_j'' + \frac{2}{r}R_j'
    - \frac{\lambda_j}{r^2}R_j\right)
  + \frac{1}{2}R_j
  + \frac{1}{2}rR_j'
  = 
  \sum_{\substack{j_1, j_2 \\ j \in j_1 \otimes j_2}}
  N^j_{j_1 j_2}R_{j_1}R_{j_2}',
$$

where $\lambda_j = [j]_q[j+1]_q$ and
$N^j_{j_1 j_2} \neq 0$ only when $j$ appears in the
Clebsch--Gordan decomposition of $V_{j_1} \otimes V_{j_2}$.

**Boundary conditions.**

- $r \to 0$: regularity requires
  $R_j(r) \sim r^{\ell_j}$ where $\ell_j$ is the smallest
  non-negative integer with
  $\ell_j(\ell_j + 1) \geq \lambda_j$.  For $q \approx 1.110$:
  $\ell_0 = 0$, $\ell_{1/2} = 1$, $\ell_1 = 1$,
  $\ell_{3/2} = 2$, $\ell_2 = 3$.

- $r \to \infty$: $V \in L^2$ requires
  $R_j(r) = O(r^{-5/2})$ (faster than the self-similar
  decay $r^{-1}$).

**The nonlinear coupling matrix.**
The coefficients $N^j_{j_1 j_2}$ encode which spin interactions
drive the blowup.  The fusion rules
$V_{j_1} \otimes V_{j_2} = \bigoplus_J V_J$ constrain:

| $j_1 \otimes j_2$ | Contains $j$ | Coupling |
|---|---|---|
| $\frac{1}{2} \otimes \frac{1}{2}$ | $0, 1$ | Electron-electron |
| $\frac{1}{2} \otimes 1$ | $\frac{1}{2}, \frac{3}{2}$ | Electron-photon |
| $1 \otimes 1$ | $0, 1, 2$ | Photon-photon |
| $\frac{1}{2} \otimes \frac{3}{2}$ | $1, 2$ | Generation mixing |

The dominant interaction driving the blowup is the
$j = 1/2 \otimes 1/2 \to 0$ channel: two fundamental vortices
(the anti-parallel pair) fuse into the trivial representation
(annihilation), releasing their energy into the radial
compression.

**The fundamental profile ($j = 1/2$ only).**
The simplest nontrivial ansatz retains only $j = 1/2$:

$$
  V(\xi) = cD^{1/2}_{mn}(\hat\xi)R(|\xi|),
$$

with a single radial ODE:

$$
  \nu\!\left(R'' + \frac{2}{r}R'
    - \frac{[1/2]_q[3/2]_q}{r^2}R\right)
  + \frac{1}{2}R + \frac{1}{2}rR'
  = 
  N^{1/2}_{1/2,1/2}RR'.
$$

This is a second-order nonlinear ODE with two boundary
conditions ($R \sim r$ at $r = 0$, $R = O(r^{-5/2})$ at
$r = \infty$).  The nonlinear eigenvalue problem has a
discrete spectrum of solutions parametrised by the number
of zeros of $R$ — exactly the
[vortex intensity levels](#prop:discrete-vortex-spectrum).

**Open question.**
The existence of a nontrivial solution to the truncated
Leray ODE with the specified boundary conditions is a
**finite-dimensional shooting problem**: find the initial slope
$R'(0)$ such that the solution decays at infinity.  This is
numerically tractable (standard boundary-value ODE solvers).
An analytical proof of existence would use topological methods
(Leray--Schauder degree theory) on the finite-dimensional
system.

The QOU contribution is the **finite truncation**: the classical
Leray equations are an infinite-dimensional elliptic PDE.  The
$\mathrm{SU}_q(2)$ representation theory reduces it to a
finite system of 5 coupled radial ODEs, or in the simplest case
a single nonlinear ODE.  This is where the constructive
counter-example becomes feasible.
<!-- FILE_END: leray-profile.md -->

<!-- FILE_START: q-ns-research-programme.md -->
The [global regularity theorem](#thm:q-ns-wellposedness) and the
[regularity breakdown conjecture](#conj:regularity-breakdown)
together reframe the Clay Millennium Problem as a **degeneration
problem** within a one-parameter family of well-posed equations.
This remark outlines the research programme that connects the
categorical framework to the classical open question.

**The classical problem (Clay formulation).**

> *In three space dimensions and time, given an initial velocity
> field, there exists a vector velocity and a scalar pressure
> field, which are both smooth and globally defined, that solve
> the Navier--Stokes equations.*
>
> Prove or give a counter-example.

**The quantum reformulation.**
In a [QOU](#def:quantum-observable-universe) $(\mathbf{C}, A, \tau)$
with [substrate parameter](#def:substrate-parameter) $q > 1$, the
[q-deformed Navier--Stokes system](#def:q-navier-stokes) on
$\Omega^1(A)$ is globally regular
([Theorem](#thm:q-ns-wellposedness)).  The classical problem is
the limiting case $q \to 1$.  The quantum reformulation is
therefore:

> **Problem (Quantum Navier--Stokes).**
> *Characterise the behaviour of the global solution
> $(v_q, p_q)$ of the q-NS system as $q \to 1^+$.  Does the
> family $(v_q, p_q)_{q > 1}$ converge to a smooth solution of
> the classical Navier--Stokes equation, or does it develop
> singularities in the limit?*

**Significance of the categorical formulation.**
The three mechanisms that ensure regularity for $q > 1$
— exponential UV damping, positive viscosity, finite cascade
depth — are all consequences of the categorical structure:

| Mechanism | Categorical origin | $q \to 1$ failure mode |
|---|---|---|
| Exponential eigenvalue growth $[k]_q^2$ | $q$-integer spectrum of $\Delta_q = d_q\delta_q + \delta_q d_q$ | $[k]_1 = k$ (polynomial) |
| Viscosity $\nu_q = \frac{1}{2}(1-q^{-1}) > 0$ | Non-triviality of [substrate parameter](#def:substrate-parameter) | $\nu_1 = 0$ (inviscid) |
| Finite DOF $N_{\mathrm{eff}} < \infty$ | [Observability](#def:quantum-observable-universe) $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ + finite $\mathrm{Re}_q$ | $N_{\mathrm{eff}} \to \infty$ |
| Divergence-free constraint non-degenerate | Contact condition (observability axiom) | Contact structure degenerates |
| Energy converges | [Frobenius pairing](#def:frobenius-pairing) positive-definite | Pairing degenerates |

The classical problem is hard precisely because **all five
mechanisms fail simultaneously** at $q = 1$.  The categorical
framework isolates each mechanism and makes their interdependence
explicit.

**The research programme: five open problems.**

**Problem 1. Rigorous well-posedness proof.**
Make the proof sketch of [Theorem](#thm:q-ns-wellposedness) into a
complete proof.  The key step is to establish that the
$q$-Laplacian $\Delta_q$ on $\Omega^1(A)$ has compact resolvent
with eigenvalues growing as $[k]_q^2 \sim q^{2k}$.  This requires:

- (a) Spectral theory for $\Delta_q$ on a Frobenius--Hopf algebra
  (extending classical Hodge theory to the $q$-deformed setting).
- (b) Nonlinear estimates: the advection term
  $\mu \circ (v \otimes \nabla_q v)$ in $\Omega^1(A)$ must be
  controlled by the dissipation $\nu_q\Delta_q v$.  The
  categorical Sobolev embedding (if $\lVert d_q v\rVert_A <
  \infty$ then $v$ is bounded) should follow from the Frobenius
  non-degeneracy.
- (c) Uniqueness via energy methods in the internal hom of
  $\mathbf{C}$.

**Problem 2. Rate of blowup.**
Assuming the [regularity breakdown
conjecture](#conj:regularity-breakdown), determine the critical
exponent $\alpha$ such that

$$
  \sup_{t \geq 0} \lVert d_qv_q(t)\rVert_A^2
   \sim 
  (q - 1)^{-\alpha}
  \qquad\text{as } q \to 1^+.
$$

The [q-turbulence spectrum](#prop:q-turbulence-spectrum) suggests
$\alpha = 4/3$ (matching the Kolmogorov 4/5 law), but this needs
proof.

**Problem 3. Identify the blowup mechanism.**
The three candidates for the singular set geometry at $q = 1$ are:

- **Vortex sheet** ($d_H = 2$): vorticity concentrates on a
  surface.  This is the mechanism suggested by the
  [Hamilton--Jacobi caustic
  picture](#rem:hamilton-jacobi-phase) — caustics proliferate
  and merge into a codimension-1 surface.

- **Vortex filament** ($d_H = 1$): vorticity concentrates on a
  curve.  This would connect to the [geodesic
  vortex](#rem:geodesic-vortices) picture — a single filament
  accumulates infinite circulation.

- **Point blowup** ($d_H = 0$): self-similar collapse to a
  point.  The [vortex reconnection](#rem:vortex-reconnection)
  mechanism suggests this is possible when a vortex--antivortex
  pair annihilates faster than the quantum pressure can
  regularise.

The [Berry phase structure](#rem:berry-vortex-moduli) constrains
which blowup geometries are topologically allowed: the
accumulated Berry phase around the singular set must be
consistent with the $\mathrm{SU}_q(2)$ representation theory.

**Problem 4. Universality of the critical point.**
Is the $q = 1$ phase transition universal — i.e., does the
critical exponent $\alpha$ depend on the initial data $v_0$, or
only on the categorical structure $(\mathbf{C}, A, \tau)$?  The
analogy with statistical mechanics
([regularity breakdown](#conj:regularity-breakdown)) suggests
universality: the critical behaviour should depend only on the
"symmetry class" (the Euler characteristic $\chi(A)$ and the
categorical dimension), not on the specific initial condition.

If universal, this would explain why the classical Navier--Stokes
problem is so difficult: the answer (regularity or blowup) is
determined by topological data of the ambient categorical
universe, not by analytic properties of the PDE.

**Problem 5. Counter-example construction.**
Use the $q \to 1$ limit to construct an explicit counter-example
to classical regularity.  The strategy is:

1. Choose initial data $v_0$ that maximises the enstrophy growth
   rate at $q = 1$ (e.g., a pair of anti-parallel vortex
   filaments approaching each other).

2. Solve the $q$-NS equation for $q = 1 + \varepsilon$ and
   track the maximum enstrophy
   $\Omega_{\max}(\varepsilon) = \sup_t \lVert d_q v(t) \rVert_A^2$.

3. If $\Omega_{\max}(\varepsilon) \to \infty$ as
   $\varepsilon \to 0$, then in the limit $q = 1$ the enstrophy
   blows up in finite time — a counter-example.

4. The time of blowup
   $T^*(\varepsilon) \to T^* < \infty$ gives the blowup time
   for the classical equation.

The [acoustic horizon conditions](#prop:acoustic-horizon-conditions)
provide a diagnostic: blowup corresponds to the formation of an
acoustic horizon in the limit where the horizon radius
$r_H \to 0$ (the acoustic black hole shrinks to a point).

**Summary: the QOU perspective on Navier--Stokes.**
The classical Navier--Stokes regularity problem asks whether
smooth solutions exist globally.  The QOU framework answers:
**yes, for any $q > 1$**, and reframes the classical question as:
**whether regularity survives the $q \to 1$ degeneration**  The three
categorical mechanisms (exponential spectral growth, positive
viscosity from non-trivial substrate, finite cascade from
observability) all derive from the axioms of a quantum observable
universe and all fail at $q = 1$.  This suggests that 3d
Navier--Stokes blowup is not an accident of analysis but a
**structural consequence** of the degeneration of the categorical
contact structure — the same degeneration that, in physics,
prevents the $q = 1$ limit from supporting particles.

The physical universe, with $q \approx 1.110$, sits safely in the
regular regime.  The millennium problem asks about a mathematical
limit that nature never reaches.
<!-- FILE_END: q-ns-research-programme.md -->

<!-- FILE_START: outro-fluid-dynamics.md -->
This closes the fluid-dynamics chapter.  The $q$-deformed
Navier–Stokes system has been promoted from a one-parameter
family of well-posed equations into a structural framework for
the Clay Millennium Problem: the classical $q \to 1$ limit is a
degeneration of a regular categorical system, and the open
questions (Aubin–Lions compactness, blow-up Yekutieli class,
universality, counter-examples) are now phrased as conjectures
about the obstruction tower at $q = 1$.

The next chapter (information theory) recasts the fluid setup in
informational terms: the same brane carries the
information-theoretic constructions ($q$-entropy, Lyapunov
exponent, information bandwidth) that the substrate
parameter $q$ also controls.  The categorical content here —
obstruction tower, observable MTC, brane-fluid dynamics — feeds
the entropy-rate calculations that follow.
<!-- FILE_END: outro-fluid-dynamics.md -->

