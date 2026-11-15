import QOU.Basic

/-!
# QOU.BraidKnot.HeckeAnyonicSubstrate — anyonic Hecke substrate (conjecture)

Class axiomatisation of [conj:hecke-anyonic-substrate]: every QOU
particle is an anyon before observation, governed by the braid-group
action on `H_n(R, q)` via `σ_i ↦ T_{s_i}` modulo the Hecke quadratic
relation `(T_{s_i} - q)(T_{s_i} + 1) = 0`.

The `class HeckeAnyonicSubstrate` plays the role of `sorry` for the
conjecture: providing an instance asserts that the QOU substrate's
full particle spectrum is realised as `H_n(R, q)`-modules.

**What the fields actually carry** (corrected 2026-09-14): the braid
action and the Hecke quadratic relation, and nothing else.  This
paragraph used to list a third item, *observation-functor
compatibility*, which no field encodes and none ever did — the
`proof-claims-unencoded` pattern of AGENTS.md §3b-tax, a docstring
enumerating properties the fields do not carry.  That content is not
missing from the corpus, it lives one file over as
`KazhdanLusztigClassicalLimit.kl_compatible_with_tau`, which takes
`[HeckeAnyonicSubstrate R q]` as a hypothesis and states the `q = 1`
collapse of the statistical phase under `τ`.  It cannot be stated
here: this class has no `τ` and no target for it to land in.

Downstream theorems
take the class as `[HeckeAnyonicSubstrate q]` and are conditional on
the conjecture per AGENTS.md §3b-cond.

LaTeX: `\label{conj:hecke-anyonic-substrate}`

References:
- Kassel, C. (1995). *Quantum Groups*. Springer GTM 155.
- Kitaev, A. (2006). Anyons in an exactly solved model and beyond.
  Annals of Physics 321(1).
- Nayak, C. et al. (2008). Non-Abelian anyons and topological
  quantum computation. Reviews of Modern Physics 80(3).
- Khovanov, M. & Lauda, A. D. (2009). A diagrammatic approach to
  categorification of quantum groups I. Representation Theory 13.
-/

namespace QOU.BraidKnot

universe u

/-- **Hecke anyonic substrate (conjecture).**

    The `class` axiomatises that every QOU particle is an anyon at
    generic `q`: its topological statistics are governed by the
    braid-group action on a normal form `T : NormalForm` through the
    Hecke surjection.

    The fields encode:
    - `braidAction` — the action of generator `i` on a normal form;
    - `heckeQuadratic` — the defining relation
      `(σ_i - q) ∘ (σ_i + 1) = 0`;
    - `anyonic_holds` — the **conjectural** statement that the QOU
      particle spectrum is exhausted by `H_n(R, q)`-modules. -/
