import MathlibExt.CechChernClass
import MathlibExt.TorsorObstruction
import MathlibExt.TorsorDescent
import Mathlib.CategoryTheory.Sites.Spaces

/-!
# Continuous-function sheaves, their torsors, and the Chern obstruction

Bean `qou-bvxd`, open item 4(c) ("principal `U(1)`-bundles ↔ `U(1)`-cocycles"),
at the level of **sheaf torsors**. Parent `qou-533l`.

* `isSheaf_contPresheaf`: for any topological group `G`, the presheaf
  `V ↦ C(V, G)` of `MathlibExt.CechChernClass` is a **sheaf** on the site of
  opens of `X` (`Opens.grothendieckTopology X`). The proof glues continuous
  functions directly: compatibility makes the glued function well defined,
  and it is continuous because it agrees with a continuous section on an open
  neighbourhood of each point.
* `sieve_ofObjects_mem`: a family `U` of opens covering `X` generates a covering
  sieve of every open.
* `contTorsor γ`: the `C(-,G)`-torsor glued from a `G`-valued Čech 1-cocycle
  `γ` (Mathlib's `PresheafOfGroups.OneCocycle`), via `cocycleTorsor` of
  `MathlibExt.CocycleTorsor`. Its canonical sections have transition cocycle
  `γ` (`contTorsor_transition`).
* `contTorsorIso`: conversely, every `C(-,G)`-torsor with a section over each
  `U i` is isomorphic, as a presheaf, to the torsor glued from its transition
  cocycle (`descentIso` of `MathlibExt.TorsorDescent`).

So on an open cover, `C(-,G)`-torsors trivialised on the cover and
`G`-valued 1-cocycles are the same data. For `G = U(1)` this is item 4(c) for
torsor sheaves. The comparison with Mathlib's `FiberBundle` (total spaces) is
not done.

* `exists_realReduction_iff`: **a `U(1)`-torsor trivialised on the cover, whose
  transition functions have local real lifts `ξ`, comes from a
  `C(-,ℝ)`-torsor (compatibly with the sections) iff its Chern 2-cochain
  `chernClass` is an integer coboundary.** This is Yekutieli's Thm 4.17
  (`exists_liftAlong_iff_isCoboundary`) on the exponential sequence.

Sorry-free. No analytic input beyond `CechChernClass`; the gluing uses only
point-set topology. The module sits under `QOU/Transcendental/` because the
strangler-boundary audit (`scripts/transcendental-boundary-audit.py`) classes
`Continuous` as analysis; the torsor and cocycle layer it builds on stays in
`MathlibExt/`.
-/

-- Ref: [manuscript] lifting-and-descent, thm:qu-to-qou item 2 (circle bundles ↔ cocycles)

open CategoryTheory Opposite TopologicalSpace QOU.MathlibExt.StackGerbe

namespace QOU.CentralExtension

namespace Cech

variable {X : Type} [TopologicalSpace X]

/-! ### `C(-,G)` is a sheaf -/

section Sheaf

variable (G : Type) [TopologicalSpace G] [Group G] [IsTopologicalGroup G]

/-- A section of the underlying presheaf of sets, as a continuous map. -/
abbrev secF {V : (Opens X)ᵒᵖ} (f : (contPresheaf X G ⋙ forget GrpCat).obj V) :
    C(V.unop, G) := f

theorem map_secF_apply {V W : Opens X} (φ : W ⟶ V)
    (f : (contPresheaf X G ⋙ forget GrpCat).obj (op V)) (z : W) :
    secF G ((contPresheaf X G ⋙ forget GrpCat).map φ.op f) z = secF G f ⟨z.1, φ.le z.2⟩ :=
  rfl

/-- **`V ↦ C(V, G)` is a sheaf on the opens of `X`.** -/
theorem isSheaf_contPresheaf :
    Presheaf.IsSheaf (Opens.grothendieckTopology X) (contPresheaf X G ⋙ forget GrpCat) := by
  rw [isSheaf_iff_isSheaf_of_type]
  intro V S hS x hx
  -- For each point of `V`, choose a member of the sieve containing it.
  have hS' : ∀ y : V, ∃ (W : Opens X) (f : W ⟶ V), S f ∧ y.1 ∈ W := fun y => hS y.1 y.2
  choose W f hf hyW using hS'
  -- Any two members of the sieve agree at a common point.
  have agree : ∀ (W₁ W₂ : Opens X) (f₁ : W₁ ⟶ V) (f₂ : W₂ ⟶ V) (h₁ : S f₁) (h₂ : S f₂)
      (z : X) (z₁ : z ∈ W₁) (z₂ : z ∈ W₂),
      secF G (x f₁ h₁) ⟨z, z₁⟩ = secF G (x f₂ h₂) ⟨z, z₂⟩ := by
    intro W₁ W₂ f₁ f₂ h₁ h₂ z z₁ z₂
    have e := hx (homOfLE (inf_le_left : W₁ ⊓ W₂ ≤ W₁)) (homOfLE inf_le_right) h₁ h₂
      (Subsingleton.elim _ _)
    exact congrArg (fun F : (contPresheaf X G ⋙ forget GrpCat).obj (op (W₁ ⊓ W₂)) =>
      secF G F ⟨z, z₁, z₂⟩) e
  let t : V → G := fun y => secF G (x (f y) (hf y)) ⟨y.1, hyW y⟩
  have ht : ∀ (W' : Opens X) (f' : W' ⟶ V) (h' : S f') (y : V) (hy : y.1 ∈ W'),
      t y = secF G (x f' h') ⟨y.1, hy⟩ :=
    fun W' f' h' y hy => agree _ _ _ _ _ _ _ _ _
  have tcont : Continuous t := by
    rw [continuous_iff_continuousAt]
    intro y
    let O : Set V := {z | z.1 ∈ W y}
    have hO : IsOpen O := (W y).isOpen.preimage continuous_subtype_val
    refine ContinuousOn.continuousAt ?_ (hO.mem_nhds (hyW y))
    rw [continuousOn_iff_continuous_restrict]
    have : O.restrict t = fun z : O => secF G (x (f y) (hf y)) ⟨z.1.1, z.2⟩ := by
      funext z
      exact ht _ _ _ _ _
    rw [this]
    exact (secF G (x (f y) (hf y))).continuous.comp
      ((continuous_subtype_val.comp continuous_subtype_val).subtype_mk fun z => z.2)
  refine ⟨(⟨t, tcont⟩ : C(V, G)), ?_, ?_⟩
  · intro W' f' h'
    apply ContinuousMap.ext
    intro z
    rw [map_secF_apply]
    exact ht W' f' h' ⟨z.1, f'.le z.2⟩ z.2
  · intro t' ht'
    apply ContinuousMap.ext
    intro y
    have e := congrArg (fun F : (contPresheaf X G ⋙ forget GrpCat).obj (op (W y)) =>
      secF G F ⟨y.1, hyW y⟩) (ht' (f y) (hf y))
    exact e

end Sheaf

/-! ### Covers and sieves -/

theorem sieve_ofObjects_mem {I : Type} {U : I → Opens X} (hU : ∀ x : X, ∃ i, x ∈ U i)
    (T : Opens X) : Sieve.ofObjects U T ∈ Opens.grothendieckTopology X T := by
  intro x hx
  obtain ⟨i, hi⟩ := hU x
  exact ⟨T ⊓ U i, homOfLE inf_le_left, ⟨i, ⟨homOfLE inf_le_right⟩⟩, hx, hi⟩

/-! ### Torsors of `C(-,G)` and `G`-valued cocycles -/

section Torsor

variable {G : Type} [TopologicalSpace G] [Group G] [IsTopologicalGroup G]
variable {I : Type} {U : I → Opens X} (hU : ∀ x : X, ∃ i, x ∈ U i)

/-- **The `C(-,G)`-torsor glued from a `G`-valued 1-cocycle** on an open cover. -/
noncomputable def contTorsor (γ : PresheafOfGroups.OneCocycle (contPresheaf X G) U) :
    MulSheafTorsor (Opens.grothendieckTopology X) (contPresheaf X G ⋙ forget GrpCat) :=
  cocycleTorsor (isPresheafOfGroups_forget _) (isSheaf_contPresheaf G)
    (sieve_ofObjects_mem hU) (ofOneCocycle γ)

/-- The canonical sections of `contTorsor γ` have transition functions `γ`. -/
theorem contTorsor_transition (γ : PresheafOfGroups.OneCocycle (contPresheaf X G) U)
    (i j : I) {V : Opens X} (a : V ⟶ U i) (b : V ⟶ U j) :
    (contTorsor hU γ).carrier.map a.op (cocycleSection (ofOneCocycle γ) i) =
      (contTorsor hU γ).torsor.action.smul (op V) (γ.ev i j a b)
        ((contTorsor hU γ).carrier.map b.op (cocycleSection (ofOneCocycle γ) j)) :=
  cocycleSection_transition (g := ofOneCocycle γ) (isPresheafOfGroups_forget _) i j a b

/-- **Every `C(-,G)`-torsor trivialised on the cover is a glued one**: it is
isomorphic, as a presheaf, to the torsor glued from its transition cocycle. -/
noncomputable def contTorsorIso
    (P : MulSheafTorsor (Opens.grothendieckTopology X) (contPresheaf X G ⋙ forget GrpCat))
    (s : ∀ i, P.carrier.obj (op (U i))) :
    P.carrier ≅ (contTorsor hU (toOneCocycle (transition P s))).carrier :=
  descentIso P s (isPresheafOfGroups_forget _) (sieve_ofObjects_mem hU)

end Torsor

/-! ### The Chern obstruction for `U(1)`-torsors -/

section Chern

variable {I : Type} {U : I → Opens X} (hU : ∀ x : X, ∃ i, x ∈ U i)
variable (P : MulSheafTorsor (Opens.grothendieckTopology X) (contPresheaf X Circle ⋙ forget GrpCat))
  (s : ∀ i, P.carrier.obj (op (U i)))
  (ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U)
  (hξ : IsRealLift (toOneCocycle (transition P s)) ξ)

include hU in
/-- **A `U(1)`-torsor lifts to an `ℝ`-torsor iff its Chern cochain is a
coboundary.** For a `C(-,U(1))`-torsor `P` with sections `sᵢ` on an open cover
whose transition functions have local real lifts `ξ`, `P` is the pushforward
along `exp(i·)` of a `C(-,ℝ)`-torsor, with sections mapping to the `sᵢ`, iff
`c₁` is the coboundary of an integer 1-cochain. -/
theorem exists_realReduction_iff :
    (∃ (L : LiftAlong (projForget (expExtension X)) P) (t : ∀ i, L.torsor.carrier.obj (op (U i))),
        ∀ i, L.hom.app _ (t i) = s i) ↔
      PresheafCentralExtension.IsCoboundary (chernClass (toOneCocycle (transition P s)) ξ hξ) :=
  exists_liftAlong_iff_isCoboundary (expExtension X) P s (sieve_ofObjects_mem hU)
    (isSheaf_contPresheaf (Multiplicative ℝ)) ξ hξ

end Chern

end Cech

end QOU.CentralExtension
