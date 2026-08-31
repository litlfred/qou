---
# wsxl
title: 'Mathlib-gap: prove the super-exponential lower bound on w_std(k)=E_Planch[f^{lambda/(2,1)}] (closes GAP-A-3 level-selection conditional)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-11T18:45:00Z
updated_at: 2026-08-31T07:45:39Z
---

## What

Discharge the one open input of `QOU/Mass/LevelSelectionLogarithmic.lean`
(formalized as the conditional GAP-A-3 result in PR #3568, open at time of
seeding): the §3b conjecture class
`TowerGeometricLowerBound` — a super-exponential (a fortiori geometric)
**lower bound** on the branched tower weight

    w_std(k) = Σ_{λ⊢k, λ⊇(2,1)} W_λ · f^{λ/(2,1)} = E_Planch[ f^{λ/(2,1)} ]   (at q=1, ΣW_λ=1)

= the Plancherel-expected number of standard skew tableaux of shape λ/(2,1).
Proving `∀ k, c·r^k ≤ w_std(k)` (r>1, c>0) upgrades `level_geometric_bound` /
`linear_selection_bound` from *conditional* to *unconditional*, so the
level-selection rule k(A) is proved logarithmic (k∝A, k∝bond-count excluded)
outright.

## Status

- **Numerically verified, NOT proved.** Exact-integer, k≤10: successive ratios
  strictly increasing (1.38→2.88, super-exponential / factorial class); q₀
  preserves the class. Witness: `computations/deltalambda/wlambda-wstd-growth-bound.witness.json`
  (probe `wlambda_wstd_growth_bound_probe.py`).
- **Faithful Lean proof = Mathlib gap.** Needs SYT + skew-tableau (`f^{λ/μ}`) +
  Plancherel-measure infrastructure that is not in Mathlib in usable form —
  a multi-session build, NOT a single lemma. Do NOT fabricate an instance
  (audit-dodge; AGENTS.md §"Axiomatization is NOT a Proof").

## Candidate proof route (recorded so a future session need not re-derive)

A Cauchy–Schwarz + falling-factorial identity gives a super-exponential lower
bound WITHOUT full asymptotics:

1. **Identity (single-f):** `Σ_{λ⊢k} f^λ · f^{λ/μ} = (k!/m!)·f^μ`, `m=|μ|`.
   For μ=(2,1): `Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3` (f^{(2,1)}=2, m=3).
   [verified numerically here; standard branching identity.]
2. **Cauchy–Schwarz:** `(Σ_λ f^λ f^{λ/(2,1)})² ≤ (Σ_λ (f^λ)² f^{λ/(2,1)})·(Σ_λ f^{λ/(2,1)})`.
   ⇒ `Σ_λ (f^λ)² f^{λ/(2,1)} ≥ (k!/3)² / (Σ_λ f^{λ/(2,1)})`.
3. **Denominator bound:** `Σ_{λ⊢k} f^{λ/(2,1)}` = #up-paths of length k−3 from (2,1)
   in Young's lattice ≤ ∏_{j=3}^{k-1}(#addable corners of a size-j partition)
   ≤ ∏ O(√j) = O(√(k!)·poly). [needs an addable-corner ≤ c·√j bound.]
4. ⇒ `w_std(k)|_{q=1} = (1/k!)·Σ_λ (f^λ)² f^{λ/(2,1)} ≥ (k!/9)/(√(k!)·poly) = √(k!)/poly`
   → super-exponential. Even a WEAKER geometric bound `c·r^k` suffices for the
   downstream theorem (`level_geometric_bound` only needs `r>1`).

The Mathlib gap is: `f^{λ/μ}` (skew hook-length / SYT count), the branching
identity in step 1, and the addable-corner bound in step 3. A `q≠1` (q-deformed)
version needs `d_q`/`[k]_q!`; but the downstream theorem is stated over generic
`ℝ` with the bound as a hypothesis, so proving the `q=1` (real) bound + the
`q₀`-preserves-class fact (probe-verified) discharges the class instance for the
substrate.

