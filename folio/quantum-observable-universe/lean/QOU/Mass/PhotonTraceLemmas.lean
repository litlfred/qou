/-
  Photon and trace lemmas in `H₃(q)`.

  All statements are about an algebra `A` over a commutative ring `R` with two
  elements `a, b` (the images of `σ₀, σ₁`) satisfying the relations of `H₃(q)`
  (`HeckeH3Rel`, with `h = q − q⁻¹`). Nothing numerical is used.

  The photon `γ` is `def:photon` (`QOU.Photon.photon`), imported, not redefined.

  1. **Switched photon.** `γ′(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` equals
     `γ(φ₀ − hφ₀₁, φ₁, φ₀₁)`, so the two photon families are the same set, and
     `β_Bor = γ′(0,0,qh)·γ′(0,0,−q⁻¹h)` (`borromean_eq_switched_photons`).
  2. **Commuting separators.** A photon built on generators that commute with
     an element `s` commutes with `s` (`commute_photon`); a separator commuting
     with the second photon can be moved past it (`separator_commute`); and for
     any cyclic trace two commuting photons can be wrapped round a word
     (`trace_wrap`). These are the zero cases of the `H₅` photon-separation probe.
  3. **The two-dimensional block.** If `a, b` are `2 × 2` matrices over a field
     satisfying the relations, and `V = σ₀σ₁⁻¹` has no fixed vector and is not a
     scalar, then `tr V = −(1 + h²)` and `det V = 1`
     (`vertex_trace_det_two`): `V` satisfies `V² + (1+h²)V + 1 = 0` there.
  4. **Flavour no-go.** For any product of factors `α·1 + β·σᵢ` (this covers
     `σᵢ⁻¹ = σᵢ − h` and every typed crossing operator and its inverse), and any
     `R`-linear cyclic trace `t`, swapping `σ₀ ↔ σ₁` in every factor and reversing
     the order does not change `t` (`trace_flip_reverse`). The swap is inner
     (conjugation by `Δ = σ₀σ₁σ₀`), and reversal fixes the basis
     `1, σ₀, σ₁, σ₀σ₁σ₀` and exchanges `σ₀σ₁ ↔ σ₁σ₀`, which a cyclic trace cannot
     tell apart. So a trace cannot separate two nucleon words related by this
     anti-automorphism.

  -- Ref: [iwahori1964] https://doi.org/10.15083/00039809
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.Mass.BorromeanPhotonFactorisation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Adjugate
import Mathlib.Tactic.LinearCombination

namespace QOU.Mass.PhotonTraceLemmas

open QOU.Mass.BorromeanPhotonFactorisation
open QOU.Photon (photon Colour)

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable {h : R} {a b : A}

/-! ### 1. The switched photon -/

/-- `γ′(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`, with `σ₀σ₁⁻¹` written as `vertex h a b`. -/
def photonSwitched (h φ₀ φ₁ φ₀₁ : R) (a b : A) : A :=
  1 + φ₀ • a + φ₁ • b + φ₀₁ • vertex h a b

theorem photonSwitched_eq (h φ₀ φ₁ φ₀₁ : R) (a b : A) :
    photonSwitched h φ₀ φ₁ φ₀₁ a b = photon a b (⟨φ₀ - h * φ₀₁, φ₁, φ₀₁⟩ : Colour R) := by
  simp only [photonSwitched, photon, vertex_eq, smul_sub, smul_smul]
  module

theorem photon_eq_switched (h φ₀ φ₁ φ₀₁ : R) (a b : A) :
    photon a b (⟨φ₀, φ₁, φ₀₁⟩ : Colour R) = photonSwitched h (φ₀ + h * φ₀₁) φ₁ φ₀₁ a b := by
  rw [photonSwitched_eq, add_sub_cancel_right]

theorem photonPlus_eq_switched (q h : R) (a b : A) :
    photonPlus q h a b = photonSwitched h 0 0 (q * h) a b := by
  simp only [photonPlus, photonSwitched, zero_smul, add_zero]

theorem photonMinus_eq_switched (q' h : R) (a b : A) :
    photonMinus q' h a b = photonSwitched h 0 0 (-(q' * h)) a b := by
  simp only [photonMinus, photonSwitched, zero_smul, add_zero, neg_smul, sub_eq_add_neg]

/-- `β_Bor = γ′(0,0,qh) · γ′(0,0,−q⁻¹h)`: two switched photons, each with only
    its last term. -/
