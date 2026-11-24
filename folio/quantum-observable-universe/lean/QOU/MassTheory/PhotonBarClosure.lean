/-
  Bar involution on the photon (audit 2026-11-21-proton-q3-kl-coordinate, Round 6).

  Setting. `A` is an `R`-algebra with units `σ₀, σ₁` obeying the Hecke relation in the
  form `σᵢ⁻¹ = σᵢ - h` (`h = q - q⁻¹`). The bar involution is a ring map `b : A → A`,
  semilinear over a ring map `θ : R → R` (`q ↦ q⁻¹`, so `θ h = -h`), with `b σᵢ = σᵢ⁻¹`.
  No relation beyond these hypotheses is used. Generic commutative ring (§7c).

  Results.
  * `bar_photon`: `b γ(φ) = s·1 + (θφ₀ + hθφ₀₁)σ₀ + (θφ₁ - hθφ₀₁)σ₁ + θφ₀₁·σ₀σ₁⁻¹`
    with `s = 1 - h(θφ₀ + θφ₁)`: the photon family is closed under bar up to the scale `s`
    (`bar_photon_eq_smul`); a chiral photon maps to a photon exactly (`bar_chiral`).
  * `bar_vertex`: `b(σ₀σ₁⁻¹) = σ₀⁻¹σ₁ = σ₀σ₁⁻¹ + hσ₀ - hσ₁`.
  * With `{1, σ₀, σ₁, σ₀σ₁⁻¹}` linearly independent and `h` a non-zero-divisor, strict bar
    invariance forces `φ₀ + φ₁ = 0` (`phi_sum_zero_of_bar_fixed`), no nonzero chiral photon
    is bar-fixed (`chiral_bar_fixed_iff`), and the vertex is not bar-fixed.
  * Characters `χ` with `χ σ₀ = χ σ₁` (the trivial and sign characters) take the value
    `1 + φ₀₁` on every photon with `φ₀ + φ₁ = 0`; any two such characters agree on every
    finite product of such photons, so no such product is a nonzero multiple of an element
    killed by one character and not the other (`no_multiple_of_split`).
  * The three-dimensional weight-space representation separates `(σ₀⁻¹σ₁)³` from
    `(σ₀σ₁⁻¹)³` (`bar_borromean_ne`), so `b V³ ≠ V³` in `H₃(q)`.

  -- Ref: [leitner2026] def:photon; audit Round 6
-/
import QOU.StandardModel.Photon
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

namespace QOU.MassTheory.PhotonBarClosure

open QOU.Photon

section Abstract

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- The bar image of a unit is the inverse of the bar image. -/
theorem bar_inv_unit (b : A →+* A) (σ : Aˣ) (hb : b σ = ↑σ⁻¹) : b ↑σ⁻¹ = σ := by
  have h1 : b ↑σ⁻¹ * ↑σ⁻¹ = 1 := by
    calc b ↑σ⁻¹ * ↑σ⁻¹ = b ↑σ⁻¹ * b ↑σ := by rw [hb]
      _ = b (↑σ⁻¹ * ↑σ) := (map_mul b _ _).symm
      _ = 1 := by rw [Units.inv_mul, map_one]
  calc b ↑σ⁻¹ = b ↑σ⁻¹ * (↑σ⁻¹ * ↑σ) := by rw [Units.inv_mul, mul_one]
    _ = (b ↑σ⁻¹ * ↑σ⁻¹) * ↑σ := by rw [mul_assoc]
    _ = σ := by rw [h1, one_mul]

/-- `σ₀⁻¹σ₁ = σ₀σ₁⁻¹ + hσ₀ - hσ₁` from `σᵢ⁻¹ = σᵢ - h`. -/
theorem inv_mul_eq (σ₀ σ₁ : Aˣ) (h : R)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1) :
    (↑σ₀⁻¹ : A) * σ₁ = vertex (σ₀ : A) σ₁ + h • (σ₀ : A) - h • (σ₁ : A) := by
  have e1 : (σ₁ : A) = ↑σ₁⁻¹ + h • 1 := by rw [hi1]; abel
  unfold vertex
  rw [hi0, e1, hi1]
  simp only [sub_mul, mul_add, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, smul_sub, smul_smul]
  abel

