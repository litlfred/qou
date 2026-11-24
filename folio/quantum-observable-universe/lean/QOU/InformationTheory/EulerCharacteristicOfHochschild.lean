import Mathlib.Tactic
import Mathlib.Data.Int.Interval
import Mathlib.Algebra.Ring.NegOnePow
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# The Euler characteristic of Hochschild homology is the Hodge one

The 2026-09-15 separation of the four "Euler characteristics"
(`rem:three-euler-characteristics`) reads the `−6` of Bring's curve as the
alternating sum of the Hochschild homology of the base curve,
`Σ_n (−1)^n dim HH_n(M₀) = 2 − 2g`. That reading has two cited inputs and one
identity, and this file proves the identity.

* **HKR at the level of dimensions** (Hochschild–Kostant–Rosenberg; Loday 3.4.4):
  for a smooth projective variety `X` of dimension `d`,
  `HH_n(X) ≅ ⊕_{j − i = n} H^i(X, Ω^j)`, so `dim HH_n = Σ_{j − i = n} h^{i,j}`.
  Encoded as the definition `hhDim`.
* **Hodge decomposition** (cited, not proved here): `Σ_{i,j} (−1)^{i+j} h^{i,j}`
  is the topological Euler characteristic `χ_eu(X)`. Encoded as the definition
  `hodgeEuler`; the identification with `χ_eu` is not a claim of this file.
* **The identity proved here** (`hhEuler_eq_hodgeEuler`):
  `Σ_n (−1)^n dim HH_n = Σ_{i,j} (−1)^{i+j} h^{i,j}`. The sign `(−1)^{j−i}` equals
  `(−1)^{i+j}` because the exponents differ by `2i` (`neg_one_zpow_sub`); re-indexing the
  double sum over the Hodge square is the rest.

For a curve (`d = 1`; `h^{0,0} = h^{1,1} = 1`, `h^{1,0} = h^{0,1} = g`) the sum is
`2 − 2g` (`hhEuler_curve`), and `−6` at `g = 4` (`hhEuler_bring`). The three
Hochschild dimensions of a curve are `2, g, g` (`hhDim_curve_*`), which is the
ledger `rem:three-euler-characteristics` quotes: `HH_0` alone has two components
and neither is `−6`.

None of this involves the quantum dimension `dim_q`, which is a different object.
Dimensions are integers; no `ℝ`, no numerics, no `sorry`.

-- Ref: [loday-1998] https://doi.org/10.1007/978-3-662-11389-9
-- Ref: [hkr-1962] https://doi.org/10.1090/S0002-9947-1962-0142598-8
-/

namespace QOU.Information

open Finset

/-- Hodge numbers `h i j = dim H^i(X, Ω^j)` of a `d`-dimensional variety, as a
function on `ℕ × ℕ` (entries with `i > d` or `j > d` are never read). -/
abbrev HodgeNumbers := ℕ → ℕ → ℤ

/-- HKR at the level of dimensions: `dim HH_n = Σ_{j − i = n} h^{i,j}`, the sum over
the `(d+1) × (d+1)` Hodge square. -/
def hhDim (d : ℕ) (h : HodgeNumbers) (n : ℤ) : ℤ :=
  ∑ i ∈ range (d + 1), ∑ j ∈ range (d + 1), if (j : ℤ) - i = n then h i j else 0

/-- The Euler characteristic of Hochschild homology, `Σ_{n = −d}^{d} (−1)^n dim HH_n`.
The sign `(−1)^n` for `n : ℤ` is `Int.negOnePow n`, coerced to `ℤ`. -/
def hhEuler (d : ℕ) (h : HodgeNumbers) : ℤ :=
  ∑ n ∈ Finset.Icc (-(d : ℤ)) d, ((Int.negOnePow n : ℤˣ) : ℤ) * hhDim d h n

/-- The Hodge Euler characteristic `Σ_{i,j} (−1)^{i+j} h^{i,j}`. The Hodge
decomposition identifies it with `χ_eu(X)`; that identification is cited, not
proved here. -/
def hodgeEuler (d : ℕ) (h : HodgeNumbers) : ℤ :=
  ∑ i ∈ range (d + 1), ∑ j ∈ range (d + 1), (-1 : ℤ) ^ (i + j) * h i j

/-- `(−1)^{j − i} = (−1)^{i + j}` in `ℤ`: the two exponents differ by `2i`. -/
theorem neg_one_zpow_sub (i j : ℕ) :
    ((Int.negOnePow ((j : ℤ) - i) : ℤˣ) : ℤ) = (-1 : ℤ) ^ (i + j) := by
  have h : Int.negOnePow ((j : ℤ) - i) = Int.negOnePow ((i + j : ℕ) : ℤ) := by
    rw [Int.negOnePow_eq_iff]
    exact ⟨-(i : ℤ), by push_cast; ring⟩
  rw [h, Int.coe_negOnePow_natCast]

/-- **The alternating sum over Hochschild homology is the Hodge Euler characteristic**
(sorry-free). Re-index `Σ_n Σ_{j − i = n}` as `Σ_{i,j}` and apply `neg_one_zpow_sub`. -/
theorem hhEuler_eq_hodgeEuler (d : ℕ) (h : HodgeNumbers) :
    hhEuler d h = hodgeEuler d h := by
  unfold hhEuler hhDim hodgeEuler
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun i hi => ?_)
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [Finset.sum_eq_single ((j : ℤ) - i)]
  · simp [neg_one_zpow_sub]
  · intro n _ hn
    simp [Ne.symm hn]
  · intro hnot
    exfalso
    apply hnot
    rw [Finset.mem_Icc]
    have hi' := Finset.mem_range.1 hi
    have hj' := Finset.mem_range.1 hj
    omega

