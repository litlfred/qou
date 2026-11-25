/-
  Where the photon lives: first-order structure of `def:photon` in `H₃(q)`.

  The photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner ruling 2026-11-18/20,
  `QOU.Photon.photon`). This file proves five small facts used in
  `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md`.

  1. **The augmentation jet is torsion** (`hecke_sub_mul_self`, `sub_eq_smul_sq`).
     At the trivial augmentation `ε(σ) = q` the generator `σ − q` satisfies
     `(σ − q)² = −[2]_q·(σ − q)`. Over a field with `[2]_q ≠ 0` the generator is
     therefore in `I²`, so the first-order jet `I/I²` of `H_n(q)` at an augmentation
     vanishes. The photon does not live in `I/I²`: that space is zero.
  2. **A photon is not in `1 + ker ε`** (`augmentation_photon`): for an algebra map
     `ε` with `ε σ₀ = ε σ₁ = q`, `ε(γ) = 1 + q·φ₀ + q·φ₁ + φ₀₁`. So `γ − 1 ∈ ker ε`
     only on a hyperplane of colour weights.
  3. **The two-photon pairing breaks the σ₀ ↔ σ₁ symmetry** (`gram_vertex_asymmetry`,
     `gram_vertex_asymmetry_factor`). For any cyclic trace with the Markov property at
     the last strand, `t(σ₀·V) − t(σ₁·V) = h·(z² − hz − 1) = h·(z − q)(z + q⁻¹)`.
     The single-photon trace treats `φ₀` and `φ₁` alike; the pairing with the vertex
     does not, unless the trace is one of the two one-dimensional characters
     (`z = q` or `z = −q⁻¹`) or `h = 0`.
  4. **The trace parameter can be heard** (`audible_q`): over a field, if two values
     `q, q'` give the same `h = q − q⁻¹` and the same convention-D Markov parameter
     `z = q³/(q²+1)`, then `q = q'` or `q⁴ + 1 = 0`.

  The trace-form Gram matrix of the trace-free parts in the two-dimensional block is
  computed in `computations/probes/photon_jet_spectral/` and is not formalised here.

  Generic commutative ring `R` (§7c), except (4) and the field version of (1), which
  need division.

  -- Ref: [leitner2026] predicted-spectra, def:photon
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.StandardModel.Photon
import Mathlib.Algebra.Algebra.Hom
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Module

namespace QOU.PhotonJet

open QOU.Photon

