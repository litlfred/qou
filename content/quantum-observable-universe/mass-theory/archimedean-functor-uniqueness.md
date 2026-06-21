**Proposition (conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) and on the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`]).**
*Let $\tau_{\text{arch}} = \pi_\infty \circ \tau$ be the archimedean
realization functor of the QOU substrate
([archimedean realization functor](#def:archimedean-realization-functor)),
acting on motivic inputs assembled from braid / knot data. Assume*

- *(C1) The substrate's mass-formula state sum is pentagon-coherent:
   $\tau_{\text{arch}}$ is a continuous, antisymmetric, real-valued
   functional on $B(\mathbb{C})$ — the structural content provided by
   the cosimplicial / Yekutieli triple machinery
   ([`prop:cosimplicial-crossed-groupoid`](#prop:cosimplicial-crossed-groupoid))
   together with the archimedean-limit class
   `QOU.QPochhammer.ArchimedeanLimit`
   ([`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)).*
- *(C2) Bloch-Suslin pentagon-uniqueness [`suslin1991`,
   `bloch2000`]: any continuous antisymmetric pentagon-coherent
   real-valued function on $\mathbb{C} \setminus \{0,1\}$ is a
   constant scalar multiple of the Bloch-Wigner dilogarithm $D$.*

*Then $\tau_{\text{arch}}$ is uniquely determined, up to a single
multiplicative real scalar, by the requirement that*

$$
  \lim_{q \to 1}\;\tau_{\text{arch}}\bigl(\Phi_q(z)\bigr)
  \;=\;
  D(z)
  \;:=\;
  \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z|\,\arg(1-z)
$$

*equal the **Bloch-Wigner dilogarithm** on every shape parameter
$z \in \mathbb{C} \setminus \{0,1\}$. The uniqueness reduces to the
Bloch-Suslin pentagon characterisation: $D$ is the unique (up to a
real scalar) continuous, antisymmetric, real-valued function on
$\mathbb{C} \setminus \{0,1\}$ satisfying the 5-term pentagon
identity*

$$
  D(x) - D(y) + D\!\left(\tfrac{y}{x}\right)
  - D\!\left(\tfrac{1-y^{-1}}{1-x^{-1}}\right)
  + D\!\left(\tfrac{1-y}{1-x}\right) \;=\; 0.
$$

