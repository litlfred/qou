import Mathlib.Tactic
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.FreeAlgebra

/-!
# The Iwahori–Hecke algebra `H_{n+1}(q)`, presented

Bean `qou-k4oq`, **layer 1**. Built from scratch: **Mathlib has no Hecke algebras.**

Measured 2026-09-05 — Mathlib contains **zero** files matching `HeckeAlgebra`,
`IwahoriHecke`, `QuantumGroup`, `BraidGroup`, `RMatrix`, `YangBaxter` or
`TemperleyLieb`. Only `GroupTheory.Coxeter` exists. So there is nothing to build on
and nothing to import; this file is the foundation.

## What is here (layer 1: the presentation and its algebra)

`H_{n+1}(q)` on generators `σ_0 … σ_{n-1}` (`n+1` strands) as a `RingQuot` of
`FreeAlgebra R (Fin n)`, in the corpus's convention (AGENTS.md §7a), over a generic
`CommRing R` with `q : Rˣ` — no `ℝ`, per §7c.

* `sigma_sq` — the quadratic relation `σ_i² = h σ_i + 1`, `h = q − q⁻¹`.
* `sigma_braid`, `sigma_far` — the braid and far-commutation relations.
* `sigma_eigen` — `(σ_i − q)(σ_i + q⁻¹) = 0`: the two eigenvalues `q` (symmetric
  channel) and `−q⁻¹` (antisymmetric), which is what makes the skein relation work.
* `sigmaUnit` — `σ_i` is a **unit**, with the explicit inverse `σ_i − h`.
* `skein` — `σ_i − σ_i⁻¹ = q − q⁻¹`, i.e. `L₊ − L₋ = (q−q⁻¹) L₀`.
* `hParam_one`, `sigma_sq_of_hParam_eq_zero` — at `q = 1` the deformation vanishes and
  the quadratic relation becomes `σ_i² = 1`, the `S_{n+1}` group-algebra presentation.
* `lift`, `lift_sigma`, `algHom_ext` — **the universal property.** Without this the
  presentation is inert; it is what lets a representation, a trace, or any other map
  *out of* `H_{n+1}(q)` be defined by naming generator images and checking three
  relations.

## 🛑 What is NOT here — and one of these is a soundness caveat, not a wishlist

* **NONTRIVIALITY IS NOT PROVED.** Nothing here shows `H_{n+1}(q) ≠ 0`. A presentation
  whose relations collapse would satisfy every theorem above *vacuously*. Establishing
  `dim = (n+1)!` needs the **`T_w` basis theorem** (Bourbaki/Matsumoto: a reduced word
  gives a well-defined `T_w`, independent of reduction), which is the deep result of
  the subject and is **layer 2**. Until it lands, do not read these theorems as
  statements about a nonzero algebra.
* No `T_w` basis, no length function, no Kazhdan–Lusztig basis.
* No **Markov trace**, no Wedderburn/Hoefsmit decomposition — those are layers 3–4 and
  are what bean `qou-mpq5` scoped as the multi-week piece.
* No R-matrix, and hence no quantum Schur–Weyl. `WeightedPermutationCharacter` closed
  the *trace-weight* half of `q ≠ 1`; the **braiding** half needs this algebra plus its
  representation theory, i.e. layers 2–4.

-- Ref: [manuscript] bean qou-k4oq; the Iwahori–Hecke presentation is standard
-- (Iwahori 1964; Jones 1987 for the skein/Markov reading used by this corpus).
-/

namespace QOU.IwahoriHecke

open FreeAlgebra

variable (R : Type*) [CommRing R] (q : Rˣ) (n : ℕ)

/-- `h = q − q⁻¹`, the Hecke deformation parameter. At `q = 1` it vanishes and the
quadratic relation degenerates to `σ² = 1`. -/
def hParam : R := (q : R) - (↑q⁻¹ : R)

/-- The defining relations of the Iwahori–Hecke algebra `H_{n+1}(q)` on `n` generators
`σ_0 … σ_{n-1}` (so `n + 1` strands), in the corpus's convention (AGENTS.md §7a):

* **quadratic** `σ_i² = (q − q⁻¹) σ_i + 1`, equivalently `(σ_i − q)(σ_i + q⁻¹) = 0`;
* **braid** `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`;
* **far commutation** `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`. -/
inductive HeckeRel : FreeAlgebra R (Fin n) → FreeAlgebra R (Fin n) → Prop
  | quadratic (i : Fin n) :
      HeckeRel (ι R i * ι R i) (algebraMap R _ (hParam R q) * ι R i + 1)
  | braid (i j : Fin n) (hij : (i : ℕ) + 1 = (j : ℕ)) :
      HeckeRel (ι R i * ι R j * ι R i) (ι R j * ι R i * ι R j)
  | far (i j : Fin n) (hij : (i : ℕ) + 1 < (j : ℕ)) :
      HeckeRel (ι R i * ι R j) (ι R j * ι R i)

