/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Syntax
import QOU.OrientedSkein.SkeinDatum

/-!
# `QOU.OrientedSkein.OS.Interpret` — interpreting the syntax of `OS(z, t)` in a skein datum

Stage 3b of the formalisation of the oriented skein category `OS(z, t)` (issue #7703).

Given an `R`-linear monoidal category `𝒞` (not assumed strict; associators and unitors are
explicit) carrying oriented skein data `D : OrientedSkeinDatum q qi t δ E F`, this file interprets
the syntax of `QOU.OrientedSkein.OS.Syntax` in `𝒞`:

* a word `w` goes to the right-nested tensor product `obj w` of its letters (`true ↦ E`,
  `false ↦ F`, `[] ↦ 𝟙_`);
* a generator goes to `S`, `T`, the cup `η_ F E` or the cap `ε_ F E` (`genHom`), a layer
  `⟨l, g, r⟩` to the generator whiskered by `obj l` and `obj r` through the canonical isomorphisms
  `μ a b : obj (a ++ b) ≅ obj a ⊗ obj b` (`stepHom`), and a valid string of layers to the composite
  of its layers (`pathHom`);
* the path algebra goes `R`-linearly to the hom-modules (`interp x y : PA R →ₗ[R] (obj x ⟶ obj y)`),
  a basis element going to its path when it is valid from `x` to `y` and to `0` otherwise.

The interpretation is a functor on the hom-modules `supp R x y` (`interp_one`, `interp_mul`),
commutes with whiskering (`interp_whiskA`), and kills every defining relation of `OS(z, t)`
(`interp_rel`).  These are the facts needed to descend `interp` to the quotient category and so
obtain the functor `OS(z, t) ⥤ 𝒞` of Brundan's universal property.

## Main definitions

* `obj`, `μ` — words as objects, and the canonical isomorphisms `obj (a ++ b) ≅ obj a ⊗ obj b`.
* `wl`, `wr` — left and right whiskering of a morphism between words by a word, through `μ`.
* `genHom`, `stepHom`, `pathHom` — the images of generators, layers and valid strings.
* `interp` — the `R`-linear interpretation of the path algebra.

## Main statements

* `μ_assoc` — associativity of `μ`, the coherence fact everything else rests on.
* `interp_pth`, `interp_one`, `interp_mul` — `interp` is functorial on `supp R x y`.
* `interp_whiskA` — `interp` intertwines `whiskA a b` with whiskering by `obj a`, `obj b`.
* `interp_rel` — every defining relation `quad`, `braid`, `zigE`, `zigF`, `TS`, `ST`, `dim`,
  `ichg` of `OS(z, t)` is sent to `0`.

Sorry-free.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

universe v u

set_option linter.unusedSectionVars false

section Interp

variable {R : Type*} [CommRing R] {q qi t δ : R}
variable {𝒞 : Type u} [Category.{v} 𝒞] [Preadditive 𝒞] [Linear R 𝒞]
  [MonoidalCategory 𝒞] [MonoidalPreadditive 𝒞] [MonoidalLinear R 𝒞]
variable {E F : 𝒞} [ExactPairing F E]

variable (E F) in
/-- The object attached to an orientation: `true ↦ E`, `false ↦ F`. -/
def col : Bool → 𝒞
  | true => E
  | false => F

variable (E F) in
/-- The object attached to a word: the right-nested tensor product of its letters. -/
def obj : Word → 𝒞
  | [] => 𝟙_ 𝒞
  | b :: w => col E F b ⊗ obj w

@[simp] theorem obj_nil : obj E F [] = 𝟙_ 𝒞 := rfl
@[simp] theorem obj_cons (b : Bool) (w : Word) : obj E F (b :: w) = col E F b ⊗ obj E F w := rfl

variable (E F) in
/-- The canonical isomorphism `obj (a ++ b) ≅ obj a ⊗ obj b`. -/
def μ : (a b : Word) → (obj E F (a ++ b) ≅ obj E F a ⊗ obj E F b)
  | [], b => (λ_ (obj E F b)).symm
  | x :: a, b => whiskerLeftIso (col E F x) (μ a b) ≪≫ (α_ _ _ _).symm

/-- `μ [] b` is the inverse left unitor. -/
theorem μ_nil (b : Word) : μ E F [] b = (λ_ (obj E F b)).symm := rfl
/-- The recursion step of `μ`. -/
theorem μ_cons (x : Bool) (a b : Word) :
    μ E F (x :: a) b = whiskerLeftIso (col E F x) (μ E F a b) ≪≫ (α_ _ _ _).symm := rfl

/-- Transport along an equality of words under a leading letter. -/
theorem eqToHom_cons (x : Bool) {w w' : Word} (h : w = w')
    (h' : obj E F (x :: w) = obj E F (x :: w')) :
    eqToHom h' = col E F x ◁ eqToHom (congrArg (obj E F) h) := by
  subst h; simp

