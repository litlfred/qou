# Workplan — Step 9b per-isotope binding: approach selection across the four sub-gaps

**Branch**: `claude/canonical-derivation-gaps-vuu01v`
**Date**: 2026-07-02
**Status**: survey in progress (this stub will be filled with the corpus-state
summary and the chosen approach per sub-gap).

## Scope

Step 9b of the canonical derivation chain
([cheat sheet §0](../canonical-derivation-cheat-sheet.md)) — the 🔴 open gate —
decomposed into four sub-gaps:

1. **q₀^(10A−5) residual** — trace-canonical `Δ_λ(K) ≈ q₀^(10A−5)`
   (D exact to 0.01 q₀-units, ³He off −1.40, Z-dependent). Task:
   derive-or-refute the exponent from W_free vs W_atom crossing/jet
   bookkeeping (formalize-first).
2. **Per-depth α_k assignment rule** — tower coefficients structural
   (z² Markov at k=2, m_e·8G plateau at k≥4) but the depth-assignment is
   empirical; tower undershoots D −73% … ⁴He −50%.
3. **Many-body series not closed** — pairwise bond-sum captures 26% of
   ⁴He; canonical link-volume assignment per nucleus, the ρ·A scale rule,
   and 2/3/4-body reconciliation all open.
4. **Brane-tower normalization** (PR #3016) — Borromean single pipeline
   converges ∀Z with the right shape, wrong normalization: the missing
   per-λ weight.

## Method

Per the formalize-first probe discipline ([AGENTS.md](../../AGENTS.md)): survey the corpus
first (three parallel sweep agents over audits/computations/coordination
ledgers), then for each sub-gap identify the structural invariant that
prunes the hypothesis class before running any probe. Findings and the
per-gap approach decision land here.

## Survey findings

### Gap 1 — q₀^(10A−5) residual: mostly SETTLED since the cheat-sheet framing

The cheat-sheet §0 row (and this workplan's scope item 1) lags the
2026-06-29 audit wave. Current state:

- **The global `10A−5` law is REFUTED at A ≥ 5** (scope-limited): ⁶Li
  measures `log_{q₀}Δ_λ = 36.1` vs predicted 55. `B_pred` saturates
  (~0.7 for all A) while `B_AME` grows linearly, so the exponent is
  logarithmic in A, not linear
  ([z-correction audit §slope](../audits/2026-06-29-delta-lambda-z-correction-writhe.md)).
- **The bookkeeping side is DERIVED, Lean sorry-free**: `len(W_free) = 11A`,
  interfaces = bonds = A−1, `10A−5 = 5·(2A−1)` over chain units
  (nucleons + bonds), offset −5 = open-chain boundary, `σ+σ⁻¹ = 10A−2`
  (A-only, bar-even), writhe `= 4Z` (Z-only, bar-odd)
  (`QOU/Mass/BindingResidualExponent.lean`,
  `QOU/BraidKnot/DeltaLambdaExponentKeystone.lean`).
- **H1 (trace-side location) REFUTED**: the 10/nucleon increment is
  carried by ord(B_AME), not by the framework trace
  ([H1 refutation](../audits/2026-06-13-9b-h1-exponent-location-refuted.md)).
  Deriving the exponent ≡ deriving B_AME(A) itself.
- **Per-site "5" caveat**: against the exact Kashaev `B_sym` the
  per-site exponent collapses to ≈0–1, so the 5 is an artifact of
  B_pred's linearization, not a Bring-quintic q₀⁵.
- **What survives as genuinely open**: (a) the mirror-pair proton-excess
  penalty coefficient κ = b/4 ≈ −0.437 (b(A) constant −1.747 ± 0.030 across
  A=6–12; sign derived from the p≠n intra-writhe seed 3 vs 1, magnitude
  open); (b) the IMME same-T quadratic `c ≈ −0.1` constancy check + the
  `imme_third_diff_zero` Δ³=0 prediction on a 4th multiplet member.

**Implication**: "derive-or-refute 10A−5" is DONE (refuted-as-global,
derived-as-bookkeeping). Remaining leverage is the Z-correction /
IMME leg, which is a *prediction check*, not a closure search.

### Gap 2 — per-depth α_k assignment: the tower contradicts the derived α_k

- The depth-stratified tower (`binding_depth_stratified_rust.py:62-88`)
  uses α_0=1, α_1=1, α_2=z², α_3=1, α_{k≥4}=m_e·8G. But the framework's
  own Markov-pairing derivation `prop:alpha-k-derivation-procedure`
  ([explicit-alpha-k-h3](../../content/quantum-observable-universe/mass-theory/explicit-alpha-k-h3.md))
  gives **α_1 = 0** and **α_3 = h·z² + z ≈ 0.5514** at H₃. The production
  tower silently overrides two of the four derived values.
- All assignment-repair attempts refuted: geometric recursion
  (`alpha-k-categorical-closure.md`), knot-magnitude β-reweighting,
  self-conjugate restriction (witnesses: best is uniform, max/min 1.82).
- Structural diagnosis
  ([canonical-default audit §why](../audits/2026-06-09-binding-canonical-default-depth-stratified.md)):
  the additive tower has **no A-scale slot** and its χ-differences
  concentrate at depths where α_k is small — an additive α_k·Φ_k sum
  cannot close regardless of assignment. Magic-A flat (⁴He +5.87%)
  beats the tower (−50%) *by not decomposing*.
- The live productive direction per
  [`docs/coordination/2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md):
  extensive many-body / SW-period-residue / jet-order body-series, not
  α_k retuning.

**Implication**: the cheap, honest move is a small probe — evaluate the
tower with the *derived* α_k (α_1=0, α_3=h·z²+z) as an audit datum —
plus a doc correction recording that the tower's assignment contradicts
`prop:alpha-k-derivation-procedure`. The strategic weight shifts to the
body-order series (Gap 3/4).

### Gap 3 — many-body series: the gate has moved to "additive extensive term"

- The [intensive-vs-extensive audit](../audits/2026-06-02-binding-intensive-vs-extensive-derivation.md)
  dissolved the per-block-density gate: `B = E₀·Δtr_M` is intensive
  (saturates ~3–4 MeV; A-growth 1.65× vs required 12.72×), and **no
  per-block weight can convert an intensive quantity into an extensive
  one**. The missing object is an *additive extensive term*.
- Pairwise chain bond-sum: ⁴He 26% (many-body residual +20.9 MeV,
  [many-body ceiling](../audits/2026-06-02-binding-many-body-ceiling.md)).
- The unifying object is `prop:binding-manybody-jet-filtration`
  (`B = Σ_{n≥2} B_n`, body order = jet vertical degree): n=2 (deuteron)
  and n=4 (magic-A, ⁴He-specific — NOT an A-linear bulk, per the
  [A-scaling diagnostic correction](../audits/2026-06-28-delta-lambda-borromean-ascaling-diagnostic.md))
  anchored; **n=3 open**; ρ_F=2 consumed as §3b-cond input.
- Known inconsistency (link-assignment open item): the deuteron n=2
  anchor is quoted both as `m_e·Vol(6₂)` (+1.1%) and `m_e·Vol(𝓑₃)·Δtr`
  (+0.19%) in cheat-sheet §9.3; and `binding_k_solver.py` assigns
  braid-closure (chain, Vol=0) vs volume-registry (Borromean, 8G) to the
  same nucleus ([link-assignment audit](../audits/2026-06-03-binding-link-assignment-heuristic.md)).

### Gap 4 — brane-tower normalization: U-shaped residual, per-λ weight is the frontier

- Borromean single pipeline (`borromean_binding_recompute.py`):
  τ = 0.998562 < 1 ⇒ converges ∀Z. Residual `net/target` is **U-shaped
  with 6.17× spread**: D 1.115 (over), ⁴He 0.226 (max under), ¹⁶O 0.440,
  ⁵⁶Fe 1.392 (over). Edge-set sparsification refuted (worsens to 17.9×).
- "Missing per-λ weight" concretely: the tower applies uniform E₀ where
  the canonical `B = m_e·Σ_λ y_λ χ^λ Δ_λ` carries a per-partition weight.
- The [formalize-first plan §7](../audits/2026-06-28-brane-tower-formalize-first-plan.md)
  identifies **one missing object answering both** the isobar
  hyperbolic-volume recovery and the binding closure: the FR-restricted
  per-partition projector weight `χ^λ → χ^λ·χ^λ(e_{K*})`. Named next
  steps: (1) do NOT author the false bound `|tr_M(ξ)| < q₀` on the
  atom-word; (2) re-express the tower over β_Bor (done, PR #3016);
  (3) **Lean the true bound** `|tr_M(β_Bor)| < 1 ⇒ pair traces < q₀`;
  (4) bean `ovud` (wire the Li₂^q brane tower into production F_Bor).

## Approach decision (2026-07-02)

Ordered by cost/decisiveness, honoring the Δ_λ gate (no 7th fit ansatz)
and formalize-first:

1. **Doc currency (this PR, cheap, zero-risk).** The cheat-sheet §0 9b
   row still says "derive-or-refute 10A−5" — that item RESOLVED on
   2026-06-29 (refuted-as-global at A≥5, derived-as-bookkeeping
   `10A−5 = 5(2A−1)` Lean sorry-free). Update the row to point at the
   surviving open legs (per-λ weight; κ; IMME checks).
2. **Derived-α_k probe (cheap, decisive).** Evaluate the depth-stratified
   tower with the framework's own derived H₃ α_k (α_1=0, α_3=h·z²+z)
   instead of the empirical assignment (α_1=α_3=1). Either outcome is a
   permanent audit datum: improvement ⇒ the empirical assignment was the
   bug; degradation ⇒ scope-limited negative confirming the structural
   "no additive tower closes" diagnosis.
3. **IMME prediction checks (cheap, falsifiable).** c(A) constancy at
   A=10,12 same-T; `imme_third_diff_zero` (Δ³=0) on a 4th multiplet
   member. Genuine predictions, not closure search.
4. **Per-λ FR-projector weight on the Borromean tower (the strategic
   frontier, larger).** Implement `χ^λ·χ^λ(e_{K*})` per plan §7 and test
   against the U-shaped residual; Lean the true convergence bound.
   This is the one move that attacks the actual Δ_λ frontier with a
   *structural* (projector, not fitted) candidate.

## Executed 2026-07-02

- **Item 2 (derived-α_k probe): DONE — scope-limited negative.**
  `computations/probes/binding_depth_stratified_derived_alpha_probe.py`
  (+ witness). Same LR Φ_k pipeline, ⁴He chi now 77/77. Production
  baseline reproduced exactly (ratios 0.2728 / 0.3310 / 0.3437 / 0.4970,
  max/min 1.822). Derived assignment (α_1=0, α_3=h·z²+z) degrades every
  atom: ratios 0.1402 / 0.2535 / 0.2676 / 0.4608, max/min 3.286 — the
  depth-1 stratum that α_1=0 removes carries ~half of the deuteron's
  predicted binding. Scope (a): constrains the
  derived-α_k-in-additive-tower combination only; does not exclude the
  derived α_k as an ingredient of a multiplicative / A-scaled assembly.
  The documented contradiction (tower overrides derived values) is real
  but is not the undershoot's cause — further support for the
  "no additive assignment closes" structural diagnosis.
- **Item 1 (doc currency): DONE.** Cheat-sheet §0 9b row refreshed —
  `10A−5` marked resolved (refuted-as-global / derived-as-bookkeeping),
  probe result recorded, owner-gap column now points at the per-λ
  weight, κ, IMME checks, and bean `ovud`.
- Items 3 (IMME checks) and 4 (per-λ FR-projector weight) remain queued
  pending owner direction.

## Executed 2026-07-02 (round 2 — owner approved legs 1+3+4)

- **IMME Δ³=0 quartet check: PASSES.**
  `computations/delta_lambda_imme_quartet.py` (+ witness). A=9 T=3/2
  quartet ⁹Li/⁹Be/⁹B/⁹C, inner members IAS-corrected (14.3925 / 14.6550
  MeV): same-T third difference Δ³ = −0.012 (cubic d = −0.002,
  |d/b| = 0.001) vs ground-state Δ³ = −0.50 (pure T-contamination,
  collapses 42× under IAS). First falsifiable test of the degree-2 IMME
  truncation — it survives, matching Lean `imme_third_diff_zero`.
  b(9) = −1.84, same-T c(9) = −0.071, consistent with the triplet trends.
- **Per-λ FR-projector, H₃ proxy: scope-limited negative.**
  `computations/probes/borromean_per_lambda_fr_probe.py` (+ witness).
  Wedderburn re-lift of τ (1.96e-4 convention mismatch vs the Lean
  closed form flagged), (2,1)-channel reweight by 4 structural 4₁
  Fricke candidates × 2 placements: all 8 are monotone rescales of the
  U-shaped residual (baseline spread 6.166 reproduced); none flatten it.
  Sharpened spec: a per-nucleon scalar factor structurally cannot bend
  the U — the FR weight must act per-partition at H_{3A} (fr_pullback
  machinery over Borromean atom words), which is the remaining open test.
- **κ location decomposition: FRAMEWORK-side (inverts the H1 pattern).**
  `computations/probes/kappa_writhe_side_decomposition_probe.py`
  (+ witness). Exact split b_total = b_AME − b_pred from the IMME
  witnesses: b_pred (interface asymmetry z vs z−h) is A-constant ≈ +1.37
  and carries ~78% of |b|; b_AME ≈ −0.40. So κ = −0.437 ≈ −0.343
  (framework) − 0.094 (AME): unlike the bar-even leading term (H1
  refutation), **κ is derivable from the canonical trace**. Near-match
  flag (not asserted): log_q₀(z/(z−h))/4 = 1.2998 within 5% of b_pred/4.

### Follow-up queue (next session / follow-up branch)

1. Derive b_pred's A→∞ closed form from the tower's interface algebra
   (the 1.2998 near-match is the natural first candidate to
   prove-or-refute symbolically).
2. H_{3A} per-partition FR test: run `fr_pullback_k3_test.py` machinery
   over Borromean atom words (needs `compute_atom_chi_rust.py`
   regeneration for the Borromean representation; A ≤ 4 cheap, A ≥ 5
   hours).
3. Lean the true convergence bound `|tr_M(β_Bor)| < 1 ⇒ pair traces < q₀`
   (brane-tower plan §5 step 3).
4. Resolve the 1.96e-4 y-lambda-vs-closed-form τ convention mismatch.

## Executed 2026-07-02 (round 3 — legs 1/2/3/4)

- **Leg 1 — b_pred closed form: DERIVED.**
  `computations/probes/b_pred_mirror_slope_closed_form.py` (+ witness).
  `b_pred(A) = log_q₀(τ_p/τ_n) + log[(1−ε(N,Z))/(1−ε(Z,N))]/((N−Z)·ln q₀)`,
  `ε(Z,N) = z^{Z−1}(z−h/2)(z−h)^{N−1}` — matches the measured A=6..12
  slopes to their rounding; plateau = log_q₀(τ_p/τ_n) = 1.37181; hence
  κ_FW = −0.34295 DERIVED (the ~78% framework share of κ). The
  interface-only candidate 1.2998 is refuted as the asymptote (scope a).
  Discriminant recorded: the Borromean pipeline (τ_p = τ_n, GAP-A-4)
  must show a different b_pred — a test between nucleon representations.
- **Leg 3 — Lean convergence bound: DONE, sorry-free.**
  `QOU/BraidsAndKnots/BorromeanTowerConvergence.lean` — trace < 1 for
  h ≠ 0 (sharp at h = 0), |t| < 1 on h² ≤ 1, pair + dressed-pair Li₂^q
  radius bounds, composite `borromean_pair_within_radius`. Verified
  lean-direct exit 0. The refuted atom-word bound is not stated.
- **Leg 2 — H_{3A} FR test: BLOCKED in this sandbox.** pyhecke_native
  wheel unreachable; local cargo build 403s on the clarabel fork
  (github.com/litlfred/Clarabel.rs outside session scope) even with
  CARGO_NET_GIT_FETCH_WITH_CLI and --no-default-features (the
  [patch.crates-io] git source resolves at metadata time). Unblock
  paths: the stub-crate recipe (pyhecke-native README §Clarabel) or an
  unrestricted environment. Spec is in the round-2 follow-up queue.
- **Leg 4 — prepare-merge run on PR #3213** (see PR).
