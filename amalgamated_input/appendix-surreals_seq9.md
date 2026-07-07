<!-- FILE_START: infinitesimal-observability.md -->
The QOU observability axiom requires
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def:quantum-observable-universe)
condition (ii)): the trivial representation does not appear in
the adjoint of $A$. This is a *rigidity* condition that
guarantees $A$ has no infinitesimal symmetries beyond the
identity.

Under a surreal lift, this can be relaxed to allow
infinitesimally many symmetries.

## Conjecture

The **$\varepsilon$-relaxed observability axiom** is:

$$
  \dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))
   \;\leq\; \varepsilon,
$$

interpreted as: the hom-space is non-empty but every element has
$\mathbf{No}$-norm bounded by an infinitesimal $\varepsilon$.

The conjecture: a surreal QOU satisfying $\varepsilon$-relaxed
observability has standard-part image satisfying strict
observability.

## Plausibility

In the archimedean case, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$
is either zero or non-zero — there is no "small" middle ground.
In the surreal case, hom-spaces are $\mathbf{No}$-modules, so
"small" becomes "infinitesimal-norm" in a meaningful sense.

A natural example: take a strict-observability $A$ and add an
infinitesimal generator $\xi \in \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$
with $|\xi| = \varepsilon$. The resulting structure is a surreal
QOU with $\dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))
= 1$ but $|\xi| = \varepsilon$, so the condition is satisfied if
"$\leq \varepsilon$" is read as norm-bound.

Whether such $\xi$ can be constructed cohomologically (rather than
imposed by hand) is open. The natural source is a non-trivial
class in $\mathrm{HH}^1(A, A)$ that becomes trivialised in the
archimedean limit but persists at infinitesimal order.

## Standard-part recovery

Applying $\mathrm{St}$ kills the infinitesimal $\xi$ (since
$\mathrm{st}(\varepsilon) = 0$), so the archimedean image has
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ — strict
observability is recovered. This is the easy direction of the
conjecture.

The hard direction is **lifting**: given an archimedean QOU with
strict observability, does there exist a surreal QOU above it
with relaxed observability and a non-trivial $\xi$? If so, the
relaxation is a strict generalisation; if not, the relaxation is
a tautology.

## Significance

The observability axiom controls *what counts as an observable*
in QOU: if $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, every
endomorphism of $A$ is detectable by the fibre functor $\tau$.
Under the relaxation, infinitesimally many endomorphisms might be
*almost-detectable* — visible at first order in $\varepsilon$ but
invisible to standard-part archimedean observers.

Under a physical reading (if one is allowed): this corresponds
to *near-symmetries* — symmetries that are spontaneously broken
at archimedean scale but restored at infinitesimal scale. The
analog in particle physics is approximate isospin or chiral
symmetry, which are exact in some idealised limit and broken at
the physical scale by small parameters.
## Proof strategy

