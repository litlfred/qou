import Mathlib.LinearAlgebra.Projection
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Algebra.Bilinear

/-!
# QOU.MassCore.CentreCocentre — the provable core of `conj:mass-categorical-descent`

Standalone file (not wired into the QOU library).  Everything is over a
generic commutative ring `K` and a `K`-algebra `A`; no `ℝ`, no analysis,
no physical constants.

## Part I — centre / commutator splitting (positive core)

Hypothesis: the centre `Z(A)` and the `K`-span `[A,A]` of commutators are
complementary submodules, `A = Z(A) ⊕ [A,A]`.  (Classical instance, not
formalised here: `A` split semisimple over a field `K` with every block
dimension `d_λ` invertible in `K`, e.g. `A = H_n(q)` over `ℚ(q)`; then
`[A,A] = ⊕_λ sl_{d_λ}` and `Z(A) = ⊕_λ K·1_λ`.)

Under it, with `desc x := π_Z x` (projection along `[A,A]`) and
`trans x := x - desc x`:

* `decomp`        : `x = desc x + trans x`;
* `desc_mem_center`, `trans_mem_commSpan`, `decomp_unique`;
* `desc_idem`, `desc_mul_central` (`Z(A)`-linearity);
* `trace_eq_trace_desc` : every trace `τ` (`τ(ab) = τ(ba)`) satisfies
  `τ x = τ (desc x)`, i.e. `τ (trans x) = 0`;
* `desc_map_auto`, `desc_map_anti` : `desc` commutes with every algebra
  automorphism and every algebra anti-automorphism;
* `refl_involutive` : `θ_Z := 2·desc − id` is an involution.

## Part II — the corpus descent idempotent is not central (negative)

`def:descent-involution` is `τ̂ = ℓ ∘ 𝔡` with `𝔡 ∘ ℓ = id`.  If `ℓ(b)` is
non-central for some `b` then `range τ̂ ⊄ Z(A)` (`descent_range_not_central`).
For the Hecke tower, `ℓ : H_2 ↪ H_3` sends `g_1 ↦ g_1`, and `g_1` is not
central in `H_3(q)` over any nontrivial commutative ring: an explicit
2-dimensional representation (`G1`, `G2`) satisfies the Hecke quadratic and
braid relations but `G1 * G2 ≠ G2 * G1` (`hecke_g1_not_central`).
-/

namespace QOU.MassCore.CentreCocentre

section Split

variable (K A : Type*) [CommRing K] [Ring A] [Algebra K A]

/-- The `K`-span of all additive commutators `ab − ba`. -/
def commSpan : Submodule K A :=
  Submodule.span K {x : A | ∃ a b : A, x = a * b - b * a}

/-- The centre of `A`, as a `K`-submodule. -/
def centreSub : Submodule K A :=
  Subalgebra.toSubmodule (Subalgebra.center K A)

variable {K A}

lemma mem_centreSub_iff {z : A} : z ∈ centreSub K A ↔ ∀ b : A, b * z = z * b := by
  unfold centreSub
  rw [Subalgebra.mem_toSubmodule, Subalgebra.mem_center_iff]

/-- Every trace kills `[A,A]`. -/
lemma trace_vanish_commSpan {M : Type*} [AddCommGroup M] [Module K M]
    (τ : A →ₗ[K] M) (hτ : ∀ a b : A, τ (a * b) = τ (b * a))
    {c : A} (hc : c ∈ commSpan K A) : τ c = 0 := by
  have hle : commSpan K A ≤ LinearMap.ker τ := by
    unfold commSpan
    rw [Submodule.span_le]
    rintro x ⟨a, b, rfl⟩
    simp [LinearMap.mem_ker, map_sub, hτ a b]
  exact hle hc

/-- Non-vacuity of the hypothesis: every commutative algebra satisfies it
    (`Z(A) = A`, `[A,A] = 0`).  The split-semisimple instance
    (`⊕_λ M_{d_λ}(K)`, `d_λ` invertible) is classical and not formalised here. -/
