import Mathlib.Tactic

/-!
# QOU.BraidKnot.frobenius_antipode_unifies — Kazhdan–Lusztig bar-semilinear `σᵢ ↦ σᵢ⁻¹`

Canonical Lean for content block
[`conj:frobenius-antipode-unifies-chirality-and-tower`](../../../mass-theory/frobenius-antipode-unifies-chirality-and-tower.md).

## Group-level inverse vs. Hecke Kazhdan–Lusztig bar-semilinearity (`TN-6`)

1. **On the braid group `B_n` (or any `Group G`):** `S : g ↦ g⁻¹` is an involutive
   anti-homomorphism (`frobenius_antipode_unifies`).
2. **On the Iwahori–Hecke algebra `H_n(R, q)` (`σᵢ² = h σᵢ + 1`, `h = q - q⁻¹`):**
   - **No `R`-linear anti-endomorphism** sends `σᵢ ↦ σᵢ⁻¹` when `2h ≠ 0`:
     `hecke_rlinear_inv_obstruction` proves `(σᵢ⁻¹)² - h σᵢ⁻¹ - 1 = -(2h) σᵢ⁻¹`,
     so `no_rlinear_hecke_inv_antihom` forces `2h = 0` (`q = ±1` in char `≠ 2`).
   - **Kazhdan–Lusztig bar-semilinearity (`bar(q) = q⁻¹`, hence `bar(h) = -h`):**
     `kl_bar_preserves_hecke_quadratic` proves `(σᵢ⁻¹)² - (-h) σᵢ⁻¹ - 1 = 0`
     identically over any commutative ring `R`, and `KLBarInvolution` packages
     the bar-semilinear anti-involution fixing bar-self-dual combinations `x + bar x`.
   - **Markov trace intertwining:** under Convention D (`z_D(q) = q³/(q² + 1)`),
     `tr_M` is NOT invariant under `σᵢ ↦ σᵢ⁻¹`; instead
     `markovZ_inv_crossing_eq_bar` proves
     `tr_{M,q}(σᵢ⁻¹) = z_D(q) - (q - q⁻¹) = z_D(q⁻¹) = q⁻⁴ z_D(q)`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031 (bar involution on Hecke algebras)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/frobenius-antipode-unifies-chirality-and-tower.md
-/

namespace QOU.BraidKnot

/-- The group-level inverse map `g ↦ g⁻¹` on `B_n` (or the unit group of `H_n(R, q)`). -/
def frobeniusAntipode {G : Type*} [Group G] : G → G := fun g => g⁻¹

/-- **Generator inverse on `G`:** `S(σᵢ) = σᵢ⁻¹`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower (S(σᵢ) = σᵢ⁻¹)
theorem frobeniusAntipode_generator {G : Type*} [Group G] (σ : ℕ → G) (i : ℕ) :
    frobeniusAntipode (σ i) = (σ i)⁻¹ := rfl

/-- **Anti-homomorphism on `G`:** `S(a·b) = S(b)·S(a)`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower (S(ab) = S(b)S(a))
theorem frobeniusAntipode_antihom {G : Type*} [Group G] (a b : G) :
    frobeniusAntipode (a * b) = frobeniusAntipode b * frobeniusAntipode a := by
  unfold frobeniusAntipode
  exact mul_inv_rev a b

/-- **Involution on `G`:** `S(S g) = g`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower
theorem frobeniusAntipode_involutive {G : Type*} [Group G] (g : G) :
    frobeniusAntipode (frobeniusAntipode g) = g := by
  unfold frobeniusAntipode
  exact inv_inv g

/-- **Group-level synthesis statement** of `conj:frobenius-antipode-unifies-chirality-and-tower`. -/
-- Ref: [leitner2026] conj:frobenius-antipode-unifies-chirality-and-tower
theorem frobenius_antipode_unifies {G : Type*} [Group G] (σ : ℕ → G) :
    (∀ i, frobeniusAntipode (σ i) = (σ i)⁻¹) ∧
    (∀ a b : G, frobeniusAntipode (a * b)
        = frobeniusAntipode b * frobeniusAntipode a) :=
  ⟨fun i => frobeniusAntipode_generator σ i,
   fun a b => frobeniusAntipode_antihom a b⟩

/-! ## Kazhdan–Lusztig bar-semilinearity vs. impossible `R`-linearity on `H_n(R, q)` -/

/-- **Obstruction to `R`-linear `σ ↦ σ⁻¹` on `H_n(R, q)`.**
    If `σ * σ_inv = 1` and `σ ^ 2 - h * σ - 1 = 0` in a commutative ring `R`,
    evaluating the *untwisted* polynomial `X² - h X - 1` at `σ_inv` leaves the
    non-zero obstruction `-(2 * h) * σ_inv`. -/
