/-
Copyright (c) 2026 QOU authors. Released under the Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# The rank-two Hecke (Iwahori) algebra and its Ocneanu/Markov trace

This file constructs, concretely and sorry-free, the **single-generator Hecke
algebra** `H₂(q) = R[σ] / (σ² = h·σ + 1)` (with `h = q - q⁻¹` the substrate
bandwidth) as a rank-two free `R`-algebra, and equips it with the
**Ocneanu/Markov trace** `tr(a·1 + b·σ) = a + z·b`.

## Why this exists

`QOU.MathlibExt.OcneanuTrace` defines the *abstract* Markov-trace functional
(the tower `H`, generators `g`/`ginv`, the parameters `z`/`zinv`, the trace and
Markov axioms) and derives its general consequences. Two concrete instances of
that structure already exist in the corpus:

* `unitMarkovTrace` — `A = R`, generators are scalar units. Non-degenerate in
  `z` but degenerate in the algebra (no genuine crossing).
* `QOU.MathlibExt.SymmetricGroupTowerWitness` — the genuine growing
  **non-commutative** tower `MonoidAlgebra R (Equiv.Perm ℕ)`, but at **q = 1**,
  where every generator squares to `1` (`h = 0`) and the Markov parameter is
  forced to `z = 0`. It exercises the tower/filtration content but **not** the
  Hecke quadratic relation at `q ≠ 1`.

The piece those two miss — and which this file supplies — is a concrete algebra
in which the **quadratic relation `σ² = h·σ + 1` genuinely bites**: `h ≠ 0`,
the two Markov parameters differ (`zinv = z - h ≠ z`), and the trace is
**not** multiplicative on `σ`. That is exactly the `q ≠ 1` content, at the
smallest level (one generator, `H₂`).

## Scope (what this does NOT do)

`H₂` has a single generator, so it cannot instantiate the *infinite* tower of
`OcneanuTrace.MarkovTrace`: the stabilisation axiom `tr(a · g n) = z · tr a`
for every level `n` forces degeneracy once the tower stops growing. The genuine
non-commutative Hecke tower `H_∞(q)` at `q ≠ 1` — where the braid relation is
written and `SandwichReduces` must be proved by rewriting rather than by a
permutation-support argument — remains the hard-Mathlib-gap epic (bean
`qou-08a2` / `qou-301d`). This file is the `q ≠ 1`, single-generator
**witness**, complementary to the `q = 1`, infinite-tower symmetric-group
witness.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/

namespace QOU.MathlibExt.HeckeRankTwoMarkov

variable {R : Type*} [CommRing R]

/-- An element of the rank-two Hecke algebra `R[σ]/(σ² = h·σ + 1)`, written
`const · 1 + gen · σ`.  The bandwidth `h` is a type index so that the ring
structure can depend on it. -/
@[ext]
structure Hecke2 (R : Type*) [CommRing R] (h : R) where
  /-- Coefficient of `1`. -/
  const : R
  /-- Coefficient of the generator `σ`. -/
  gen : R

namespace Hecke2

variable {h : R}

/-! ### Ring data -/

instance : Zero (Hecke2 R h) := ⟨⟨0, 0⟩⟩
instance : One (Hecke2 R h) := ⟨⟨1, 0⟩⟩
instance : Add (Hecke2 R h) := ⟨fun x y => ⟨x.const + y.const, x.gen + y.gen⟩⟩
instance : Neg (Hecke2 R h) := ⟨fun x => ⟨-x.const, -x.gen⟩⟩
/-- Multiplication: `(a + bσ)(c + dσ) = (ac + bd) + (ad + bc + h·bd)σ`, using
`σ² = h·σ + 1`. -/
instance : Mul (Hecke2 R h) :=
  ⟨fun x y => ⟨x.const * y.const + x.gen * y.gen,
               x.const * y.gen + x.gen * y.const + h * (x.gen * y.gen)⟩⟩
/-- Scalar action, component-wise. -/
instance : SMul R (Hecke2 R h) := ⟨fun r x => ⟨r * x.const, r * x.gen⟩⟩

@[simp] lemma zero_const : (0 : Hecke2 R h).const = 0 := rfl
@[simp] lemma zero_gen : (0 : Hecke2 R h).gen = 0 := rfl
@[simp] lemma one_const : (1 : Hecke2 R h).const = 1 := rfl
@[simp] lemma one_gen : (1 : Hecke2 R h).gen = 0 := rfl
@[simp] lemma add_const (x y : Hecke2 R h) : (x + y).const = x.const + y.const := rfl
@[simp] lemma add_gen (x y : Hecke2 R h) : (x + y).gen = x.gen + y.gen := rfl
@[simp] lemma neg_const (x : Hecke2 R h) : (-x).const = -x.const := rfl
@[simp] lemma neg_gen (x : Hecke2 R h) : (-x).gen = -x.gen := rfl
@[simp] lemma mul_const (x y : Hecke2 R h) :
    (x * y).const = x.const * y.const + x.gen * y.gen := rfl
