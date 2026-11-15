import Mathlib.Tactic

/-!
# QOU.BraidKnot.DeltaLambdaRefutation — formalize-the-refutation of Δ_λ closure ansätze

The per-isotope binding formula `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` requires per-partition
`Δ_λ` values. The per-partition **VALUE is now PROVED** (2026-08-02, sorry-free,
general-n): `Δ_λ = (-1)^{n(λ)}·dim V_λ`
(`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`). The six ansätze refuted
below (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov) did **not** fail on the value — they failed to derive
the many-body **MAGNITUDE** `r* ≈ 1.585` (which no per-block `Δ_λ` can supply; the
missing term is super-pairwise, pairwise cap `ρ_A ≤ C(A,2)` proved in
`QOU.MassTheory.exchangeDet_pow_two_le_four`). So the gate rule —
**"do not propose a seventh fit-based ansatz for the magnitude"** — still stands, and
this file operationalises the *magnitude*-refutations (the value is now Lean-proved,
not merely enforced by reviewer vigilance).

This file **operationalises** that rule per the *formalize-the-refutation* discipline
(`.claude/skills/local/compute-author.md §3.4`): a refuted ansatz becomes a
machine-checked inequality `tol < |prediction − target|`, not a prose warning, so the
dead ansatz cannot be silently re-proposed and slip past review.

The numbers are 12-figure truncations of the 50-dps witness
`computations/rho-k-h3a-co-casimir.witness.json` (`allPassed: true`); the refutation
holds with enormous margin (gap ≈ 4.526 m_e units vs tol 1), so 12 figures is far more
than the inequality needs. Statements are decidable rational (in)equalities — sorry-free,
`norm_num`-discharged over `ℚ`.

## Lemmas

- `coCasimir_closureGap_eq` — the closure gap equals `|prediction − target|` exactly.
- `coCasimir_refuted_deuteron` — **magnitude** refutation: the ansatz misses by > tol.
- `coCasimir_wrong_sign` — **sign** refutation: the ansatz predicts a *positive*
  binding-density sum where the empirical target is *negative*.

Follow-up (per compute-author §3.4): promote to a content-block triple
`lem:frobenius-cocasimir-refuted-deuteron` beside
[`conj:rho-prefactor-structural`](../../../../mass-theory/conj-rho-prefactor-structural.md)
(GAP-A-4), and add the remaining five refuted ansätze as their clean witnessed
numbers become available.

## References

- [leitner2026] `computations/rho-k-h3a-co-casimir.witness.json` (50 dps, `allPassed: true`)
- [leitner2026] `docs/audits/2026-05-18-delta-lambda-gating-context.md` (Option B; the six failed ansätze)
-/

namespace QOU.BraidKnot.DeltaLambdaRefutation

/-- Frobenius co-Casimir predicted `Σ_λ y_λ χ^λ Δ_λ` at the deuteron (in `m_e` units).
12-figure truncation of `/data/co_casimir_prediction/sum_contributions_signed`
(50 dps value `0.17312047167782761…`; the witness was regenerated 2026-10-05 at the
proton pin, and this figure was updated 2026-11-15 from the stale `0.144959224127`).
-- Ref: [leitner2026] computations/rho-k-h3a-co-casimir.witness.json -/
def coCasimirSum : ℚ := 173120471677 / 1000000000000

/-- Empirical `−B_D/m_e` (in `m_e` units), the deuteron binding-density target.
12-figure truncation of `/data/target_signed` (50 dps value `−4.35336749125644…`).
-- Ref: [leitner2026] computations/rho-k-h3a-co-casimir.witness.json -/
def targetSigned : ℚ := -4353367491256 / 1000000000000

/-- Closure gap `|prediction − target|`, witness `/data/.../closure_gap_LHS_minus_RHS`
(50 dps value `4.52648796293427…`). -/
def closureGap : ℚ := 4526487962933 / 1000000000000

/-- Viability tolerance: a candidate `Δ_λ` closure must land the deuteron
binding-density sum within `1` `m_e` unit of the empirical target to be viable.
The co-Casimir ansatz misses by ≈ 4.5, so the verdict is insensitive to `tol`. -/
def tol : ℚ := 1

