import HeckeTemperleyLieb.TLQuotientModularData
import Mathlib.CategoryTheory.Linear.Basic

/-!
# The semisimplified Temperley–Lieb category on all strand counts at once

Bean `hkmt`. `TLRectangularHom` builds, for each bound `N`, the category `TLObj T hε N` of
objects `[a]` (`a + 1` strands, `a ≤ N`) with hom spaces the corners `[b] · Q N · [a]` of the
quotient by negligibles, and shows that the cup map `stab : TLObj N ⥤ TLObj (N + 2)` is full and
faithful. This file glues all the levels into **one** `K`-linear category and moves the simples,
the braiding, the trace and the modular data onto it.

## Parity

Adding two strands keeps the parity of the strand count, so the levels form two chains
(`N` even, `N` odd). Inside level `N` the object `[a]` with `N − a` odd is `P a N = 0`, a zero
object (`P_eq_zero_of_parity`). The legs below therefore start from `LObj T hε N`, the objects
of level `N` with the right parity.

## The glued category `GObj T hε`

Objects are labels `a : ℕ` (the object `[a]` has `a + 1` strands). A morphism `[a] → [b]` is a
sequence `f : ∀ N, Q T N` that is eventually a morphism `[a] → [b]` at level `N` and eventually
stable under adding two strands (`capQ (f N) = f (N + 2)`), taken modulo sequences that are
eventually `0`. That is the direct limit of the hom spaces along `capQ`. Composition is the
pointwise product. Both parities live in one sequence: between labels of different parity every
hom space is `0` (`hom_eq_zero_of_parity`). So this is the colimit in **linear** categories, where
the two chains are joined by zero hom spaces. (The colimit in `Cat` would have no morphisms at all
between the two parities.)

* `GObj T hε` is a `Category`, `Preadditive` and `Linear K`.
* `leg N : LObj T hε N ⥤ GObj T hε` is **full and faithful** (`leg_full`, `leg_faithful`).
* `stabL_comp_leg`: `stabL N ⋙ leg (N + 2) = leg N`, so the legs form a cocone.
* Every object is in the image of a leg (`leg_obj`), and so is every morphism between objects of
  the same parity (fullness).

## What descends

* `endEquiv a : Q T a ≃ₐ[K] End [a]`: the endomorphism algebra of `[a]` in the glued category is
  the quotient algebra `Q a` on `a + 1` strands.
* `simples_glued`: at a primitive `2(k+2)`-th root, every simple idempotent of every `End [a]` is
  isomorphic (Murray–von Neumann) to the image of a standard object with labels below `k`, and
  that image is nonzero.
* `crossingG_*`, `jw_mul_fullTwistG`: the crossings, their inverses, the braid relations and the
  twist eigenvalue on `End [n]`.
* `trG`: the trace on `End [a]`. It is cyclic and nondegenerate (`trG_comm`,
  `trG_nondegenerate`). `trG_level`: computed at any level `a + 2k` with the unnormalised
  weight `δ^{N+1}`, it gives the same number, so the trace does not depend on the level.
* `cH_eq_trG` and `modular_data_glued`: the Hopf-link entries are glued traces, and the braid
  `S`-matrix on the complete list of simples is `[(i+1)(j+1)]` and invertible.

Not here: the monoidal structure (the thread proving the Hecke category modular owns it), the
unit object (labels start at one strand), and the universal property of the colimit against an
arbitrary linear cocone.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] Index for subfactors, §4.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLGlued

open CategoryTheory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLHopfRow
open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLBraidedModular
open QOU.HeckeTemperleyLieb.TLRectHom QOU.HeckeTemperleyLieb.TLQuotientModular

/-! ## Parity -/

section Parity

variable {K : Type*} [Field K] (δ : K)

/-- `[a]` vanishes at a level of the wrong parity. -/
theorem P_eq_zero_of_parity {a : ℕ} : ∀ N, N % 2 ≠ a % 2 → P δ a N = 0
  | 0, h => by simp only [P]; rw [if_neg (by omega)]
  | 1, h => by simp only [P]; rw [if_neg (by omega)]
  | n + 1 + 1, h => by
    rw [P_succ_succ δ (by omega), P_eq_zero_of_parity n (by omega), capEmb_zero]

end Parity

/-- Two-step induction from `M0`. -/
theorem two_step {M0 : ℕ} {p : ℕ → Prop} (h0 : p M0) (h1 : p (M0 + 1))
    (h2 : ∀ M, M0 ≤ M → p M → p (M + 1 + 1)) : ∀ M, M0 ≤ M → p M := by
  intro M
  induction M using Nat.strong_induction_on with
  | _ M ih =>
    intro hM
    by_cases hlt : M < M0 + 2
    · rcases (show M = M0 ∨ M = M0 + 1 by omega) with rfl | rfl
      · exact h0
      · exact h1
    · obtain ⟨M', rfl⟩ : ∃ M', M = M' + 1 + 1 := ⟨M - 2, by omega⟩
      exact h2 M' (by omega) (ih M' (by omega) (by omega))

section Glue

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

theorem PQ_eq_zero_of_parity {a N : ℕ} (h : N % 2 ≠ a % 2) : PQ T a N = 0 := by
  show ((P δ a N : TLFin K δ N) : Q T N) = 0
  rw [P_eq_zero_of_parity δ N h, RingCon.coe_zero]

/-- A morphism between objects of different parity, or at a level of the wrong parity, is `0`. -/
theorem eq_zero_of_mem_parity {N a b : ℕ} {φ : Q T N} (hφ : φ ∈ HomSp T N a b)
    (h : N % 2 ≠ a % 2 ∨ N % 2 ≠ b % 2) : φ = 0 := by
  rw [← (mem_Hom T).mp hφ]
  rcases h with h | h
  · rw [PQ_eq_zero_of_parity T h, mul_zero]
  · rw [PQ_eq_zero_of_parity T h, zero_mul, zero_mul]