theorem borromean_eq_switched_photons (H : HeckeH3Rel h a b) {q q' : R}
    (hh : q - q' = h) (hq : q * q' = 1) :
    vertex h a b * vertex h a b * vertex h a b
      = photonSwitched h 0 0 (q * h) a b * photonSwitched h 0 0 (-(q' * h)) a b := by
  rw [← photonPlus_eq_switched, ← photonMinus_eq_switched]
  exact borromean_eq_two_photons H hh hq

/-! ### 2. Commuting separators -/

/-- A photon on generators `c, d` commutes with anything commuting with `c` and `d`. -/
theorem commute_photon {s c d : A} (hc : Commute s c) (hd : Commute s d) (φ : Colour R) :
    Commute s (photon c d φ) := by
  unfold photon
  exact (((Commute.one_right s).add_right (hc.smul_right φ.phi0)).add_right
    (hd.smul_right φ.phi1)).add_right ((hc.mul_right hd).smul_right φ.phi01)

/-- A separator commuting with the second photon moves past it. -/
theorem separator_commute (u g s g' w : A) (hs : Commute s g') :
    u * g * s * g' * w = u * g * g' * s * w := by
  rw [mul_assoc (u * g) s g', hs.eq, ← mul_assoc (u * g) g' s]

/-- For a cyclic trace, two commuting photons can be wrapped round a word. -/
theorem trace_wrap (t : A →ₗ[R] R) (ht : ∀ x y : A, t (x * y) = t (y * x))
    (g g' X : A) (hc : Commute g g') : t (g * X * g') = t (g * g' * X) := by
  rw [ht (g * X) g', ← mul_assoc, ← hc.eq]

/-! ### 3. The two-dimensional block -/

section TwoByTwo

variable {K : Type*} [Field K]

theorem cayleyHamilton_two (M : Matrix (Fin 2) (Fin 2) K) :
    M * M - M.trace • M + M.det • (1 : Matrix (Fin 2) (Fin 2) K) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.det_fin_two] <;> ring

/-- On a `2 × 2` representation in which `V = σ₀σ₁⁻¹` has no fixed vector
    (`det (V − 1) ≠ 0`) and is not a scalar, `tr V = −(1 + h²)` and `det V = 1`. -/
theorem vertex_trace_det_two {hK : K} {a b : Matrix (Fin 2) (Fin 2) K}
    (H : HeckeH3Rel hK a b) (hfix : (vertex hK a b - 1).det ≠ 0)
    (hscalar : ∀ c : K, vertex hK a b ≠ c • 1) :
    (vertex hK a b).trace = -(1 + hK ^ 2) ∧ (vertex hK a b).det = 1 := by
  set V := vertex hK a b with hV
  have hcub := vertex_cubic_factor H
  rw [← hV] at hcub
  have hQ : V * V + (1 + hK ^ 2) • V + 1 = 0 := by
    have hs : (V - 1).det • (V * V + (1 + hK ^ 2) • V + 1) = 0 := by
      rw [← one_mul (V * V + (1 + hK ^ 2) • V + 1), ← smul_mul_assoc, ← Matrix.adjugate_mul,
        mul_assoc, hcub, mul_zero]
    rcases smul_eq_zero.mp hs with h1 | h1
    · exact absurd h1 hfix
    · exact h1
  have key : (1 + hK ^ 2 + V.trace) • V + (1 - V.det) • (1 : Matrix (Fin 2) (Fin 2) K) = 0 := by
    calc (1 + hK ^ 2 + V.trace) • V + (1 - V.det) • (1 : Matrix (Fin 2) (Fin 2) K)
        = (V * V + (1 + hK ^ 2) • V + 1) - (V * V - V.trace • V + V.det • 1) := by module
      _ = 0 := by rw [hQ, cayleyHamilton_two V, sub_zero]
  have hα : 1 + hK ^ 2 + V.trace = 0 := by
    by_contra hne
    apply hscalar (-(1 - V.det) / (1 + hK ^ 2 + V.trace))
    have hlin : (1 + hK ^ 2 + V.trace) • V = -((1 - V.det) • (1 : Matrix (Fin 2) (Fin 2) K)) :=
      eq_neg_of_add_eq_zero_left key
    calc V = (1 + hK ^ 2 + V.trace)⁻¹ • ((1 + hK ^ 2 + V.trace) • V) := by
          rw [smul_smul, inv_mul_cancel₀ hne, one_smul]
      _ = (-(1 - V.det) / (1 + hK ^ 2 + V.trace)) • 1 := by
          rw [hlin, smul_neg, smul_smul, ← neg_smul]
          congr 1
          ring
  rw [hα, zero_smul, zero_add] at key
  have hdet : 1 - V.det = 0 := by
    rcases smul_eq_zero.mp key with h1 | h1
    · exact h1
    · exact absurd h1 one_ne_zero
  constructor
  · linear_combination hα
  · linear_combination -hdet

end TwoByTwo

/-! ### 4. Flavour no-go: flip and reversal do not change a cyclic trace -/

section Flip

/-- A factor `α·1 + β·g`, where `g` is the first (`false`) or second (`true`)
    generator. `σᵢ⁻¹ = σᵢ − h`, every typed crossing operator and its inverse
    have this form. -/
structure Factor (R : Type*) where
  α : R
  β : R
  second : Bool

/-- Swap `σ₀ ↔ σ₁` in a factor. -/
def Factor.flip (f : Factor R) : Factor R := ⟨f.α, f.β, !f.second⟩

/-- The generator named by a flag. -/
def gen (a b : A) : Bool → A
  | false => a
  | true => b

def Factor.eval (a b : A) (f : Factor R) : A := f.α • (1 : A) + f.β • gen a b f.second

/-- The product of a list of factors, in order. -/
def evalList (a b : A) (L : List (Factor R)) : A := (L.map (Factor.eval a b)).prod

/-- Coefficients on the basis `1, a, b, ab, ba, aba`. -/
structure Coeffs (R : Type*) where
  c1 : R
  ca : R
  cb : R
  cab : R
  cba : R
  caba : R

namespace Coeffs

def toA (a b : A) (c : Coeffs R) : A :=
  c.c1 • (1 : A) + c.ca • a + c.cb • b + c.cab • (a * b) + c.cba • (b * a) + c.caba • (a * (b * a))

/-- The same coefficients on the reversed basis, `ab ↔ ba`. -/
def toArev (a b : A) (c : Coeffs R) : A :=
  c.c1 • (1 : A) + c.ca • a + c.cb • b + c.cab • (b * a) + c.cba • (a * b) + c.caba • (a * (b * a))

def one : Coeffs R := ⟨1, 0, 0, 0, 0, 0⟩

def lin (x y : R) (c d : Coeffs R) : Coeffs R :=
  ⟨x * c.c1 + y * d.c1, x * c.ca + y * d.ca, x * c.cb + y * d.cb,
   x * c.cab + y * d.cab, x * c.cba + y * d.cba, x * c.caba + y * d.caba⟩

/-- Right multiplication by a generator, read off the `H₃` relations. -/
def mulGen (h : R) (c : Coeffs R) : Bool → Coeffs R
  | false => ⟨c.ca, c.c1 + h * c.ca, c.cba, c.caba, c.cb + h * c.cba, c.cab + h * c.caba⟩
  | true => ⟨c.cb, c.cab, c.c1 + h * c.cb, c.ca + h * c.cab, c.caba, c.cba + h * c.caba⟩

def mulFactor (h : R) (c : Coeffs R) (f : Factor R) : Coeffs R :=
  lin f.α f.β c (mulGen h c f.second)

theorem toA_one (a b : A) : (one : Coeffs R).toA a b = 1 := by
  simp [toA, one]

theorem toArev_one (a b : A) : (one : Coeffs R).toArev a b = 1 := by
  simp [toArev, one]

theorem toA_lin (a b : A) (x y : R) (c d : Coeffs R) :
    (lin x y c d).toA a b = x • c.toA a b + y • d.toA a b := by
  simp only [toA, lin, add_smul, smul_add, smul_smul]
  module

theorem toArev_lin (a b : A) (x y : R) (c d : Coeffs R) :
    (lin x y c d).toArev a b = x • c.toArev a b + y • d.toArev a b := by
  simp only [toArev, lin, add_smul, smul_add, smul_smul]
  module

variable (H : HeckeH3Rel h a b)
include H

theorem toA_mul_gen (c : Coeffs R) (g : Bool) :
    c.toA a b * gen a b g = (c.mulGen h g).toA a b := by
  cases g
  · simp only [toA, mulGen, gen, add_mul, smul_mul_assoc, one_mul, mul_assoc, H.quad_a,
      mul_add, mul_smul_comm, mul_one, smul_add, smul_smul, add_smul]
    module
  · simp only [toA, mulGen, gen, add_mul, smul_mul_assoc, one_mul, mul_assoc, H.quad_b,
      red_bab' H, red_aa H, mul_add, mul_smul_comm, mul_one, smul_add, smul_smul, add_smul]
    module

theorem gen_mul_toArev (c : Coeffs R) (g : Bool) :
    gen a b g * c.toArev a b = (c.mulGen h g).toArev a b := by
  cases g
  · simp only [toArev, mulGen, gen, mul_add, mul_smul_comm, mul_one, ← mul_assoc, H.quad_a,
      add_mul, smul_mul_assoc, one_mul, smul_add, smul_smul, add_smul]
    simp only [mul_assoc]
    module
  · simp only [toArev, mulGen, gen, mul_add, mul_smul_comm, mul_one, mul_assoc, red_bb H,
      red_bab H, red_bab' H, H.quad_a, H.quad_b, add_mul, smul_mul_assoc, one_mul, smul_add,
      smul_smul, add_smul]
    module

theorem toA_mul_factor (c : Coeffs R) (f : Factor R) :
    c.toA a b * f.eval a b = (c.mulFactor h f).toA a b := by
  rw [mulFactor, toA_lin, ← toA_mul_gen H, Factor.eval, mul_add, mul_smul_comm, mul_smul_comm,
    mul_one]

theorem factor_mul_toArev (c : Coeffs R) (f : Factor R) :
    f.eval a b * c.toArev a b = (c.mulFactor h f).toArev a b := by
  rw [mulFactor, toArev_lin, ← gen_mul_toArev H, Factor.eval, add_mul, smul_mul_assoc,
    smul_mul_assoc, one_mul]

end Coeffs

open Coeffs

section Expand

variable (H : HeckeH3Rel h a b)
include H

theorem toA_mul_evalList (L : List (Factor R)) (c : Coeffs R) :
    c.toA a b * evalList a b L = (L.foldl (mulFactor h) c).toA a b := by
  induction L generalizing c with
  | nil => simp [evalList]
  | cons f L ih =>
    simp only [evalList, List.map_cons, List.prod_cons, List.foldl_cons] at ih ⊢
    rw [← mul_assoc, toA_mul_factor H, ih]

theorem evalList_reverse_mul_toArev (L : List (Factor R)) (c : Coeffs R) :
    evalList a b L.reverse * c.toArev a b = (L.foldl (mulFactor h) c).toArev a b := by
  induction L generalizing c with
  | nil => simp [evalList]
  | cons f L ih =>
    simp only [evalList, List.reverse_cons, List.map_append, List.prod_append, List.map_cons,
      List.map_nil, List.prod_cons, List.prod_nil, mul_one, List.foldl_cons] at ih ⊢
    rw [mul_assoc, factor_mul_toArev H, ih]

theorem evalList_eq (L : List (Factor R)) :
    evalList a b L = (L.foldl (mulFactor h) one).toA a b := by
  rw [← toA_mul_evalList H, toA_one, one_mul]

theorem evalList_reverse_eq (L : List (Factor R)) :
    evalList a b L.reverse = (L.foldl (mulFactor h) one).toArev a b := by
  rw [← evalList_reverse_mul_toArev H, toArev_one, mul_one]

end Expand

/-- A cyclic trace does not see the exchange `ab ↔ ba`. -/
theorem trace_toArev (t : A →ₗ[R] R) (ht : ∀ x y : A, t (x * y) = t (y * x))
    (c : Coeffs R) : t (c.toArev a b) = t (c.toA a b) := by
  have hba : t (b * a) = t (a * b) := ht b a
  simp only [Coeffs.toArev, Coeffs.toA, map_add, map_smul, smul_eq_mul, hba]

/-- **Reversal.** A cyclic trace is unchanged by reversing a product of factors. -/
theorem trace_reverse (H : HeckeH3Rel h a b) (t : A →ₗ[R] R)
    (ht : ∀ x y : A, t (x * y) = t (y * x)) (L : List (Factor R)) :
    t (evalList a b L.reverse) = t (evalList a b L) := by
  rw [evalList_reverse_eq H, evalList_eq H, trace_toArev t ht]

theorem mul_inv_a (H : HeckeH3Rel h a b) : a * (a - h • 1) = 1 := by
  rw [mul_sub, mul_smul_comm, mul_one, H.quad_a]; abel

theorem inv_mul_a (H : HeckeH3Rel h a b) : (a - h • 1) * a = 1 := by
  rw [sub_mul, smul_mul_assoc, one_mul, H.quad_a]; abel

/-- The half twist `Δ = σ₀σ₁σ₀`. -/
def delta (a b : A) : A := a * (b * a)

/-- Its inverse `σ₀⁻¹σ₁⁻¹σ₀⁻¹`. -/
def deltaInv (h : R) (a b : A) : A := (a - h • 1) * ((b - h • 1) * (a - h • 1))

section Delta

variable (H : HeckeH3Rel h a b)
include H

theorem delta_mul_deltaInv : delta a b * deltaInv h a b = 1 := by
  have e1 := mul_inv_a H
  have e2 := H.mul_inv
  simp only [delta, deltaInv]
  calc a * (b * a) * ((a - h • 1) * ((b - h • 1) * (a - h • 1)))
      = a * (b * (a * (a - h • 1)) * (b - h • 1)) * (a - h • 1) := by noncomm_ring
    _ = 1 := by rw [e1, mul_one, e2, mul_one, e1]

theorem deltaInv_mul_delta : deltaInv h a b * delta a b = 1 := by
  have e1 := inv_mul_a H
  have e2 := H.inv_mul
  simp only [delta, deltaInv]
  calc (a - h • 1) * ((b - h • 1) * (a - h • 1)) * (a * (b * a))
      = (a - h • 1) * ((b - h • 1) * ((a - h • 1) * a) * b) * a := by noncomm_ring
    _ = 1 := by rw [e1, mul_one, e2, mul_one, e1]

/-- `Δ σ₀ = σ₁ Δ` and `Δ σ₁ = σ₀ Δ`. -/
theorem delta_mul_gen (g : Bool) : delta a b * gen a b g = gen a b (!g) * delta a b := by
  have hb := H.braid
  cases g
  · simp only [delta, gen, Bool.not_false]
    calc a * (b * a) * a = (a * b * a) * a := by noncomm_ring
      _ = (b * a * b) * a := by rw [hb]
      _ = b * (a * (b * a)) := by noncomm_ring
  · simp only [delta, gen, Bool.not_true]
    calc a * (b * a) * b = a * (b * a * b) := by noncomm_ring
      _ = a * (a * b * a) := by rw [hb]
      _ = a * (a * (b * a)) := by noncomm_ring

theorem delta_mul_factor (f : Factor R) :
    delta a b * f.eval a b = f.flip.eval a b * delta a b := by
  simp only [Factor.eval, Factor.flip, mul_add, add_mul, mul_smul_comm, smul_mul_assoc, mul_one,
    one_mul, delta_mul_gen H]

theorem delta_mul_evalList (L : List (Factor R)) :
    delta a b * evalList a b L = evalList a b (L.map Factor.flip) * delta a b := by
  induction L with
  | nil => simp [evalList]
  | cons f L ih =>
    simp only [evalList, List.map_cons, List.prod_cons] at ih ⊢
    rw [← mul_assoc, delta_mul_factor H, mul_assoc, ih, mul_assoc]

end Delta

/-- **Flip.** Swapping `σ₀ ↔ σ₁` in every factor does not change a cyclic trace:
    the swap is conjugation by `Δ`. -/
theorem trace_flip (H : HeckeH3Rel h a b) (t : A →ₗ[R] R)
    (ht : ∀ x y : A, t (x * y) = t (y * x)) (L : List (Factor R)) :
    t (evalList a b (L.map Factor.flip)) = t (evalList a b L) := by
  calc t (evalList a b (L.map Factor.flip))
      = t (evalList a b (L.map Factor.flip) * delta a b * deltaInv h a b) := by
        rw [mul_assoc, delta_mul_deltaInv H, mul_one]
    _ = t (delta a b * evalList a b L * deltaInv h a b) := by rw [delta_mul_evalList H]
    _ = t (evalList a b L * deltaInv h a b * delta a b) := by
        rw [mul_assoc, ht (delta a b) _]
    _ = t (evalList a b L) := by rw [mul_assoc, deltaInv_mul_delta H, mul_one]

/-- **Flavour no-go.** For any cyclic trace, a product of factors `α·1 + β·σᵢ`
    and its image under the anti-automorphism `θ` (swap `σ₀ ↔ σ₁`, reverse the
    order) have the same trace. So no trace separates two nucleon words related
    by `θ`. -/
theorem trace_flip_reverse (H : HeckeH3Rel h a b) (t : A →ₗ[R] R)
    (ht : ∀ x y : A, t (x * y) = t (y * x)) (L : List (Factor R)) :
    t (evalList a b (L.map Factor.flip).reverse) = t (evalList a b L) := by
  rw [trace_reverse H t ht, trace_flip H t ht]

end Flip

end QOU.Mass.PhotonTraceLemmas
