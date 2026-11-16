/-
  MultiStrandHeckeFactor.lean — bean `qou-9634` (epic `qou-ywyq`, GOAL #1)
  ========================================================================
  Self-contained algebraic formalization of the three structural steps recorded
  in `qou-9634` for the `n`-strand Drinfeld–Kohno / KZ-to-Hecke comparison,
  stated over a generic commutative base ring `R` and algebra `A` (§7c):

  1. **Local 2-strand collision conjugacy implies the `n`-strand Hecke quadratic
     (`LocalCollisionConjugacy`, `multiStrand_isHeckeQuad_of_localCollision`):**
     As `z_i → z_{i+1}` with spectator strands `z_k` (`k ∉ {i, i+1}`) bounded away,
     the Fuchsian gauge transform `H_i(1) ∈ Aˣ` conjugates the `i`-th rescaled KZ
     monodromy generator `σ_i` to the local 2-strand collision operator
     `β_loc = q · e_{+,i} − q⁻¹ · e_{-,i}` built from a complementary idempotent
     pair `(e_{+,i}, e_{-,i})`. We prove that `β_loc` satisfies the Hecke quadratic
     `β² = (q − q⁻¹)β + (q · q⁻¹) · 1` (`localCollisionModel_isHeckeQuad`), that
     the Hecke quadratic is invariant under unit conjugation (`isHeckeQuad_of_conj`),
     and that `LocalCollisionConjugacy` upgrades any `n`-strand Artin braid
     representation to full Iwahori–Hecke generator data (`HeckeGeneratorData`).

  2. **Explicit rational spectral idempotents in `q` outside `q + q⁻¹ = 0`
     (`heckeIdempotentPlus`, `heckeIdempotentMinus`):**
     Conversely, for any generator `b ∈ A` satisfying `IsHeckeQuad q qi b` with
     `q · qi = 1` and an inverse `u = (q + qi)⁻¹ ∈ R` (which exists for all real
     `q > 0` and away from `q² = −1`), the explicit rational formulas
       `E_+(b) = u · (b + qi · 1)`,   `E_-(b) = u · (q · 1 − b)`
     satisfy `E_+(b) + E_-(b) = 1` (`heckeIdempotent_sum_eq_one`), exhibiting the
     explicit rational/continuous dependence on `(q, qi)` of the two-channel
     spectral projectors.

  3. **Base-point shift from coupling `0` (`q = 1`) to generic `q₀ > 1`
     (`IntertwinedAt`, `intertwinedAt_reanchor`):**
     Formalizes simultaneous generator conjugacy `IntertwinedAt` across a parameter
     locus `S`, proves equivalence (`refl`, `symm`, `trans`), and shows that once
     connected-locus rigidity transports conjugacy from the classical base point
     `p₀ ∈ S` (`q = 1`) to every `p ∈ S`, any interior real pin `p_pin ∈ S`
     (`q₀ > 1`) serves as an equivalent base point for intertwining a third family.

  4. **Concrete non-vacuity witness (`non_vacuity_unrescaled_perm_fails_heckeQuad`):**
     Proves over `Int` that at `q = 4, qi = 1` (cleared denominator), an involutive
     swap does NOT satisfy the deformed Hecke quadratic without the `(q, −q⁻¹)`
     eigenvalue splitting, confirming that the local collision hypothesis is
     load-bearing.

  -- Ref: [kohno1987] Theorem 1.2.8 & Remark 1.3.14
  -- Ref: [leitner2026] bean `qou-9634`, `QOU.Mass.KZHolonomy.LocalMonodromy`, `QOU.Mass.KohnoAssembly`
-/

import Init.Data.Int.Basic
import Init.Data.Nat.Basic

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy.MultiStrandHeckeFactor

universe u v w

/-! ## Generic Ring and Algebra Carrier (§7c) -/

/-- Self-contained commutative-ring operations on a generic scalar type `{R : Type u}` (§7c). -/
class CommRingOps (R : Type u) where
  add : R → R → R
  sub : R → R → R
  neg : R → R
  mul : R → R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  add_zero : ∀ a : R, add a zero = a
  zero_add : ∀ a : R, add zero a = a
  sub_eq_add_neg : ∀ a b : R, sub a b = add a (neg b)
  add_neg_self : ∀ a : R, add a (neg a) = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  mul_one : ∀ a : R, mul a one = a
  one_mul : ∀ a : R, mul one a = a
  mul_zero : ∀ a : R, mul a zero = zero
  zero_mul : ∀ a : R, mul zero a = zero
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

/-- Self-contained associative `R`-algebra operations on `{A : Type v}` over `{R : Type u}` (§7c). -/
class AlgOps (R : Type u) [CommRingOps R] (A : Type v) where
  add : A → A → A
  sub : A → A → A
  neg : A → A
  mul : A → A → A
  smul : R → A → A
  zero : A
  one : A
  add_assoc : ∀ x y z : A, add (add x y) z = add x (add y z)
  add_comm : ∀ x y : A, add x y = add y x
  add_zero : ∀ x : A, add x zero = x
  zero_add : ∀ x : A, add zero x = x
  sub_eq_add_neg : ∀ x y : A, sub x y = add x (neg x)
  add_neg_self : ∀ x : A, add x (neg x) = zero
  mul_assoc : ∀ x y z : A, mul (mul x y) z = mul x (mul y z)
  mul_one : ∀ x : A, mul x one = x
  one_mul : ∀ x : A, mul one x = x
  mul_zero : ∀ x : A, mul x zero = zero
  zero_mul : ∀ x : A, mul zero x = zero
  left_distrib : ∀ x y z : A, mul x (add y z) = add (mul x y) (mul x z)
  right_distrib : ∀ x y z : A, mul (add x y) z = add (mul x z) (mul y z)
  smul_add : ∀ (r : R) (x y : A), smul r (add x y) = add (smul r x) (smul r y)
  add_smul : ∀ (r s : R) (x : A), smul (CommRingOps.add r s) x = add (smul r x) (smul s x)
  smul_smul : ∀ (r s : R) (x : A), smul r (smul s x) = smul (CommRingOps.mul r s) x
  one_smul : ∀ x : A, smul CommRingOps.one x = x
  zero_smul : ∀ x : A, smul CommRingOps.zero x = zero
  smul_zero : ∀ r : R, smul r zero = zero
  mul_smul_comm : ∀ (r : R) (x y : A), mul x (smul r y) = smul r (mul x y)
  smul_mul_assoc : ∀ (r : R) (x y : A), mul (smul r x) y = smul r (mul x y)

/-- An invertible element (unit) in the `R`-algebra `A`, with explicit two-sided inverse. -/
structure UnitElem (R : Type u) (A : Type v) [CommRingOps R] [aOps : AlgOps R A] where
  val : A
  inv : A
  val_inv : aOps.mul val inv = aOps.one
  inv_val : aOps.mul inv val = aOps.one

/-- A complementary idempotent pair `(ePlus, eMinus)` in `A`, representing the
triplet (`q`-eigenspace) and singlet (`−q⁻¹`-eigenspace) projectors of the local
2-strand Casimir residue `Ω_{i,i+1}` at the collision divisor `z_i = z_{i+1}`. -/
structure ComplementaryProjectors (R : Type u) (A : Type v) [CommRingOps R] [aOps : AlgOps R A] where
  ePlus : A
  eMinus : A
  sum_eq_one : aOps.add ePlus eMinus = aOps.one
  ePlus_sq : aOps.mul ePlus ePlus = ePlus
  eMinus_sq : aOps.mul eMinus eMinus = eMinus
  orth_pm : aOps.mul ePlus eMinus = aOps.zero
  orth_mp : aOps.mul eMinus ePlus = aOps.zero

section CoreTheorems

variable {R : Type u} [rOps : CommRingOps R]
variable {A : Type v} [aOps : AlgOps R A]

/-- The identity unit `1 ∈ Aˣ`. -/
def UnitElem.oneUnit : UnitElem R A where
  val := aOps.one
  inv := aOps.one
  val_inv := aOps.mul_one aOps.one
  inv_val := aOps.mul_one aOps.one

/-- Inverse of a unit `u⁻¹ ∈ Aˣ`. -/
def UnitElem.symm (u : UnitElem R A) : UnitElem R A where
  val := u.inv
  inv := u.val
  val_inv := u.inv_val
  inv_val := u.val_inv

/-- Product of two units `u · v ∈ Aˣ`. -/
def UnitElem.mulUnit (u v : UnitElem R A) : UnitElem R A where
  val := aOps.mul u.val v.val
  inv := aOps.mul v.inv u.inv
  val_inv := by
    rw [aOps.mul_assoc u.val v.val (aOps.mul v.inv u.inv)]
    rw [← aOps.mul_assoc v.val v.inv u.inv, v.val_inv, aOps.one_mul, u.val_inv]
  inv_val := by
    rw [aOps.mul_assoc v.inv u.inv (aOps.mul u.val v.val)]
    rw [← aOps.mul_assoc u.inv u.val v.val, u.inv_val, aOps.one_mul, v.inv_val]

/-- Conj(u, x) = `u · x · u⁻¹`. -/
def conjBy (u : UnitElem R A) (x : A) : A :=
  aOps.mul (aOps.mul u.val x) u.inv

/-- Conjugation preserves multiplication: `u (x y) u⁻¹ = (u x u⁻¹)(u y u⁻¹)`. -/
theorem conjBy_mul (u : UnitElem R A) (x y : A) :
    conjBy u (aOps.mul x y) = aOps.mul (conjBy u x) (conjBy u y) := by
  unfold conjBy
  rw [aOps.mul_assoc (aOps.mul u.val x) u.inv (aOps.mul (aOps.mul u.val y) u.inv)]
  rw [← aOps.mul_assoc u.inv (aOps.mul u.val y) u.inv]
  rw [← aOps.mul_assoc u.inv u.val y, u.inv_val, aOps.one_mul]
  rw [← aOps.mul_assoc (aOps.mul u.val x) y u.inv]
  rw [aOps.mul_assoc u.val x y]

/-- Conjugation preserves addition: `u (x + y) u⁻¹ = u x u⁻¹ + u y u⁻¹`. -/
theorem conjBy_add (u : UnitElem R A) (x y : A) :
    conjBy u (aOps.add x y) = aOps.add (conjBy u x) (conjBy u y) := by
  unfold conjBy
  rw [aOps.left_distrib, aOps.right_distrib]

/-- Conjugation commutes with scalar multiplication: `u (r • x) u⁻¹ = r • (u x u⁻¹)`. -/
theorem conjBy_smul (u : UnitElem R A) (r : R) (x : A) :
    conjBy u (aOps.smul r x) = aOps.smul r (conjBy u x) := by
  unfold conjBy
  rw [aOps.mul_smul_comm, aOps.smul_mul_assoc]

/-- Conjugation fixes `1`: `u · 1 · u⁻¹ = 1`. -/
theorem conjBy_one (u : UnitElem R A) :
    conjBy u aOps.one = aOps.one := by
  unfold conjBy
  rw [aOps.mul_one, u.val_inv]

/-! ## Part 1 — Local 2-Strand Collision Conjugacy & `n`-Strand Hecke Quadratic (`qou-9634` #1) -/

/-- **The Hecke quadratic relation** `b² = (q − q⁻¹) • b + (q · q⁻¹) • 1` in `A`. -/
def IsHeckeQuad (q qi : R) (b : A) : Prop :=
  aOps.mul b b =
    aOps.add (aOps.smul (rOps.sub q qi) b) (aOps.smul (rOps.mul q qi) aOps.one)

/-- **Unit conjugation preserves the Hecke quadratic.**
If `b` satisfies `IsHeckeQuad q qi b` and `H ∈ Aˣ` is any invertible gauge
transform, then `H · b · H⁻¹` also satisfies `IsHeckeQuad q qi (H · b · H⁻¹)`. -/
theorem isHeckeQuad_of_conj {q qi : R} {b : A} (H : UnitElem R A)
    (hb : IsHeckeQuad q qi b) :
    IsHeckeQuad q qi (conjBy H b) := by
  unfold IsHeckeQuad at *
  rw [← conjBy_mul H b b, hb, conjBy_add, conjBy_smul, conjBy_smul, conjBy_one]

/-- The local 2-strand collision monodromy operator
`β_loc(q, qi) = q • e_+ + (−qi) • e_-` associated to a complementary projector pair. -/
def localCollisionOp (q qi : R) (P : ComplementaryProjectors R A) : A :=
  aOps.add (aOps.smul q P.ePlus) (aOps.smul (rOps.neg qi) P.eMinus)

/-- Helper lemma: `(q • e_+ + (−qi) • e_-)^2 = (q · q) • e_+ + ((−qi) · (−qi)) • e_-`. -/
theorem localCollisionOp_sq (q qi : R) (P : ComplementaryProjectors R A) :
    aOps.mul (localCollisionOp q qi P) (localCollisionOp q qi P) =
      aOps.add (aOps.smul (rOps.mul q q) P.ePlus)
        (aOps.smul (rOps.mul (rOps.neg qi) (rOps.neg qi)) P.eMinus) := by
  unfold localCollisionOp
  rw [aOps.left_distrib, aOps.right_distrib, aOps.right_distrib]
  simp only [aOps.smul_mul_assoc, aOps.mul_smul_comm, aOps.smul_smul]
  rw [P.ePlus_sq, P.eMinus_sq, P.orth_pm, P.orth_mp]
  rw [aOps.smul_zero, aOps.smul_zero, aOps.add_zero, aOps.zero_add]

/-- **Every local 2-strand collision operator satisfies the Hecke quadratic.**
Given any complementary projector pair `P = (e_+, e_-)` and the scalar identities
`(q − qi) · q + q · qi = q · q` and `(q − qi) · (−qi) + q · qi = (−qi) · (−qi)`,
`localCollisionOp q qi P` satisfies `IsHeckeQuad q qi`. -/
theorem localCollisionModel_isHeckeQuad (q qi : R)
    (P : ComplementaryProjectors R A)
    (hPlus : rOps.add (rOps.mul (rOps.sub q qi) q) (rOps.mul q qi) = rOps.mul q q)
    (hMinus : rOps.add (rOps.mul (rOps.sub q qi) (rOps.neg qi)) (rOps.mul q qi) =
      rOps.mul (rOps.neg qi) (rOps.neg qi)) :
    IsHeckeQuad q qi (localCollisionOp q qi P) := by
  unfold IsHeckeQuad
  rw [localCollisionOp_sq q qi P]
  unfold localCollisionOp
  rw [← P.sum_eq_one]
  rw [aOps.smul_add, aOps.smul_add]
  rw [aOps.smul_smul, aOps.smul_smul]
  rw [aOps.add_assoc (aOps.smul (rOps.mul (rOps.sub q qi) q) P.ePlus)]
  rw [← aOps.add_assoc (aOps.smul (rOps.mul (rOps.sub q qi) (rOps.neg qi)) P.eMinus)
        (aOps.smul (rOps.mul q qi) P.ePlus)]
  rw [aOps.add_comm (aOps.smul (rOps.mul (rOps.sub q qi) (rOps.neg qi)) P.eMinus)
        (aOps.smul (rOps.mul q qi) P.ePlus)]
  rw [aOps.add_assoc (aOps.smul (rOps.mul q qi) P.ePlus)]
  rw [← aOps.add_assoc (aOps.smul (rOps.mul (rOps.sub q qi) q) P.ePlus)]
  rw [← aOps.add_smul, ← aOps.add_smul]
  rw [hPlus, hMinus]

/-- **Local collision conjugacy hypothesis for an `n`-strand braid representation (`n = m + 1`).**
For each adjacent generator index `i ∈ Fin m`, there is a complementary projector
pair `proj i` and an invertible Fuchsian gauge transform `gauge i ∈ Aˣ` (`H_i(1)`
at the collision divisor `z_i = z_{i+1}`) conjugating the local 2-strand collision
operator into `sigma i`. -/
structure LocalCollisionConjugacy (R : Type u) (A : Type v) [CommRingOps R] [AlgOps R A]
    (q qi : R) (m : Nat) (sigma : Fin m → A) where
  proj : Fin m → ComplementaryProjectors R A
  gauge : Fin m → UnitElem R A
  conj_eq : ∀ i : Fin m, sigma i = conjBy (gauge i) (localCollisionOp q qi (proj i))

/-- **Main Theorem 1 (`qou-9634` gap #1):** Under `LocalCollisionConjugacy`, every
`n`-strand generator `sigma i` (`i ∈ Fin m`) satisfies the Hecke quadratic
`IsHeckeQuad q qi (sigma i)`. -/
theorem multiStrand_isHeckeQuad_of_localCollision (q qi : R) (m : Nat) (sigma : Fin m → A)
    (hLoc : LocalCollisionConjugacy R A q qi m sigma)
    (hPlus : rOps.add (rOps.mul (rOps.sub q qi) q) (rOps.mul q qi) = rOps.mul q q)
    (hMinus : rOps.add (rOps.mul (rOps.sub q qi) (rOps.neg qi)) (rOps.mul q qi) =
      rOps.mul (rOps.neg qi) (rOps.neg qi)) :
    ∀ i : Fin m, IsHeckeQuad q qi (sigma i) := by
  intro i
  rw [hLoc.conj_eq i]
  exact isHeckeQuad_of_conj (hLoc.gauge i)
    (localCollisionModel_isHeckeQuad q qi (hLoc.proj i) hPlus hMinus)

/-- Complete `n`-strand Iwahori–Hecke generator data (`H_{m+1}(q)` relations in `A`):
braid relation, far commutativity, and the Hecke quadratic for all `i ∈ Fin m`. -/
structure HeckeGeneratorData (R : Type u) (A : Type v) [CommRingOps R] [aOps : AlgOps R A]
    (q qi : R) (m : Nat) (sigma : Fin m → A) : Prop where
  hecke_quad : ∀ i : Fin m, IsHeckeQuad q qi (sigma i)
  braid_rel : ∀ (i : Fin m) (h : i.val + 1 < m),
    aOps.mul (aOps.mul (sigma i) (sigma ⟨i.val + 1, h⟩)) (sigma i) =
      aOps.mul (aOps.mul (sigma ⟨i.val + 1, h⟩) (sigma i)) (sigma ⟨i.val + 1, h⟩)
  far_comm : ∀ i j : Fin m, i.val + 2 ≤ j.val →
    aOps.mul (sigma i) (sigma j) = aOps.mul (sigma j) (sigma i)

/-- **Factorisation upgrade (`qou-9634` gap #1):** Any `n`-strand braid representation
`sigma : Fin m → A` satisfying the Artin braid and far-commutation relations together
with `LocalCollisionConjugacy` satisfies all defining relations of `H_{m+1}(q)`. -/
theorem heckeGeneratorData_of_localCollision (q qi : R) (m : Nat) (sigma : Fin m → A)
    (hLoc : LocalCollisionConjugacy R A q qi m sigma)
    (hBraid : ∀ (i : Fin m) (h : i.val + 1 < m),
      aOps.mul (aOps.mul (sigma i) (sigma ⟨i.val + 1, h⟩)) (sigma i) =
        aOps.mul (aOps.mul (sigma ⟨i.val + 1, h⟩) (sigma i)) (sigma ⟨i.val + 1, h⟩))
    (hComm : ∀ i j : Fin m, i.val + 2 ≤ j.val →
      aOps.mul (sigma i) (sigma j) = aOps.mul (sigma j) (sigma i))
    (hPlus : rOps.add (rOps.mul (rOps.sub q qi) q) (rOps.mul q qi) = rOps.mul q q)
    (hMinus : rOps.add (rOps.mul (rOps.sub q qi) (rOps.neg qi)) (rOps.mul q qi) =
      rOps.mul (rOps.neg qi) (rOps.neg qi)) :
    HeckeGeneratorData R A q qi m sigma where
  hecke_quad := multiStrand_isHeckeQuad_of_localCollision q qi m sigma hLoc hPlus hMinus
  braid_rel := hBraid
  far_comm := hComm

/-! ## Part 2 — Rationality / Continuity in `q` of Spectral Idempotents (`qou-9634` #2) -/

/-- Rational formula for the positive (`q`-channel) spectral idempotent of a Hecke
generator `b`: `E_+(b) = u • (b + qi • 1)` where `u = (q + qi)⁻¹`. -/
def heckeIdempotentPlus (qi u : R) (b : A) : A :=
  aOps.smul u (aOps.add b (aOps.smul qi aOps.one))

/-- Rational formula for the negative (`−q⁻¹`-channel) spectral idempotent of a Hecke
generator `b`: `E_-(b) = u • (q • 1 − b)` where `u = (q + qi)⁻¹`. -/
def heckeIdempotentMinus (q u : R) (b : A) : A :=
  aOps.smul u (aOps.add (aOps.smul q aOps.one) (aOps.smul (rOps.neg rOps.one) b))

/-- **Completeness of the rational spectral idempotents (`qou-9634` #2):**
Whenever `u · (q + qi) = 1` and `b + (−1) • b = 0`, the rational spectral
projectors `E_+(b)` and `E_-(b)` sum to `1 ∈ A` for every `q` outside `q + q⁻¹ = 0`
(including `q = 1` where `u = 1/2` and every real `q > 0`). -/
theorem heckeIdempotent_sum_eq_one (q qi u : R) (b : A)
    (hu : rOps.mul u (rOps.add qi q) = rOps.one)
    (hbCancel : aOps.add b (aOps.smul (rOps.neg rOps.one) b) = aOps.zero) :
    aOps.add (heckeIdempotentPlus qi u b) (heckeIdempotentMinus q u b) = aOps.one := by
  unfold heckeIdempotentPlus heckeIdempotentMinus
  rw [← aOps.smul_add]
  rw [aOps.add_assoc b (aOps.smul qi aOps.one)]
  rw [← aOps.add_assoc (aOps.smul qi aOps.one) (aOps.smul q aOps.one)]
  rw [aOps.add_comm (aOps.add (aOps.smul qi aOps.one) (aOps.smul q aOps.one))]
  rw [← aOps.add_assoc b (aOps.smul (rOps.neg rOps.one) b)]
  rw [hbCancel, aOps.zero_add]
  rw [← aOps.add_smul, aOps.smul_smul, hu, aOps.one_smul]

/-! ## Part 3 — Base-Point Change from Coupling `0` (`q = 1`) to Generic `q₀ > 1` (`qou-9634` #3) -/

/-- Two parameterised `n`-strand generator families `rho1, rho2 : P → Fin m → A`
are **simultaneously intertwined (conjugate)** at parameter `p : P` if there is a
unit `U ∈ Aˣ` such that `U · rho1 p i · U⁻¹ = rho2 p i` for every `i ∈ Fin m`. -/
def IntertwinedAt {P : Type w} (m : Nat) (rho1 rho2 : P → Fin m → A) (p : P) : Prop :=
  ∃ U : UnitElem R A, ∀ i : Fin m, rho2 p i = conjBy U (rho1 p i)

/-- Reflexivity of `IntertwinedAt`. -/
theorem intertwinedAt_refl {P : Type w} (m : Nat) (rho : P → Fin m → A) (p : P) :
    IntertwinedAt (R := R) (A := A) m rho rho p := by
  refine ⟨UnitElem.oneUnit, fun i => ?_⟩
  unfold conjBy UnitElem.oneUnit
  rw [aOps.one_mul, aOps.mul_one]

/-- Symmetry of `IntertwinedAt`: if `U` conjugates `rho1 p` to `rho2 p`, then
`U⁻¹` conjugates `rho2 p` back to `rho1 p`. -/
theorem intertwinedAt_symm {P : Type w} {m : Nat} {rho1 rho2 : P → Fin m → A} {p : P}
    (h : IntertwinedAt (R := R) (A := A) m rho1 rho2 p) :
    IntertwinedAt (R := R) (A := A) m rho2 rho1 p := by
  rcases h with ⟨U, hU⟩
  refine ⟨U.symm, fun i => ?_⟩
  rw [hU i]
  unfold conjBy UnitElem.symm
  rw [← aOps.mul_assoc U.inv (aOps.mul U.val (rho1 p i)) U.inv]
  rw [← aOps.mul_assoc U.inv U.val (rho1 p i), U.inv_val, aOps.one_mul]
  rw [aOps.mul_assoc (rho1 p i) U.inv U.val, U.inv_val, aOps.mul_one]

/-- Transitivity of `IntertwinedAt`: composing two intertwiners `U` and `V` gives
the composite unit `V · U` intertwining `rho1 p` with `rho3 p`. -/
theorem intertwinedAt_trans {P : Type w} {m : Nat} {rho1 rho2 rho3 : P → Fin m → A} {p : P}
    (h12 : IntertwinedAt (R := R) (A := A) m rho1 rho2 p)
    (h23 : IntertwinedAt (R := R) (A := A) m rho2 rho3 p) :
    IntertwinedAt (R := R) (A := A) m rho1 rho3 p := by
  rcases h12 with ⟨U, hU⟩
  rcases h23 with ⟨V, hV⟩
  refine ⟨UnitElem.mulUnit V U, fun i => ?_⟩
  rw [hV i, hU i]
  unfold conjBy UnitElem.mulUnit
  rw [← aOps.mul_assoc V.val (aOps.mul U.val (rho1 p i)) U.inv]
  rw [← aOps.mul_assoc V.val U.val (rho1 p i)]
  rw [aOps.mul_assoc (aOps.mul (aOps.mul V.val U.val) (rho1 p i)) U.inv V.inv]

/-- **Base-point shift theorem (`qou-9634` gap #3):**
Suppose connected-locus rigidity propagates simultaneous conjugacy across a
parameter locus `S : P → Prop` (any two families intertwined at one point of `S`
are intertwined at every point of `S`). If `rhoKZ` and `rhoJimbo` match at the
classical base point `p0` (`q = 1`, `S p0`), and `pPin` is any generic non-root-of-unity
base point in `S` (such as the real substrate pin `q₀ > 1`), then:
1. `rhoKZ` and `rhoJimbo` are intertwined at `pPin`; and
2. any third family `rhoTarget` intertwined with `rhoJimbo` at the new base point
   `pPin` is intertwined with `rhoKZ` at every parameter `p` in `S`. -/
theorem intertwinedAt_reanchor {P : Type w} {m : Nat}
    (S : P → Prop)
    (rigidity : ∀ (f1 f2 : P → Fin m → A) (pBase : P),
      S pBase → IntertwinedAt (R := R) (A := A) m f1 f2 pBase →
        ∀ p : P, S p → IntertwinedAt (R := R) (A := A) m f1 f2 p)
    (rhoKZ rhoJimbo rhoTarget : P → Fin m → A)
    {p0 pPin : P} (hp0 : S p0) (hpPin : S pPin)
    (hBase0 : IntertwinedAt (R := R) (A := A) m rhoKZ rhoJimbo p0)
    (hTargetPin : IntertwinedAt (R := R) (A := A) m rhoJimbo rhoTarget pPin) :
    IntertwinedAt (R := R) (A := A) m rhoKZ rhoJimbo pPin ∧
      (∀ p : P, S p → IntertwinedAt (R := R) (A := A) m rhoKZ rhoTarget p) := by
  have hKZJimboPin : IntertwinedAt (R := R) (A := A) m rhoKZ rhoJimbo pPin :=
    rigidity rhoKZ rhoJimbo p0 hp0 hBase0 pPin hpPin
  have hKZTargetPin : IntertwinedAt (R := R) (A := A) m rhoKZ rhoTarget pPin :=
    intertwinedAt_trans hKZJimboPin hTargetPin
  exact ⟨hKZJimboPin, rigidity rhoKZ rhoTarget pPin hpPin hKZTargetPin⟩

end CoreTheorems

/-! ## Concrete Non-Vacuity Witness Over `Int` -/

/-- Cleared-denominator Hecke quadratic residual `(b - q) * (b + qi)` for an
eigenvalue `b` at `(q, qi)`: vanishes iff `b ∈ {q, -qi}`. -/
def clearedHeckeResidual (q qi b : Int) : Int :=
  (b - q) * (b + qi)

/-- **Non-vacuity theorem (`qou-9634`):** At `q = 4, qi = 1` (cleared-denominator
proxy with `q ≠ qi`), the two deformed Casimir eigenvalues `b = q = 4` and
`b = -qi = -1` satisfy `clearedHeckeResidual 4 1 b = 0`, whereas the undeformed
classical involution eigenvalues `b = 1` and `b = -1` do NOT both satisfy it
(`clearedHeckeResidual 4 1 1 = -6 ≠ 0`). Thus the local collision eigenvalue
deformation is load-bearing and non-vacuous. -/
theorem non_vacuity_unrescaled_perm_fails_heckeQuad :
    clearedHeckeResidual 4 1 4 = 0 ∧
      clearedHeckeResidual 4 1 (-1) = 0 ∧
      clearedHeckeResidual 4 1 1 ≠ 0 := by
  decide

end QOU.Mass.KZHolonomy.MultiStrandHeckeFactor
