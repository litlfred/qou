/-
# Jones basic-construction interface for the Hecke tower — proved idempotent layer + honest OPEN classes

A1 tower-induction scaffold (beans `qou-2c4t` / `qou-iri6`, milestone
`qou-lv5t`): the inductive route to general-`n` Hecke semisimplicity is
Wenzl's tower argument through the Jones basic construction — conditional
expectation `ε : H_{n+1} → H_n`, Jones projection `e_n`, and the
semisimplicity ascent along a nondegenerate Markov trace. This file
supplies that route's interface in the repo's TIERED, honest form
(STRICT, §"Axiomatization is NOT a Proof"):

**PROVED layer (sorry-free, unconditional).** The Jones projection is
*derivable* from the quadratic alone, in ANY `R`-algebra: for `s` with
`s² = (q − q⁻¹)•s + 1` and `q + q⁻¹ ≠ 0`,

  `e := (q + q⁻¹)⁻¹ • (q•1 − s)`

is idempotent (`jonesIdempotent_mul_self`), spans the `−q⁻¹` eigen-channel
(`mul_jonesIdempotent` / `jonesIdempotent_mul`), and recovers the
generator (`generator_eq_jones`). So the *local* projection layer of the
basic construction is not conjectural — it is theorem-level at every rank
simultaneously, feeding on `HeckeGeneralRankQuadratic.mulSimple_quadratic`
and the concrete rung quadratics. A concrete 2×2 slice
(`jonesIdempotent_h2`) pins `e = diag(0,1)` for the diagonal generator of
`HeckeBraidedCategoryScaffold.heckeQuadratic_h2`.

**OPEN layer (§3b conjecture classes, NO instances).** What the local
algebra cannot supply is the *tower* data: the conditional expectation
(`HeckeConditionalExpectation`), the basic-construction absorption
`e·y·e = ι(ε y)·e` (`JonesBasicConstruction`), and the Wenzl ascent
"level-`n` semisimple + trace nondegenerate ⇒ level-`n+1` semisimple"
(`WenzlTowerStep`). Each is a content-bearing DEPENDENT conjecture class
binding `HeckeBraidedPresentation` in its type (the §3b-tax dependency
edge); none carries an instance. Concrete evidence at the proved rungs:
`H3.trM_markov_σ₁` (Markov reduction), `wedderburn₃` +
`isSemisimpleRing_H3A` (the n = 3 ascent target realized explicitly).

HONESTY (STRICT): nothing here proves the tower step. The classes state
the open induction hypotheses; the proved layer is only the local
idempotent algebra. No instance is declared for any OPEN class; nothing
is wired; general-`n` semisimplicity remains open.

Base ring (§7c): generic `[Field R]` (needs `q⁻¹`, `(q+q⁻¹)⁻¹`), never
`ℝ`; no ordering, no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001
-/
import QOU.Machinery.HeckeBraidedCategoryScaffold
import Mathlib.RingTheory.SimpleModule.Basic

namespace QOU.Machinery.HeckeTower

open QOU.Machinery.HeckeBraidedCategory

/-! ## Proved layer — the Jones projection from the quadratic alone -/

variable {R : Type*} [Field R] {H : Type*} [Ring H] [Algebra R H]

/-- The **Jones projection** attached to a Hecke generator: the
normalized `−q⁻¹`-eigenchannel projector `e = (q+q⁻¹)⁻¹ • (q•1 − s)`.
Defined for any element of any `R`-algebra; its projection identities
below need only the Hecke quadratic. -/
noncomputable def jonesIdempotent (q : R) (s : H) : H :=
  (q + q⁻¹)⁻¹ • (q • (1 : H) - s)

/-- The defining sum: `(q+q⁻¹) • e = q•1 − s`, i.e. the generator is
recovered as `s = q•1 − (q+q⁻¹)•e` (`generator_eq_jones`). -/
theorem smul_jonesIdempotent (q : R) (s : H) (hd : q + q⁻¹ ≠ 0) :
    (q + q⁻¹) • jonesIdempotent q s = q • (1 : H) - s := by
  rw [jonesIdempotent, smul_smul, mul_inv_cancel₀ hd, one_smul]

/-- **Generator recovery**: `s = q•1 − (q+q⁻¹)•e`. Together with
`jonesIdempotent_mul_self` this exhibits the Hecke algebra's generator
layer as the idempotent layer of the basic construction — the standard
Temperley–Lieb change of generators. -/
theorem generator_eq_jones (q : R) (s : H) (hd : q + q⁻¹ ≠ 0) :
    s = q • (1 : H) - (q + q⁻¹) • jonesIdempotent q s := by
  rw [smul_jonesIdempotent q s hd, sub_sub_cancel]