/-- The bar image of the chiral vertex. -/
theorem bar_vertex (b : A →+* A) (σ₀ σ₁ : Aˣ) (h : R)
    (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1) :
    b (vertex (σ₀ : A) σ₁) = vertex (σ₀ : A) σ₁ + h • (σ₀ : A) - h • (σ₁ : A) := by
  unfold vertex
  rw [map_mul, hb0, bar_inv_unit b σ₁ hb1]
  exact inv_mul_eq σ₀ σ₁ h hi0 hi1

/-- The bar-image colour. -/
def barColour (θ : R →+* R) (h : R) (c : Colour R) : Colour R :=
  ⟨θ c.phi0 + h * θ c.phi01, θ c.phi1 - h * θ c.phi01, θ c.phi01⟩

/-- The identity coefficient of the bar image. -/
def barScale (θ : R →+* R) (h : R) (c : Colour R) : R := 1 - h * (θ c.phi0 + θ c.phi1)

/-- **Bar on the photon.** `b γ(c) = γ(barColour c) + (s - 1)·1`. -/
theorem bar_photon (θ : R →+* R) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1) (c : Colour R) :
    b (photon (σ₀ : A) σ₁ c) =
      photon (σ₀ : A) σ₁ (barColour θ h c) + (barScale θ h c - 1) • (1 : A) := by
  have hv := bar_vertex b σ₀ σ₁ h hb0 hb1 hi0 hi1
  simp only [photon, map_add, map_one, hb, hb0, hb1, hv, barColour, barScale]
  rw [hi0, hi1]
  simp only [smul_sub, smul_add, smul_smul, add_smul, sub_smul]
  module

/-- Scaling the colour weights. -/
def Colour.smul (u : R) (c : Colour R) : Colour R := ⟨u * c.phi0, u * c.phi1, u * c.phi01⟩

/-- **Closure up to scale.** If `s` is a unit with inverse `u`, `b γ(c) = s • γ(u • c')`. -/
theorem bar_photon_eq_smul (θ : R →+* R) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1) (c : Colour R)
    (u : R) (hu : barScale θ h c * u = 1) :
    b (photon (σ₀ : A) σ₁ c) =
      barScale θ h c • photon (σ₀ : A) σ₁ (Colour.smul u (barColour θ h c)) := by
  rw [bar_photon θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1 c]
  set s := barScale θ h c
  simp only [photon, Colour.smul, smul_add, smul_smul]
  have e : ∀ x : R, s * (u * x) = x := fun x => by rw [← mul_assoc, hu, one_mul]
  rw [e, e, e]
  simp only [sub_smul, one_smul]
  abel

/-- **A chiral photon maps exactly to a photon:** `b γ(0,0,c) = γ(hθc, -hθc, θc)`. -/
theorem bar_chiral (θ : R →+* R) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1) (c : R) :
    b (photon (σ₀ : A) σ₁ ⟨0, 0, c⟩) = photon (σ₀ : A) σ₁ ⟨h * θ c, -(h * θ c), θ c⟩ := by
  rw [bar_photon θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1]
  simp [barColour, barScale, sub_eq_add_neg]

/-! ### Strict invariance, under linear independence of `{1, σ₀, σ₁, σ₀σ₁⁻¹}` -/

/-- Coefficients in an independent four-element family are determined. -/
theorem coeffs4 (v₀ v₁ v₂ v₃ : A) (hind : LinearIndependent R ![v₀, v₁, v₂, v₃])
    (a₀ a₁ a₂ a₃ b₀ b₁ b₂ b₃ : R)
    (he : a₀ • v₀ + a₁ • v₁ + a₂ • v₂ + a₃ • v₃ = b₀ • v₀ + b₁ • v₁ + b₂ • v₂ + b₃ • v₃) :
    a₀ = b₀ ∧ a₁ = b₁ ∧ a₂ = b₂ ∧ a₃ = b₃ := by
  have key := (Fintype.linearIndependent_iff.mp hind) ![a₀ - b₀, a₁ - b₁, a₂ - b₂, a₃ - b₃]
    (by
      have e : (a₀ - b₀) • v₀ + (a₁ - b₁) • v₁ + (a₂ - b₂) • v₂ + (a₃ - b₃) • v₃ = 0 := by
        have h0 := sub_eq_zero.mpr he
        rw [← h0]; simp only [sub_smul]; abel
      simpa [Fin.sum_univ_four] using e)
  refine ⟨?_, ?_, ?_, ?_⟩
  · exact sub_eq_zero.mp (by simpa using key 0)
  · exact sub_eq_zero.mp (by simpa using key 1)
  · exact sub_eq_zero.mp (by simpa using key 2)
  · exact sub_eq_zero.mp (by simpa using key 3)