section Torsion

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **Hecke torsion.** If `σ² = (q − q')σ + 1` with `q·q' = 1`, then
`(σ − q)² = −(q + q')·(σ − q)`. -/
theorem hecke_sub_mul_self {q q' : R} (hq : q * q' = 1) {σ : A}
    (H : σ * σ = (q - q') • σ + 1) :
    (σ - algebraMap R A q) * (σ - algebraMap R A q)
      = -((q + q') • (σ - algebraMap R A q)) := by
  have hc : ∀ x : A, algebraMap R A q * x = q • x := fun x => (Algebra.smul_def q x).symm
  have hc' : ∀ x : A, x * algebraMap R A q = q • x := fun x => by
    rw [← Algebra.commutes, Algebra.smul_def]
  rw [sub_mul, mul_sub, mul_sub, H, hc, hc', hc, Algebra.algebraMap_eq_smul_one]
  have h1 : (1 : A) = (q * q') • (1 : A) := by rw [hq, one_smul]
  rw [smul_smul]
  conv_lhs => rw [h1]
  match_scalars <;> first | linear_combination q ^ 2 * hq | linear_combination (0 : R) * hq

end Torsion

section TorsionField

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- Over a field with `[2]_q = q + q⁻¹ ≠ 0`, the augmentation generator `σ − q` is a
multiple of its own square, so it lies in `I²`: the first-order jet `I/I²` at this
generator vanishes. -/
theorem sub_eq_smul_sq {q q' : K} (hq : q * q' = 1) (h2 : q + q' ≠ 0) {σ : A}
    (H : σ * σ = (q - q') • σ + 1) :
    σ - algebraMap K A q
      = (-(q + q')⁻¹) • ((σ - algebraMap K A q) * (σ - algebraMap K A q)) := by
  rw [hecke_sub_mul_self hq H, smul_neg, neg_smul, neg_neg, smul_smul,
    inv_mul_cancel₀ h2, one_smul]

end TorsionField

section Augmentation

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The augmentation of a photon.** -/
theorem augmentation_photon (ε : A →ₐ[R] R) {q q' : R} (hq : q * q' = 1)
    (σ₀ : A) (σ₁ : Aˣ) (h0 : ε σ₀ = q) (h1 : ε (σ₁ : A) = q) (c : Colour R) :
    ε (photon σ₀ σ₁ c) = 1 + q * c.phi0 + q * c.phi1 + c.phi01 := by
  have hinv : ε (↑σ₁⁻¹ : A) = q' := by
    have h := congrArg ε (Units.mul_inv σ₁)
    rw [map_mul, map_one, h1] at h
    calc ε (↑σ₁⁻¹ : A) = (q' * q) * ε (↑σ₁⁻¹ : A) := by rw [mul_comm q' q, hq, one_mul]
      _ = q' * (q * ε (↑σ₁⁻¹ : A)) := by ring
      _ = q' := by rw [h, mul_one]
  simp only [photon, vertex, map_add, map_one, map_smul, map_mul, h0, h1, hinv, smul_eq_mul]
  linear_combination c.phi01 * hq

end Augmentation

section Gram

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The two-photon pairing distinguishes σ₀ from σ₁ against the vertex.**
`a, b` are the images of `σ₀, σ₁`, the vertex is `a·b⁻¹ = a·(b − h)`; `t` is any
`R`-linear cyclic trace with `t 1 = 1`, `t a = z` and the Markov rule `t(x·b) = z·t(x)`
at `x = a·a`. -/
theorem gram_vertex_asymmetry {h z : R} {a b : A}
    (Ha : a * a = h • a + 1) (Hb : b * b = h • b + 1)
    (t : A →ₗ[R] R) (hcyc : ∀ x y : A, t (x * y) = t (y * x))
    (h1 : t 1 = 1) (ha : t a = z) (hmk : t (a * a * b) = z * t (a * a)) :
    t (a * (a * (b - h • 1))) - t (b * (a * (b - h • 1))) = h * (z ^ 2 - h * z - 1) := by
  have hbb : b * (b - h • 1) = 1 := by
    rw [mul_sub, Hb, mul_smul_comm, mul_one]; abel
  have e1 : t (a * (a * (b - h • 1))) = (z - h) * (h * z + 1) := by
    have hm : t (a * a) = h * z + 1 := by
      rw [Ha, map_add, map_smul, ha, h1, smul_eq_mul]
    rw [← mul_assoc, mul_sub, map_sub, mul_smul_comm, mul_one, map_smul, hmk, hm, smul_eq_mul]
    ring
  have e2 : t (b * (a * (b - h • 1))) = z := by
    have hbb' : (b - h • 1) * b = 1 := by
      rw [sub_mul, Hb, smul_mul_assoc, one_mul]; abel
    rw [hcyc, mul_assoc, hbb', mul_one, ha]
  rw [e1, e2]
  ring

/-- With `h = q − q'` and `q·q' = 1`: `z² − hz − 1 = (z − q)(z + q')`. The asymmetry
vanishes exactly at the two one-dimensional characters `z = q`, `z = −q'`. -/
theorem gram_vertex_asymmetry_factor {q q' z : R} (hq : q * q' = 1) :
    z ^ 2 - (q - q') * z - 1 = (z - q) * (z + q') := by
  linear_combination hq

end Gram

section Audible

variable {K : Type*} [Field K]

/-- **The aether parameter is audible.** Under convention D the single-photon response
`1 + z(φ₀+φ₁) + z(z−h)φ₀₁` fixes `h` and `z`; these fix `q` up to `q⁴ + 1 = 0`. -/
theorem audible_q {q p : K} (hq : q ≠ 0) (hp : p ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hp2 : p ^ 2 + 1 ≠ 0)
    (hh : q - q⁻¹ = p - p⁻¹) (hz : q ^ 3 / (q ^ 2 + 1) = p ^ 3 / (p ^ 2 + 1)) :
    q = p ∨ q ^ 4 + 1 = 0 := by
  -- from `hh`: (q - p)(q p + 1) = 0
  have h1 : (q - p) * (q * p + 1) = 0 := by
    field_simp at hh
    linear_combination hh
  rcases mul_eq_zero.mp h1 with h | h
  · exact Or.inl (sub_eq_zero.mp h)
  · right
    -- p = -q⁻¹
    have hpq : p = -q⁻¹ := by
      field_simp
      linear_combination h
    subst hpq
    have hz' : q ^ 3 * ((-q⁻¹) ^ 2 + 1) = (-q⁻¹) ^ 3 * (q ^ 2 + 1) := by
      rw [div_eq_div_iff hq2 hp2] at hz
      exact hz
    have key : (q ^ 4 + 1) * (q ^ 2 + 1) = 0 := by
      field_simp at hz'
      linear_combination hz'
    rcases mul_eq_zero.mp key with h' | h'
    · exact h'
    · exact absurd h' hq2

end Audible

end QOU.PhotonJet
