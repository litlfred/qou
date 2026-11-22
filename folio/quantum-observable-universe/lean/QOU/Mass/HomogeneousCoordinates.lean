import Mathlib.Tactic
import Mathlib.Algebra.Ring.GeomSum

/-!
# Homogeneous-coordinate lemmas

Issue #9083. These are the statements the corpus currently proves or states in an
affine chart, restated in homogeneous coordinates where the chart bookkeeping
(`z ≠ 0`, the point at infinity, the normalisation `x₀ + x₁ = C`) disappears.

1. `bring_h3_certificate` — on Bring's curve (`p₁ = p₂ = p₃ = 0` in five
   coordinates) the complete homogeneous cubic `h₃(x₂, x₀, x₁)` vanishes: an
   explicit ideal certificate, so the colour cubic is cut out homogeneously with
   no `x₀ + x₁ = C` normalisation.
2. `h3_nonsingular` — the plane cubic `h₃(X,z,w) = 0` has no singular point: the
   three partials vanish only at `0`.
3. `affineChartOrigin_glue` — from the quantum-plane relation `y x = q (x y)` with
   `q` central, the charts `z = y x⁻¹`, `w = y⁻¹ x` glue by `z w = q⁻¹`
   (`rem:affine-chart-origin-of-i-and-q`). The ordering is the content:
   `chart_glue_trivial` shows `(y x⁻¹)(x y⁻¹) = 1` in any group, so the glue
   coefficient is fixed by the homogeneous relation, not by the affine charts.
4. `qIntHom` — the binary form `h_{n-1}(z,w)`; symmetry, homogeneity, and the
   telescoping identity, with no `q ≠ 0` hypotheses.
-/

namespace QOU.Mass.HomogeneousCoordinates

section Bring
variable {R : Type*} [CommRing R]

/-- The complete homogeneous symmetric cubic in three variables. -/
def h3 (X z w : R) : R :=
  X^3 + X^2*z + X^2*w + X*z^2 + X*z*w + X*w^2 + z^3 + z^2*w + z*w^2 + w^3

/-- Power sum of five coordinates. -/
def p (x₀ x₁ x₂ x₃ x₄ : R) (n : ℕ) : R := x₀^n + x₁^n + x₂^n + x₃^n + x₄^n

/-- **Bring certificate** (ring identity): `6·h₃(x₂,x₀,x₁) = A·p₁ + B·p₂ + 2·p₃`. -/
theorem bring_h3_certificate (x₀ x₁ x₂ x₃ x₄ : R) :
    6 * h3 x₂ x₀ x₁ =
      (x₀^2 + 2*x₀*x₁ + 2*x₀*x₂ - x₀*x₃ - x₀*x₄ + x₁^2 + 2*x₁*x₂ - x₁*x₃ - x₁*x₄
          + x₂^2 - x₂*x₃ - x₂*x₄ - 2*x₃^2 + 2*x₃*x₄ - 2*x₄^2) * p x₀ x₁ x₂ x₃ x₄ 1
      + 3 * (x₀ + x₁ + x₂) * p x₀ x₁ x₂ x₃ x₄ 2
      + 2 * p x₀ x₁ x₂ x₃ x₄ 3 := by
  unfold h3 p; ring

