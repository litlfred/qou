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
`e·ι₂ y·e = ι₂(ι(ε y))·e` one level up (`JonesBasicConstruction`), and the Wenzl ascent
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

/-- **Rank-bounded braided presentation.** The three Hecke relations, each
guarded so it only speaks about generators that exist at rank `n`:
`σ₀, …, σ_{n-2}` for `H_n`.

Compare `HeckeBraidedCategory.HeckeBraidedPresentation`, whose unguarded `∀ i`
forces an infinite generator family — the reason it has no contentful instance.
The guards here are exactly what makes a finite algebra able to satisfy it. -/
class HeckeBraidedPresentationOfRank (q : R) (n : ℕ) (H : Type*)
    [Ring H] [Algebra R H] (σ : ℕ → H) : Prop where
  /-- Hecke quadratic, for generators present at rank `n`. -/
  hecke_quadratic : ∀ i, i + 1 < n → σ i * σ i = (q - q⁻¹) • σ i + 1
  /-- Braid relation, for adjacent pairs both present at rank `n`. -/
  braid_adjacent : ∀ i, i + 2 < n → σ i * σ (i + 1) * σ i = σ (i + 1) * σ i * σ (i + 1)
  /-- Far commutation, for non-adjacent pairs both present at rank `n`. -/
  far_commute : ∀ i j, i + 1 < j → j + 1 < n → σ i * σ j = σ j * σ i

/-- The unbounded class implies the bounded one at every rank — the guards only
discard obligations. So existing consumers lose nothing by moving over. -/
theorem ofRank_of_unbounded {q : R} {H : Type*} [Ring H] [Algebra R H]
    {σ : ℕ → H} [inst : QOU.Machinery.HeckeBraidedCategory.HeckeBraidedPresentation R q H σ]
    (n : ℕ) : HeckeBraidedPresentationOfRank q n H σ where
  hecke_quadratic i _ := inst.hecke_quadratic i
  braid_adjacent i _ := inst.braid_adjacent i
  far_commute i j hij _ := inst.far_commute i j hij

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
class HeckeConditionalExpectation (R : Type*) [Field R] (q : R) (rank : ℕ)
    (Hn Hn1 : Type*) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn) : Prop where
  /-- `ε` retracts the tower inclusion: `ε (ι x) = x`. -/
  retract : ∀ x : Hn, ε (ι x) = x
  /-- `ε` is an `(Hn, Hn)`-bimodule map:
  `ε (ι x * y * ι z) = x * ε y * z`. -/
  bimodule : ∀ (x z : Hn) (y : Hn1), ε (ι x * y * ι z) = x * ε y * z

/-- **§3b DEPENDENT conjecture — basic-construction absorption (bean
`qou-iri6`).** Three levels `Hn ⊂ Hn1 ⊂ Hn2`, with `ι : Hn → Hn1`,
`ι₂ : Hn1 → Hn2`, and a conditional expectation `ε : Hn1 → Hn`. The Jones
projection `e = jonesIdempotent q (σn2 n)` lives one level **above** `Hn1`, and
for every `y : Hn1` it absorbs through `ε`:
`e · ι₂ y · e = ι₂ (ι (ε y)) · e`. This is the defining relation of the Jones
basic construction `⟨Hn1, e⟩` ([jones1983] §3: `e x e = E_N(x) e` for `x ∈ M`).
The field `compat` asks that `ι₂` carry the lower generators to the upper ones.