/-- The recorded closure gap equals `|prediction − target|` exactly (rational identity);
this ties the `closureGap` literal to the predicted/target literals so they cannot drift
apart independently. -/
theorem coCasimir_closureGap_eq : |coCasimirSum - targetSigned| = closureGap := by
  have h : coCasimirSum - targetSigned = closureGap := by
    unfold coCasimirSum targetSigned closureGap; norm_num
  rw [h]
  exact abs_of_pos (by unfold closureGap; norm_num)

/-- **Refutation (magnitude).** The Frobenius co-Casimir `Δ_λ` ansatz misses the
deuteron binding-density target by more than the viability tolerance (gap ≈ 4.526
`m_e` units > `tol = 1`). This is the machine-checked face of the witness's
`closure_gap_LHS_minus_RHS`; it makes "the co-Casimir ansatz is refuted" a theorem,
not a prose warning. -/
theorem coCasimir_refuted_deuteron : tol < |coCasimirSum - targetSigned| := by
  rw [coCasimir_closureGap_eq]
  unfold tol closureGap; norm_num

/-- **Refutation (sign).** A stronger, scale-free defect: the co-Casimir ansatz predicts
a *positive* binding-density sum (`coCasimirSum > 0`) where the empirical target is
*negative* (`targetSigned < 0`). The wrong sign cannot be repaired by any positive
normalisation `ρ > 0`, so the refutation survives the (separately gated) overall-scale
freedom. -/
theorem coCasimir_wrong_sign : 0 < coCasimirSum ∧ targetSigned < 0 := by
  unfold coCasimirSum targetSigned
  refine ⟨by norm_num, by norm_num⟩

/-! ## The six refuted Δ_λ closure ansätze — landscape (anti-re-walk index)

Per AGENTS.md §"Δ_λ gate", six closure ansätze are refuted, and the "no seventh
fit-based ansatz" rule depends on knowing *why* each is dead. They fail by
**structurally different** mechanisms — only the co-Casimir ansatz fails as a clean
numeric miss (the `≠` lemmas above), so the other five are catalogued here with their
mechanism + the formalisation/audit that carries each refutation, rather than forced
into a miss-shaped lemma they do not fit (which would misrepresent them).

| # | ansatz | refutation mechanism | where |
|---|--------|----------------------|-------|
| B | Frobenius co-Casimir `1/dim_q(λ)` | clean numeric **miss + wrong sign** (gap ≈ 4.526 m_e; pred > 0, target < 0) | **this file** (`coCasimir_*`) |
| C | Demazure-fibre `y_λ·D_w/D_{w₀}` | **tautological** — `Δ_λ ~ 10⁻⁵`, reproduces `M_LO`, vortex-blind | `2026-05-18-delta-lambda-gating-context.md` row C |
| D-Plancherel | LP shadow price `min Σ\|Δ_λ\|·w_λ` | **under-determined** (not a miss) — reproduces Occam exactly, `L∞ = 1.9e-15`; shifts the freedom to the cost choice | gating-context row D-Plancherel |
| D-Frobenius | LP alt cost | under-determined — picks a different singleton (`λ=[6]`, `Δ=−47.16`); same defect | gating-context row D-Frobenius |
| E | crystal-graph (Kashiwara, `q→1`) | **KL-positivity prune** — target `Δ_λ = sgn(w₀)·dim` is mixed-sign, KL multiplicities are `≥ 0`, so no `Σ_w n^w_λ·X_w` can supply the chirality sign | Lean sorry-free `QOU.BraidsAndKnots.S5SO3FiberAction.PartitionOf5.deltaSign_mixed`; `2026-06-16-option-e-probe4-kl-positivity-prune.md` |
| F | Wenzl-bridge augmented Markov | **ill-posed** — over-determined axiom set (closure-pickle) | gating-context row F |

The co-Casimir `≠` lemmas above are the machine-checked face of row B; rows C/D/F are
refuted by mechanism (documented, not miss-shaped); row E is independently Lean-proved.
Together these close the "no 7th ansatz" gate: a candidate must defeat **all six**
distinct mechanisms, not merely beat one number. -/

end QOU.BraidKnot.DeltaLambdaRefutation