/-- On Bring's curve, the colour cubic holds in homogeneous form. -/
theorem h3_of_bring {K : Type*} [Field K] [CharZero K] {x₀ x₁ x₂ x₃ x₄ : K}
    (h1 : p x₀ x₁ x₂ x₃ x₄ 1 = 0) (h2 : p x₀ x₁ x₂ x₃ x₄ 2 = 0)
    (h3' : p x₀ x₁ x₂ x₃ x₄ 3 = 0) : h3 x₂ x₀ x₁ = 0 := by
  have h := bring_h3_certificate x₀ x₁ x₂ x₃ x₄
  rw [h1, h2, h3'] at h
  have : (6 : K) ≠ 0 := by norm_num
  simpa [this] using h

/-- Dehomogenisation: `h₃(X, z, 1)` is the corpus colour cubic. -/
theorem h3_dehom (X z : R) :
    h3 X z 1 = X^3 + (z+1)*X^2 + (z^2+z+1)*X + (z^3+z^2+z+1) := by
  unfold h3; ring

end Bring

section Smooth
variable {K : Type*} [Field K]

/-- The three partial derivatives of `h₃`. -/
def dX (X z w : K) : K := 3*X^2 + 2*X*z + 2*X*w + z^2 + z*w + w^2
def dz (X z w : K) : K := X^2 + 2*X*z + X*w + 3*z^2 + 2*z*w + w^2
def dw (X z w : K) : K := X^2 + X*z + 2*X*w + z^2 + 2*z*w + 3*w^2

/-- Certificate: `X⁴` lies in the ideal of the partials. -/
theorem X4_cert (X z w : K) :
    120 * X^4 =
      (45*X^2 - 25*X*w - 20*X*z + 5*w^2 + 34*w*z + 15*z^2) * dX X z w
      - (15*X^2 + 10*X*w + 5*w^2 + 11*w*z + 5*z^2) * dz X z w
      - 2 * w * (-5*X + 3*z) * dw X z w := by
  unfold dX dz dw; ring

theorem dX_perm (X z w : K) : dX z X w = dz X z w := by unfold dX dz; ring
theorem dz_perm (X z w : K) : dz z X w = dX X z w := by unfold dX dz; ring
theorem dw_perm (X z w : K) : dw z X w = dw X z w := by unfold dw; ring
theorem dX_perm' (X z w : K) : dX w z X = dw X z w := by unfold dX dw; ring
theorem dz_perm' (X z w : K) : dz w z X = dz X z w := by unfold dz; ring
theorem dw_perm' (X z w : K) : dw w z X = dX X z w := by unfold dX dw; ring

private theorem first_zero [CharZero K] {X z w : K}
    (h1 : dX X z w = 0) (h2 : dz X z w = 0) (h3 : dw X z w = 0) : X = 0 := by
  have h := X4_cert X z w
  rw [h1, h2, h3] at h
  have : (120 : K) * X^4 = 0 := by simpa using h
  have hX : X^4 = 0 := by
    rcases mul_eq_zero.mp this with h | h
    · norm_num at h
    · exact h
  exact pow_eq_zero_iff (by norm_num) |>.mp hX

/-- **The colour curve is a smooth plane cubic.** If all three partials of
`h₃` vanish at `(X,z,w)`, then `X = z = w = 0`; so no point of `ℙ²` is singular. -/
theorem h3_nonsingular [CharZero K] {X z w : K}
    (h1 : dX X z w = 0) (h2 : dz X z w = 0) (h3 : dw X z w = 0) :
    X = 0 ∧ z = 0 ∧ w = 0 := by
  refine ⟨first_zero h1 h2 h3, ?_, ?_⟩
  · exact first_zero (X := z) (z := X) (w := w)
      (by rw [dX_perm]; exact h2) (by rw [dz_perm]; exact h1) (by rw [dw_perm]; exact h3)
  · exact first_zero (X := w) (z := z) (w := X)
      (by rw [dX_perm']; exact h3) (by rw [dz_perm']; exact h2) (by rw [dw_perm']; exact h1)

end Smooth

section QuantumPlane
variable {G : Type*} [Group G]

/-- With the charts `z = y x⁻¹`, `w = x y⁻¹`, the glue is `1` in any group:
the formula `z w = q⁻¹` for this ordering is false. -/
theorem chart_glue_trivial (x y : G) : (y * x⁻¹) * (x * y⁻¹) = 1 := by group

/-- **Quantum-plane chart glue.** If `x y = q (y x)` with `q` central, then with
the charts `z = x⁻¹ y`, `w = x y⁻¹` the glue is `z w = q⁻¹`. -/
theorem quantumPlane_chart_glue {x y q : G} (hq : ∀ g : G, q * g = g * q)
    (hxy : x * y = q * (y * x)) : (x⁻¹ * y) * (x * y⁻¹) = q⁻¹ := by
  have h : y * x = q⁻¹ * (x * y) := by rw [hxy]; group
  calc (x⁻¹ * y) * (x * y⁻¹) = x⁻¹ * (y * x) * y⁻¹ := by group
    _ = x⁻¹ * (q⁻¹ * (x * y)) * y⁻¹ := by rw [h]
    _ = q⁻¹ * (x⁻¹ * x * y * y⁻¹) := by
        have hq' : ∀ g : G, q⁻¹ * g = g * q⁻¹ := fun g => by
          have := hq g
          calc q⁻¹ * g = q⁻¹ * (g * q) * q⁻¹ := by group
            _ = q⁻¹ * (q * g) * q⁻¹ := by rw [this]
            _ = g * q⁻¹ := by group
        rw [show x⁻¹ * (q⁻¹ * (x * y)) * y⁻¹ = (x⁻¹ * q⁻¹) * (x * y) * y⁻¹ by group,
          ← hq' x⁻¹]
        group
    _ = q⁻¹ := by group

/-- **The chart glue of `rem:affine-chart-origin-of-i-and-q`.** With the quantum-plane
relation `y x = q (x y)` and `q` central, the Reeb chart `z = y x⁻¹` and the antipodal
chart `w = y⁻¹ x` satisfy `z w = q⁻¹`. -/
theorem affineChartOrigin_glue {x y q : G} (hq : ∀ g : G, q * g = g * q)
    (hyx : y * x = q * (x * y)) : (y * x⁻¹) * (y⁻¹ * x) = q⁻¹ := by
  -- `x⁻¹ y⁻¹ = (y x)⁻¹ = (x y)⁻¹ q⁻¹ = y⁻¹ x⁻¹ q⁻¹`, and `q⁻¹` is central.
  have hinv : x⁻¹ * y⁻¹ = y⁻¹ * x⁻¹ * q⁻¹ := by
    have : (y * x)⁻¹ = (q * (x * y))⁻¹ := by rw [hyx]
    simpa [mul_inv_rev, mul_assoc] using this
  have hq' : ∀ g : G, q⁻¹ * g = g * q⁻¹ := fun g => by
    have := hq g
    calc q⁻¹ * g = q⁻¹ * (g * q) * q⁻¹ := by group
      _ = q⁻¹ * (q * g) * q⁻¹ := by rw [this]
      _ = g * q⁻¹ := by group
  calc (y * x⁻¹) * (y⁻¹ * x) = y * (x⁻¹ * y⁻¹) * x := by group
    _ = y * (y⁻¹ * x⁻¹ * q⁻¹) * x := by rw [hinv]
    _ = x⁻¹ * (q⁻¹ * x) := by group
    _ = q⁻¹ := by rw [hq' x]; group

end QuantumPlane

section QInt
variable {R : Type*} [CommRing R]

/-- The binary form `h_{n-1}(z,w) = ∑_{i<n} zⁱ w^{n-1-i}`. -/
def qIntHom (z w : R) (n : ℕ) : R :=
  ∑ i ∈ Finset.range n, z ^ i * w ^ (n - 1 - i)

/-- Bar symmetry is the swap of the two homogeneous coordinates. -/
theorem qIntHom_symm (z w : R) (n : ℕ) : qIntHom z w n = qIntHom w z n := by
  unfold qIntHom
  rw [← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun i hi => ?_
  have hi := Finset.mem_range.mp hi
  rw [mul_comm]
  congr 2; omega

/-- Homogeneity of degree `n - 1`. -/
theorem qIntHom_smul (c z w : R) (n : ℕ) :
    qIntHom (c * z) (c * w) n = c ^ (n - 1) * qIntHom z w n := by
  unfold qIntHom
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  have hi := Finset.mem_range.mp hi
  have hc : c ^ (n - 1) = c ^ i * c ^ (n - 1 - i) := by rw [← pow_add]; congr 1; omega
  rw [mul_pow, mul_pow, hc]; ring

/-- Telescoping: `(z − w) · h_{n-1}(z,w) = zⁿ − wⁿ`. -/
theorem sub_mul_qIntHom (z w : R) (n : ℕ) :
    (z - w) * qIntHom z w n = z ^ n - w ^ n := by
  unfold qIntHom
  rw [← Commute.geom_sum₂_mul (Commute.all z w) n, mul_comm]

/-- The geometric convention is the chart `w = 1`. -/
theorem qIntHom_one (Q : R) (n : ℕ) :
    qIntHom Q 1 n = ∑ i ∈ Finset.range n, Q ^ i := by
  simp [qIntHom]

/-- The balanced-to-geometric twist, for every `n`, from homogeneity alone:
`h(q, q⁻¹) = q⁻¹^(n-1) · h(q², 1)` for a unit `q`. -/
theorem qIntHom_twist (q : Rˣ) (n : ℕ) :
    qIntHom (q : R) (↑q⁻¹) n = (↑q⁻¹ : R) ^ (n - 1) * qIntHom ((q : R) ^ 2) 1 n := by
  rw [← qIntHom_smul]
  congr 1
  · rw [sq, ← mul_assoc, Units.inv_mul, one_mul]
  · simp

end QInt

end QOU.Mass.HomogeneousCoordinates