/-- **Left eigen-channel identity**: `s · (q•1 − s) = (−q⁻¹) • (q•1 − s)`
— the unnormalized Jones projection spans the antisymmetric channel. -/
theorem mul_sub_channel (q : R) (s : H) (hq : q ≠ 0)
    (hs : s * s = (q - q⁻¹) • s + 1) :
    s * (q • (1 : H) - s) = (-q⁻¹) • (q • (1 : H) - s) := by
  rw [mul_sub, mul_smul_comm, mul_one, hs, smul_sub, smul_smul, neg_mul,
    inv_mul_cancel₀ hq, sub_add_eq_sub_sub, ← sub_smul]
  have hsc : q - (q - q⁻¹) = q⁻¹ := by ring
  rw [hsc, neg_smul, neg_smul, one_smul, sub_neg_eq_add]
  abel

/-- Auxiliary product identity: `(q•1 − s)² = (q+q⁻¹) • (q•1 − s)` under
the Hecke quadratic — the unnormalized idempotency, from the channel
identity. -/
theorem sub_sq_eq (q : R) (s : H) (hq : q ≠ 0)
    (hs : s * s = (q - q⁻¹) • s + 1) :
    (q • (1 : H) - s) * (q • (1 : H) - s) = (q + q⁻¹) • (q • (1 : H) - s) := by
  calc (q • (1 : H) - s) * (q • (1 : H) - s)
      = q • (q • (1 : H) - s) - s * (q • (1 : H) - s) := by
        rw [sub_mul, smul_mul_assoc, one_mul]
    _ = q • (q • (1 : H) - s) - (-q⁻¹) • (q • (1 : H) - s) := by
        rw [mul_sub_channel q s hq hs]
    _ = (q + q⁻¹) • (q • (1 : H) - s) := by
        rw [← sub_smul]
        congr 1
        ring

/-- **The Jones projection is idempotent** — sorry-free, from the Hecke
quadratic alone, in any `R`-algebra: `e² = e`. This is the proved local
layer of the basic construction, valid at every rank simultaneously
(apply to `s = σᵢ` of any presentation). -/
theorem jonesIdempotent_mul_self (q : R) (s : H) (hq : q ≠ 0)
    (hd : q + q⁻¹ ≠ 0) (hs : s * s = (q - q⁻¹) • s + 1) :
    jonesIdempotent q s * jonesIdempotent q s = jonesIdempotent q s := by
  rw [jonesIdempotent, smul_mul_smul_comm, sub_sq_eq q s hq hs, smul_smul,
    mul_assoc, inv_mul_cancel₀ hd, mul_one]

/-- The generator acts on its Jones projection by the antisymmetric
eigenvalue: `s * e = (−q⁻¹) • e`. -/
theorem mul_jonesIdempotent (q : R) (s : H) (hq : q ≠ 0)
    (hs : s * s = (q - q⁻¹) • s + 1) :
    s * jonesIdempotent q s = (-q⁻¹) • jonesIdempotent q s := by
  rw [jonesIdempotent, mul_smul_comm, mul_sub_channel q s hq hs, smul_smul,
    smul_smul, mul_comm ((q + q⁻¹)⁻¹) (-q⁻¹)]

/-- Right-hand twin: `e * s = (−q⁻¹) • e`. -/
theorem jonesIdempotent_mul (q : R) (s : H) (hq : q ≠ 0)
    (hs : s * s = (q - q⁻¹) • s + 1) :
    jonesIdempotent q s * s = (-q⁻¹) • jonesIdempotent q s := by
  have key : (q • (1 : H) - s) * s = (-q⁻¹) • (q • (1 : H) - s) := by
    rw [sub_mul, smul_mul_assoc, one_mul, hs, smul_sub, smul_smul, neg_mul,
      inv_mul_cancel₀ hq, sub_add_eq_sub_sub, ← sub_smul]
    have hsc : q - (q - q⁻¹) = q⁻¹ := by ring
    rw [hsc, neg_smul, neg_smul, one_smul, sub_neg_eq_add]
    abel
  rw [jonesIdempotent, smul_mul_assoc, key, smul_smul, smul_smul,
    mul_comm ((q + q⁻¹)⁻¹) (-q⁻¹)]

/-- **Concrete 2×2 slice**: for the diagonal generator
`σ = diag(q, −q⁻¹)` of `heckeQuadratic_h2`, the Jones projection is
exactly the antisymmetric-channel projector `diag(0, 1)`. -/
theorem jonesIdempotent_h2 (q : R) (hd : q + q⁻¹ ≠ 0) :
    jonesIdempotent q (Matrix.of ![![q, 0], ![0, -q⁻¹]]) =
      Matrix.of ![![0, 0], ![0, (1 : R)]] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jonesIdempotent, Matrix.smul_apply, Matrix.sub_apply,
      Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [mul_comm, ← sub_neg_eq_add, sub_neg_eq_add, add_comm]
  exact mul_inv_cancel₀ (by rwa [add_comm] at hd)

