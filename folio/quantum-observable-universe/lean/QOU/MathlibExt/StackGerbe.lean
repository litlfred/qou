import Mathlib.CategoryTheory.Sites.SheafHom
import Mathlib.CategoryTheory.Sites.Subsheaf

/-!
# Stacks and gerbes, design D3: descent of morphisms, `Hom = Iso` on torsors, and `Tors(A)` gerbe axioms

Mathlib (rev `f897ebc`) has no stacks, gerbes or descent data. This file develops
design D3 (beans `qou-t1dx`, `qou-skn4`, parent `qou-533l`; Yekutieli,
arXiv:0801.0083, §1–2) over an arbitrary Grothendieck site `(C, J)`:

1. **Milestone 1 — Descent of morphisms (`isSheaf_equivariantHom`):**
   If `Q` is a `J`-sheaf, then for every presheaf `P`, the presheaf on `C` sending `X` to
   the set of `A`-equivariant morphisms `P|_{C/X} ⟶ Q|_{C/X}` is a `J`-sheaf.
2. **Milestone 2 — Groupoid fibres (`Hom = Iso`) on `A`-torsors (`isIso_of_equivariantHom_torsor`):**
   For `A`-torsors (`SheafTorsor J A P`), every `A`-equivariant morphism
   `φ : P|_{C/X} ⟶ Q|_{C/X}` is an isomorphism (`IsIso φ.val`), with `A`-equivariant
   inverse (`inv_mem_equivariantHom`). Specifically:
   - `equivariantHom_injective`: if `αP, αQ` are pseudo-torsors (`IsPseudoTorsor`), every
     `A`-equivariant morphism is sectionwise injective.
   - `equivariantHom_surjective_of_nonempty`: at every object `Y` where `P(Y)` is
     non-empty, every `A`-equivariant morphism into a pseudo-torsor `Q` is surjective.
   - `equivariantHom_surjective`: if `P` is a locally non-empty `J`-sheaf and `Q` is a
     `J`-sheaf pseudo-torsor, sectionwise surjectivity holds for every `Y` by gluing the
     unique local preimages along the local-nonemptiness covering sieve in `J`.
3. **Milestone 3 — Band isomorphism and `Tors(A)` gerbe axioms (`trivialTorsorEndEquiv`,
   `equivariantHom_of_sections`, `torsor_locallyConnected`):**
   - `IsPresheafOfGroups A` and `regularAction A`: a presheaf of groups acts on itself by
     left multiplication as a globally trivial pseudo-torsor (`isPseudoTorsor_regularAction`).
   - `trivialTorsorEndEquiv`: canonical bijection
     `(equivariantHom (regularAction A hA) (regularAction A hA)).obj (op X) ≃ A.obj (op X)`
     identifying the `A`-equivariant automorphisms of the trivial torsor over `C/X` with
     `A(X)` (the band axiom).
   - `equivariantHom_of_sections`: any pair of local sections `p₀ ∈ P(V)` and `q₀ ∈ Q(V)`
     of multiplicative pseudo-torsors induces a canonical `A`-equivariant morphism
     `P|_{C/V} ⟶ Q|_{C/V}` sending `p₀` to `q₀`.
   - `torsor_locallyConnected`: for any two multiplicative `A`-torsors `P, Q` over `(C, J)`
     and any `U : C`, the sieve of morphisms `f : V ⟶ U` over which `P|_{C/V}` and
     `Q|_{C/V}` admit an `A`-equivariant isomorphism belongs to `J U` (local connectedness
     of `Tors(A)`).
   - `SiteGerbeData J A` and `torsorSiteGerbe J A`: genuine Grothendieck-topology gerbe
     carrier over `(C, J)` banded by `A`, instantiated sorry-free by `MulSheafTorsor J A`.
-/

universe w v u

namespace QOU.MathlibExt.StackGerbe

open CategoryTheory Opposite

variable {C : Type u} [Category.{v} C]

/-- An action of a presheaf of operators `A` on a presheaf `P`, natural in the base.
For a presheaf of groups `G` take `A = G ⋙ forget GrpCat`. The group axioms are not
needed for the descent-of-morphisms statement below, so they are not imposed here. -/
structure PresheafAction (A P : Cᵒᵖ ⥤ Type w) where
  /-- The action on sections over `U`. -/
  smul : ∀ U : Cᵒᵖ, A.obj U → P.obj U → P.obj U
  /-- Restriction commutes with the action. -/
  map_smul : ∀ {U V : Cᵒᵖ} (f : U ⟶ V) (a : A.obj U) (p : P.obj U),
    P.map f (smul U a p) = smul V (A.map f a) (P.map f p)

variable {A P Q : Cᵒᵖ ⥤ Type w}

/-- The subpresheaf of `presheafHom P Q` of `A`-equivariant morphisms over `C/X`. -/
def equivariantHom (αP : PresheafAction A P) (αQ : PresheafAction A Q) :
    Subpresheaf (presheafHom P Q) where
  obj X := {φ | ∀ (Y : (Over X.unop)ᵒᵖ) (a : A.obj (op Y.unop.left))
      (p : P.obj (op Y.unop.left)),
      φ.app Y (αP.smul _ a p) = αQ.smul _ a (φ.app Y p)}
  map f _ hφ := fun Y a p => hφ (op ((Over.map f.unop).obj Y.unop)) a p