theorem capQ_zero (n : ℕ) : capQ T hε n 0 = 0 := by
  simpa using capQ_smul T hε n 0 0

/-- Two sequences that are stable under adding two strands from `M0` on, and agree at `M0` and
`M0 + 1`, agree from `M0` on. -/
theorem agree {M0 : ℕ} {s t : ∀ N, Q T N}
    (hs : ∀ M, M0 ≤ M → capQ T hε M (s M) = s (M + 1 + 1))
    (ht : ∀ M, M0 ≤ M → capQ T hε M (t M) = t (M + 1 + 1))
    (h0 : s M0 = t M0) (h1 : s (M0 + 1) = t (M0 + 1)) : ∀ M, M0 ≤ M → s M = t M :=
  two_step (p := fun M => s M = t M) h0 h1 fun M hM ih => by
    show s (M + 1 + 1) = t (M + 1 + 1)
    rw [← hs M hM, ← ht M hM, ih]

/-! ## Sequences and the direct limit -/

/-- From level `N0` on, `f` is a morphism `[a] → [b]` and is stable under adding two strands. -/
def Compat (a b : ℕ) (f : ∀ N, Q T N) (N0 : ℕ) : Prop :=
  ∀ N, N0 ≤ N → f N ∈ HomSp T N a b ∧ capQ T hε N (f N) = f (N + 1 + 1)

/-- Eventually compatible sequences. -/
def Seq (a b : ℕ) : Submodule K (∀ N, Q T N) where
  carrier := {f | ∃ N0, Compat T hε a b f N0}
  zero_mem' := ⟨0, fun N _ => ⟨(HomSp T N a b).zero_mem, capQ_zero T hε N⟩⟩
  add_mem' := by
    rintro f g ⟨N1, hf⟩ ⟨N2, hg⟩
    refine ⟨max N1 N2, fun N hN =>
      ⟨(HomSp T N a b).add_mem (hf N (by omega)).1 (hg N (by omega)).1, ?_⟩⟩
    show capQ T hε N (f N + g N) = f (N + 1 + 1) + g (N + 1 + 1)
    rw [capQ_add, (hf N (by omega)).2, (hg N (by omega)).2]
  smul_mem' := by
    rintro c f ⟨N0, hf⟩
    refine ⟨N0, fun N hN => ⟨(HomSp T N a b).smul_mem c (hf N hN).1, ?_⟩⟩
    show capQ T hε N (c • f N) = c • f (N + 1 + 1)
    rw [capQ_smul, (hf N hN).2]

/-- Eventually zero sequences. -/
def EvZ : Submodule K (∀ N, Q T N) where
  carrier := {f | ∃ N0, ∀ N, N0 ≤ N → f N = 0}
  zero_mem' := ⟨0, fun _ _ => rfl⟩
  add_mem' := by
    rintro f g ⟨N1, hf⟩ ⟨N2, hg⟩
    exact ⟨max N1 N2, fun N hN => by
      show f N + g N = 0
      rw [hf N (by omega), hg N (by omega), add_zero]⟩
  smul_mem' := by
    rintro c f ⟨N0, hf⟩
    exact ⟨N0, fun N hN => by show c • f N = 0; rw [hf N hN, smul_zero]⟩

/-- **The glued hom space `Hom([a], [b])`**: the direct limit of the level hom spaces. -/
abbrev GHom (a b : ℕ) : Type _ :=
  ↥(Seq T hε a b) ⧸ (EvZ T).comap (Seq T hε a b).subtype

variable {T hε}

local notation "⟪" f "⟫" => Submodule.Quotient.mk f

theorem compat_of_mem {a b : ℕ} (f : Seq T hε a b) : ∃ N0, Compat T hε a b f.1 N0 := f.2

theorem mk_eq_iff {a b : ℕ} (f g : Seq T hε a b) :
    (⟪f⟫ : GHom T hε a b) = ⟪g⟫ ↔ ∃ N0, ∀ N, N0 ≤ N → f.1 N = g.1 N := by
  rw [Submodule.Quotient.eq, Submodule.mem_comap]
  show (∃ N0, ∀ N, N0 ≤ N → (f - g).1 N = 0) ↔ _
  constructor
  · rintro ⟨N0, h⟩
    exact ⟨N0, fun N hN => sub_eq_zero.mp (show f.1 N - g.1 N = 0 from h N hN)⟩
  · rintro ⟨N0, h⟩
    exact ⟨N0, fun N hN => (show f.1 N - g.1 N = 0 from sub_eq_zero.mpr (h N hN))⟩

variable (T hε) in
/-- The identity sequence `N ↦ [a]`. -/
noncomputable def idSeq (a : ℕ) : Seq T hε a a :=
  ⟨fun N => PQ T a N, a, fun N hN => ⟨id_mem T hε N a, capQ_PQ T hε (by omega)⟩⟩

/-- Pointwise product of sequences. -/
noncomputable def mulSeq {a b c : ℕ} (g : Seq T hε b c) (f : Seq T hε a b) : Seq T hε a c :=
  ⟨g.1 * f.1, by
    obtain ⟨N1, hg⟩ := compat_of_mem g
    obtain ⟨N2, hf⟩ := compat_of_mem f
    refine ⟨max N1 N2, fun N hN => ⟨comp_mem T hε (hf N (by omega)).1 (hg N (by omega)).1, ?_⟩⟩
    show capQ T hε N (g.1 N * f.1 N) = g.1 (N + 1 + 1) * f.1 (N + 1 + 1)
    rw [capQ_mul, (hg N (by omega)).2, (hf N (by omega)).2]⟩

