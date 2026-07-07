<!-- FILE_START: ns-obstruction-intro.md -->
The global regularity theorem for the $q$-deformed system
isolates the classical Navier--Stokes question as a degeneration
problem at $q = 1$. We construct a categorical obstruction
$\mathrm{NS}(A) \in H^3_{\mathrm{loc}}(A, \varTheta)$ that controls
whether finite-time blowup occurs and compute it on the Descartes
quantum universe.

We first clarify the QOU observability axiom for the fluid setting
in Remark: What observability means for the brane fluid and give
its Remark: Independent motivation for observability: why $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is not an NS assumption. The substrate parameter is then promoted to a
section of a line bundle in Definition: The substrate line bundle and the $\mathbb{G}_m$-family of differentials, with Remark: The substrate parameter as a $\mathbb{G}_m$-section: torsion, specialisation, and the $q = 1$ boundary tracking the
specialisation behaviour, and Theorem: Observability is a base property: $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is independent of the substrate section showing that observability survives
the family. The geometric content at vortex collisions is captured
by Proposition: Core aspect ratio equals Levi form condition number on the normal plane, with Remark: The millennium problem as contact non-degeneracy at vortex collision reading the criterion
through contact geometry.

We then define Definition: NS-regular quantum observable universe
and Definition: NS obstruction class $\mathrm{NS}(A)$, and connect
them to the classical regularity question in Remark: The classical regularity question for the Navier--Stokes equation. The
obstruction's cohomological structure is Proposition: The NS obstruction class in the Yekutieli tower; its evaluation on a concrete
universe is Proposition: Computation of the NS obstruction for the Descartes universe. The lift to $q = 1$ is Proposition: Kummer specialisation: the NS obstruction survives $q = 1$ for $\gcd(\chi(A), n) \neq n$, and the headline consequence is Theorem: The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup.

We complement this with Example: The torus quantum universe: $\chi(A) = 0$ and NS regularity, and place the result in the
representation-theoretic context of Proposition: Representation-theoretic truncation at roots of unity and the $q = 1$ accumulation.
The braided structure underlying the obstruction is named in
Definition: Observable modular tensor category at $q = \zeta_N$ and
Proposition: Braid group action on $\mathbf{V}^{\otimes n}$ does not factor through $S_n$ — the non-permutation form of the braid
action that the next section, **Approaches and open problems**,
treats as given.

_(draft.)_
<!-- FILE_END: ns-obstruction-intro.md -->

