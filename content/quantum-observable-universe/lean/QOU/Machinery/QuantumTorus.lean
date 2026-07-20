import Mathlib.Tactic
import Mathlib.Algebra.SkewMonoidAlgebra.Basic

/-!
# QOU.Machinery.QuantumTorus — the skew-Laurent q-Weyl ring (NT-T2 brick B1)

**The quantum torus `T = R⟨L^±,M^±⟩/(LM − q²ML)` as a skew-Laurent ring.**

Brick B1 of the Nguyen–Tran strong-AJ decomposition
(`docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md`).  The
paper's quantum torus is the skew-Laurent presentation `A[L^±; σ]` with
coefficient ring `A = R[M^±]` and `σ(M) = q²·M` (paper: `t²`, corpus:
`q = t⁴`).  This file realises it on Mathlib's early-stage
`Mathlib.Algebra.SkewMonoidAlgebra` with the L-degree group
`G = Multiplicative ℤ` acting on `A` by the automorphism `σ`
(the action of `Multiplicative.ofAdd 1`).

`SkewMonoidAlgebra A (Multiplicative ℤ)` is *exactly* the skew-Laurent
ring: finitely-supported `ℤ → A` with the twisted product
`single m a · single n b = single (m+n) (a · σᵐ b)` (Mathlib
`single_mul_single`).  Its `support : Finset (Multiplicative ℤ)` is the
L-degree structure that brick B3 (skew-Euclidean division) divides on.

## What is proved here (sorry-free)

* `sigma` — the σ-twist (action of `ofAdd 1`), a ring automorphism of `A`.
* `emb : A →+* QuantumTorus A` — the coefficient (M-side) embedding.
* `Lgen`, `Linv` — the `L^{±1}` generators, with `Lgen * Linv = 1 = Linv * Lgen`
  (`Lgen` is a **unit**: `LUnit`).
* `Lgen_mul_emb` — the **q-Weyl commutation** `L · a = σ(a) · L` (and the
  `L⁻¹` transpose).  With a distinguished `σ`-eigenvector `M` (`σ M = c·M`)
  this specialises to the paper's `L·M = c·M·L` (`qWeyl_eigen_commutation`,
  `c = q²`).
* Degree / basis basics: `emb`/`Lgen`/monomial `coeff` lemmas, `Lgen ≠ 0`,
  `single`-monomial support.
* **Evaluation to the function model** (`ℕ → K`, the corpus `QDifferenceOperator`
  carrier of `QOU.BraidKnot.AJFigureEight`): the shift `shiftFwd` and
  scalar-power `mulPow q` operators satisfy the q-Weyl relation
  `shiftFwd ∘ mulPow q = q • (mulPow q ∘ shiftFwd)`
  (`funcModel_qWeyl`) — so the corpus tower operators are a genuine q-Weyl
  representation.
* `torusEval` — the universal ring-hom evaluation of the torus into any
  semiring, from a coefficient ring-hom + an image unit for `L` satisfying
  the twist compatibility (a thin re-exposure of `liftNCRingHom`).

## Base ring (§7c)

Generic `{A : Type*} [CommRing A]` for the coefficient ring and generic
`{K : Type*} [Field K]` for the function model.  No `ℝ`, no ordering, no
archimedean construct: the whole file is algebraic.  Inverses in the
function model use `[Field K]` only through scalar powers `q^N`.
-/

noncomputable section

namespace QOU.Machinery.QuantumTorus

open SkewMonoidAlgebra

/-- The L-degree group: `Multiplicative ℤ`, additively the `L`-exponent. -/
abbrev Ldeg := Multiplicative ℤ

variable {A : Type*} [CommRing A] [MulSemiringAction Ldeg A]

set_option linter.dupNamespace false in
/-- **The quantum torus** as the skew-Laurent ring `A[L^±; σ]`:
    finitely-supported `ℤ → A` with the σ-twisted product.  Here `A = R[M^±]`
    is the M-coefficient ring and the L-degree group `Multiplicative ℤ` acts
    by the twist automorphism `σ`. -/
abbrev QuantumTorus (A : Type*) [Semiring A] [MulSemiringAction Ldeg A] :=
  SkewMonoidAlgebra A Ldeg

/-- The σ-twist automorphism of the coefficient ring: the action of the
    L-degree generator `ofAdd 1`.  For the paper's torus `σ(M) = q²·M`. -/
def sigma (a : A) : A := (Multiplicative.ofAdd (1 : ℤ)) • a