/-- **Composition** in the glued category. -/
noncomputable def compH {a b c : ℕ} (f : GHom T hε a b) (g : GHom T hε b c) : GHom T hε a c :=
  Quotient.liftOn₂' f g (fun f g => ⟪mulSeq g f⟫) (by
    intro f1 g1 f2 g2 hf hg
    have hf' : (⟪f1⟫ : GHom T hε a b) = ⟪f2⟫ := Quotient.sound hf
    have hg' : (⟪g1⟫ : GHom T hε b c) = ⟪g2⟫ := Quotient.sound hg
    rw [mk_eq_iff] at hf' hg' ⊢
    obtain ⟨N1, h1⟩ := hf'
    obtain ⟨N2, h2⟩ := hg'
    exact ⟨max N1 N2, fun N hN => by
      show g1.1 N * f1.1 N = g2.1 N * f2.1 N
      rw [h1 N (by omega), h2 N (by omega)]⟩)

theorem compH_mk {a b c : ℕ} (f : Seq T hε a b) (g : Seq T hε b c) :
    compH (⟪f⟫ : GHom T hε a b) ⟪g⟫ = ⟪mulSeq g f⟫ := rfl

theorem compH_id {a b : ℕ} (f : GHom T hε a b) : compH ⟪idSeq T hε a⟫ f = f := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  rw [compH_mk, mk_eq_iff]
  obtain ⟨N0, hf⟩ := compat_of_mem f
  exact ⟨N0, fun N hN => right_mul_of_mem T hε (hf N hN).1⟩

theorem compH_id' {a b : ℕ} (f : GHom T hε a b) : compH f ⟪idSeq T hε b⟫ = f := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  rw [compH_mk, mk_eq_iff]
  obtain ⟨N0, hf⟩ := compat_of_mem f
  exact ⟨N0, fun N hN => left_mul_of_mem T hε (hf N hN).1⟩

theorem compH_assoc {a b c d : ℕ} (f : GHom T hε a b) (g : GHom T hε b c) (h : GHom T hε c d) :
    compH (compH f g) h = compH f (compH g h) := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  obtain ⟨h, rfl⟩ := Submodule.Quotient.mk_surjective _ h
  rw [compH_mk, compH_mk, compH_mk, compH_mk]
  congr 1
  exact Subtype.ext (funext fun N => (mul_assoc (h.1 N) (g.1 N) (f.1 N)).symm)

