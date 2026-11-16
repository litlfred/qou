import QOU.MathlibExt.OcneanuTrace
import QOU.Mass.HeckeStokesEigenvalues
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic

/-!
# `HeckeMonodromy` — Step 2 of the canonical chain as a §3b conjecture class

Option **A** of `docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md`. Cheat-sheet §2a records
that Step 2 (geometry → `H_n(q)`) is *stipulated*: the curvature 2-form is defined to be the Hecke
quadratic `F(σ) = σ² − (q − q⁻¹)σ − 1`, so "flatness derives the Hecke relation" is a tautology, and
the geometry it cites (`prop:hecke-spectral-sequence`) has no declaration in `content/`.

This class is the honest restatement §2a asks for. **The conjecture** (primary, §3b-tax — no other
conjecture class among its binders): *the framework's flat connection on the complement of the
discriminant locus of the colour cubic has braid-group monodromy landing in the Hecke tower that
carries the Markov trace, its generators satisfy the Hecke quadratic and the braid relations, and
its classical shadow — under a ring map `ε` lying over the specialisation `q ↦ 1` — is the
Picard–Lefschetz involution measured in `colour_cubic_branch_monodromy_probe.py`.* The fields carry
exactly that content; nothing is `True`, nothing is empty.

**The base is a ring, not a field (restated 2026-11-15, issue #7992).** The tower is an algebra over
a commutative ring `R` (the model case is the Laurent ring `ℤ[q, q⁻¹]`) and `q : Rˣ`. The shadow
field says `ε(q) = 1`: the shadow is the specialisation `q ↦ 1`. The involution is then a theorem
(`shadow_involution`), not a field. The earlier form took `q` in a field `K` and asked for
`ε(g)² = 1` directly; over a field with `q − q⁻¹ ≠ 0` that forces the shadow ring to be zero
(`subsingleton_of_isUnit_h`), because a single algebra at fixed `q` cannot see `q = 1`. The
rank-one model `LaurentModel.laurentModel` shows the restated class has a nonzero shadow (`ℤ`).

**The KZ model case is derived, not assumed.** For the 𝔰𝔩₂ Knizhnik–Zamolodchikov connection
on two points, the `quad` and `shadow_involution` fields are theorems:
`QOU.Mass.KohnoTwoPoint.kzExchange_quad` and `kzExchange_shadow_involution` (sorry-free; the
`braid`/`far_comm` fields are vacuous for one generator). For `n ≥ 3` the braid relation needs
holonomy over configuration space (bean `qou-9634`); and that the substrate connection *is* KZ is
open (bean `qou-d0qq`). The polynomial `F(σ)` is the eigenvalue relation of the monodromy of a
flat connection; "curvature" in older text means this.

What the file **derives** from the class (sorry-free, unconditional given the instance):

* `hecke_factor` — the generator factors as `(g − q)(g + q⁻¹) = 0` in the algebra: the two
  Stokes/Hecke eigenvalues `q, −q⁻¹` of `QOU.Mass.HeckeStokes.stokes_curvature_factors` are now a
  *consequence* of the monodromy relation rather than the definition of a curvature;
* `shadow_involution` — each shadow generator is an involution, derived from `quad` and
  `ε(q) = 1`;
* `shadow_hecke_at_one` — the shadow satisfies the `q = 1` Hecke quadratic `(X − 1)(X + 1) = 0`;
* `shadow_kills_h` — `ε(h • g) = 0` with `h = q − q⁻¹`: the classical shadow *is* the `h = 0`
  specialisation, so the deformation parameter is exactly what the shadow forgets. This is the
  sense in which what remains stipulated is the deformation `1 ↦ q` and nothing else.

**What this does NOT do.** It does not construct the connection (option C) and it does not define
the forms `(α, β)` route D2 needs. `NaStokesKeystone.lean`'s docstring claim *"has curvature 2-form
`F(σ)`"* is, from here on, to be read as an instance of this class, not as a fact.

Base ring §7c: generic `CommRing R` with a unit `q`, generic `Ring A`/`Ring B` for the tower and
its shadow; nothing archimedean.

-- Ref: [leitner2026] docs/canonical-derivation-cheat-sheet.md §2a
-- Ref: [leitner2026] computations/probes/colour_cubic_branch_monodromy_probe.py
-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — the model theorem (KZ monodromy factors
--      through the Hecke algebra), for option C.
-/

namespace QOU.Mass

open QOU.MathlibExt.OcneanuTrace

/-- **Conjecture (Step 2 as monodromy).** For a Markov-trace tower `T : MarkovTrace R A` over a
commutative ring `R`, with generators `T.g i`, a unit `q : Rˣ`, and a ring map `ε : A →+* B`: the
generators are the monodromies of the substrate connection around the branch points of the colour
cubic, so they satisfy the Hecke quadratic with `h = q − q⁻¹` and the braid and far-commutation
relations of the braid group; and `ε` lies over the specialisation `q ↦ 1`, which makes each shadow
generator an involution (the Picard–Lefschetz transposition on the two colliding roots,
`shadow_involution`). -/
class HeckeMonodromy {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (T : MarkovTrace R A) (q : Rˣ) {B : Type*} [Ring B] (ε : A →+* B) : Prop where
  /-- The Hecke quadratic on every generator, with `h = q − q⁻¹`. -/
  quad : ∀ i, T.g i * T.g i = ((q : R) - ↑q⁻¹) • T.g i + 1
  /-- The braid relation between neighbours. -/
  braid : ∀ i, T.g i * T.g (i + 1) * T.g i = T.g (i + 1) * T.g i * T.g (i + 1)
  /-- Far commutation. -/
  far_comm : ∀ i j, i + 2 ≤ j → T.g i * T.g j = T.g j * T.g i
  /-- The shadow is the specialisation `q ↦ 1`. -/
  shadow_at_one : ε (algebraMap R A q) = 1

namespace HeckeMonodromy

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A) (q : Rˣ) {B : Type*} [Ring B] (ε : A →+* B)

/-- **The two Stokes/Hecke eigenvalues are a consequence.** Every generator factors as
`(g − q)(g + q⁻¹) = 0` in `A` — the algebra behind `stokes_curvature_factors`, now derived from
the monodromy hypothesis instead of stipulated as a curvature. -/
theorem hecke_factor [HeckeMonodromy T q ε] (i : ℕ) :
    (T.g i - algebraMap R A q) * (T.g i + algebraMap R A ↑q⁻¹) = 0 := by
  have hquad := HeckeMonodromy.quad (T := T) (q := q) (ε := ε) i
  rw [Algebra.smul_def, map_sub] at hquad
  have hc : algebraMap R A ↑q⁻¹ * T.g i = T.g i * algebraMap R A ↑q⁻¹ := Algebra.commutes _ _
  have hinv : algebraMap R A q * algebraMap R A ↑q⁻¹ = 1 := by
    rw [← map_mul, Units.mul_inv, map_one]
  calc (T.g i - algebraMap R A q) * (T.g i + algebraMap R A ↑q⁻¹)
      = T.g i * T.g i + T.g i * algebraMap R A ↑q⁻¹ - algebraMap R A q * T.g i
          - algebraMap R A q * algebraMap R A ↑q⁻¹ := by noncomm_ring
    _ = ((algebraMap R A q - algebraMap R A ↑q⁻¹) * T.g i + 1) + T.g i * algebraMap R A ↑q⁻¹
          - algebraMap R A q * T.g i - 1 := by rw [hquad, hinv]
    _ = 0 := by rw [← hc]; noncomm_ring

/-- The shadow also sends `q⁻¹` to `1`. -/
theorem shadow_at_one_inv [HeckeMonodromy T q ε] : ε (algebraMap R A ↑q⁻¹) = 1 := by
  have h : ε (algebraMap R A q) * ε (algebraMap R A ↑q⁻¹) = 1 := by
    rw [← map_mul, ← map_mul, Units.mul_inv, map_one, map_one]
  rwa [HeckeMonodromy.shadow_at_one (T := T), one_mul] at h

/-- **The shadow forgets exactly the deformation.** `ε((q − q⁻¹) • g) = 0`: the classical target
sees `h = 0`, i.e. the `q = 1` specialisation. What Step 2 leaves stipulated is therefore the
deformation `1 ↦ q` alone. -/
theorem shadow_kills_h [HeckeMonodromy T q ε] (i : ℕ) : ε (((q : R) - ↑q⁻¹) • T.g i) = 0 := by
  rw [Algebra.smul_def, map_mul, map_sub, map_sub, HeckeMonodromy.shadow_at_one (T := T),
    shadow_at_one_inv T q ε, sub_self, zero_mul]

/-- **The shadow is an involution (derived).** Push the Hecke quadratic through `ε`: the
`h • g` term dies (`shadow_kills_h`), leaving `ε(g)² = 1`. -/
theorem shadow_involution [HeckeMonodromy T q ε] (i : ℕ) : ε (T.g i) * ε (T.g i) = 1 := by
  have h := congrArg ε (HeckeMonodromy.quad (T := T) (q := q) (ε := ε) i)
  rwa [map_mul, map_add, shadow_kills_h T q ε, zero_add, map_one] at h

/-- The classical shadow satisfies the Hecke quadratic at `q = 1`: `(X − 1)(X + 1) = 0`. -/
theorem shadow_hecke_at_one [HeckeMonodromy T q ε] (i : ℕ) :
    (ε (T.g i) - 1) * (ε (T.g i) + 1) = 0 := by
  have h := shadow_involution T q ε i
  calc (ε (T.g i) - 1) * (ε (T.g i) + 1) = ε (T.g i) * ε (T.g i) - 1 := by noncomm_ring
    _ = 0 := by rw [h, sub_self]

/-- **Why the base must be a ring and not a field.** If `q − q⁻¹` is a unit of `R` (for instance
`R` a field and `q ≠ ±1`), then `ε` sends it both to a unit and, since `ε(q) = ε(q⁻¹) = 1`, to `0`,
so the shadow ring is zero. A tower at one fixed value of `q` cannot carry the `q = 1` shadow; the
parameter has to vary, as it does over `ℤ[q, q⁻¹]` (`LaurentModel.laurentModel`). This is the
defect of the earlier field-based form of this class. -/
theorem subsingleton_of_isUnit_h [HeckeMonodromy T q ε] (hq : IsUnit ((q : R) - ↑q⁻¹)) :
    Subsingleton B := by
  have h0 : ε (algebraMap R A ((q : R) - ↑q⁻¹)) = 0 := by
    rw [map_sub, map_sub, HeckeMonodromy.shadow_at_one (T := T), shadow_at_one_inv T q ε, sub_self]
  have hu : IsUnit (ε (algebraMap R A ((q : R) - ↑q⁻¹))) := (hq.map (algebraMap R A)).map ε
  rw [h0] at hu
  exact subsingleton_of_zero_eq_one (isUnit_zero_iff.mp hu)

/-! ### The shadow is a Coxeter representation

The probe finds the classical monodromy group to be `S₃`, generated by transpositions. Pushing the
three relations through `ε` shows why that is forced by the class: the shadow generators satisfy
the Coxeter presentation of the symmetric group — involutions, braid relation, far commutation — so
`ε ∘ ϱ` factors through `S_n` and is a permutation representation. -/

/-- The shadow satisfies the braid relation. -/
theorem shadow_braid [HeckeMonodromy T q ε] (i : ℕ) :
    ε (T.g i) * ε (T.g (i + 1)) * ε (T.g i) = ε (T.g (i + 1)) * ε (T.g i) * ε (T.g (i + 1)) := by
  have h := HeckeMonodromy.braid (T := T) (q := q) (ε := ε) i
  have := congrArg ε h
  simpa only [map_mul] using this

/-- The shadow satisfies far commutation. -/
theorem shadow_far_comm [HeckeMonodromy T q ε] (i j : ℕ) (hij : i + 2 ≤ j) :
    ε (T.g i) * ε (T.g j) = ε (T.g j) * ε (T.g i) := by
  have h := HeckeMonodromy.far_comm (T := T) (q := q) (ε := ε) i j hij
  have := congrArg ε h
  simpa only [map_mul] using this

/-- Each shadow generator is a unit, its own inverse (a transposition). -/
theorem shadow_isUnit [HeckeMonodromy T q ε] (i : ℕ) : IsUnit (ε (T.g i)) :=
  ⟨⟨ε (T.g i), ε (T.g i), shadow_involution T q ε i, shadow_involution T q ε i⟩, rfl⟩

/-- **Coxeter presentation.** The three relations of `S_n` on the shadow generators, bundled:
involution, braid, far commutation. This is the content of "the classical shadow is a
permutation representation", which the probe measured as `S₃` at `n = 3`. -/
theorem shadow_coxeter [HeckeMonodromy T q ε] :
    (∀ i, ε (T.g i) * ε (T.g i) = 1) ∧
    (∀ i, ε (T.g i) * ε (T.g (i + 1)) * ε (T.g i) = ε (T.g (i + 1)) * ε (T.g i) * ε (T.g (i + 1))) ∧
    (∀ i j, i + 2 ≤ j → ε (T.g i) * ε (T.g j) = ε (T.g j) * ε (T.g i)) :=
  ⟨shadow_involution T q ε, shadow_braid T q ε, shadow_far_comm T q ε⟩

end HeckeMonodromy

/-! ### A model with a nonzero shadow, over `ℤ[q, q⁻¹]`

The rank-one tower: `A = R = ℤ[q, q⁻¹]`, every generator is `q` (the trivial, "symmetric"
one-dimensional representation of the Hecke algebra, `q² = (q − q⁻¹) q + 1`), the trace is the
identity, and `ε : ℤ[q, q⁻¹] → ℤ` evaluates at `q = 1`. It satisfies every field of
`HeckeMonodromy`, and its shadow ring `ℤ` is not zero. So the restated class is consistent with a
nonzero shadow, which the field-based form was not. The model says nothing about the substrate
connection. -/

namespace HeckeMonodromy.LaurentModel

open LaurentPolynomial

/-- The Laurent ring `ℤ[q, q⁻¹]`. -/
abbrev R : Type := LaurentPolynomial ℤ

/-- The deformation parameter `q = T 1`, a unit with inverse `T (-1)`. -/
noncomputable def qU : Rˣ :=
  ⟨T 1, T (-1), by rw [← T_add]; simp, by rw [← T_add]; simp⟩

theorem qU_val : ((qU : Rˣ) : R) = T 1 := rfl

theorem qU_inv : ((qU⁻¹ : Rˣ) : R) = T (-1) := rfl

/-- The rank-one Markov-trace tower over `ℤ[q, q⁻¹]`. -/
noncomputable def tower : MarkovTrace R R where
  H := fun _ => ⊤
  H_mono := fun _ _ _ => le_rfl
  g := fun _ => T 1
  g_mem := fun _ => trivial
  ginv := fun _ => T (-1)
  ginv_mem := fun _ => trivial
  ginv_mul := fun _ => by rw [← T_add]; simp
  mul_ginv := fun _ => by rw [← T_add]; simp
  tr := LinearMap.id
  tr_mul_comm := fun a b => mul_comm a b
  tr_one := rfl
  z := T 1
  zinv := T (-1)
  markov := fun _ a _ => mul_comm a _
  markov_inv := fun _ a _ => mul_comm a _

/-- Evaluation at `q = 1`. -/
noncomputable def evalOne : R →+* ℤ := eval₂ (RingHom.id ℤ) 1

theorem evalOne_T (n : ℤ) : evalOne (T n) = 1 := by
  simp [evalOne, eval₂_T]

instance laurentModel : HeckeMonodromy tower qU evalOne where
  quad := fun _ => by
    show T 1 * T 1 = ((qU : R) - ↑qU⁻¹) • T 1 + 1
    rw [qU_val, qU_inv, smul_eq_mul, sub_mul, ← T_add, ← T_add]
    simp [T_zero]
  braid := fun _ => rfl
  far_comm := fun _ _ _ => rfl
  shadow_at_one := evalOne_T 1

/-- The model's shadow ring is not zero. -/
theorem shadow_nontrivial : Nontrivial ℤ := inferInstance

end HeckeMonodromy.LaurentModel

end QOU.Mass
