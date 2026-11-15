import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# W_λ normalization invariance — the geometric `d_q²/D²` vs keystone `d_q²/[n]_q!` fork

Formalize-first companion to the C1-normalization question raised on PR #2524
(Beasley–Witten Seifert–CS localization gives `W_λ = d_q²/D²`, the true
RT/Verlinde Plancherel measure, whereas the keystone consumer uses
`d_q²/[n]_q!`). The two families differ only by the **single, λ-independent**
global factor `F/D²` (`F = [n]_q!`, `D² = Σ_λ d_q²`). This file proves that
structural fact *before* the numerical consumer probe is run, so the probe's
verdict is bounded in advance:

* `wPlanch_eq_global_factor` — the geometric weight is the keystone weight times
  the **λ-independent** scalar `F/D²`. (The normalization change is a global
  rescale, not a per-block reshuffle.)
* `wPlanch_sum_one` — the geometric weight is a genuine probability measure
  (`Σ_λ = 1`), by construction `D² = Σ_λ d_q²`.
* `wKey_sum_eq_Z` — the keystone weight sums to `Z = D²/F`, **not** `1` in
  general (the `Z(n)` defect; `keystone_wlambda_Z_defect_n_scaling.py`).
* `ratio_invariant` — **the pruning result.** Any *same-block* ratio of weights
  (e.g. muon `(3,2)` vs electron `(3,1,1)`, both `⊢ 5`) is **identical** under
  the two normalizations: the `F/D²` factor cancels. Hence the C1 choice is
  **invisible** to any generation observable expressed as a same-`n` ratio /
  normalized-within-`n` weight; it can shift a prediction only through a
  cross-`n` or absolute (un-normalized) use of `W_λ`.

Everything is a pure field identity over a generic `{R : Type*} [Field R]`
(§7c: no archimedean input; `q₀` and the 210 ppb target are never used). The
q-dimensions `d : ι → R` and the factor `F` are abstract; the result holds for
the Hecke q-dimensions specialized at any `q`.

LaTeX label: `prop:wlambda-normalization-invariance`

## References

- [leitner2026] docs/audits/2026-06-20-keystone-wlambda-beasley-witten-localization.md (PR #2524, the C1 finding)
- [leitner2026] docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py (the `Z(n)` defect)
-/

namespace QOU.BraidKnot.WLambdaNorm

variable {R : Type*} [Field R] {ι : Type*}

/-- Global quantum dimension `D² = Σ_{λ∈s} d_q(λ)²` of an `n`-block. -/
def D2 (s : Finset ι) (d : ι → R) : R := ∑ l ∈ s, (d l) ^ 2

/-- Geometric / RT–Verlinde Plancherel weight `w_λ = d_q(λ)²/D²` (Beasley–Witten
localization output; the true probability measure). -/
def wPlanch (s : Finset ι) (d : ι → R) (l : ι) : R := (d l) ^ 2 / D2 s d

/-- Keystone weight `W_λ = d_q(λ)²/F` with `F = [n]_q!` (the consumer form). -/
def wKey (d : ι → R) (F : R) (l : ι) : R := (d l) ^ 2 / F

/-- **The normalization change is one λ-independent global factor.**
`wPlanch = (F/D²) · wKey`. The geometric and keystone weights are proportional
with a constant (`F/D²`) that does not depend on the block `λ`. -/
theorem wPlanch_eq_global_factor (s : Finset ι) (d : ι → R) (F : R)
    (hF : F ≠ 0) (hD : D2 s d ≠ 0) (l : ι) :
    wPlanch s d l = (F / D2 s d) * wKey d F l := by
  unfold wPlanch wKey
  field_simp

/-- **Geometric weight is a probability measure.** `Σ_{λ∈s} d_q²/D² = 1`
(`D² = Σ d_q²` by construction). -/
theorem wPlanch_sum_one (s : Finset ι) (d : ι → R) (hD : D2 s d ≠ 0) :
    ∑ l ∈ s, wPlanch s d l = 1 := by
  unfold wPlanch
  rw [← Finset.sum_div]
  exact div_self hD

/-- **Keystone weight sums to the defect `Z = D²/F`, not `1`.** This is the
`Z(n)` of the defect script: `Σ_{λ∈s} d_q²/F = (Σ d_q²)/F = D²/F`. -/
theorem wKey_sum_eq_Z (s : Finset ι) (d : ι → R) (F : R) :
    ∑ l ∈ s, wKey d F l = D2 s d / F := by
  unfold wKey D2
  rw [← Finset.sum_div]

/-- **Pruning result: same-block ratios are normalization-invariant.**
For any two blocks `l, m` in the same `n` (with `d m ≠ 0`), the ratio of
geometric weights equals the ratio of keystone weights — the `F/D²` factor
cancels. Consequence: the C1 normalization choice cannot change any generation
observable expressed as a same-`n` ratio. -/
theorem ratio_invariant (s : Finset ι) (d : ι → R) (F : R)
    (hF : F ≠ 0) (hD : D2 s d ≠ 0) {l m : ι} (hm : d m ≠ 0) :
    wPlanch s d l / wPlanch s d m = wKey d F l / wKey d F m := by
  have hm2 : (d m) ^ 2 ≠ 0 := pow_ne_zero 2 hm
  unfold wPlanch wKey
  field_simp

/-- **Both ratios equal the bare q-dimension ratio `d_l²/d_m²`** — the
normalization-independent content. -/
theorem ratio_eq_qdim_ratio (s : Finset ι) (d : ι → R)
    (hD : D2 s d ≠ 0) {l m : ι} (hm : d m ≠ 0) :
    wPlanch s d l / wPlanch s d m = (d l) ^ 2 / (d m) ^ 2 := by
  have hm2 : (d m) ^ 2 ≠ 0 := pow_ne_zero 2 hm
  unfold wPlanch
  field_simp

end QOU.BraidKnot.WLambdaNorm