/-! ## OPEN layer — the tower data as §3b dependent conjecture classes

None of the classes below carries an instance. Each binds
`HeckeBraidedPresentation` (and its predecessors in this file) in its
type — the §3b-tax dependency edge — and each field is a real quantified
equation (never `True`, never an empty body). -/

/-- **§3b DEPENDENT conjecture — conditional expectation onto the
subalgebra (bean `qou-iri6`).** GIVEN the two Hecke braided presentations
and the tower inclusion `ι : Hn →ₐ Hn1`, an `R`-linear conditional
expectation `ε : Hn1 →ₗ Hn`: a retraction of `ι` that is an
`(Hn, Hn)`-bimodule map. This is the first tower datum of the Jones basic
construction; for Hecke algebras it is classically built from the
Kazhdan–Lusztig/word filtration (`ε` reads off the coefficient layer over
the parabolic subalgebra), which is exactly what Mathlib lacks at
general rank. OPEN — no instance. -/
class HeckeConditionalExpectation (R : Type*) [Field R] (q : R)
    (Hn Hn1 : Type*) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn : ℕ → Hn) (σn1 : ℕ → Hn1)
    [HeckeBraidedPresentation R q Hn σn] [HeckeBraidedPresentation R q Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn) : Prop where
  /-- `ε` retracts the tower inclusion: `ε (ι x) = x`. -/
  retract : ∀ x : Hn, ε (ι x) = x
  /-- `ε` is an `(Hn, Hn)`-bimodule map:
  `ε (ι x * y * ι z) = x * ε y * z`. -/
  bimodule : ∀ (x z : Hn) (y : Hn1), ε (ι x * y * ι z) = x * ε y * z

/-- **§3b DEPENDENT conjecture — basic-construction absorption (bean
`qou-iri6`).** GIVEN a conditional expectation, the level-`n` Jones
projection `e = jonesIdempotent q (σn1 n)` absorbs through it:
`e · y · e = ι (ε y) · e` for every `y : Hn1`. This is the defining
relation of the Jones basic construction `⟨Hn1, e⟩`; combined with the
PROVED local layer (`jonesIdempotent_mul_self` at `σn1 n`) it generates
the Temperley–Lieb quotient tower. OPEN — no instance. -/
class JonesBasicConstruction (R : Type*) [Field R] (q : R)
    (Hn Hn1 : Type*) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn : ℕ → Hn) (σn1 : ℕ → Hn1)
    [HeckeBraidedPresentation R q Hn σn] [HeckeBraidedPresentation R q Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn)
    [HeckeConditionalExpectation R q Hn Hn1 σn σn1 ι ε] (n : ℕ) : Prop where
  /-- Absorption: `e · y · e = ι (ε y) · e` with
  `e = jonesIdempotent q (σn1 n)`. -/
  absorb : ∀ y : Hn1,
    jonesIdempotent q (σn1 n) * y * jonesIdempotent q (σn1 n) =
      ι (ε y) * jonesIdempotent q (σn1 n)

/-- **§3b DEPENDENT conjecture — the Wenzl tower step (bean `qou-2c4t`,
the A1 apex).** GIVEN the presentations, the inclusion, and the Markov
trace at level `n+1`, semisimplicity ASCENDS the tower wherever the
trace is nondegenerate: if `Hn` is semisimple and `trn1` has no nonzero
left kernel, then `Hn1` is semisimple. This is Wenzl's induction step
[wenzl1988, Thm 2.2]; the proved rungs `isSemisimpleRing_H3A` (and the
rank-2 `HeckeH2Wedderburn`) realize its conclusion concretely at
`n = 2, 3` without the tower machinery. OPEN — no instance; proving this
class's field for symmetric-group Coxeter data is exactly the general-`n`
target the explicit-Wedderburn route cannot reach. -/
class WenzlTowerStep (R : Type*) [Field R] (q : R)
    (Hn Hn1 : Type*) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn : ℕ → Hn) (σn1 : ℕ → Hn1)
    [HeckeBraidedPresentation R q Hn σn] [HeckeBraidedPresentation R q Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (trn1 : Hn1 → R) : Prop where
  /-- Semisimplicity ascends along a nondegenerate Markov trace. -/
  semisimple_ascend :
    IsSemisimpleRing Hn →
    (∀ y : Hn1, y ≠ 0 → ∃ z : Hn1, trn1 (y * z) ≠ 0) →
    IsSemisimpleRing Hn1

end QOU.Machinery.HeckeTower
