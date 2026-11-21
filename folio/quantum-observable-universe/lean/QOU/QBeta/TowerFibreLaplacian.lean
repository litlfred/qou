/-
# The fibre-side q-Laplacian has leading eigenvalue exactly `1`

Bean `qou-y3bm`. The E₀ tower factor `1/(1 - ℏ_q²)` used by
`qbeta_e0.tower_summed` is the `λ₁ = 1` member of the family
`1/(1 - ℏ_q² λ₁)` (`QOU.QBeta.towerSum_iterated_eq_simple_iff`). The note in
`TowerGeometricSum.lean` (2026-11-15, issue #8053) argued `λ₁ = 1` in prose: the
`q`-Laplacian `Δ_q = -(z D_q)²` satisfies `Δ_q zᵏ = -[k]_q² zᵏ` "exactly — no
length occurs". This file PROVES that sentence, from the difference quotient,
over any field.

## What is proved here (sorry-free, generic `[Field R]`, §7c)

* `qEuler_zpow` — `z · D_q(wᵏ)(z) = [k]_q · zᵏ` for every `k : ℤ`, where
  `D_q f (z) = (f(qz) - f(q⁻¹z)) / ((q - q⁻¹) z)` and `[k]_q` is the balanced
  `q`-integer. A computation from the difference quotient, not a definition.
* `qLaplacian_zpow` — `Δ_q(wᵏ)(z) = -[k]_q² · zᵏ`.
* `qInt_one` and `qLaplacian_leading` — on the leading mode `k = 1` the
  eigenvalue is `-1` for EVERY `q` with `q ≠ q⁻¹`: no further parameter occurs.
* `towerFactor_fibre` (over `ℝ`) — feeding that eigenvalue's magnitude into the
  iterated tower gives exactly the implemented factor `(1 - ℏ_q²)⁻¹`.

## What is NOT proved, and is still open in `qou-y3bm`

The decay proposition (`prop:brane-tower-q-laplacian-decay`, Step 1) uses the
ARCHIMEDEAN eigenvalue `[k]_q² ℏ_q / L_q²`, i.e. this fibre eigenvalue times the
unit-restoring factor `ℏ_q / L_q²`. So `λ₁ = 1` now reduces to ONE placement
statement:

  (P) the residual `Δ^{(n)}` in the E₀ tower `Σ ℏ_q^{2n} Δ^{(n)}` is the n-th
      iterate of the FIBRE operator proved here, not of its archimedean image.

(P) is not proved here, and nothing in this file should be cited as proving it.
Two further premises of the tower factor are untouched: that E₀'s residual is
this iterate at all (the corpus has a second definition of `Δ^{(n)}`, free minus
atom binding, `prop:jet-tower-convergence`), and the uniform bound, which
`DeltaMaxUniformBound.lean` carries as the structure field `per_level_bound`.

The `q`-derivative and `q`-integers are the standard ones of quantum calculus
(Kac and Cheung, *Quantum Calculus*, Ch. 1); nothing here depends on a citation,
since every statement is proved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import QOU.QBeta.TowerGeometricSum

namespace QOU.QBeta.TowerFibre

section Generic

variable {R : Type*} [Field R]

/-- The balanced `q`-integer `[k]_q = (qᵏ - q⁻ᵏ) / (q - q⁻¹)`, for `k : ℤ`. -/
def qInt (q : R) (k : ℤ) : R := (q ^ k - q⁻¹ ^ k) / (q - q⁻¹)

/-- The symmetric `q`-derivative `D_q f (z) = (f(qz) - f(q⁻¹z)) / ((q - q⁻¹) z)`. -/
def qDeriv (q : R) (f : R → R) (z : R) : R :=
  (f (q * z) - f (q⁻¹ * z)) / ((q - q⁻¹) * z)

/-- The fibre `q`-Laplacian `Δ_q f = -(z D_q)(z D_q) f`. -/
def qLaplacian (q : R) (f : R → R) (z : R) : R :=
  -(z * qDeriv q (fun w => w * qDeriv q f w) z)

/-- `q ≠ q⁻¹` forces `q ≠ 0` (at `q = 0` both sides are `0`). -/
theorem ne_zero_of_sub_inv_ne_zero {q : R} (hq : q - q⁻¹ ≠ 0) : q ≠ 0 := by
  rintro rfl
  simp at hq

/-- **The `q`-Euler operator on a monomial**, from the difference quotient:
`z · D_q(wᵏ)(z) = [k]_q · zᵏ`. -/
theorem qEuler_zpow (q z : R) (hq : q - q⁻¹ ≠ 0) (hz : z ≠ 0) (k : ℤ) :
    z * qDeriv q (fun w => w ^ k) z = qInt q k * z ^ k := by
  have hq0 : q ≠ 0 := ne_zero_of_sub_inv_ne_zero hq
  unfold qDeriv qInt
  simp only [mul_zpow]
  field_simp

/-- **The fibre `q`-Laplacian on a monomial**: `Δ_q(wᵏ)(z) = -[k]_q² zᵏ`.
The only parameter in the eigenvalue is `q`. -/
theorem qLaplacian_zpow (q z : R) (hq : q - q⁻¹ ≠ 0) (hz : z ≠ 0) (k : ℤ) :
    qLaplacian q (fun w => w ^ k) z = -(qInt q k ^ 2 * z ^ k) := by
  have hq0 : q ≠ 0 := ne_zero_of_sub_inv_ne_zero hq
  have hqz : q * z ≠ 0 := mul_ne_zero hq0 hz
  have hqiz : q⁻¹ * z ≠ 0 := mul_ne_zero (inv_ne_zero hq0) hz
  unfold qLaplacian
  -- evaluate the inner Euler operator at the two shifted points
  have e1 := qEuler_zpow q (q * z) hq hqz k
  have e2 := qEuler_zpow q (q⁻¹ * z) hq hqiz k
  have hin : qDeriv q (fun w => w * qDeriv q (fun w => w ^ k) w) z
      = qInt q k * qDeriv q (fun w => w ^ k) z := by
    unfold qDeriv at e1 e2 ⊢
    simp only at e1 e2 ⊢
    rw [e1, e2]
    ring
  rw [hin, ← mul_assoc, mul_comm z, mul_assoc, qEuler_zpow q z hq hz k]
  ring

/-- `[1]_q = 1` whenever `q ≠ q⁻¹`. -/
theorem qInt_one (q : R) (hq : q - q⁻¹ ≠ 0) : qInt q 1 = 1 := by
  unfold qInt
  simp only [zpow_one]
  exact div_self hq

/-- **The leading mode has eigenvalue exactly `-1`, for every admissible `q`.**
`Δ_q(w)(z) = -z`: the magnitude `λ₁ = [1]_q² = 1` carries no free scale. -/
theorem qLaplacian_leading (q z : R) (hq : q - q⁻¹ ≠ 0) (hz : z ≠ 0) :
    qLaplacian q (fun w => w ^ (1 : ℤ)) z = -(1 * z) := by
  rw [qLaplacian_zpow q z hq hz 1, qInt_one q hq, zpow_one, one_pow]

end Generic

section Archimedean

/-- **The fibre eigenvalue reproduces the implemented tower factor exactly.**
If the tower's residual is the iterate of the fibre `q`-Laplacian (premise (P)
in the module docstring — NOT proved here), its leading-mode ratio is
`[1]_q² = 1` and the iterated tower factor `(1 - ℏ_q² λ₁)⁻¹` is
`(1 - ℏ_q²)⁻¹`, the value `qbeta_e0.tower_summed` uses. -/
theorem towerFactor_fibre {q : ℝ} (hq : q - q⁻¹ ≠ 0) :
    (1 - QOU.QBeta.hbarQ q ^ 2 * qInt q 1 ^ 2)⁻¹ = (1 - QOU.QBeta.hbarQ q ^ 2)⁻¹ := by
  rw [qInt_one q hq, one_pow, mul_one]

end Archimedean

end QOU.QBeta.TowerFibre