theorem isCompl_of_comm {C : Type*} [CommRing C] [Algebra K C] :
    IsCompl (centreSub K C) (commSpan K C) := by
  have h1 : centreSub K C = ⊤ := by
    rw [eq_top_iff]; intro x _
    rw [mem_centreSub_iff]; intro b; exact mul_comm b x
  have h2 : commSpan K C = ⊥ := by
    unfold commSpan
    rw [Submodule.span_eq_bot]
    rintro _ ⟨a, b, rfl⟩
    rw [mul_comm, sub_self]
  rw [h1, h2]; exact isCompl_top_bot

variable (h : IsCompl (centreSub K A) (commSpan K A))
include h

/-- The descended (central) part: projection onto `Z(A)` along `[A,A]`. -/
noncomputable def desc : A →ₗ[K] A :=
  (centreSub K A).subtype ∘ₗ Submodule.linearProjOfIsCompl _ _ h

/-- The transient part `x − desc x`. -/
noncomputable def trans : A →ₗ[K] A := LinearMap.id - desc h

theorem decomp (x : A) : x = desc h x + trans h x := by
  simp [trans]

lemma desc_mem_centreSub (x : A) : desc h x ∈ centreSub K A :=
  (Submodule.linearProjOfIsCompl _ _ h x).2

theorem desc_mem_center (x : A) : desc h x ∈ Subalgebra.center K A :=
  (Subalgebra.mem_toSubmodule _).1 (desc_mem_centreSub h x)