-- Ref: [kitaev2006] Kitaev, "Anyons in an exactly solved model and beyond," arXiv:cond-mat/0506438
-- Ref: [nayak2008] Nayak, Simon, Stern, Freedman, Das Sarma, "Non-Abelian Anyons and Topological Quantum Computation," arXiv:0707.1889
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
class HeckeAnyonicSubstrate (R : Type u) [CommRing R] (q : R) where
  /-- Abstract type of Hecke normal forms `T_w ∈ H_n(R, q)`. -/
  NormalForm : Type u
  /-- `T_w` are elements of the algebra `H_n(R, q)`, so normal forms carry
      its additive structure. Instance field: see `heckeQuadratic`. -/
  [addCommGroup : AddCommGroup NormalForm]
  /-- ... and its `R`-module structure, which is what lets the quadratic
      relation be written down at all. -/
  [isModule : Module R NormalForm]
  /-- Action of the `i`-th braid generator on a normal form. -/
  braidAction : ℕ → NormalForm → NormalForm
  /-- The Hecke quadratic relation `(T_{s_i} - q)(T_{s_i} + 1) = 0`, in the
      equivalent acted-on form `T_i^2 = (q - 1) T_i + q`.

      **Transcribed from the block's own displayed equation** (2026-09-14).
      `hecke-anyonic-substrate.md` states the relation as
      `(T_{s_i} - q)(T_{s_i} + 1) = 0`; expanding gives
      `T^2 + (1 - q) T - q = 0`, i.e. `T^2 = (q - 1) T + q`, and applying that
      to a normal form `T` is the field below. Nothing here is chosen: the
      formula is the block's, and a reviewer checks this line against the `.md`
      rather than against any reasoning of mine.

      **What it replaces.** The field used to read `heckeQuadratic : Prop` — a
      field typed with the *universe* `Prop`, so the instance supplied a
      proposition rather than a proof of one and `True` was a legal choice. Its
      own docstring recorded that the relation was held "abstractly as a Prop
      the concrete instance supplies", that nothing read it, and that encoding
      it "means giving `NormalForm` the algebra structure first". That last
      sentence is the fix, and it is cheap: `NormalForm` now carries
      `AddCommGroup` and `Module R` as instance fields, which is *weaker* than
      what the block already asserts (it places `T_w` in the algebra
      `H_n(R, q)`), so requiring a module structure adds no claim.

      The relation is now **consumed**: `braidAction_injective` below derives
      from it that every braid generator acts injectively whenever `q` is a
      unit. -/
  heckeQuadratic : ∀ (i : ℕ) (T : NormalForm),
    braidAction i (braidAction i T) = (q - 1) • braidAction i T + q • T
  /-- **The conjecture itself**: every QOU particle's normal form
      lies in the image of the braid action.  This field plays the
      role of `sorry` for `conj:hecke-anyonic-substrate`. -/
  anyonic_holds : ∀ T : NormalForm, ∃ i, ∃ T₀ : NormalForm,
    T = braidAction i T₀

namespace HeckeAnyonicSubstrate

attribute [instance] HeckeAnyonicSubstrate.addCommGroup HeckeAnyonicSubstrate.isModule

/-- **The quadratic relation, consumed.** At any `q` that is a unit, every braid
    generator acts *injectively* on normal forms.

    This is the first declaration in the corpus to read `heckeQuadratic`, and it
    is why the field is worth encoding: `(T_i - q)(T_i + 1) = 0` rearranges to
    `T_i (T_i - (q - 1)) = q`, so `q • -` factors through `braidAction i` and
    injectivity follows from `q` being cancellable. No linearity of
    `braidAction` is needed, and none is assumed — only the relation itself.

    **It can fail, which is the point.** The `IsUnit q` hypothesis is
    load-bearing rather than decorative: at `q = 0` the relation reads
    `T_i^2 = -T_i`, which the zero action satisfies on any module, so the
    conclusion is false there for any `NormalForm` with more than one element.
    A statement that survived every `q` would be saying nothing about `q`. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem braidAction_injective
    {R : Type u} [CommRing R] {q : R} [H : HeckeAnyonicSubstrate R q]
    (hq : IsUnit q) (i : ℕ) :
    Function.Injective (H.braidAction i) := by
  have key : ∀ T : H.NormalForm,
      q • T = H.braidAction i (H.braidAction i T) - (q - 1) • H.braidAction i T := by
    intro T
    rw [H.heckeQuadratic i T]
    abel
  intro T₁ T₂ h
  have hsmul : q • T₁ = q • T₂ := by rw [key T₁, key T₂, h]
  obtain ⟨u, hu⟩ := hq
  have := congrArg (fun x : H.NormalForm => ((u⁻¹ : Rˣ) : R) • x) hsmul
  simpa [smul_smul, ← hu, ← Units.val_mul] using this


/-- Trivial unconditional fact: the predicate `anyonic_holds` is
    propositional and therefore `Subsingleton`-like — two proofs of
    the same existential agree as Props.  This is a scaffolding lemma
    showing the class can be used unconditionally to extract data. -/