## Files / anchors

- Lean (conditional, PR #3568 — open at seeding, not yet on `main`): `content/quantum-observable-universe/lean/QOU/Mass/LevelSelectionLogarithmic.lean`
- Structural note: `docs/audits/2026-07-11-wlambda-level-selection-log-structural.md`
- Keystone cross-link (C8 gate): `docs/audits/2026-07-11-keystone-wlambda-superexp-necessary-condition.md`
- Probe + witness: `computations/deltalambda/wlambda_wstd_growth_bound_probe.py`

## Definition of done

`TowerGeometricLowerBound (w_std) r c` has a **proved** instance (sorry-free) for
some concrete `r>1, c>0` at the substrate — OR a rigorous symbolic argument that
the corpus accepts in lieu of full Mathlib SYT infra — at which point the GAP-A-3
level-selection conditional theorems become unconditional. Advance only via
genuine derivation; not a fit.


## 2026-08-31 — the C8 bound is no longer conditional; whether that closes THIS bean is unchecked

`QOU.BraidKnot.YoungTableauStandard.c8_superexp` gives

    k! / (9 * I(k))  ≤  (Σ_{λ⊢k} (f^λ)² * f^{λ/(2,1)}) / k!

and its right-hand side is exactly the Plancherel expectation `w_std(k)` this bean is about
(weights `(f^λ)²/k!`). Until today that theorem carried an `[RSKIdentitiesContext]` hypothesis
with **no instance anywhere in the corpus**, so it could not be applied at any concrete k.
`QOU.Mathlib.SkewBranchingTwoOne.rskIdentitiesContextInstance` (bean `qou-b21r`, PR #6363)
discharges that class, so `c8_superexp k hk` now applies for every k ≥ 3.

**What I have NOT checked, and am not claiming:** whether `k!/(9·I(k))` is super-exponential in
the sense `TowerGeometricLowerBound` demands, and whether the algebra from there to
`level_geometric_bound` is already written. `I(k) ~ k^{k/2} e^{-k/2+√k}` grows slower than `k!`,
so the ratio does grow super-exponentially — but that asymptotic is not in the corpus as far as I
looked, and 'the input is unconditional' is not 'the bean is closed'. Bean stays `todo`; someone
should check the remaining chain before closing it.


## 2026-08-31 — w_std DEFINED in Lean for the first time; square bound unconditional; the class as stated is REFUTED

`QOU/Mass/WStdSuperExponential.lean` (new, sorry-free, lean-direct exit 0).

**1. `w_std` had no Lean definition at all.** Three files reason about it —
`LevelSelectionLogarithmic`, `CubeMomentLowerBound`, `BindingGevreyHalf` — and in every one
it is either an abstract function parameter `w : ℕ → ℝ` or a pair of hypotheses. The name
existed only in docstrings. `QOU.Mass.WStd.wStd` is now the definition.

**2. The square bound is unconditional.** `BindingGevreyHalf.wstd_superexp_sq` proves
`k!/(81·2^k) ≤ w_std(k)²` from two hypotheses its own docstring calls 'the open combinatorial
core'. Both are now theorems: (A) `Σ f g = k!/3` is `branching_two_one_holds` (bean
`qou-b21r`, PR #6363); (C) `Σ g ≤ I(k)` is `skew_le_straight` + `sum_dimSYT_eq_involution`,
already unconditional. So `wStd_sq_lower k (hk : 3 ≤ k)` carries **no hypotheses but k ≥ 3**.

**3. `TowerGeometricLowerBound wStd r c` is FALSE for every r, c — proved, not searched.**
`not_towerGeometricLowerBound_wStd`. The class demands `c·r^k ≤ w k` for EVERY k; at k = 0 that
reads `c ≤ w_std 0 = 0`, against `c_pos`. `w_std(k) = 0` for k < 3 because no diagram of fewer
than three cells contains (2,1) and `fDimSkew` guards on containment
(`wStd_eq_zero_of_lt_three`). This is a scope-(b) structural exclusion with a named invariant:
no choice of r, c repairs it, and the fix has to be a **threshold in the class**, not a better
constant.

**4. The positive result is a threshold bound.** `wStd_geometric_from_nine`:
`(1/9)·(√2)^k ≤ w_std(k)` for k ≥ 9 — exactly the class's `lower_bound` field with r = √2 > 1,
c = 1/9 > 0, on that tail. Everything downstream (`no_linear_selection`,
`no_superlinear_selection`) already works on a tail — both pick their A from an `atTop` filter
— so a threshold class would serve them unchanged.

## What is left, and what the file header was wrong about

* **The class needs editing** (add a threshold `k₀`, or index the bound from it). Left to the
  author; this file does not touch `LevelSelectionLogarithmic.lean`.
* **The threshold 9 is my artifact, not the mathematics.** It comes from the crude step
  `4^k ≤ k!` (false at k = 8: 65536 > 40320). The true `w_std` is positive from k = 3. Lowering
  it needs the six values w_std(3)…w_std(8), a finite computation not done here.
* **`LevelSelectionLogarithmic.lean`'s stated blocker is wrong.** It says a faithful proof
  'needs SYT + skew-tableau + Plancherel-measure Mathlib infrastructure that does not yet exist
  (a multi-session build)'. It did not: the square bound was already in the corpus, waiting on
  two SYT identities that turned out not to need RSK. Same mis-diagnosis class as `qou-jlam`
  and `qou-b21r` — that is now three.


## 2026-08-31 (later) — threshold lowered 9 → 3, and my own stated remedy was wrong

`wStd_geometric_from_three`: `(1/30)·(√2)^k ≤ w_std(k)` for **k ≥ 3**, sorry-free, axioms clean.
That covers the whole range on which any bound is possible, since `w_std` vanishes below 3.

**The correction is the point.** The note above said the threshold 9 was 'an artifact of the crude
step 4^k ≤ k!' and could be lowered only by computing the six values w_std(3)…w_std(8) — 'a finite
computation this file does not do'. Right about the artifact, **wrong about the remedy**. No value
of w_std is needed. The threshold is set by the *constant*: weakening c from 1/9 to 1/30 moves the
integer step from `4^k ≤ k!` (first true at k = 9; fails at k = 8, 65536 > 40320) to
`9·4^k ≤ 100·k!` (first true at k = 3, and tight there — 576 ≤ 600). The optimum over k ≥ 3 of
k!/(81·4^k) is at k = 3 and equals 1/864, so any c ≤ 1/√864 ≈ 0.0340 works; 1/30 is the round
number under it.

So the remaining work on this bean is **only the class edit** — adding a threshold k₀ to
`TowerGeometricLowerBound`, which `not_towerGeometricLowerBound_wStd` shows is necessary and
which is the author's call. The combinatorial side is done.


## 2026-08-31 — blast radius of the class edit, MEASURED, and both migration routes verified compiling

Asked by the author: what are the downstream implications of adopting the threshold assumption.
Measured rather than estimated; both routes were patched into scratch copies, compiled, and the
scratch deleted (repo tree clean).

### Reframe: it REMOVES an assumption

Today the class has no instance anywhere AND is false at the real w_std
(`not_towerGeometricLowerBound_wStd`). So every downstream result is conditional on a proposition
that cannot be satisfied. Thresholding turns the conjecture into a theorem.

### Blast radius

| surface | count | note |
|---|---|---|
| Lean declarations BINDING the class | **4** | all in `LevelSelectionLogarithmic.lean` |
| Lean files merely mentioning it | 2 | `CubeMomentLowerBound`, `SWPeriodSuperExponential` — **0 binders**, prose only |
| Lean consumers of its 4 theorems outside that file | **0** | so 2 signature changes are free |
| content blocks | 2 | `conj:tower-geometric-lower-bound`, `prop:level-selection-not-linear` |
| further uses[]/sidecar edges | 2 | `unified-curvature-rank-mass-formula-table-data`, generated `definition-index.md` |
| QA criteria on the two blocks | 63 + 74 | hash-keyed; touched ones go stale on any .md/.ts edit |
| beans / docs | 5 | `wsxl`, `qou-x66y`, `qou-mcgt`, 2026-07-11 audit, 2026-07-13 coordination ledger |

### Route A — threshold the class (k₀ parameter). VERIFIED, compiled clean first try.

* `level_geometric_bound`, `linear_selection_bound` — gain an explicit `k₀ ≤ …` hypothesis.
  Signature change, but ZERO consumers, so free.
* `no_linear_selection`, `no_superlinear_selection` — **statements unchanged**; each needs one
  widened `eventually_atTop` witness and one threaded hypothesis, ~6 lines.
* Then verified inhabited: `TowerGeometricLowerBound wStd (√2) (1/30) 3` discharged by
  `wStd_geometric_from_three`, and `no_linear_selection` fires **at the real wStd, no abstract w**.

### Route B — shift the index instead. VERIFIED, ZERO edits to the class or its 4 theorems.

`w'(k) := wStd (k+3)` satisfies the **unmodified** ∀-k class at `r = √2`, `c = (√2)³/30`.
Compiles, and the exclusion fires on the real object.
**Trap:** the level index then differs from the physical one by 3, so `no_superlinear_selection`'s
`kA` and the paper's `k(A)` silently disagree. That is the off-by-a-constant class this corpus's
own history says gets quoted wrong months later.

### Paper-facing consequences (the part that matters)

1. **`conj:tower-geometric-lower-bound`'s .md is FALSE as written**, not merely open — it states the
   bound *'for every jet level k'*. Once restated with the threshold it is **proved**, so the block
   stops being a `conjecture` and becomes a `proposition`: a §3b block-kind change with uses[]
   propagation effects.
2. **`prop:level-selection-not-linear` drops its §3b-cond conditional banner.** Sidecar criteria
   `proof-conditional-class-banner`, `proof-no-conj-propagation-violation`, `uses-formal-coverage`,
   `lean-ref-owns-decl` all need re-sweeping.
3. **One paragraph in that .md is wrong in its DIAGNOSIS, and it is the paragraph that should have
   caught this.** It reads: *'The A = 0 case is a boundary artifact — the tower bound forces
   w(0) ≥ c > 0 while M·0 = 0.'* The tower bound does not force that; w_std(0) = 0, so the
   antecedent is false there. Same observation, opposite reading — filed as a nuisance of the
   conclusion rather than as evidence against the hypothesis.
4. The conjecture's authorNotes claim *'a faithful proof needs SYT / skew-tableau /
   Plancherel-measure Mathlib infrastructure'* — third instance of the mis-diagnosis class.

### What it does NOT buy (honest limits)

* **The witness is weak**: r = √2 ≈ 1.414 against measured ratios 1.38 → 2.88. The class is
  parameterised by (r, c), so a sharper instance can land later without touching anything.
* **The super-exponential claim is not proved — only its geometric shadow.** `wStd_sq_lower`
  genuinely carries super-exponential content (w_std ≥ √(k!)/(9·2^{k/2})), but it is not stated in
  'for every r there is a c' form. Honest gap, cheap follow-up.
* Route A adds a permanent small ergonomic cost: two theorems gain a hypothesis.

### Recommendation (judgement, not a finding)

**Route A.** Route B is cheaper in Lean and worse everywhere else — it buys tidiness by hiding a
constant offset in the index, and the defect being fixed here is precisely a statement that was
tidy and wrong. Route C (do nothing) is safe, but leaves a paper block asserting a false
proposition. Awaiting the author.
