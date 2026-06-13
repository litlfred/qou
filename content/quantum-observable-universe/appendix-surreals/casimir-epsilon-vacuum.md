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

## Why $\mathrm{st}$ does not annihilate

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
[Hoefsmit-additivity probe](../../../folio-assistant/computations/probes/casimir-hoefsmit-additivity-probe.witness.json)).
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

## What is open (the actual conjecture)

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

## Why this matters

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
