import Mathlib.Tactic

/-!
# QOU.BraidKnot.spectral_sequence_h3_explicit

**Canonical declaration** for content block
[`conj:spectral-sequence-h3-explicit`](../../../quantum-observable-universe/braids-and-knots/spectral-sequence-h3-explicit.md): *QOU.BraidKnot.spectral_sequence_h3_explicit*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.BraidKnot


/-- Abstract context for the `spectral_sequence_h3_explicit` claim —
    manuscript-named typed fields below; sub-claims (i) the explicit
    `d_1`-differential, (ii) the explicit `d_2`-differential, and (iii) the
    concretised page-identifications for `H_3(R, q)` are the three `Prop`
    **parameters**.

    **Parameterised 2026-09-13.**  The three sub-claims were `Prop`-valued
    *fields* with a `_holds` witness beside each — fields typed with the
    *universe* `Prop`, so the instance chose the proposition and
    `⟨True, trivial⟩` discharged all three.  Any
    `[SpectralSequenceH3ExplicitContext]`-conditional result was
    unconditional.  `QOU.ProofHygiene.SelfAssumingContexts` is the
    machine-checked statement of why this shape is a defect *regardless of
    intent*: the carrier asserts nothing even as a conjecture, so it cannot
    serve as a conjectural witness either.

    As parameters, the propositions are fixed by whoever writes the binder
    and appear in the type of every consumer, so a witness proves *that*
    proposition rather than one the instance picked.  The carrier stays
    inhabitable — it is a conjecture carrier and `Nonempty K ↔ C` is the
    correct semantics for one — but the vacuity is now visible in the type
    instead of hidden in the instance.

    **No mathematical judgement is made here, deliberately.**  An earlier
    attempt encoded sub-claim (i) as `d₁ ∘ d₁ = 0`; that is true of *any*
    differential and is not the manuscript's claim, which is the explicit
    *formula*.  The same attempt encoded (iii) as page-stabilisation past
    `r = 3`, keying the index to `3` by association with `H_3` — which is
    the Hecke **strand count**, not a spectral-sequence page index.  Both
    were the author's call to make, not this file's; parameterising states
    the shape without pre-empting either.  The conjectures are untouched
    and still open: no instance is supplied. -/
class SpectralSequenceH3ExplicitContext
    (d1Explicit d2Explicit pagesConcretised : Prop) where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Strand count of the Hecke algebra (manuscript: `H_3` ⇒ 3). -/
  n_strands : ℕ
  /-- Manuscript fact (encoded in the file's name): the Hecke algebra
      under study is `H_3(R, q)`, i.e. the 3-strand case. -/
  claim_strand_count : n_strands = 3
  /-- The Hecke algebra `H_3(R, q)` — abstract carrier. -/
  HeckeH3 : Type
  /-- Witness for manuscript sub-claim (i) — the explicit `d_1`-differential
      of the GB-filtered Hochschild spectral sequence on `H_3(R, q)`. -/
  claim_i_d1_differential_holds : d1Explicit
  /-- Witness for manuscript sub-claim (ii) — the explicit `d_2`-differential. -/
  claim_ii_d2_differential_holds : d2Explicit
  /-- Witness for manuscript sub-claim (iii) — the `E_∞` page identifications
      are *concretised* on `H_3(R, q)` for the single-nucleon case. -/
  claim_iii_page_identifications_concretised_holds : pagesConcretised

/-- **Content statement** (from manuscript):

This proposition computes the differentials $d_1, d_2$ of the
GB-filtered Hochschild spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) **explicitly**
on $H_3(R, q)$ over the paper's ground ring $R$ (paper's categorical base ring),
making the page identifications
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
concrete for the single-nucleon case.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/spectral-sequence-h3-explicit.ts
def spectral_sequence_h3_explicit
    {d1Explicit d2Explicit pagesConcretised : Prop}
    [ctx : SpectralSequenceH3ExplicitContext
             d1Explicit d2Explicit pagesConcretised] :
    ctx.n_strands = 3 ∧ d1Explicit ∧ d2Explicit ∧ pagesConcretised :=
  ⟨ctx.claim_strand_count, ctx.claim_i_d1_differential_holds,
   ctx.claim_ii_d2_differential_holds,
   ctx.claim_iii_page_identifications_concretised_holds⟩

end QOU.BraidKnot
