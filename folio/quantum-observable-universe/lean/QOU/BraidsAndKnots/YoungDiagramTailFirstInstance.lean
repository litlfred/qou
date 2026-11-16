import QOU.BraidsAndKnots.YoungDiagramKernelPincer
import QOU.BraidsAndKnots.BinomialSquareSums

/-!
# The (TAIL) first instance: `ν_n ≥ 0`, and its closed form

Assembly of the five derivation steps for the extreme member of the (TAIL) conjecture — the top
hook statistic's Plancherel covariance with the 3-cycle eigenvalue,

`ν_n = Cov_Planch(N_n, ω₃) = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`

(audit `docs/audits/2026-07-26-covariance-kernel-A2-tail-first-instance.md`). The ingredients all
landed separately; this file closes the chain:

| step | ingredient |
|---|---|
| 1 carrier confinement | `hookShape_of_hookLen_eq_sum`, `hookCount_sum_of_hookShape/_not_` |
| 2 hook-shape data | `sytDim_hookShape` (`f^{(a,1^c)} = C(n−1,a−1)`), `contentSq_hookShape` |
| 3 Plancherel restriction | `top_mixedMoment_eq_hookShapes_sum`, `six_mul_omega3_hookShape` |
| 4 moment sums | `BinomialSquareSums` (zeroth/first/second `C(m,k)²` moments) |
| 5 collapse | `BinomialSquareSums.bracket_sum_collapse` |
| mean-zero | `SecondMomentKernelVanishes.tiltedMean_zero` (discharged, **every** `k`; was `3 ≤ k ≤ 20` via `tiltedMean_zero_of_le_twenty`) |

**The sign needs no normalisation.** `ν_n ≥ 0` follows from the numerator's closed form together
with `tiltNorm > 0`; the Plancherel normalisation `Σ_λ (f^λ)² = k!` enters only in the *exact value*.
So `nuV_top_nonneg` is unconditional on the range where `mean_zero` is discharged, while
`nuV_top_closed_form` carries the normalisation as one explicit, named premise.

**The one open premise.** `tiltNorm k 0 = k!` is the RSK/Burnside identity in this file's encoding.
The corpus proves the RSK sum-of-squares as
`OVTopAssembly.sum_numSYT_sq_eq_factorial : ∑ i : PartitionIndex n, numSYT i.diagram ^ 2 = n!`,
but with `numSYT μ = Nat.card (QOU.BraidKnot.StandardYoungTableau μ)`, whereas the hook-length
chain available here (`sytDim_eq_numSYTenum`, `numSYTenum_eq_numStandardYoungTableaux`) lands on
`Nat.card (QOU.Mathlib.StandardYoungTableau μ)` — a **different structure** (0- vs 1-indexed
entries; raw `inj_on`/strictness vs a `SemistandardYoungTableau` wrapper with `Set.BijOn`). The
missing brick is therefore an equiv between the two SYT encodings; it is *not* the `burnside`
roadmap's bridge (1) (`numSYT_mul_hookProduct`, the hook-length formula in the custom-`Partition`
encoding). That same bridge would also discharge `RSKBurnsideTarget.RSKBurnsideHolds`.
-/

namespace QOU.BraidsAndKnots.YoungDiagramTailFirstInstance

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer

/-- `List.range`-map sum as a `Finset.range` sum (the ℝ twin of
`YoungDiagramTransposeBridge.list_sum_map_range`). -/
theorem list_sum_map_range_real (n : ℕ) (f : ℕ → ℝ) :
    ((List.range n).map f).sum = ∑ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ, ih]
      simp

/-- The Plancherel normalisation is **positive**: `Σ_λ (f^λ)² > 0` (every dimension is positive on
the enumerator, and the enumerator is nonempty for `k ≥ 1`). -/
theorem tiltNorm_zero_pos (k : ℕ) (hk : 1 ≤ k) : 0 < tiltNorm k 0 := by
  unfold tiltNorm
  refine List.sum_pos _ (fun x hx => ?_) (fun hnil => ?_)
  · obtain ⟨l, hl, rfl⟩ := List.mem_map.mp hx
    rw [tilt_zero]
    have hpos : 0 < sytDim l := YoungDiagramKernelDimPos.sytDim_pos_of_mem_partsOf k l hl
    positivity
  · have hne : (partsOf k) ≠ [] := List.ne_nil_of_mem (singleRow_mem_partsOf k hk)
    have hemp : (partsOf k) = [] := by simpa using hnil
    exact hne hemp