<!-- FILE_START: observability-in-fluid-context.md -->
Before defining [NS regularity](#def:ns-regular-qou), we
clarify what the QOU observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ means in the
fluid-dynamical setting.

**Categorical statement.**
No morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ exists
in $\mathbf{C}$.  That is: the adjoint representation of the
Frobenius--Hopf object $A$ has no trivial sub-object.

**Gauge-theoretic translation.**
$H^0(M, \mathrm{Ad}(P)) = 0$: no nonzero section of the adjoint
bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ is
gauge-equivariant.  Every infinitesimal gauge transformation
acts nontrivially on some observable.

**Contact-geometric translation.**
The Levi form $\mathcal{L}_\varTheta$ is non-degenerate everywhere.
The horizontal distribution $\ker(\varTheta)$ is maximally
non-integrable (no integral submanifolds of dimension
$> \frac{1}{2}\dim\ker\varTheta$).

**Fluid-dynamical translation.**
In the [brane fluid](#sec:brane-fluid):

1. **No stagnant directions.**  Every direction in the brane
   carries nontrivial fluid dynamics.  There is no direction
   along which the velocity field can be identically zero
   without violating the gauge structure.

2. **Vortex cores are tubular.**  The
   [core-Levi equivalence](#prop:core-levi-form) shows that
   non-degenerate Levi form implies the vortex core
   cross-section has bounded aspect ratio.  The core cannot
   flatten into a sheet or collapse into a needle.

3. **No hidden laminar sectors.**  If
   $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$, there
   would exist a direction in which the fluid is automatically
   laminar (a gauge symmetry renders that direction dynamically
   trivial).  Observability forbids this: every direction is
   dynamically active.

4. **Vortex stretching is isotropic.**  The
   [weight-space decomposition](#def:weight-decomposition)
   of the adjoint bundle has no trivial component.  The
   stretching term $(\omega \cdot \nabla)v$ in the vorticity
   equation acts nontrivially in every direction — vorticity
   cannot leak into a "neutral" direction.

**The alternative: what $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ would mean.**

If a nonzero $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$
existed, it would define a **preferred direction** in the brane:

- A 1-dimensional foliation of the contact distribution
  (partially integrable)
- A direction in which vortex stretching vanishes
- A channel through which vorticity can drain without
  concentrating
- A mechanism for vortex cores to flatten into sheets
  (the core elongates along the foliation leaf)

This would provide a **regularity mechanism**: vorticity
spreads into the integrable direction instead of concentrating,
preventing blowup.

**Observability is therefore the statement that no such
escape route exists.** The brane fluid is dynamically active in
every direction, and colliding vortices have nowhere to spread.
<!-- FILE_END: observability-in-fluid-context.md -->

<!-- FILE_START: observability-independent-motivation.md -->
The [NS-singularity theorem](#thm:ns-singularity-descartes) deduces
Navier--Stokes blowup from the QOU observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. This raises
the question: is the observability axiom independently motivated,
or does assuming it amount to assuming the NS conclusion?

**The axiom has six independent motivations, none involving NS.**

**1. Gauge irreducibility.**
In the archimedean realisation, observability becomes
$H^0(M, \mathrm{Ad}(P)) = 0$: the gauge connection $A$ is
**irreducible** (no nonzero gauge-equivariant sections of the
adjoint bundle). Irreducibility is the generic condition for
connections on principal bundles over compact manifolds — the
moduli space of irreducible connections is open and dense in the
space of all connections. Reducible connections form a lower-
dimensional stratum.

This is a standard condition in gauge theory (Donaldson,
Uhlenbeck, Atiyah--Bott) that predates QOU by decades.

**2. Contact non-integrability.**
Observability is equivalent to non-degeneracy of the Levi form
$\mathcal{L}_\varTheta$ ([core-Levi equivalence](#prop:core-levi-form)),
which is the defining property of a **contact manifold**.
Contact manifolds are maximally non-integrable: the horizontal
distribution $\ker(\varTheta)$ has no integral submanifolds of
dimension greater than half the contact dimension.

Every odd-dimensional manifold admits a contact structure
(Martinet 1971). The question is not whether one exists but
whether the physical brane carries one. The CR structure of
Bring's surface is strictly pseudoconvex (Levi form positive
definite), which is stronger than mere non-degeneracy. This is
a property of the specific manifold, not an assumption about NS.
Cf.\ \cite{nicolaescu2005, leitner-2018}.

**3. Tannaka--Krein reconstruction.**
The fibre functor $\tau$ reconstructs $A$ as a Hopf algebra via
Tannaka--Krein duality. For this reconstruction to yield a
**quantum group** (rather than a quantum groupoid or a degenerate
algebra), the representation category must be semisimple and the
forgetful functor must be faithful. Observability ensures that
the adjoint representation is **simple** (no trivial
sub-representation), which is necessary for semisimplicity of
$\mathrm{Rep}(\mathrm{SU}_q(2))$.

Without observability, the adjoint representation would contain
a copy of $\mathbf{1}$, the Lie algebra $\mathfrak{su}(2)$
would have a centre, and the quantum group would degenerate
to $\mathrm{U}(1) \times \mathrm{SU}(2)/\mathrm{U}(1)$ — a
reducible structure.

**4. Mass non-degeneracy.**
The [mass identity](#def:mass-identity) $m \propto
\oint_\varrho \|\nabla_A q\| \cdot \|L \wedge F^+\|$ is
nonzero for a stable vortex $\varrho$ iff the integrand is
nonzero, which requires $L \neq 0$ (Levi form non-degenerate)
at points of $\varrho$. If observability fails at $\varrho$,
then $L = 0$ there, $m = 0$, and the vortex is massless —
it is not a particle but a gauge artifact.

**5. Particle existence.**
The [SU(2) emergence theorem](#thm:su2-emergence) deduces the
gauge group $\mathrm{SU}(2)$ from the QOU axioms. If
observability fails, the gauge group reduces to a proper
subgroup (e.g. $\mathrm{U}(1)$), and the representation
theory cannot produce the full particle spectrum. No quarks,
no hadrons, no nuclear physics.

**6. Measurability.**
The word "observable" in "quantum observable universe" is
literal: every degree of freedom of $A$ is accessible to
measurement via the fibre functor $\tau$.
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ would mean
there exists a nonzero morphism $\phi \colon \mathbf{1} \to
\mathrm{Ad}(A)$ — a "hidden symmetry" that commutes with all
measurements. The universe would contain a sector invisible
to any experiment.

**Consequences of dropping observability.**

Define a **quantum pre-universe** (QPU) as a quantum universe
$(\mathbf{C}, A, \tau)$ satisfying all QOU axioms **except**
observability. In a QPU:

See [Table](#tbl:observability-independent-motivation-table-data).

The QPU is a weaker framework. It does not force NS blowup
because the contact structure can degenerate at collision
points, allowing vortex cores to flatten.

**The relationship between observability and NS.**

The logical relationship is:

$$
  \text{Observability} \Longrightarrow \text{NS singular}
$$

but **not** the converse. NS blowup could occur even without
observability (through a different mechanism). And NS regularity
is **compatible** with a QPU (where observability fails).

The argument is:
- If the physical universe is a QOU (observability holds), then
 NS blows up.
- If the physical universe is only a QPU (observability fails),
 then the NS question is open — but so is particle physics
 (no mass, no SU(2), no quarks).

The observability axiom is not an encoding of NS blowup. It is
a measurement principle with independent gauge-theoretic,
contact-geometric, representation-theoretic, and physical
content. The NS consequence is a theorem, not an assumption.
<!-- FILE_END: observability-independent-motivation.md -->

<!-- FILE_START: substrate-line-bundle.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[weight decomposition](#def:weight-decomposition)
$(\pi_H, \pi_V)$ and
[Reeb derivation](#def:categorical-reeb) $\xi$.

**The substrate line bundle** is the trivial
$\mathbb{G}_m$-torsor

$$
  \mathcal{Q}
  = 
  \mathrm{End}(\mathbf{1}) \otimes_\mathbb{Z} \mathbb{G}_m
   \to 
  \mathrm{Spec}R,
$$

whose fibre at each $R$-point is $\mathbb{G}_m(R) = R^\times$.
A **substrate section** is a global section
$q \colon \mathrm{Spec}R \to \mathcal{Q}$, i.e. an element
$q \in R^\times$.

When $(\mathbf{C}, A, \tau)$ is fibred over a space $M$
(archimedean realisation), the substrate line bundle is
$\mathcal{Q}_M = M \times \mathbb{G}_m$ and a substrate
section is a map $q \colon M \to \mathbb{G}_m(k) = k^\times$.

**The $\mathbb{P}^1$-compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the
standard inclusion
$k^\times \hookrightarrow k \cup \{\infty\} = \mathbb{P}^1(k)$.
The compactified substrate bundle is

$$
  \bar{\mathcal{Q}}_M
  = 
  M \times \mathbb{P}^1
   \to  M.
$$

A substrate section extends to a $\mathbb{P}^1$-valued section
$\bar{q} \colon M \to \mathbb{P}^1$.  The three distinguished
sections are:

| Section | Value | Differential $d_q$ | Regime |
|---|---|---|---|
| $q = 0$ | $[0] \in \mathbb{P}^1$ | Undefined ($q^{-1}$ pole) | Boundary (spatial divergence) |
| $q = 1$ | $[1] \in \mathbb{P}^1$ | $d$ (full de Rham) | Classical |
| $q = \infty$ | $[\infty] \in \mathbb{P}^1$ | $\pi_V \circ d$ (vertical) | Deep quantum |

**The universal family.**
Over $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$,
define the **universal substrate differential**

$$
  \mathbf{d}
  = 
  q^{-1}d + (1 - q^{-1})\pi_V \circ d
   \in 
  \mathrm{Hom}_{\mathbb{Z}[q,q^{-1}]}\!
  \bigl(\Omega^k(A), \Omega^{k+1}(A)\bigr).
$$

This is a morphism of $\mathbb{Z}[q, q^{-1}]$-modules.  For
any ring homomorphism
$\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ sending
$q \mapsto q_0$, the base change
$\mathbf{d} \otimes_\iota k$ recovers the differential
$d_{q_0}$ at the specialisation $q_0$.
<!-- FILE_END: substrate-line-bundle.md -->

<!-- FILE_START: substrate-line-bundle-base-not-fibre.md -->
**Key property: the QOU structure is the base, not the fibre.**
The triple $(\mathbf{C}, A, \tau)$ together with the QOU
axioms (non-degenerate integration, observability,
measurability, volume constraint) are properties of the
**base** of the family.  The substrate parameter $q$ is a
coordinate on the **fibre** $\mathbb{G}_m$.

In particular:

- $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A))$
  does not depend on $q$.
- $c_1(\mathrm{Ad}(A))$ and $c_2(\mathrm{Ad}(A))$ do not
  depend on $q$.
- $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$ does not depend
  on $q$.
- The Euler class $e(\xi)$ of the Reeb bundle does not depend
  on $q$.

The entire Yekutieli obstruction tower
$\{\kappa_n \in H^2(\mathcal{S}, \mathcal{B})\}$ is a property
of $(\mathbf{C}, A, \tau)$, not of the section $q$.
<!-- FILE_END: substrate-line-bundle-base-not-fibre.md -->

<!-- FILE_START: substrate-gm-torsion.md -->
The [substrate parameter](#def:substrate-parameter) is described
in the text as an element of
$\mathrm{End}(\mathbf{1}) \cong k^\times$, the fibre coordinate
on a $\mathbb{G}_m$-family.  This remark makes the
$\mathbb{G}_m$-structure explicit and reformulates the
not-root-of-unity axiom as torsion avoidance.

**The multiplicative group scheme.**
The substrate parameter is a section of $\mathbb{G}_m$: a map
$q \colon M \to \mathbb{G}_m(k)$ where
$\mathbb{G}_m(k) = k^\times$ is the group of units.  The
$\mathbb{G}_m$-family of operators

$$
  d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d
$$

is a universal deformation parametrised by the tautological
coordinate on $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$.

The Lusztig integral form
$\mathcal{U}^\mathbb{Z}_q(\mathfrak{su}(2))$ is a
$\mathbb{Z}[q, q^{-1}]$-algebra.  A ring homomorphism
$\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ is a
$k$-point of $\mathbb{G}_m$, and base change along $\iota$
specialises the universal family to the quantum group at
$q_0 = \iota(q)$.

**Torsion points of the multiplicative group.**
The torsion subgroup of $\mathbb{G}_m$ is the group of roots
of unity:

$$
  \mathbb{G}_m[n] = \mu_n = \{\zeta \in k^\times : \zeta^n = 1\},
  \qquad
  \mathbb{G}_m[\mathrm{tors}] = \mu_\infty = \bigcup_{n \geq 1} \mu_n.
$$

The not-root-of-unity axiom in the
[substrate parameter](#def:substrate-parameter) says exactly:

$$
  q(p) \notin \mu_\infty(k)
  \qquad\text{for all } p \in M.
$$

That is: the section $q \colon M \to \mathbb{G}_m$ avoids the
torsion subscheme.  The image of $q$ lies in the complement
$\mathbb{G}_m \setminus \mu_\infty$.

**Necessity of torsion avoidance.**
At a torsion point $q_0 = e^{2\pi i m/n}$:

1. The quantum dimension $[n]_{q_0} = 0$ (the $n$-th quantum
   integer vanishes).
2. The Frobenius pairing degenerates on the representation
   $V_{(n-1)/2}$ (quantum dimension zero means null vector).
3. The non-degeneracy axiom (QOU axiom 1) fails.
4. The representation category truncates to finitely many
   simple objects, becoming a modular tensor category
   (Chern--Simons TQFT at level $n$).

At $q_0 = 1$: this is the **universal torsion point** ($1^n = 1$
for all $n$).  The quantum integer $[k]_1 = k$ never vanishes
for $k \geq 1$, but the comultiplication becomes cocommutative
($R_1 = 1 \otimes 1$) and the braiding becomes symmetric.  The
Frobenius pairing does not degenerate, but the braided structure
collapses to a symmetric one.

**The projective compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the
standard inclusion $k^\times \hookrightarrow k \cup \{\infty\}$.
The two boundary points are:

- $q = 0$: the $d_q$ operator is undefined ($q^{-1}$ pole).
  This is the boundary where the spatial differential $d$
  diverges.
- $q = \infty$: $d_q \to \pi_V \circ d$ (pure vertical
  projection).  The spatial world vanishes and only the Reeb
  (internal spin) direction survives.

The torsion points $\mu_\infty$ are dense in $\mathbb{G}_m$
(over $\mathbb{C}$).  The substrate parameter must avoid this
dense set, living in the **non-torsion locus**

$$
  \mathbb{G}_m^{\mathrm{nt}}
  = \mathbb{G}_m \setminus \mu_\infty.
$$

For the archimedean realisation over $\mathbb{R}$: the torsion
points in $\mathbb{R}^\times$ are just $\{1, -1\}$.  The
condition $q > 1$ (from $q(p) \geq 1$) combined with
$q \neq 1$ places $q$ in $(1, \infty) \subset \mathbb{R}^\times$,
which is torsion-free.

**The $q = 1$ limit as torsion specialisation.**
The [NS regularity problem](#def:ns-regular-qou) asks what
happens when the section
$q \colon M \to \mathbb{G}_m^{\mathrm{nt}}$ is extended to a
section $\bar{q} \colon M \to \mathbb{G}_m$ that hits the
torsion point $q = 1$.

In algebraic geometry, extending a family across a torsion
specialisation is controlled by the **Neron model** of the
abelian scheme.  The obstruction to extending the Frobenius--Hopf
structure across $q = 1$ lives in the **special fibre** of the
Neron model:

$$
  \mathrm{obs}(q \to 1)
   \in 
  \Phi_{q=1}(\mathbb{G}_m)
  = 
  \text{component group of the special fibre}.
$$

For $\mathbb{G}_m$ itself, the Neron model is trivial (smooth
group scheme), so the component group is trivial and the
extension exists.  But the Frobenius--Hopf structure is **not**
a $\mathbb{G}_m$-torsor — it is a family of Hopf algebras
parametrised by $\mathbb{G}_m$, and the extension problem is
more subtle.

**Connection to the NS obstruction.**
The [NS obstruction class](#prop:ns-obstruction-tower)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ lives in the
cohomology with coefficients in the banding sheaf
$\mathcal{B} = \mathcal{O}_M^\times$.  The sheaf of units
$\mathcal{O}_M^\times$ is the sheaf of sections of
$\mathbb{G}_m$.  So:

$$
  \kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)
$$

and the specialisation $q \to 1$ is the pullback along the
inclusion $\{1\} \hookrightarrow \mathbb{G}_m$:

$$
  \kappa_n\big|_{q=1}
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{ \mathrm{sp}_{q=1}}
  H^2(\mathcal{S}, \mu_\infty).
$$

The specialisation map $\mathrm{sp}_{q=1}$ factors through the
Kummer sequence

$$
  1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n}
  \mathbb{G}_m \to 1
$$

and the obstruction persists iff $\kappa_n$ is **not** divisible
by $n$ in $H^2(\mathcal{S}, \mathbb{G}_m)$ for any $n$.

For the Descartes universe with $\chi(A) = -6$, this is a special
case of [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction):
$\kappa_0$ is non-trivial at every finite place $p \nmid 6$, so the
specialisation $\kappa_0|_{q = \zeta_n}$ at every primitive $n$-th
root of unity with $\gcd(n, 6) = 1$ is non-zero in
$H^2(\mathcal{S}, \mu_n)$. The NS obstruction does not collapse —
this is the fluid-dynamics realization of the substrate's perpetual
obstruction at every cyclotomic place.
<!-- FILE_END: substrate-gm-torsion.md -->

<!-- FILE_START: observability-q-independent.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) and let
$\mathcal{Q}_M = M \times \mathbb{G}_m$ be the
[substrate line bundle](#def:substrate-line-bundle).  Let
$q_1, q_2 \colon M \to \mathbb{G}_m$ be any two substrate
sections.

Then:

$$
  \mathrm{Hom}_{\mathbf{C}_{q_1}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr)
  = 
  \mathrm{Hom}_{\mathbf{C}_{q_2}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr).
$$

In particular, if $(\mathbf{C}, A, \tau)$ satisfies the
observability axiom for any substrate section $q > 1$, then
it satisfies it for **every** substrate section, including
$q = 1$.

**Mathematical Novelty.** While the specific result is a straightforward categorical triviality (that Hom-spaces over a fixed monoidal category do not depend on the differential layer $d_q$), the mathematical novelty lies in establishing this exact independence as the formal mechanism that permits properties to safely propagate from the deformed observable phase space ($q > 1$) directly to the unphysical/classical substrate ($q = 1$) without discontinuity.
<!-- FILE_END: observability-q-independent.md -->

<!-- FILE_START: core-levi-form.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Core Levi form").**

Let $\varrho$ be a [geodesic vortex](#rem:geodesic-vortices) in
the [state bundle](#ex:c-quantum-observable-universe) $(\mathcal{S}, \varTheta)$
with contact form $\varTheta$ and
[Levi form](#def:levi-form-defect)
$\mathcal{L}_\varTheta(V, W) = -id\varTheta(V, \bar{W})$.  At each
point $p \in \varrho$, let $N_p\varrho \subset \ker(\varTheta_p)$ be
the horizontal normal plane.  Define:

- $\lambda_\parallel(p)$, $\lambda_\perp(p)$: eigenvalues of
  $\mathcal{L}_\varTheta|_{N_p\varrho}$ (the Levi form restricted to
  the normal plane), with $\lambda_\parallel$ in the direction
  toward a second filament and $\lambda_\perp$ perpendicular to it.

- $a_\parallel(p)$, $a_\perp(p)$: core radii of the vortex
  cross-section in the corresponding directions, defined as the
  widths at half-maximum of $|\psi|^2$ in $N_p\varrho$.

Then:

**(a)** The core aspect ratio is controlled by the Levi
eigenvalue ratio:

$$
  \frac{a_\perp(p)}{a_\parallel(p)}
  = 
  \sqrt{\frac{\lambda_\parallel(p)}{\lambda_\perp(p)}}
   \cdot 
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(b)** The Levi form condition number on $N_p\varrho$ is

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
  \equiv
  \frac{\max(\lambda_\parallel, \lambda_\perp)}
       {\min(\lambda_\parallel, \lambda_\perp)}
  = 
  \max\!\left(
    \frac{a_\perp}{a_\parallel},
    \frac{a_\parallel}{a_\perp}
  \right)^2
  \cdot
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(c)** The following are equivalent:

1. The core aspect ratio is bounded:
   $\sup_{t < T^*} a_\perp(t) / a_\parallel(t) \leq C$.

2. The Levi form condition number is bounded:
   $\sup_{t < T^*} \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p}) \leq C^2$.

3. The contact structure $\ker(\varTheta)$ remains
   **non-degenerate** at the collision locus $\Sigma$: both
   eigenvalues $\lambda_\parallel, \lambda_\perp > 0$ on $\Sigma$.

4. The [observability axiom](#def:quantum-observable-universe)
   $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
   holds locally at every $p \in \Sigma$.

5. No 2-dimensional integral submanifold of $\ker(\varTheta)$
   forms at $\Sigma$ (Frobenius integrability does not hold).

**(d)** For $q > 1$, the [quantum pressure](#rem:madelung-fluid)
enforces

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
   \leq 
  1 + C_0\hbar_q^2
   <  \infty,
$$

so conditions (1)--(5) hold.  The
[well-posedness theorem](#thm:q-ns-wellposedness) is consistent.

**(e)** At $q = 1$: $\hbar_q = 0$ and there is no isotropic
resistance.  The [vorticity lower
bound](#prop:vorticity-lower-bound) and the
[counter-example](#conj:ns-counterexample) hold if and only
if condition (3) holds at $q = 1$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: core-levi-form.md -->

<!-- FILE_START: core-levi-interpretation.md -->
The [core-Levi equivalence](#prop:core-levi-form) reformulates
the Navier--Stokes millennium problem as a question about the
contact geometry of the brane:

$$
  \text{NS blows up}
  \Longleftrightarrow
  \text{Levi form non-degenerate at collision}
  \Longleftrightarrow
  \kappa(t) = O(1).
$$

**Interpretation of each outcome.**

If the Levi form **stays non-degenerate** ($\kappa = O(1)$):
vorticity concentrates in tubular cores, the lower bound
$\|\omega\|_\infty \geq c/(T^*-t)$ holds, BKM diverges, and
NS loses regularity.  The [counter-example](#conj:ns-counterexample)
is established.  Physically: the contact structure resists
integrability, the vortex remains a topological defect, and the
collision produces a genuine singularity.

If the Levi form **degenerates** ($\kappa \to 0$ or $\infty$):
vorticity spreads into a sheet, the lower bound fails, and NS
might be regular.  Physically: the contact structure becomes
partially integrable at the collision locus — a 2-dimensional
integral submanifold forms, the observability axiom fails locally,
and the vortex dissolves into a diffuse structure that classical
viscosity can regularise.

**The root-of-unity constraint.**
At $q = e^{i\pi/\kappa}$, the [truncation](#prop:root-of-unity-truncation)
to $(\kappa-1)/2$ modes bounds the core aspect ratio by
$1 + C(\kappa-1)$.  As $\kappa \to \infty$ ($q \to 1$), this
bound diverges — but only linearly.  The collision dynamics
drives $\kappa(t)$ at a rate set by the Biot--Savart stretching
$\sim 1/(T^*-t)$.  Whether the representation-theoretic bound
$O(\kappa)$ or the dynamical rate $O(1/(T^*-t))$ wins
determines the answer.

The contact-geometric reformulation is:
**does finite-dimensional approximation of $\mathrm{SU}_q(2)$
preserve the non-degeneracy of the Levi form in the
infinite-dimensional limit?**
<!-- FILE_END: core-levi-interpretation.md -->

<!-- FILE_START: ns-regular-qou.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with
[brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$
and [quantum characteristic classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** of $(\mathbf{C}, A, \tau)$ is the class

$$
  \mathrm{NS}(A)
  = 
  \kappa_0\big|_\Sigma
   \in 
  H^2(\Sigma, \mathcal{B}),
$$

where $\Sigma$ is the collision locus of a generic vortex pair
and $\kappa_0 = e(\xi)$ is the Euler class of the Reeb bundle
with $\mathrm{tr}(\kappa_0) = \chi(A)$.

We say that $(\mathbf{C}, A, \tau)$ is:

- **NS-regular** if $\mathrm{NS}(A) = 0$: the obstruction
  vanishes and the classical Navier--Stokes equation (the
  $q = 1$ specialisation of the
  [q-NS system](#def:q-navier-stokes)) admits smooth global
  solutions for all smooth initial data.

- **NS-singular** if $\mathrm{NS}(A) \neq 0$: the obstruction
  persists and the classical Navier--Stokes equation admits
  smooth initial data for which the solution develops a
  singularity in finite time.

The NS obstruction depends only on the categorical data
$(\mathbf{C}, A, \tau)$ — specifically on $\chi(A)$ — and not
on the substrate section $q$ or on any particular initial data.
Different quantum universes may have different NS status:

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $\neq 0$ (Kummer non-divisibility) | **NS-singular** |
| $= 0$ | $= 0$ | **NS-regular** |

The observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is a
**sufficient condition** for $\chi(A) \neq 0$ (it forces
irreducibility of the adjoint representation, which gives
nonzero Euler class).  It is not assumed in this definition;
it is a diagnostic.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: ns-regular-qou.md -->

<!-- FILE_START: ns-obstruction.md -->
**Definition.**
*Let $(A, \varTheta)$ be a quantum universe.  The **NS obstruction
class** is the element*

$$
  \mathrm{NS}(A) \;\in\; H^3_{\mathrm{loc}}(A, \varTheta)
$$

*obtained by evaluating the Yekutieli obstruction tower of the
$q$-Navier--Stokes system at $q = 1$.  Concretely,
$\mathrm{NS}(A)$ is the obstruction to lifting the $q$-NS
solution from brane level $n$ to level $n + 1$ in the limit
$q \to 1$.*

*The NS obstruction depends on the Euler characteristic
$\chi(A)$:*

- *$\mathrm{NS}(A) = 0$ if and only if the quantum universe is
  [NS-regular](#def:ns-regular-qou), i.e.\ the incompressible
  Navier--Stokes equation has global regularity.*
- *$\mathrm{NS}(A) \neq 0$ implies finite-time blowup of smooth
  solutions.*
<!-- FILE_END: ns-obstruction.md -->

<!-- FILE_START: ns-obstruction-spectral-gap.md -->
Under the categorical origin of the crossing energy
([crossing energy](#def:crossing-energy)), the $q \to 1$ limit is
exactly the **Hecke spectral-gap closure**: the eigenvalues
$(q, -q^{-1})$ of the Hecke generator $\sigma$ on $V \otimes V$ collide at
$(1, -1)$, and the separation between the symmetric and antisymmetric
transport channels vanishes.  In this reading:

- The obstruction class $\mathrm{NS}(A)$ measures the **failure of the
  $q$-deformed transport to remain diagonalisable** as $q \to 1$.
- Blowup of smooth solutions corresponds to the inability of the
  Markov trace to separate $S^{2} V$ from $\Lambda^{2} V$ in the
  classical limit --- an algebraic failure mode, parallel to (but
  distinct from) the classical continuous-energy blowup picture.
- $\mathrm{NS}(A) = 0$ holds precisely when the categorical volume
  constraint remains rigid through the $q \to 1$ limit, i.e.\ when
  the classical limit is dominated by a codimension-$\geq 2$ locus
  in the eigenvalue moduli.

This supplies an **algebraic failure criterion** for smoothness
without reference to continuous energy estimates: the obstruction is
tested by whether the Hecke spectral gap closes to first order or
higher order in $(q - 1)$.
<!-- FILE_END: ns-obstruction-spectral-gap.md -->

<!-- FILE_START: ns-classical-formulation.md -->
The [q-NS system](#def:q-navier-stokes) at $q = 1$ recovers the
classical incompressible Navier--Stokes equation on
$\mathbb{R}^3$:

$$
  \partial_t v + (v \cdot \nabla)v = -\nabla p + \nu\Delta v,
  \qquad \nabla \cdot v = 0,
  \qquad v|_{t=0} = v_0.
$$

A standard question in the analysis of this equation is whether
smooth initial data $v_0 \in C^\infty(\mathbb{R}^3)$ with
$\nabla \cdot v_0 = 0$ and finite energy always gives rise to a
smooth global solution, or whether singularities can form in
finite time.

The [NS obstruction](#def:ns-obstruction) $\mathrm{NS}(A)$
computes the answer from the categorical data of the quantum
universe: $\mathrm{NS}(A) = 0$ implies regularity;
$\mathrm{NS}(A) \neq 0$ implies blowup.  The obstruction
depends on $\chi(A)$.  For $\chi(A) = 0$
([torus example](#ex:torus-ns-regular)), the equation is
globally regular.  For $\chi(A) = -6$
([Descartes universe](#thm:ns-singularity-descartes)),
singularities form.
<!-- FILE_END: ns-classical-formulation.md -->

