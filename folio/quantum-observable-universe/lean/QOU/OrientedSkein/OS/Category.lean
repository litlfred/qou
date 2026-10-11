/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Syntax
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.BilinearMap

/-!
# `QOU.OrientedSkein.OS.Category` — the oriented skein category as an `R`-linear category

Stage 3b of the formalisation of the oriented skein category `OS(z, t)` (issue #7703).

Using the syntax of `QOU.OrientedSkein.OS.Syntax`, the hom-module `x ⟶ y` of `OS` is the
`R`-module of formal linear combinations of valid strings of layers from `x` to `y`
(`supp R x y ⊆ PA R`), modulo the submodule `rels x y` spanned by all *sandwiches*

  `π · whiskA a b (ρ.lhs - ρ.rhs) · π'`

of a defining relation `ρ`, whiskered by arbitrary words `a, b` and pre- and post-composed with
arbitrary valid strings `π, π'`.  Composition is multiplication in the path algebra, which is
concatenation of strings, so associativity and bilinearity are inherited from the ring structure
of `PA R = MonoidAlgebra R (FreeMonoid Step)`.

The span is closed under composition on either side (`mul_mem_rels_left/right`) and under
whiskering (`whiskA_mem_rels`), which is what makes composition and the monoidal structure (next
file) descend to the quotient.

## Main definitions

* `rels q qi t δ x y` — the relations between `x` and `y`.
* `HomQ q qi t δ x y` — the hom-module `supp R x y ⧸ rels`.
* `OSCat q qi t δ` — the oriented skein category: objects are words, with `Category`,
  `Preadditive` and `Linear R` instances.

Sorry-free.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory

noncomputable section

variable {R : Type*} [CommRing R]

/-! ## Elements of `supp` -/

theorem pth_toList (m : FreeMonoid Step) : (pth m.toList : PA R) = Finsupp.single m 1 := rfl

theorem single_eq_smul_pth (m : FreeMonoid Step) (c : R) :
    (Finsupp.single m c : PA R) = c • pth m.toList := by
  rw [pth_toList, Finsupp.smul_single, smul_eq_mul, mul_one]

/-- Induction principle for `supp R x y`: it is spanned by the valid strings. -/
theorem supp_induction {x y : Word} {P : PA R → Prop} (h0 : P 0)
    (hadd : ∀ f g, P f → P g → P (f + g)) (hsmul : ∀ (c : R) f, P f → P (c • f))
    (hp : ∀ π, Valid x π y → P (pth π)) {f : PA R} (hf : f ∈ supp R x y) : P f := by
  rw [supp, Finsupp.mem_supported] at hf
  rw [← Finsupp.sum_single f, Finsupp.sum]
  refine Finset.sum_induction _ P hadd h0 fun m hm => ?_
  rw [single_eq_smul_pth]
  exact hsmul _ _ (hp _ (hf hm))

theorem one_mem_supp {x y : Word} (h : x = y) : (1 : PA R) ∈ supp R x y :=
  pth_mem_supp (R := R) (π := []) h

theorem mul_mem_supp {x y z : Word} {f g : PA R} (hf : f ∈ supp R x y) (hg : g ∈ supp R y z) :
    f * g ∈ supp R x z := by
  refine supp_induction (P := fun f => f * g ∈ supp R x z) (by simp) (fun f f' h h' => ?_)
    (fun c f h => ?_) (fun π hπ => ?_) hf
  · beta_reduce at *; rw [add_mul]; exact Submodule.add_mem _ h h'
  · beta_reduce at *; rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ h
  refine supp_induction (P := fun g => pth π * g ∈ supp R x z) (by simp) (fun g g' h h' => ?_)
    (fun c g h => ?_) (fun π' hπ' => ?_) hg
  · beta_reduce at *; rw [mul_add]; exact Submodule.add_mem _ h h'
  · beta_reduce at *; rw [mul_smul_comm]; exact Submodule.smul_mem _ _ h
  show pth π * pth π' ∈ _
  rw [pth_mul]
  exact pth_mem_supp (hπ.append hπ')

/-- `supp` only depends on the words up to equality; a form convenient when the words are given
by different but equal expressions. -/
theorem whiskA_mem_supp' (a b : Word) {x y x' y' : Word} (hx : x' = a ++ (x ++ b))
    (hy : y' = a ++ (y ++ b)) {f : PA R} (hf : f ∈ supp R x y) : whiskA a b f ∈ supp R x' y' := by
  subst hx hy; exact whiskA_mem_supp a b hf

/-! ## The relations -/

variable (q qi t δ : R)

/-- The **sandwiches** of the defining relations: `π · whiskA a b ρ.rel · π'` for valid strings
`π : x → a ρ.src b` and `π' : a ρ.tgt b → y`. -/
def sandwiches (x y : Word) : Set (PA R) :=
  {f | ∃ (ρ : Rel) (a b : Word) (π π' : List Step), Valid x π (a ++ (ρ.src ++ b)) ∧
    Valid (a ++ (ρ.tgt ++ b)) π' y ∧ f = pth π * whiskA a b (ρ.rel q qi t δ) * pth π'}

/-- The submodule of relations between `x` and `y`. -/
def rels (x y : Word) : Submodule R (PA R) := Submodule.span R (sandwiches q qi t δ x y)

variable {q qi t δ}

theorem rels_le_supp (x y : Word) : rels q qi t δ x y ≤ supp R x y := by
  refine Submodule.span_le.mpr ?_
  rintro _ ⟨ρ, a, b, π, π', h, h', rfl⟩
  exact mul_mem_supp (mul_mem_supp (pth_mem_supp h) (whiskA_mem_supp a b (ρ.rel_mem q qi t δ)))
    (pth_mem_supp h')

theorem mul_mem_rels_left {x y z : Word} {f g : PA R} (hf : f ∈ rels q qi t δ x y)
    (hg : g ∈ supp R y z) : f * g ∈ rels q qi t δ x z := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
      obtain ⟨ρ, a, b, π, π', h, h', rfl⟩ := hf
      refine supp_induction (P := fun g => pth π * whiskA a b (ρ.rel q qi t δ) * pth π' * g ∈
        rels q qi t δ x z) (by simp) (fun g g' hg hg' => ?_) (fun c g hg => ?_)
        (fun π'' h'' => ?_) hg
      · beta_reduce at *; rw [mul_add]; exact Submodule.add_mem _ hg hg'
      · beta_reduce at *; rw [mul_smul_comm]; exact Submodule.smul_mem _ _ hg
      · beta_reduce at *; rw [mul_assoc, pth_mul]
        exact Submodule.subset_span ⟨ρ, a, b, π, π' ++ π'', h, h'.append h'', rfl⟩
  | zero => simp
  | add f f' _ _ h h' => rw [add_mul]; exact Submodule.add_mem _ h h'
  | smul c f _ h => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ h

theorem mul_mem_rels_right {x y z : Word} {f g : PA R} (hf : f ∈ supp R x y)
    (hg : g ∈ rels q qi t δ y z) : f * g ∈ rels q qi t δ x z := by
  induction hg using Submodule.span_induction with
  | mem g hg =>
      obtain ⟨ρ, a, b, π, π', h, h', rfl⟩ := hg
      refine supp_induction (P := fun f => f * (pth π * whiskA a b (ρ.rel q qi t δ) * pth π') ∈
        rels q qi t δ x z) (by simp) (fun f f' hf hf' => ?_) (fun c f hf => ?_)
        (fun π'' h'' => ?_) hf
      · beta_reduce at *; rw [add_mul]; exact Submodule.add_mem _ hf hf'
      · beta_reduce at *; rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ hf
      · beta_reduce at *; rw [← mul_assoc, ← mul_assoc, pth_mul]
        exact Submodule.subset_span ⟨ρ, a, b, π'' ++ π, π', h''.append h, h', rfl⟩
  | zero => simp
  | add g g' _ _ h h' => rw [mul_add]; exact Submodule.add_mem _ h h'
  | smul c g _ h => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ h

theorem whiskA_mem_rels (c d : Word) {x y : Word} {f : PA R} (hf : f ∈ rels q qi t δ x y) :
    whiskA c d f ∈ rels q qi t δ (c ++ (x ++ d)) (c ++ (y ++ d)) := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
      obtain ⟨ρ, a, b, π, π', h, h', rfl⟩ := hf
      refine Submodule.subset_span ⟨ρ, c ++ a, b ++ d, π.map (Step.whisk c d),
        π'.map (Step.whisk c d), by simpa using h.whisk c d, by simpa using h'.whisk c d, ?_⟩
      rw [whiskA_mul, whiskA_mul, whiskA_pth, whiskA_pth, whiskA_whiskA]
  | zero => simp
  | add f f' _ _ h h' => rw [map_add]; exact Submodule.add_mem _ h h'
  | smul r f _ h => rw [map_smul]; exact Submodule.smul_mem _ _ h

theorem whiskA_mem_rels' (c d : Word) {x y x' y' : Word} (hx : x' = c ++ (x ++ d))
    (hy : y' = c ++ (y ++ d)) {f : PA R} (hf : f ∈ rels q qi t δ x y) :
    whiskA c d f ∈ rels q qi t δ x' y' := by
  subst hx hy; exact whiskA_mem_rels c d hf

/-- A defining relation, whiskered, lies in the relations. -/
theorem whiskA_rel_mem_rels (ρ : Rel) (a b : Word) {x y : Word} (hx : x = a ++ (ρ.src ++ b))
    (hy : y = a ++ (ρ.tgt ++ b)) : whiskA a b (ρ.rel q qi t δ) ∈ rels q qi t δ x y :=
  Submodule.subset_span ⟨ρ, a, b, [], [], hx, hy.symm, by rw [pth_nil, one_mul, mul_one]⟩

/-! ## The hom-modules -/

variable (q qi t δ)

/-- The relations, as a submodule of `supp R x y`. -/
def relsIn (x y : Word) : Submodule R (supp R x y) :=
  (rels q qi t δ x y).comap (supp R x y).subtype

/-- The **hom-module** `x ⟶ y` of the oriented skein category. -/
abbrev HomQ (x y : Word) := supp R x y ⧸ relsIn q qi t δ x y

variable {q qi t δ}

/-- The class of a valid linear combination of strings. -/
def mk {x y : Word} (f : PA R) (hf : f ∈ supp R x y) : HomQ q qi t δ x y :=
  Submodule.Quotient.mk ⟨f, hf⟩

theorem mk_surjective {x y : Word} (g : HomQ q qi t δ x y) :
    ∃ (f : PA R) (hf : f ∈ supp R x y), mk f hf = g := by
  obtain ⟨⟨f, hf⟩, rfl⟩ := Submodule.Quotient.mk_surjective _ g
  exact ⟨f, hf, rfl⟩

theorem mk_eq_mk {x y : Word} {f g : PA R} (hf : f ∈ supp R x y) (hg : g ∈ supp R x y) :
    (mk f hf : HomQ q qi t δ x y) = mk g hg ↔ f - g ∈ rels q qi t δ x y :=
  Submodule.Quotient.eq _

theorem mk_eq_mk_of_sub_mem {x y : Word} {f g : PA R} (hf : f ∈ supp R x y)
    (hg : g ∈ supp R x y) (h : f - g ∈ rels q qi t δ x y) :
    (mk f hf : HomQ q qi t δ x y) = mk g hg :=
  (mk_eq_mk hf hg).mpr h

theorem mk_add {x y : Word} {f g : PA R} (hf : f ∈ supp R x y) (hg : g ∈ supp R x y) :
    (mk (f + g) (Submodule.add_mem _ hf hg) : HomQ q qi t δ x y) = mk f hf + mk g hg := rfl

theorem mk_smul {x y : Word} (c : R) {f : PA R} (hf : f ∈ supp R x y) :
    (mk (c • f) (Submodule.smul_mem _ c hf) : HomQ q qi t δ x y) = c • mk f hf := rfl

theorem mk_zero {x y : Word} : (mk 0 (Submodule.zero_mem _) : HomQ q qi t δ x y) = 0 := rfl

/-- Changing the proof of membership, or the words up to equality, does not change `mk`. -/
theorem mk_congr {x y : Word} {f g : PA R} (hfg : f = g) (hf : f ∈ supp R x y)
    (hg : g ∈ supp R x y) : (mk f hf : HomQ q qi t δ x y) = mk g hg := by
  subst hfg; rfl

/-! ## Composition -/

/-- Multiplication `supp x y × supp y z → supp x z`, as a bilinear map. -/
def mulS (x y z : Word) : supp R x y →ₗ[R] supp R y z →ₗ[R] supp R x z :=
  LinearMap.mk₂ R (fun f g => ⟨f.1 * g.1, mul_mem_supp f.2 g.2⟩)
    (fun _ _ _ => Subtype.ext (add_mul _ _ _))
    (fun _ _ _ => Subtype.ext (smul_mul_assoc _ _ _))
    (fun _ _ _ => Subtype.ext (mul_add _ _ _))
    (fun _ _ _ => Subtype.ext (mul_smul_comm _ _ _))

variable (q qi t δ) in
/-- **Composition** of the oriented skein category, as a bilinear map of hom-modules. -/
def compQ (x y z : Word) : HomQ q qi t δ x y →ₗ[R] HomQ q qi t δ y z →ₗ[R] HomQ q qi t δ x z :=
  (relsIn q qi t δ x y).liftQ
    (((relsIn q qi t δ y z).liftQ ((mulS x y z).compr₂ (relsIn q qi t δ x z).mkQ).flip
      (fun g hg => LinearMap.ext fun f => (Submodule.Quotient.mk_eq_zero _).mpr
        (mul_mem_rels_right f.2 hg))).flip)
    (fun f hf => LinearMap.ext fun g => by
      obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ g
      exact (Submodule.Quotient.mk_eq_zero _).mpr (mul_mem_rels_left hf g.2))

theorem compQ_mk {x y z : Word} {f g : PA R} (hf : f ∈ supp R x y) (hg : g ∈ supp R y z) :
    compQ q qi t δ x y z (mk f hf) (mk g hg) = mk (f * g) (mul_mem_supp hf hg) := rfl

/-! ## The category -/

/-- The **oriented skein category** `OS(z, t)` (with `z = q - qi`, and `δ` standing for
`(t - t⁻¹)/z`): its objects are words in `E` and `F`. -/
@[ext]
structure OSCat (q qi t δ : R) : Type where
  /-- The underlying word. -/
  w : Word

instance : Category (OSCat q qi t δ) where
  Hom X Y := HomQ q qi t δ X.w Y.w
  id X := mk 1 (one_mem_supp rfl)
  comp {X Y Z} f g := compQ q qi t δ X.w Y.w Z.w f g
  id_comp {X Y} f := by
    obtain ⟨f, hf, rfl⟩ := mk_surjective f
    exact (compQ_mk _ _).trans (mk_congr (one_mul f) _ _)
  comp_id {X Y} f := by
    obtain ⟨f, hf, rfl⟩ := mk_surjective f
    exact (compQ_mk _ _).trans (mk_congr (mul_one f) _ _)
  assoc {W X Y Z} f g h := by
    obtain ⟨f, hf, rfl⟩ := mk_surjective f
    obtain ⟨g, hg, rfl⟩ := mk_surjective g
    obtain ⟨h, hh, rfl⟩ := mk_surjective h
    exact mk_congr (mul_assoc f g h) _ _

/-- A morphism of `OS` from a valid linear combination of strings. -/
abbrev homMk {X Y : OSCat q qi t δ} (f : PA R) (hf : f ∈ supp R X.w Y.w) : X ⟶ Y := mk f hf

theorem homMk_surjective {X Y : OSCat q qi t δ} (g : X ⟶ Y) :
    ∃ (f : PA R) (hf : f ∈ supp R X.w Y.w), homMk f hf = g :=
  mk_surjective g

@[simp] theorem homMk_comp {X Y Z : OSCat q qi t δ} {f g : PA R} (hf : f ∈ supp R X.w Y.w)
    (hg : g ∈ supp R Y.w Z.w) :
    (homMk f hf : X ⟶ Y) ≫ (homMk g hg : Y ⟶ Z) = homMk (f * g) (mul_mem_supp hf hg) := rfl

theorem id_eq_homMk (X : OSCat q qi t δ) : 𝟙 X = homMk 1 (one_mem_supp rfl) := rfl

instance : Preadditive (OSCat q qi t δ) where
  homGroup X Y := inferInstanceAs (AddCommGroup (HomQ q qi t δ X.w Y.w))
  add_comp {X Y Z} f f' g := LinearMap.map_add₂ (compQ q qi t δ X.w Y.w Z.w) f f' g
  comp_add {X Y Z} f g g' := (compQ q qi t δ X.w Y.w Z.w f).map_add g g'

instance : Linear R (OSCat q qi t δ) where
  homModule X Y := inferInstanceAs (Module R (HomQ q qi t δ X.w Y.w))
  smul_comp {X Y Z} c f g := LinearMap.map_smul₂ (compQ q qi t δ X.w Y.w Z.w) c f g
  comp_smul {X Y Z} f c g := (compQ q qi t δ X.w Y.w Z.w f).map_smul c g

theorem homMk_add {X Y : OSCat q qi t δ} {f g : PA R} (hf : f ∈ supp R X.w Y.w)
    (hg : g ∈ supp R X.w Y.w) :
    (homMk (f + g) (Submodule.add_mem _ hf hg) : X ⟶ Y) = homMk f hf + homMk g hg := rfl

theorem homMk_smul {X Y : OSCat q qi t δ} (c : R) {f : PA R} (hf : f ∈ supp R X.w Y.w) :
    (homMk (c • f) (Submodule.smul_mem _ c hf) : X ⟶ Y) = c • homMk f hf := rfl

theorem homMk_sub {X Y : OSCat q qi t δ} {f g : PA R} (hf : f ∈ supp R X.w Y.w)
    (hg : g ∈ supp R X.w Y.w) :
    (homMk (f - g) (Submodule.sub_mem _ hf hg) : X ⟶ Y) = homMk f hf - homMk g hg := rfl

/-- Two morphisms are equal when their representatives differ by a relation. -/
theorem homMk_eq_homMk {X Y : OSCat q qi t δ} {f g : PA R} (hf : f ∈ supp R X.w Y.w)
    (hg : g ∈ supp R X.w Y.w) (h : f - g ∈ rels q qi t δ X.w Y.w) :
    (homMk f hf : X ⟶ Y) = homMk g hg :=
  mk_eq_mk_of_sub_mem hf hg h

end

end QOU.OrientedSkein.OS
