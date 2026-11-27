import Mathlib.Tactic
import Mathlib.Analysis.Complex.Polynomial.Basic

/-!
# The `sl₃` structure-constant tensor is the commutator of two Casimir legs

Formalises two results of the probe
`computations/probes/mn_own_identity/mn_three_gluon_vertex_probe.py`
(pre-registration `PREREGISTRATION-three-gluon-vertex.md`, measurements M1 and M4).

`V = R³` with basis `e₀, e₁, e₂`; `V^{⊗3}` has basis `e_x`, `x ∈ Idx3 = Fin 3 × Fin 3 × Fin 3`.
Operators are matrices `Idx3 × Idx3`. `permOp σ` sends `e_y ↦ e_{σ y}`; `P₁₂, P₂₃, P₁₃` are the
slot transpositions and `C = P₁₂ P₂₃` (`cyc`).

## (A) `[Ω₁₂, Ω₂₃] = −F`, `F = −¼ (C − C²)`

* `omega12_omega23_commutator` (any field): with `Ω_{ij} = (P_{ij} − 1/3)/2`,
  `[Ω₁₂, Ω₂₃] = ¼ (C − C²)`. The one non-formal input is the braid relation of the
  transpositions, `P₂₃ P₁₂ = C²`, checked on the 27 basis labels.
* `gellMann i r`: the eight Gell-Mann generators `T^a = λ^a/2`, written over any field of
  characteristic zero that contains `i` with `i² = −1` and `r` with `r² = 1/3` (`r` stands for
  `1/√3` in `λ₈`). `gellMann_hyps_satisfiable` shows `ℂ` is such a field, so the hypotheses are not
  vacuous.
* `fierz`: `Σ_a T^a_{ab} T^a_{cd} = ½ (δ_{ad} δ_{cb} − ⅓ δ_{ab} δ_{cd})` (81 cases).
  Hence `omega12GM_eq` etc.: the Casimir tensor `Σ_a T^a ⊗ T^a` on slots `ij` is `(P_{ij} − 1/3)/2`.
* `fGM i r = Σ_{a,b} T^a ⊗ T^b ⊗ [T^a, T^b]`. **Dictionary**: the structure constants are
  *defined* by `[T^a, T^b] = i f^{abc} T^c`, so `fGM = i f^{abc} T^a ⊗ T^b ⊗ T^c` term by term;
  this file does not tabulate the 512 numbers `f^{abc}` (the probe does, and checks the defining
  relation). `fGM_eq_commutator`: `F = [Ω₁₃, Ω₂₃]` for any family `T`.
* `fGM_eq_neg_quarter_cyc`: `F = −¼ (C − C²)`; `omega_commutator_eq_neg_fGM`: `[Ω₁₂, Ω₂₃] = −F`.
  No `d^{abc}` component appears: the commutator is exactly a multiple of the antisymmetrised
  3-cycle. This is standard `sl₃` algebra, not a QOU result.

## (B) The `F`-coefficient of the photon letter and of the Borromean core

Jimbo braiding `Ř_c` on `V ⊗ V` (convention of the probe and of `def:down-quark`):
`Ř_c e_{ii} = q e_{ii}`, `Ř_c e_{ij} = e_{ji}` (`i < j`), `Ř_c e_{ij} = e_{ji} + h e_{ij}` (`i > j`),
`h = q − q⁻¹`; `σ₀ = Ř_c ⊗ 1`, `σ₁ = 1 ⊗ Ř_c`, `σ₁⁻¹ = 1 ⊗ (Ř_c − h)`.
The photon letter is `σ₀ σ₁⁻¹` (`letter`) and the Borromean core is `V³ = (σ₀ σ₁⁻¹)³` (`core`).

`hs M X = Σ_{x,y} M_{xy} X_{xy} = tr(Mᵀ X)` is the Hilbert–Schmidt pairing, and
`fOp = −¼ (C − C²)` (`= fGM`, `fGM_eq_fOp`). The probe's "F-coefficient" of `X` is the coefficient
of `F` in the classical-`SU(3)` Haar average of `X`, expanded in its adapted basis
`{1, P₁₂+P₁₃+P₂₃, C+C², C−C², P₁₂−P₂₃, P₁₂−2P₁₃+P₂₃}`. Here:

* `hs_fOp_permOp_*`, `hs_fOp_cyc_add_cyc_sq`: `F` is HS-orthogonal to `1`, to each transposition,
  and to `C + C²`, i.e. to the other five adapted vectors; `hs_fOp_fOp`: `⟨F, F⟩ = 3`.
  Hence the `F`-coefficient of the HS-orthogonal projection of `X` onto the span of the
  permutation operators is `fCoef X = ⟨F, X⟩ / ⟨F, F⟩`.
* `fCoef_letter`: `fCoef (σ₀σ₁⁻¹) = −(q+1)²/(2q)`.
* `fCoef_core`: `fCoef (V³) = −(q−1)²(q+1)⁴(q⁴+1)/(2q⁵)` (zero at `q = 1`).
* Comparisons from the probe: `fCoef_s0s1` (`σ₀σ₁`: the same `−(q+1)²/(2q)`),
  `fCoef_s1inv_s0` (`σ₁⁻¹σ₀`: `+(q+1)²/(2q)`), `fCoef_s0s1s0` (`σ₀σ₁σ₀`: `0` at every `q`).

These are exact identities over any field with `q ≠ 0`, `2 ≠ 0`, `3 ≠ 0`.

**Not formalised.** (1) That the Haar average over `SU(3)` is the HS-orthogonal projection onto
the commutant, and that the commutant of `SU(3)` on `V^{⊗3}` is spanned by the six permutation
operators (Schur–Weyl duality); `fCoef` is therefore the probe's F-coefficient only through these
two standard facts. (2) The numbers `f^{abc}` and `d^{abc}` themselves (see the dictionary above).
(3) The probe's measurements M2, M3, M5 (CYBE, `ħ`-expansion, four strands). The projection is
classical `SU(3)` and not `U_q`-covariant, as the probe states; nothing here selects a vertex, a
coupling or a gluon (the gluon of `def:derived-atom` step 4 stays open).

Base ring (§7c): generic fields throughout; only `gellMann_hyps_satisfiable` mentions `ℂ`.

-- Ref: [kassel1995] Kassel, *Quantum Groups*, ch. VIII (Jimbo `R`-matrix)
-- Ref: [fulton-harris1991] Fulton–Harris, *Representation Theory*, §6 (Schur–Weyl), §15 (`sl₃`)
-- Ref: [leitner2026] computations/probes/mn_own_identity/mn_three_gluon_vertex_probe.py (M1, M4)
-/

open Matrix

namespace QOU.Braiding.ColourStructureConstantCommutator

/-- Basis labels of `V^{⊗3}`, `V = R³`: (slot 1, slot 2, slot 3). -/
abbrev Idx3 := Fin 3 × Fin 3 × Fin 3

/-- Exchange of slots 1 and 2. -/
def swap12 : Equiv.Perm Idx3 where
  toFun x := (x.2.1, x.1, x.2.2)
  invFun x := (x.2.1, x.1, x.2.2)
  left_inv _ := rfl
  right_inv _ := rfl

/-- Exchange of slots 2 and 3. -/
def swap23 : Equiv.Perm Idx3 where
  toFun x := (x.1, x.2.2, x.2.1)
  invFun x := (x.1, x.2.2, x.2.1)
  left_inv _ := rfl
  right_inv _ := rfl

/-- Exchange of slots 1 and 3. -/
def swap13 : Equiv.Perm Idx3 where
  toFun x := (x.2.2, x.2.1, x.1)
  invFun x := (x.2.2, x.2.1, x.1)
  left_inv _ := rfl
  right_inv _ := rfl

/-- Braid relation of the transpositions: `P₂₃ P₁₂ = (P₁₂ P₂₃)²`. -/
theorem swap23_mul_swap12 : swap23 * swap12 = (swap12 * swap23) * (swap12 * swap23) := by
  ext x <;> rcases x with ⟨a, b, c⟩ <;> rfl

theorem swap13_mul_swap23 : swap13 * swap23 = (swap12 * swap23) * (swap12 * swap23) := by
  ext x <;> rcases x with ⟨a, b, c⟩ <;> rfl

theorem swap23_mul_swap13 : swap23 * swap13 = swap12 * swap23 := by
  ext x <;> rcases x with ⟨a, b, c⟩ <;> rfl

