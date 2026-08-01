# P≠NP-in-QOU: the two-axis map and the wall inventory

**Date:** 2026-08-01 · **Scope:** consolidates the P≠NP-in-QOU formalization
(the `qou-f9wl` epic and its offshoots) into one map — what is *proved*, what is
*ruled out*, and the single precisely-stated *open* link. Read this before
re-attacking any P≠NP route: several plausible-looking routes are already
proved dead here.

## The one-paragraph summary

The QOU **localizes** P≠NP to a specific, named object. Every *magnitude /
counting* statement is proved sorry-free; the framework proves that **no
trace-, birthday-, Euler-characteristic-, or `K₀`-invariant can cross to the
decision axis**; and the single open link `res ≠ 0 ⟹ P≠NP` is reduced to:
*the fibre-level (root-of-unity) `HH₁` cocycle over Bring's surface is nonzero
and non-algebraic.* That last clause **is** the Millennium problem (it must
clear the algebrization barrier), and it stays open. The value of the program is
the *localization*, not a proof.

## The two axes

Every decision problem sits in a plane with two independent coordinates:

| Axis | Measures | Proved home | Verdict |
|---|---|---|---|
| **Magnitude** | size of the solution set — count, ω-grade, surreal *birthday*, Euler char `χ`, `K₀`, any **trace** | the cocenter `HH₀ = A/[A,A]` | everything here is **proved**; it **cannot** cross the wall |
| **Quantifier / decision** | logical form — `∃`/`∀` alternation depth (PH), *which* witnesses accept | the commutator subspace `[A,A]` = `ker(every trace)`; `HH₁` | the one **open** link lives here |

`#P`-hardness is invariant under P vs NP (Toda), so magnitude facts hold in
*both* worlds and can never separate them. That invariance is the wall.

## Inventory of the formalization (all sorry-free unless noted)

**Grade / bound-management (magnitude, proved).**
- `Information.PhysicalIntractability` — the bandwidth (Bekenstein) lower bound;
  `SuperPolynomial` (fixed 2026-08-01: an `n = 0` escape made `(n+1)²`
  spuriously super-poly; witness now guarded `n ≥ 1`).
- `Information.SurrealBudgetGrade` — the ω-grade cost/budget squeeze
  (`SuperPolynomial = ord_ω(cost) > ord_ω(budget)`).
- `Information.PolyGrowthAlgebra` — the budget grade as a closed algebra
  (`+`, `×`, domination); `not_superPolynomial_of_polyGrowth` (the reverse
  squeeze on the constant-safe class).