/-- **Strict bar invariance forces `θφ₀ + θφ₁ = 0` and the three coefficient equations.** -/
theorem bar_fixed_coeffs (θ : R →+* R) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1)
    (hind : LinearIndependent R ![(1 : A), σ₀, σ₁, vertex (σ₀ : A) σ₁])
    (c : Colour R) (hfix : b (photon (σ₀ : A) σ₁ c) = photon (σ₀ : A) σ₁ c) :
    h * (θ c.phi0 + θ c.phi1) = 0 ∧ θ c.phi0 + h * θ c.phi01 = c.phi0 ∧
      θ c.phi1 - h * θ c.phi01 = c.phi1 ∧ θ c.phi01 = c.phi01 := by
  rw [bar_photon θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1] at hfix
  obtain ⟨k0, k1, k2, k3⟩ := coeffs4 _ _ _ _ hind
    (barScale θ h c) (θ c.phi0 + h * θ c.phi01) (θ c.phi1 - h * θ c.phi01) (θ c.phi01)
    1 c.phi0 c.phi1 c.phi01 (by
      have e : barScale θ h c • (1 : A) + (θ c.phi0 + h * θ c.phi01) • (σ₀ : A) +
          (θ c.phi1 - h * θ c.phi01) • (σ₁ : A) + θ c.phi01 • vertex (σ₀ : A) σ₁ =
          photon (σ₀ : A) σ₁ (barColour θ h c) + (barScale θ h c - 1) • (1 : A) := by
        simp only [photon, barColour, sub_smul, one_smul]; abel
      rw [e, hfix]; simp only [photon, one_smul])
  refine ⟨?_, k1, k2, k3⟩
  unfold barScale at k0
  linear_combination -k0

/-- With `h` a non-zero-divisor and `θ` injective, a bar-fixed photon has `φ₀ + φ₁ = 0`. -/
theorem phi_sum_zero_of_bar_fixed (θ : R →+* R) (hθ : Function.Injective θ) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hh : ∀ x : R, h * x = 0 → x = 0)
    (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1)
    (hind : LinearIndependent R ![(1 : A), σ₀, σ₁, vertex (σ₀ : A) σ₁])
    (c : Colour R) (hfix : b (photon (σ₀ : A) σ₁ c) = photon (σ₀ : A) σ₁ c) :
    c.phi0 + c.phi1 = 0 := by
  have := hh _ (bar_fixed_coeffs θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1 hind c hfix).1
  exact hθ (by rw [map_add, map_zero]; exact this)

/-- **No nonzero chiral photon is bar-fixed.** -/
theorem chiral_bar_fixed_iff (θ : R →+* R) (hθ : Function.Injective θ) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hh : ∀ x : R, h * x = 0 → x = 0)
    (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1)
    (hind : LinearIndependent R ![(1 : A), σ₀, σ₁, vertex (σ₀ : A) σ₁]) (c : R) :
    b (photon (σ₀ : A) σ₁ ⟨0, 0, c⟩) = photon (σ₀ : A) σ₁ ⟨0, 0, c⟩ ↔ c = 0 := by
  constructor
  · intro hfix
    have k := (bar_fixed_coeffs θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1 hind _ hfix).2.1
    simp only [map_zero, zero_add] at k
    exact hθ (by rw [map_zero]; exact hh _ k)
  · rintro rfl
    rw [bar_chiral θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1]; simp