section Perm
variable {R : Type*} [CommRing R]

/-- The operator `e_y ↦ e_{σ y}` of a permutation of basis labels. -/
def permOp (σ : Equiv.Perm Idx3) : Matrix Idx3 Idx3 R := fun x y => if x = σ y then 1 else 0

theorem permOp_mul (σ τ : Equiv.Perm Idx3) :
    (permOp σ : Matrix Idx3 Idx3 R) * permOp τ = permOp (σ * τ) := by
  ext x y
  simp only [permOp, mul_apply, mul_ite, mul_one, mul_zero, Equiv.Perm.mul_apply]
  rw [Finset.sum_ite_eq']; simp

theorem permOp_one : (permOp 1 : Matrix Idx3 Idx3 R) = 1 := by
  ext x y; simp [permOp, one_apply]

end Perm

section CommutatorPerm
variable {R : Type*} [Field R]

/-- `Ω = (P − 1/3)/2` on the pair of slots exchanged by `σ`. -/
def omegaP (σ : Equiv.Perm Idx3) : Matrix Idx3 Idx3 R := (2 : R)⁻¹ • (permOp σ - (3 : R)⁻¹ • 1)

/-- The cyclic permutation operator `C = P₁₂ P₂₃`. -/
def cyc : Matrix Idx3 Idx3 R := permOp swap12 * permOp swap23

theorem cyc_eq : (cyc : Matrix Idx3 Idx3 R) = permOp (swap12 * swap23) := permOp_mul _ _

theorem cyc_sq : (cyc : Matrix Idx3 Idx3 R) * cyc = permOp swap23 * permOp swap12 := by
  simp only [cyc, permOp_mul, swap23_mul_swap12]

lemma comm_shift {A : Type*} [Ring A] [Algebra R A] (t s : R) (a b : A) :
    (t • (a - s • 1)) * (t • (b - s • 1)) - (t • (b - s • 1)) * (t • (a - s • 1))
      = (t * t) • (a * b - b * a) := by
  simp only [smul_sub, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one, smul_smul]
  module

/-- **(A), permutation form.** `[Ω₁₂, Ω₂₃] = ¼ (C − C²)` on `V^{⊗3}`. -/
theorem omega12_omega23_commutator :
    (omegaP swap12 : Matrix Idx3 Idx3 R) * omegaP swap23 - omegaP swap23 * omegaP swap12
      = (4 : R)⁻¹ • (cyc - cyc * cyc) := by
  rw [cyc_sq, omegaP, omegaP, comm_shift, cyc]
  congr 1; rw [← mul_inv]; norm_num

end CommutatorPerm

section GellMann
variable {K : Type*} [Field K] [CharZero K]
/-- The Gell-Mann generators `T^a = λ^a / 2`, `a = 1..8` (indexed `0..7`); `i` plays `√−1` and
`r` plays `1/√3`. -/
def gellMann (i r : K) : Fin 8 → Matrix (Fin 3) (Fin 3) K :=
  ![(2 : K)⁻¹ • !![0, 1, 0; 1, 0, 0; 0, 0, 0],
    (2 : K)⁻¹ • !![0, -i, 0; i, 0, 0; 0, 0, 0],
    (2 : K)⁻¹ • !![1, 0, 0; 0, -1, 0; 0, 0, 0],
    (2 : K)⁻¹ • !![0, 0, 1; 0, 0, 0; 1, 0, 0],
    (2 : K)⁻¹ • !![0, 0, -i; 0, 0, 0; i, 0, 0],
    (2 : K)⁻¹ • !![0, 0, 0; 0, 0, 1; 0, 1, 0],
    (2 : K)⁻¹ • !![0, 0, 0; 0, 0, -i; 0, i, 0],
    (2 : K)⁻¹ • !![r, 0, 0; 0, r, 0; 0, 0, -2 * r]]

set_option maxHeartbeats 1000000 in
/-- **Fierz identity** for `sl₃`: `Σ_a T^a_{ab} T^a_{cd} = ½ (δ_{ad} δ_{cb} − ⅓ δ_{ab} δ_{cd})`. -/
theorem fierz (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) (a b c d : Fin 3) :
    ∑ e, gellMann i r e a b * gellMann i r e c d
      = (2 : K)⁻¹ * ((if a = d ∧ c = b then 1 else 0) - (3 : K)⁻¹ * (if a = b ∧ c = d then 1 else 0)) := by
  simp only [Fin.sum_univ_eight, gellMann]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp <;> ring_nf <;> simp only [hi, hr] <;> ring_nf
/-- `A ⊗ B ⊗ C` on `V^{⊗3}`. -/
def tens3 (A B C : Matrix (Fin 3) (Fin 3) K) : Matrix Idx3 Idx3 K :=
  fun x y => A x.1 y.1 * B x.2.1 y.2.1 * C x.2.2 y.2.2

omit [CharZero K] in
theorem tens3_mul (A B C A' B' C' : Matrix (Fin 3) (Fin 3) K) :
    tens3 A B C * tens3 A' B' C' = tens3 (A * A') (B * B') (C * C') := by
  ext ⟨x1, x2, x3⟩ ⟨y1, y2, y3⟩
  simp only [tens3, mul_apply, Fintype.sum_prod_type, Fin.sum_univ_three]
  ring

omit [CharZero K] in
theorem tens3_sub_right (A B C D : Matrix (Fin 3) (Fin 3) K) :
    tens3 A B (C - D) = tens3 A B C - tens3 A B D := by
  ext x y; simp [tens3, mul_sub]

/-- `Ω₁₂ = Σ_a T^a ⊗ T^a ⊗ 1` built from the Gell-Mann generators. -/
def omega12GM (i r : K) : Matrix Idx3 Idx3 K := ∑ e, tens3 (gellMann i r e) (gellMann i r e) 1
/-- `Ω₂₃ = Σ_a 1 ⊗ T^a ⊗ T^a`. -/
def omega23GM (i r : K) : Matrix Idx3 Idx3 K := ∑ e, tens3 1 (gellMann i r e) (gellMann i r e)
/-- `Ω₁₃ = Σ_a T^a ⊗ 1 ⊗ T^a`. -/
def omega13GM (i r : K) : Matrix Idx3 Idx3 K := ∑ e, tens3 (gellMann i r e) 1 (gellMann i r e)

theorem omega12GM_eq (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) :
    omega12GM i r = omegaP swap12 := by
  ext ⟨x1, x2, x3⟩ ⟨y1, y2, y3⟩
  simp only [omega12GM, Matrix.sum_apply, tens3, ← Finset.sum_mul, fierz i r hi hr]
  simp only [omegaP, permOp, swap12, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    Equiv.coe_fn_mk, Prod.mk.injEq, smul_eq_mul]
  by_cases h : x3 = y3 <;> simp [h]

theorem omega23GM_eq (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) :
    omega23GM i r = omegaP swap23 := by
  ext ⟨x1, x2, x3⟩ ⟨y1, y2, y3⟩
  simp only [omega23GM, Matrix.sum_apply, tens3, mul_assoc, ← Finset.mul_sum, fierz i r hi hr]
  simp only [omegaP, permOp, swap23, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    Equiv.coe_fn_mk, Prod.mk.injEq, smul_eq_mul]
  by_cases h : x1 = y1 <;> simp [h]

theorem omega13GM_eq (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) :
    omega13GM i r = omegaP swap13 := by
  ext ⟨x1, x2, x3⟩ ⟨y1, y2, y3⟩
  simp only [omega13GM, Matrix.sum_apply, tens3, mul_right_comm _ ((1 : Matrix (Fin 3) (Fin 3) K) _ _),
    ← Finset.sum_mul, fierz i r hi hr]
  simp only [omegaP, permOp, swap13, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    Equiv.coe_fn_mk, Prod.mk.injEq, smul_eq_mul]
  by_cases h : x2 = y2 <;> simp [h]

/-- `F = Σ_{a,b} T^a ⊗ T^b ⊗ [T^a, T^b]`. -/
def fGM (i r : K) : Matrix Idx3 Idx3 K :=
  ∑ e, ∑ f, tens3 (gellMann i r e) (gellMann i r f)
    (gellMann i r e * gellMann i r f - gellMann i r f * gellMann i r e)

omit [CharZero K] in
theorem fGM_eq_commutator (i r : K) :
    fGM i r = omega13GM i r * omega23GM i r - omega23GM i r * omega13GM i r := by
  simp only [fGM, omega13GM, omega23GM, Finset.sum_mul_sum, tens3_mul, one_mul, mul_one,
    tens3_sub_right, Finset.sum_sub_distrib]
  rw [Finset.sum_comm (f := fun x y => tens3 _ _ (gellMann i r y * gellMann i r x))]


/-- **(A), structure-constant form.** `F = i f^{abc} T^a ⊗ T^b ⊗ T^c = −¼ (C − C²)`. -/
theorem fGM_eq_neg_quarter_cyc (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) :
    fGM i r = -(4 : K)⁻¹ • (cyc - cyc * cyc) := by
  rw [fGM_eq_commutator, omega13GM_eq i r hi hr, omega23GM_eq i r hi hr, omegaP, omegaP,
    comm_shift, permOp_mul, permOp_mul, swap13_mul_swap23, swap23_mul_swap13, cyc_eq, permOp_mul,
    ← mul_inv]
  norm_num
  module

/-- **(A), the probe's M1.** `[Ω₁₂, Ω₂₃] = −F = −i f^{abc} T^a ⊗ T^b ⊗ T^c`, with `Ω` the
Gell-Mann Casimir tensor `Σ_a T^a ⊗ T^a`. -/
theorem omega_commutator_eq_neg_fGM (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) :
    omega12GM i r * omega23GM i r - omega23GM i r * omega12GM i r = -fGM i r := by
  rw [omega12GM_eq i r hi hr, omega23GM_eq i r hi hr, omega12_omega23_commutator,
    fGM_eq_neg_quarter_cyc i r hi hr, neg_smul, neg_neg]

end GellMann

section Braid
variable {K : Type*} [Field K]

/-- Basis vector `e_y` of `V^{⊗3}`. -/
def bvec (y : Idx3) : Idx3 → K := fun x => if x = y then 1 else 0

/-- Column `(i,j)` of the Jimbo braiding `Ř_c` on `V ⊗ V`: coefficient of `e_{kl}` in `Ř_c e_{ij}`. -/
def rcCol (q : K) (ij kl : Fin 3 × Fin 3) : K :=
  if ij.1 = ij.2 then (if kl = ij then q else 0)
  else if ij.1 < ij.2 then (if kl = (ij.2, ij.1) then 1 else 0)
  else (if kl = (ij.2, ij.1) then 1 else 0) + (if kl = ij then q - q⁻¹ else 0)

/-- Column of `Ř_c⁻¹ = Ř_c − h`. -/
def rcInvCol (q : K) (ij kl : Fin 3 × Fin 3) : K :=
  rcCol q ij kl - (if kl = ij then q - q⁻¹ else 0)

/-- `σ₀ = Ř_c ⊗ 1` on slots 1,2. -/
def s0 (q : K) : Matrix Idx3 Idx3 K := fun x y => rcCol q (y.1, y.2.1) (x.1, x.2.1) * (if x.2.2 = y.2.2 then 1 else 0)
/-- `σ₁ = 1 ⊗ Ř_c` on slots 2,3. -/
def s1 (q : K) : Matrix Idx3 Idx3 K := fun x y => (if x.1 = y.1 then 1 else 0) * rcCol q (y.2.1, y.2.2) (x.2.1, x.2.2)
/-- `σ₁⁻¹ = 1 ⊗ Ř_c⁻¹`. -/
def s1inv (q : K) : Matrix Idx3 Idx3 K := fun x y => (if x.1 = y.1 then 1 else 0) * rcInvCol q (y.2.1, y.2.2) (x.2.1, x.2.2)

theorem mulVec_bvec (M : Matrix Idx3 Idx3 K) (y : Idx3) : M *ᵥ bvec y = fun x => M x y := by
  funext x; simp [mulVec, dotProduct, bvec]

theorem s0_bvec (q : K) (a b c : Fin 3) :
    s0 q *ᵥ bvec (a, b, c) =
      if a = b then q • bvec (a, b, c)
      else if a < b then bvec (b, a, c)
      else bvec (b, a, c) + (q - q⁻¹) • bvec (a, b, c) := by
  rw [mulVec_bvec]; funext ⟨x1, x2, x3⟩
  by_cases h3 : x3 = c <;> by_cases hab : a = b
  · subst hab h3; simp [s0, rcCol, bvec]
  all_goals by_cases hlt : a < b <;> simp [s0, rcCol, bvec, hab, hlt, h3]

theorem s1inv_bvec (q : K) (a b c : Fin 3) :
    s1inv q *ᵥ bvec (a, b, c) =
      if b = c then q⁻¹ • bvec (a, b, c)
      else if b < c then bvec (a, c, b) - (q - q⁻¹) • bvec (a, b, c)
      else bvec (a, c, b) := by
  rw [mulVec_bvec]; funext ⟨x1, x2, x3⟩
  by_cases h1 : x1 = a <;> by_cases hbc : b = c
  · subst h1 hbc; simp [s1inv, rcInvCol, rcCol, bvec]; split_ifs <;> ring
  all_goals by_cases hlt : b < c <;> simp [s1inv, rcInvCol, rcCol, bvec, hbc, hlt, h1]

theorem s1_bvec (q : K) (a b c : Fin 3) :
    s1 q *ᵥ bvec (a, b, c) =
      if b = c then q • bvec (a, b, c)
      else if b < c then bvec (a, c, b)
      else bvec (a, c, b) + (q - q⁻¹) • bvec (a, b, c) := by
  rw [mulVec_bvec]; funext ⟨x1, x2, x3⟩
  by_cases h1 : x1 = a <;> by_cases hbc : b = c
  · subst h1 hbc; simp [s1, rcCol, bvec]
  all_goals by_cases hlt : b < c <;> simp [s1, rcCol, bvec, hbc, hlt, h1]

/-- Hilbert–Schmidt pairing `⟨M, X⟩ = tr(Mᵀ X)`. -/
def hs (M X : Matrix Idx3 Idx3 K) : K := ∑ x, ∑ y, M x y * X x y

theorem hs_permOp (σ : Equiv.Perm Idx3) (X : Matrix Idx3 Idx3 K) :
    hs (permOp σ) X = ∑ y, X (σ y) y := by
  rw [hs, Finset.sum_comm]; congr 1; funext y
  simp [permOp, ite_mul]

/-- The permutation form of `F`: `−¼ (C − C²)`, `C = P₁₂ P₂₃`. -/
def fOp : Matrix Idx3 Idx3 K :=
  -(4 : K)⁻¹ • (permOp (swap12 * swap23) - permOp ((swap12 * swap23) * (swap12 * swap23)))

/-- `⟨F, X⟩ = −¼ Σ_y (X_{C y, y} − X_{C² y, y})`. -/
theorem hs_fOp (X : Matrix Idx3 Idx3 K) :
    hs fOp X = -(4 : K)⁻¹ * ∑ y, ((X *ᵥ bvec y) ((swap12 * swap23) y)
      - (X *ᵥ bvec y) (((swap12 * swap23) * (swap12 * swap23)) y)) := by
  have hlin : ∀ (c : K) (A B : Matrix Idx3 Idx3 K), hs (c • (A - B)) X = c * (hs A X - hs B X) := by
    intro c A B; simp only [hs, Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, mul_sub, sub_mul,
      Finset.sum_sub_distrib, Finset.mul_sum, mul_assoc]
  rw [fOp, hlin, hs_permOp, hs_permOp, ← Finset.sum_sub_distrib]
  simp [mulVec_bvec]

/-- The photon chiral letter `σ₀ σ₁⁻¹` on `V^{⊗3}`. -/
def letter (q : K) : Matrix Idx3 Idx3 K := s0 q * s1inv q

set_option maxHeartbeats 4000000 in
theorem hs_fOp_letter (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    hs fOp (letter q) = -3 * (q + 1) ^ 2 / (2 * q) := by
  rw [hs_fOp]
  simp only [letter, ← mulVec_mulVec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [s1inv_bvec q, s0_bvec, mulVec_sub, mulVec_smul, bvec, swap12, swap23]
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  field_simp
  ring


/-- The Borromean core `V³ = (σ₀ σ₁⁻¹)³`. -/
def core (q : K) : Matrix Idx3 Idx3 K := letter q * letter q * letter q

set_option maxHeartbeats 8000000 in
theorem hs_fOp_core (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    hs fOp (core q) = -3 * (q - 1) ^ 2 * (q + 1) ^ 4 * (q ^ 4 + 1) / (2 * q ^ 5) := by
  rw [hs_fOp]
  simp only [core, letter, ← mulVec_mulVec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [s1inv_bvec q, s0_bvec, mulVec_add, mulVec_sub, mulVec_smul, bvec, swap12, swap23]
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  field_simp
  ring

/-- `σ₀ σ₁` (for comparison with the photon letter). -/
def s0s1 (q : K) : Matrix Idx3 Idx3 K := s0 q * s1 q
/-- `σ₁⁻¹ σ₀` (the photon letter in the reversed order). -/
def s1invS0 (q : K) : Matrix Idx3 Idx3 K := s1inv q * s0 q
/-- `σ₀ σ₁ σ₀`. -/
def s0s1s0 (q : K) : Matrix Idx3 Idx3 K := s0 q * s1 q * s0 q

/-- The `σ`-relations hold for these matrices: `σ₁ σ₁⁻¹ = 1` (so `s1inv` is the inverse), checked
column by column. -/
theorem s1_mul_s1inv (q : K) (hq : q ≠ 0) : s1 q * s1inv q = 1 := by
  ext x ⟨a, b, c⟩
  have := congrFun (show (s1 q * s1inv q) *ᵥ bvec (a, b, c) = (1 : Matrix Idx3 Idx3 K) *ᵥ bvec (a, b, c) by
    rw [← mulVec_mulVec, one_mulVec, s1inv_bvec]
    by_cases hbc : b = c
    · subst hbc; simp [s1_bvec, mulVec_smul, smul_smul, inv_mul_cancel₀ hq]
    by_cases hlt : b < c
    · have hcb : ¬ c < b := lt_asymm hlt
      simp [hbc, hlt, s1_bvec, mulVec_sub, mulVec_smul, hcb, Ne.symm hbc]
    · have hcb : c < b := lt_of_le_of_ne (not_lt.mp hlt) (Ne.symm hbc)
      simp [hbc, hlt, s1_bvec, hcb, Ne.symm hbc]) x
  simpa [mulVec_bvec] using this

set_option maxHeartbeats 4000000 in
theorem hs_fOp_s0s1 (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    hs fOp (s0s1 q) = -3 * (q + 1) ^ 2 / (2 * q) := by
  rw [hs_fOp]
  simp only [s0s1, ← mulVec_mulVec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [s1_bvec q, s0_bvec, mulVec_add, mulVec_smul, bvec, swap12, swap23]
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  field_simp
  ring

set_option maxHeartbeats 4000000 in
theorem hs_fOp_s1invS0 (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    hs fOp (s1invS0 q) = 3 * (q + 1) ^ 2 / (2 * q) := by
  rw [hs_fOp]
  simp only [s1invS0, ← mulVec_mulVec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [s1inv_bvec q, s0_bvec, mulVec_add, mulVec_smul, bvec, swap12, swap23]
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  field_simp
  ring

set_option maxHeartbeats 4000000 in
theorem hs_fOp_s0s1s0 (q : K) : hs fOp (s0s1s0 q) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [s0s1s0, ← mulVec_mulVec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [s1_bvec q, s0_bvec, mulVec_add, mulVec_smul, bvec, swap12, swap23]
  ring

/-! ### Orthogonality: `F` against the other adapted vectors -/

theorem hs_fOp_permOp_one : hs fOp (permOp 1 : Matrix Idx3 Idx3 K) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [permOp, swap12, swap23]

theorem hs_fOp_permOp_swap12 : hs fOp (permOp swap12 : Matrix Idx3 Idx3 K) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [permOp, swap12, swap23]

theorem hs_fOp_permOp_swap23 : hs fOp (permOp swap23 : Matrix Idx3 Idx3 K) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [permOp, swap12, swap23]
  ring

theorem hs_fOp_permOp_swap13 : hs fOp (permOp swap13 : Matrix Idx3 Idx3 K) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [permOp, swap12, swap23, swap13]
  ring

theorem hs_fOp_cyc_add_cyc_sq :
    hs fOp (permOp (swap12 * swap23) + permOp ((swap12 * swap23) * (swap12 * swap23)) :
      Matrix Idx3 Idx3 K) = 0 := by
  rw [hs_fOp, mul_eq_zero]; right
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [permOp, swap12, swap23]

theorem hs_fOp_fOp (h2 : (2 : K) ≠ 0) : hs (fOp : Matrix Idx3 Idx3 K) fOp = 3 := by
  rw [hs_fOp]
  simp only [mulVec_bvec, Fintype.sum_prod_type, Fin.sum_univ_three]
  simp [fOp, permOp, swap12, swap23]
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  field_simp
  ring

/-- The `F`-coefficient: `⟨F, X⟩ / ⟨F, F⟩`. Since `F` is HS-orthogonal to the other five adapted
vectors (lemmas above), this is the coefficient of `F` in the HS-orthogonal projection of `X` onto
the span of the six permutation operators. -/
def fCoef (X : Matrix Idx3 Idx3 K) : K := hs fOp X / hs fOp fOp

/-- `X − fCoef X • F` is HS-orthogonal to `F`. -/
theorem hs_fOp_sub_fCoef (X : Matrix Idx3 Idx3 K) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    hs fOp (X - fCoef X • fOp) = 0 := by
  have hlin : hs fOp (X - fCoef X • fOp) = hs fOp X - fCoef X * hs fOp fOp := by
    simp only [hs, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul, mul_sub,
      Finset.sum_sub_distrib, Finset.mul_sum]
    congr 1; refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => by ring
  rw [hlin, fCoef, hs_fOp_fOp h2, div_mul_cancel₀ _ h3, sub_self]

/-- **(B), photon letter.** `fCoef (σ₀ σ₁⁻¹) = −(q+1)²/(2q)`. -/
theorem fCoef_letter (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    fCoef (letter q) = -(q + 1) ^ 2 / (2 * q) := by
  rw [fCoef, hs_fOp_letter q hq h2, hs_fOp_fOp h2]; field_simp

/-- **(B), Borromean core.** `fCoef ((σ₀ σ₁⁻¹)³) = −(q−1)²(q+1)⁴(q⁴+1)/(2q⁵)`. -/
theorem fCoef_core (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    fCoef (core q) = -(q - 1) ^ 2 * (q + 1) ^ 4 * (q ^ 4 + 1) / (2 * q ^ 5) := by
  rw [fCoef, hs_fOp_core q hq h2, hs_fOp_fOp h2]; field_simp

theorem fCoef_s0s1 (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    fCoef (s0s1 q) = -(q + 1) ^ 2 / (2 * q) := by
  rw [fCoef, hs_fOp_s0s1 q hq h2, hs_fOp_fOp h2]; field_simp

theorem fCoef_s1invS0 (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    fCoef (s1invS0 q) = (q + 1) ^ 2 / (2 * q) := by
  rw [fCoef, hs_fOp_s1invS0 q hq h2, hs_fOp_fOp h2]; field_simp

theorem fCoef_s0s1s0 (q : K) : fCoef (s0s1s0 q) = 0 := by
  rw [fCoef, hs_fOp_s0s1s0 q, zero_div]

end Braid

section Bridge
variable {K : Type*} [Field K] [CharZero K]

/-- The Gell-Mann `F` of (A) is the `fOp` of (B). -/
theorem fGM_eq_fOp (i r : K) (hi : i ^ 2 = -1) (hr : r ^ 2 = (3 : K)⁻¹) : fGM i r = fOp := by
  rw [fGM_eq_neg_quarter_cyc i r hi hr, fOp, cyc_eq, permOp_mul]

end Bridge

/-- The hypotheses of the Gell-Mann section are satisfiable: `ℂ` with `i = I` and `r` a square
root of `1/3`, which exists because `ℂ` is algebraically closed (no `Real.sqrt`, transcendental
boundary, owner ruling 2026-11-27). -/
theorem gellMann_hyps_satisfiable :
    ∃ i r : ℂ, i ^ 2 = -1 ∧ r ^ 2 = (3 : ℂ)⁻¹ := by
  obtain ⟨r, hr⟩ := IsAlgClosed.exists_pow_nat_eq (3 : ℂ)⁻¹ two_pos
  exact ⟨Complex.I, r, Complex.I_sq, hr⟩

end QOU.Braiding.ColourStructureConstantCommutator