/-- **Descent of morphisms for `A`-presheaves.** If `Q` is a sheaf, the presheaf of
`A`-equivariant morphisms `P|_{C/X} ⟶ Q|_{C/X}` is a sheaf, for every presheaf `P`. -/
theorem isSheaf_equivariantHom (J : GrothendieckTopology C)
    (αP : PresheafAction A P) (αQ : PresheafAction A Q) (hQ : Presheaf.IsSheaf J Q) :
    Presieve.IsSheaf J (equivariantHom αP αQ).toPresheaf := by
  have hQ' : Presieve.IsSheaf J Q := (isSheaf_iff_isSheaf_of_type J Q).mp hQ
  have hH : Presieve.IsSheaf J (presheafHom P Q) :=
    (isSheaf_iff_isSheaf_of_type J _).mp (Presheaf.IsSheaf.hom P Q hQ)
  rw [Subpresheaf.isSheaf_iff _ hH]
  intro X φ hφ Y a p
  obtain ⟨Y⟩ := Y
  have hcov := J.pullback_stable Y.hom hφ
  refine (hQ' _ hcov).isSeparatedFor.ext ?_
  intro Z k hk
  have heq := hk (op (Over.mk (𝟙 Z))) (A.map k.op a) (P.map k.op p)
  rw [presheafHom_map_app_op_mk_id] at heq
  have nat := fun (x : P.obj (op Y.left)) =>
    congr_fun (φ.naturality (Over.homMk k : Over.mk (k ≫ Y.hom) ⟶ Y).op) x
  simp only [types_comp_apply] at nat
  calc Q.map k.op (φ.app (op Y) (αP.smul _ a p))
      = φ.app (op (Over.mk (k ≫ Y.hom))) (P.map k.op (αP.smul _ a p)) := (nat _).symm
    _ = φ.app (op (Over.mk (k ≫ Y.hom))) (αP.smul _ (A.map k.op a) (P.map k.op p)) := by
        rw [αP.map_smul]; rfl
    _ = αQ.smul _ (A.map k.op a) (φ.app (op (Over.mk (k ≫ Y.hom))) (P.map k.op p)) := heq
    _ = αQ.smul _ (A.map k.op a) (Q.map k.op (φ.app (op Y) p)) :=
        congrArg (αQ.smul _ (A.map k.op a)) (nat p)
    _ = Q.map k.op (αQ.smul _ a (φ.app (op Y) p)) := (αQ.map_smul _ _ _).symm

/-! ### Milestone 2: `Hom = Iso` on `A`-torsors -/

/-- A presheaf action `αP` of `A` on `P` is a **pseudo-torsor** (formal principal
homogeneous space) if for every `U` and every pair of sections `p, q ∈ P(U)`, there is a
unique operator `a ∈ A(U)` sending `p` to `q`. -/
def PresheafAction.IsPseudoTorsor (αP : PresheafAction A P) : Prop :=
  ∀ (U : Cᵒᵖ) (p q : P.obj U), ∃! a : A.obj U, αP.smul U a p = q

/-- The sieve of morphisms `f : V ⟶ U` over which `P(V)` is non-empty. -/
def localNonemptySieve (P : Cᵒᵖ ⥤ Type w) (U : C) : Sieve U where
  arrows V _ := Nonempty (P.obj (op V))
  downward_closed := fun ⟨p⟩ g => ⟨P.map g.op p⟩

/-- A presheaf `P` is **locally non-empty** with respect to a Grothendieck topology `J`
if for every object `U : C`, `localNonemptySieve P U` belongs to `J U`. -/
def LocallyNonempty (J : GrothendieckTopology C) (P : Cᵒᵖ ⥤ Type w) : Prop :=
  ∀ U : C, localNonemptySieve P U ∈ J U

/-- An **`A`-torsor** (`SheafTorsor J A P`) on a site `(C, J)` is a `J`-sheaf `P`
equipped with a pseudo-torsor action of `A` that is locally non-empty with respect to `J`. -/
structure SheafTorsor (J : GrothendieckTopology C) (A P : Cᵒᵖ ⥤ Type w) where
  /-- The underlying `A`-action on `P`. -/
  action : PresheafAction A P
  /-- `P` is a `J`-sheaf. -/
  isSheaf : Presheaf.IsSheaf J P
  /-- The action of `A` on sections of `P` is simply transitive. -/
  isPseudoTorsor : action.IsPseudoTorsor
  /-- `P` has local sections on a `J`-covering sieve of every object `U`. -/
  locallyNonempty : LocallyNonempty J P

/-- Every `A`-equivariant morphism between pseudo-torsors is sectionwise injective. -/
theorem equivariantHom_injective {αP : PresheafAction A P} {αQ : PresheafAction A Q}
    (hP : αP.IsPseudoTorsor) (hQ : αQ.IsPseudoTorsor)
    {X : Cᵒᵖ} (φ : (equivariantHom αP αQ).obj X) (Y : (Over X.unop)ᵒᵖ) :
    Function.Injective (φ.1.app Y) := by
  intro p₁ p₂ hp
  obtain ⟨a, ha, _⟩ := hP (op Y.unop.left) p₁ p₂
  obtain ⟨e, he, _⟩ := hP (op Y.unop.left) p₁ p₁
  obtain ⟨_, _, huniqQ⟩ := hQ (op Y.unop.left) (φ.1.app Y p₁) (φ.1.app Y p₁)
  have haQ : αQ.smul (op Y.unop.left) a (φ.1.app Y p₁) = φ.1.app Y p₁ := by
    have hφa := (φ.2 Y a p₁).symm
    change αQ.smul (op Y.unop.left) a (φ.1.app Y p₁) =
      φ.1.app Y (αP.smul (op Y.unop.left) a p₁) at hφa
    rw [hφa, ha, hp]
  have heQ : αQ.smul (op Y.unop.left) e (φ.1.app Y p₁) = φ.1.app Y p₁ := by
    have hφe := (φ.2 Y e p₁).symm
    change αQ.smul (op Y.unop.left) e (φ.1.app Y p₁) =
      φ.1.app Y (αP.smul (op Y.unop.left) e p₁) at hφe
    rw [hφe, he]
  have hae : a = e := (huniqQ a haQ).trans (huniqQ e heQ).symm
  rw [← ha, hae, he]

/-- At any object `Y` where `P` has a section, every `A`-equivariant morphism into a
pseudo-torsor `Q` is surjective on sections over `Y`. -/
theorem equivariantHom_surjective_of_nonempty {αP : PresheafAction A P} {αQ : PresheafAction A Q}
    (hQ : αQ.IsPseudoTorsor) {X : Cᵒᵖ} (φ : (equivariantHom αP αQ).obj X)
    (Y : (Over X.unop)ᵒᵖ) (hne : Nonempty (P.obj (op Y.unop.left))) :
    Function.Surjective (φ.1.app Y) := by
  obtain ⟨p₀⟩ := hne
  intro q
  obtain ⟨a, ha, _⟩ := hQ (op Y.unop.left) (φ.1.app Y p₀) q
  refine ⟨αP.smul (op Y.unop.left) a p₀, ?_⟩
  have hφa := φ.2 Y a p₀
  change φ.1.app Y (αP.smul (op Y.unop.left) a p₀) =
    αQ.smul (op Y.unop.left) a (φ.1.app Y p₀) at hφa
  rw [hφa, ha]

/-- Every `A`-equivariant morphism between `A`-torsors is sectionwise surjective: local
preimages on the `J`-covering sieve where `P` is non-empty agree on overlaps by
`equivariantHom_injective`, hence glue in the sheaf `P` to a global preimage. -/
theorem equivariantHom_surjective (J : GrothendieckTopology C)
    (TP : SheafTorsor J A P) (TQ : SheafTorsor J A Q)
    {X : Cᵒᵖ} (φ : (equivariantHom TP.action TQ.action).obj X) (Y : (Over X.unop)ᵒᵖ) :
    Function.Surjective (φ.1.app Y) := by
  intro q
  obtain ⟨Y⟩ := Y
  have hP' : Presieve.IsSheaf J P := (isSheaf_iff_isSheaf_of_type J P).mp TP.isSheaf
  have hQ' : Presieve.IsSheaf J Q := (isSheaf_iff_isSheaf_of_type J Q).mp TQ.isSheaf
  let S : Sieve Y.left := localNonemptySieve P Y.left
  have hS : S ∈ J Y.left := TP.locallyNonempty Y.left
  have hsurj : ∀ ⦃Z : C⦄ (f : Z ⟶ Y.left), S.arrows f →
      ∃ x : P.obj (op Z), φ.1.app (op (Over.mk (f ≫ Y.hom))) x = Q.map f.op q := by
    intro Z f hf
    exact equivariantHom_surjective_of_nonempty TQ.isPseudoTorsor φ
      (op (Over.mk (f ≫ Y.hom))) hf (Q.map f.op q)
  let fam : Presieve.FamilyOfElements P S.arrows := fun Z f hf => (hsurj f hf).choose
  have hfam_spec : ∀ ⦃Z : C⦄ (f : Z ⟶ Y.left) (hf : S.arrows f),
      φ.1.app (op (Over.mk (f ≫ Y.hom))) (fam f hf) = Q.map f.op q :=
    fun Z f hf => (hsurj f hf).choose_spec
  have hcomp : fam.Compatible := by
    intro Z₁ Z₂ W g₁ g₂ f₁ f₂ hf₁ hf₂ hgf
    apply equivariantHom_injective TP.isPseudoTorsor TQ.isPseudoTorsor φ
      (op (Over.mk ((g₁ ≫ f₁) ≫ Y.hom)))
    have hw₁ : g₁ ≫ (Over.mk (f₁ ≫ Y.hom)).hom = (Over.mk ((g₁ ≫ f₁) ≫ Y.hom)).hom :=
      (Category.assoc g₁ f₁ Y.hom).symm
    have hw₂ : g₂ ≫ (Over.mk (f₂ ≫ Y.hom)).hom = (Over.mk ((g₁ ≫ f₁) ≫ Y.hom)).hom := by
      change g₂ ≫ f₂ ≫ Y.hom = (g₁ ≫ f₁) ≫ Y.hom
      rw [← Category.assoc, hgf]
    have nat₁ := congr_fun (φ.1.naturality
      (Over.homMk g₁ hw₁ : Over.mk ((g₁ ≫ f₁) ≫ Y.hom) ⟶ Over.mk (f₁ ≫ Y.hom)).op) (fam f₁ hf₁)
    have nat₂ := congr_fun (φ.1.naturality
      (Over.homMk g₂ hw₂ : Over.mk ((g₁ ≫ f₁) ≫ Y.hom) ⟶ Over.mk (f₂ ≫ Y.hom)).op) (fam f₂ hf₂)
    change φ.1.app (op (Over.mk ((g₁ ≫ f₁) ≫ Y.hom))) (P.map g₁.op (fam f₁ hf₁)) =
      Q.map g₁.op (φ.1.app (op (Over.mk (f₁ ≫ Y.hom))) (fam f₁ hf₁)) at nat₁
    change φ.1.app (op (Over.mk ((g₁ ≫ f₁) ≫ Y.hom))) (P.map g₂.op (fam f₂ hf₂)) =
      Q.map g₂.op (φ.1.app (op (Over.mk (f₂ ≫ Y.hom))) (fam f₂ hf₂)) at nat₂
    rw [nat₁, hfam_spec f₁ hf₁, nat₂, hfam_spec f₂ hf₂, ← FunctorToTypes.map_comp_apply,
      ← FunctorToTypes.map_comp_apply, ← op_comp, ← op_comp, hgf]
  let p : P.obj (op Y.left) := (hP' S hS).amalgamate fam hcomp
  have hp_amalg : ∀ ⦃Z : C⦄ (f : Z ⟶ Y.left) (hf : S.arrows f), P.map f.op p = fam f hf :=
    fun Z f hf => (hP' S hS).valid_glue hcomp f hf
  refine ⟨p, ?_⟩
  refine (hQ' S hS).isSeparatedFor.ext ?_
  intro Z f hf
  have nat := congr_fun (φ.1.naturality
    (Over.homMk f : Over.mk (f ≫ Y.hom) ⟶ Y).op) p
  change φ.1.app (op (Over.mk (f ≫ Y.hom))) (P.map f.op p) =
    Q.map f.op (φ.1.app (op Y) p) at nat
  rw [← nat, hp_amalg f hf, hfam_spec f hf]

/-- **`Hom = Iso` on `A`-torsors (Milestone 2).** Every `A`-equivariant morphism
`φ : P|_{C/X} ⟶ Q|_{C/X}` between `A`-torsors on `(C, J)` is an isomorphism of
presheaves on `(Over X.unop)ᵒᵖ`. -/
theorem isIso_of_equivariantHom_torsor (J : GrothendieckTopology C)
    (TP : SheafTorsor J A P) (TQ : SheafTorsor J A Q)
    {X : Cᵒᵖ} (φ : (equivariantHom TP.action TQ.action).obj X) :
    IsIso φ.1 := by
  haveI : ∀ Y : (Over X.unop)ᵒᵖ, IsIso (φ.1.app Y) := fun Y =>
    (isIso_iff_bijective (φ.1.app Y)).mpr
      ⟨equivariantHom_injective TP.isPseudoTorsor TQ.isPseudoTorsor φ Y,
       equivariantHom_surjective J TP TQ φ Y⟩
  exact NatIso.isIso_of_isIso_app φ.1

/-- The identity morphism of `P|_{C/X}` is `A`-equivariant. -/
theorem id_mem_equivariantHom (αP : PresheafAction A P) (X : Cᵒᵖ) :
    𝟙 ((Over.forget X.unop).op ⋙ P) ∈ (equivariantHom αP αP).obj X :=
  fun _ _ _ => rfl

/-- The composition of two `A`-equivariant morphisms over `C/X` is `A`-equivariant. -/
theorem comp_mem_equivariantHom {R : Cᵒᵖ ⥤ Type w}
    {αP : PresheafAction A P} {αQ : PresheafAction A Q} {αR : PresheafAction A R}
    {X : Cᵒᵖ} (φ : (equivariantHom αP αQ).obj X) (ψ : (equivariantHom αQ αR).obj X) :
    (φ.1 ≫ ψ.1) ∈ (equivariantHom αP αR).obj X := by
  intro Y a p
  change ψ.1.app Y (φ.1.app Y (αP.smul (op Y.unop.left) a p)) =
    αR.smul (op Y.unop.left) a (ψ.1.app Y (φ.1.app Y p))
  have hφ := φ.2 Y a p
  change φ.1.app Y (αP.smul (op Y.unop.left) a p) =
    αQ.smul (op Y.unop.left) a (φ.1.app Y p) at hφ
  have hψ := ψ.2 Y a (φ.1.app Y p)
  change ψ.1.app Y (αQ.smul (op Y.unop.left) a (φ.1.app Y p)) =
    αR.smul (op Y.unop.left) a (ψ.1.app Y (φ.1.app Y p)) at hψ
  rw [hφ, hψ]

/-- The inverse of an `A`-equivariant isomorphism of `A`-presheaves is again
`A`-equivariant. -/
theorem inv_mem_equivariantHom {αP : PresheafAction A P} {αQ : PresheafAction A Q}
    {X : Cᵒᵖ} (φ : (equivariantHom αP αQ).obj X) [IsIso φ.1] :
    inv φ.1 ∈ (equivariantHom αQ αP).obj X := by
  intro Y a q
  apply (isIso_iff_bijective (φ.1.app Y)).mp inferInstance |>.1
  have h1 : φ.1.app Y ((inv φ.1).app Y (αQ.smul (op Y.unop.left) a q)) =
      αQ.smul (op Y.unop.left) a q := by
    change (inv φ.1 ≫ φ.1).app Y (αQ.smul (op Y.unop.left) a q) = _
    simp
  have h2 : φ.1.app Y (αP.smul (op Y.unop.left) a ((inv φ.1).app Y q)) =
      αQ.smul (op Y.unop.left) a q := by
    have hφ := φ.2 Y a ((inv φ.1).app Y q)
    change φ.1.app Y (αP.smul (op Y.unop.left) a ((inv φ.1).app Y q)) =
      αQ.smul (op Y.unop.left) a (φ.1.app Y ((inv φ.1).app Y q)) at hφ
    rw [hφ]
    congr 1
    change (inv φ.1 ≫ φ.1).app Y q = q
    simp
  exact h1.trans h2.symm

/-! ### Milestone 3: Band isomorphism and `Tors(A)` gerbe axioms -/

/-- Compatibility of a presheaf `A` carrying sectionwise group structure `[∀ U, Group (A.obj U)]`
with restriction maps. -/
structure IsPresheafOfGroups (A : Cᵒᵖ ⥤ Type w) [∀ U : Cᵒᵖ, Group (A.obj U)] : Prop where
  /-- Restriction preserves multiplication. -/
  map_mul : ∀ {U V : Cᵒᵖ} (f : U ⟶ V) (a b : A.obj U), A.map f (a * b) = A.map f a * A.map f b
  /-- Restriction preserves the identity element. -/
  map_one : ∀ {U V : Cᵒᵖ} (f : U ⟶ V), A.map f 1 = 1

/-- Compatibility of a `PresheafAction A P` with the sectionwise group multiplication on `A`. -/
structure PresheafAction.IsMulAction [∀ U : Cᵒᵖ, Group (A.obj U)]
    (αP : PresheafAction A P) : Prop where
  /-- Identity element acts trivially. -/
  one_smul : ∀ (U : Cᵒᵖ) (p : P.obj U), αP.smul U 1 p = p
  /-- Product acts by iterated action. -/
  mul_smul : ∀ (U : Cᵒᵖ) (a b : A.obj U) (p : P.obj U),
    αP.smul U (a * b) p = αP.smul U a (αP.smul U b p)

/-- The regular left action of a presheaf of groups `A` on itself. -/
def regularAction (A : Cᵒᵖ ⥤ Type w) [∀ U : Cᵒᵖ, Group (A.obj U)]
    (hA : IsPresheafOfGroups A) : PresheafAction A A where
  smul _ a p := a * p
  map_smul f a p := hA.map_mul f a p

/-- The regular action of `A` on itself is a multiplicative action. -/
theorem isMulAction_regularAction (A : Cᵒᵖ ⥤ Type w) [∀ U : Cᵒᵖ, Group (A.obj U)]
    (hA : IsPresheafOfGroups A) : (regularAction A hA).IsMulAction where
  one_smul _ p := one_mul p
  mul_smul _ a b p := mul_assoc a b p

/-- The regular action of a presheaf of groups `A` on itself is a pseudo-torsor:
for any `p, q ∈ A(U)`, `a = q * p⁻¹` is the unique element satisfying `a * p = q`. -/
theorem isPseudoTorsor_regularAction (A : Cᵒᵖ ⥤ Type w) [∀ U : Cᵒᵖ, Group (A.obj U)]
    (hA : IsPresheafOfGroups A) : (regularAction A hA).IsPseudoTorsor := by
  intro U p q
  refine ⟨q * p⁻¹, inv_mul_cancel_right q p, fun a (ha : a * p = q) => ?_⟩
  rw [← ha, mul_inv_cancel_right]

/-- Any presheaf with a global section over every `U` is locally non-empty for every
Grothendieck topology `J`. -/
theorem locallyNonempty_of_nonempty (J : GrothendieckTopology C) (P : Cᵒᵖ ⥤ Type w)
    (hne : ∀ U : Cᵒᵖ, Nonempty (P.obj U)) : LocallyNonempty J P := by
  intro U
  have htop : localNonemptySieve P U = ⊤ := by
    ext V f
    simp only [localNonemptySieve, Sieve.top_apply, iff_true]
    exact hne (op V)
  rw [htop]
  exact J.top_mem U

/-- The **trivial `A`-torsor** on `(C, J)` associated to a `J`-sheaf of groups `A`. -/
def trivialSheafTorsor (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (hA : IsPresheafOfGroups A)
    (hAsheaf : Presheaf.IsSheaf J A) : SheafTorsor J A A where
  action := regularAction A hA
  isSheaf := hAsheaf
  isPseudoTorsor := isPseudoTorsor_regularAction A hA
  locallyNonempty := locallyNonempty_of_nonempty J A (fun _ => ⟨1⟩)

/-- **Band isomorphism for the trivial `A`-torsor (`Aut(trivial) ≃ A(X)`).**
For any presheaf of groups `A` and any object `X : C`, the `A`-equivariant endomorphisms
of the trivial `A`-torsor over `C/X` are in canonical bijection with `A.obj (op X)` via
evaluation at `1 ∈ A.obj (op X)` at `Over.mk (𝟙 X)`. -/
def trivialTorsorEndEquiv (A : Cᵒᵖ ⥤ Type w) [∀ U : Cᵒᵖ, Group (A.obj U)]
    (hA : IsPresheafOfGroups A) (X : C) :
    (equivariantHom (regularAction A hA) (regularAction A hA)).obj (op X) ≃ A.obj (op X) where
  toFun φ := φ.1.app (op (Over.mk (𝟙 X))) (1 : A.obj (op X))
  invFun g :=
    ⟨{ app := fun Y p =>
         (regularAction A hA).smul (op Y.unop.left) p (A.map Y.unop.hom.op g)
       naturality := fun Y₁ Y₂ k => by
         ext (p : A.obj (op Y₁.unop.left))
         change (regularAction A hA).smul (op Y₂.unop.left) (A.map k.unop.left.op p)
             (A.map Y₂.unop.hom.op g) =
           A.map k.unop.left.op
             ((regularAction A hA).smul (op Y₁.unop.left) p (A.map Y₁.unop.hom.op g))
         rw [(regularAction A hA).map_smul, ← FunctorToTypes.map_comp_apply, ← op_comp,
           Over.w k.unop] },
     fun Y a p => by
       change (regularAction A hA).smul (op Y.unop.left)
         ((regularAction A hA).smul (op Y.unop.left) a p) (A.map Y.unop.hom.op g) =
         (regularAction A hA).smul (op Y.unop.left) a
           ((regularAction A hA).smul (op Y.unop.left) p (A.map Y.unop.hom.op g))
       exact mul_assoc a p (A.map Y.unop.hom.op g)⟩
  left_inv φ := by
    apply Subtype.ext
    apply NatTrans.ext
    funext ⟨Y⟩ (p : A.obj (op Y.left))
    have hw : (Y.hom : Y.left ⟶ X) ≫ (Over.mk (𝟙 X)).hom = Y.hom := Category.comp_id Y.hom
    have nat := congr_fun (φ.1.naturality
      (Over.homMk Y.hom hw : Y ⟶ Over.mk (𝟙 X)).op) (1 : A.obj (op X))
    change (φ.1.app (op Y) (A.map Y.hom.op (1 : A.obj (op X))) : A.obj (op Y.left)) =
      A.map Y.hom.op (φ.1.app (op (Over.mk (𝟙 X))) (1 : A.obj (op X))) at nat
    rw [hA.map_one] at nat
    have hφ := φ.2 (op Y) p (1 : A.obj (op Y.left))
    change φ.1.app (op Y) ((regularAction A hA).smul (op Y.left) p 1) =
      (regularAction A hA).smul (op Y.left) p (φ.1.app (op Y) (1 : A.obj (op Y.left))) at hφ
    have hp1 : (regularAction A hA).smul (op Y.left) p 1 = p := mul_one p
    rw [hp1] at hφ
    change (regularAction A hA).smul (op Y.left) p
      (A.map Y.hom.op (φ.1.app (op (Over.mk (𝟙 X))) (1 : A.obj (op X)))) = φ.1.app (op Y) p
    rw [← nat, ← hφ]
  right_inv g := by
    change (regularAction A hA).smul (op X) 1 (A.map (𝟙 (op X)) g) = g
    rw [A.map_id, types_id_apply]
    exact one_mul g

/-- Given two multiplicative pseudo-torsors `(P, αP)` and `(Q, αQ)` and sections
`p₀ ∈ P(V)` and `q₀ ∈ Q(V)`, there is a canonical `A`-equivariant morphism
`P|_{C/V} ⟶ Q|_{C/V}` sending the restrictions of `p₀` to the restrictions of `q₀`. -/
noncomputable def equivariantHom_of_sections [∀ U : Cᵒᵖ, Group (A.obj U)]
    {αP : PresheafAction A P} {αQ : PresheafAction A Q}
    (hP : αP.IsPseudoTorsor) (hPm : αP.IsMulAction) (hQm : αQ.IsMulAction)
    {V : C} (p₀ : P.obj (op V)) (q₀ : Q.obj (op V)) :
    (equivariantHom αP αQ).obj (op V) :=
  ⟨{ app := fun Y p =>
       αQ.smul (op Y.unop.left)
         (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀) p).choose
         (Q.map Y.unop.hom.op q₀)
     naturality := fun Y₁ Y₂ k => by
       ext p
       simp only [Functor.comp_obj, Opposite.unop_op, Functor.op_obj, Over.forget_obj,
         Functor.comp_map, Functor.op_map, Over.forget_map, types_comp_apply]
       set a := (hP (op Y₁.unop.left) (P.map Y₁.unop.hom.op p₀) p).choose
       have ha : αP.smul (op Y₁.unop.left) a (P.map Y₁.unop.hom.op p₀) = p :=
         (hP (op Y₁.unop.left) (P.map Y₁.unop.hom.op p₀) p).choose_spec.1
       have huniq := (hP (op Y₂.unop.left) (P.map Y₂.unop.hom.op p₀)
         (P.map k.unop.left.op p)).choose_spec.2
       have ha_map : αP.smul (op Y₂.unop.left) (A.map k.unop.left.op a)
           (P.map Y₂.unop.hom.op p₀) = P.map k.unop.left.op p := by
         have h1 := (αP.map_smul k.unop.left.op a (P.map Y₁.unop.hom.op p₀)).symm
         rw [ha, ← FunctorToTypes.map_comp_apply, ← op_comp, Over.w k.unop] at h1
         exact h1
       have hchoose_eq : (hP (op Y₂.unop.left) (P.map Y₂.unop.hom.op p₀)
           (P.map k.unop.left.op p)).choose = A.map k.unop.left.op a :=
         (huniq (A.map k.unop.left.op a) ha_map).symm
       rw [hchoose_eq, αQ.map_smul, ← FunctorToTypes.map_comp_apply, ← op_comp, Over.w k.unop] },
   fun Y b p => by
     set a := (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀) p).choose
     have ha : αP.smul (op Y.unop.left) a (P.map Y.unop.hom.op p₀) = p :=
       (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀) p).choose_spec.1
     have huniq := (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀)
       (αP.smul (op Y.unop.left) b p)).choose_spec.2
     have hba : αP.smul (op Y.unop.left) (b * a) (P.map Y.unop.hom.op p₀) =
         αP.smul (op Y.unop.left) b p := by
       rw [hPm.mul_smul, ha]
     have hchoose_eq : (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀)
         (αP.smul (op Y.unop.left) b p)).choose = b * a :=
       (huniq (b * a) hba).symm
     change αQ.smul (op Y.unop.left)
       (hP (op Y.unop.left) (P.map Y.unop.hom.op p₀) (αP.smul (op Y.unop.left) b p)).choose
       (Q.map Y.unop.hom.op q₀) =
       αQ.smul (op Y.unop.left) b (αQ.smul (op Y.unop.left) a (Q.map Y.unop.hom.op q₀))
     rw [hchoose_eq, hQm.mul_smul]⟩

