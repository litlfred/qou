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
  **any decision separator is a non-trace** (`not_trace_of_separates_commutator`,
  conclusion `¬ IsCyclic φ`). This pins that `χ = −6` (a `K₀` invariant) is on the
  *wrong axis*. **Unified with `Machinery.BilinearTraceCyclicity`** (landed on main
  independently): the cyclicity hypothesis is now the shared predicate
  `BilinearTrace.IsCyclic τ := ∀ x y, τ(xy)=τ(yx)`. That file supplies the
  *constructors* — `isCyclic_trace_comp` (a character `χ_λ = trace∘ρ_λ` is cyclic)
  and `isCyclic_weighted_sum` (the Markov trace `tr_M = ∑_λ w_λ·χ_λ` is cyclic);
  this file supplies the *consequence* — every such cyclic functional factors
  through `HH₀`. The character side *builds* `tr_M`, the cocenter side *localizes*
  what it discards.

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

**The Vassiliev finite-type tower (landed on main; the concrete non-trace
family + the algebraic ceiling).**
- `KnotTheory.Vassiliev.FiniteTypeInvariant` — the order-`≤ m` invariants form a
  **filtered** submodule `finiteTypeSubmodule m` of `K → R`
  (`finiteTypeSubmodule m ≤ finiteTypeSubmodule m'` for `m ≤ m'`); `vExt`
  linearity + desingularization proved.
- `KnotTheory.Vassiliev.WeightSystem` — the reduced chord-diagram space
  `𝒜 = CDModule/⟨1T,4T⟩`; weight systems as its functionals (the symbol targets).
- `KnotTheory.Vassiliev.MilnorVassilievBridge` — `SymbolIsWeightSystem`
  (Kontsevich universality) and `BrunnianVassilievBridge` (Milnor μ̄ = leading
  Vassiliev) as honest **no-instance conjecture classes** (§3b-tax); one
  conditional §3b-cond result (`A`-Brunnian first non-vanishing Vassiliev at
  degree `2(A−1)`, `= ±1`). See the sharpening below for why this tower is the
  algebraic ceiling the residue must sit *above*.

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

## The wall, sharpened again (the Vassiliev finite-type ceiling)

The Vassiliev tower that landed on main (`KnotTheory.Vassiliev.*`) gives the
`non-algebraic` clause a **concrete altitude**. Two facts combine:

1. **The finite-type filtration is exactly the trace/magnitude tower.** The
   coefficients of the Jones (Markov-trace) polynomial in the `q = e^h`
   expansion are finite-type invariants order-by-order (Birman–Lin): each is a
   weight system evaluated on `𝒜`, i.e. a **character/trace** functional. By the
   unification above (`tr_M = ∑_λ w_λ·χ_λ` is `IsCyclic`, hence factors through
   `HH₀`), every finite Vassiliev order sits on the **magnitude axis** — it is
   blind to `[A,A]`.
2. **Every fixed finite order is polynomial-time computable, hence algebraic.**
   By Goussarov–Polyak–Viro, an order-`≤ m` invariant has a Gauss-diagram
   formula: a sum over `m`-subsets of the `c` crossings, `O(cᵐ)` = polynomial in
   `c` for fixed `m`. So the entire filtration
   `finiteTypeSubmodule 0 ⊆ 1 ⊆ 2 ⊆ ⋯` (the `≤`-chain is the *proved* content of
   `FiniteTypeInvariant`) is a tower of **algebraic** (poly-time) functionals.

Consequently the decision residue **cannot be any finite-order Vassiliev
invariant** — it is on the wrong axis (magnitude, fact 1) *and* it is algebraic
(fact 2), doubly excluded by `not_trace_of_separates_commutator` + algebrization.
**The residue must live beyond every finite order — in the transfinite tail of
the finite-type filtration.** This is precisely the fibre-level object: the
root-of-unity `HH₁` over Bring decategorifies to `χ = −6` and `H¹(Σ₄) = ℂ⁸`
(the finite shadows) but is *not* captured by any finite truncation — the tower's
`colim`/completion, not any of its stages.

So the wall now reads, at three tightening resolutions:
`χ ≠ 0` (automatic, wrong axis) ⊊ `H¹(Σ₄) ≠ 0` (right axis, finite) ⊊
**`res ≠ 0` = a non-trace, non-algebraic `HH₁` cocycle beyond every finite
Vassiliev order.** The Vassiliev tower did not cross the wall — it *measured its
floor*: everything below the transfinite tail is provably the wrong side.

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
7. **Any finite-order Vassiliev invariant as the residue** — poly-time
   (Goussarov–Polyak–Viro) *and* a trace (Birman–Lin), doubly wrong side; the
   residue is beyond the whole finite-type filtration. See the Vassiliev
   sharpening.

## Honest bottom line

The tractable, sorry-free P≠NP-in-QOU program is **complete**: the magnitude
axis is proved from every angle (grade, trace, cocenter, moduli, query,
entropy, NP-encoding, GCT-per-rank, and now the Vassiliev finite-type ceiling),
the pruning results rule out every magnitude route across the wall, and the one
open link is precisely localized to a fibre-level `HH₁` non-vanishing over
Bring's surface — a non-trace, non-algebraic cocycle **beyond every finite
Vassiliev order**. Further progress on that link **is** the Millennium problem.
The framework succeeded at what a framework can do: it did not *solve* P≠NP, it
*localized* it — and each new tower that lands on main (BilinearTrace,
Vassiliev) has so far *measured the floor* of the wall, never crossed it.