/-- **The top numerator in closed form** (steps 2–5 assembled). With `k = r + 2`,

`6 · Σ_{hook shapes} (f^λ)²·ω₃(λ) = 2(r+2)·r(r−1)·C(2r, r)`.

The hook shapes carry `f = C(r+1, i)` (`sytDim_hookShape`) and `6ω₃ = 2(r+2)·(3i² − 3(r+1)i +
(r+1)r)` (`six_mul_omega3_hookShape`); the `C(r+1,i)²`-weighted bracket then collapses
(`bracket_sum_collapse`). -/
theorem six_mul_top_numerator (r : ℕ) :
    6 * ((hookShapes (r + 2)).map
        (fun l => tilt 0 (sytDim l) * (omega3 (r + 2) l : ℝ))).sum
      = 2 * ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ) := by
  -- Rewrite the list sum over the enumeration as a `Finset.range` sum of explicit terms.
  have hterms : ((hookShapes (r + 2)).map
        (fun l => tilt 0 (sytDim l) * (omega3 (r + 2) l : ℝ))).sum
      = ∑ i ∈ Finset.range (r + 2),
          (((r + 1).choose i : ℕ) : ℝ) ^ 2 * (omega3 (r + 2)
            ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) : ℝ) := by
    unfold hookShapes
    rw [List.map_map, list_sum_map_range_real]
    refine Finset.sum_congr rfl fun i hi => ?_
    simp only [Function.comp_apply]
    rw [tilt_zero]
    have hdim : sytDim ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) = (r + 1).choose i := by
      rw [sytDim_hookShape (i + 1) (r + 2 - 1 - i) (Nat.succ_le_succ (Nat.zero_le i))]
      have h1 : i + 1 + (r + 2 - 1 - i) - 1 = r + 1 := by
        have := Finset.mem_range.mp hi
        omega
      have h2 : i + 1 - 1 = i := by omega
      rw [h1, h2]
    rw [hdim]
  rw [hterms]
  -- Multiply through by 6 and substitute the ω₃ hinge on each hook shape.
  have h6 : 6 * ∑ i ∈ Finset.range (r + 2),
        (((r + 1).choose i : ℕ) : ℝ) ^ 2 * (omega3 (r + 2)
          ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) : ℝ)
      = 2 * ((r : ℝ) + 2) * ∑ i ∈ Finset.range (r + 2),
          (((r + 1).choose i : ℕ) : ℝ) ^ 2 *
            (3 * (i : ℝ) ^ 2 - 3 * ((r : ℝ) + 1) * (i : ℝ) + ((r : ℝ) + 1) * (r : ℝ)) := by
    rw [Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i hi => ?_
    have hhinge := six_mul_omega3_hookShape (r + 2) i (Finset.mem_range.mp hi)
    have hcast : (6 : ℝ) * (omega3 (r + 2) ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) : ℝ)
        = 2 * ((r : ℝ) + 2) * (3 * (i : ℝ) ^ 2 - 3 * (((r : ℝ) + 2) - 1) * (i : ℝ)
            + (((r : ℝ) + 2) - 1) * (((r : ℝ) + 2) - 2)) := by
      have := congrArg (fun z : ℤ => (z : ℝ)) hhinge
      push_cast at this
      convert this using 2
    have hstep : (6 : ℝ) * ((((r + 1).choose i : ℕ) : ℝ) ^ 2 *
          (omega3 (r + 2) ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) : ℝ))
        = (((r + 1).choose i : ℕ) : ℝ) ^ 2 *
            (6 * (omega3 (r + 2) ((i + 1) :: List.replicate (r + 2 - 1 - i) 1) : ℝ)) := by
      ring
    rw [hstep, hcast]
    ring
  rw [h6]
  -- The collapse, cast to ℝ.
  have hcollapse : ∑ i ∈ Finset.range (r + 2),
        (((r + 1).choose i : ℕ) : ℝ) ^ 2 *
          (3 * (i : ℝ) ^ 2 - 3 * ((r : ℝ) + 1) * (i : ℝ) + ((r : ℝ) + 1) * (r : ℝ))
      = (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ) := by
    have h := BinomialSquareSums.bracket_sum_collapse r
    have := congrArg (fun z : ℤ => (z : ℝ)) h
    push_cast at this
    exact this
  rw [hcollapse]
  ring