theorem trans_mem_commSpan (x : A) : trans h x ∈ commSpan K A := by
  have hsum := Submodule.IsCompl.projection_add_projection_eq_self h x
  have e : desc h x = Submodule.IsCompl.projection h x := rfl
  have ht : trans h x = Submodule.IsCompl.projection h.symm x := by
    simp only [trans, LinearMap.sub_apply, LinearMap.id_apply]
    rw [e]; exact (eq_sub_of_add_eq' hsum).symm
  rw [ht]; exact (Submodule.linearProjOfIsCompl _ _ h.symm x).2

lemma desc_of_centre {z : A} (hz : z ∈ centreSub K A) : desc h z = z := by
  simp [desc, Submodule.linearProjOfIsCompl_apply_left h ⟨z, hz⟩]

lemma desc_of_comm {c : A} (hc : c ∈ commSpan K A) : desc h c = 0 := by
  simp [desc, Submodule.linearProjOfIsCompl_apply_right' h c hc]

/-- Uniqueness of the splitting. -/
theorem decomp_unique {x z c : A} (hz : z ∈ centreSub K A) (hc : c ∈ commSpan K A)
    (hx : x = z + c) : desc h x = z ∧ trans h x = c := by
  have hd : desc h x = z := by
    rw [hx, map_add, desc_of_centre h hz, desc_of_comm h hc, add_zero]
  refine ⟨hd, ?_⟩
  show x - desc h x = c
  rw [hd, hx]; abel

theorem desc_idem (x : A) : desc h (desc h x) = desc h x :=
  desc_of_centre h (desc_mem_centreSub h x)

/-- `desc` is `Z(A)`-linear. -/
theorem desc_mul_central {z : A} (hz : z ∈ centreSub K A) (x : A) :
    desc h (z * x) = z * desc h x := by
  have hzc := (mem_centreSub_iff).1 hz
  -- z * x = z * desc x + z * trans x, first central, second in [A,A]
  have h1 : z * desc h x ∈ centreSub K A := by
    rw [mem_centreSub_iff]
    intro b
    have hd := (mem_centreSub_iff).1 (desc_mem_centreSub h x)
    rw [← mul_assoc, hzc b, mul_assoc, hd b, ← mul_assoc]
  have h2 : z * trans h x ∈ commSpan K A := by
    have hmem := trans_mem_commSpan h x
    have hle : commSpan K A ≤ (commSpan K A).comap (LinearMap.mulLeft K z) := by
      unfold commSpan
      rw [Submodule.span_le]
      rintro y ⟨a, b, rfl⟩
      simp only [SetLike.mem_coe, Submodule.mem_comap, LinearMap.mulLeft_apply]
      apply Submodule.subset_span
      refine ⟨z * a, b, ?_⟩
      have hb : b * (z * a) = z * (b * a) := by rw [← mul_assoc, hzc b, mul_assoc]
      rw [hb, mul_sub, mul_assoc]
    exact hle hmem
  have hx : z * x = z * desc h x + z * trans h x := by
    rw [← mul_add, ← decomp h x]
  exact (decomp_unique h h1 h2 hx).1

/-- Every trace factors through the descended part: the transient part is
    trace-invisible. -/
theorem trace_eq_trace_desc {M : Type*} [AddCommGroup M] [Module K M]
    (τ : A →ₗ[K] M) (hτ : ∀ a b : A, τ (a * b) = τ (b * a)) (x : A) :
    τ x = τ (desc h x) := by
  have h0 : τ (trans h x) = 0 := trace_vanish_commSpan τ hτ (trans_mem_commSpan h x)
  conv_lhs => rw [decomp h x]
  rw [map_add, h0, add_zero]

/-- `desc` commutes with every `K`-algebra automorphism. -/
theorem desc_map_auto (θ : A ≃ₐ[K] A) (x : A) : desc h (θ x) = θ (desc h x) := by
  have hz : θ (desc h x) ∈ centreSub K A := by
    rw [mem_centreSub_iff]
    intro b
    have hd := (mem_centreSub_iff).1 (desc_mem_centreSub h x)
    have : b = θ (θ.symm b) := (θ.apply_symm_apply b).symm
    rw [this, ← map_mul, ← map_mul, hd]
  have hc : θ (trans h x) ∈ commSpan K A := by
    have hle : commSpan K A ≤ (commSpan K A).comap θ.toLinearMap := by
      unfold commSpan
      rw [Submodule.span_le]
      rintro y ⟨a, b, rfl⟩
      simp only [SetLike.mem_coe, Submodule.mem_comap, AlgEquiv.toLinearMap_apply,
        map_sub, map_mul]
      exact Submodule.subset_span ⟨θ a, θ b, rfl⟩
    exact hle (trans_mem_commSpan h x)
  have hx : θ x = θ (desc h x) + θ (trans h x) := by
    rw [← map_add, ← decomp h x]
  exact (decomp_unique h hz hc hx).1

/-- `desc` commutes with every `K`-linear anti-automorphism
    (`θ(ab) = θ(b) θ(a)`), e.g. the Hecke anti-involution `T_w ↦ T_{w⁻¹}`. -/
theorem desc_map_anti (θ : A ≃ₗ[K] A) (hθ : ∀ a b : A, θ (a * b) = θ b * θ a)
    (x : A) : desc h (θ x) = θ (desc h x) := by
  have hz : θ (desc h x) ∈ centreSub K A := by
    rw [mem_centreSub_iff]
    intro b
    have hd := (mem_centreSub_iff).1 (desc_mem_centreSub h x)
    have : b = θ (θ.symm b) := (θ.apply_symm_apply b).symm
    rw [this, ← hθ, ← hθ, hd]
  have hc : θ (trans h x) ∈ commSpan K A := by
    have hle : commSpan K A ≤ (commSpan K A).comap θ.toLinearMap := by
      unfold commSpan
      rw [Submodule.span_le]
      rintro y ⟨a, b, rfl⟩
      simp only [SetLike.mem_coe, Submodule.mem_comap, LinearEquiv.coe_coe,
        map_sub, hθ]
      exact Submodule.subset_span ⟨θ b, θ a, rfl⟩
    exact hle (trans_mem_commSpan h x)
  have hx : θ x = θ (desc h x) + θ (trans h x) := by
    rw [← map_add, ← decomp h x]
  exact (decomp_unique h hz hc hx).1

/-- The centre reflection `θ_Z = 2·desc − id` is an involution
    (+1-eigenspace `Z(A)`, −1-eigenspace `[A,A]`). -/
noncomputable def refl : A →ₗ[K] A := desc h + desc h - LinearMap.id

theorem refl_involutive (x : A) : refl h (refl h x) = x := by
  simp only [refl, LinearMap.sub_apply, LinearMap.add_apply, LinearMap.id_apply,
    map_sub, map_add, desc_idem]
  abel

end Split

section Negative

variable {K A B : Type*} [CommRing K] [Ring A] [Algebra K A]
  [AddCommGroup B] [Module K B]

/-- For any retraction pair `𝔡 ∘ ℓ = id`, the idempotent `τ̂ = ℓ ∘ 𝔡`
    fixes `range ℓ`; so if `range ℓ` contains a non-central element, the
    descended image `range τ̂` is not contained in the centre. -/
theorem descent_range_not_central (ℓ : B →ₗ[K] A) (𝔡 : A →ₗ[K] B)
    (hret : 𝔡 ∘ₗ ℓ = LinearMap.id) (b : B) (hb : ℓ b ∉ Subalgebra.center K A) :
    ∃ x : A, ℓ (𝔡 x) ∉ Subalgebra.center K A := by
  refine ⟨ℓ b, ?_⟩
  have : 𝔡 (ℓ b) = b := by
    simpa using congrArg (fun f => f b) hret
  rw [this]; exact hb

/-! ### Explicit Hecke representation (convention `(g − q)(g + q⁻¹) = 0`) -/

variable {R : Type*} [CommRing R]

/-- `g_1 ↦ G1` -/
def G1 (q qi : R) : Matrix (Fin 2) (Fin 2) R := !![q, 1; 0, -qi]
/-- `g_2 ↦ G2` -/
def G2 (q qi : R) : Matrix (Fin 2) (Fin 2) R := !![-qi, 0; 1, q]

theorem G1_quad (q qi : R) (hq : q * qi = 1) :
    G1 q qi * G1 q qi = (q - qi) • G1 q qi + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [G1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    first
    | linear_combination (-q - qi) * hq
    | linear_combination (q + qi) * hq
    | linear_combination (-1 : R) * hq
    | linear_combination hq
    | ring

theorem G2_quad (q qi : R) (hq : q * qi = 1) :
    G2 q qi * G2 q qi = (q - qi) • G2 q qi + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [G2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    first
    | linear_combination (-q - qi) * hq
    | linear_combination (q + qi) * hq
    | linear_combination (-1 : R) * hq
    | linear_combination hq
    | ring

theorem G_braid (q qi : R) (hq : q * qi = 1) :
    G1 q qi * G2 q qi * G1 q qi = G2 q qi * G1 q qi * G2 q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [G1, G2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    first
    | linear_combination (-q - qi) * hq
    | linear_combination (q + qi) * hq
    | linear_combination (-1 : R) * hq
    | linear_combination hq

theorem G_not_comm [Nontrivial R] (q qi : R) (hq : q * qi = 1) :
    G1 q qi * G2 q qi ≠ G2 q qi * G1 q qi := by
  intro hc
  have h00 := congrArg (fun M => M 0 0) hc
  simp [G1, G2, Matrix.mul_apply, Fin.sum_univ_two] at h00
  -- h00 : -(q*qi) + 1 = -(qi*q)  (up to simp normal form)
  have : (1 : R) = 0 := by linear_combination h00 + 0 * hq
  exact one_ne_zero this

/-- **`g_1` is not central in any algebra mapping onto the explicit
    representation** — in particular in `H_3(q)` over any nontrivial
    commutative ring (whose presentation makes `g_i ↦ G_i` an algebra map,
    by `G1_quad`, `G2_quad`, `G_braid`). -/
theorem hecke_g1_not_central [Nontrivial R] {H : Type*} [Ring H] [Algebra R H]
    (q qi : R) (hq : q * qi = 1) (g1 g2 : H)
    (ρ : H →ₐ[R] Matrix (Fin 2) (Fin 2) R) (h1 : ρ g1 = G1 q qi) (h2 : ρ g2 = G2 q qi) :
    g1 ∉ Subalgebra.center R H := by
  intro hc
  have hcomm : g2 * g1 = g1 * g2 := (Subalgebra.mem_center_iff.mp hc) g2
  apply G_not_comm q qi hq
  rw [← h1, ← h2, ← map_mul, ← map_mul, hcomm]

end Negative

end QOU.MassCore.CentreCocentre