@[simp] lemma mul_gen (x y : Hecke2 R h) :
    (x * y).gen = x.const * y.gen + x.gen * y.const + h * (x.gen * y.gen) := rfl
@[simp] lemma smul_const (r : R) (x : Hecke2 R h) : (r • x).const = r * x.const := rfl
@[simp] lemma smul_gen (r : R) (x : Hecke2 R h) : (r • x).gen = r * x.gen := rfl

/-! ### Ring and algebra structure -/

instance : AddCommGroup (Hecke2 R h) where
  add := (· + ·)
  neg := Neg.neg
  zero := 0
  nsmul := @nsmulRec _ ⟨(0 : Hecke2 R h)⟩ ⟨(· + ·)⟩
  zsmul := @zsmulRec _ ⟨(0 : Hecke2 R h)⟩ ⟨(· + ·)⟩ ⟨Neg.neg⟩
    (@nsmulRec _ ⟨(0 : Hecke2 R h)⟩ ⟨(· + ·)⟩)
  add_zero _ := by ext <;> simp
  zero_add _ := by ext <;> simp
  add_comm _ _ := by ext <;> simp <;> ring
  add_assoc _ _ _ := by ext <;> simp <;> ring
  neg_add_cancel _ := by ext <;> simp

instance : AddGroupWithOne (Hecke2 R h) :=
  { (inferInstance : AddCommGroup (Hecke2 R h)) with one := 1 }

instance : CommRing (Hecke2 R h) where
  __ := (inferInstance : AddCommGroup (Hecke2 R h))
  __ := (inferInstance : AddGroupWithOne (Hecke2 R h))
  mul := (· * ·)
  npow := @npowRec _ ⟨(1 : Hecke2 R h)⟩ ⟨(· * ·)⟩
  mul_zero _ := by ext <;> simp
  zero_mul _ := by ext <;> simp
  mul_one _ := by ext <;> simp
  one_mul _ := by ext <;> simp
  mul_comm _ _ := by ext <;> simp <;> ring
  mul_assoc _ _ _ := by ext <;> simp <;> ring
  left_distrib _ _ _ := by ext <;> simp <;> ring
  right_distrib _ _ _ := by ext <;> simp <;> ring

instance : Algebra R (Hecke2 R h) where
  smul r x := ⟨r * x.const, r * x.gen⟩
  algebraMap :=
    { toFun := fun r => ⟨r, 0⟩
      map_one' := by ext <;> simp
      map_mul' := by intro _ _; ext <;> simp <;> ring
      map_zero' := by ext <;> simp
      map_add' := by intro _ _; ext <;> simp }
  commutes' _ _ := by ext <;> simp <;> ring
  smul_def' _ _ := by ext <;> simp <;> ring

/-! ### The generator and the quadratic relation -/

/-- The Hecke generator `σ = 0·1 + 1·σ`. -/
def sigma : Hecke2 R h := ⟨0, 1⟩

/-- The inverse generator `σ⁻¹ = σ - h·1 = -h·1 + 1·σ`. -/
def sigmaInv : Hecke2 R h := ⟨-h, 1⟩

@[simp] lemma sigma_const : (sigma : Hecke2 R h).const = 0 := rfl
@[simp] lemma sigma_gen : (sigma : Hecke2 R h).gen = 1 := rfl
@[simp] lemma sigmaInv_const : (sigmaInv : Hecke2 R h).const = -h := rfl
@[simp] lemma sigmaInv_gen : (sigmaInv : Hecke2 R h).gen = 1 := rfl

/-- **The Hecke quadratic relation** `σ² = h·σ + 1`. -/
theorem sigma_sq : (sigma : Hecke2 R h) * sigma = h • sigma + 1 := by
  ext <;> simp

/-- `σ⁻¹` is a genuine two-sided inverse of `σ` (using the quadratic relation). -/
theorem sigma_mul_sigmaInv : (sigma : Hecke2 R h) * sigmaInv = 1 := by
  ext <;> simp

theorem sigmaInv_mul_sigma : (sigmaInv : Hecke2 R h) * sigma = 1 := by
  ext <;> simp

/-- `σ` is a unit; its inverse is `σ - h·1`. -/
def sigmaUnit : (Hecke2 R h)ˣ where
  val := sigma
  inv := sigmaInv
  val_inv := sigma_mul_sigmaInv
  inv_val := sigmaInv_mul_sigma

/-! ### The Ocneanu/Markov trace -/

/-- The **Ocneanu/Markov trace** on `H₂`, with Markov parameter `z`:
`tr(a·1 + b·σ) = a + z·b`.  It is an `R`-linear functional. -/
def ocneanuTrace (z : R) : Hecke2 R h →ₗ[R] R where
  toFun x := x.const + z * x.gen
  map_add' _ _ := by simp only [add_const, add_gen]; ring
  map_smul' _ _ := by
    simp only [smul_const, smul_gen, RingHom.id_apply, smul_eq_mul]; ring

@[simp] lemma ocneanuTrace_apply (z : R) (x : Hecke2 R h) :
    ocneanuTrace z x = x.const + z * x.gen := rfl

/-- **(T2) Normalisation:** the trace of `1` is `1`. -/
theorem ocneanuTrace_one (z : R) : ocneanuTrace z (1 : Hecke2 R h) = 1 := by
  simp

/-- The trace of the generator is the Markov parameter `z`. -/
theorem ocneanuTrace_sigma (z : R) : ocneanuTrace z (sigma : Hecke2 R h) = z := by
  simp

/-- The trace of the inverse generator is `z - h`; this is the second Markov
parameter `zinv` (matching `OcneanuTrace.markovParam_inv_eq_sub`). -/
theorem ocneanuTrace_sigmaInv (z : R) :
    ocneanuTrace z (sigmaInv : Hecke2 R h) = z - h := by
  simp only [ocneanuTrace_apply, sigmaInv_const, sigmaInv_gen]; ring

/-- **(T1) The trace property** `tr(xy) = tr(yx)` — automatic here because `H₂`
is commutative. -/
theorem ocneanuTrace_mul_comm (z : R) (x y : Hecke2 R h) :
    ocneanuTrace z (x * y) = ocneanuTrace z (y * x) := by
  rw [mul_comm]

/-- **(T3) Markov stabilisation.** For any scalar element `c·1` of the bottom of
the tower `H₁ = R·1`, `tr((c·1) · σ) = z · tr(c·1)`. -/
theorem ocneanuTrace_markov (z c : R) :
    ocneanuTrace z ((c • (1 : Hecke2 R h)) * sigma) = z * ocneanuTrace z (c • (1 : Hecke2 R h)) := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen, smul_const, smul_gen,
    one_const, one_gen, sigma_const, sigma_gen]; ring