/-- The Iwahori–Hecke algebra `H_{n+1}(q)`, presented by generators and relations. -/
def HeckeAlgebra := RingQuot (HeckeRel R q n)

namespace HeckeAlgebra

instance : Ring (HeckeAlgebra R q n) := inferInstanceAs (Ring (RingQuot _))
instance : Algebra R (HeckeAlgebra R q n) := inferInstanceAs (Algebra R (RingQuot _))

variable {R q n}

/-- The braid generator `σ_i` in `H_{n+1}(q)`. -/
def sigma (i : Fin n) : HeckeAlgebra R q n :=
  RingQuot.mkAlgHom R (HeckeRel R q n) (ι R i)

/-- **The quadratic relation.** `σ_i² = h σ_i + 1` with `h = q − q⁻¹`. -/
theorem sigma_sq (i : Fin n) :
    sigma (q := q) i * sigma i = algebraMap R _ (hParam R q) * sigma i + 1 := by
  have := RingQuot.mkAlgHom_rel R (s := HeckeRel R q n) (HeckeRel.quadratic (R := R) (q := q) i)
  simpa [sigma] using this

/-- **The braid relation.** -/
theorem sigma_braid (i j : Fin n) (hij : (i : ℕ) + 1 = (j : ℕ)) :
    sigma (q := q) i * sigma j * sigma i = sigma j * sigma i * sigma j := by
  have := RingQuot.mkAlgHom_rel R (s := HeckeRel R q n) (HeckeRel.braid (R := R) (q := q) i j hij)
  simpa [sigma] using this

/-- **Far commutation.** -/
theorem sigma_far (i j : Fin n) (hij : (i : ℕ) + 1 < (j : ℕ)) :
    sigma (q := q) i * sigma j = sigma j * sigma i := by
  have := RingQuot.mkAlgHom_rel R (s := HeckeRel R q n) (HeckeRel.far (R := R) (q := q) i j hij)
  simpa [sigma] using this

/-- **The eigenvalue factorisation** `(σ_i − q)(σ_i + q⁻¹) = 0`: the generator has the
two eigenvalues `q` (symmetric channel) and `−q⁻¹` (antisymmetric channel). -/
theorem sigma_eigen (i : Fin n) :
    (sigma (q := q) i - algebraMap R _ (q : R)) *
      (sigma i + algebraMap R _ (↑q⁻¹ : R)) = 0 := by
  have hs := sigma_sq (q := q) i
  have hc : ∀ r : R, algebraMap R (HeckeAlgebra R q n) r * sigma i
      = sigma i * algebraMap R _ r := fun r => Algebra.commutes r (sigma i)
  have hab : algebraMap R (HeckeAlgebra R q n) (q : R) * algebraMap R _ (↑q⁻¹ : R) = 1 := by
    rw [← map_mul, q.mul_inv, map_one]
  have hsub : algebraMap R (HeckeAlgebra R q n) (hParam R q)
      = algebraMap R _ (q : R) - algebraMap R _ (↑q⁻¹ : R) := by
    rw [hParam, map_sub]
  calc (sigma (q := q) i - algebraMap R _ (q : R)) * (sigma i + algebraMap R _ (↑q⁻¹ : R))
      = sigma i * sigma i + sigma i * algebraMap R _ (↑q⁻¹ : R)
        - algebraMap R _ (q : R) * sigma i
        - algebraMap R _ (q : R) * algebraMap R _ (↑q⁻¹ : R) := by noncomm_ring
    _ = (algebraMap R _ (hParam R q) * sigma i + 1)
        + sigma i * algebraMap R _ (↑q⁻¹ : R)
        - algebraMap R _ (q : R) * sigma i - 1 := by rw [hs, hab]
    _ = (algebraMap R _ (q : R) - algebraMap R _ (↑q⁻¹ : R)) * sigma i
        + sigma i * algebraMap R _ (↑q⁻¹ : R)
        - algebraMap R _ (q : R) * sigma i - 1 + 1 := by rw [hsub]; noncomm_ring
    _ = sigma i * algebraMap R _ (↑q⁻¹ : R)
        - algebraMap R _ (↑q⁻¹ : R) * sigma i := by noncomm_ring
    _ = 0 := by rw [hc]; noncomm_ring

/-- **`σ_i` is a unit**, with the explicit inverse `σ_i − h`. -/
theorem sigma_mul_sub (i : Fin n) :
    sigma (q := q) i * (sigma i - algebraMap R _ (hParam R q)) = 1 := by
  have hs := sigma_sq (q := q) i
  have hcomm : algebraMap R (HeckeAlgebra R q n) (hParam R q) * sigma i
      = sigma i * algebraMap R _ (hParam R q) := Algebra.commutes _ _
  rw [mul_sub, hs, hcomm]
  noncomm_ring