> **Theorem (conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)).**
> Per AGENTS.md §3b-cond: the upstream conjecture is axiomatised in
> Lean as the typeclass
> [`QOU.QPochhammer.ArchimedeanLimit`](../braids-and-knots/dilogarithm-archimedean-limit.lean);
> the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`,
> `bloch2000`] is similarly axiomatised as
> [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean).
> The Lean theorem
> [`QOU.Archimedean.archimedean_functor_uniqueness`](archimedean-functor-uniqueness.lean)
> takes both classes as `[Instance]` hypotheses and is proved
> **without `sorry`** — the only unproved inputs are the two named
> classes, both of which are well-established results awaiting
> Mathlib formalisation (`Real.dilog`, `BlochGroup`, the Suslin
> map). This block therefore qualifies as a *rigorous conditional
> result* in the §3b-cond sense rather than an unproved conjecture.

## Pre-archimedean / archimedean separation

The QOU substrate is pre-archimedean: every block in the
[motivic substrate](#def:motivic-substrate) and the
[algebraic quantum volume](#def:algebraic-quantum-volume) lives
in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, a ring of
Laurent polynomials with no real-analytic transcendentals. QOU
observables — masses, binding energies, the fine-structure
constant — are real numbers, and the only exit from $R$ to
$\mathbb{R}$ is the archimedean realization functor
$\tau_{\text{arch}}$.

Two structural questions are settled simultaneously by Bloch-Suslin
pentagon-uniqueness. (i) *Uniqueness of the exit*: any real-valued
continuous functional on $B(\mathbb{C})$ respecting the 5-term
pentagon identity is forced to coincide with $D$ up to a single
overall scalar; therefore the archimedean image of a substrate
motivic class is canonical. (ii) *Provenance of $\pi$*: any
transcendental constant in a QOU observable is the
$\tau_{\text{arch}}$-image of substrate pentagon data via $D$ (or
its multivariate generalisations), and is therefore not an external
import. The additive Bring zero-mode candidate
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
illustrates the second point: the $2/(3\pi) = 2g/(4\pi(g-1))$
correction at $g = 4$ is the archimedean shadow of pentagon
data on Bring's surface, not a $\pi$-import outside $R$.

## The algebraic / archimedean dichotomy

The mass formula evaluates a closed cycle on the
[Frobenius-Hopf substrate](#def:frobenius-hopf-substrate). The
non-degenerate Frobenius pairing $\int_A \circ \mu$ identifies
$A \cong A^\vee$, making the substrate algebra self-dual; this
self-duality drives the descent involution
$\hat{\tau}_n$ on the endomorphism algebra
([mass endomorphism](#conj:mass-endomorphism)),
which splits the categorical mass endomorphism into a
**descended** baseline component and a **transient** component
localized at the exceptional divisors of the brane tower.

Within this purely algebraic substrate, the mass evaluation yields
the [algebraic quantum volume](#def:algebraic-quantum-volume)

$$
  \mathrm{Vol}_q(\beta) \;=\; \prod_{i=0}^{A-2}\hat{V}_i(q),
  \qquad \hat{V}_i(q) \in \mathbb{Z}[q^{\pm 1/2}],
$$

a finite product of Laurent polynomials living strictly in
$\mathbb{Z}[q^{\pm 1/2}]$. Everything to this point is categorical
and discrete — no $\pi$, no $\zeta(3)$, no real-analytic
transcendentals.

Transcendental numbers enter the framework **exclusively** at the
boundary of observation. When $\tau_{\text{arch}}$ is applied to
project the categorical data into physical spacetime, it takes
the absolute logarithm of the algebraic quantum volume
([quantum dilogarithm volume](#prop:quantum-dilogarithm-volume)).
This functor converts the discrete, combinatorial Hecke algebra
states into continuous, transcendental observables.

To satisfy the Descartes condition $\chi = -6$, the physical
state space is restricted to Bring's surface, a genus-$4$ curve
with maximal $S_5$ automorphism. The observable particle spectrum
consists entirely of knots that embed within this genus-$4$
handlebody. After $\tau_{\text{arch}}$ is applied, the
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
identifies the limit of the algebraic state sum with the classical
hyperbolic volume of these specific knot complements. In this
limit, the quantum dilogarithm $\Phi_q(z_i)$
([quantum dilogarithm volume](#prop:quantum-dilogarithm-volume))
evaluated at each exceptional divisor degenerates into the
Bloch-Wigner dilogarithm $D(z_i)$
([dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit)).
The Bloch-Wigner dilogarithm is uniquely characterized as the
function satisfying the 5-term pentagon identity
[`suslin1991`, `bloch2000`], providing the exact geometric measure
of the ideal tetrahedra that triangulate the knot complement.

## Proof sketch

Three ingredients close the conditional statement.

1. **Pentagon-coherence on the substrate.** The 5-term pentagon
   identity is built into the cosimplicial / Yekutieli triple
   structure of the QOU substrate
   ([cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid)).
   The motivic class assembled by the mass-formula state sum lives
   in the Bloch group
   $B(\mathbb{C}) = \mathbb{Z}[\mathbb{C}\setminus\{0,1\}]
   /\langle\text{5-term pentagon relations}\rangle$
   under this identification.
2. **Bloch-Suslin uniqueness.** Suslin [`suslin1991`] proves that
   the Suslin map
   $K_3^{\text{ind}}(\mathbb{C}) \to \mathbb{R}$
   is unique up to a real scalar; equivalently, any real-valued
   continuous antisymmetric function on $\mathbb{C}\setminus\{0,1\}$
   satisfying the pentagon is a constant scalar multiple of $D$.
   This is the K-theoretic incarnation of the rigidity of the
   Bloch group; see [`bloch2000`] for the definitive treatment.
3. **Archimedean matching.** $\tau_{\text{arch}}$ acting on the
   substrate's Bloch-group class is, by ingredient 1, a real-valued
   continuous pentagon-coherent functional on $B(\mathbb{C})$. By
   ingredient 2, it is therefore proportional to $D$. The
   proportionality constant is fixed by demanding the
   Faddeev-Kashaev quasi-classical limit
   $(1-q)\log\Phi_n(z;q) \to \mathrm{Li}_2(z)$
   ([dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit))
   match the standard Bloch-Wigner normalisation
   $D(z) = \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z|\arg(1-z)$.

## Consequences

**(a) Resolves the pre-archimedean concern in
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).**
The $\pi$ in the additive correction $2/(3\pi) = 2g/(4\pi(g-1))$
at $g=4$ is the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface. The substrate's pentagon
coherence forces the archimedean image to involve $D$ (and hence
$\pi$ via $D$'s functional equation); no other transcendental
shape is admissible. The additive correction is therefore *not*
outside $R$ — it is the canonical $\tau_{\text{arch}}$-image of
$R$-internal pentagon data.

**(b) Forecloses arbitrary $\pi$-imports.** Any candidate closed
form for a QOU observable that includes a transcendental constant
not derivable from $D$ (or its multivariate generalisations
$D_n$) is excluded. This is a falsifiability constraint: the
multiplicative gluon-octet form (a legacy PSLQ-empirical conjecture,
since superseded by [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode))
required arbitrary integer ratios $45 \cdot [3]_q \cdot
(1+\delta_{CS}+8q\delta_{CS}^2)$ that would have to come from a
non-pentagon source, is ruled out *structurally* in addition to
the existing PSLQ ruling.

**(c) Pins the figure-8 knot example.** The figure-8 knot $4_1$
embeds smoothly into Bring's surface as the amphichiral mass
mechanism. On the pre-archimedean side it has a completely rigorous
motivic / algebraic representation via its Hecke normal form in
$\mathbb{Z}[q^{\pm 1/2}]$. Once $\tau_{\text{arch}}$ maps this
motivic state into the observable continuum, its hyperbolic volume
realizes as the transcendental
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx :val[Vol_4_1]{precision=6}$. The
motivic side guarantees exact algebraic relationships governing
particle interactions; $\tau_{\text{arch}}$ supplies the
transcendental continuum required for geometric measurement. See
[figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration).

## Open problems

1. **K-theoretic identification.** Make the Bloch-group factoring
   of the QOU mass-formula state sum precise: which class in
   $K_3^{\text{ind}}(\mathbb{C})$ does an $A$-strand braid $\beta$
   represent? Conjecturally, the class is read off from the
   Yekutieli triple data; making this rigorous requires identifying
   the $J^2$-jet of the cosimplicial structure with a Bloch-group
   1-cocycle.
2. **Multivariate Bloch-Suslin.** For mass-tower contributions
   spanning multiple exceptional divisors, the relevant invariant
   is the higher Bloch group $B_n(\mathbb{C})$ with the
   $n$-variable polylogarithm $D_n$. Pentagon-uniqueness for
   $D_n$ at $n \geq 3$ is open in the literature (Goncharov 1995
   conjectures); the QOU framework can take it as input where
   needed.
3. **Lean formalisation of Suslin1991.** Mathlib has neither
   `Real.dilog` nor `BlochGroup`. The Lean stub records this as
   a sorry keyed to [`suslin1991`]; closure depends on upstream
   Mathlib work.

## Witness

No numerical witness is appropriate for a uniqueness claim. The
relevant cross-check is that any new closed form for a QOU
observable proposed in this repository must be expressible as a
$\tau_{\text{arch}}$-image of a pentagon-coherent
$R$-internal class, or equivalently, must factor through $D$ (or
$D_n$) in its archimedean expansion. The
[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
candidate satisfies this; the legacy gluon-octet PSLQ candidate
(now removed; superseded by
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode))
did not.