-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
theorem hecke_rlinear_inv_obstruction {R : Type*} [CommRing R]
    (σ σ_inv h : R) (hinv : σ * σ_inv = 1) (hquad : σ ^ 2 - h * σ - 1 = 0) :
    σ_inv ^ 2 - h * σ_inv - 1 = -(2 * h) * σ_inv := by
  linear_combination -σ_inv ^ 2 * hquad + (σ * σ_inv + 1 - h * σ_inv) * hinv

/-- **No `R`-linear anti-endomorphism sends `σ ↦ σ⁻¹` unless `2h = 0`.** -/
theorem no_rlinear_hecke_inv_antihom {R : Type*} [CommRing R]
    (σ σ_inv h : R) (hinv : σ * σ_inv = 1) (hquad : σ ^ 2 - h * σ - 1 = 0)
    (h_rlin : σ_inv ^ 2 - h * σ_inv - 1 = 0) :
    2 * h = 0 := by
  have hobs : -(2 * h) * σ_inv = 0 := by
    rw [← hecke_rlinear_inv_obstruction σ σ_inv h hinv hquad, h_rlin]
  calc
    2 * h = -((-(2 * h) * σ_inv) * σ) + 2 * h * (1 - σ * σ_inv) := by ring
    _ = 0 := by rw [hobs, hinv]; ring

/-- **Kazhdan–Lusztig bar-semilinearity (`bar(h) = -h`) preserves the Hecke relation:**
    replacing `h` by `-h` and `σ` by `σ_inv` gives `σ_inv ^ 2 - (-h) * σ_inv - 1 = 0`
    unconditionally over any commutative ring `R`. -/
-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
theorem kl_bar_preserves_hecke_quadratic {R : Type*} [CommRing R]
    (σ σ_inv h : R) (hinv : σ * σ_inv = 1) (hquad : σ ^ 2 - h * σ - 1 = 0) :
    σ_inv ^ 2 - (-h) * σ_inv - 1 = 0 := by
  linear_combination -σ_inv ^ 2 * hquad + (σ * σ_inv + 1 - h * σ_inv) * hinv

/-- **Kazhdan–Lusztig bar-semilinear anti-involution** on an `R`-algebra `H`
    with coefficient bar involution `barR : R →+* R` (`barR q = q⁻¹`, `barR h = -h`). -/
structure KLBarInvolution (R : Type*) [CommRing R] (H : Type*) [Ring H] [Algebra R H] where
  /-- Coefficient involution `q ↦ q⁻¹` on `R`. -/
  barR : R →+* R
  barR_invol : ∀ r : R, barR (barR r) = r
  /-- Additive map `x ↦ x̄` on `H`. -/
  barH : H →+ H
  barH_invol : ∀ x : H, barH (barH x) = x
  barH_one : barH 1 = 1
  /-- Anti-multiplicativity `x * y ↦ ȳ * x̄`. -/
  barH_anti_mul : ∀ x y : H, barH (x * y) = barH y * barH x
  /-- `barR`-semilinearity `r • x ↦ barR(r) • x̄`. -/
  barH_semilinear : ∀ (r : R) (x : H), barH (r • x) = barR r • barH x

/-- Every combination `x + x̄` (such as `σᵢ + σᵢ⁻¹ = 2(σᵢ - h/2)`) is fixed by the
    Kazhdan–Lusztig bar involution. -/
theorem KLBarInvolution.sym_fixed {R : Type*} [CommRing R] {H : Type*} [Ring H] [Algebra R H]
    (B : KLBarInvolution R H) (x : H) :
    B.barH (x + B.barH x) = x + B.barH x := by
  rw [map_add, B.barH_invol, add_comm]

/-- **Convention-D Markov trace under crossing inversion (`σᵢ⁻¹ = σᵢ - h`):**
    `tr_{M,q}(σᵢ⁻¹) = z_D(q) - (q - q⁻¹) = z_D(q⁻¹) = q⁻⁴ z_D(q)`, NOT `z_D(q)`. -/
theorem markovZ_inv_crossing_eq_bar {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) = (q⁻¹) ^ 3 / ((q⁻¹) ^ 2 + 1) ∧
      q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) = (q⁻¹) ^ 4 * (q ^ 3 / (q ^ 2 + 1)) := by
  have h1q2 : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have hqi2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro h0
    apply hq2
    have hmul : q ^ 2 * ((q⁻¹) ^ 2 + 1) = 0 := by rw [h0, mul_zero]
    have hexp : q ^ 2 * ((q⁻¹) ^ 2 + 1) = 1 + q ^ 2 := by field_simp
    rw [hexp, add_comm] at hmul
    exact hmul
  constructor
  · field_simp; ring
  · field_simp; ring

end QOU.BraidKnot