/-- The sieve of morphisms `f : V ⟶ U` over which two `A`-presheaves `(P, αP)` and
`(Q, αQ)` admit an `A`-equivariant isomorphism `P|_{C/V} ≅ Q|_{C/V}`. -/
def localIsoSieve (αP : PresheafAction A P) (αQ : PresheafAction A Q) (U : C) : Sieve U where
  arrows V _ := ∃ φ : (equivariantHom αP αQ).obj (op V), IsIso φ.1
  downward_closed := fun {V W f} ⟨φ, hφ⟩ g => by
    refine ⟨(equivariantHom αP αQ).toPresheaf.map g.op φ, ?_⟩
    change IsIso ((presheafHom P Q).map g.op φ.1)
    haveI : ∀ Y : (Over W)ᵒᵖ, IsIso (((presheafHom P Q).map g.op φ.1).app Y) := fun Y => by
      change IsIso (φ.1.app (op ((Over.map g).obj Y.unop)))
      infer_instance
    exact NatIso.isIso_of_isIso_app _

/-- **Local connectedness of `Tors(A)` (Milestone 3).** For any two multiplicative
`A`-torsors `TP` and `TQ` on `(C, J)` and any `U : C`, the sieve `localIsoSieve` of
morphisms `f : V ⟶ U` over which `P|_{C/V}` and `Q|_{C/V}` are `A`-equivariantly
isomorphic belongs to `J U`. -/
theorem torsor_locallyConnected (J : GrothendieckTopology C) [∀ U : Cᵒᵖ, Group (A.obj U)]
    (TP : SheafTorsor J A P) (TQ : SheafTorsor J A Q)
    (hPm : TP.action.IsMulAction) (hQm : TQ.action.IsMulAction) (U : C) :
    localIsoSieve TP.action TQ.action U ∈ J U := by
  have hinter : localNonemptySieve P U ⊓ localNonemptySieve Q U ∈ J U :=
    J.intersection_covering (TP.locallyNonempty U) (TQ.locallyNonempty U)
  refine J.superset_covering ?_ hinter
  intro V f ⟨⟨p₀⟩, ⟨q₀⟩⟩
  let φ := equivariantHom_of_sections TP.isPseudoTorsor hPm hQm p₀ q₀
  exact ⟨φ, isIso_of_equivariantHom_torsor J TP TQ φ⟩