/-- Associativity of `μ`. -/
@[reassoc]
theorem μ_assoc (a b c : Word) :
    (μ E F a (b ++ c)).hom ≫ (obj E F a ◁ (μ E F b c).hom) =
      eqToHom (congrArg (obj E F) (List.append_assoc a b c).symm) ≫ (μ E F (a ++ b) c).hom ≫
        ((μ E F a b).hom ▷ obj E F c) ≫ (α_ _ _ _).hom := by
  induction a with
  | nil =>
      simp only [μ_nil, Iso.symm_hom, eqToHom_refl, Category.id_comp, List.nil_append]
      monoidal
  | cons x a ih =>
      rw [eqToHom_cons x (List.append_assoc a b c).symm]
      simp only [List.cons_append, μ_cons, Iso.trans_hom, whiskerLeftIso_hom, Iso.symm_hom, comp_whiskerRight,
        Category.assoc, obj_cons]
      rw [← associator_inv_naturality_right, ← whiskerLeft_comp_assoc, ih]
      simp only [whiskerLeft_comp, Category.assoc]
      congr 1
      monoidal


/-- Associativity of `μ`, inverse form. -/
@[reassoc]
theorem μ_assoc_inv (a b c : Word) :
    (obj E F a ◁ (μ E F b c).inv) ≫ (μ E F a (b ++ c)).inv =
      (α_ _ _ _).inv ≫ ((μ E F a b).inv ▷ obj E F c) ≫ (μ E F (a ++ b) c).inv ≫
        eqToHom (congrArg (obj E F) (List.append_assoc a b c)) := by
  rw [← cancel_epi ((μ E F a (b ++ c)).hom ≫ (obj E F a ◁ (μ E F b c).hom))]
  conv_rhs => rw [μ_assoc]
  simp

/-- Associativity of `μ`, rearranged. -/
@[reassoc]
theorem μ_assoc' (a b c : Word) :
    (μ E F (a ++ b) c).hom ≫ ((μ E F a b).hom ▷ obj E F c) =
      eqToHom (congrArg (obj E F) (List.append_assoc a b c)) ≫ (μ E F a (b ++ c)).hom ≫
        (obj E F a ◁ (μ E F b c).hom) ≫ (α_ _ _ _).inv := by
  rw [μ_assoc_assoc]; simp

/-- Associativity of `μ`, inverse form rearranged. -/
theorem μ_assoc_inv' (a b c : Word) :
    ((μ E F a b).inv ▷ obj E F c) ≫ (μ E F (a ++ b) c).inv =
      (α_ _ _ _).hom ≫ (obj E F a ◁ (μ E F b c).inv) ≫ (μ E F a (b ++ c)).inv ≫
        eqToHom (congrArg (obj E F) (List.append_assoc a b c).symm) := by
  rw [μ_assoc_inv_assoc]; simp

/-- `μ x []` is the inverse right unitor, up to `x ++ [] = x`. -/
theorem μ_nil_right (x : Word) :
    (μ E F x []).hom = eqToHom (congrArg (obj E F) (List.append_nil x)) ≫ (ρ_ (obj E F x)).inv := by
  induction x with
  | nil => simp [μ_nil, unitors_inv_equal]
  | cons b x ih =>
      rw [eqToHom_cons b (List.append_nil x)]
      simp only [List.cons_append, μ_cons, Iso.trans_hom, whiskerLeftIso_hom, Iso.symm_hom, ih,
        whiskerLeft_comp, Category.assoc, obj_cons]
      congr 1
      monoidal