theorem sub_mul_sigma (i : Fin n) :
    (sigma (q := q) i - algebraMap R _ (hParam R q)) * sigma i = 1 := by
  have hs := sigma_sq (q := q) i
  have hcomm : algebraMap R (HeckeAlgebra R q n) (hParam R q) * sigma i
      = sigma i * algebraMap R _ (hParam R q) := Algebra.commutes _ _
  rw [sub_mul, hs]
  noncomm_ring

/-- `σ_i` as a unit of the algebra. -/
def sigmaUnit (i : Fin n) : (HeckeAlgebra R q n)ˣ where
  val := sigma i
  inv := sigma i - algebraMap R _ (hParam R q)
  val_inv := sigma_mul_sub i
  inv_val := sub_mul_sigma i

/-- **The skein relation** `σ_i − σ_i⁻¹ = q − q⁻¹` (AGENTS.md §7a): the Hecke quadratic
relation multiplied through by `σ_i⁻¹`. In knot-theoretic terms `L₊ − L₋ = (q−q⁻¹) L₀`. -/
theorem skein (i : Fin n) :
    sigma (q := q) i - ↑(sigmaUnit (q := q) i)⁻¹ = algebraMap R _ (hParam R q) := by
  show sigma i - (sigma i - algebraMap R _ (hParam R q)) = _
  exact sub_sub_cancel _ _

/-- **At `q = 1` the deformation vanishes**: `h = 0`, so the quadratic relation becomes
`σ_i² = 1` and the algebra degenerates to the group-algebra presentation of `S_{n+1}`. -/
theorem hParam_one : hParam R (1 : Rˣ) = 0 := by simp [hParam]

theorem sigma_sq_of_hParam_eq_zero (i : Fin n) (h0 : hParam R q = 0) :
    sigma (q := q) i * sigma i = 1 := by
  rw [sigma_sq, h0]; simp

/-! ### The universal property

Without this the presentation is inert: it is what lets a representation, a trace, or
any other map *out of* `H_{n+1}(q)` be defined by naming the images of the generators
and checking the three relations. -/

variable {A : Type*} [Ring A] [Algebra R A]

/-- **The universal property.** A family satisfying the three Hecke relations extends
to an algebra map out of `H_{n+1}(q)`. -/
theorem lift_rel (f : Fin n → A)
    (hquad : ∀ i, f i * f i = algebraMap R A (hParam R q) * f i + 1)
    (hbraid : ∀ i j : Fin n, (i : ℕ) + 1 = (j : ℕ) → f i * f j * f i = f j * f i * f j)
    (hfar : ∀ i j : Fin n, (i : ℕ) + 1 < (j : ℕ) → f i * f j = f j * f i) :
    ∀ ⦃x y⦄, HeckeRel R q n x y → FreeAlgebra.lift R f x = FreeAlgebra.lift R f y := by
  rintro x y hrel
  cases hrel with
  | quadratic i => simp [hquad]
  | braid i j hij => simpa using hbraid i j hij
  | far i j hij => simpa using hfar i j hij

def lift (f : Fin n → A)
    (hquad : ∀ i, f i * f i = algebraMap R A (hParam R q) * f i + 1)
    (hbraid : ∀ i j : Fin n, (i : ℕ) + 1 = (j : ℕ) → f i * f j * f i = f j * f i * f j)
    (hfar : ∀ i j : Fin n, (i : ℕ) + 1 < (j : ℕ) → f i * f j = f j * f i) :
    HeckeAlgebra R q n →ₐ[R] A :=
  RingQuot.liftAlgHom R ⟨FreeAlgebra.lift R f, lift_rel f hquad hbraid hfar⟩

@[simp] theorem lift_sigma (f : Fin n → A)
    (hquad : ∀ i, f i * f i = algebraMap R A (hParam R q) * f i + 1)
    (hbraid : ∀ i j : Fin n, (i : ℕ) + 1 = (j : ℕ) → f i * f j * f i = f j * f i * f j)
    (hfar : ∀ i j : Fin n, (i : ℕ) + 1 < (j : ℕ) → f i * f j = f j * f i) (i : Fin n) :
    lift (q := q) f hquad hbraid hfar (sigma i) = f i := by
  show RingQuot.liftAlgHom R ⟨FreeAlgebra.lift R f, lift_rel f hquad hbraid hfar⟩
      (RingQuot.mkAlgHom R (HeckeRel R q n) (ι R i)) = f i
  rw [RingQuot.liftAlgHom_mkAlgHom_apply]
  simp

/-- Two algebra maps out of `H_{n+1}(q)` agreeing on the generators are equal. -/
theorem algHom_ext {F G : HeckeAlgebra R q n →ₐ[R] A}
    (h : ∀ i, F (sigma i) = G (sigma i)) : F = G := by
  refine RingQuot.ringQuot_ext' (S := R) F G ?_
  refine FreeAlgebra.hom_ext (funext fun i => ?_)
  simpa [sigma] using h i

end HeckeAlgebra
end QOU.IwahoriHecke