/-- **The chiral vertex is not bar-fixed** (for `h ≠ 0` and independence). -/
theorem vertex_not_bar_fixed (b : A →+* A) (σ₀ σ₁ : Aˣ) (h : R) (hh0 : h ≠ 0)
    (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1)
    (hind : LinearIndependent R ![(1 : A), σ₀, σ₁, vertex (σ₀ : A) σ₁]) :
    b (vertex (σ₀ : A) σ₁) ≠ vertex (σ₀ : A) σ₁ := by
  intro hfix
  rw [bar_vertex b σ₀ σ₁ h hb0 hb1 hi0 hi1] at hfix
  obtain ⟨-, k1, -, -⟩ := coeffs4 _ _ _ _ hind 0 h (-h) 1 0 0 0 1 (by
    calc (0 : R) • (1 : A) + h • (σ₀ : A) + (-h) • (σ₁ : A) + (1 : R) • vertex (σ₀ : A) σ₁
        = vertex (σ₀ : A) σ₁ + h • (σ₀ : A) - h • (σ₁ : A) := by
          rw [zero_smul, one_smul, neg_smul]; abel
      _ = vertex (σ₀ : A) σ₁ := hfix
      _ = (0 : R) • (1 : A) + (0 : R) • (σ₀ : A) + (0 : R) • (σ₁ : A) +
            (1 : R) • vertex (σ₀ : A) σ₁ := by simp)
  exact hh0 k1

/-! ### Characters with `χ σ₀ = χ σ₁` (trivial and sign) -/

/-- A character with `χ σ₀ = χ σ₁ = t` takes `1 + t(φ₀ + φ₁) + φ₀₁` on the photon. -/
theorem char_photon (χ : A →ₐ[R] R) (σ₀ σ₁ : Aˣ) (t : R)
    (h0 : χ σ₀ = t) (h1 : χ σ₁ = t) (c : Colour R) :
    χ (photon (σ₀ : A) σ₁ c) = 1 + t * (c.phi0 + c.phi1) + c.phi01 := by
  have hinv : χ ↑σ₁⁻¹ * t = 1 := by
    rw [← h1, ← map_mul, Units.inv_mul, map_one]
  have hv : χ (vertex (σ₀ : A) σ₁) = 1 := by
    unfold vertex; rw [map_mul, h0, mul_comm]; exact hinv
  simp only [photon, map_add, map_one, map_smul, h0, h1, hv, smul_eq_mul]
  ring

/-- A photon with `φ₀ + φ₁ = 0` has the same value `1 + φ₀₁` under every such character. -/
theorem char_photon_of_sum_zero (χ : A →ₐ[R] R) (σ₀ σ₁ : Aˣ)
    (h01 : χ σ₀ = χ σ₁) (c : Colour R) (hc : c.phi0 + c.phi1 = 0) :
    χ (photon (σ₀ : A) σ₁ c) = 1 + c.phi01 := by
  rw [char_photon χ σ₀ σ₁ (χ σ₁) h01 rfl c, hc]; ring

/-- Two characters with `χ σ₀ = χ σ₁` agree on every product of photons with `φ₀ + φ₁ = 0`. -/
theorem chars_agree_on_products (χ₁ χ₂ : A →ₐ[R] R) (σ₀ σ₁ : Aˣ)
    (e1 : χ₁ σ₀ = χ₁ σ₁) (e2 : χ₂ σ₀ = χ₂ σ₁) (l : List (Colour R))
    (hl : ∀ c ∈ l, c.phi0 + c.phi1 = 0) :
    χ₁ (l.map (photon (σ₀ : A) σ₁)).prod = χ₂ (l.map (photon (σ₀ : A) σ₁)).prod := by
  induction l with
  | nil => simp
  | cons c l ih =>
    have hc := hl c (by simp)
    simp only [List.map_cons, List.prod_cons, map_mul]
    rw [char_photon_of_sum_zero χ₁ σ₀ σ₁ e1 c hc, char_photon_of_sum_zero χ₂ σ₀ σ₁ e2 c hc,
      ih (fun d hd => hl d (by simp [hd]))]

/-- **No product of such photons is a nonzero multiple of an element split by the characters.**
If `χ₁ x = 0` and `χ₂ x ≠ 0` (as for `x₋`: trivial `0`, sign `≠ 0`), then
`∏ γ(cᵢ) = λ • x` with all `φ₀ + φ₁ = 0` forces `λ = 0`. -/
theorem no_multiple_of_split [IsDomain R] (χ₁ χ₂ : A →ₐ[R] R) (σ₀ σ₁ : Aˣ)
    (e1 : χ₁ σ₀ = χ₁ σ₁) (e2 : χ₂ σ₀ = χ₂ σ₁) (l : List (Colour R))
    (hl : ∀ c ∈ l, c.phi0 + c.phi1 = 0) (x : A) (hx1 : χ₁ x = 0) (hx2 : χ₂ x ≠ 0)
    (lam : R) (hP : (l.map (photon (σ₀ : A) σ₁)).prod = lam • x) : lam = 0 := by
  have := chars_agree_on_products χ₁ χ₂ σ₀ σ₁ e1 e2 l hl
  rw [hP, map_smul, map_smul, hx1, smul_eq_mul, smul_eq_mul, mul_zero] at this
  exact (mul_eq_zero.mp this.symm).resolve_right hx2