theorem compH_add_left {a b c : ℕ} (f f' : GHom T hε a b) (g : GHom T hε b c) :
    compH (f + f') g = compH f g + compH f' g := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  obtain ⟨f', rfl⟩ := Submodule.Quotient.mk_surjective _ f'
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  rw [← Submodule.Quotient.mk_add, compH_mk, compH_mk, compH_mk, ← Submodule.Quotient.mk_add]
  congr 1
  exact Subtype.ext (funext fun N => mul_add (g.1 N) (f.1 N) (f'.1 N))

theorem compH_add_right {a b c : ℕ} (f : GHom T hε a b) (g g' : GHom T hε b c) :
    compH f (g + g') = compH f g + compH f g' := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  obtain ⟨g', rfl⟩ := Submodule.Quotient.mk_surjective _ g'
  rw [← Submodule.Quotient.mk_add, compH_mk, compH_mk, compH_mk, ← Submodule.Quotient.mk_add]
  congr 1
  exact Subtype.ext (funext fun N => add_mul (g.1 N) (g'.1 N) (f.1 N))

theorem compH_smul_left {a b c : ℕ} (r : K) (f : GHom T hε a b) (g : GHom T hε b c) :
    compH (r • f) g = r • compH f g := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  rw [← Submodule.Quotient.mk_smul, compH_mk, compH_mk, ← Submodule.Quotient.mk_smul]
  congr 1
  exact Subtype.ext (funext fun N => mul_smul_comm r (g.1 N) (f.1 N))

theorem compH_smul_right {a b c : ℕ} (r : K) (f : GHom T hε a b) (g : GHom T hε b c) :
    compH f (r • g) = r • compH f g := by
  obtain ⟨f, rfl⟩ := Submodule.Quotient.mk_surjective _ f
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  rw [← Submodule.Quotient.mk_smul, compH_mk, compH_mk, ← Submodule.Quotient.mk_smul]
  congr 1
  exact Subtype.ext (funext fun N => smul_mul_assoc r (g.1 N) (f.1 N))

/-! ## The glued category -/

/-- **Objects of the glued semisimplified Temperley–Lieb category**: labels `a`, the object
`[a]` having `a + 1` strands. -/
structure GObj (T : MarkovTower δ ε) (hε : δ * ε = 1) where
  /-- The object `[a]` has `a + 1` strands. -/
  a : ℕ

/-- **The semisimplified Temperley–Lieb category on all strand counts.** -/
noncomputable instance : Category (GObj T hε) where
  Hom X Y := GHom T hε X.a Y.a
  id X := ⟪idSeq T hε X.a⟫
  comp f g := compH f g
  id_comp f := compH_id f
  comp_id f := compH_id' f
  assoc f g h := compH_assoc f g h

theorem comp_def {X Y Z : GObj T hε} (f : X ⟶ Y) (g : Y ⟶ Z) : f ≫ g = compH f g := rfl

theorem id_def (X : GObj T hε) : 𝟙 X = (⟪idSeq T hε X.a⟫ : GHom T hε X.a X.a) := rfl

noncomputable instance : Preadditive (GObj T hε) where
  homGroup X Y := inferInstanceAs (AddCommGroup (GHom T hε X.a Y.a))
  add_comp _ _ _ f f' g := compH_add_left f f' g
  comp_add _ _ _ f g g' := compH_add_right f g g'

noncomputable instance : Linear K (GObj T hε) where
  homModule X Y := inferInstanceAs (Module K (GHom T hε X.a Y.a))
  smul_comp _ _ _ r f g := compH_smul_left r f g
  comp_smul _ _ _ f r g := compH_smul_right r f g

/-- **Hom spaces between labels of different parity vanish.** -/
theorem hom_eq_zero_of_parity {X Y : GObj T hε} (h : X.a % 2 ≠ Y.a % 2) (f : X ⟶ Y) : f = 0 := by
  obtain ⟨s, rfl⟩ := Submodule.Quotient.mk_surjective _ (show GHom T hε X.a Y.a from f)
  rw [show (0 : X ⟶ Y) = (⟪(0 : Seq T hε X.a Y.a)⟫ : GHom T hε X.a Y.a) from
    (Submodule.Quotient.mk_zero _).symm]
  rw [mk_eq_iff]
  obtain ⟨N0, hs⟩ := compat_of_mem s
  exact ⟨N0, fun N hN => eq_zero_of_mem_parity T (hs N hN).1 (by omega)⟩

/-! ## The levels and the legs -/

variable (T hε) in
/-- **Objects of level `N` of the right parity**: labels `a ≤ N` with `N − a` even. -/
structure LObj (T : MarkovTower δ ε) (hε : δ * ε = 1) (N : ℕ) where
  /-- The object `[a]` has `a + 1` strands. -/
  a : ℕ
  le : a ≤ N
  par : a % 2 = N % 2

/-- **Level `N`**: the corners `[b] · Q N · [a]`, as in `TLObj`, on the objects of the right
parity. -/
noncomputable instance (N : ℕ) : Category (LObj T hε N) where
  Hom X Y := ↥(HomSp T N X.a Y.a)
  id X := ⟨PQ T X.a N, id_mem T hε N X.a⟩
  comp f g := ⟨g.1 * f.1, comp_mem T hε f.2 g.2⟩
  id_comp f := Subtype.ext (right_mul_of_mem T hε f.2)
  comp_id f := Subtype.ext (left_mul_of_mem T hε f.2)
  assoc f g h := Subtype.ext (mul_assoc h.1 g.1 f.1).symm

/-- The underlying element of a level morphism. -/
def lval {N : ℕ} {X Y : LObj T hε N} (f : X ⟶ Y) : Q T N :=
  (show ↥(HomSp T N X.a Y.a) from f).1

theorem lval_mem {N : ℕ} {X Y : LObj T hε N} (f : X ⟶ Y) : lval f ∈ HomSp T N X.a Y.a :=
  (show ↥(HomSp T N X.a Y.a) from f).2

/-- A level morphism from an element of the hom space. -/
def lmk {N : ℕ} {X Y : LObj T hε N} (φ : Q T N) (h : φ ∈ HomSp T N X.a Y.a) : X ⟶ Y :=
  (⟨φ, h⟩ : ↥(HomSp T N X.a Y.a))

theorem lhom_ext {N : ℕ} {X Y : LObj T hε N} {f g : X ⟶ Y} (h : lval f = lval g) : f = g :=
  Subtype.ext h

variable (T hε) in
/-- **Extension of a level-`N` element to all levels**: the iterated cup map from `N` on, `0`
below `N` and at levels of the other parity. -/
noncomputable def ext (N : ℕ) (φ : Q T N) : (M : ℕ) → Q T M
  | 0 => if h : N = 0 then h ▸ φ else 0
  | 1 => if h : N = 1 then h ▸ φ else 0
  | M + 1 + 1 => if h : N = M + 1 + 1 then h ▸ φ else
      if N ≤ M then capQ T hε M (ext N φ M) else 0

variable (T hε) in
theorem ext_self : ∀ (N : ℕ) (φ : Q T N), ext T hε N φ N = φ
  | 0, φ => by rw [ext]; exact dif_pos rfl
  | 1, φ => by rw [ext]; exact dif_pos rfl
  | n + 1 + 1, φ => by rw [ext]; exact dif_pos rfl

variable (T hε) in
theorem ext_succ_succ {N M : ℕ} (φ : Q T N) (hM : N ≤ M) :
    ext T hε N φ (M + 1 + 1) = capQ T hε M (ext T hε N φ M) := by
  rw [ext, dif_neg (by omega), if_pos hM]

variable (T hε) in
theorem ext_succ : ∀ (N : ℕ) (φ : Q T N), ext T hε N φ (N + 1) = 0
  | 0, φ => by rw [ext, dif_neg (by omega)]
  | n + 1, φ => by rw [ext, dif_neg (by omega), if_neg (by omega)]

variable (T hε) in
/-- At levels of the other parity the extension vanishes. -/
theorem ext_parity {N : ℕ} (φ : Q T N) : ∀ k, ext T hε N φ (N + 2 * k + 1) = 0
  | 0 => ext_succ T hε N φ
  | k + 1 => by
    rw [show N + 2 * (k + 1) + 1 = N + 2 * k + 1 + 1 + 1 by omega,
      ext_succ_succ T hε φ (by omega), ext_parity φ k, capQ_zero]

variable (T hε) in
theorem ext_compat {N : ℕ} (φ : Q T N) :
    ∀ M, N ≤ M → capQ T hε M (ext T hε N φ M) = ext T hε N φ (M + 1 + 1) :=
  fun _ hM => (ext_succ_succ T hε φ hM).symm

variable (T hε) in
theorem ext_mem {N a b : ℕ} {φ : Q T N} (hφ : φ ∈ HomSp T N a b) (ha : a ≤ N) (hb : b ≤ N) :
    ∀ M, N ≤ M → ext T hε N φ M ∈ HomSp T M a b :=
  two_step (p := fun M => ext T hε N φ M ∈ HomSp T M a b)
    (by show ext T hε N φ N ∈ _; rw [ext_self]; exact hφ)
    (by show ext T hε N φ (N + 1) ∈ _; rw [ext_succ]; exact (HomSp T _ a b).zero_mem)
    (fun M hM ih => by
      show ext T hε N φ (M + 1 + 1) ∈ _
      rw [ext_succ_succ T hε φ hM]
      exact capQ_mem T hε (by omega) (by omega) ih)

variable (T hε) in
theorem ext_mul_ev {N : ℕ} (φ ψ : Q T N) :
    ∀ M, N ≤ M → ext T hε N (ψ * φ) M = ext T hε N ψ M * ext T hε N φ M :=
  agree T hε (ext_compat T hε _) (fun M hM => by
      show capQ T hε M (ext T hε N ψ M * ext T hε N φ M) =
        ext T hε N ψ (M + 1 + 1) * ext T hε N φ (M + 1 + 1)
      rw [capQ_mul, ext_succ_succ T hε ψ hM, ext_succ_succ T hε φ hM])
    (by show _ = _ * _; rw [ext_self, ext_self, ext_self])
    (by show _ = _ * _; rw [ext_succ, ext_succ, ext_succ, mul_zero])

variable (T hε) in
theorem ext_add_ev {N : ℕ} (φ ψ : Q T N) :
    ∀ M, N ≤ M → ext T hε N (φ + ψ) M = ext T hε N φ M + ext T hε N ψ M :=
  agree T hε (ext_compat T hε _) (fun M hM => by
      show capQ T hε M (ext T hε N φ M + ext T hε N ψ M) =
        ext T hε N φ (M + 1 + 1) + ext T hε N ψ (M + 1 + 1)
      rw [capQ_add, ext_succ_succ T hε φ hM, ext_succ_succ T hε ψ hM])
    (by show _ = _ + _; rw [ext_self, ext_self, ext_self])
    (by show _ = _ + _; rw [ext_succ, ext_succ, ext_succ, add_zero])

variable (T hε) in
theorem ext_smul_ev {N : ℕ} (c : K) (φ : Q T N) :
    ∀ M, N ≤ M → ext T hε N (c • φ) M = c • ext T hε N φ M :=
  agree T hε (ext_compat T hε _) (fun M hM => by
      show capQ T hε M (c • ext T hε N φ M) = c • ext T hε N φ (M + 1 + 1)
      rw [capQ_smul, ext_succ_succ T hε φ hM])
    (by show _ = _ • _; rw [ext_self, ext_self])
    (by show _ = _ • _; rw [ext_succ, ext_succ, smul_zero])

variable (T hε) in
/-- The extension of a level morphism, as a glued sequence. -/
noncomputable def extSeq {N a b : ℕ} (φ : Q T N) (hφ : φ ∈ HomSp T N a b) (ha : a ≤ N)
    (hb : b ≤ N) : Seq T hε a b :=
  ⟨ext T hε N φ, N, fun M hM => ⟨ext_mem T hε hφ ha hb M hM, ext_compat T hε φ M hM⟩⟩

variable (T hε) in
/-- **The leg at level `N`.** -/
noncomputable def leg (N : ℕ) : LObj T hε N ⥤ GObj T hε where
  obj X := ⟨X.a⟩
  map {X Y} f := (⟪extSeq T hε (lval f) (lval_mem f) X.le Y.le⟫ : GHom T hε X.a Y.a)
  map_id X := by
    rw [id_def, mk_eq_iff]
    refine ⟨N, agree T hε (ext_compat T hε _)
      (fun M hM => capQ_PQ T hε (by have := X.le; show X.a ≠ M + 1 + 1; omega))
      (ext_self T hε N _) ?_⟩
    show ext T hε N (PQ T X.a N) (N + 1) = PQ T X.a (N + 1)
    rw [ext_succ, PQ_eq_zero_of_parity T (by have := X.par; omega)]
  map_comp {X Y Z} f g := by
    rw [comp_def, compH_mk, mk_eq_iff]
    exact ⟨N, ext_mul_ev T hε (lval f) (lval g)⟩

theorem leg_map {N : ℕ} {X Y : LObj T hε N} (f : X ⟶ Y) :
    (leg T hε N).map f = (⟪extSeq T hε (lval f) (lval_mem f) X.le Y.le⟫ : GHom T hε X.a Y.a) :=
  rfl

/-- Every object of the glued category is in the image of a leg. -/
theorem leg_obj (X : GObj T hε) : (leg T hε X.a).obj ⟨X.a, le_rfl, rfl⟩ = X := rfl

variable (T hε) in
theorem ext_inj {N : ℕ} {φ ψ : Q T N} :
    ∀ k, ext T hε N φ (N + 2 * k) = ext T hε N ψ (N + 2 * k) → φ = ψ
  | 0, h => by
    rw [show N + 2 * 0 = N by omega, ext_self, ext_self] at h
    exact h
  | k + 1, h => by
    rw [show N + 2 * (k + 1) = N + 2 * k + 1 + 1 by omega, ext_succ_succ T hε φ (by omega),
      ext_succ_succ T hε ψ (by omega)] at h
    exact ext_inj k (capQ_injective T hε _ h)

variable (T hε) in
/-- Every element of a higher level `N + 2k` comes from level `N`. -/
theorem descend {N a b : ℕ} (ha : a ≤ N) (hb : b ≤ N) :
    ∀ k (ψ : Q T (N + 2 * k)), ψ ∈ HomSp T (N + 2 * k) a b →
      ∃ φ ∈ HomSp T N a b, ext T hε N φ (N + 2 * k) = ψ
  | 0, ψ, hψ => ⟨ψ, hψ, ext_self T hε N ψ⟩
  | k + 1, ψ, hψ => by
    obtain ⟨φ', hφ', hφ'ψ⟩ := capQ_surj T hε (N := N + 2 * k) (by omega) (by omega)
      (show ψ ∈ HomSp T (N + 2 * k + 1 + 1) a b from hψ)
    obtain ⟨φ, hφ, hφφ'⟩ := descend ha hb k φ' hφ'
    refine ⟨φ, hφ, ?_⟩
    show ext T hε N φ (N + 2 * k + 1 + 1) = ψ
    rw [ext_succ_succ T hε φ (by omega), hφφ', hφ'ψ]

/-- **The legs are faithful.** -/
instance leg_faithful (N : ℕ) : (leg T hε N).Faithful where
  map_injective {X Y} {f g} h := by
    rw [leg_map, leg_map, mk_eq_iff] at h
    obtain ⟨M0, hM⟩ := h
    exact lhom_ext (ext_inj T hε M0 (hM (N + 2 * M0) (by omega)))

/-- **The legs are full.** -/
instance leg_full (N : ℕ) : (leg T hε N).Full where
  map_surjective {X Y} g := by
    obtain ⟨s, rfl⟩ := Submodule.Quotient.mk_surjective _ (show GHom T hε X.a Y.a from g)
    obtain ⟨N0, hs⟩ := compat_of_mem s
    obtain ⟨φ, hφ, hφs⟩ := descend T hε X.le Y.le N0 _ (hs (N + 2 * N0) (by omega)).1
    refine ⟨lmk φ hφ, ?_⟩
    rw [leg_map, mk_eq_iff]
    refine ⟨N + 2 * N0, agree T hε (fun M hM => ext_compat T hε φ M (by omega))
      (fun M hM => (hs M (by omega)).2) hφs ?_⟩
    show ext T hε N φ (N + 2 * N0 + 1) = s.1 (N + 2 * N0 + 1)
    rw [ext_parity, eq_zero_of_mem_parity T (hs _ (by omega)).1
      (Or.inl (by have := X.par; omega))]

variable (T hε) in
/-- **Adding two strands**, on the objects of the right parity. -/
noncomputable def stabL (N : ℕ) : LObj T hε N ⥤ LObj T hε (N + 1 + 1) where
  obj X := ⟨X.a, by have := X.le; omega, by have := X.par; omega⟩
  map {X Y} f := lmk (capQ T hε N (lval f)) (capQ_mem T hε X.le Y.le (lval_mem f))
  map_id X := lhom_ext (capQ_PQ T hε (by have := X.le; omega))
  map_comp f g := lhom_ext (capQ_mul T hε N (lval g) (lval f))

/-- **The legs form a cocone**: adding two strands and then gluing is gluing. -/
theorem stabL_comp_leg (N : ℕ) : stabL T hε N ⋙ leg T hε (N + 1 + 1) = leg T hε N := by
  refine CategoryTheory.Functor.ext (fun X => rfl) (fun X Y f => ?_)
  simp only [eqToHom_refl, Category.id_comp, Category.comp_id, Functor.comp_map]
  rw [leg_map, leg_map, mk_eq_iff]
  refine ⟨N + 1 + 1, agree T hε (ext_compat T hε _)
    (fun M hM => ext_compat T hε _ M (by omega)) ?_ ?_⟩
  · show ext T hε (N + 1 + 1) (capQ T hε N (lval f)) (N + 1 + 1) = ext T hε N (lval f) (N + 1 + 1)
    rw [ext_self, ext_succ_succ T hε _ le_rfl, ext_self]
  · show ext T hε (N + 1 + 1) (capQ T hε N (lval f)) (N + 1 + 1 + 1) =
      ext T hε N (lval f) (N + 1 + 1 + 1)
    rw [ext_succ]
    exact (ext_parity T hε (lval f) 1).symm

/-! ## The endomorphism algebras -/

theorem mem_top (a : ℕ) (φ : Q T a) : φ ∈ HomSp T a a a := by
  rw [mem_Hom]
  show ((P δ a a : TLFin K δ a) : Q T a) * φ * ((P δ a a : TLFin K δ a) : Q T a) = φ
  rw [P_self, RingCon.coe_one, one_mul, mul_one]

variable (T hε) in
/-- The top object `[a]` at level `a`. -/
def top (a : ℕ) : LObj T hε a := ⟨a, le_rfl, rfl⟩

variable (T hε) in
/-- An element of `Q a` as an endomorphism of `[a]` in the glued category. -/
noncomputable def toEnd (a : ℕ) (φ : Q T a) : End (GObj.mk a : GObj T hε) :=
  (leg T hε a).map (X := top T hε a) (Y := top T hε a) (lmk φ (mem_top a φ))

variable (T hε) in
noncomputable def toEndL (a : ℕ) : Q T a →ₗ[K] End (GObj.mk a : GObj T hε) where
  toFun := toEnd T hε a
  map_add' x y := by
    show (⟪_⟫ : GHom T hε a a) = (⟪_⟫ : GHom T hε a a) + ⟪_⟫
    rw [← Submodule.Quotient.mk_add, mk_eq_iff]
    exact ⟨a, ext_add_ev T hε x y⟩
  map_smul' c x := by
    show (⟪_⟫ : GHom T hε a a) = c • (⟪_⟫ : GHom T hε a a)
    rw [← Submodule.Quotient.mk_smul, mk_eq_iff]
    exact ⟨a, ext_smul_ev T hε c x⟩

variable (T hε) in
noncomputable def toEndAlg (a : ℕ) : Q T a →ₐ[K] End (GObj.mk a : GObj T hε) :=
  AlgHom.ofLinearMap (toEndL T hε a)
    (by
      show (leg T hε a).map _ = 𝟙 _
      rw [show lmk (X := top T hε a) (Y := top T hε a) 1 (mem_top a 1) = 𝟙 (top T hε a) from
        lhom_ext (by
          show (1 : Q T a) = ((P δ a a : TLFin K δ a) : Q T a)
          rw [P_self, RingCon.coe_one]), CategoryTheory.Functor.map_id])
    (fun x y => by
      show (leg T hε a).map _ = (leg T hε a).map _ ≫ (leg T hε a).map _
      rw [← CategoryTheory.Functor.map_comp]
      rfl)

variable (T hε) in
/-- **`End [a]` in the glued category is the quotient algebra on `a + 1` strands.** -/
noncomputable def endEquiv (a : ℕ) : Q T a ≃ₐ[K] End (GObj.mk a : GObj T hε) :=
  AlgEquiv.ofBijective (toEndAlg T hε a)
    ⟨fun x y h => by
      have h' : (leg T hε a).map (X := top T hε a) (Y := top T hε a) (lmk x (mem_top a x)) =
          (leg T hε a).map (X := top T hε a) (Y := top T hε a) (lmk y (mem_top a y)) := h
      exact congrArg lval ((leg T hε a).map_injective h'),
    fun e => by
      obtain ⟨f, hf⟩ := (leg T hε a).map_surjective (X := top T hε a) (Y := top T hε a) e
      exact ⟨lval f, hf⟩⟩

/-! ## Transport of simples along algebra isomorphisms -/

section Transport

variable {A B : Type*} [Ring A] [Ring B] [Algebra K A] [Algebra K B]

theorem isSimpleIdem_of_algEquiv (E : A ≃ₐ[K] B) {x : A} (h : IsSimpleIdem K (E x)) :
    IsSimpleIdem K x := by
  obtain ⟨h1, h2, h3⟩ := h
  refine ⟨E.injective (by rw [map_mul, h1]), fun hx => h2 (by rw [hx, map_zero]), fun y => ?_⟩
  obtain ⟨c, hc⟩ := h3 (E y)
  exact ⟨c, E.injective (by rw [map_mul, map_mul, map_smul, hc])⟩

theorem mvn_map (E : A ≃ₐ[K] B) {f g : A} (h : MvN f g) : MvN (E f) (E g) := by
  obtain ⟨hf, hg, u, v, hu, hv, huv, hvu⟩ := h
  exact ⟨by rw [← map_mul, hf], by rw [← map_mul, hg], E u, E v,
    by rw [← map_mul, ← map_mul, hu], by rw [← map_mul, ← map_mul, hv],
    by rw [← map_mul, huv], by rw [← map_mul, hvu]⟩

end Transport

/-! ## The trace -/

variable (T hε) in
/-- **The trace on `End [a]`** in the glued category. -/
noncomputable def trG (a : ℕ) (e : End (GObj.mk a : GObj T hε)) : K :=
  tauQ T a ((endEquiv T hε a).symm e)

theorem trG_endEquiv (a : ℕ) (φ : Q T a) : trG T hε a (endEquiv T hε a φ) = tauQ T a φ := by
  rw [trG, AlgEquiv.symm_apply_apply]

theorem trG_comm (a : ℕ) (e f : End (GObj.mk a : GObj T hε)) :
    trG T hε a (e * f) = trG T hε a (f * e) := by
  rw [trG, trG, map_mul, map_mul, tauQ_comm]

/-- **The trace form on every `End [a]` is nondegenerate.** -/
theorem trG_nondegenerate (a : ℕ) (e : End (GObj.mk a : GObj T hε))
    (h : ∀ f, trG T hε a (e * f) = 0) : e = 0 := by
  have h0 : (endEquiv T hε a).symm e = 0 := tauQ_nondegenerate T a _ fun ψ => by
    have := h (endEquiv T hε a ψ)
    rwa [trG, map_mul, AlgEquiv.symm_apply_apply] at this
  rw [← (endEquiv T hε a).apply_symm_apply e, h0, map_zero]

theorem tauQ_capQ (n : ℕ) (x : Q T n) :
    tauQ T (n + 1 + 1) (capQ T hε n x) = δ⁻¹ * (ε * tauQ T n x) := by
  obtain ⟨y, rfl⟩ := coe_surj T x
  rw [capQ_coe, tauQ_coe, tauQ_coe, tau_capEmb]

variable (T hε) in
/-- With the unnormalised weight `δ^{N+1}`, the trace of the extension is the same at every level
`N + 2k`. -/
theorem tauQ_ext {N : ℕ} (φ : Q T N) : ∀ k,
    δ ^ (N + 2 * k + 1) * tauQ T (N + 2 * k) (ext T hε N φ (N + 2 * k)) =
      δ ^ (N + 1) * tauQ T N φ
  | 0 => by rw [show N + 2 * 0 = N by omega, ext_self]
  | k + 1 => by
    have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
    have h1 : δ * δ⁻¹ = 1 := mul_inv_cancel₀ hδ
    rw [show N + 2 * (k + 1) = N + 2 * k + 1 + 1 by omega, ext_succ_succ T hε φ (by omega),
      tauQ_capQ, ← tauQ_ext φ k]
    set t := tauQ T (N + 2 * k) (ext T hε N φ (N + 2 * k))
    linear_combination (δ ^ (N + 2 * k + 1) * t * δ * ε) * h1 + (δ ^ (N + 2 * k + 1) * t) * hε

/-- **The glued trace does not depend on the level used to compute it.** For `φ ∈ Q a`, the
weighted trace `δ^{N+1} τ_N` of its image at any level `N = a + 2k` is `δ^{a+1} trG`. -/
theorem trG_level (a : ℕ) (φ : Q T a) (k : ℕ) :
    δ ^ (a + 2 * k + 1) * tauQ T (a + 2 * k) (ext T hε a φ (a + 2 * k)) =
      δ ^ (a + 1) * trG T hε a (endEquiv T hε a φ) := by
  rw [trG_endEquiv, tauQ_ext]

/-! ## The braiding -/

section Braiding

variable {A : K} (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

variable (T hε A) in
/-- The crossing `σᵢ` as an endomorphism of `[n]` in the glued category. -/
noncomputable def crossingG {n : ℕ} (i : Fin n) : End (GObj.mk n : GObj T hε) :=
  endEquiv T hε n (crossingQ A T i)

variable (T hε A) in
/-- The inverse crossing in the glued category. -/
noncomputable def crossingInvG {n : ℕ} (i : Fin n) : End (GObj.mk n : GObj T hε) :=
  endEquiv T hε n (crossingInvQ A T i)

include hA hδ in
theorem crossingG_mul_inv {n : ℕ} (i : Fin n) :
    crossingG T hε A i * crossingInvG T hε A i = 1 := by
  rw [crossingG, crossingInvG, ← map_mul, crossingQ_mul_inv T hA hδ, map_one]

include hA hδ in
theorem crossingInvG_mul {n : ℕ} (i : Fin n) :
    crossingInvG T hε A i * crossingG T hε A i = 1 := by
  rw [crossingG, crossingInvG, ← map_mul, crossingInvQ_mul T hA hδ, map_one]

include hA hδ in
/-- **The braid relation in the glued category.** -/
theorem crossingG_braid {n : ℕ} {i j : Fin n} (h : i.val + 1 = j.val ∨ j.val + 1 = i.val) :
    crossingG T hε A i * crossingG T hε A j * crossingG T hε A i =
      crossingG T hε A j * crossingG T hε A i * crossingG T hε A j := by
  simp only [crossingG, ← map_mul, crossingQ_braid T hA hδ h]

theorem crossingG_commute {n : ℕ} {i j : Fin n}
    (h : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val)) :
    crossingG T hε A i * crossingG T hε A j = crossingG T hε A j * crossingG T hε A i := by
  simp only [crossingG, ← map_mul, crossingQ_commute T h]

/-- **The twist in the glued category.** The full twist acts on the image of `p_n` by
`A^{n(n+1)}`. -/
theorem jw_mul_fullTwistG {n : ℕ} (hS : JWSpec δ n) :
    endEquiv T hε n (jw δ n : Q T n) * endEquiv T hε n (fullTwist δ A n : Q T n) =
      A ^ (n * (n + 1)) • endEquiv T hε n (jw δ n : Q T n) := by
  rw [← map_mul, jw_mul_fullTwistQ T hS, map_smul]

/-- **Every Hopf-link entry is a glued trace.** -/
theorem cH_eq_trG (n m : ℕ) :
    cH A T n m = trG T hε (n + m + 1) (endEquiv T hε (n + m + 1)
      ((wB δ n m * cable δ A n (m + 1) : TLFin K δ (n + m + 1)) : Q T (n + m + 1))) := by
  rw [trG_endEquiv, cH_eq_tauQ]

end Braiding

end Glue

/-! ## Modular data of the glued category -/

section Modular

variable {K : Type*} [Field K]

/-- **Modular data of the glued semisimplified Temperley–Lieb category at a root of unity.**
With `ζ = ω²` a primitive `2(k+2)`-th root and `δ = ζ + ζ⁻¹`:
1. every simple idempotent of every `End [a]` of the glued category is isomorphic to the image of
   the vacuum or some `p_m`, `m < k`, with cups, and that image is nonzero;
2. the braid `S`-matrix on these `k + 1` simples, whose entries are glued traces (`cH_eq_trG`),
   is `[(i+1)(j+1)]`;
3. it is invertible. -/
theorem modular_data_glued (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2)))
    {ε : K} (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) :
    (∀ (a : ℕ) (e : End (GObj.mk a : GObj T hε)), IsSimpleIdem K e →
      ∃ s, StdLt (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) k a s ∧
        MvN e (endEquiv T hε a (s : Q T a)) ∧ endEquiv T hε a (s : Q T a) ≠ 0) ∧
    braidS (ω : K) T k = sMatrix (ω ^ 2) k ∧
    (braidS (ω : K) T k).det ≠ 0 := by
  refine ⟨fun a e he => ?_, braidS_eq_sMatrix ω k hζ T hε, braidS_det_ne_zero ω k hζ T hε⟩
  set E := endEquiv T hε a
  have hφ : IsSimpleIdem K (E.symm e) :=
    isSimpleIdem_of_algEquiv E (by rwa [AlgEquiv.apply_symm_apply])
  obtain ⟨s, hs, hmvn, hne⟩ := simple_mvn_stdLt_root k hζ T hε a _ hφ
  refine ⟨s, hs, ?_, fun h => hne (E.injective (by rw [h, map_zero]))⟩
  have := mvn_map E hmvn
  rwa [AlgEquiv.apply_symm_apply] at this

end Modular

end QOU.HeckeTemperleyLieb.TLGlued