/-- A multiplicative `A`-torsor on `(C, J)`, bundling `SheafTorsor J A P` with
`action.IsMulAction`. -/
structure MulSheafTorsor (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] where
  /-- Underlying presheaf of the torsor. -/
  carrier : Cᵒᵖ ⥤ Type w
  /-- Torsor structure on `carrier`. -/
  torsor : SheafTorsor J A carrier
  /-- Compatibility of the action with the group structure on `A`. -/
  isMulAction : torsor.action.IsMulAction

/-- The fibre category `TorsorFibre J A X` of `A`-torsors over `X : C`, whose objects are
multiplicative `A`-torsors and whose morphisms `T₁ ⟶ T₂` are `A`-equivariant morphisms
`T₁.carrier|_{C/X} ⟶ T₂.carrier|_{C/X}`. -/
@[nolint unusedArguments]
def TorsorFibre (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (_X : C) : Type (max u v (w + 1)) :=
  MulSheafTorsor J A

/-- Category instance on `TorsorFibre J A X`. -/
instance torsorFibreCategory (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (X : C) : Category (TorsorFibre J A X) where
  Hom T₁ T₂ := (equivariantHom T₁.torsor.action T₂.torsor.action).obj (op X)
  id T := ⟨𝟙 _, id_mem_equivariantHom T.torsor.action (op X)⟩
  comp φ ψ := ⟨φ.1 ≫ ψ.1, comp_mem_equivariantHom φ ψ⟩
  id_comp _ := Subtype.ext (Category.id_comp _)
  comp_id _ := Subtype.ext (Category.comp_id _)
  assoc _ _ _ := Subtype.ext (Category.assoc _ _ _)

/-- **Groupoid instance on `TorsorFibre J A X` (Milestone 2/3):** every `A`-equivariant
morphism between `A`-torsors over `C/X` is an isomorphism (`isIso_of_equivariantHom_torsor`)
with `A`-equivariant inverse (`inv_mem_equivariantHom`). -/
noncomputable instance torsorFibreGroupoid (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (X : C) : Groupoid (TorsorFibre J A X) where
  inv {T₁ T₂} φ :=
    haveI : IsIso φ.1 := isIso_of_equivariantHom_torsor J T₁.torsor T₂.torsor φ
    ⟨inv φ.1, inv_mem_equivariantHom φ⟩
  inv_comp {T₁ T₂} φ := by
    haveI : IsIso φ.1 := isIso_of_equivariantHom_torsor J T₁.torsor T₂.torsor φ
    exact Subtype.ext (IsIso.inv_hom_id φ.1)
  comp_inv {T₁ T₂} φ := by
    haveI : IsIso φ.1 := isIso_of_equivariantHom_torsor J T₁.torsor T₂.torsor φ
    exact Subtype.ext (IsIso.hom_inv_id φ.1)

/-- Base-change functor `TorsorFibre J A Y ⥤ TorsorFibre J A X` along a morphism
`f : X ⟶ Y` in `C`, restricting `A`-equivariant morphisms along `Over.map f`. -/
def torsorPullback (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] {X Y : C} (f : X ⟶ Y) :
    TorsorFibre J A Y ⥤ TorsorFibre J A X where
  obj T := T
  map {T₁ T₂} φ := (equivariantHom T₁.torsor.action T₂.torsor.action).toPresheaf.map f.op φ
  map_id _ := rfl
  map_comp _ _ := rfl

/-- Base-change along the identity morphism `𝟙 X` is the identity functor on `TorsorFibre J A X`. -/
theorem torsorPullback_id (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (X : C) :
    torsorPullback J A (𝟙 X) = 𝟭 (TorsorFibre J A X) := by
  refine CategoryTheory.Functor.ext (fun _ => rfl) (fun T₁ T₂ φ => ?_)
  simp only [Functor.id_map]
  exact congr_fun
    ((equivariantHom T₁.torsor.action T₂.torsor.action).toPresheaf.map_id (op X)) φ

/-- Base-change along a composite `f ≫ g` equals the composite of the base-change functors. -/
theorem torsorPullback_comp (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z) :
    torsorPullback J A (f ≫ g) = torsorPullback J A g ⋙ torsorPullback J A f := by
  refine CategoryTheory.Functor.ext (fun _ => rfl) (fun T₁ T₂ φ => ?_)
  simp only [Functor.comp_map]
  exact congr_fun
    ((equivariantHom T₁.torsor.action T₂.torsor.action).toPresheaf.map_comp g.op f.op) φ

/-- Genuine Grothendieck-topology **gerbe data** (`SiteGerbeData J A`) banded by a
sheaf of groups `A` on a site `(C, J)`, capturing the four defining properties of
`Tors(A)`:
1. **Descent of morphisms (prestack axiom):** for any objects `T₁, T₂`, the presheaf of
   morphisms between `T₁` and `T₂` is a `J`-sheaf.
2. **Groupoid fibres (`Hom = Iso`):** every morphism between objects over `C/X` is an
   isomorphism.
3. **Non-emptiness:** the category of objects is inhabited (hence locally non-empty).
4. **Local connectedness:** for any two objects `T₁, T₂` and any `U : C`, the sieve of
   morphisms `V ⟶ U` over which `T₁` and `T₂` become isomorphic belongs to `J U`.
5. **Band isomorphism:** the endomorphisms of the distinguished object over `X` are in
   bijection with `A.obj (op X)`. -/
structure SiteGerbeData (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w) where
  /-- Type of objects of the gerbe. -/
  Obj : Type (max u v (w + 1))
  /-- Underlying presheaf of an object. -/
  presheafOf : Obj → (Cᵒᵖ ⥤ Type w)
  /-- Underlying `A`-action of an object. -/
  actionOf : ∀ T : Obj, PresheafAction A (presheafOf T)
  /-- Distinguished neutral object. -/
  neutral : Obj
  /-- (1) Descent of morphisms: `equivariantHom` between any two objects is a `J`-sheaf. -/
  hom_isSheaf : ∀ T₁ T₂ : Obj,
    Presieve.IsSheaf J (equivariantHom (actionOf T₁) (actionOf T₂)).toPresheaf
  /-- (2) Groupoid fibres: every `A`-equivariant morphism between objects is an isomorphism. -/
  hom_isIso : ∀ (T₁ T₂ : Obj) {X : Cᵒᵖ}
    (φ : (equivariantHom (actionOf T₁) (actionOf T₂)).obj X), IsIso φ.1
  /-- (3) Local connectedness: any two objects are locally isomorphic on a `J`-covering sieve. -/
  locallyConnected : ∀ (T₁ T₂ : Obj) (U : C),
    localIsoSieve (actionOf T₁) (actionOf T₂) U ∈ J U
  /-- (4) Band isomorphism on the neutral object over every `X : C`. -/
  bandEquiv : ∀ X : C,
    (equivariantHom (actionOf neutral) (actionOf neutral)).obj (op X) ≃ A.obj (op X)

/-- **Instantiation of `SiteGerbeData J A` by the torsor gerbe `Tors(A)` (Milestone 3).** -/
noncomputable def torsorSiteGerbe (J : GrothendieckTopology C) (A : Cᵒᵖ ⥤ Type w)
    [∀ U : Cᵒᵖ, Group (A.obj U)] (hA : IsPresheafOfGroups A)
    (hAsheaf : Presheaf.IsSheaf J A) : SiteGerbeData J A where
  Obj := MulSheafTorsor J A
  presheafOf T := T.carrier
  actionOf T := T.torsor.action
  neutral :=
    { carrier := A
      torsor := trivialSheafTorsor J A hA hAsheaf
      isMulAction := isMulAction_regularAction A hA }
  hom_isSheaf T₁ T₂ := isSheaf_equivariantHom J T₁.torsor.action T₂.torsor.action T₂.torsor.isSheaf
  hom_isIso T₁ T₂ _ φ := isIso_of_equivariantHom_torsor J T₁.torsor T₂.torsor φ
  locallyConnected T₁ T₂ U :=
    torsor_locallyConnected J T₁.torsor T₂.torsor T₁.isMulAction T₂.isMulAction U
  bandEquiv X := trivialTorsorEndEquiv A hA X

end QOU.MathlibExt.StackGerbe