/-- Inverse form of `μ_nil_right`. -/
theorem μ_nil_right_inv (x : Word) :
    (μ E F x []).inv = (ρ_ (obj E F x)).hom ≫ eqToHom (congrArg (obj E F) (List.append_nil x).symm) := by
  rw [← cancel_epi (μ E F x []).hom, Iso.hom_inv_id, μ_nil_right]
  simp

variable (E F) in
/-- Left whiskering of a morphism between words by a word `a`, through `μ`. -/
def wl (a : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) : obj E F (a ++ x) ⟶ obj E F (a ++ y) :=
  (μ E F a x).hom ≫ (obj E F a ◁ f) ≫ (μ E F a y).inv

variable (E F) in
/-- Right whiskering of a morphism between words by a word `b`, through `μ`. -/
def wr (b : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) : obj E F (x ++ b) ⟶ obj E F (y ++ b) :=
  (μ E F x b).hom ≫ (f ▷ obj E F b) ≫ (μ E F y b).inv

/-- `wl` preserves composition. -/
theorem wl_comp (a : Word) {x y z : Word} (f : obj E F x ⟶ obj E F y) (g : obj E F y ⟶ obj E F z) :
    wl E F a (f ≫ g) = wl E F a f ≫ wl E F a g := by simp [wl]

/-- `wr` preserves composition. -/
theorem wr_comp (b : Word) {x y z : Word} (f : obj E F x ⟶ obj E F y) (g : obj E F y ⟶ obj E F z) :
    wr E F b (f ≫ g) = wr E F b f ≫ wr E F b g := by simp [wr]

/-- `wl` preserves identities. -/
theorem wl_id (a x : Word) : wl E F a (𝟙 (obj E F x)) = 𝟙 _ := by simp [wl]

/-- `wr` preserves identities. -/
theorem wr_id (b x : Word) : wr E F b (𝟙 (obj E F x)) = 𝟙 _ := by simp [wr]