/-- **The trivial and sign characters intertwine bar with `θ` on photons.** If `χ σ₀ = χ σ₁ = t`
and `θ t = t - h` (true for `t = q` and `t = -q⁻¹` when `h = q - q⁻¹`), then
`χ (b γ) = θ (χ γ)`. -/
theorem char_bar_photon (θ : R →+* R) (b : A →+* A)
    (hb : ∀ (r : R) (x : A), b (r • x) = θ r • b x)
    (σ₀ σ₁ : Aˣ) (h : R) (hb0 : b σ₀ = ↑σ₀⁻¹) (hb1 : b σ₁ = ↑σ₁⁻¹)
    (hi0 : (↑σ₀⁻¹ : A) = σ₀ - h • 1) (hi1 : (↑σ₁⁻¹ : A) = σ₁ - h • 1)
    (χ : A →ₐ[R] R) (t : R) (h0 : χ σ₀ = t) (h1 : χ σ₁ = t) (hθt : θ t = t - h)
    (c : Colour R) :
    χ (b (photon (σ₀ : A) σ₁ c)) = θ (χ (photon (σ₀ : A) σ₁ c)) := by
  rw [bar_photon θ b hb σ₀ σ₁ h hb0 hb1 hi0 hi1, map_add, char_photon χ σ₀ σ₁ t h0 h1,
    char_photon χ σ₀ σ₁ t h0 h1, map_smul, map_one, smul_eq_mul]
  simp only [barColour, barScale, map_add, map_mul, map_one, hθt]
  ring

end Abstract

/-! ### `b V³ ≠ V³` in the three-dimensional weight-space representation -/

section Concrete

open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-- The bar image `(σ₀⁻¹σ₁)³` of `V³ = (σ₀σ₁⁻¹)³`, on the `(2,1)` weight space. -/
def barBorromeanV3A (q : R) : Matrix (Fin 3) (Fin 3) R :=
  (A₁Inv q * A₂ q) * (A₁Inv q * A₂ q) * (A₁Inv q * A₂ q)

/-- The `(0,1)` entry of `(σ₀⁻¹σ₁)³ - (σ₀σ₁⁻¹)³` is `-(q² - 1)³(q⁴ + 1)/q⁵`. -/
theorem barBorromean_sub_apply (q : R) (hq : q ≠ 0) :
    (barBorromeanV3A q - borromeanV3A q) 0 1 = -((q ^ 2 - 1) ^ 3 * (q ^ 4 + 1)) / q ^ 5 := by
  simp [barBorromeanV3A, borromeanV3A, borromeanVA, A₁, A₂, A₁Inv, A₂Inv,
    Matrix.mul_apply]
  field_simp
  ring

/-- **`b V³ ≠ V³`** whenever `q² ≠ 1` and `q⁴ ≠ -1`. -/
theorem bar_borromean_ne (q : R) (hq : q ≠ 0) (h2 : q ^ 2 ≠ 1) (h4 : q ^ 4 + 1 ≠ 0) :
    barBorromeanV3A q ≠ borromeanV3A q := by
  intro he
  have := barBorromean_sub_apply q hq
  rw [he, sub_self, Matrix.zero_apply] at this
  have h2' : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h2
  have : (q ^ 2 - 1) ^ 3 * (q ^ 4 + 1) = 0 := by
    have hq5 : q ^ 5 ≠ 0 := pow_ne_zero _ hq
    field_simp at this
    linear_combination this
  rcases mul_eq_zero.mp this with h | h
  · exact h2' (pow_eq_zero_iff (by norm_num) |>.mp h)
  · exact h4 h

end Concrete

end QOU.MassTheory.PhotonBarClosure
