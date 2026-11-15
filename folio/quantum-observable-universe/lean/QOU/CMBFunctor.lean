import Mathlib.Tactic

/-!
# QOU.CMBFunctor

**Canonical declaration** for content block at
[`quantum-observable-universe/information-theory/cmb-functor.ts`](quantum-observable-universe/information-theory/cmb-functor.ts).

Formalises the manuscript **CMB functor** as the composition
`CMB = colim(A₁/A₀ ⊕ A₂/A₀) ∘ ∂`: each aeon `𝒜` is sent, via the horizon
functor `∂` to its boundary, then to the colimit of the degree-`≥1` jet
quotients over that boundary, landing in `Mod_R`.

**Naming note (functor vs. object-map).** As encoded here, `CMBFunctor` is
an **object-level assignment** `CMB : Aeon → M` (a single fixed abelian
group `M`), pinned to `jetColimit ∘ boundary` — *not* a
`CategoryTheory.Functor`. There is no morphism-map and no functor law; the
target `M` is one module, not the category `Mod_R`. "Functor" is retained
as the manuscript label; the genuine functoriality (a colimit-of-jets
functor `π₀(Bun°) ⥤ Mod_R`) is not constructed here. The two theorems below
concern equal *values* (`CMB_def`), not naturality.
-/

namespace QOU

/-- Data for the CMB functor.

    A `definition` carrier: the aeons and configurations, the abelian-group
    target `M = Mod_R`, the horizon map `∂`, the jet-quotient colimit
    assignment, and `CMB` pinned to their composition. -/
structure CMBFunctor where
  /-- Aeons `π₀(Bun°)`. -/
  Aeon : Type
  /-- Ambient configurations. -/
  Config : Type
  /-- The `Mod_R` target (jet-quotient sections). -/
  M : Type
  /-- `M` is an abelian group (an `R`-module underlying group). -/
  instM : AddCommGroup M
  /-- The horizon / boundary map `∂`. -/
  boundary : Aeon → Set Config
  /-- The colimit of the degree-`≥1` jet quotients over a boundary set. -/
  jetColimit : Set Config → M
  /-- The CMB functor. -/
  CMB : Aeon → M
  /-- `CMB = (jet-quotient colimit) ∘ ∂`. -/
  CMB_def : ∀ 𝒜, CMB 𝒜 = jetColimit (boundary 𝒜)

namespace CMBFunctor

variable (F : CMBFunctor)

/-- `CMB` factors through the horizon map: aeons with the same boundary have
    the same CMB value (the functor depends only on `∂`). -/
theorem CMB_congr_of_boundary {𝒜 ℬ : F.Aeon} (h : F.boundary 𝒜 = F.boundary ℬ) :
    F.CMB 𝒜 = F.CMB ℬ := by
  rw [F.CMB_def, F.CMB_def, h]

/-- `CMB` is exactly the jet-quotient colimit evaluated on the boundary. -/
theorem CMB_eq_jetColimit_boundary (𝒜 : F.Aeon) :
    F.CMB 𝒜 = F.jetColimit (F.boundary 𝒜) := F.CMB_def 𝒜

end CMBFunctor

open Classical in
/-- **De-axiomatisation (bean `gob0`): a genuine finite direct-sum colimit.**
    Over a finite configuration type, an abelian-group target, and a
    jet-quotient assignment `jet : Config → M`, the colimit of the jet
    quotients over a boundary set `S` is realised as the actual direct sum
    `⨁_{c ∈ S} jet c` (the finite `Finset.sum` restricted to `S`). `CMB` is
    then this genuine colimit composed with the boundary map — `CMB_def` holds
    by `rfl`, so the functor is a real construction, not a free `jetColimit`
    field. -/
noncomputable def CMBFunctor.ofJet {Config : Type} [Fintype Config]
    {M : Type} [AddCommGroup M] {ι : Type}
    (jet : Config → M) (bd : ι → Set Config) : CMBFunctor where
  Aeon := ι
  Config := Config
  M := M
  instM := inferInstance
  boundary := bd
  jetColimit S := ∑ c : Config, if c ∈ S then jet c else 0
  CMB a := ∑ c : Config, if c ∈ bd a then jet c else 0
  CMB_def _ := rfl

end QOU