-- Ref: [leitner2026] braids-and-knots/hecke-anyonic-substrate
theorem normal_form_inhabited_of_action
    {R : Type u} [CommRing R] {q : R} [H : HeckeAnyonicSubstrate R q]
    (T : H.NormalForm) :
    Nonempty H.NormalForm :=
  ⟨T⟩

/-- **Counter-model at `q = 0`** — a `def`, never an `instance`.

    Over `R = ℤ` at `q = 0`, with normal forms `ℤ` and the action that negates
    on strand `0` and kills every other strand, all three fields hold. It exists
    for two reasons, and neither is to discharge the conjecture.

    1. It proves the `IsUnit q` hypothesis of `braidAction_injective` is
       load-bearing (`braidAction_not_injective_at_zero` below), so that theorem
       says something about `q` rather than holding for free.
    2. It makes concrete what the class does **not** settle: an instance exists,
       so *possessing* one is not evidence for `conj:hecke-anyonic-substrate`.
       See the scope note below for why, and what would change it.

    Per AGENTS.md §3b-tax this is deliberately **not** an `instance` — a global
    instance would silently discharge every `[HeckeAnyonicSubstrate R q]`
    hypothesis in the tree. Same disposition as
    `KazhdanLusztigClassicalLimit.canonical`. -/
-- Ref: [leitner2026] conj:hecke-anyonic-substrate (counter-model, not a witness)
def zeroQCounterModel : HeckeAnyonicSubstrate ℤ 0 where
  NormalForm := ℤ
  braidAction i T := if i = 0 then -T else 0
  heckeQuadratic := by
    intro i T
    by_cases h : i = 0 <;> simp [h]
  anyonic_holds := fun T => ⟨0, -T, by simp⟩

/-- `IsUnit q` is load-bearing in `braidAction_injective`: drop it and the
    statement is false, witnessed at `q = 0` on strand `1`. -/
-- Ref: [leitner2026] conj:hecke-anyonic-substrate
theorem braidAction_not_injective_at_zero :
    ¬ Function.Injective (zeroQCounterModel.braidAction 1) := by
  intro h
  have h10 : (1 : ℤ) = 0 := h (by rfl)
  exact one_ne_zero h10

/-! **Scope — what the encoded relation does and does not buy (2026-09-14).**

`heckeQuadratic` no longer asserts nothing: it is the block's own displayed
relation and `braidAction_injective` reads it. But the class as a whole is still
satisfiable by a degenerate model — `zeroQCounterModel` above is one, and
`.claude/skills/local/lean-generation.md` records another (`NormalForm := PUnit`,
which satisfies every field at any `q`). So an instance remains weak evidence.

The cause is structural and is **not** fixed by encoding more fields. The
conjecture's content is *exhaustion* — "the entire particle spectrum realises as
`H_n(R, q)`-modules", per the block's own "Conjectural status" paragraph — and
exhaustion cannot be stated by a class whose *instance* chooses `NormalForm`:
whatever the instance names, `anyonic_holds` quantifies only over that. Stating
it needs `NormalForm` and `braidAction` to be **caller-supplied parameters**, the
shape `DimMasterPentagon` was rebuilt into (PR #6671, mass-theory/dim-master-pentagon),
where a `∀` about caller data can fail.

That is a class-arity change reaching `KazhdanLusztigClassicalLimit`,
`RootOfUnityMTCTruncation` and `lusztig-canonical-basis-q-eq-1`, all of which
take `[HeckeAnyonicSubstrate R q]` and read `H.NormalForm`. It is left to the
author rather than taken here. Tracked as bean `qou-9yt9`. -/

/-! **No canonical instance is provided — `conj:hecke-anyonic-substrate` is open.**
Per AGENTS.md §3b-tax, an unproved primary conjecture is represented by a
content-bearing class with **no** instance (the open state); a genuine instance
over a real Hecke `NormalForm` arrives once the substrate realisation is
established. Downstream conditional theorems in `KazhdanLusztigClassicalLimit`
take `[HeckeAnyonicSubstrate R q]` as an explicit hypothesis. -/

end HeckeAnyonicSubstrate

end QOU.BraidKnot
