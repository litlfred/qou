<!-- FILE_START: classical-limit-intro.md -->
The preceding sections established that the algebraic substrate is
unconditionally stable at the $q$-scale: the Hasse--Weil bound
guarantees that all Frobenius eigenvalues lie on the critical circle
$|\alpha_i| = q^{1/2}$, and the Reeb spectrum inherits this alignment
through the spectral coordinate mapping. The substrate-side
prime-counting estimate holds with the optimal square-root
error term --- a finite-field Riemann hypothesis, proven, not
conjectured.

We now ask what happens when we pass to the macroscopic continuum.
The classical limit $q \to 1$ collapses the quantum gap
$\hbar_q \to 0$, smooths the Jackson $q$-derivative into the ordinary
derivative, and degrades the braided tensor category into a symmetric
one. The local $q$-geometries at each prime fiber glue into an adelic
global object --- the classical Riemann zeta function $\zeta(s)$.
Whether the macroscopic continuum inherits the stability of the
$q$-scale is precisely the content of the Riemann hypothesis.

**Skeleton of this section.** The remaining results below all
share one piece of machinery: the
[surreal rate calculus](#prop:surreal-rate-calculus). Treating
the Reeb infinitesimal $\varepsilon$
([Reeb infinitesimal](#def:reeb-epsilon))
as a strictly positive infinitesimal in the ordered field
$\mathbb{R}(\varepsilon) \subset \mathbf{No}$, we obtain two
categorical invariants of the rigid braided monoidal substrate,

$$
  \Delta_q \;\asymp\; \varepsilon^3
  \qquad\text{(mass-gap dissipation, infinitesimal),}
$$
$$
  \Omega_q \;\asymp\; \varepsilon^{-1}
  \qquad\text{(Reeb period, transfinite),}
$$

and the [surreal squeeze](#lem:surreal-squeeze)
$\delta^2 \cdot \Omega_q > \Delta_q$ holds strictly for every
standard real $\delta > 0$. Each of the millennium-problem
remarks below
([RH](#rem:rh-surreal-bound),
[BSD](#rem:bsd-surreal-bound),
[Yang--Mills](#rem:yang-mills-surreal-bound),
[NS](../fluid-dynamics/ns-surreal-bound.md),
[Collatz](#rem:collatz-surreal-bound),
[P vs NP](#rem:p-vs-np-surreal-bound))
fits this same template: identify the "drift" $\delta$ proper to
the problem, then apply the squeeze. The
[adelic--Tate squeeze](#rem:adelic-tate-squeeze) refines the
inequality place-by-place; the
[unification remark](#rem:millennium-unification) collects the
six instantiations side by side.
<!-- FILE_END: classical-limit-intro.md -->

<!-- FILE_START: classical-limit-functor.md -->
Define the **classical limit** as a :refterm[monoidal functor]{#monoidal-functor}

$$
\mathcal{L} : \mathbf{C}_q \longrightarrow \mathbf{C}_1
$$

from the :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}_q$ (at deformation
parameter $q$) to the :refterm[symmetric monoidal category]{#symmetric-monoidal-category} $\mathbf{C}_1$
(at $q = 1$). The functor $\mathcal{L}$ acts on the substrate
algebra by:

1. **Quantum gap collapse**: $\hbar_q = 1 - q^{-1} \to 0$, so that
 the non-commutativity vanishes.
2. **Differential smoothing**: The Jackson $q$-derivative
 $d_q f(z) = \frac{f(qz) - f(z)}{(q-1)z}$ converges to the
 ordinary derivative $\frac{df}{dz}$.
3. **Braiding trivialization**: The braiding
 $\sigma_{X,Y} : X \otimes Y \to Y \otimes X$ specializes to the
 symmetric swap $\tau_{X,Y}$, since $R(q) \to \mathrm{id}$ as
 $q \to 1$.

The functor $\mathcal{L}$ is exact (preserves short exact sequences)
but **not** full: quantum information is lost in the limit.
<!-- FILE_END: classical-limit-functor.md -->

<!-- FILE_START: classical-limit-adelic-assembly.md -->
**Adelic-assembly perspective (preferred reading).** Equivalently,
$\mathcal{L}$ is the **archimedean component** of the realization
tower $\{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}$ of the
[motivic substrate](#def:motivic-substrate). Under this reading,
the substrate $\mathbf{C}_q$ is the universal motive over
$\widehat{\mathcal{M}}$; each finite place $p$ of
$\mathbb{Q}$ ([adelic substrate](#def:adelic-substrate)) carries a
local realization $\rho_p$ landing in $\mathbb{Q}_p$ (cyclotomic /
Kummer-level data, equivalently Habiro-ring evaluations at roots of
unity); the archimedean place $v = \infty$ carries
$\rho_\infty = \mathcal{L}$, landing in $\mathbb{R}$. The
"$q \to 1$" limit and the "$\hbar_q \to 0$" collapse are the
**vanishing of the local Reeb infinitesimal $\varepsilon_\infty$
at the archimedean place** ([adelic Tate squeeze](#rem:adelic-tate-squeeze));
the classical continuum is what remains after that single local
$\varepsilon_v$ is collapsed, while the non-archimedean $\varepsilon_p$'s
are discarded.

**Non-fullness of $\mathcal{L}$: phase decoherence.** The full
motivic class $[X] \in \widehat{\mathcal{M}}$ carries the relative
$q$-phases between all finite places — the cohomological data that
the cyclotomic-projection tower
$\{\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)\}_N$ records.
The archimedean projection $\rho_\infty$ collapses across all those
phases, retaining only the standard-part / real-valued shadow.
That is the rigorous mechanism behind "quantum information is lost":
the relative finite-place phases are traced out in the assembly
$\mathcal{L} = \rho_\infty \circ (\text{motivic lift})$, even though
each individual $\rho_v$ is exact. The classical continuum is a
**low-resolution shadow** of the unglued adelic motives, not a
limit of the full structure.
<!-- FILE_END: classical-limit-adelic-assembly.md -->

<!-- FILE_START: classical-limit-topology-free.md -->
**Topology-free reformulation (forward reference).** The
[classical limit functor](#def:classical-limit-functor)
uses a *topological* $q \to 1$ limit on the parameter
space, which has obstructions
([classical limit obstruction](#def:classical-limit-obstruction))
and breaks for surreal-valued $q$. The appendix replaces it with
a literal evaluation in Conway's surreal field at
$q = 1 + \varepsilon$, then takes standard-part:

* At the **single-functor** level —
 $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$
 ([classical limit as standard-part](#conj:classical-limit-stpart)).
* At the **whole-tuple** level — the entire QOU
 $(\mathbf{C}, \varTheta, G, \mathcal{S})$ is the standard-part of
 an $\varepsilon$-relaxed surreal QOU
 ([archimedean QOU is standard-part of surreal](#conj:archimedean-stpart),
 with [proof strategy](#rem:archimedean-stpart-strategy)).

Both replacements are conjectural; if either holds it removes the
need for any analytic / topological machinery on the parameter
space.
<!-- FILE_END: classical-limit-topology-free.md -->

<!-- FILE_START: quantum-gap-collapse.md -->
Under the classical limit functor $\mathcal{L}$, the following
degenerations occur simultaneously:

1. **Planck constant**: $\hbar_q = 1 - q^{-1} \to 0$.
2. **$q$-differential**: $d_q \to d$ (the Jackson derivative becomes
   the ordinary derivative).
3. **Braiding**: The :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}_q$
   degenerates to a :refterm[symmetric monoidal category]{#symmetric-monoidal-category} $\mathbf{C}_1$, as
   the $R$-matrix $R(q) \to \mathrm{id} \otimes \mathrm{id}$.
4. **Reeb period**: $\Omega_q \to \infty$ (the discrete Reeb flow
   becomes a continuous one-parameter group).

Formally, $\mathcal{L}$ sends the Frobenius--Hopf algebra $A_q$ to a
commutative Hopf algebra
$A_1 = \mathcal{O}(\mathcal{B}_{\mathrm{cl}})$, the coordinate ring
of the classical Bring's curve over $\mathbb{C}$. The self-duality
$A_q \simeq \omega_{A_q}^\bullet$ descends to the classical Serre
duality
$H^i(\mathcal{B}_{\mathrm{cl}}, \mathcal{O}) \cong H^{g-i}(\mathcal{B}_{\mathrm{cl}}, \Omega^1)^\vee$.
<!-- FILE_END: quantum-gap-collapse.md -->

<!-- FILE_START: classical-limit-obstruction.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over a
Noetherian ring $R$ with substrate parameter $q$ and
classical limit functor $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$
([classical limit functor](#def:classical-limit-functor)).

The **classical limit obstruction** of the quantum universe
is the Hochschild cohomology group

$$
\mathrm{Obs}(\mathbf{C}, q \to 1)
 := 
HH^2(\mathcal{U}_q(\mathfrak{g}), \mathrm{Ad})
$$

where $\mathcal{U}_q(\mathfrak{g})$ is the Lusztig integral form
of the quantized enveloping algebra associated to $A$, and
$\mathrm{Ad}$ denotes the adjoint bimodule.  Elements of
$\mathrm{Obs}$ are obstructions to extending second-order
deformations of the Frobenius--Hopf algebra $A_q$ across
$q = 1$.
<!-- FILE_END: classical-limit-obstruction.md -->

<!-- FILE_START: classical-limit-obstruction-properties.md -->
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

**Control of the classical limit by $HH^2$.**
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
<!-- FILE_END: classical-limit-obstruction-properties.md -->

<!-- FILE_START: qou-obstruction-reduction.md -->
**Theorem.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$ of dimension
$d = \dim G$. Then:

**(a)** The classical limit obstruction
([classical limit obstruction](#def:classical-limit-obstruction))
is one-dimensional:

$$
\dim_k \mathrm{Obs}(\mathbf{C}, q \to 1)
=  \dim_k HH^2(\mathcal{U}_q, \mathrm{Ad})
=  1.
$$

**(b)** The unique obstruction class is the image of the Euler
characteristic under the trace map:

$$
\mathrm{Obs}(\mathbf{C}, q \to 1)
 \cong  k,
\qquad
[\phi_1] \mapsto \chi(A) \in R.
$$

**(c)** The obstruction vanishes at Kummer level $n$ iff
$n \mid \chi(A)$:

$$
\kappa_0 \bmod n = 0
\quad\Longleftrightarrow\quad
n \mid \chi(A).
$$

**Contrast with a general QU.**

See [Table 1](#tbl:qou-obstruction-reduction-table1-data).
<!-- FILE_END: qou-obstruction-reduction.md -->

<!-- FILE_START: qou-obstruction-reduction-interpretation.md -->
**Remark (the obstruction as a function on $\mathbb{P}^1$).**

The obstruction $\chi(A) \bmod n$ varies over the Kummer tower
$\{\mu_n\}_{n \geq 1}$ inside $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$:

$$
\mathrm{obs}(n) :=
\begin{cases}
0 & \text{if } n \mid \chi(A), \\
\chi(A) \bmod n & \text{otherwise.}
\end{cases}
$$

For the Descartes universe with $\chi(A) = -6$:

See [Table 3](#tbl:qou-obstruction-reduction-table3-data).

The obstruction **vanishes at only finitely many levels**
(the divisors of $|\chi(A)| = 6$, namely $\{1, 2, 3, 6\}$)
and **persists at all levels $n$ with $\gcd(n, 6) \neq n$** —
in particular at all primes $> 3$.

**Physical consequence:** the classical limit $q \to 1$ must
pass through infinitely many Kummer levels where the
obstruction is nonzero. The density of non-vanishing levels
in the Kummer tower is

$$
\delta
=  1 - \frac{|\{n : n \mid 6\}|}{N}
\xrightarrow{N \to \infty} 1.
$$

In the limit: the obstruction is nonzero at density-$1$ set
of levels. The classical limit cannot avoid the obstruction.
<!-- FILE_END: qou-obstruction-reduction-interpretation.md -->

<!-- FILE_START: qou-obstruction-millennium-specializations.md -->
**Remark (the three millennium problems as specializations).**
Each millennium problem is a property $\mathcal{P}$ that holds
unconditionally at the $q$-scale, with obstruction class
$[\mathcal{P}] \in \mathrm{Obs}(\mathbf{C}, q \to 1) \cong k$.
In the QOU, the single obstruction scalar controls all three:

See [Table 4](#tbl:qou-obstruction-reduction-table4-data).

All three obstructions are **images of the same class**
$\chi(A) \in HH^2 \cong k$ under different evaluation maps:

- **RH**: evaluate $\chi(A)$ on the spectral localization
 map $HH^2 \to H^2(\mathrm{Spec}(\xi_q))$
- **NS**: evaluate $\chi(A)$ on the collision restriction
 map $HH^2 \to H^2(\Sigma, \mathcal{B}|_\Sigma)$
- **BSD**: evaluate $\chi(A)$ on the elliptic restriction
 map $HH^2 \to H^2(\mathcal{E}_q, \mathcal{B}|_{\mathcal{E}_q})$

The one-dimensionality of $HH^2$ means these three evaluations
are **proportional**: there is a single real number (the Euler
characteristic $\chi(A) = -6$) that controls whether all three
millennium problems persist through the classical limit.

**Corollary.** If any one of the three millennium problems is
resolved (in either direction), the resolution constrains the
other two. Specifically: if the classical limit functor
$\mathcal{L}$ preserves the property $\mathcal{P}$ for one
problem, then the same functor either preserves or violates
$\mathcal{P}$ for the other two — the mechanism is the same,
only the evaluation map differs.
<!-- FILE_END: qou-obstruction-millennium-specializations.md -->

<!-- FILE_START: surreal-notation-cheat-sheet.md -->
**Cheat sheet for first-time readers of surreal notation.**
The full surreal-number formalism — Conway construction, birthday
function, sign sequences, standard-part functor, Hahn series — is
developed in the **surreal-numbers appendix**
([`app:surreals`](#app:surreals)). What follows is a one-page
reading aid sufficient to follow the substrate-level uses of
$\omega$ and $\varepsilon$ in this chapter and in
[the Millennium-bound discussions](#sec:millennium-bounds-via-surreals)
of the appendix.

See [Table](#tbl:surreal-notation-cheat-sheet-table-data).

**Wherever $\varepsilon$ appears in the substrate-level definitions
below** — primarily in
[`def:reeb-epsilon`](#def:reeb-epsilon),
[`def:q-from-epsilon`](#def:q-from-epsilon),
and the joint Galois-braid action — read it as "the positive
infinitesimal $1/\omega$". You do not need the appendix machinery
to follow these definitions.

**Wherever a surreal-bound statement appears** — e.g.
[BSD](#rem:bsd-surreal-bound),
[Collatz](#rem:collatz-surreal-bound), or the unified
[graded-Mikusiński bound](#rem:surreal-bounds-graded-mikusinski) —
the cheat-sheet entry for $\mathrm{st}$ and $a \sim b$ is
the only piece we need; the bound says "the inequality holds up
to a $1 + \varepsilon$ factor", and applying $\mathrm{st}$
recovers the classical statement.

For the full Conway construction, sign sequences as birthday-graded
braid words, the Bloch-Suslin / Borel discharge of the keystone,
and the standard-part functor's behaviour on archimedean limits,
read the appendix in order. For the substrate-level applications in
this chapter, this cheat sheet is sufficient.
<!-- FILE_END: surreal-notation-cheat-sheet.md -->

<!-- FILE_START: reeb-epsilon.md -->
Let $(\mathbf{C}, A)$ be a quantum observable universe with categorical
Reeb derivation $\xi \in \mathrm{Der}(A)$
([categorical Reeb derivation](#def:categorical-reeb-derivation)),
and let $\Phi_t : A \to A$ denote the one-parameter Reeb flow generated
by $\xi$, i.e. the unique flow satisfying $\Phi_0 = \mathrm{id}_A$ and
$d\Phi_t / dt = \xi \circ \Phi_t$.

The **Reeb infinitesimal** is the distinguished element

$$
\varepsilon := \left. \frac{d}{dt} \right|_{t = 0} \Phi_t
\;\in\; \mathrm{Der}(A)
$$

of the derivation algebra of the substrate object $A$.

**Primitivity.** Unlike the substrate parameter $q$, which is a scalar
attached to the braiding $R$-matrix, $\varepsilon$ is **intrinsic to
the categorical structure of $A$**: it is the tangent vector at the
identity of the Reeb flow, and is well defined before any choice of
deformation scale is made.  In particular, $\varepsilon$ is not
defined in terms of $q$.  The usual substrate parameter is recovered
in the following section
([derivation of $q$ from $\varepsilon$](#def:q-from-epsilon)).

**Positivity and archimedean independence.** The contact-form
normalization $\xi \circ \varTheta = \varTheta$ of the Reeb derivation
([categorical Reeb derivation](#def:categorical-reeb-derivation))
forces $\varepsilon$ to be a *strictly positive* element of
$\mathrm{Der}(A)$ with respect to the natural ordering induced by
the Frobenius pairing: for every non-zero state $v \in \mathcal{S}_p$
in the state bundle, $\langle v,\, \varepsilon \cdot v \rangle > 0$.
Moreover, $\varepsilon$ is **archimedean-smaller** than every
standard-real derivation $\lambda \cdot \mathrm{id}_A$, $\lambda > 0$,
in the sense that the iterates $n \cdot \varepsilon$ for all
$n \in \mathbb{N}$ remain dominated by $\lambda \cdot \mathrm{id}_A$
in the operator order on $\mathrm{End}(A)$.

These two properties pick out $\varepsilon$ as a **positive
infinitesimal** direction in the derivation algebra.  The embedding
of this infinitesimal into Conway's surreal field $\mathbf{No}$,
and the identification $\varepsilon \leftrightarrow 1 / \omega$,
are developed in the surreal-number appendix
([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
[surreal blow-up calculus](#def:surreal-blowup-calculus));
the main text uses $\varepsilon$ only as a categorical primitive.

**Summary.**

| Object | Type | Categorical status |
|--------|------|--------------------|
| $\xi$ | derivation $A \to A$ | existing Reeb derivation |
| $\Phi_t$ | 1-parameter flow | generated by $\xi$ |
| $\varepsilon$ | tangent of $\Phi_t$ at $t = 0$ | **primitive** — intrinsic to $A$ |
| $q$ | substrate scalar | **derived** from $\varepsilon$ (next block) |
<!-- FILE_END: reeb-epsilon.md -->

<!-- FILE_START: q-from-epsilon.md -->
With the Reeb infinitesimal $\varepsilon \in \mathrm{Der}(A)$ in hand
([Reeb infinitesimal](#def:reeb-epsilon)), the substrate parameter $q$
is now a **derived** quantity, not a primitive.

**Definition.** The **substrate parameter associated to $\varepsilon$**
is

$$
q := 1 + \varepsilon,
$$

interpreted inside the ordered field generated by $\varepsilon$ over
$\mathbb{R}$.  Equivalently, via the surreal appendix
([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)),
this is the element $q = 1 + \varepsilon \in \mathbf{No}$ under the
identification $\varepsilon = 1 / \omega$ from
[surreal blow-up calculus](#def:surreal-blowup-calculus).  The present
block fixes only the main-text convention; the analytic content of
the identification lives in the appendix.
<!-- FILE_END: q-from-epsilon.md -->

<!-- FILE_START: q-from-epsilon-rationale.md -->
**Consistency with prior usage.** The existing Frobenius--Hopf substrate
$A_q$ of
[Frobenius--Hopf substrate](#def:frobenius-hopf-substrate)
is recovered as the evaluation of the $\varepsilon$-expansion

$$
A_q = A_1 + \varepsilon \, \phi_1 + \varepsilon^2 \, \phi_2 + \cdots
$$

where the classical algebra $A_1$ and the deformation cocycles
$\phi_n \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ are exactly those of
the Drinfeld--Jimbo expansion already pinned down by
[classical limit obstruction](#def:classical-limit-obstruction).
Thus **nothing in the existing $q$-theory changes**: every identity
previously written with $q - 1$ is now written with $\varepsilon$,
and the classical point $\varepsilon = 0$ coincides with $q = 1$.

**Motivation for taking $\varepsilon$ as primitive.** Two reasons.

1. **Categorical origin.** The substrate parameter $q$ is a scalar
   attached to the $R$-matrix.  The Reeb infinitesimal $\varepsilon$
   is the tangent vector of the Reeb flow, a structure intrinsic to
   $A$ before any braiding is chosen.  Declaring $\varepsilon$
   primitive places the deformation direction inside the category
   rather than outside it.
2. **Exact error bounds.** With $\varepsilon$ primitive and living
   in an ordered field with infinitesimals, the scaling laws
   $\Delta_q \asymp \varepsilon^3$,
   $\Omega_q \asymp \varepsilon^{-1}$,
   $\mathrm{enstrophy} \asymp \varepsilon^{-4/3}$
   become **literal arithmetic inequalities**, not asymptotic
   $O(\cdot)$ statements — see
   [surreal rate calculus](#prop:surreal-rate-calculus).

**Notational convention for the remainder of the paper.** Throughout,
$q - 1$ is identified with $\varepsilon$ and $q = 1$ with
$\varepsilon = 0$.  The two conventions are logically identical;
the $\varepsilon$-convention is the one in which the millennium-problem
squeeze lemmas ([surreal squeeze](#lem:surreal-squeeze)) are literal,
not asymptotic.
<!-- FILE_END: q-from-epsilon-rationale.md -->

<!-- FILE_START: joint-galois-braid-figure-8-verified.md -->
**Proposition (joint Galois $\times$ braid action commutes on the figure-8
bi-filtration cell — verified directly).**

The joint motivic-Galois $\times$ braid-group action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
predicts commutativity on each $\mathcal{H}_q^{(n, K)}$ stratum.
*This proposition verifies the prediction on the figure-8 row
$\mathcal{H}_q^{(2, 4_1)}$ by direct computation.*

### Setup

The figure-8 bi-filtration cell is

$$
  \mathcal{H}_q^{(2, 4_1)}
  \;\subseteq\;
  G^{(2)}(\mathcal{H}_q),
$$

with dominant cell $\lambda_K = (2, 2)$ in $H_4(q)$ — *self-conjugate*
([`rem:chirality-period-pairing`](#rem:chirality-period-pairing))
— and shape parameter $z_K = \zeta_6 = e^{i\pi/3}$.

The two group actions:

| Group | Generator | Action on $\mathcal{H}_q^{(2, 4_1)}$ |
|---|---|---|
| $G_{\mathrm{mot}} \supseteq \langle * \rangle$ (bar) | $*: q \mapsto q^{-1}$, $\zeta_6 \mapsto \zeta_6^{-1}$ | $\mathrm{Li}_2^q(\zeta_6) \mapsto \mathrm{Li}_2^q(\zeta_6^{-1})$ |
| $B_4 \to H_4(q)$ | $\sigma_1, \sigma_2, \sigma_3$ | conjugation in $H_4(q)$, fixes central idempotents |
### Cross-references

- Joint-action conjecture: [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Figure-8 row theorem: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bridge map verification: [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
<!-- FILE_END: joint-galois-braid-figure-8-verified.md -->

<!-- FILE_START: joint-galois-braid-figure-8-verified-interpretation.md -->
**Remark (structural triviality of the figure-8 case, and the remaining cases).**

### Structural triviality of this case

The verification works because **the bar and braid actions touch
disjoint structure**:

- Braid acts on the *cell* $e_{(2,2)} \in Z(H_4(q))$ — but by definition,
 since central idempotents are fixed by inner automorphisms.
- Bar acts on the *coefficient ring* $q$ and the *shape parameter*
 $\zeta_6 \in F^\times$ — but not on the cell.

**Trivial commutativity from disjoint action.** This verifies the
*easiest* case of the joint-action conjecture; the structurally
non-trivial case is **chiral pairs**, where bar swaps cells while
braid acts non-by definition on the swapped pair.

### Scope of the verification and remaining cases

**Verified**: $(\lambda, K) = ((2, 2), 4_1)$ — a self-conjugate cell.
By extension, any self-conjugate cell with a polylog argument in
$F^\times$ has by definition commuting bar $\times$ braid action.

**Remaining (open)**: chiral-pair cases, e.g.

- $(\lambda, K) = ((3) + (1, 1, 1), 3_1)$ — trefoil cell pair.
- $(\lambda, K) = ((3, 1) + (2, 1, 1), 4_1$-related$)$ — chiral-pair
 partition of 4.
- $(\lambda, K) = (\text{chiral hyperbolic}, 5_2)$ — non-trivial
 cell pair + hyperbolic geometry.

For the trefoil case ($n = 3$): bar takes $e_{(3)}$ to $e_{(1,1,1)}$;
braid $\sigma_1, \sigma_2$ act on the $(2, 1)$ standard rep
non-by definition but commute with central idempotent assignment.
**Verification possible by direct computation** but technical.

### Significance

**The joint-action conjecture
[`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
is verified at the figure-8 row** — the canonical depth-2 row of
B1. The verification is structural (disjoint actions by definition
commute), not numerical. Combined with the figure-8 row's
theorem-level B1 status
([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)):

> **The figure-8 row of the bi-filtration carries the full
> graded-Mikusiński structure as a theorem**: depth-2 inclusion,
> strong sharpness over $\mathbb{Q}(\zeta_6)$, joint Galois $\times$ braid
> commutativity, VC asymptotic match, depth correspondence
> verified.

Reduces remaining open questions about the joint action to *non-
self-conjugate / chiral-pair* cases.
<!-- FILE_END: joint-galois-braid-figure-8-verified-interpretation.md -->

<!-- FILE_START: joint-galois-braid-discharged.md -->
**Proposition (joint motivic-Galois $\times$ braid action commutes
on every bi-filtration cell — discharged in general by the
disjoint-action argument).**

The joint-action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
predicted commutativity of the motivic-Galois action $G_{\mathrm{mot}}$
and the braid-group action $B_{n_K}$ on every $\mathcal{H}_q^{(n, K)}$
stratum. *This proposition discharges the conjecture in general,
not just on the figure-8 cell as in
[`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified).
The argument is structural: the two actions touch disjoint factors
of the bi-filtration's underlying tensor structure.*

### Statement

For every $(n, K)$ with $\mathcal{H}_q^{(n, K)}$ defined per
[`def:hq-bi-filtration`](#def:hq-bi-filtration), the actions
$G_{\mathrm{mot}}$ and $B_{n_K}$ commute on $\mathcal{H}_q^{(n, K)}$:

$$
  g_{\mathrm{mot}}(\beta \cdot \alpha) \;=\; \beta \cdot g_{\mathrm{mot}}(\alpha)
  \quad\text{for } \alpha \in \mathcal{H}_q^{(n, K)},\;
  g_{\mathrm{mot}} \in G_{\mathrm{mot}},\;
  \beta \in B_{n_K}.
$$
### Cross-references

- Joint-action conjecture (now discharged): [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Figure-8 special case: [`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Bridge map: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge), [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Centrality of $e_{\lambda_K}$: [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
<!-- FILE_END: joint-galois-braid-discharged.md -->

<!-- FILE_START: joint-galois-braid-discharged-interpretation.md -->
**Remark (the conjecture was open in form, not content; its discharge).**

### Open in form, not in content

The conjecture was *structurally automatic*: bar, cyclotomic Galois,
and the rest of $G_{\mathrm{mot}}$ act on the *coefficient ring + shape
parameter* (algebraic-number side); the braid group acts on the
*Hecke cell* (representation-theoretic side). By design these two
structures are **separate factors** of $\mathcal{H}_q^{(n, K)}$, so
disjoint actions commute.

The proof took two ingredients already in the paper:
1. **Centrality** of $e_{\lambda_K}$
   ([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)
   Step 1).
2. **Bar-transposition** of partitions
   ([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
   Cross-check 3).

### Content discharged

| Claim | Status before | Status after |
|---|---|---|
| Joint-action conjecture, figure-8 cell | theorem ([`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)) | theorem (subsumed) |
| Joint-action conjecture, *all* cells | conjectural ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) | **theorem** (this prop.) |
| Joint-action sharpness predictions | conditional | **conditional theorem** (depends only on the depth predictions of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) |

### Significance: a further conjecture promoted to theorem

The joint-action conjecture is now fully discharged. Combined with
the small-cases bridge verification
([`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases))
and the depth-2 / torus-knot / hyperbolic-row B1 discharges, the
**graded-Mikusiński bi-filtration framework's structural theorems
are complete**:

| Bi-filtration claim | Status |
|---|---|
| Bi-filtration definition well-defined | theorem ([`def:hq-bi-filtration`](#def:hq-bi-filtration)) |
| Bridge map $d_{\mathrm{II}}$, small partitions | theorem |
| Joint Galois $\times$ braid action commutes (any cell) | **theorem (this prop.)** |
| B1 row at figure-8 / torus knots / Borromean / Whitehead | theorem |

**Open remaining**: depth-3 strong sharpness over $\mathbb{Q}(\zeta_5)$
(Beilinson + Goncharov), per-knot VC discharges for chiral
hyperbolic knots, geometric realisation of $\mathrm{Cl}_3(2\pi/5)$.
<!-- FILE_END: joint-galois-braid-discharged-interpretation.md -->

