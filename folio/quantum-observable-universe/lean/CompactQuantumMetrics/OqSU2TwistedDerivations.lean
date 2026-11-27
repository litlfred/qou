import CompactQuantumMetrics.OqSU2Characters

/-!
# Twisted derivations of `O_q(SU(2))` and the jump of `Aut⊗(τ)` at `q = 1`

Consequences of the character classification (`OqSU2Characters.lean`), all over a generic
commutative ring or field, with no analysis and no empirical input.

## Twisted derivations (the "which character?" gap of `OqSU2Coproduct.lean`)

A left-invariant vector field of a covariant calculus is `X_φ = (id ⊗ φ)Δ` for a functional
`φ` with the twisted Leibniz rule `φ(xy) = φ(x) χ(y) + ε(x) φ(y)` (`leftInvOp_leibniz`).
`χ` must be a character, so by `char_eq_diagChar` it is `χ_u = (u, 0, 0, u⁻¹)` whenever
`q² − 1` is a unit: the twist is a point of the torus `Aut⊗(τ)`.

* `twistedDerivation_rels`: for twist `χ_u`, `φ(1) = 0`, `φ(δ) = −u⁻¹ φ(α)`,
  `(1 − q u) φ(β) = 0` and `(1 − q u) φ(γ) = 0`.
* `twistedDerivation_offDiag_forces`: over a field, a twisted derivation that is non-zero
  on `β` or on `γ` has `u = q⁻¹`. The off-diagonal fields of a calculus are therefore
  twisted by exactly the point `χ_{q⁻¹}` whose two-sided action is the Haar modular
  automorphism (`modularAut_eq_twoSided`). A diagonal (Cartan) field leaves `u` free.

## Haar is fixed by its modular automorphism

* `haarState_modularAut`: `h ∘ σ = h` for `q² ≠ 1`, from `σ = L_{χ_{q⁻¹}} ∘ R_{χ_{q⁻¹}}` and
  one-sided invariance under every character.

## The classical limit is a jump of `Aut⊗(τ)`

* `points_jump_at_one`: over any field `K`, for every `ε ≠ 0` with `ε ≠ −2` no character of
  `O_{1+ε}(SU(2))` is non-zero on `β`, while `O_1(SU(2))` has one. The points of `Aut⊗(τ)`
  are the torus at every `q = 1 + ε` with `ε ≠ 0`, however small, and jump to a group
  containing a unipotent point at `q = 1`. Taking `K` non-archimedean (the surreals,
  `ε` infinitesimal) shows a standard part cannot recover the classical points: the classical
  limit passes through the Hopf algebra (the coend of `τ`), not through groups of points.

No empirical value enters any proof.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {R : Type*} [CommRing R]

section twisted

variable (q u : Rˣ)

/-- **Relations satisfied by a `χ_u`-twisted derivation.** If
`φ(xy) = φ(x) χ_u(y) + ε(x) φ(y)` for all `x, y`, then `φ(1) = 0`, `φ(δ) = −u⁻¹ φ(α)`, and
`(1 − q u) φ(β) = 0 = (1 − q u) φ(γ)`. -/
theorem twistedDerivation_rels (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y : OqSU2 R q,
      φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y) :
    φ 1 = 0 ∧
    φ (δ q) = -(((u⁻¹ : Rˣ) : R) * φ (α q)) ∧
    (1 - (q : R) * u) * φ (β q) = 0 ∧
    (1 - (q : R) * u) * φ (γ q) = 0 := by
  have hχα : diagCharAlgHom q u (α q) = (u : R) := by simp [diagCharAlgHom]
  have hχβ : diagCharAlgHom q u (β q) = 0 := by simp [diagCharAlgHom]
  have hχγ : diagCharAlgHom q u (γ q) = 0 := by simp [diagCharAlgHom]
  have hχδ : diagCharAlgHom q u (δ q) = ((u⁻¹ : Rˣ) : R) := by simp [diagCharAlgHom]
  have hεα : counit (R := R) q (α q) = 1 := by simp [counit, diagCharAlgHom]
  have hεβ : counit (R := R) q (β q) = 0 := by simp [counit, diagCharAlgHom]
  have hεγ : counit (R := R) q (γ q) = 0 := by simp [counit, diagCharAlgHom]
  have hεδ : counit (R := R) q (δ q) = 1 := by simp [counit, diagCharAlgHom]
  -- `φ(1) = φ(1)·1 + 1·φ(1)`
  have h1 : φ 1 = 0 := by
    have := hφ 1 1
    simp only [mul_one, map_one, one_mul] at this
    calc φ 1 = (φ 1 + φ 1) - φ 1 := by ring
      _ = φ 1 - φ 1 := by rw [← this]
      _ = 0 := sub_self _
  refine ⟨h1, ?_, ?_, ?_⟩
  · -- `αδ − q βγ = 1`, and `φ(βγ) = 0`.
    have hbg := hφ (β q) (γ q)
    rw [hχγ, hεβ] at hbg
    have had := hφ (α q) (δ q)
    rw [hχδ, hεα] at had
    have hdet := congrArg φ (rel_det_left (R := R) q)
    rw [map_sub, map_smul, smul_eq_mul, had, hbg, h1] at hdet
    linear_combination hdet
  · -- `αβ = q βα`.
    have hab := hφ (α q) (β q)
    rw [hχβ, hεα] at hab
    have hba := hφ (β q) (α q)
    rw [hχα, hεβ] at hba
    have hrel := congrArg φ (rel_ab (R := R) q)
    rw [map_smul, smul_eq_mul, hab, hba] at hrel
    linear_combination hrel
  · -- `αγ = q γα`.
    have hag := hφ (α q) (γ q)
    rw [hχγ, hεα] at hag
    have hga := hφ (γ q) (α q)
    rw [hχα, hεγ] at hga
    have hrel := congrArg φ (rel_ag (R := R) q)
    rw [map_smul, smul_eq_mul, hag, hga] at hrel
    linear_combination hrel

