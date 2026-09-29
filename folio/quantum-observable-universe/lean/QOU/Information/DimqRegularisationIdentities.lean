import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# The exact identities behind the two regularisations of `dim_q(𝒪_q(SU(2)))`

`computations/audits/dimq_regularisation_schemes_probe.py` records what the two
standard regularisations of the divergent Peter–Weyl sum

  `dim_q(A) = Σ_{m ≥ 1} [m]_q² = (1/u²) Σ_{m ≥ 1} (q^{2m} + q^{-2m} − 2)`,  `u = q − q⁻¹`,

give.  Each scheme reduces to an **exact rational identity in `q`**, and those
identities are what this file proves — over an arbitrary field, with the
non-vanishing of every denominator as an explicit hypothesis.

* **ζ-scheme.**  Continuing the two geometric series, `Σ q^{2m} ↦ q²/(1 − q²)`
  and `Σ q^{−2m} ↦ q⁻²/(1 − q⁻²)`, the two pieces sum to `−1`
  (`zeta_geometric_pair_eq_neg_one`), so with `Σ 1 ↦ ζ(0) = −1/2` the
  numerator is `−1 − 2ζ(0) = 0` **for every `q`**.  The analytic continuation
  itself (that these are the ζ-regularised values) is the cited convention;
  only the algebra is proved here.
* **Hadamard finite part.**  Dropping the pole `−2t/(1 − t)` at `t = 1` leaves
  `−1/u²`.  `hadamard_eq_neg_six_iff` says this equals `−6` exactly when
  `u² = 1/6`, i.e. never at the substrate parameter (`u(q₀)² ≈ 0.0437`, probe).
* **The fundamental object is finite.**  `qint_two` is `[2]_q = q + q⁻¹`,
  the value `tr(id_V) = dim_q(V)` takes on the fundamental `V`.

Nothing here selects a scheme, and nothing here derives `−6`.
-/

namespace QOU.Information.DimqRegularisation

variable {K : Type*} [Field K]

/-- The two continued geometric series sum to `−1`:
`q²/(1 − q²) + q⁻²/(1 − q⁻²) = −1` whenever `q ≠ 0` and `q² ≠ 1`. -/
theorem zeta_geometric_pair_eq_neg_one (q : K) (hq : q ≠ 0) (h₁ : q ^ 2 - 1 ≠ 0) :
    q ^ 2 / (1 - q ^ 2) + (q ^ 2)⁻¹ / (1 - (q ^ 2)⁻¹) = -1 := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h₁' : 1 - q ^ 2 ≠ 0 := by
    intro h; apply h₁; linear_combination -h
  have h₂ : 1 - (q ^ 2)⁻¹ = (q ^ 2 - 1) / q ^ 2 := by
    field_simp
  have h₂' : 1 - (q ^ 2)⁻¹ ≠ 0 := by
    rw [h₂]; exact div_ne_zero h₁ hq2
  rw [h₂, div_div_eq_mul_div, inv_mul_cancel₀ hq2, div_add_div _ _ h₁' h₁,
    div_eq_iff (mul_ne_zero h₁' h₁)]
  ring

/-- Hence the ζ-regularised numerator `(−1) − 2·ζ(0)` vanishes once `ζ(0)` is
taken as `−1/2`: the scheme gives `dim_q^ζ(A) = 0` for every admissible `q`.
(`CharZero` is needed only to know that `2 ≠ 0`.) -/
theorem zeta_numerator_eq_zero [CharZero K] (q : K) (hq : q ≠ 0) (h₁ : q ^ 2 - 1 ≠ 0) :
    q ^ 2 / (1 - q ^ 2) + (q ^ 2)⁻¹ / (1 - (q ^ 2)⁻¹) - 2 * (-1 / 2 : K) = 0 := by
  rw [zeta_geometric_pair_eq_neg_one q hq h₁]
  norm_num

/-- The Hadamard finite part `−1/u²` equals `−6` iff `u² = 1/6`. -/
theorem hadamard_eq_neg_six_iff [CharZero K] (u : K) (hu : u ≠ 0) :
    -1 / u ^ 2 = -6 ↔ u ^ 2 = 1 / 6 := by
  have hu2 : u ^ 2 ≠ 0 := pow_ne_zero 2 hu
  have h6 : (6 : K) ≠ 0 := by norm_num
  constructor
  · intro h
    rw [div_eq_iff hu2] at h
    rw [eq_div_iff h6]
    linear_combination h
  · intro h
    rw [h]
    norm_num

/-- `[2]_q = (q² − q⁻²)/(q − q⁻¹) = q + q⁻¹` — the quantum dimension of the
fundamental object, finite for every `q ≠ 0` with `q² ≠ 1` (equivalently
`q − q⁻¹ ≠ 0`). -/
theorem qint_two (q : K) (hq : q ≠ 0) (h₁ : q ^ 2 - 1 ≠ 0) :
    (q ^ 2 - (q ^ 2)⁻¹) / (q - q⁻¹) = q + q⁻¹ := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h₁' : -1 + q ^ 2 ≠ 0 := by
    intro h; apply h₁; linear_combination h
  field_simp
  ring

end QOU.Information.DimqRegularisation