**Magnitude/decision boundary (why magnitude can't cross).**
- `Information.MagnitudeAxisBoundary` — `census_blind_to_decision`: a genuinely
  different decision pair on which every census-/birthday-factoring functional
  agrees.
- `Information.MagnitudeTraceCommutator` — `[Q,M]` as an operator lemma:
  `tr_M` kills commutators; `trace_comp_conjOp` (`M∘Q = M`). This *is* why the
  Jones polynomial is a knot invariant (Markov move I).
- `Information.CocenterTraceFactor` — the trace factors through `HH₀ = A/[A,A]`
  (`traceCocenter`); a trace is **blind to `[A,A]`** (`trace_eq_of_sub_mem_commutator`);
  **any decision separator is a non-trace** (`not_trace_of_separates_commutator`).
  This pins that `χ = −6` (a `K₀` invariant) is on the *wrong axis*.

**#P over the problem space (moduli).**
- `Information.CountingModuliGrade` — `#P` as an ω-graded section over the
  problem moduli; counting axis proved unconditional (`physical_point_hard`);
  decision axis = `PhotonicDecisionHard` (no-instance conditional class).
- `Information.PNeqNpWallUnification` — one super-poly-cost lemma subsuming the
  bridge-horizon (`3^n`) and moduli (`physicalCost = 3^{3n}`) separations.

**The three-wall Skein bridge (q-Collatz / q-NS / P-vs-NP unification).**
- `Information.SkeinObservationBridge` — the three problems as one `len`-filtered
  orbit read through `obs = tr_M`; `regular_and_halts_of_len_orbit_descent`
  (one descent closes q-Collatz + q-NS; P-vs-NP adds the poly rate).
- `Information.SkeinGradeConnective`, `SkeinShadowConjInvariance` — wire the
  grade + the lossy-trace-shadow into the bridge.
- `Information.SkeinHorizonLowerBound`, `SkeinInfoLowerBound`, `SkeinNPEncoding`
  — the query-model / entropy-floor / NP-encoding counting lower bounds
  (`cwdx` #6 and `l525` #5 are **covered here** — do not duplicate).

**GCT.**
- `Information.GCTMultiplicityObstruction` (scaffold, no-instance class),
  `GCTSchurMultiplicity` (a proved TL Schur-element multiplicity drop),
  `GCTPerRankObstruction` (the drop at every rank). All **regime** separations,
  **not** `QouGCTObstruction` (`VP`-vs-`VNP`) instances.

**q-Collatz `D∞` (Mathlib-gap + bracketing).**
- `MathlibExt.LaurentTwoValuation` — the `[2]_q`-adic valuation on `ℤ[q^{±1}]`
  (Mathlib-gap fill; cycle values `v(q⁻¹)=0`, `v(1+q⁻¹)=1`).
- `AppendixSurreals.collatz_vtwo_domain_rescope` — the `v_[2]`-increase witness
  **escapes `D∞`** (out-of-cone).
- `AppendixSurreals.collatz_vtwo_cycle_descent` — `v_[2]` **descends** on the
  fundamental cycle. Together: `v_[2]` is a live `D∞` descent candidate on every
  `D∞` element checked. Not a closure.

## The wall map

```
quantifier / decision axis  (PH depth, [A,A], HH₁)
        ▲
   NP ──┤   ● res ≠ 0 ⟹ P≠NP        ← THE WALL (open; fibre HH₁, non-algebraic)
        │   ⋮  (no magnitude/trace invariant reaches up here)
    P ──┤   ● 3^{3n} counting cost    ← PROVED (physical_point_hard, unconditional)
        └───────────────────────────────────▶  magnitude axis (count / χ / K₀ / trace)
```

Both points sit at the same large magnitude coordinate; the counting one is
proved; the arrow up is P≠NP.

## The wall, precisely stated (the `χ = −6` sharpening)

For a QOU, the axioms fix the Bring fibre `Σ₄`, so
`χ(Σ₄) = b₀ − b₁ + b₂ = 1 − 8 + 1 = −6`. But:

- `χ = −6` is the **alternating sum** = a `K₀`/Hattori–Stallings **trace**;
  by `CocenterTraceFactor` it factors through `HH₀` and is **blind to `[A,A]`**.
  So `χ ≠ 0`, however axiom-fixed, is **never** the decision residue.
- The decision content is the term `χ` folds away: `b₁ = 2g = 8` = `H¹(Σ₄)`,
  Hodge piece `HH₁ = H¹(𝒪) = ℂ⁴` (the `S₅` standard rep). Right axis, but
  **finite** — 4–8 numbers cannot separate exponentially many braid classes.
- At generic `q` (the observable substrate) `HH₁(H_n(q)) = 0` (semisimple), so
  the residue can be nonzero only at the **root-of-unity / fibre level**, whose
  `HH₁` is the infinite object decategorifying to both `χ = −6` and
  `H¹(Σ₄) = ℂ⁸`.

**Therefore `res ≠ 0` is: the fibre-level `HH₁` cocycle over Bring is nonzero
and non-algebraic.** Not "`χ ≠ 0`" (automatic, wrong axis), not "`H¹(Σ₄) ≠ 0`"
(true but finite). This is a sharper statement of the wall than the framework
had, and it is exactly what `not_trace_of_separates_commutator` forces (the
residue is a non-trace) plus the algebrization barrier (it must be
non-algebraic).

## Ruled out — do not re-attack these

1. **`χ(A) ≠ 0` as the residue** — wrong axis (`K₀`/trace, blind to `[A,A]`).
2. **Birthday / census / ω-grade / any trace crossing** — `census_blind_to_decision`,
   `trace_comp_conjOp`, `trace_eq_of_sub_mem_commutator`.
3. **The categorical `decision_collapse` contradiction** — circular (smuggles
   the wall into an `h_resolve` hypothesis); "exp group growth ⟹ no poly
   decision" is false (braid word problem ∈ P). See
   [2026-08-01-categorical-pnp-contradiction-dialog-assessment.md](2026-08-01-categorical-pnp-contradiction-dialog-assessment.md).
4. **Global `v_[2]` descent** for q-Collatz — `= solving q-Collatz`.
5. **`cwdx` (#6) / `l525` (#5) as new work** — already formalized (Skein
   lower-bound files); duplication only.
6. **Fabricating a `QouPNeqNp` / `TraceFaithfulness` / `PhotonicDecisionHard`
   / `QouGCTObstruction` instance** — axiom laundering = claiming P≠NP.

## Honest bottom line

The tractable, sorry-free P≠NP-in-QOU program is **complete**: the magnitude
axis is proved from every angle (grade, trace, cocenter, moduli, query,
entropy, NP-encoding, GCT-per-rank), the pruning results rule out every
magnitude route across the wall, and the one open link is precisely localized to
a fibre-level `HH₁` non-vanishing over Bring's surface. Further progress on that
link **is** the Millennium problem. The framework succeeded at what a framework
can do: it did not *solve* P≠NP, it *localized* it.