end twisted

section field

variable {K : Type*} [Field K] (q u : Kˣ)

/-- **Off-diagonal fields are twisted by the pivotal point.** Over a field, a
`χ_u`-twisted derivation that is non-zero on `β` or on `γ` has `u = q⁻¹`. -/
theorem twistedDerivation_offDiag_forces (φ : OqSU2 K q →ₗ[K] K)
    (hφ : ∀ x y : OqSU2 K q,
      φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y)
    (hoff : φ (β q) ≠ 0 ∨ φ (γ q) ≠ 0) : u = q⁻¹ := by
  obtain ⟨-, -, hb, hg⟩ := twistedDerivation_rels q u φ hφ
  have hqu : 1 - (q : K) * u = 0 := by
    rcases hoff with h | h
    · exact (mul_eq_zero.mp hb).resolve_right h
    · exact (mul_eq_zero.mp hg).resolve_right h
  apply Units.ext
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  simp only [Units.val_inv_eq_inv_val]
  field_simp
  linear_combination -hqu

/-- **Haar is fixed by its modular automorphism**, `h ∘ σ = h`, for `q² ≠ 1`. -/
theorem haarState_modularAut (hq : (q : K) ^ 2 ≠ 1) (x : OqSU2 K q) :
    haarState q (modularAut q x) = haarState q x := by
  rw [modularAut_eq_twoSided, AlgHom.comp_apply, haarState_leftTrans_char q hq,
    haarState_rightTrans_char q hq]

end field

section jump

variable {K : Type*} [Field K]

/-- **The points of `Aut⊗(τ)` jump at `q = 1`.** For every `ε ≠ 0, −2` in a field `K`
(with `1 + ε` a unit), every character of `O_{1+ε}(SU(2))` vanishes on `β`; at `q = 1` there
is a character that does not. Over a non-archimedean `K` this holds for infinitesimal `ε`. -/
theorem points_jump_at_one :
    (∀ (q : Kˣ), (q : K) ≠ 1 → (q : K) ≠ -1 →
      ∀ χ : OqSU2 K q →ₐ[K] K, χ (β q) = 0) ∧
    ∃ χ : OqSU2 K (1 : Kˣ) →ₐ[K] K, χ (β 1) ≠ 0 := by
  refine ⟨fun q h1 hm1 χ => ?_, exists_nondiag_char_at_one⟩
  have hu : IsUnit ((q : K) ^ 2 - 1) := by
    apply Ne.isUnit
    have : (q : K) ^ 2 - 1 = ((q : K) - 1) * ((q : K) + 1) := by ring
    rw [this]
    exact mul_ne_zero (sub_ne_zero.mpr h1) (fun h => hm1 (eq_neg_of_add_eq_zero_left h))
  exact (char_offdiag_zero hu χ).1

end jump

end QOU.AlgebraicSubstrate.OqSU2