/-- `wl` of a transport is a transport. -/
theorem wl_eqToHom (a : Word) {x y : Word} (h : x = y) (h' : obj E F x = obj E F y) :
    wl E F a (eqToHom h') = eqToHom (congrArg (obj E F) (congrArg (a ++ ·) h)) := by
  subst h; simp [wl]

/-- `wr` of a transport is a transport. -/
theorem wr_eqToHom (b : Word) {x y : Word} (h : x = y) (h' : obj E F x = obj E F y) :
    wr E F b (eqToHom h') = eqToHom (congrArg (obj E F) (congrArg (· ++ b) h)) := by
  subst h; simp [wr]

/-- Whiskering by the empty word on the left does nothing. -/
theorem wl_nil {x y : Word} (f : obj E F x ⟶ obj E F y) : wl E F [] f = f := by
  simp [wl, μ_nil]

/-- Whiskering by the empty word on the right does nothing, up to `x ++ [] = x`. -/
theorem wr_nil {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wr E F [] f = eqToHom (congrArg (obj E F) (List.append_nil x)) ≫ f ≫
      eqToHom (congrArg (obj E F) (List.append_nil y).symm) := by
  simp [wr, μ_nil_right, μ_nil_right_inv]

/-- Iterated left whiskering. -/
theorem wl_wl (a c : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wl E F a (wl E F c f) = eqToHom (congrArg (obj E F) (List.append_assoc a c x).symm) ≫
      wl E F (a ++ c) f ≫ eqToHom (congrArg (obj E F) (List.append_assoc a c y)) := by
  simp only [wl, whiskerLeft_comp, Category.assoc]
  rw [μ_assoc_assoc, μ_assoc_inv, ← associator_naturality_right_assoc, Iso.hom_inv_id_assoc,
    ← whisker_exchange_assoc, hom_inv_whiskerRight_assoc]

/-- Iterated right whiskering. -/
theorem wr_wr (b d : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wr E F b (wr E F d f) = eqToHom (congrArg (obj E F) (List.append_assoc x d b)) ≫
      wr E F (d ++ b) f ≫ eqToHom (congrArg (obj E F) (List.append_assoc y d b).symm) := by
  simp only [wr, comp_whiskerRight, Category.assoc]
  rw [μ_assoc'_assoc, μ_assoc_inv', associator_naturality_left_assoc, Iso.inv_hom_id_assoc,
    whisker_exchange_assoc, whiskerLeft_hom_inv_assoc]

/-- Left and right whiskering commute. -/
theorem wr_wl (b c : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wr E F b (wl E F c f) = eqToHom (congrArg (obj E F) (List.append_assoc c x b)) ≫
      wl E F c (wr E F b f) ≫ eqToHom (congrArg (obj E F) (List.append_assoc c y b).symm) := by
  simp only [wr, wl, comp_whiskerRight, Category.assoc]
  rw [μ_assoc'_assoc, μ_assoc_inv', associator_naturality_middle_assoc, Iso.inv_hom_id_assoc]
  simp only [whiskerLeft_comp, Category.assoc]


/-- Iterated two-sided whiskering. -/
theorem wlr_wlr (a b c d : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wl E F a (wr E F b (wl E F c (wr E F d f))) =
      eqToHom (congrArg (obj E F) (by simp)) ≫ wl E F (a ++ c) (wr E F (d ++ b) f) ≫
        eqToHom (congrArg (obj E F) (by simp)) := by
  rw [wr_wl, wl_comp, wl_comp, wl_eqToHom _ (List.append_assoc c (x ++ d) b),
    wl_eqToHom _ (List.append_assoc c (y ++ d) b).symm, wl_wl, wr_wr, wl_comp, wl_comp,
    wl_eqToHom _ (List.append_assoc x d b), wl_eqToHom _ (List.append_assoc y d b).symm]
  simp


/-- Interchange: `f` and `f'` on disjoint strands commute. -/
theorem wr_wl_exchange {x y x' y' : Word} (f : obj E F x ⟶ obj E F y) (f' : obj E F x' ⟶ obj E F y') :
    wr E F x' f ≫ wl E F y f' = wl E F x f' ≫ wr E F y' f := by
  simp only [wr, wl, Category.assoc, Iso.inv_hom_id_assoc]
  rw [whisker_exchange_assoc]

variable (D : OrientedSkeinDatum q qi t δ E F)

/-- The image of a generator: `S`, `T`, the cup `η_ F E` and the cap `ε_ F E`, conjugated by the
right unitors `obj [x, y] = col x ⊗ (col y ⊗ 𝟙) ≅ col x ⊗ col y`. -/
def genHom : (g : Gen) → (obj E F g.src ⟶ obj E F g.tgt)
  | .S => (E ◁ (ρ_ E).hom) ≫ D.cross.S ≫ (E ◁ (ρ_ E).inv)
  | .T => (F ◁ (ρ_ E).hom) ≫ D.T ≫ (E ◁ (ρ_ F).inv)
  | .C => η_ F E ≫ (F ◁ (ρ_ E).inv)
  | .D => (E ◁ (ρ_ F).hom) ≫ ε_ F E

/-- The image of a layer `⟨l, g, r⟩`: the generator, whiskered by `l` and `r`. -/
def stepHom (s : Step) : obj E F s.src ⟶ obj E F s.tgt :=
  wl E F s.l (wr E F s.r (genHom D s.g))

/-- The image of a valid string of layers: the composite of its layers. -/
def pathHom : (π : List Step) → (x y : Word) → Valid x π y → (obj E F x ⟶ obj E F y)
  | [], _, _, h => eqToHom (congrArg (obj E F) h)
  | s :: π, _, y, h => eqToHom (congrArg (obj E F) h.1) ≫ stepHom D s ≫ pathHom π s.tgt y h.2

/-- `pathHom` of the empty string. -/
@[simp] theorem pathHom_nil (x y : Word) (h : Valid x [] y) :
    pathHom D [] x y h = eqToHom (congrArg (obj E F) h) := rfl

/-- `pathHom` of a nonempty string. -/
@[simp] theorem pathHom_cons (s : Step) (π : List Step) (x y : Word) (h : Valid x (s :: π) y) :
    pathHom D (s :: π) x y h =
      eqToHom (congrArg (obj E F) h.1) ≫ stepHom D s ≫ pathHom D π s.tgt y h.2 := rfl

/-- `pathHom` only depends on the words up to equality. -/
theorem pathHom_congr (π : List Step) {x x' y y' : Word} (hx : x = x') (hy : y = y')
    (h : Valid x π y) (h' : Valid x' π y') :
    pathHom D π x y h = eqToHom (congrArg (obj E F) hx) ≫ pathHom D π x' y' h' ≫
      eqToHom (congrArg (obj E F) hy.symm) := by
  subst hx hy; simp

/-- `pathHom` turns concatenation into composition. -/
theorem pathHom_append : ∀ (π π' : List Step) {x y z : Word} (h : Valid x (π ++ π') z)
    (h1 : Valid x π y) (h2 : Valid y π' z),
    pathHom D (π ++ π') x z h = pathHom D π x y h1 ≫ pathHom D π' y z h2
  | [], π', x, y, z, h, h1, h2 => by
      subst h1; simp
  | s :: π, π', x, y, z, h, h1, h2 => by
      simp only [List.cons_append, pathHom_cons, Category.assoc]
      rw [pathHom_append π π' h.2 h1.2 h2]

open Classical in
variable (E F) in
/-- The coefficient morphism of a basis element `m` of the path algebra, as a morphism
`obj x ⟶ obj y`: its path if it is valid from `x` to `y`, and `0` otherwise. -/
noncomputable def pathHom' (x y : Word) (m : FreeMonoid Step) : obj E F x ⟶ obj E F y :=
  if h : Valid x m.toList y then pathHom D m.toList x y h else 0

/-- **The interpretation** of the path algebra in `𝒞`, between the words `x` and `y`. -/
noncomputable def interp (x y : Word) : PA R →ₗ[R] (obj E F x ⟶ obj E F y) :=
  Finsupp.linearCombination R (pathHom' E F D x y)

/-- `interp` on a basis element. -/
theorem interp_single (x y : Word) (m : FreeMonoid Step) (r : R) :
    interp D x y (Finsupp.single m r) = r • pathHom' E F D x y m :=
  Finsupp.linearCombination_single R _ _

/-- `interp` of a valid string of layers is its path. -/
theorem interp_pth {x y : Word} {π : List Step} (h : Valid x π y) :
    interp D x y (pth π) = pathHom D π x y h := by
  simp [pth, interp_single, pathHom', h]

/-- `interp` vanishes on a basis element that is not valid from `x` to `y`. -/
theorem interp_single_of_not_valid {x y : Word} {m : FreeMonoid Step} (h : ¬ Valid x m.toList y)
    (r : R) : interp D x y (Finsupp.single m r) = 0 := by
  simp [interp_single, pathHom', h]

/-- `interp` preserves identities. -/
theorem interp_one (x : Word) : interp D x x 1 = 𝟙 _ := by
  rw [← pth_nil, interp_pth D (valid_refl x)]; simp

/-- Induction principle for `supp R x y`. -/
theorem supp_induction_single {x y : Word} {P : PA R → Prop} (h0 : P 0)
    (hadd : ∀ f g, P f → P g → P (f + g))
    (hs : ∀ m r, Valid x (FreeMonoid.toList m) y → P (Finsupp.single m r))
    {f : PA R} (hf : f ∈ supp R x y) : P f := by
  rw [← Finsupp.sum_single f]
  apply Finset.sum_induction _ P hadd h0
  intro m hm
  exact hs m _ ((Finsupp.mem_supported R f).1 hf hm)

/-- `interp` preserves composition on the hom-modules `supp R x y`. -/
theorem interp_mul {x y z : Word} {f g : PA R} (hf : f ∈ supp R x y) (hg : g ∈ supp R y z) :
    interp D x z (f * g) = interp D x y f ≫ interp D y z g := by
  refine supp_induction_single (P := fun f => interp D x z (f * g) = interp D x y f ≫ interp D y z g)
    (by simp) (fun f f' h h' => by simp [add_mul, h, h', Preadditive.add_comp]) ?_ hf
  intro m r hm
  refine supp_induction_single (P := fun g => interp D x z (MonoidAlgebra.single m r * g) =
      interp D x y (MonoidAlgebra.single m r) ≫ interp D y z g)
    (by simp) (fun g g' h h' => by simp [mul_add, h, h', Preadditive.comp_add]) ?_ hg
  intro m' r' hm'
  have hmm : Valid x (FreeMonoid.toList (m * m')) z := by
    rw [FreeMonoid.toList_mul]; exact hm.append hm'
  rw [MonoidAlgebra.single_mul_single, interp_single, interp_single, interp_single]
  simp only [pathHom', dif_pos hm, dif_pos hm', dif_pos hmm, Linear.smul_comp, Linear.comp_smul,
    smul_smul]
  rw [mul_comm r' r, ← pathHom_append D _ _ (by rwa [← FreeMonoid.toList_mul]) hm hm']
  rfl


/-- The image of a whiskered layer. -/
theorem stepHom_whisk (a b : Word) (s : Step) :
    stepHom D (s.whisk a b) = eqToHom (congrArg (obj E F) (Step.whisk_src a b s)) ≫
      wl E F a (wr E F b (stepHom D s)) ≫ eqToHom (congrArg (obj E F) (Step.whisk_tgt a b s).symm) := by
  simp only [stepHom, wlr_wlr]
  simp

/-- The image of a whiskered string of layers. -/
theorem pathHom_whisk (a b : Word) : ∀ (π : List Step) (x y : Word) (h : Valid x π y)
    (h' : Valid (a ++ (x ++ b)) (π.map (Step.whisk a b)) (a ++ (y ++ b))),
    pathHom D (π.map (Step.whisk a b)) _ _ h' = wl E F a (wr E F b (pathHom D π x y h))
  | [], x, y, h, h' => by
      subst h; simp [wl_id, wr_id]
  | s :: π, x, y, h, h' => by
      simp only [List.map_cons, pathHom_cons]
      rw [pathHom_congr D _ (Step.whisk_tgt a b s) rfl h'.2 (Valid.whisk a b h.2),
        pathHom_whisk a b π _ _ h.2, stepHom_whisk, wr_comp, wr_comp, wl_comp, wl_comp,
        wr_eqToHom _ h.1, wl_eqToHom _ (congrArg (· ++ b) h.1)]
      simp

/-- `interp` intertwines `whiskA a b` with whiskering by `obj a` and `obj b`. -/
theorem interp_whiskA {x y : Word} (a b : Word) {f : PA R} (hf : f ∈ supp R x y) :
    interp D (a ++ (x ++ b)) (a ++ (y ++ b)) (whiskA a b f) =
      (μ E F a (x ++ b)).hom ≫ (obj E F a ◁ ((μ E F x b).hom ≫ (interp D x y f ▷ obj E F b) ≫
        (μ E F y b).inv)) ≫ (μ E F a (y ++ b)).inv := by
  refine supp_induction_single (P := fun f => interp D (a ++ (x ++ b)) (a ++ (y ++ b)) (whiskA a b f) =
      (μ E F a (x ++ b)).hom ≫ (obj E F a ◁ ((μ E F x b).hom ≫ (interp D x y f ▷ obj E F b) ≫
        (μ E F y b).inv)) ≫ (μ E F a (y ++ b)).inv) ?_ ?_ ?_ hf
  · simp
  · intro f g hf hg
    simp only [map_add, hf, hg, MonoidalPreadditive.add_whiskerRight, Preadditive.add_comp,
      Preadditive.comp_add, MonoidalPreadditive.whiskerLeft_add]
  · intro m r hm
    have hm' : Valid (a ++ (x ++ b)) (FreeMonoid.toList
        (FreeMonoid.ofList ((FreeMonoid.toList m).map (Step.whisk a b)))) (a ++ (y ++ b)) :=
      Valid.whisk a b hm
    rw [whiskA_single, interp_single, interp_single]
    simp only [pathHom', dif_pos hm, dif_pos hm']
    erw [pathHom_whisk D a b _ x y hm (Valid.whisk a b hm)]
    simp only [wl, wr, MonoidalLinear.smul_whiskerRight, Linear.smul_comp, Linear.comp_smul,
      MonoidalLinear.whiskerLeft_smul]


/-- Unfold the interpretation of a concrete string of layers down to structural morphisms. -/
local macro "os_unfold" : tactic => `(tactic| simp only [pathHom_cons, pathHom_nil, stepHom, wl, wr,
  genHom, Gen.src, Gen.tgt, List.nil_append, List.cons_append, μ_cons, μ_nil, Iso.trans_hom,
  Iso.trans_inv, Iso.symm_hom, Iso.symm_inv, whiskerLeftIso_hom, whiskerLeftIso_inv, obj_cons,
  obj_nil, col, eqToHom_refl, Category.id_comp, Category.comp_id, sidewaysPath])

/-- Rewrite `interp` of a concrete valid string of layers to `pathHom`. -/
local macro "os_pth" : tactic => `(tactic| simp (disch := simp [Step.src, Step.tgt, Gen.src, Gen.tgt,
  sidewaysPath]) only [interp_pth])

/-- The quadratic relation holds. -/
theorem interp_rel_quad : interp D [true, true] [true, true] (Rel.quad.rel q qi t δ) = 0 := by
  have k2 : pathHom D [⟨[], .S, []⟩, ⟨[], .S, []⟩] [true, true] [true, true] ⟨rfl, rfl, rfl⟩ =
      (E ◁ (ρ_ E).hom) ≫ (D.cross.S ≫ D.cross.S) ≫ (E ◁ (ρ_ E).inv) := by
    os_unfold; monoidal
  have k1 : pathHom D [⟨[], .S, []⟩] [true, true] [true, true] ⟨rfl, rfl⟩ =
      (E ◁ (ρ_ E).hom) ≫ D.cross.S ≫ (E ◁ (ρ_ E).inv) := by
    os_unfold; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub, map_add, map_smul]
  os_pth
  rw [k2, k1, D.cross.quad]
  simp [Preadditive.add_comp, Preadditive.comp_add]
  exact sub_self _

/-- The braid relation holds. -/
theorem interp_rel_braid :
    interp D [true, true, true] [true, true, true] (Rel.braid.rel q qi t δ) = 0 := by
  have kl : pathHom D [⟨[], .S, [true]⟩, ⟨[true], .S, []⟩, ⟨[], .S, [true]⟩] [true, true, true]
      [true, true, true] ⟨rfl, rfl, rfl, rfl⟩ =
      (E ◁ E ◁ (ρ_ E).hom) ≫ (leftCross D.cross.S E ≫ (E ◁ D.cross.S) ≫ leftCross D.cross.S E) ≫
        (E ◁ E ◁ (ρ_ E).inv) := by
    os_unfold; simp only [leftCross]; monoidal
  have kr : pathHom D [⟨[true], .S, []⟩, ⟨[], .S, [true]⟩, ⟨[true], .S, []⟩] [true, true, true]
      [true, true, true] ⟨rfl, rfl, rfl, rfl⟩ =
      (E ◁ E ◁ (ρ_ E).hom) ≫ ((E ◁ D.cross.S) ≫ leftCross D.cross.S E ≫ (E ◁ D.cross.S)) ≫
        (E ◁ E ◁ (ρ_ E).inv) := by
    os_unfold; simp only [leftCross]; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [kl, kr, D.cross.braid, sub_self]

/-- The zigzag relation on `E` holds. -/
theorem interp_rel_zigE : interp D [true] [true] (Rel.zigE.rel q qi t δ) = 0 := by
  have k : pathHom D [⟨[true], .C, []⟩, ⟨[], .D, [true]⟩] [true] [true] ⟨rfl, rfl, rfl⟩ =
      (ρ_ E).hom ≫ ((ρ_ E).inv ≫ (E ◁ η_ F E ≫ (α_ _ _ _).inv ≫ ε_ F E ▷ E) ≫ (λ_ E).hom) ≫
        (ρ_ E).inv := by
    os_unfold; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [k, ExactPairing.coevaluation_evaluation]
  simp
  exact sub_self _

/-- The zigzag relation on `F` holds. -/
theorem interp_rel_zigF : interp D [false] [false] (Rel.zigF.rel q qi t δ) = 0 := by
  have k : pathHom D [⟨[], .C, [false]⟩, ⟨[false], .D, []⟩] [false] [false] ⟨rfl, rfl, rfl⟩ =
      (ρ_ F).hom ≫ ((λ_ F).inv ≫ (η_ F E ▷ F ≫ (α_ _ _ _).hom ≫ F ◁ ε_ F E) ≫ (ρ_ F).hom) ≫
        (ρ_ F).inv := by
    os_unfold; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [k, ExactPairing.evaluation_coevaluation]
  simp
  exact sub_self _

/-- `T` followed by the sideways crossing is the identity. -/
theorem interp_rel_TS : interp D [false, true] [false, true] (Rel.TS.rel q qi t δ) = 0 := by
  have k : pathHom D (⟨[], .T, []⟩ :: sidewaysPath) [false, true] [false, true]
      ⟨rfl, rfl, rfl, rfl, rfl⟩ =
      (F ◁ (ρ_ E).hom) ≫ (D.T ≫ sideways D.cross.S) ≫ (F ◁ (ρ_ E).inv) := by
    os_unfold; simp only [sideways]; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [k, D.T_sideways]
  simp
  exact sub_self _

/-- The sideways crossing followed by `T` is the identity. -/
theorem interp_rel_ST : interp D [true, false] [true, false] (Rel.ST.rel q qi t δ) = 0 := by
  have k : pathHom D (sidewaysPath ++ [⟨[], .T, []⟩]) [true, false] [true, false]
      (by simp [Step.src, Step.tgt, Gen.src, Gen.tgt, sidewaysPath]) =
      (E ◁ (ρ_ F).hom) ≫ (sideways D.cross.S ≫ D.T) ≫ (E ◁ (ρ_ F).inv) := by
    os_unfold; simp only [sideways]; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [k, D.sideways_T]
  simp
  exact sub_self _

/-- The dimension relation holds. -/
theorem interp_rel_dim : interp D [] [] (Rel.dim.rel q qi t δ) = 0 := by
  have k : pathHom D [⟨[], .C, []⟩, ⟨[], .T, []⟩, ⟨[], .D, []⟩] [] [] ⟨rfl, rfl, rfl, rfl⟩ =
      η_ F E ≫ D.T ≫ ε_ F E := by
    os_unfold; monoidal
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub, map_smul]
  os_pth
  rw [k, D.dim]
  simp

/-- Left whiskering by a concatenation. -/
theorem wl_append (a c : Word) {x y : Word} (f : obj E F x ⟶ obj E F y) :
    wl E F (a ++ c) f = eqToHom (congrArg (obj E F) (List.append_assoc a c x)) ≫
      wl E F a (wl E F c f) ≫ eqToHom (congrArg (obj E F) (List.append_assoc a c y).symm) := by
  rw [wl_wl]; simp

/-- The interchange relation holds. -/
theorem interp_rel_ichg (g g' : Gen) (m : Word) :
    interp D (g.src ++ (m ++ g'.src)) (g.tgt ++ (m ++ g'.tgt)) ((Rel.ichg g g' m).rel q qi t δ) = 0 := by
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub]
  os_pth
  rw [sub_eq_zero]
  simp only [pathHom_cons, pathHom_nil, stepHom, wl_nil, wr_nil, wl_comp,
    wl_eqToHom _ (List.append_nil g'.src), wl_eqToHom _ (List.append_nil g'.tgt).symm,
    wl_append, Category.assoc]
  have := wr_wl_exchange (E := E) (F := F) (genHom D g) (wl E F m (genHom D g'))
  simp only [eqToHom_trans, eqToHom_trans_assoc, eqToHom_refl, Category.id_comp,
    Category.comp_id]
  exact this

/-- **Every defining relation of `OS(z, t)` holds under the interpretation.** -/
theorem interp_rel (ρ : Rel) : interp D ρ.src ρ.tgt (ρ.rel q qi t δ) = 0 := by
  cases ρ with
  | quad => exact interp_rel_quad D
  | braid => exact interp_rel_braid D
  | zigE => exact interp_rel_zigE D
  | zigF => exact interp_rel_zigF D
  | TS => exact interp_rel_TS D
  | ST => exact interp_rel_ST D
  | dim => exact interp_rel_dim D
  | ichg g g' m => exact interp_rel_ichg D g g' m

end Interp

end QOU.OrientedSkein.OS