/-! ## Curves -/

/-- The Hodge numbers of a smooth projective curve of genus `g`:
`h^{0,0} = h^{1,1} = 1` and `h^{1,0} = h^{0,1} = g` (Serre duality). -/
def curveHodge (g : ℤ) : HodgeNumbers := fun i j =>
  if i = 0 ∧ j = 0 then 1
  else if i = 1 ∧ j = 1 then 1
  else if (i = 1 ∧ j = 0) ∨ (i = 0 ∧ j = 1) then g
  else 0

/-- `dim HH_0 = h^{0,0} + h^{1,1} = 2`: the rank and the point class. -/
theorem hhDim_curve_zero (g : ℤ) : hhDim 1 (curveHodge g) 0 = 2 := by
  have _ : curveHodge g 0 0 = 1 := rfl
  have _ : curveHodge g 1 1 = 1 := rfl
  simp [hhDim, curveHodge, Finset.sum_range_succ]

/-- `dim HH_1 = h^{0,1}(Ω¹) = h^{0,1}`, read as `H^0(Ω^1)`: `g`. -/
theorem hhDim_curve_one (g : ℤ) : hhDim 1 (curveHodge g) 1 = g := by
  have _ : curveHodge g 0 1 = g := rfl
  have _ : curveHodge g 0 0 = 1 := rfl
  simp [hhDim, curveHodge, Finset.sum_range_succ]

/-- `dim HH_{−1} = h^{1,0}`, read as `H^1(𝒪)`: `g`. -/
theorem hhDim_curve_neg_one (g : ℤ) : hhDim 1 (curveHodge g) (-1) = g := by
  have _ : curveHodge g 1 0 = g := rfl
  have _ : curveHodge g 0 0 = 1 := rfl
  simp [hhDim, curveHodge, Finset.sum_range_succ]

/-- **For a curve of genus `g` the Hochschild Euler characteristic is `2 − 2g`.** -/
theorem hhEuler_curve (g : ℤ) : hhEuler 1 (curveHodge g) = 2 - 2 * g := by
  rw [hhEuler_eq_hodgeEuler]
  simp [hodgeEuler, curveHodge, Finset.sum_range_succ]
  ring

/-- **Bring's curve, `g = 4`: `−6`.** The `−6` of `lem:brings-euler-characteristic`
is this alternating sum, not a trace. -/
theorem hhEuler_bring : hhEuler 1 (curveHodge 4) = -6 := by
  rw [hhEuler_curve]; norm_num

/-- **Total Hochschild dimension of a curve vs. alternating Euler characteristic (`qou-9w89`).**
The ungraded total dimension `dim HH_{-1} + dim HH_0 + dim HH_1` equals `2 + 2g`
(strictly positive for `g ≥ 0`), separating the unsigned dimension sum from the
alternating Euler characteristic `2 - 2g`. -/
theorem hhDim_curve_total (g : ℤ) :
    hhDim 1 (curveHodge g) (-1) + hhDim 1 (curveHodge g) 0 + hhDim 1 (curveHodge g) 1 =
      2 + 2 * g := by
  rw [hhDim_curve_neg_one, hhDim_curve_zero, hhDim_curve_one]
  ring

/-- **Conditional HKR dimension identification (`qou-9w89`, §3b-cond).**
Carries the hypothesis that an abstractly defined Hochschild dimension profile
`hhActual : ℤ → ℤ` agrees with the Hodge diagonal sum `hhDim d h` on `[-d, d]`. -/
class HKRDimensionConjecture (d : ℕ) (h : HodgeNumbers) (hhActual : ℤ → ℤ) : Prop where
  /-- HKR graded-dimension identification on the support `[-d, d]`. -/
  dim_eq : ∀ n ∈ Finset.Icc (-(d : ℤ)) d, hhActual n = hhDim d h n

/-- Under `[HKRDimensionConjecture d h hhActual]`, the alternating sum of `hhActual`
over `[-d, d]` equals the Hodge Euler characteristic `hodgeEuler d h`. -/
theorem actual_hhEuler_eq_hodgeEuler (d : ℕ) (h : HodgeNumbers) (hhActual : ℤ → ℤ)
    [hk : HKRDimensionConjecture d h hhActual] :
    (∑ n ∈ Finset.Icc (-(d : ℤ)) d, ((Int.negOnePow n : ℤˣ) : ℤ) * hhActual n) =
      hodgeEuler d h := by
  rw [← hhEuler_eq_hodgeEuler d h]
  change (∑ n ∈ Finset.Icc (-(d : ℤ)) d, ((Int.negOnePow n : ℤˣ) : ℤ) * hhActual n) =
    ∑ n ∈ Finset.Icc (-(d : ℤ)) d, ((Int.negOnePow n : ℤˣ) : ℤ) * hhDim d h n
  refine Finset.sum_congr rfl (fun n hn => ?_)
  rw [hk.dim_eq n hn]

end QOU.Information
