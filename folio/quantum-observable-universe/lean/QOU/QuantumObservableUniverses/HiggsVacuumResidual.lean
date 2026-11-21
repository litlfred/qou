import Mathlib.CategoryTheory.Monoidal.Linear
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

/-!
# QOU.QuantumObservableUniverses.HiggsVacuumResidual — the vacuum idempotent and its residual

Content block: `prop:higgs-vacuum-residual-idempotent`
(`knots-particles-confinement/higgs-vacuum-residual-idempotent.md`).

Constraint (G-4) of `conj:g-action-on-substrate` defines the Higgs idempotent
`e_H = ϱ_Φ ϱ_Φ^* / tr(ϱ_Φ^* ϱ_Φ)` from a vacuum morphism `ϱ_Φ : 𝟙 → A^{(H)}`.
In `GActionOnSubstrate.lean` that datum is recorded only as a real number
(`qDimHiggsIdempotent`). This file supplies the honest morphism-level
statement, in an arbitrary `K`-linear category (`K` a field):

* **(a)** Given a point `ϱ : U ⟶ X`, a copoint `ϱ* : X ⟶ U` and a scalar
  `t ≠ 0` with `ϱ ≫ ϱ* = t • 𝟙 U`, the endomorphism
  `e = t⁻¹ • (ϱ* ≫ ϱ) : X ⟶ X` is idempotent (`PointCopoint.proj_idem`), it
  fixes the point and the copoint, and the **residual** `r = 𝟙 X - e` is the
  complementary idempotent (`resid_idem`, `proj_comp_resid`,
  `resid_comp_proj`, `proj_add_resid`) and annihilates the vacuum
  (`pt_comp_resid`, `resid_comp_copt`). The Higgs case is `U = 𝟙_ C`
  (`VacuumPairing`). Mathlib's `≫` is diagrammatic, so `ϱ* ≫ ϱ` is the
  composite `X → 𝟙 → X`, written `ϱ ϱ*` in the paper's applicative order.

* **(b)** For an involution `σ` (`σ ≫ σ = 𝟙`) and a scalar `c` with
  `c + c = 1` (i.e. `c = 1/2`, which exists iff `char K ≠ 2`), the
  symmetriser `P₊ = c • (𝟙 + σ)` and antisymmetriser `P₋ = c • (𝟙 - σ)` are
  complementary orthogonal idempotents, `σ`-even and `σ`-odd, and they commute
  with every endomorphism that commutes with `σ`. In a symmetric monoidal
  `K`-linear category with `σ = β_{X,X}` this applies to `e ⊗ e`: the
  residual `𝟙 - e ⊗ e` of the two-vacuum idempotent splits as the sum of the
  two idempotents `(𝟙 - e ⊗ e) ≫ P₊` and `(𝟙 - e ⊗ e) ≫ P₋`, which are
  orthogonal (`tensorResid_split`, `tensorResid_symPart_idem`,
  `tensorResid_altPart_idem`, `tensorResid_symPart_comp_altPart`). The
  residual itself expands as `e ⊗ r + r ⊗ e + r ⊗ r`
  (`tensorResid_eq`), and the purely residual summand carries its own
  symmetric idempotent `(r ⊗ r) ≫ P₊` (`residSq_symPart_idem`).

* **(a′)** For any additive, `K`-homogeneous, cyclic `K`-valued trace `tr`
  on endomorphisms (`CyclicTrace`), `tr e = tr (𝟙 U)` and
  `tr r = tr (𝟙 X) - tr (𝟙 U)` (`tr_proj`, `tr_resid`). For the Higgs datum
  with `tr (𝟙 (𝟙_ C)) = 1`, `tr e_H = 1` (`VacuumPairing.tr_proj_eq_one`).

