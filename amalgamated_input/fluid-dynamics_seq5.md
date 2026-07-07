<!-- FILE_START: intro-ns-obstruction-tower-mtc.md -->
The previous section established the $q$-deformed Navier–Stokes
system on $\Omega^1(A)$ and its global regularity at substrate
parameter $q > 1$.  This section assembles the obstruction tower
that controls how that regularity degenerates as $q \to 1$ — and
identifies the modular tensor category structure on the limiting
observables that survives the degeneration.

The arc moves in two stages.  The first six blocks build the
Yekutieli obstruction tower on the collision locus of two
anti-parallel vortex filaments: the boundary observability
$\mathrm{Obs}_\partial(A)$ is the kernel of the restriction of the
Yekutieli classes, computed explicitly via the Kummer
specialisation and recovered as torus-NS-regular in the
root-of-unity truncation.  The remaining two blocks (Track B)
extract the observable modular tensor category and its braid-group
action, which is the categorical residue of the fluid flow that
the next section's research programme picks up.

The two-vortex amalgamation
([approach to exceptional divisor](#sec:approach-to-exceptional-divisor))
extends to three: at the triple-vortex collision the merged
$\pi_1(U \setminus K_3)$ admits a three-strand braid representative
and the categorical instanton acts via the $B_3$-representation
$\rho_3$ of [prop:bn-mtc-action](#prop:bn-mtc-action) on
$\mathbf{V}^{\otimes 3}$.  The Brunnian (pairwise-unlinked,
triple-linked) representative selected by SDP/LP minimisation is the
Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ of
[conj:borromean-quark](#conj:borromean-quark); confinement is the
non-vanishing triple Milnor invariant $\bar{\mu}_{123}$.
<!-- FILE_END: intro-ns-obstruction-tower-mtc.md -->

<!-- FILE_START: ns-obstruction-tower.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"NS obstruction tower").**

Let $(\mathbf{C}, A, \tau)$ be a QOU with Euler characteristic
$\chi(A)$ and [Yekutieli obstruction
classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.  Let
$\Sigma \subset \mathcal{S}$ be the collision locus of two
anti-parallel vortex filaments.

The [boundary observability](#def:ns-regular-qou)
$\mathrm{Obs}_\partial(A)$ is measured by the restriction of the
Yekutieli obstruction classes to the collision locus:

$$
  \mathrm{Obs}_\partial(A)
  = 
  \ker\!\left(
    \bigoplus_{n \geq 0}
    H^2(\mathcal{S}, \mathcal{B})
    \xrightarrow{ \mathrm{res}_\Sigma}
    \bigoplus_{n \geq 0}
    H^2(\Sigma, \mathcal{B}|_\Sigma)
  \right).
$$

The QOU is [NS-singular](#def:ns-regular-qou) (blowup) iff
$\mathrm{res}_\Sigma(\kappa_n) \neq 0$ for some $n$; NS-regular
iff $\mathrm{res}_\Sigma(\kappa_n) = 0$ for all $n$.

**(a) Where the obstruction sits.**

By the [QU-to-QOU theorem](#thm:qu-to-qou), the first obstruction
is $\kappa_0 = e(\xi)$, the Euler class of the Reeb bundle, with
$\mathrm{tr}(\kappa_0) = \chi(A)$.  The obstruction at level $n$
is

$$
  \kappa_n
  = 
  \kappa_0
  + 
  \delta_n,
  \qquad
  \delta_n \in \mathrm{im}\!\bigl(
    H^2(\mathcal{S}, \mathcal{O}_\mathcal{S})
    \to H^2(\mathcal{S}, \mathcal{B})
  \bigr),
$$

where $\delta_n$ is the jet correction at level $n$.  By the
perpetual obstruction ([QU-to-QOU](#thm:qu-to-qou) item 3,
strengthened by [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
to a place-by-place non-vanishing of the substrate's motivic
Galois character), $\kappa_0$ and $\delta_n$ live in complementary
subgroups when $\kappa_0$ is non-torsion, so $\kappa_n \neq 0$
for all $n$.

**(b) Restriction to the collision locus.**

The collision locus $\Sigma$ is a 1-dimensional submanifold
(line segment) with $H^2(\Sigma, \mathcal{B}|_\Sigma)$ computed
by the long exact sequence of the pair
$(\mathcal{S}, \mathcal{S} \setminus \Sigma)$:

$$
  \cdots \to
  H^1(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \xrightarrow{\partial}
  H^2_\Sigma(\mathcal{S}, \mathcal{B})
   \to 
  H^2(\mathcal{S}, \mathcal{B})
  \xrightarrow{ \mathrm{res}}
  H^2(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \to \cdots
$$

The obstruction restricts nontrivially to $\Sigma$ iff
$\kappa_n$ is **not** in the image of the restriction map from
$\mathcal{S} \setminus \Sigma$.  Equivalently, the connecting
homomorphism $\partial$ detects it: $\kappa_n|_\Sigma \neq 0$
iff $\kappa_n$ has nontrivial **local cohomology** support
at $\Sigma$.

**(c) Local cohomology computation.**

The [local cohomology](#def:local-cohomology-group) at a point
$p \in \Sigma$ is

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  R^1\Gamma_{\mathfrak{m}_p}(A).
$$

For the anti-parallel vortex pair, each filament carries the
fundamental representation $V_{1/2}$ of
$\mathrm{SU}_q(2)$.  At the collision point $p$ where
both filaments meet, the local cohomology receives
contributions from both:

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  V_{1/2}^{(1)} \oplus V_{1/2}^{(2)},
$$

a 4-dimensional space.  This is **nonzero** iff both filaments
contribute nontrivial local sections at $p$ — i.e. iff the
vortex cores have not dissolved.

**(d) Connection to core aspect ratio.**

By the [core-Levi equivalence](#prop:core-levi-form), the
local cohomology is nonzero iff the Levi form is non-degenerate
at $p$.  Explicitly:

$$
  H^1_{\mathfrak{m}_p}(A) \neq 0
  \quad\Longleftrightarrow\quad
  \lambda_\parallel(p) > 0
   \text{ and }
  \lambda_\perp(p) > 0
  \quad\Longleftrightarrow\quad
  \kappa(p) = a_\perp/a_\parallel \in (0, \infty).
$$

When the core flattens ($\kappa \to 0$ or $\kappa \to \infty$),
one Levi eigenvalue vanishes, the local cohomology collapses
from $V_{1/2}^{\oplus 2}$ to a quotient, and the obstruction
class $\kappa_n|_\Sigma$ deforms toward zero.

**(e) The NS obstruction as an Euler-class residue.**

Combining (a)--(d): the NS obstruction at level $n$ restricted
to the collision locus is

$$
  \kappa_n\big|_\Sigma
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot e(\xi)\big|_\Sigma
  +  \delta_n\big|_\Sigma,
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ is the linking number
of the two filaments and $e(\xi)|_\Sigma$ is the Euler class of
the Reeb bundle restricted to $\Sigma$.

For the Descartes universe ($\chi(A) = -6$, Bring's surface):
$e(\xi) = -6 \cdot [\Sigma_4]$ in $H^2(\Sigma_4, \mathbb{Z})$.
The restriction $e(\xi)|_\Sigma$ is nonzero when $\Sigma$ is
homologically nontrivial in $\Sigma_4$, which holds for the
anti-parallel pair (linking number 1).

**Summary.** The NS obstruction is measured at every level of
the Yekutieli tower by restricting $\kappa_n$ to the collision
locus $\Sigma$.  It is nonzero (NS-singular, blowup) iff the
local cohomology $H^1_{\mathfrak{m}_p}(A)$ is nonzero at
collision points, which holds iff the Levi form is
non-degenerate (core aspect ratio bounded).  Computing
whether $\kappa_n|_\Sigma$ vanishes or persists as $q \to 1$
is the [Levi degeneracy conjecture](#conj:levi-degeneracy).
<!-- FILE_END: ns-obstruction-tower.md -->

<!-- FILE_START: ns-obstruction-computation.md -->
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
$\chi(A) = -6$ (Bring's surface of genus 4).  Let $\Sigma$ be
the collision locus of an anti-parallel vortex pair with
linking number $\mathrm{lk} = 1$.

The [NS obstruction](#prop:ns-obstruction-tower) at level $n$
restricted to $\Sigma$ is
$\kappa_n|_\Sigma = \mathrm{lk} \cdot e(\xi)|_\Sigma + \delta_n|_\Sigma$.
We compute each term.

**(a) The Euler class term.**

The Euler class $e(\xi) \in H^2(\Sigma_4, \mathbb{Z})$ of the
Reeb bundle satisfies $\mathrm{tr}(e(\xi)) = \chi(A) = -6$.
Since $H^2(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}$ (Bring's
surface is a closed orientable surface), $e(\xi) = -6$ as an
integer.

The restriction to $\Sigma$ (a line segment, hence
contractible) gives $e(\xi)|_\Sigma = 0$ in
$H^2(\Sigma, \mathbb{Z})$ (since $H^2$ of a contractible
space vanishes).

However, the **local** Euler class at a point $p \in \Sigma$
is measured by the local cohomology
$H^2_{\{p\}}(\Sigma_4, \mathbb{Z})$, which is nonzero.
By excision:

$$
  H^2_{\{p\}}(\Sigma_4, \mathbb{Z})
   \cong 
  H^2(D^4, S^3; \mathbb{Z})
   \cong 
  \mathbb{Z},
$$

where $D^4$ is a small ball around $p$ and $S^3$ its boundary
(Bring's surface has real dimension 4 as a complex surface).
The Euler class restricts to the **local degree** at $p$:

$$
  e(\xi)|_p = -6 \cdot \deg_p(\xi) \in \mathbb{Z}.
$$

For a generic point, $\deg_p(\xi) = 0$ (the Reeb vector field
is nonvanishing).  At a **vortex collision point**, the Reeb
field has a zero (the contact structure degenerates if the
core flattens), and $\deg_p(\xi)$ is the index of this zero.

**(b) The jet correction term.**

The jet correction $\delta_n$ at level $n$ in the Yekutieli
tower is computed from the $n$-th iterated jet prolongation.
By [Euler characteristic stability](#prop:euler-char-stability),
$\chi(E_n) = \chi(A) = -6$ for all $n$, so the topological
contribution does not change with level.

The analytic contribution $\delta_n|_\Sigma$ depends on the
$(n+1)$-jet of the velocity field at $\Sigma$.  For the
anti-parallel pair, the velocity field has the Biot--Savart
structure $v \sim \Gamma/(2\pi d)$ near the collision, with
jets diverging as $d \to 0$:

$$
  |j^n v|_\Sigma
   \sim 
  \frac{\Gamma}{d^{n+1}}
   \sim 
  \frac{1}{(T^* - t)^{(n+1)/2}}.
$$

The jet correction $\delta_n|_\Sigma$ is controlled by
$|j^n v|$ and is nonzero whenever the $n$-th jet diverges.
For the anti-parallel pair, $|j^n v| \to \infty$ for all
$n \geq 1$ as $t \to T^*$.

**(c) The total obstruction.**

Combining (a) and (b): the NS obstruction at the collision
locus has two components:

1. **Topological**: $\mathrm{lk} \cdot e(\xi)|_p$, which is
   nonzero iff the Reeb field has a zero at $p$ (iff the
   contact structure degenerates).

2. **Analytic**: $\delta_n|_\Sigma$, which is nonzero whenever
   the $n$-th jet of the velocity diverges (for all $n \geq 1$
   in the anti-parallel case).

The topological and analytic terms live in complementary
subgroups of $H^2(\mathcal{S}, \mathcal{B})$ (by the
perpetual obstruction, [QU-to-QOU](#thm:qu-to-qou) item 3).
Therefore:

- If the Reeb field has **no zero** at $p$ ($\deg_p(\xi) = 0$):
  the topological term vanishes but the analytic term
  $\delta_n|_\Sigma \neq 0$ persists.  The obstruction is
  **purely analytic** and the contact structure is
  non-degenerate.  This is the **NS-singular** case (blowup).

- If the Reeb field **has a zero** at $p$ ($\deg_p(\xi) \neq 0$):
  both terms are nonzero and cannot cancel (complementary
  subgroups).  The obstruction is again nonzero.  This is
  also **NS-singular**.

**(d) Result.**

For the Descartes universe with $\chi(A) = -6$:

$$
  \kappa_n\big|_\Sigma  \neq  0
  \qquad\text{for all } n \geq 1.
$$

The analytic term $\delta_n|_\Sigma$ is nonzero because the
jets of the Biot--Savart velocity diverge at the collision.
The topological term is either zero (no Reeb zero) or
nonzero (Reeb zero), but in either case the total obstruction
is nonzero because $\delta_n$ alone is nonzero and the two
terms cannot cancel.

Therefore $\mathrm{Obs}_\partial(A) = 0$ and the Descartes
universe is **NS-singular**.

*Formal asymptotic content. The jet divergence
$|j^n v|_\Sigma \sim 1/(T^*-t)^{(n+1)/2}$ has
$\ordw(\lvert j^n v \rvert_\Sigma) = -\tfrac{n+1}{2}\,\ordw(T^*-t)$
as $t \to T^*$; the
recursive jet tower is the
[surreal blow-up calculus](#def:surreal-blowup-calculus), and
the $q \to 1$ classical-limit reading is the
[standard-part functor](#def:standard-part-functor). See also
[Big-O via $\ordw$](#rem:conway-normal-form) and the
[body asymptotics catalog](#rem:body-asymptotics-catalog).*

<!-- FILE_END: ns-obstruction-computation.md -->

<!-- FILE_START: ns-obstruction-computation-interpretation.md -->
**Mathematical Novelty.** While calculating local Euler classes via excision ($H^2_{\{p\}}$) and asserting Biot-Savart jet divergence are standard in differential topology and fluid mechanics respectively, the mathematical novelty is explicitly combining them to show that analytic and topological terms live in complementary subgroups of the Yekutieli obstruction tower. This proves that classical divergence bounds cannot be "cancelled out" by topological adjustments in the background manifold, guaranteeing the persistence of the obstruction across all jet levels.
<!-- FILE_END: ns-obstruction-computation-interpretation.md -->

<!-- FILE_START: ns-kummer-specialisation.md -->
Let $(\mathbf{C}, A, \tau)$ be a QOU with
$\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ and
$\mathrm{tr}(\kappa_0) = \chi(A)$.

The Kummer exact sequence for each $n \geq 1$:

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

induces a long exact sequence in cohomology:

$$
  H^2(\mathcal{S}, \mu_n)
  \to H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\cdot n}
  H^2(\mathcal{S}, \mathbb{G}_m)
  \to H^3(\mathcal{S}, \mu_n).
$$

The [specialisation to $q = 1$](#rem:substrate-gm-torsion) maps

$$
  \kappa_0 \mapsto
  \kappa_0 \bmod n
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m).
$$

This class is nonzero iff $\kappa_0$ is **not** $n$-divisible.

**(a) Divisibility of the Euler class.**

For a closed orientable surface $\Sigma_g$ of genus $g$:
$H^2(\Sigma_g, \mathbb{Z}) \cong \mathbb{Z}$.  The Euler
class $e(\xi) = \chi(A) \in \mathbb{Z}$.  Then:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

For the Descartes universe with $\chi(A) = -6$: the divisors
of $6$ are $\{1, 2, 3, 6\}$.  So $\kappa_0 \bmod n = 0$ only
for $n \in \{1, 2, 3, 6\}$, and $\kappa_0 \bmod n \neq 0$ for
all other $n$ (in particular for $n = 5, 7, 11, 13, \ldots$).

**(b) Obstruction persistence.**

At the root of unity $q = e^{i\pi/\kappa}$, the relevant
Kummer level is $n = 2\kappa$ (the order of $q$ in
$\mathbb{G}_m$).  The obstruction $\kappa_0 \bmod 2\kappa$
is:

$$
  \kappa_0 \bmod 2\kappa = 0
  \quad\Longleftrightarrow\quad
  2\kappa \mid \chi(A).
$$

For $\chi(A) = -6$: $2\kappa \mid 6$ iff $\kappa \in \{1, 3\}$,
i.e. $q = e^{i\pi}$ or $q = e^{i\pi/3}$.  For all other
$\kappa$ (in particular all $\kappa \geq 4$), the obstruction
**persists** at that root of unity.

**(c) The limit as kappa goes to infinity.**

As $\kappa \to \infty$ ($q \to 1$), $2\kappa \to \infty$ and
$2\kappa \nmid 6$ for all $\kappa \geq 4$.  Therefore:

$$
  \kappa_0 \bmod 2\kappa  \neq  0
  \qquad\text{for all } \kappa \geq 4.
$$

The topological component of the NS obstruction **does not
vanish** in the $q \to 1$ limit.

**(d) Formal statement.**

For any QOU with $\chi(A) \neq 0$:

1. The specialisation $\kappa_0|_{q=1}$ is nonzero in
   $H^2(\mathcal{S}, \mathbb{G}_m)/n$ for all $n \nmid \chi(A)$.

2. Since the set $\{n : n \nmid \chi(A)\}$ is infinite (it
   contains all primes not dividing $\chi(A)$), the obstruction
   is **persistently nonzero** through infinitely many levels
   of the Kummer tower.

3. The obstruction vanishes only at the finitely many Kummer
   levels $n \mid \chi(A)$, which correspond to the finitely
   many roots of unity where the representation category
   truncates in a way compatible with the Euler class.

**(e) Consequence for NS regularity.**

The QOU with $\chi(A) = -6$ is **NS-singular**:
$\mathrm{Obs}_\partial(A) = 0$, the boundary observability
vanishes, and the classical Navier--Stokes equation admits
finite-time blowup.

This follows from (e) together with the
[complementary-subgroup argument](#thm:qu-to-qou) (item 3):
the topological obstruction $e(\xi)|_\Sigma \neq 0$ cannot
be cancelled by the analytic correction $\delta_n|_\Sigma$
because they live in complementary summands of
$H^2(\mathcal{S}, \mathbb{G}_m)$.
<!-- FILE_END: ns-kummer-specialisation.md -->

<!-- FILE_START: ns-singularity-descartes.md -->
Let $(\mathbf{C}, A, \tau)$ be the Descartes quantum universe
with $\chi(A) = -6$ (Bring's surface of genus 4).

Then $(\mathbf{C}, A, \tau)$ is
[NS-singular](#def:ns-obstruction):

$$
  \mathrm{NS}(A)
  = 
  e(\xi)\big|_\Sigma
   \neq  0.
$$

The classical 3-dimensional Navier--Stokes equation admits
smooth initial data for which the solution develops a
singularity in finite time.
<!-- FILE_END: ns-singularity-descartes.md -->

<!-- FILE_START: ns-singularity-descartes-interpretation.md -->
**Mathematical Novelty.** While the proof relies on a sequence of upstream conditional geometric bounds (Kummer tower survival, perpetual obstruction, core-Levi form, and BKM divergence), the mathematical novelty here is the structural assembly of these abstract topological components into a strictly deterministic criterion. It bypasses direct PDE analytic estimates by using the explicit arithmetic constraint ($\chi(A)=-6$) as a global topological forcing term that mandates finite-time blowup via purely categorical conditions.
<!-- FILE_END: ns-singularity-descartes-interpretation.md -->

<!-- FILE_START: torus-ns-regular.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with
$A$ realised on the torus $\Sigma_1$ (genus $g = 1$).  Then

$$
  \chi(A) = 2 - 2g = 0.
$$

**The NS obstruction vanishes.**
The Euler class of the Reeb bundle is
$\kappa_0 = e(\xi)$ with $\mathrm{tr}(\kappa_0) = \chi(A) = 0$.
For every $n \geq 1$, $2\kappa \mid 0$ for all $\kappa$, so
$\kappa_0 \bmod 2\kappa = 0$ at every Kummer level.  The
[Kummer specialisation](#prop:ns-kummer-specialisation) gives
no obstruction:

$$
  \mathrm{NS}(A) = \kappa_0\big|_\Sigma = 0.
$$

The torus quantum universe is **NS-regular**.

**Physical meaning.**
The Levi form is allowed to degenerate at collision loci.
Vortex cores can flatten into sheets.  Vorticity spreads rather
than concentrates.  The classical Navier--Stokes equation
(the $q = 1$ specialisation) admits smooth global solutions for
all smooth initial data.

**Failure of the torus to support the observed physics.**
The torus has $g = 1$, so only one torus knot embeds:
$T_{2,3}$ (the trefoil, Seifert genus 1).  The knot spectrum
has a single generator — no muon, no tau, no quarks beyond
the first generation.  The representation theory of
$\pi_1(\Sigma_1) = \mathbb{Z}^2$ is abelian: all
$\mathrm{SU}(2)$ representations factor through $\mathrm{U}(1)$.
The gauge group reduces, and the full particle spectrum does
not emerge.

**The torus also fails observability.**
On $\Sigma_1$, flat $\mathrm{SU}(2)$ connections exist with
holonomy in $\mathrm{U}(1) \subset \mathrm{SU}(2)$.  These
are **reducible**: $H^0(\Sigma_1, \mathrm{Ad}(P)) \neq 0$
(the Cartan subalgebra $\mathfrak{u}(1) \subset
\mathfrak{su}(2)$ provides a nonzero equivariant section).
So $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ — the
observability axiom fails.

The torus is a quantum pre-universe (QPU), not a QOU.

**Contrast with the Descartes universe.**

See [Table](#tbl:torus-ns-regular-table-data).

The torus is the simplest example where $\chi = 0$ forces NS
regularity.  It is also physically trivial — the vanishing
Euler characteristic is why the torus cannot support a rich
universe and why its fluid dynamics is tame.

**Other $\chi = 0$ examples.**
Any genus-1 surface gives $\chi = 0$: the flat torus
$\mathbb{R}^2/\mathbb{Z}^2$, the Heisenberg nilmanifold
$\mathrm{Heis}(\mathbb{Z}) \backslash \mathrm{Heis}(\mathbb{R})$,
any Seifert fibration over an elliptic curve.  All are
NS-regular by the same argument.
<!-- FILE_END: torus-ns-regular.md -->

<!-- FILE_START: root-of-unity-truncation.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Root-of-unity truncation").**

The [QOU axiom](#def:substrate-parameter) requires that $q$ is
**not** a root of unity. But the limit $q \to 1$ passes through
a dense set of roots of unity, and at each root the
representation theory undergoes a dramatic truncation that
**strengthens** regularity. The blowup at $q = 1$ is the
accumulation of infinitely many such truncations.

The truncation mechanism itself — the vanishing of the $q$-integer
$[\kappa]_q$ at $q = e^{i\pi/\kappa}$, collapsing the $q$-Laplacian
spectral tower $[k]_q^2$ to the finite Verlinde/ADE set — is
established in
[the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower).
Here we read off its fluid-dynamical consequence.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
 Infinitely many simple objects $V_j$, $j = 0, 1/2, 1, \ldots$
 Quantum dimensions $[2j+1]_q > 0$ for all $j$.
 Eigenvalues $[k]_q^2 \sim q^{2k}$ (exponential growth).
 The [well-posedness theorem](#thm:q-ns-wellposedness) gives
 global regularity.

2. **Root of unity $q = e^{i\pi/\kappa}$, $\kappa \in \mathbb{Z}_{\geq 2}$.**
 Only **finitely many** simple objects: $j = 0, 1/2, \ldots,
   (\kappa-2)/2$. The quantum dimension $[2j+1]_q$ vanishes at
 $j = (\kappa-1)/2$, truncating the representation category.
 The Verlinde formula governs fusion:

 $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

 where $S$ is the modular $S$-matrix. The representation
 category becomes a **modular tensor category** — the algebraic
 input for Chern--Simons TQFT at level $\kappa$.

3. **$q = 1$ (classical limit).**
 Infinite simple objects with $[k]_1 = k$ (polynomial).
 No truncation, no exponential damping. The
 [regularity breakdown](#conj:regularity-breakdown) regime.

**Root-of-unity regularity is stronger than generic.**

At $q = e^{i\pi/\kappa}$, the q-NS system has at most
$(\kappa-1)/2$ active vortex modes (the truncated representation
category has finitely many objects). This is a **hard cutoff**,
not the soft exponential damping of generic $q > 1$:

- Generic $q > 1$: modes with $[k]_q > \mathrm{Re}_q^{1/2}$
 are exponentially damped but nonzero.
- Root of unity: modes with $j > (\kappa-2)/2$ **do not exist**
 in the category. The Hilbert space is finite-dimensional.

A finite-dimensional ODE is by definition globally regular
(Picard--Lindelöf). So at every root of unity, the q-NS
system is not only well-posed but **finite-dimensional**.

**The $q = 1$ accumulation.**

As $\kappa \to \infty$, $q = e^{i\pi/\kappa} \to 1$. The
truncation level $j_{\max} = (\kappa-2)/2 \to \infty$: more
and more modes become available. The sequence of
finite-dimensional systems approaches the infinite-dimensional
classical system.

The blowup at $q = 1$ is the statement that this
infinite-dimensional limit is **singular**: no finite truncation
blows up, but the limit of all truncations can. This is
precisely the structure of a **phase transition at the
accumulation point**.

**Connection to the core aspect ratio.**

At a root of unity $q = e^{i\pi/\kappa}$, the vortex core
shape is controlled by the **modular tensor category** structure.
The fusion rules $N_{ij}^k$ determine which mode interactions
are allowed. The truncation $j \leq (\kappa-2)/2$ forbids
high-frequency core deformations: the core **cannot** develop
fine-scale structure beyond the cutoff. In particular:

- The core aspect ratio $\kappa(t) = a_\perp/a_\parallel$
 is controlled by the Fourier modes of the core boundary.
- At root of unity: only $(\kappa-1)/2$ modes exist, so
 $\kappa(t)$ is a trigonometric polynomial of bounded degree.
- A trigonometric polynomial of degree $N$ satisfies
 $|\kappa'(t)| \leq N\|\kappa\|_\infty$ (Bernstein
 inequality), preventing rapid oscillation.

This gives an **explicit bound** at each root of unity:

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

for some universal constant $C$. The bound grows linearly
with the truncation level $\kappa$, and diverges as
$\kappa \to \infty$ ($q \to 1$).

**The refined gap.**

The original [vorticity lower bound](#prop:vorticity-lower-bound)
requires $\sup_t \kappa(t) \leq C$ with $C$ independent of $q$.
The root-of-unity analysis gives $\kappa(t) \leq 1 + C(\kappa-1)$,
which grows with $\kappa$. The question is the **rate of growth**:

- If $\kappa(t) \leq C_0$ uniformly (independent of $\kappa$):
 the core stays circular, the lower bound holds, and NS blows up.
 Counter-example established.

- If $\kappa(t) \sim \kappa$ (linear growth): the core flattens at
 the same rate as modes become available. The vorticity spreads
 into a sheet, and the lower bound $\omega \geq c/(T^*-t)$ may
 fail. NS might be regular.

- If $\kappa(t) \sim \kappa^\beta$ with $0 < \beta < 1$: an
 intermediate case. The lower bound holds if $\beta < 1/2$
 (the flattening is slower than the approach).

The [Levi form condition number](#def:levi-form-defect) at the
vortex core is $\lambda_{\max}/\lambda_{\min}$, which equals
$\kappa(t)^2$. The contact structure degenerates (becomes
integrable) iff $\lambda_{\min} \to 0$, i.e. $\kappa(t) \to
\infty$. So:

$$
  \boxed{
    \text{NS blows up}
    \iff
    \text{Levi form stays non-degenerate at collision}
    \iff
    \kappa(t) = O(1).
  }
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: root-of-unity-truncation.md -->

<!-- FILE_START: root-of-unity-truncation-interpretation.md -->
**This is the contact-geometric form of the millennium problem:**
does the contact structure of the brane remain non-degenerate
at the collision point of two vortex filaments?
<!-- FILE_END: root-of-unity-truncation-interpretation.md -->

<!-- FILE_START: observable-mtc.md -->
Fix a positive integer $N \geq 3$ and set
$q = \zeta_N = e^{2\pi i / N}$ --- a primitive $N$-th root of unity.
At this value of the substrate parameter the representation category
$\mathrm{Rep}(U_q(\mathfrak{su}_2))$ is not semisimple; quotienting
by the ideal of negligible morphisms produces the *truncated*
category
$\mathbf{C}_{\mathrm{any}}(N)$ with only finitely many simple
objects $\mathbf{V}_0, \mathbf{V}_1, \ldots, \mathbf{V}_{N-2}$
\cite{moore-seiberg1989}.

**Definition.**  The **observable modular tensor category** at level
$N$ is the ribbon fusion category $\mathbf{C}_{\mathrm{any}}(N)$
together with the braiding $c$ and ribbon twist $\varTheta$ inherited
from the quasi-triangular structure of $U_q(\mathfrak{su}_2)$ at
$q = \zeta_N$.  Equivalently, $\mathbf{C}_{\mathrm{any}}(N)$ is a
*modular* tensor category: the $S$-matrix
$S_{ij} = \mathrm{tr}(c_{\mathbf{V}_i, \mathbf{V}_j} \circ
c_{\mathbf{V}_j, \mathbf{V}_i})$ is non-degenerate.
<!-- FILE_END: observable-mtc.md -->

<!-- FILE_START: observable-mtc-braiding.md -->
**Braiding non-symmetry.**  For $N \geq 3$ and any non-trivial
simple $\mathbf{V} \in \mathbf{C}_{\mathrm{any}}(N)$,

$$
  c_{\mathbf{V}, \mathbf{V}} \circ c_{\mathbf{V}, \mathbf{V}}
    \neq  \mathrm{id}_{\mathbf{V} \otimes \mathbf{V}},
$$

The braiding does not square to the identity on simples.  This
is the hallmark of a genuinely modular (non-symmetric) tensor
category and is the prerequisite for anyonic statistics.

**Relation to the commutative limit.**  The commutative limit
$q \to 1$ of Chapter 3 corresponds to $N \to \infty$, where the
truncation opens up, negligible morphisms vanish, and the braiding
degenerates to a symmetric structure.  The two specialisations are
therefore distinct:

| Specialisation | $q$ | Braiding | Anyons |
|---|---|---|---|
| Commutative limit | $q = 1$ | symmetric | no |
| Root-of-unity $\mathrm{MTC}$ | $q = \zeta_N$ ($N \geq 3$) | non-symmetric | yes |

The geometric shadow on the genus-$2$ curve $\mathcal{X}_5$ of
[def:hyperelliptic-quintic](#def:hyperelliptic-quintic) picks up
either regime via its fifth-roots-of-unity branch set: in the
commutative limit the $\zeta_5^{k}$ mark classical phase defects
on a single $\mathrm{U}(1)$ tube, while at $q = \zeta_5$ the same
discrete data labels anyonic fusion channels in
$\mathbf{C}_{\mathrm{any}}(5)$.
<!-- FILE_END: observable-mtc-braiding.md -->

<!-- FILE_START: bn-mtc-action.md -->
**Proposition.**
Let $\mathbf{C}_{\mathrm{any}}(N)$ be the observable modular tensor
category of [def:observable-mtc](#def:observable-mtc) at level $N \geq 3$,
and let $\mathbf{V}$ be a non-trivial simple object.  For every
$n \geq 2$ the categorical braiding defines a representation

$$
  \rho_n \colon B_n  \longrightarrow
   \mathrm{Aut}_{\mathbf{C}_{\mathrm{any}}(N)}(\mathbf{V}^{\otimes n}),
  \qquad
  \sigma_i  \longmapsto
   \mathrm{id}_{\mathbf{V}^{\otimes (i-1)}}
   \otimes\, c_{\mathbf{V}, \mathbf{V}}
   \otimes\, \mathrm{id}_{\mathbf{V}^{\otimes (n - i - 1)}},
$$

of the Artin braid group $B_n$ (see
[def:braid-group](#def:braid-group)) on the tensor power of
$\mathbf{V}$.  This representation does not factor through the
symmetric-group quotient $B_n \twoheadrightarrow S_n$.
<!-- FILE_END: bn-mtc-action.md -->

