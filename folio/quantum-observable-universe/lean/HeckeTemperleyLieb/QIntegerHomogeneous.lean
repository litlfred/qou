import Mathlib.Tactic
import MathlibExt.HomogeneousCoordinates
import HeckeTemperleyLieb.QHookDimensionBalanced
import HeckeTemperleyLieb.QIntegerCanonical

/-!
# The two q-integer conventions are two charts of one binary form

Issue #9083, part 2. `QOU.MathlibExt.QIntegerCanonical` keeps two named conventions,
the balanced `qIntBal` and the geometric `qIntGeo`, and warns that mixing them is a
recurring bug (bean `qou-lksc`). Both are restrictions of the binary form

  `qIntHom z w n = h_{n-1}(z, w) = ∑_{i<n} zⁱ w^{n-1-i}`

of `QOU.Mass.HomogeneousCoordinates`:

* `qIntGeo_eq_qIntHom` — the geometric convention is the chart `w = 1`;
* `qIntBal_eq_qIntHom` — the balanced convention is the chart `z w = 1`, evaluated at
  `(q, q⁻¹)` (away from `q − q⁻¹ = 0`, where `qIntBal` is a `0/0` quotient);
* `qIntBal_eq_twist_of_homogeneous` — the corpus twist `qIntBal_eq_twist` re-derived:
  it is homogeneity of degree `n − 1`, since `(q, q⁻¹) = q⁻¹ · (q², 1)`;
* `qFactBal_eq_centering` — the factorial form for **every** `n`:
  `[n]_q!^bal = q^{−n(n−1)/2} · ∏_{k ≤ n} [k]_{q²}^geo`, the identity
  `PoincareCenteringOfQ3` records as "checked n = 1..6". The exponent `n(n−1)/2` is
  the sum of the per-factor degrees `k − 1`.
-/

namespace QOU.Mass.QIntegerHomogeneous

open QOU.Mass.HomogeneousCoordinates

variable {R : Type*} [Field R]

/-- The geometric convention is the chart `w = 1`. -/
theorem qIntGeo_eq_qIntHom (Q : R) (n : ℕ) :
    QOU.QInteger.qIntGeo Q n = qIntHom Q 1 n := by
  rw [qIntHom_one]; rfl

/-- The balanced convention is the binary form at `(q, q⁻¹)`. -/
theorem qIntBal_eq_qIntHom {q : R} (h : q - q⁻¹ ≠ 0) (n : ℕ) :
    QOU.QInteger.qIntBal q n = qIntHom q q⁻¹ n := by
  show QOU.Mass.QHookDimensionBalanced.qIntBal q n = _
  unfold QOU.Mass.QHookDimensionBalanced.qIntBal
  rw [div_eq_iff h, mul_comm, sub_mul_qIntHom]

/-- Homogeneity at `(q, q⁻¹) = q⁻¹ · (q², 1)`. -/
theorem qIntHom_inv_twist {q : R} (hq : q ≠ 0) (n : ℕ) :
    qIntHom q q⁻¹ n = q⁻¹ ^ (n - 1) * qIntHom (q ^ 2) 1 n := by
  rw [← qIntHom_smul]
  congr 1
  · field_simp
  · ring

/-- **The corpus twist, re-derived from homogeneity.** Same statement and hypotheses
as `QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist`. -/
theorem qIntBal_eq_twist_of_homogeneous (q : R) (n : ℕ)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    QOU.QInteger.qIntBal q n = q⁻¹ ^ (n - 1) * QOU.QInteger.qIntGeo (q ^ 2) n := by
  rw [qIntBal_eq_qIntHom (QOU.Mass.QHookDimensionBalanced.sub_inv_ne_zero hq hq2),
    qIntGeo_eq_qIntHom, qIntHom_inv_twist hq]

/-- **Poincaré centering for every `n`.** The balanced q-factorial is the geometric
q-factorial in `q²`, centred by `q^{−n(n−1)/2}`. -/
theorem qFactBal_eq_centering (q : R) (n : ℕ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    QOU.QInteger.qFactBal q n
      = q⁻¹ ^ (n * (n - 1) / 2) * ∏ k ∈ Finset.range n, QOU.QInteger.qIntGeo (q ^ 2) (k + 1) := by
  unfold QOU.QInteger.qFactBal
  simp_rw [qIntBal_eq_twist_of_homogeneous q _ hq hq2, Finset.prod_mul_distrib,
    Finset.prod_pow_eq_pow_sum, Nat.add_sub_cancel, Finset.sum_range_id]

end QOU.Mass.QIntegerHomogeneous