No rigidity is used: the idempotent algebra needs only the scalar pairing
`ϱ ≫ ϱ* = t • 𝟙`. In a rigid category `ϱ*` would be obtained from `ϱ` by a
self-duality of `X`; that construction is not formalised here. The trace in
(a′) is a hypothesis (a `CyclicTrace` structure), not a construction of the
pivotal trace of `Rep(SU_q(2))`. No representation-theoretic identification
(spin) is claimed. Everything is a theorem about the stated hypotheses; the reading of
`(r ⊗ r) ≫ P₊` as a graviton channel is interpretation and lives only in the
remark `rem:higgs-vacuum-residual-graviton`.

Base ring: an arbitrary field `K` (§7c: algebraic only, no archimedean input).

LaTeX label: `prop:higgs-vacuum-residual-idempotent`
-/

namespace QOU.QuantumObservableUniverses

open CategoryTheory CategoryTheory.MonoidalCategory

universe v u

/-! ## (a) Point / copoint pairs and the normalised idempotent -/

section PointCopointSection

variable (K : Type*) [Field K] {C : Type u} [Category.{v} C] [Preadditive C] [Linear K C]

/-- A **point / copoint pair through `U`** with invertible pairing: morphisms
`pt : U ⟶ X` and `copt : X ⟶ U` with `pt ≫ copt = scalar • 𝟙 U`,
`scalar ≠ 0`. For `U = 𝟙_ C` this is the vacuum datum `(ϱ_Φ, ϱ_Φ^*)` of
Constraints (G-3)/(G-4); `scalar` is the endomorphism `ϱ_Φ^* ϱ_Φ` of the unit
read as a scalar, which agrees with (G-3)'s `tr_F(ϱ_Φ^* ϱ_Φ)` when the trace
normalises the unit (`tr_F (𝟙 𝟙) = 1`). -/
structure PointCopoint (U X : C) where
  /-- The point `ϱ : U ⟶ X`. -/
  pt : U ⟶ X
  /-- The copoint `ϱ* : X ⟶ U`. -/
  copt : X ⟶ U
  /-- The pairing scalar `t`. -/
  scalar : K
  /-- The pairing is invertible. -/
  scalar_ne_zero : scalar ≠ 0
  /-- `ϱ ≫ ϱ* = t • 𝟙 U`. -/
  pt_comp_copt : pt ≫ copt = scalar • 𝟙 U

/-- The **Higgs vacuum datum**: a point / copoint pair through the monoidal
unit, `ϱ_Φ : 𝟙 ⟶ X`, `ϱ_Φ^* : X ⟶ 𝟙`, `ϱ_Φ ≫ ϱ_Φ^* = t • 𝟙_𝟙`. -/
abbrev VacuumPairing [MonoidalCategory C] (X : C) := PointCopoint K (𝟙_ C) X

namespace PointCopoint

variable {K} {U X : C} (P : PointCopoint K U X)