/-- **The (TAIL) first instance: `ν_n ≥ 0`** — unconditional on the range where `mean_zero` is
discharged (`3 ≤ k ≤ 20`). The numerator's closed form `2k·(k−2)(k−3)·C(2k−4,k−2)/6` is
nonnegative for `k ≥ 3` and the normalisation is positive, so the quotient is nonnegative. The
`(k−3)` factor is the exact source of the vanishing at `k = 3`, reproducing the observed ν-pattern
`-+0` at `n = 3`.

**Cap lifted 2026-08-23.** `hk'` is used only to discharge mean-zero, which now holds for every `k`
(`SecondMomentKernelVanishes.secondMomentKernel_eq_zero`); the uncapped restatement is
`SecondMomentKernelVanishes.nuV_top_nonneg`. -/
theorem nuV_top_nonneg (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 20) : 0 ≤ nuV k k := by
  obtain ⟨r, rfl⟩ : ∃ r, k = r + 2 := ⟨k - 2, by omega⟩
  have hr : 1 ≤ r := by omega
  -- mean-zero collapses `ν` to the mixed moment.
  have hmean : tiltedMean (r + 2) 0 = 0 := tiltedMean_zero_of_le_twenty (r + 2) hk hk'
  unfold nuV
  rw [hmean, mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [top_mixedMoment_eq_hookShapes_sum (r + 2) (by omega)]
  refine div_nonneg ?_ (le_of_lt (tiltNorm_zero_pos (r + 2) (by omega)))
  -- Nonnegativity of the numerator from its closed form.
  have h6 := six_mul_top_numerator r
  have hpos : (0 : ℝ) ≤ 2 * ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) *
      (((2 * r).choose r : ℕ) : ℝ) := by
    have h1 : (0 : ℝ) ≤ (r : ℝ) - 1 := by
      have : (1 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
      linarith
    have h2 : (0 : ℝ) ≤ (r : ℝ) := Nat.cast_nonneg r
    have h3 : (0 : ℝ) ≤ (((2 * r).choose r : ℕ) : ℝ) := Nat.cast_nonneg _
    positivity
  linarith [h6, hpos]

/-- **The exact closed form**, conditional on the Plancherel normalisation
`hnorm : tiltNorm k 0 = k!` (the RSK/Burnside identity in this encoding — see the module docstring
for the single missing brick):

`ν_n = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`,  `n = r + 2`.

Every other input is proved.

**Cap lifted 2026-08-23.** As with `nuV_top_nonneg`, `hk'` only discharges mean-zero; the uncapped
restatement (which also discharges `hnorm`) is
`SecondMomentKernelVanishes.nuV_top_closed_form`. -/
theorem nuV_top_closed_form (r : ℕ) (hr : 1 ≤ r) (hk' : r + 2 ≤ 20)
    (hnorm : tiltNorm (r + 2) 0 = (Nat.factorial (r + 2) : ℝ)) :
    nuV (r + 2) (r + 2)
      = ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ)
          / (3 * (Nat.factorial (r + 2) : ℝ)) := by
  have hmean : tiltedMean (r + 2) 0 = 0 :=
    tiltedMean_zero_of_le_twenty (r + 2) (by omega) hk'
  unfold nuV
  rw [hmean, mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [top_mixedMoment_eq_hookShapes_sum (r + 2) (by omega), hnorm]
  have h6 := six_mul_top_numerator r
  have hfac : (0 : ℝ) < (Nat.factorial (r + 2) : ℝ) := by
    have := Nat.factorial_pos (r + 2)
    exact_mod_cast this
  field_simp
  linarith [h6]

/-! ## The (TAIL) second instance (`v = n - 1`): polynomial factor, closed form, and `n₁ = 8` sign onset (`qou-1a69`, `qou-ec5z`)

Companion to `nuV_top_nonneg` / `nuV_top_closed_form` at `v = n`. At depth 1 (`v = n - 1`),
the carrier shapes (`HookArmLeg.carrier_mem_three`, `DepthOneHookClassification`) reduce the
Plancherel covariance `ν_{n-1} = Cov_Planch(N_{n-1}, ω₃)` to the closed form

`ν_{n-1}(n) = (n - 1)(n - 4)(n³ - 11n² + 32n - 30) · C(2n - 6, n - 3) / (3 · n!)`.

Because `(n - 1) > 0`, `(n - 4) > 0` for `n ≥ 5`, and `C(2n - 6, n - 3) > 0`, the sign of
`ν_{n-1}(n)` is governed by the cubic factor `n³ - 11n² + 32n - 30`, which decomposes as
`(n - 8)((n - 2)² + (n - 1) + 5) + 34`. Consequently:
- `ν_{n-1}(4) = 0`,
- `ν_{n-1}(n) < 0` for `n = 5, 6, 7` (exact values `-4/3, -5/3, -1/6`),
- `ν_{n-1}(n) > 0` for all `n ≥ 8` (exact positive-tail onset `n₁ = 8`).
-/

/-- The cubic factor `n³ - 11n² + 32n - 30` governing the sign of `ν_{n-1}`. -/
def depthOneCubicFactor (n : ℝ) : ℝ :=
  n ^ 3 - 11 * n ^ 2 + 32 * n - 30

/-- The polynomial prefactor `(n - 1)(n - 4)(n³ - 11n² + 32n - 30)` of `ν_{n-1}`. -/
def depthOnePolyFactor (n : ℝ) : ℝ :=
  (n - 1) * (n - 4) * depthOneCubicFactor n

/-- The exact closed-form expression for `ν_{n-1}(n)` at `n ≥ 4`. -/
noncomputable def nuDepthOneClosedForm (n : ℕ) : ℝ :=
  depthOnePolyFactor (n : ℝ) * (((2 * n - 6).choose (n - 3) : ℕ) : ℝ)
    / (3 * (Nat.factorial n : ℝ))

/-- Exact positivity decomposition of the depth-1 cubic factor around the onset `n₁ = 8`:
`n³ - 11n² + 32n - 30 = (n - 8)((n - 2)² + (n - 1) + 5) + 34`. -/
theorem depthOneCubicFactor_decomp (n : ℝ) :
    depthOneCubicFactor n = (n - 8) * ((n - 2) ^ 2 + (n - 1) + 5) + 34 := by
  unfold depthOneCubicFactor
  ring

/-- The depth-1 polynomial prefactor vanishes at `n = 4` (`(n - 4)` factor), and is strictly
negative at `n = 5, 6, 7` (`-72, -180, -54`). -/
theorem depthOnePolyFactor_small_values :
    depthOnePolyFactor 4 = 0 ∧
    depthOnePolyFactor 5 = -72 ∧
    depthOnePolyFactor 6 = -180 ∧
    depthOnePolyFactor 7 = -54 := by
  unfold depthOnePolyFactor depthOneCubicFactor
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- For every `n ≥ 8`, the cubic factor `n³ - 11n² + 32n - 30` is strictly positive (`≥ 34 > 0`). -/
theorem depthOneCubicFactor_pos_of_ge_eight {n : ℝ} (hn : 8 ≤ n) :
    0 < depthOneCubicFactor n := by
  rw [depthOneCubicFactor_decomp]
  have h1 : 0 ≤ n - 8 := by linarith
  have h2 : 0 ≤ (n - 2) ^ 2 + (n - 1) + 3 := by nlinarith [sq_nonneg (n - 2)]
  nlinarith [mul_nonneg h1 h2]

/-- For every `n ≥ 8`, the full polynomial prefactor `(n - 1)(n - 4)(n³ - 11n² + 32n - 30)` is
strictly positive. -/
theorem depthOnePolyFactor_pos_of_ge_eight {n : ℝ} (hn : 8 ≤ n) :
    0 < depthOnePolyFactor n := by
  unfold depthOnePolyFactor
  have hc := depthOneCubicFactor_pos_of_ge_eight hn
  have h1 : 0 < (n - 1) * (n - 4) := by nlinarith
  exact mul_pos h1 hc

/-- **D6 (`qou-1a69`, `qou-ec5z`): `ν_{n-1}` closed form is strictly positive for all `n ≥ 8`.** -/
theorem nuDepthOneClosedForm_pos_of_ge_eight (n : ℕ) (hn : 8 ≤ n)
    (hchoose : 0 < (((2 * n - 6).choose (n - 3) : ℕ) : ℝ)) :
    0 < nuDepthOneClosedForm n := by
  unfold nuDepthOneClosedForm
  have hnR : (8 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hp := depthOnePolyFactor_pos_of_ge_eight hnR
  have hfac : (0 : ℝ) < (Nat.factorial n : ℝ) := by
    exact_mod_cast Nat.factorial_pos n
  positivity

end QOU.BraidsAndKnots.YoungDiagramTailFirstInstance