@[simp] theorem sigma_def (a : A) :
    sigma a = (Multiplicative.ofAdd (1 : ℤ)) • a := rfl

/-- `σ` is multiplicative (it is a ring-automorphism action). -/
theorem sigma_mul (a b : A) : sigma (a * b) = sigma a * sigma b := by
  simp [sigma, smul_mul']

/-- `σ 1 = 1`. -/
@[simp] theorem sigma_one : sigma (1 : A) = 1 := by simp [sigma]

/-! ### Coefficient embedding and the `L^{±1}` generators -/

/-- The coefficient (M-side) embedding `A → T`, `a ↦ single 1 a` — a ring
    homomorphism (`single 1` is multiplicative because `1 • b = b`). -/
def emb : A →+* QuantumTorus A where
  toFun a := single (1 : Ldeg) a
  map_one' := (one_def).symm
  map_mul' a b := by
    rw [single_mul_single, one_mul, one_smul]
  map_zero' := single_zero _
  map_add' a b := single_add _ a b

@[simp] theorem emb_apply (a : A) : emb a = single (1 : Ldeg) a := rfl

/-- `L`: the positive skew generator. -/
def Lgen : QuantumTorus A := single (Multiplicative.ofAdd (1 : ℤ)) 1

/-- `L⁻¹`: the negative skew generator. -/
def Linv : QuantumTorus A := single (Multiplicative.ofAdd (-1 : ℤ)) 1

theorem Lgen_mul_Linv : (Lgen * Linv : QuantumTorus A) = 1 := by
  rw [Lgen, Linv, single_mul_single, smul_one, mul_one, ← ofAdd_add,
    show (1 : ℤ) + -1 = 0 by ring, ofAdd_zero, one_def]

theorem Linv_mul_Lgen : (Linv * Lgen : QuantumTorus A) = 1 := by
  rw [Lgen, Linv, single_mul_single, smul_one, mul_one, ← ofAdd_add,
    show (-1 : ℤ) + 1 = 0 by ring, ofAdd_zero, one_def]

/-- `L` is a unit of the quantum torus. -/
def LUnit : (QuantumTorus A)ˣ where
  val := Lgen
  inv := Linv
  val_inv := Lgen_mul_Linv
  inv_val := Linv_mul_Lgen

@[simp] theorem LUnit_val : (LUnit : (QuantumTorus A)ˣ).val = Lgen := rfl

/-! ### The q-Weyl commutation relation -/

/-- **q-Weyl commutation (skew relation), `L · a = σ(a) · L`.**  This is the
    defining relation of the quantum torus: moving `L` past a coefficient
    twists it by `σ`.  With `σ(M) = q²·M` it is the paper's `LM = q²ML`. -/
theorem Lgen_mul_emb (a : A) :
    (Lgen * emb a : QuantumTorus A) = emb (sigma a) * Lgen := by
  rw [Lgen, emb_apply, emb_apply, single_mul_single, single_mul_single]
  simp only [mul_one, one_smul, one_mul, sigma_def]

/-- The `L⁻¹` transpose of the commutation: `L⁻¹ · σ(a) = a · L⁻¹`. -/
theorem Linv_mul_emb_sigma (a : A) :
    (Linv * emb (sigma a) : QuantumTorus A) = emb a * Linv := by
  rw [Linv, emb_apply, emb_apply, single_mul_single, single_mul_single,
    sigma_def, ← mul_smul, ← ofAdd_add]
  simp only [mul_one, one_mul, one_smul]
  rw [show (-1 : ℤ) + 1 = 0 by ring, ofAdd_zero, one_smul]

/-- **Eigen-commutation (the paper's `LM = c·ML`).**  If `M : A` is a
    σ-eigenvector, `σ(M) = c·M`, then `L·M = c·(M·L)` in the torus.  For the
    figure-eight torus `c = q²` (paper `t²`). -/
theorem qWeyl_eigen_commutation (M c : A) (hM : sigma M = c * M) :
    (Lgen * emb M : QuantumTorus A) = emb c * (emb M * Lgen) := by
  rw [Lgen_mul_emb, hM, ← mul_assoc, ← map_mul]

/-! ### Degree / support basics (feeds B2 normal form and B3 division) -/

@[simp] theorem coeff_emb (a : A) (x : Ldeg) :
    (emb a : QuantumTorus A).coeff x = if x = 1 then a else 0 := by
  rw [emb_apply, coeff_single]
  by_cases h : x = 1 <;> simp [Pi.single_apply, h]

@[simp] theorem coeff_Lgen (x : Ldeg) :
    (Lgen : QuantumTorus A).coeff x
      = if x = Multiplicative.ofAdd (1 : ℤ) then 1 else 0 := by
  rw [Lgen, coeff_single]
  by_cases h : x = Multiplicative.ofAdd (1 : ℤ) <;> simp [Pi.single_apply, h]

/-- `L ≠ 0` (over a nontrivial coefficient ring): its `ofAdd 1` coefficient
    is `1 ≠ 0`. -/
theorem Lgen_ne_zero [Nontrivial A] : (Lgen : QuantumTorus A) ≠ 0 := by
  intro h
  have : (Lgen : QuantumTorus A).coeff (Multiplicative.ofAdd (1 : ℤ)) = 0 := by
    rw [h]; simp
  rw [coeff_Lgen] at this
  simp at this

set_option linter.unusedSectionVars false in
/-- A single monomial `single n a` with `a ≠ 0` has support `{n}` — the
    L-degree of a monomial is its exponent (used by B2/B3). -/
theorem support_single_of_ne {n : Ldeg} {a : A} (ha : a ≠ 0) :
    (single n a : QuantumTorus A).support = {n} := by
  ext x
  rw [mem_support_iff, Finset.mem_singleton, coeff_single, Pi.single_apply]
  by_cases hx : x = n
  · simp [hx, ha]
  · simp [hx]

/-! ### Evaluation to the function model `ℕ → K` (interoperates with
`QOU.BraidKnot.AJFigureEight`) -/

variable {K : Type*} [Field K]

/-- The forward shift on colour towers, `L`'s image in the function model:
    `(shiftFwd J)(N) = J (N+1)` — the corpus `QDifferenceOperator` uses this
    via `J (N + j)`. -/
def shiftFwd (J : ℕ → K) : ℕ → K := fun N => J (N + 1)

/-- The multiplication-by-`q^N` operator, `M`'s image in the function model
    (`m = q^N`, the corpus meridian convention): `(mulPow q J)(N) = q^N · J N`. -/
def mulPow (q : K) (J : ℕ → K) : ℕ → K := fun N => q ^ N * J N

/-- **q-Weyl relation in the function model.**  The shift and
    scalar-power operators satisfy `shiftFwd ∘ mulPow q = q • (mulPow q ∘
    shiftFwd)` — i.e. `L·M = q·M·L` on `ℕ → K`.  This exhibits the corpus's
    colored-Jones tower operators as a genuine q-Weyl representation of the
    quantum torus (the `evaluation map to the function model`). -/
theorem funcModel_qWeyl (q : K) (J : ℕ → K) :
    shiftFwd (mulPow q J) = q • (mulPow q (shiftFwd J)) := by
  funext N
  simp only [shiftFwd, mulPow, Pi.smul_apply, smul_eq_mul]
  rw [pow_succ]
  ring

/-- **Universal evaluation of the quantum torus.**  Given a semiring `R`, a
    coefficient ring-hom `φ : A →+* R`, a unit `ℓ : Rˣ` (the image of `L`)
    and the twist compatibility `φ(y • a) · ℓ^y = ℓ^y · φ(a)` for every
    L-degree `y`, there is a ring-hom `T → R`.  A thin re-exposure of
    `liftNCRingHom` specialised to the L-degree group; the caller supplies
    the crossed-product compatibility. -/
def torusEval {R : Type*} [Semiring R] (φ : A →+* R) (ℓ : Rˣ)
    (hcomm : ∀ (a : A) (y : Ldeg),
      φ (y • a) * ((zpowersHom Rˣ ℓ) y : R) = ((zpowersHom Rˣ ℓ) y : R) * φ a) :
    QuantumTorus A →+* R :=
  liftNCRingHom φ ((Units.coeHom R).comp (zpowersHom Rˣ ℓ))
    (fun {x} {y} => hcomm x y)

theorem torusEval_emb {R : Type*} [Semiring R] (φ : A →+* R) (ℓ : Rˣ)
    (hcomm) (a : A) :
    torusEval φ ℓ hcomm (emb a) = φ a := by
  show liftNC (φ : A →+ R) ((Units.coeHom R).comp (zpowersHom Rˣ ℓ) : Ldeg → R)
      (single 1 a) = φ a
  rw [liftNC_single]
  simp

end QOU.Machinery.QuantumTorus
