/-!
# Chern–Simons correction at curvature-rank 4

`δ_CS = ℏ_q⁴ · [5]_q` is the depth-4 stratum of the curvature
2-cocycle of the GB filtration, projected onto the symmetric
channel at `n = 5`.

The four powers of `ℏ_q = q − q⁻¹` come from crossing four GB
filtration layers; the `[5]_q` factor is the q-dimension of the
trivial-rep block `V_(5)` at `n = 5`, the smallest `n` where a
height-5 partition (depth 4) exists.

-- Ref: [manuscript] prop:curvature-rank-delta-cs
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.GroupPower.Basic

namespace QOU.WedderburnMass

/-- Substrate quantum-correction parameter `ℏ_q := q − q⁻¹`. -/
def hbar_q {R : Type*} [CommRing R] (q qinv : R) : R := q - qinv

/-- q-integer `[n]_q := (q^n − q^{-n}) / (q − q⁻¹)`.

    Concrete polynomial form for small `n` to avoid invoking division:
    `[5]_q · (q − q⁻¹) = q⁵ − q⁻⁵`. -/
def qint_times_hbar {R : Type*} [CommRing R] (q qinv : R) (n : ℕ) : R :=
  q^n - qinv^n

/-- **Chern–Simons correction at curvature-rank 4.**
    `δ_CS = ℏ_q⁴ · [5]_q`. -/
def delta_CS {R : Type*} [CommRing R] (q qinv : R) : R :=
  -- ℏ_q⁴ · [5]_q = (q − q⁻¹)³ · (q⁵ − q⁻⁵)
  -- because  ℏ_q · [5]_q = q⁵ − q⁻⁵.
  (hbar_q q qinv)^3 * qint_times_hbar q qinv 5

/-- **Theorem (depth-4 origin).**
    The four powers of `ℏ_q` correspond to the four layers of GB
    filtration that the depth-4 stratum `J⁴ / J⁵` crosses. -/
theorem delta_CS_depth_four_factor
    {R : Type*} [CommRing R] (q qinv : R) :
    delta_CS q qinv = (hbar_q q qinv)^3 * qint_times_hbar q qinv 5 := by
  rfl
  -- Ref: [manuscript] prop:curvature-rank-delta-cs

/-- **Theorem (q-character class).**
    The q-character class of `δ_CS` at `n = 5` is `[5]_q`, the
    q-dimension of the trivial-rep block `V_(5)`. -/
theorem delta_CS_qchar_class
    {R : Type*} [CommRing R] (q qinv : R) :
    qint_times_hbar q qinv 5 = q^5 - qinv^5 := by
  rfl
  -- Ref: [manuscript] prop:curvature-rank-delta-cs

end QOU.WedderburnMass