/-- **(T3') Markov stabilisation by the inverse generator**, with parameter
`zinv = z - h`. -/
theorem ocneanuTrace_markov_inv (z c : R) :
    ocneanuTrace z ((c • (1 : Hecke2 R h)) * sigmaInv)
      = (z - h) * ocneanuTrace z (c • (1 : Hecke2 R h)) := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen, smul_const, smul_gen,
    one_const, one_gen, sigmaInv_const, sigmaInv_gen]; ring

/-! ### Non-degeneracy — why this is a genuine `q ≠ 1` Hecke functional -/

/-- The two Markov parameters differ **iff** the bandwidth is nonzero, i.e. iff
`q ≠ 1`.  (The symmetric-group witness has `h = 0`, so there `z = zinv`.) -/
theorem markovParam_ne_iff (z : R) : z ≠ z - h ↔ h ≠ 0 := by
  rw [ne_eq, ne_eq, not_iff_not]
  constructor
  · intro he
    have h0 : z - (z - h) = z - z := by rw [← he]
    simpa using h0
  · intro hh; rw [hh, sub_zero]

/-- **The multiplicativity defect equals the Hecke quadratic.**  The trace is
multiplicative on `σ` (`tr(σ²) = tr(σ)²`) exactly when `z` is a root of the
Hecke quadratic `X² - h·X - 1`.  Generically it is not, so the trace is a
genuinely non-multiplicative functional — the whole point of a Markov trace. -/
theorem ocneanuTrace_mul_defect (z : R) :
    ocneanuTrace z ((sigma : Hecke2 R h) * sigma)
      - ocneanuTrace z (sigma : Hecke2 R h) * ocneanuTrace z (sigma : Hecke2 R h)
      = h * z + 1 - z * z := by
  rw [sigma_sq]
  simp only [ocneanuTrace_apply, add_const, add_gen, smul_const, smul_gen,
    sigma_const, sigma_gen, one_const, one_gen]; ring

/-- A concrete non-degenerate instance over `ℚ`: at `h = 1`, `z = 0` the
multiplicativity defect is `1 ≠ 0`, so the Ocneanu trace on `H₂(ℚ)` is a
genuinely **non-multiplicative** functional (witnessing non-vacuity of
`ocneanuTrace_mul_defect`). -/
theorem exists_nonmultiplicative :
    ∃ (h z : ℚ), ocneanuTrace (h := h) z (sigma * sigma)
      - ocneanuTrace (h := h) z sigma * ocneanuTrace (h := h) z sigma ≠ 0 := by
  refine ⟨1, 0, ?_⟩
  rw [ocneanuTrace_mul_defect]; norm_num

end Hecke2

end QOU.MathlibExt.HeckeRankTwoMarkov