**Restated 2026-11-21 (owner "Fix", bean `qou-c8p8`).** The earlier form used
two levels and took `e = jonesIdempotent q (σn1 n)` inside `Hn1` itself, so `y`
could be `e`. With `e² = e`, absorption at `y = e` gave `e = ι(ε e) · e`, which
forces `e = 0` at every Markov expectation `ε(e) = τ•1` with `τ ≠ 1`
(`QOU.Machinery.HeckeTower.Instances.sameLevel_forces_e_eq_zero`). OPEN — no
general instance. -/
class JonesBasicConstruction (R : Type*) [Field R] (q : R) (rank : ℕ)
    (Hn Hn1 Hn2 : Type*) [Ring Hn] [Ring Hn1] [Ring Hn2]
    [Algebra R Hn] [Algebra R Hn1] [Algebra R Hn2]
    (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (σn2 : ℕ → Hn2) [HeckeBraidedPresentationOfRank q (rank + 1) Hn2 σn2]
    (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn)
    [HeckeConditionalExpectation R q rank Hn Hn1 σn1 ι ε]
    (ι₂ : Hn1 →ₐ[R] Hn2) (n : ℕ) : Prop where
  /-- `ι₂` carries the generators of `Hn1` to those of `Hn2`. -/
  compat : ∀ i, i + 1 < rank → ι₂ (σn1 i) = σn2 i
  /-- Absorption: `e · ι₂ y · e = ι₂ (ι (ε y)) · e` with
  `e = jonesIdempotent q (σn2 n)`, for every `y : Hn1`. -/
  absorb : ∀ y : Hn1,
    jonesIdempotent q (σn2 n) * ι₂ y * jonesIdempotent q (σn2 n) =
      ι₂ (ι (ε y)) * jonesIdempotent q (σn2 n)

/-- **§3b DEPENDENT conjecture — the Wenzl tower step (bean `qou-2c4t`,
the A1 apex).** GIVEN the presentations, the inclusion, and the Markov
trace at level `n+1`, semisimplicity ASCENDS the tower wherever the
trace is nondegenerate: if `Hn` is semisimple and `trn1` has no nonzero
left kernel, then `Hn1` is semisimple. This is Wenzl's induction step
[wenzl1988, Thm 2.2]; the proved rungs `isSemisimpleRing_H3A` (and the
rank-2 `HeckeH2Wedderburn`) realize its conclusion concretely at
`n = 2, 3` without the tower machinery. Proving this class's field for
symmetric-group Coxeter data at the *Markov* trace is the general-`n`
target the explicit-Wedderburn route cannot reach; it is still open.

**Mathlib does not supply the prerequisite; the CORPUS already does (measured
2026-08-26, bean `qou-kzjl`).** Mathlib's `traceForm_nondegenerate` is

    ∀ (K L) [Field K] [Field L] [Algebra K L] [FiniteDimensional K L]
      [Algebra.IsSeparable K L], (traceForm K L).Nondegenerate

which is wrong here in two independent ways: it runs *separable ⇒ nondegenerate*
where this field needs the converse, and both `K` and `L` are fields where
`H_n(q)` is non-commutative. Mathlib's `isSemisimpleRing_*` family is structural
(`iff_jacobson`, `iff_isArtinianRing`, …), none of it trace-form based.

That Mathlib measurement is correct and is NOT a reason to prove anything new
here. The result — *a finite-dimensional algebra over a field with
nondegenerate regular trace form is semisimple* — has been in this corpus since
brick B3d (epic `qou-hnhg`) as
`QOU.MathlibExt.isSemisimpleRing_of_regTraceForm_nondegenerate`, with its
nilpotent-trace core in `QOU.MathlibExt.TraceNilpotent`. Recorded because the
two questions are easy to conflate and one of them was: an exhaustive search of
*Mathlib* says nothing about what the corpus holds.

**What is instantiated, and what is not.**
`QOU.Machinery.HeckeRank.wenzlTowerStep_regTrace` discharges this class's field
at **general rank** for the *regular* trace `w ↦ trace (L_w)`, so the class is
no longer instance-free. It contributes an adapter between two spellings of
nondegeneracy, not a semisimplicity proof. Two things are worth reading off it
rather than assuming. First, the ascent does not consume the `Hn`-semisimple
hypothesis at all — nondegeneracy at level `n+1` is the whole of it, which makes
hypothesis 1 of the field redundant for this trace. Second: the general-`n`
Hecke target needs the field at the **Markov** trace — and that is not merely
unproved here, it is **false on `H_n` at the canonical convention D**, so no
instance of this class at the Markov trace on `H_n` can exist. The convention-D
pin `z(q²+1) = q³` forces the antisymmetric Wedderburn weight `y₍₁³₎` to `0`,
that block lies in the radical of the trace form, and `det G = 0` exactly —
`QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` and
`QOU.QBeta.MarkovGramDegenerate.gram_det_eq_zero_of_radical_combination`, both
sorry-free. Independently: the closed-form `n = 3` determinant in
`gram-matrix-h3-symbolic` carries the factor `(q²+1)z − q³`, which *is* the
convention-D pin rearranged, so `det G` vanishes identically in `q` there.

The Frobenius structure is real but lives on the quotient `H_n / rad τ ≅ TL_n(δ)`
(`pairing_descends`, `mem_radical_of_pairing_zero`), matching
`prop:markov-trace-frobenius-selection` (iii). Discharging this class at the
Markov trace over that quotient is bean `qou-s7z2`; it is genuine work, since
both the braided presentation and the tower inclusion must be restated for the
quotient. The nearest abstract statement remains
`QOU.MathlibExt.isSemisimpleRing_of_qGeneric`, which reaches semisimplicity from
`q`-genericity but takes the Gram–factorial equivalence as a hypothesis, and
whose own open input — the general `T_w`-basis determinant, the classical
Schur-element product formula — is unchanged by any of this.

-/
class WenzlTowerStep (R : Type*) [Field R] (q : R) (rank : ℕ)
    (Hn Hn1 : Type*) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (trn1 : Hn1 → R) : Prop where
  /-- Semisimplicity ascends along a nondegenerate Markov trace. -/
  semisimple_ascend :
    IsSemisimpleRing Hn →
    (∀ y : Hn1, y ≠ 0 → ∃ z : Hn1, trn1 (y * z) ≠ 0) →
    IsSemisimpleRing Hn1

/-- **§3b DEPENDENT conjecture — the coset spanning decomposition (bean
`qou-zm8z`).** GIVEN the two Hecke braided presentations and the tower
inclusion `ιlow : Hlow →ₐ Hn`, every element of the larger algebra splits as

  `w = ιlow a + Σᵢ ιlow (b i) · σn n · ιlow (c i)`

i.e. `Hn = Hlow + Hlow · σₙ · Hlow` — the level-`n` algebra is spanned by the
lower one together with its `σₙ`-double-coset. Classically this is Iwahori's
basis theorem / the Coxeter length filtration: a reduced word either avoids the
top generator (first summand) or factors through exactly one occurrence of it
(the sum). Mathlib has neither at general rank, which is why this is a class.

**This is the brick Ocneanu cyclicity induction actually runs on.** The
inductive step reduces `tr(w₁w₂)` to words of the shape `u·g·v`, and reaching
an ARBITRARY pair needs exactly this spanning statement to put a general `w`
into that shape. Without it the induction is stated only for already-decomposed
words. It was named as a deliverable of the W2 re-scope note (bean `qou-2017`)
alongside `HeckeConditionalExpectation` and `JonesBasicConstruction` and, unlike
those two, was never built.

Independent of the conditional expectation: it mentions neither `ε` nor the
Jones projection, so it can be discharged separately, and a proof of it does not
need any trace at all. OPEN — no instance. -/
class HeckeCosetSpanning (R : Type*) [Field R] (q : R) (rank : ℕ)
    (Hlow Hn : Type*) [Ring Hlow] [Ring Hn] [Algebra R Hlow] [Algebra R Hn]
    (σn : ℕ → Hn) [HeckeBraidedPresentationOfRank q rank Hn σn]
    (ιlow : Hlow →ₐ[R] Hn) (k : ℕ) : Prop where
  /-- Every `w : Hn` decomposes over the lower algebra and its `σ k`-coset. -/
  spanning : ∀ w : Hn, ∃ (a : Hlow) (s : Finset ℕ) (b c : ℕ → Hlow),
    w = ιlow a + ∑ i ∈ s, ιlow (b i) * σn k * ιlow (c i)

/-- **§3b DEPENDENT conjecture — the Markov property of the conditional
expectation (bean `qou-zm8z`).** GIVEN a conditional expectation, `ε` collapses
the `σₙ`-coset with a single scalar:

  `ε (ιlow b · σₙ · ιlow c) = z • (b · c)`.

This is the defining property of the Markov trace's `z` (the Ocneanu parameter)
at the level of `ε` rather than of `tr`. `HeckeConditionalExpectation` does NOT
imply it — that class has exactly `retract` and `bimodule`, neither of which
says anything about what `ε` does to the top generator, and `bimodule` in
particular only moves `ιlow`-factors across `ε`, leaving `ε σₙ` untouched.

**This class ASSUMES the Markov property; it does not derive it.** Its value is
that the assumption is now a named, content-bearing carrier with a stated
dependency edge, instead of an anonymous hypothesis threaded through call sites
— and that, combined with `HeckeCosetSpanning`, it is exactly enough to
*compute* `ε` on an arbitrary element (see
`MarkovTowerBridge.towerE_eq_of_spanning`). That computation is the new content;
the assumption itself is relocated, not discharged. OPEN — no instance. -/
class HeckeMarkovExpectation (R : Type*) [Field R] (q : R) (rank : ℕ)
    (Hlow Hn : Type*) [Ring Hlow] [Ring Hn] [Algebra R Hlow] [Algebra R Hn]
    (σn : ℕ → Hn) [HeckeBraidedPresentationOfRank q rank Hn σn]
    (ιlow : Hlow →ₐ[R] Hn) (εlow : Hn →ₗ[R] Hlow)
    [HeckeConditionalExpectation R q rank Hlow Hn σn ιlow εlow]
    (n : ℕ) (z : R) : Prop where
  /-- `ε` collapses the top-generator coset with the Ocneanu scalar `z`. -/
  markov : ∀ b c : Hlow, εlow (ιlow b * σn n * ιlow c) = z • (b * c)

/-! ## What `HeckeBraidedPresentation` does and does not force

Recorded while trying to build a genuine `HeckeCosetSpanning` instance (bean
`qou-zm8z`). The attempt failed, and it failed one level BELOW the spanning
decomposition — which is worth knowing before anyone else tries.

At the time of writing `HeckeBraidedPresentation` has **no instance anywhere in
the corpus**. The two results below say why that is harder than it looks, and
they are the only two facts needed to see it.

**It is satisfiable, but weakly.** `constant_generator_presentation` gives an
instance from a SINGLE element satisfying the quadratic, with `σ` constant. Both
the braid relation and far-commutation are then `rfl`. So an instance of this
class does not force two distinct generators, does not force the braid relation
to have any content, and does not force anything to fail to commute. It is much
weaker than "is a Hecke algebra".

**And a finite Hecke algebra cannot satisfy it with its true generators.** The
fields quantify over ALL `i : ℕ`, so `H_n` must supply `σ i` beyond its rank.
`far_commute_zero` is the obstruction: `σ 0` must commute with `σ j` for every
`j ≥ 2`. In `H₃` with `σ 0 = σ₁` and `σ 1 = σ₂` that rules out padding with the
last real generator, since `σ₁` and `σ₂` do not commute; and no eventually
periodic padding works either, for the same reason at the next index. The class
describes `H_∞`, not `H_n`.

So a genuine instance needs either the infinite tower, or the class re-stated
with a rank bound (`σ : Fin n → H`, relations guarded by `i + 1 < n`). That is a
change to a class three other classes bind, so it is not made here. -/

/-- **The class is satisfiable — degenerately.** Any single element satisfying
the Hecke quadratic yields an instance via the constant family; braid and
far-commutation hold by `rfl`.

Stated to pin down how weak the class is, not as a recommended instance: nothing
conditional on a `HeckeBraidedPresentation` obtained this way carries Hecke
content. -/
theorem constant_generator_presentation {R : Type*} [Field R] {q : R}
    {H : Type*} [Ring H] [Algebra R H] (s : H)
    (hs : s * s = (q - q⁻¹) • s + 1) :
    HeckeBraidedPresentation R q H (fun _ => s) where
  hecke_quadratic := fun _ => hs
  braid_adjacent := fun _ => rfl
  far_commute := fun _ _ _ => rfl

/-- **The obstruction to a finite-rank instance.** `far_commute` forces `σ 0` to
commute with every `σ j` for `j ≥ 2` — so the generators past rank cannot be
padded with a non-commuting real generator. -/
theorem far_commute_zero {R : Type*} [Field R] {q : R}
    {H : Type*} [Ring H] [Algebra R H] (σ : ℕ → H)
    [inst : HeckeBraidedPresentation R q H σ] (j : ℕ) (hj : 2 ≤ j) :
    σ 0 * σ j = σ j * σ 0 :=
  inst.far_commute 0 j (by omega)

end QOU.Machinery.HeckeTower