Same architecture as
[infinitesimal-frobenius](#conj:infinitesimal-frobenius):

**Standard-part recovery (provable now)**:

1. Given an $\varepsilon$-relaxed observability witness $\xi \in
   \mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ with
   $|\xi| \leq \varepsilon$.

2. $\mathrm{St}(\xi) = 0$ by `standardPart_of_infinitesimal`.
   The standard-part of the hom-space contains no non-zero
   elements: $\mathrm{Hom}_{\mathbb{R}}(\mathbf{1},
   \mathrm{Ad}(\mathrm{St}(A))) = 0$.

3. Strict observability holds for the standard-part image.

**Strict generalisation (open)**:

4. Construct a candidate non-trivial $\xi$. Source: a class in
   $\mathrm{HH}^1(A, A) \otimes_{\mathbb{R}} \mathbf{No}$ that
   becomes infinitesimal under standard-part.

5. Show that $\xi$ is **not** in the image of any classical (i.e.
   strict) Hochschild representative — this would establish
   strict generalisation.

**Required infrastructure**:
- `standardPart_of_infinitesimal` (proved).
- Surreal-coefficient Hochschild cohomology (does not exist in
  mathlib).
- A specific cohomological computation distinguishing
  $\mathrm{HH}^1_{\mathbb{R}} \otimes \mathbf{No}$ from
  $\mathrm{HH}^1_{\mathbf{No}}$.

**Falsification path**: prove that every infinitesimal element
of $\mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ comes
from a *real* element scaled by $\varepsilon$ (i.e., $\xi = \varepsilon
\cdot \eta$ for some $\eta \in \mathrm{Hom}_{\mathbb{R}}$). If
$\eta$ must vanish for $\xi$ to satisfy the original observability
constraint, the relaxation is empty.

**Provability assessment**: identical to
[infinitesimal-frobenius](#conj:infinitesimal-frobenius). One
side trivial, the other requires deformation theory.
<!-- FILE_END: infinitesimal-observability.md -->

<!-- FILE_START: vacuum-epsilon.md -->
The Hoefsmit scattering pipeline assigns to each link $L$ a
*geometric energy* $\mathrm{Geom}(L) \in \mathbb{R}$
([Hoefsmit scattering pipeline](#conj:hoefsmit-scattering-pipeline)).
The vacuum normalisation requires $\mathrm{Geom}(\unicode{9737}) = 0$
on the unknot, so that the empty link contributes nothing to
particle masses.

This strict-zero condition is awkward in two ways:

1. It introduces a *boundary case* — the unknot must be
 special-cased in the geometric-energy formula.
2. It is *suspicious on physical grounds* — a "vacuum energy" of exactly
 zero is the textbook signature of a fine-tuned theory, and is
 thought by many to be the wrong setting (cosmological
 constant problem, vacuum-fluctuation arguments, etc.).

Under a surreal lift, the strict zero can be relaxed.

## Conjecture

The **$\varepsilon$-relaxed vacuum axiom** is:

$$
  \mathrm{Geom}(\unicode{9737}) \;=\; \varepsilon \in \mathbf{No},
$$

a single positive infinitesimal. The conjecture: every surreal
QOU satisfies this relaxation with some choice of $\varepsilon
> 0$, and the standard-part recovers the strict vacuum:
$\mathrm{st}(\varepsilon) = 0$.

## Corollaries

If the conjecture holds, several existing results lift:

1. **Geometric-energy formula** simplifies: the special case for
 $\unicode{9737}$ is absorbed into the general formula, giving
 $\mathrm{Geom}(L) = (\text{generic formula}) +
   \varepsilon \cdot (\text{number of unknot components})$.

2. **Möbius energy regularisation** maps : the diagonal
 subtraction in the Möbius energy is exactly the
 $\varepsilon$-vacuum contribution.

3. **Mass spectrum** acquires an infinitesimal shift: every
 particle mass $\mathfrak{m}(\mathfrak{H})$ becomes
 $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$
 for some standard-real $c_{\mathfrak{H}}$. Standard-part of
 this shift is zero, so archimedean predictions are unchanged.

4. **Boundary-conditioned vacuum sums become finite**: when the
 multiplier of $\varepsilon$ is not a standard real but a
 surreal-infinite mode count, the product can have *nonzero*
 standard part, since $\omega \cdot \varepsilon = 1$. The
 parallel-plate geometry realises exactly this case: the
 [Casimir force](#conj:casimir-epsilon-vacuum) is the
 $\mathrm{st}$-image of the plate-constrained unknot-count
 gradient times $\varepsilon$. Consequences 3 and 4 are the two
 regimes of the same axiom — a finite multiplier leaves
 archimedean predictions unchanged, while a surreal-infinite
 multiplier returns a finite force.

## Significance

Two reasons:

1. **Cleaner axioms**: the strict-zero vacuum is a fine-tuning
 that would-be reviewers can object to. The
 $\varepsilon$-vacuum is a parameter, not a fine-tuning, and
 the archimedean theory is recovered by standard-part.

2. **Möbius regularisation absorbed**: the diagonal-subtraction
 trick in the Möbius energy
 ([Möbius energy proof](#prf:mobius-energy)) becomes a special
 case of $\varepsilon$-vacuum subtraction. This unifies two
 regularisations into one.

## Discussion

**Open**. The conjecture is the most directly testable of the
appendix's relaxation conjectures: pick an
$\varepsilon \in \mathbf{No}$, recompute the QOU mass spectrum,
and check whether the archimedean image agrees with the strict-
vacuum prediction. The arithmetic is rational in $\varepsilon$,
The test reduces to a comparison of two polynomials in
$\varepsilon$ at the standard-part.

## Proof strategy

The most direct of the conjectures: pure computation.

1. **Recompute geometric energy** with vacuum convention
 $\mathrm{Geom}(\unicode{9737}) = \varepsilon$. For each link
 $L$ in the QOU mass table (Z=1–20),
 $\mathrm{Geom}(L)$ now has an additive $\varepsilon$-dependent
 correction proportional to the number of unknot components.

2. **Recompute particle masses**:
 $\mathfrak{m}(\mathfrak{H}) \to \mathfrak{m}(\mathfrak{H}) +
   \varepsilon \cdot c_{\mathfrak{H}}$.

3. **Apply $\mathrm{St}$**: standard-part of
 $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$
 equals $\mathfrak{m}(\mathfrak{H})$ — the original mass. So
 archimedean predictions are unchanged.

4. **Verify Möbius regularisation absorbed**: show that the
 diagonal subtraction in
 [Möbius energy proof](#prf:mobius-energy) is exactly
 $\varepsilon \cdot (\text{boundary contribution})$, so the
 classical regularisation is the $\mathrm{St}$-image of the
 $\varepsilon$-vacuum subtraction.

**Required infrastructure**:
- `QOU.AppendixSurreals.standardPart_of_infinitesimal` (proved).
- `QOU.AppendixSurreals.standardPart_add` (axiomatic).
- Existing QOU mass table.

**Falsification path**: recompute the mass spectrum with
$\mathrm{Geom}(\unicode{9737}) = \varepsilon$ and find that some
particle mass *changes* under standard-part (i.e.,
$\mathrm{St}(\mathfrak{m} + \varepsilon \cdot c) \neq \mathfrak{m}$).
This would only happen if $c$ contained a non-infinitesimal
factor, contradicting the rational-in-$\varepsilon$ structure.

**Provability assessment**: this is a *computational* conjecture.
The verification is a mass-table re-computation that can be
done in Python/Mathematica today. Lean formalisation reduces to
the standard-part-of-infinitesimal lemma already proved.

**Easiest of the appendix conjectures to settle.**
<!-- FILE_END: vacuum-epsilon.md -->

<!-- FILE_START: casimir-epsilon-vacuum.md -->
**Conjecture (Casimir force as standard-part of $\varepsilon$-vacuum
density gradient).**
*Assume the [$\varepsilon$-relaxed vacuum axiom](#conj:vacuum-epsilon) —
every unknot component of a link $L$ contributes an infinitesimal
$\varepsilon \in \mathbf{No}$ to $\mathrm{Geom}(L)$. Let two parallel
conducting plates of area $A$ separated by $d$ constrain the
unknot-component count of the vacuum to a surreal-valued density
$N_{\unicode{9737}}^{\text{in}}(A, d) \in \mathbf{No}$ between the
plates and $N_{\unicode{9737}}^{\text{out}}(A, d)$ outside. The
standard physical Casimir force per unit area*

$$
\frac{F_{\text{Cas}}(d)}{A} \;\approx\; -\,\frac{\pi^{2}\,\hbar c}{240\, d^{4}}
$$

*is recovered as the standard-part of the surreal-energy gradient*

$$
\frac{F_{\text{Cas}}(d)}{A} \;=\; -\,\mathrm{st}\!\left(
  \frac{1}{A}\,\frac{\partial}{\partial d}\,
  \bigl[\,N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d)\,\bigr] \cdot \varepsilon
\right).
$$

## Non-annihilation of $\mathrm{st}$

A naive reading would assert $\mathrm{st}(\varepsilon) = 0$ and
conclude the force vanishes. The conjecture is precisely that this
is wrong — and that the same structural mechanism rescues both the
Casimir calculation and the cosmological-constant problem.

$\mathrm{st}$ annihilates a generic product $X \cdot \varepsilon$
*only when $X$ is finite* (i.e., in the valuation ring of
$\mathbf{No}$; see [`conj:archimedean-stpart`](#conj:archimedean-stpart)).
The unknot-component count between two plates is *not* finite — it
is surreal-infinite, matching the birthday rank of the standard
physics zero-point-mode count, which diverges. The relevant
arithmetic is

$$
\omega \cdot \varepsilon \;=\; 1 \quad (\varepsilon := \omega^{-1}),
$$

an infinitesimal times a surreal-infinite *is* a finite surreal.

Concretely, the conjecture asserts

$$
N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d)
\;=\; -\,\frac{\pi^{2}}{720}\,\frac{A}{d^{3}}\,\hbar^{2}_{q}\,\hbar c \cdot \varepsilon^{-1}
\;+\; \bigl(\text{lower-birthday corrections}\bigr),
$$

where $\hbar_{q} = 1 - q^{-1}$ is the substrate-Planck constant
([`def:quantum-planck-constant`](#def:quantum-planck-constant)).

The $\hbar^{2}_{q}$ factor is forced by dimensional consistency
with the Hoefsmit normalisation
$\mathrm{Geom}_\varepsilon(L) = \mathrm{Vol}(L)/\hbar^{2}_{q}
\cdot \mathrm{linking\_weight}(L)$
([`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline)):
$N_\unicode{9737}$ disjoint copies of the unknot contribute
$\mathrm{Geom}_\varepsilon(N_\unicode{9737} \cdot \unicode{9737})
= N_\unicode{9737} \cdot \varepsilon / \hbar^{2}_{q}$
(disjoint-union additivity of $\mathrm{Vol}$, linking_weight = 1
on disjoint unknots, per the
[Hoefsmit-additivity probe](../../../computations/probes/casimir-hoefsmit-additivity-probe.witness.json)).
The $\hbar^{2}_{q}$ in the denominator cancels the same factor in
$N_\unicode{9737}$'s formula above, leaving a finite real energy:

$$
\mathrm{Geom}_\varepsilon\bigl((N^{\text{in}}_\unicode{9737} - N^{\text{out}}_\unicode{9737}) \cdot \unicode{9737}\bigr)
\;=\; -\,\frac{\pi^{2}}{720}\,\frac{A}{d^{3}}\,\hbar c
\;+\; o(1).
$$

Applying $\partial/\partial d$ and dividing by $A$ recovers the
textbook Casimir force per unit area exactly (see the conditional
derivation below).

## Structural appeal

This is the same mechanism that closes the cosmological-constant
puzzle in surreal language: vacuum energy is "$\infty \cdot 0$" in
the archimedean view (infinite mode count times zero per-mode
energy) but a finite surreal in $\mathbf{No}$. The strict-vacuum
axiom $\mathrm{Geom}(\unicode{9737}) = 0$ throws away exactly this
product; the $\varepsilon$-relaxed axiom keeps it.

The Casimir effect is *the* clean experimental probe of this
product because the plate boundary condition selects a specific
finite *gradient* of an otherwise-infinite mode-count.

## Conditional implication (rigorous chain)

Given:

1. The $\varepsilon$-relaxed vacuum axiom
   [`conj:vacuum-epsilon`](#conj:vacuum-epsilon).
2. A plate-constrained unknot-density function satisfying
   $$
     N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d)
     \;=\; -\,\frac{\pi^{2}}{720}\,\frac{A}{d^{3}}\,\hbar^{2}_{q}\,\hbar c \cdot \varepsilon^{-1}
     \;+\; o(\varepsilon^{-1}).
   $$
3. Standard-part arithmetic
   [`conj:archimedean-stpart`](#conj:archimedean-stpart) and the
   standard-part functor [`def:standard-part-functor`](#def:standard-part-functor).

The textbook Casimir force per area follows by direct computation:

$$
\begin{aligned}
-\,\mathrm{st}\!\left(\tfrac{1}{A}\,\partial_{d}\!\bigl[N^{\text{in}}_{\unicode{9737}} - N^{\text{out}}_{\unicode{9737}}\bigr]\cdot \varepsilon\right)
&= -\,\mathrm{st}\!\left(\tfrac{1}{A}\,\partial_{d}\!\left[-\tfrac{\pi^{2}}{720}\tfrac{A}{d^{3}}\hbar c \cdot \varepsilon^{-1}\right]\cdot \varepsilon\right) \\
&= -\,\mathrm{st}\!\left(\tfrac{3\,\pi^{2}}{720}\,\tfrac{\hbar c}{d^{4}}\,\varepsilon^{-1}\cdot \varepsilon\right) \\
&= -\,\tfrac{\pi^{2}}{240}\,\tfrac{\hbar c}{d^{4}}.
\end{aligned}
$$

The sign is attractive: the gradient of the mode-count deficit
points away from the plates, and the negative force per area is
toward each other.

This conditional derivation is rigorous *modulo* the surreal-
arithmetic infrastructure already proved in
[`conj:archimedean-stpart`](#conj:archimedean-stpart). The
conditional kind (theorem-from-hypothesis) is the §3b-cond pattern:
the Lean formulation in `CasimirEpsilonVacuum.lean` takes
`[VacuumEpsilon]` and the plate-mode-count class as explicit
instance hypotheses.

## Open conjecture

The conjecture has three sub-problems, in decreasing tractability:

1. **Existence of $N_{\unicode{9737}}^{\text{in}}(A, d)$ as a
   categorical object.** There must be a construction within QOU
   producing a surreal-valued unknot-density that varies with
   plate geometry. The natural candidate is the Yekutieli-
   homotopy lift of the link-projection functor restricted to
   plate-bounded ambient isotopy — the full lift has not been
   written. *Tractability: medium.* The plate boundary is a
   conformal boundary condition on $\mathbb{R}^{3}$, which the
   substrate-conformal structure of QOU already accommodates.
   The *trace functional* the lift must reduce to is, however,
   pinned down by an **n-stability** criterion: a single-number
   observable cannot depend on the mode-cutoff $n$, and among the
   candidate functionals only the bare disjoint-component count is
   $n$-stable (the Jones value $\delta^{n-1}$ of the $n$-unlink and
   the unnormalised Wenzl sum $\sum_\lambda y_\lambda$ both diverge
   in $n$; the normalised Markov trace is $\equiv 1$ for any
   identity). Under the free-field $\leftrightarrow$ disjoint-unknot
   identification (Maxwell linearity $\Rightarrow$ unbraided modes
   $\Rightarrow$ no $y_\lambda$ weighting), the bare count is the
   physical functional.

2. **Scaling $A/d^{3} \cdot \varepsilon^{-1}$.** This is the
   standard-physics mode-count for parallel-plate Casimir. The
   QOU conjecture is that the *categorical* mode count — counting
   allowed unknot configurations in the plate-bounded ambient
   space — has the same archimedean scaling. *Tractability:
   medium.* The scaling follows from dimensional analysis on the
   substrate metric *if* the categorical mode-count has the
   expected birthday-rank dependence on $d$.

3. **Numerical prefactor $\pi^{2}/720$.** Recovers in standard
   physics from $\sum_{n\geq 1} n^{3}$ regularised to
   $\zeta(-3) = -B_{4}/4 = 1/120$ via $\zeta$-function
   regularisation. Under the disjoint-unknot model selected in
   sub-problem 1, the QOU mode-count carries the same geometric
   per-level degeneracy $\propto n^{3}$ with **no** $y_\lambda$
   weighting, so the prefactor follows from the *same* $\zeta(-3)$
   together with the $k_\perp$ geometric factor:
   $(\pi^{2}/6)\cdot|\zeta(-3)| = \pi^{2}/720$, with $q$ absent.
   This is a derivation *conditional* on the disjoint-unknot
   identification; the earlier expectation that the prefactor would
   require a non-trivial Markov trace on $H_{n}(q)$ is superseded —
   q-deformation re-enters only when modes braid (field
   interactions), at the subleading $1/d^{6}$ order. *Tractability:
   conditional on sub-problem 1.*

## Falsification path

If a categorical plate-constrained mode-count is constructed and
its surreal coefficient *does not* match
$-\pi^{2} A/(720\, d^{3}\, \varepsilon)$, the conjecture is
refuted.

The standard-physics value of $\pi^{2}/240$ (Casimir 1948) is
verified experimentally to $\sim 1\%$ (Mohideen–Roy 1998,
Lamoreaux 1997). The QOU leading term reproduces it exactly, so
this is a **consistency check** the framework passes within the
$\sim 1\%$ window — *not* a measurement that discriminates QOU from
standard QED, since both predict the textbook force. The
substrate-distinctive signal is the interacting-mode $1/d^{6}$
correction (relative size $\sim\alpha\,\lambda_C/d \approx 10^{-8}$),
which is swamped by finite-conductivity, thermal, and roughness
corrections by $\sim 10^{6}$–$10^{8}$ and is therefore not
experimentally accessible at present. The framework's live
falsification leverage is cross-sector: the same substrate $q_0$
(fixed by $\mathrm{Vol}(4_1)$ in $m_p/m_e$) is tested against
high-precision mass and decay measurements. See the
[operative-bar status audit](../../../docs/audits/2026-06-01-casimir-operative-bar-status.md).

A *weaker* partial test: if the $1/d^{4}$ scaling is recovered
but the prefactor differs, the conjecture is refined rather than
killed — analogous to the "Round-8" partial results in
[`conj:bohr-radius-categorical`](#conj:bohr-radius-categorical),
where shell-spacing ratios match but the absolute scale is
transported.

## Significance

Three reasons:

1. **Consistency test of the $\varepsilon$-vacuum axiom.** The
   Casimir effect is a clean *theoretical* setting for the
   $\varepsilon$-vacuum construction: reproducing the textbook
   force shows the relaxation is compatible with established
   physics ([`conj:vacuum-epsilon`](#conj:vacuum-epsilon)). It is a
   consistency check rather than a discriminating measurement (the
   substrate-distinctive signal is experimentally inaccessible; see
   the Falsification-path note above).

2. **Cosmological-constant heuristic.** The same
   "$\omega \cdot \varepsilon = $ finite" mechanism that drives
   Casimir would in principle apply to the cosmological
   constant — but only if the birthday rank of the relevant
   mode-count is bounded, which the Casimir derivation
   suggests it is (matching $A/d^{3}$). A QOU cosmological
   constant would then be a *boundary-conditioned* surreal
   sum, not a free parameter.

3. **Identifies the next infrastructure target.** The
   categorical plate-mode-count function
   $N_{\unicode{9737}}^{\text{in}}(A, d)$ is a concrete
   construction target with a known archimedean image. Building
   it would test the $\varepsilon$-vacuum axiom and provide a
   template for other boundary-conditioned vacuum problems
   (Lamb shift, Polyakov loops, plate-on-curved-background).

## Discussion

**Open.** The conditional implication (modulo plate-mode-count
existence and scaling) is rigorous and is formalised in
`CasimirEpsilonVacuum.lean` as a §3b-cond conditional theorem with
two class hypotheses (`VacuumEpsilon` and a new
`PlateModeCount` class carrying the surreal-coefficient axiom).

The trace functional the plate-mode-count must carry is now
identified — the bare disjoint-component count, selected by
$n$-stability — and the $\pi^{2}/720$ prefactor follows from
$(\pi^{2}/6)\cdot|\zeta(-3)|$ with no substrate dependence. The
substrate-correction series is then trivial at leading order
($\xi_{0}=1$, $\xi_{k}=0$ for $k\ge 1$ on the $1/d^{4}$ term),
with q-corrections relocated to the $1/d^{6}$ (interacting-mode)
order. The selection argument itself is machine-verified in
`CasimirNStability.lean`: the bare count is the unique $n$-stable
mode-counting functional under the Hoefsmit single-mode
normalisation, the $n$-unlink Jones value fails $n$-stability for
every $q > 0$, $q \neq 1$, and the normalised trace is
content-free. The prefactor's arithmetic core is likewise
machine-verified in `CasimirZetaPrefactor.lean`: $\zeta(-3) = 1/120$
(from Mathlib's negative-integer Bernoulli formula, with
$B'_4 = -1/30$) and $(\pi^{2}/6)\cdot(1/120) = \pi^{2}/720$; the
value $1/120$ is recovered regulator-independently from a physical
exponential cutoff (the $S(\varepsilon) - 6/\varepsilon^{4} \to 1/120$
witness), via the *same* Bernoulli number $B_4$ — so the prefactor
is not an artefact of $\zeta$-continuation. The free-field $\leftrightarrow$ disjoint-unknot
identification this rests on is **not a fresh assumption**: QOU
already represents a free photon mode as the identity braid
([`rem:trivial-knot-photon-interpretation`](#rem:trivial-knot-photon-interpretation)),
whose Markov closure is disjoint unknots
([`prop:recursive-atom-knot-atlas`](#prop:recursive-atom-knot-atlas):
$\unicode{9737}$ photon $= \mathbf{1}_{B_4}$, closure $= 4\cdot 0_1$),
and degree-$\le 1$ closures are non-hyperbolic with $\mathrm{Vol}=0$
— carrying no substrate-$q$ deformation
([`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume)).
The leading-order $\xi_{k}=0$ thus reduces to cited QOU content;
the only physical input is that the Casimir vacuum tower is built
from free photon modes (standard physics). What remains is the
full Yekutieli-homotopy lift realising the explicit categorical
object. The selection argument, the prefactor derivation, and the
grounding in the photon representation are recorded in the
[N\_⊙-construction audit](../../../docs/audits/2026-05-31-casimir-n-unknot-construction.md)
and the [free-field/disjoint grounding audit](../../../docs/audits/2026-06-01-casimir-free-field-disjoint-grounding.md)
(see also the [ξ\_2 reconciliation](../../../docs/audits/2026-05-31-casimir-xi-2-reconciliation.md)).

## See also

- [`conj:vacuum-epsilon`](#conj:vacuum-epsilon) — upstream
  conjecture: $\mathrm{Geom}(\unicode{9737}) = \varepsilon$.
- [`conj:casimir-first-q-correction`](#conj:casimir-first-q-correction) —
  the interacting-sector sequel: the first substrate correction is
  carried by the figure-eight knot $4_1$.
- [`conj:archimedean-stpart`](#conj:archimedean-stpart) —
  standard-part arithmetic used in the conditional derivation.
- [`def:standard-part-functor`](#def:standard-part-functor) — the
  $\mathrm{st}$ map from finite surreals to $\mathbb{R}$.
- Terminology: the Casimir *effect* treated here shares only its
  eponym with the [$q$-Casimir element](#def:q-casimir) of
  $\mathcal{U}_q(\mathfrak{su}(2))$, the central invariant encoding
  $q$-angular momentum.
- [`conj:bohr-radius-categorical`](#conj:bohr-radius-categorical) —
  precedent for the "scaling correct, prefactor open" status
  pattern.
- Observational test target:
  [`observations/entropic-gravity-data`](../observations/entropic-gravity-data.md)
  lists Casimir-force precision measurements as a vacuum-energy
  probe; this block makes the QOU-side prediction explicit.
- Casimir 1948 (original derivation); Mohideen–Roy 1998 and
  Lamoreaux 1997 (experimental verification).
<!-- FILE_END: casimir-epsilon-vacuum.md -->

<!-- FILE_START: casimir-first-q-correction.md -->
**Conjecture (first substrate correction to the Casimir force is
carried by $4_1$).**
*Assume the plate-constrained mode-count of
[`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum), whose
leading $1/d^{4}$ term is built from disjoint free-photon modes (the
bare photon being the identity $\mathbf{1}$, $q$-independent) and is
therefore independent of the substrate deformation. The
first contribution carrying substrate-$q$ dependence arises from the
interacting sector — vacuum modes whose braid words have degree
$\geq 2$ and whose closures are hyperbolic — and its minimal carrier
is the figure-eight knot $4_1$, entering with relative weight equal
to its Markov trace*

$$
J_{4_1}(q) \;=\; q^{-2} - q^{-1} + 1 - q + q^{2}
\;=\; 1 \;+\; \tfrac{3}{4}\,h^{2} \;+\; O(h^{4}),
\qquad h = q - q^{-1}.
$$

## Absence of $q$ in the leading term

The leading parallel-plate term is assembled from free photon modes:
each is the identity braid, whose Markov closure is a disjoint union
of unknots, and degree-$\leq 1$ closures are non-hyperbolic with
vanishing volume
([`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume)).
A mode that does not braid transmits no substrate deformation, so the
$\zeta(-3)$ prefactor $\pi^{2}/720$ of the parent conjecture is
undeformed. Substrate corrections can therefore enter only where
modes braid — the interacting sector.

## Torus closures contribute nothing

Degree $\geq 2$ is necessary for hyperbolicity but not sufficient.
The minimal degree-$\geq 2$ closures — the Hopf link
($\sigma_1^{2}$), the trefoil $3_1$ ($\sigma_1^{3}$), and the
$(2,5)$-torus knot $5_1$ ($\sigma_1^{5}$) — are torus links with
$\mathrm{Vol} = 0$, hence carry no substrate weight. The first
hyperbolic closure is the figure-eight knot $4_1$
($\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$), the unique
minimal-volume hyperbolic knot, with
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.0299$.

## The $3/4$ is exact algebra

With $h = q - q^{-1}$, the figure-eight weight satisfies the exact
field identity

$$
J_{4_1}(q) \;=\; 1 + \tfrac{3}{4}\,h^{2}
\;+\; \frac{h^{4}}{4\left(h^{2} + 8 + 4(q + q^{-1})\right)},
$$

with the remainder denominator strictly positive for $q > 0$. The
coefficient $3/4$ is forced by the identity — there is no fitted
constant. The expansion is proved sorry-free in
`FigureEightCasimirWeight.lean` (`jones41_taylor`,
`jones41_three_quarters_cleared`, `jones41_remainder_denom_pos`).
At the substrate anchor the relative weight $\tfrac{3}{4}h^{2}$
evaluates to $\approx 3\%$.

## Self-consistency with the substrate

$4_1$ is not an arbitrary carrier: the substrate parameter $q_0$ is
itself fixed through $\mathrm{Vol}(4_1)$ (the $m_p/m_e$ pin). The
knot that defines the framework's one calibrated deformation
parameter is also the carrier of the vacuum's first substrate
correction — the correction introduces no independent scale.

## Open conjecture

Two items, both requiring the interacting-mode mode-sum — the
Yekutieli-homotopy lift of the parent conjecture's mode-count
restricted to degree-$\geq 2$ closures:

1. **The power of $1/d$.** The radiative-correction analogy
   suggests $1/d^{6}$; this is an expectation, not a derivation.
2. **The absolute magnitude.** The relative weight
   $1 + \tfrac{3}{4}h^{2}$ multiplies an interacting-sector
   amplitude suppressed by $\sim \alpha\,\lambda_C/d$, far below
   the precision of current Casimir-force measurements (see the
   falsification note of the parent block); the conjecture is a
   structural prediction target, not a near-term experimental
   discriminator.

## Falsification path

Construct the interacting-mode mode-sum and extract the sector
coefficients. If the first non-vanishing substrate correction is
*not* weighted by $J_{4_1}$ — for example, if a torus-sector
contribution survives with nonzero weight, or a different
hyperbolic closure dominates — the conjecture is refuted.
## See also

- [`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum) —
  parent conjecture: the leading $1/d^{4}$ term and the
  $\varepsilon$-vacuum mechanism.
- [`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume) —
  degree-$\leq 1$ closures carry no volume, hence no substrate
  weight.
- [`conj:vacuum-epsilon`](#conj:vacuum-epsilon) — the
  $\varepsilon$-relaxed vacuum axiom upstream of both Casimir
  blocks.
<!-- FILE_END: casimir-first-q-correction.md -->

