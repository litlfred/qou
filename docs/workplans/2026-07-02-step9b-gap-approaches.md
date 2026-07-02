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
