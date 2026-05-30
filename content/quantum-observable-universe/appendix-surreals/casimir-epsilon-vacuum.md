**Conjecture (Casimir force as standard-part of $\varepsilon$-vacuum
density gradient).**
*Assume the [$\varepsilon$-relaxed vacuum axiom](#prop:vacuum-epsilon) —
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
$\mathbf{No}$; see [`prop:archimedean-stpart`](#prop:archimedean-stpart)).
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
\;=\; -\,\frac{\pi^{2}}{720}\,\frac{A}{d^{3}}\,\hbar c \cdot \varepsilon^{-1}
\;+\; \bigl(\text{lower-birthday corrections}\bigr).
$$

Multiplying by $\varepsilon$ and applying $\partial/\partial d$
recovers the textbook Casimir force per unit area exactly (see the
conditional derivation below).

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
   [`prop:vacuum-epsilon`](#prop:vacuum-epsilon).
2. A plate-constrained unknot-density function satisfying
   $$
     N_{\unicode{9737}}^{\text{in}}(A, d) - N_{\unicode{9737}}^{\text{out}}(A, d)
     \;=\; -\,\frac{\pi^{2}}{720}\,\frac{A}{d^{3}}\,\hbar c \cdot \varepsilon^{-1}
     \;+\; o(\varepsilon^{-1}).
   $$
3. Standard-part arithmetic
   [`prop:archimedean-stpart`](#prop:archimedean-stpart) and the
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
[`prop:archimedean-stpart`](#prop:archimedean-stpart). The
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
   plate-bounded ambient isotopy — but no such construction has
   been written. *Tractability: medium.* The plate boundary is a
   conformal boundary condition on $\mathbb{R}^{3}$, which the
   substrate-conformal structure of QOU already accommodates.

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
   regularisation. The QOU analogue would be a Hecke-trace
   identity on a specific subalgebra. Conjecturally derivable
   from the Markov-trace structure on $H_{n}(q)$ at the plate-
   boundary representation, but not proved. *Tractability: hard.*
   This is the same kind of prefactor obstruction that appears
   in [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical)
   round-4 (option 4a — symbolic-$q$ recompute).

## Falsification path

If a categorical plate-constrained mode-count is constructed and
its surreal coefficient *does not* match
$-\pi^{2} A/(720\, d^{3}\, \varepsilon)$, the conjecture is
refuted.

The standard-physics value of $\pi^{2}/240$ (Casimir 1948) is
verified experimentally to $\sim 1\%$ (Mohideen–Roy 1998,
Lamoreaux 1997), so the QOU prediction is unambiguous.

A *weaker* partial test: if the $1/d^{4}$ scaling is recovered
but the prefactor differs, the conjecture is refined rather than
killed — analogous to the "Round-8" partial results in
[`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical),
where shell-spacing ratios match but the absolute scale is
transported.

## Why this matters

Three reasons:

1. **Quantitative test of the $\varepsilon$-vacuum axiom.** The
   Casimir effect is the cleanest experimental probe of
   vacuum-energy structure. If QOU's $\varepsilon$-vacuum
   reproduces it, [`prop:vacuum-epsilon`](#prop:vacuum-epsilon)
   gains empirical traction. If not, the relaxation is wrong.

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

## Status

**Open.** The conditional implication (modulo plate-mode-count
existence and scaling) is rigorous and is formalised in
`CasimirEpsilonVacuum.lean` as a §3b-cond conditional theorem with
two class hypotheses (`VacuumEpsilon` and a new
`PlateModeCount` class carrying the surreal-coefficient axiom).
The plate-mode-count construction itself is not started; the
numerical prefactor is a separate open sub-problem.

## See also

- [`prop:vacuum-epsilon`](#prop:vacuum-epsilon) — upstream
  conjecture: $\mathrm{Geom}(\unicode{9737}) = \varepsilon$.
- [`prop:archimedean-stpart`](#prop:archimedean-stpart) —
  standard-part arithmetic used in the conditional derivation.
- [`def:standard-part-functor`](#def:standard-part-functor) — the
  $\mathrm{st}$ map from finite surreals to $\mathbb{R}$.
- [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical) —
  precedent for the "scaling correct, prefactor open" status
  pattern.
- Observational test target:
  [`observations/entropic-gravity-data`](../observations/entropic-gravity-data.md)
  lists Casimir-force precision measurements as a vacuum-energy
  probe; this block makes the QOU-side prediction explicit.
- Casimir 1948 (original derivation); Mohideen–Roy 1998 and
  Lamoreaux 1997 (experimental verification).