/-- The normalised idempotent `e = t⁻¹ • (ϱ* ≫ ϱ) : X ⟶ X`
(the paper's `e_H = ϱ ϱ^* / t`). -/
def proj : X ⟶ X := P.scalar⁻¹ • (P.copt ≫ P.pt)

/-- The **residual** `r = 𝟙 X - e`. -/
def resid : X ⟶ X := 𝟙 X - P.proj

theorem pt_comp_copt_assoc {Z : C} (f : U ⟶ Z) : P.pt ≫ P.copt ≫ f = P.scalar • f := by
  rw [← Category.assoc, P.pt_comp_copt, Linear.smul_comp, Category.id_comp]

/-- `e ≫ e = e`. -/
theorem proj_idem : P.proj ≫ P.proj = P.proj := by
  unfold proj
  rw [Linear.smul_comp, Linear.comp_smul, smul_smul, Category.assoc, P.pt_comp_copt_assoc,
    Linear.comp_smul, smul_smul, mul_assoc, inv_mul_cancel₀ P.scalar_ne_zero, mul_one]

/-- The idempotent fixes the point: `ϱ ≫ e = ϱ`. -/
theorem pt_comp_proj : P.pt ≫ P.proj = P.pt := by
  unfold proj
  rw [Linear.comp_smul, P.pt_comp_copt_assoc, smul_smul, inv_mul_cancel₀ P.scalar_ne_zero,
    one_smul]

/-- The idempotent fixes the copoint: `e ≫ ϱ* = ϱ*`. -/
theorem proj_comp_copt : P.proj ≫ P.copt = P.copt := by
  unfold proj
  rw [Linear.smul_comp, Category.assoc, P.pt_comp_copt, Linear.comp_smul, Category.comp_id,
    smul_smul, inv_mul_cancel₀ P.scalar_ne_zero, one_smul]

/-- `e + r = 𝟙 X`. -/
theorem proj_add_resid : P.proj + P.resid = 𝟙 X := by
  unfold resid
  abel

/-- The residual is idempotent: `r ≫ r = r`. -/
theorem resid_idem : P.resid ≫ P.resid = P.resid := by
  unfold resid
  simp only [Preadditive.sub_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id,
    P.proj_idem]
  abel

/-- `e ≫ r = 0`. -/
theorem proj_comp_resid : P.proj ≫ P.resid = 0 := by
  unfold resid
  rw [Preadditive.comp_sub, Category.comp_id, P.proj_idem, sub_self]

/-- `r ≫ e = 0`. -/
theorem resid_comp_proj : P.resid ≫ P.proj = 0 := by
  unfold resid
  rw [Preadditive.sub_comp, Category.id_comp, P.proj_idem, sub_self]

/-- The residual annihilates the point: `ϱ ≫ r = 0`. -/
theorem pt_comp_resid : P.pt ≫ P.resid = 0 := by
  unfold resid
  rw [Preadditive.comp_sub, Category.comp_id, P.pt_comp_proj, sub_self]

/-- The residual annihilates the copoint: `r ≫ ϱ* = 0`. -/
theorem resid_comp_copt : P.resid ≫ P.copt = 0 := by
  unfold resid
  rw [Preadditive.sub_comp, Category.id_comp, P.proj_comp_copt, sub_self]

end PointCopoint

end PointCopointSection

/-! ## (a′) Trace of the vacuum idempotent

Any additive, `K`-homogeneous, cyclic `K`-valued trace on endomorphisms — the
properties the categorical trace of a pivotal `K`-linear category has — sends
the normalised idempotent of a point / copoint pair through `U` to the trace of
`𝟙 U`. For the Higgs datum (`U = 𝟙_ C`) the trace of `e_H` is therefore the
dimension of the unit, whatever the dimension of `X`. -/

section TraceSection

variable (K : Type*) [Field K] (C : Type u) [Category.{v} C] [Preadditive C] [Linear K C]

/-- An additive, `K`-homogeneous, cyclic `K`-valued trace on endomorphisms.
Cyclicity is required across objects: `tr (f ≫ g) = tr (g ≫ f)` for
`f : Y ⟶ Z`, `g : Z ⟶ Y`. -/
structure CyclicTrace where
  /-- The trace of an endomorphism. -/
  tr : ∀ {Y : C}, (Y ⟶ Y) → K
  /-- Additivity. -/
  tr_add : ∀ {Y : C} (f g : Y ⟶ Y), tr (f + g) = tr f + tr g
  /-- `K`-homogeneity. -/
  tr_smul : ∀ {Y : C} (a : K) (f : Y ⟶ Y), tr (a • f) = a * tr f
  /-- Cyclicity. -/
  tr_comp_comm : ∀ {Y Z : C} (f : Y ⟶ Z) (g : Z ⟶ Y), tr (f ≫ g) = tr (g ≫ f)

variable {K C}

namespace CyclicTrace

variable (T : CyclicTrace K C)

theorem tr_sub {Y : C} (f g : Y ⟶ Y) : T.tr (f - g) = T.tr f - T.tr g := by
  have h := T.tr_add (f - g) g
  rw [sub_add_cancel] at h
  rw [h, add_sub_cancel_right]

end CyclicTrace

namespace PointCopoint

variable {U X : C} (P : PointCopoint K U X) (T : CyclicTrace K C)

/-- **Trace of the vacuum idempotent.** `tr e = tr (𝟙 U)`. -/
theorem tr_proj : T.tr P.proj = T.tr (𝟙 U) := by
  unfold proj
  rw [T.tr_smul, T.tr_comp_comm, P.pt_comp_copt, T.tr_smul, ← mul_assoc,
    inv_mul_cancel₀ P.scalar_ne_zero, one_mul]

/-- **Trace of the residual.** `tr r = tr (𝟙 X) - tr (𝟙 U)`. -/
theorem tr_resid : T.tr P.resid = T.tr (𝟙 X) - T.tr (𝟙 U) := by
  unfold resid
  rw [T.tr_sub, P.tr_proj]

end PointCopoint

/-- **Higgs case.** For a vacuum pairing through the monoidal unit, if the
trace normalises the unit (`tr (𝟙 (𝟙_ C)) = 1`), then `tr e_H = 1`, and any
value `d` asserted for `tr e_H` must equal `1`. -/
theorem VacuumPairing.tr_proj_eq_one [MonoidalCategory C] {X : C}
    (P : VacuumPairing K X) (T : CyclicTrace K C) (h1 : T.tr (𝟙 (𝟙_ C)) = 1) :
    T.tr P.proj = 1 := by
  rw [P.tr_proj T, h1]

/-- Under the same normalisation, `tr e_H = d` forces `d = 1`. -/
theorem VacuumPairing.eq_one_of_tr_proj_eq [MonoidalCategory C] {X : C}
    (P : VacuumPairing K X) (T : CyclicTrace K C) (h1 : T.tr (𝟙 (𝟙_ C)) = 1) {d : K}
    (hd : T.tr P.proj = d) : d = 1 := by
  rw [← hd, VacuumPairing.tr_proj_eq_one P T h1]

end TraceSection

/-! ## (b) Involutions: symmetric / antisymmetric idempotents -/

section Involution

variable {K : Type*} [Field K] {C : Type u} [Category.{v} C] [Preadditive C] [Linear K C]
variable {Y : C} {σ : Y ⟶ Y} {c : K}

/-- The symmetriser `P₊ = c • (𝟙 + σ)` (with `c = 1/2` in use). -/
def symPart (c : K) (σ : Y ⟶ Y) : Y ⟶ Y := c • (𝟙 Y + σ)

/-- The antisymmetriser `P₋ = c • (𝟙 - σ)` (with `c = 1/2` in use). -/
def altPart (c : K) (σ : Y ⟶ Y) : Y ⟶ Y := c • (𝟙 Y - σ)

theorem one_add_comp_self (hσ : σ ≫ σ = 𝟙 Y) :
    (𝟙 Y + σ) ≫ (𝟙 Y + σ) = (𝟙 Y + σ) + (𝟙 Y + σ) := by
  simp only [Preadditive.add_comp, Preadditive.comp_add, Category.id_comp, Category.comp_id, hσ]
  abel

theorem one_sub_comp_self (hσ : σ ≫ σ = 𝟙 Y) :
    (𝟙 Y - σ) ≫ (𝟙 Y - σ) = (𝟙 Y - σ) + (𝟙 Y - σ) := by
  simp only [Preadditive.sub_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id, hσ]
  abel

theorem one_add_comp_one_sub (hσ : σ ≫ σ = 𝟙 Y) : (𝟙 Y + σ) ≫ (𝟙 Y - σ) = 0 := by
  simp only [Preadditive.add_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id, hσ]
  abel

/-- `P₊ ≫ P₊ = P₊`. -/
theorem symPart_idem (hσ : σ ≫ σ = 𝟙 Y) (hc : c + c = 1) :
    symPart c σ ≫ symPart c σ = symPart c σ := by
  unfold symPart
  rw [Linear.smul_comp, Linear.comp_smul, smul_smul, one_add_comp_self hσ, smul_add,
    ← add_smul, ← mul_add, hc, mul_one]

/-- `P₋ ≫ P₋ = P₋`. -/
theorem altPart_idem (hσ : σ ≫ σ = 𝟙 Y) (hc : c + c = 1) :
    altPart c σ ≫ altPart c σ = altPart c σ := by
  unfold altPart
  rw [Linear.smul_comp, Linear.comp_smul, smul_smul, one_sub_comp_self hσ, smul_add,
    ← add_smul, ← mul_add, hc, mul_one]

/-- `P₊ + P₋ = 𝟙`. -/
theorem symPart_add_altPart (hc : c + c = 1) : symPart c σ + altPart c σ = 𝟙 Y := by
  unfold symPart altPart
  rw [← smul_add, show 𝟙 Y + σ + (𝟙 Y - σ) = 𝟙 Y + 𝟙 Y by abel, smul_add, ← add_smul, hc,
    one_smul]

/-- `P₊ ≫ P₋ = 0`. -/
theorem symPart_comp_altPart (hσ : σ ≫ σ = 𝟙 Y) : symPart c σ ≫ altPart c σ = 0 := by
  unfold symPart altPart
  rw [Linear.smul_comp, Linear.comp_smul, one_add_comp_one_sub hσ]
  simp only [smul_zero]

/-- `P₊` is `σ`-even: `P₊ ≫ σ = P₊`. -/
theorem symPart_comp_sigma (hσ : σ ≫ σ = 𝟙 Y) : symPart c σ ≫ σ = symPart c σ := by
  unfold symPart
  rw [Linear.smul_comp, Preadditive.add_comp, Category.id_comp, hσ, add_comm]

/-- `P₋` is `σ`-odd: `P₋ ≫ σ = -P₋`. -/
theorem altPart_comp_sigma (hσ : σ ≫ σ = 𝟙 Y) : altPart c σ ≫ σ = -altPart c σ := by
  unfold altPart
  rw [Linear.smul_comp, Preadditive.sub_comp, Category.id_comp, hσ, ← smul_neg, neg_sub]

/-- `P₊` commutes with every `E` commuting with `σ`. -/
theorem comp_symPart_comm {E : Y ⟶ Y} (hE : E ≫ σ = σ ≫ E) :
    E ≫ symPart c σ = symPart c σ ≫ E := by
  unfold symPart
  rw [Linear.comp_smul, Linear.smul_comp, Preadditive.comp_add, Preadditive.add_comp,
    Category.comp_id, Category.id_comp, hE]

/-- `P₋` commutes with every `E` commuting with `σ`. -/
theorem comp_altPart_comm {E : Y ⟶ Y} (hE : E ≫ σ = σ ≫ E) :
    E ≫ altPart c σ = altPart c σ ≫ E := by
  unfold altPart
  rw [Linear.comp_smul, Linear.smul_comp, Preadditive.comp_sub, Preadditive.sub_comp,
    Category.comp_id, Category.id_comp, hE]

/-- The complement of an idempotent is idempotent. -/
theorem one_sub_idem {E : Y ⟶ Y} (hE : E ≫ E = E) : (𝟙 Y - E) ≫ (𝟙 Y - E) = 𝟙 Y - E := by
  simp only [Preadditive.sub_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id, hE]
  abel

/-- If `E` commutes with `P`, so does `𝟙 - E`. -/
theorem one_sub_comp_comm {E P : Y ⟶ Y} (h : E ≫ P = P ≫ E) :
    (𝟙 Y - E) ≫ P = P ≫ (𝟙 Y - E) := by
  rw [Preadditive.sub_comp, Preadditive.comp_sub, Category.id_comp, Category.comp_id, h]

omit [Preadditive C] in
/-- The composite of two commuting idempotents is idempotent. -/
theorem comp_idem_of_comm {Q P : Y ⟶ Y} (hQ : Q ≫ Q = Q) (hP : P ≫ P = P)
    (h : Q ≫ P = P ≫ Q) : (Q ≫ P) ≫ (Q ≫ P) = Q ≫ P := by
  rw [Category.assoc, ← Category.assoc P Q P, ← h, Category.assoc, ← Category.assoc Q Q, hQ, hP]

end Involution

/-! ## (b) continued: the two-vacuum residual in a symmetric monoidal category -/

section Symmetric

variable {K : Type*} [Field K] {C : Type u} [Category.{v} C] [Preadditive C] [Linear K C]
  [MonoidalCategory C] [MonoidalPreadditive C] [SymmetricCategory C]

omit [Preadditive C] [MonoidalPreadditive C] in
/-- `f ⊗ f` commutes with the symmetry `β_{X,X}` (naturality of the braiding). -/
theorem tensor_self_comp_braiding {X : C} (f : X ⟶ X) :
    (f ⊗ₘ f) ≫ (β_ X X).hom = (β_ X X).hom ≫ (f ⊗ₘ f) :=
  BraidedCategory.braiding_naturality f f

omit [Preadditive C] [MonoidalPreadditive C] in
/-- The symmetry `β_{X,X}` is an involution. -/
theorem braiding_self_involutive (X : C) : (β_ X X).hom ≫ (β_ X X).hom = 𝟙 (X ⊗ X) :=
  SymmetricCategory.symmetry X X

omit [Preadditive C] [MonoidalPreadditive C] [SymmetricCategory C] in
/-- The tensor square of an idempotent is idempotent. -/
theorem tensor_self_idem {X : C} {f : X ⟶ X} (hf : f ≫ f = f) :
    (f ⊗ₘ f) ≫ (f ⊗ₘ f) = f ⊗ₘ f := by
  rw [MonoidalCategory.tensorHom_comp_tensorHom, hf]

namespace PointCopoint

variable {U X : C} (P : PointCopoint K U X)

/-- The two-vacuum idempotent `e ⊗ e` on `X ⊗ X`. -/
def tensorProj : X ⊗ X ⟶ X ⊗ X := P.proj ⊗ₘ P.proj

/-- The residual `𝟙 - e ⊗ e` on `X ⊗ X`. -/
def tensorResid : X ⊗ X ⟶ X ⊗ X := 𝟙 (X ⊗ X) - P.tensorProj

omit [MonoidalPreadditive C] [SymmetricCategory C] in
theorem tensorProj_idem : P.tensorProj ≫ P.tensorProj = P.tensorProj :=
  tensor_self_idem P.proj_idem

omit [MonoidalPreadditive C] [SymmetricCategory C] in
theorem tensorResid_idem : P.tensorResid ≫ P.tensorResid = P.tensorResid :=
  one_sub_idem P.tensorProj_idem

omit [SymmetricCategory C] in
/-- The residual expands as `e ⊗ r + r ⊗ e + r ⊗ r`. -/
theorem tensorResid_eq :
    P.tensorResid = P.proj ⊗ₘ P.resid + P.resid ⊗ₘ P.proj + P.resid ⊗ₘ P.resid := by
  have h1 : 𝟙 (X ⊗ X) = (P.proj + P.resid) ⊗ₘ (P.proj + P.resid) := by
    rw [P.proj_add_resid, MonoidalCategory.id_tensorHom_id]
  unfold tensorResid tensorProj
  rw [h1, MonoidalPreadditive.add_tensor, MonoidalPreadditive.tensor_add,
    MonoidalPreadditive.tensor_add]
  abel

omit [MonoidalPreadditive C] in
theorem tensorProj_comm_symPart (c : K) :
    P.tensorProj ≫ symPart c (β_ X X).hom = symPart c (β_ X X).hom ≫ P.tensorProj :=
  comp_symPart_comm (tensor_self_comp_braiding P.proj)

omit [MonoidalPreadditive C] in
theorem tensorProj_comm_altPart (c : K) :
    P.tensorProj ≫ altPart c (β_ X X).hom = altPart c (β_ X X).hom ≫ P.tensorProj :=
  comp_altPart_comm (tensor_self_comp_braiding P.proj)

omit [MonoidalPreadditive C] in
theorem tensorResid_comm_symPart (c : K) :
    P.tensorResid ≫ symPart c (β_ X X).hom = symPart c (β_ X X).hom ≫ P.tensorResid :=
  one_sub_comp_comm (P.tensorProj_comm_symPart c)

omit [MonoidalPreadditive C] in
theorem tensorResid_comm_altPart (c : K) :
    P.tensorResid ≫ altPart c (β_ X X).hom = altPart c (β_ X X).hom ≫ P.tensorResid :=
  one_sub_comp_comm (P.tensorProj_comm_altPart c)

omit [MonoidalPreadditive C] in
/-- The symmetric part of the two-vacuum residual is an idempotent. -/
theorem tensorResid_symPart_idem {c : K} (hc : c + c = 1) :
    (P.tensorResid ≫ symPart c (β_ X X).hom) ≫ (P.tensorResid ≫ symPart c (β_ X X).hom) =
      P.tensorResid ≫ symPart c (β_ X X).hom :=
  comp_idem_of_comm P.tensorResid_idem (symPart_idem (braiding_self_involutive X) hc)
    (P.tensorResid_comm_symPart c)

omit [MonoidalPreadditive C] in
/-- The antisymmetric part of the two-vacuum residual is an idempotent. -/
theorem tensorResid_altPart_idem {c : K} (hc : c + c = 1) :
    (P.tensorResid ≫ altPart c (β_ X X).hom) ≫ (P.tensorResid ≫ altPart c (β_ X X).hom) =
      P.tensorResid ≫ altPart c (β_ X X).hom :=
  comp_idem_of_comm P.tensorResid_idem (altPart_idem (braiding_self_involutive X) hc)
    (P.tensorResid_comm_altPart c)

omit [MonoidalPreadditive C] in
/-- **Splitting of the residual.** `𝟙 - e ⊗ e` is the sum of its symmetric and
antisymmetric parts. -/
theorem tensorResid_split {c : K} (hc : c + c = 1) :
    P.tensorResid ≫ symPart c (β_ X X).hom + P.tensorResid ≫ altPart c (β_ X X).hom =
      P.tensorResid := by
  rw [← Preadditive.comp_add, symPart_add_altPart hc, Category.comp_id]

omit [MonoidalPreadditive C] in
/-- The two parts of the residual are orthogonal. -/
theorem tensorResid_symPart_comp_altPart (c : K) :
    (P.tensorResid ≫ symPart c (β_ X X).hom) ≫ (P.tensorResid ≫ altPart c (β_ X X).hom) = 0 := by
  rw [Category.assoc, ← Category.assoc (symPart c (β_ X X).hom) P.tensorResid,
    ← P.tensorResid_comm_symPart c, Category.assoc,
    symPart_comp_altPart (braiding_self_involutive X)]
  simp

omit [MonoidalPreadditive C] in
/-- The purely residual summand `r ⊗ r` carries its own symmetric idempotent
`(r ⊗ r) ≫ P₊` (the `Sym²` of the residual). -/
theorem residSq_symPart_idem {c : K} (hc : c + c = 1) :
    ((P.resid ⊗ₘ P.resid) ≫ symPart c (β_ X X).hom) ≫
        ((P.resid ⊗ₘ P.resid) ≫ symPart c (β_ X X).hom) =
      (P.resid ⊗ₘ P.resid) ≫ symPart c (β_ X X).hom :=
  comp_idem_of_comm (tensor_self_idem P.resid_idem) (symPart_idem (braiding_self_involutive X) hc)
    (comp_symPart_comm (tensor_self_comp_braiding P.resid))

end PointCopoint

end Symmetric

end QOU.QuantumObservableUniverses
