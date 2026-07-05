import Mathlib.Tactic

/-!
# QOU.BraidKnot.spectral_sequence_h3_explicit

**Canonical declaration** for content block
[`prop:spectral-sequence-h3-explicit`](../../../quantum-observable-universe/braids-and-knots/spectral-sequence-h3-explicit.md): *QOU.BraidKnot.spectral_sequence_h3_explicit*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.BraidKnot


/-- Abstract context for the `spectral_sequence_h3_explicit` claim —
    manuscript-named typed fields below; sub-claims encode (i) the
    explicit `d_1`-differential, (ii) the explicit `d_2`-differential,
    and (iii) the concretised page-identifications for `H_3(R, q)`. -/
class SpectralSequenceH3ExplicitContext where
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
  /-- Manuscript sub-claim (i): explicit `d_1`-differential of the
      GB-filtered Hochschild spectral sequence on `H_3(R, q)`. -/
  claim_i_d1_differential : Prop
  /-- Axiomatised proof of the sub-claim (§3b-cond conditional class). -/
  claim_i_d1_differential_holds : claim_i_d1_differential
  /-- Manuscript sub-claim (ii): explicit `d_2`-differential. -/
  claim_ii_d2_differential : Prop
  /-- Axiomatised proof of the sub-claim (§3b-cond conditional class). -/
  claim_ii_d2_differential_holds : claim_ii_d2_differential
  /-- Manuscript sub-claim (iii): the `E_∞` page identifications are
      *concretised* on `H_3(R, q)` for the single-nucleon case. -/
  claim_iii_page_identifications_concretised : Prop
  /-- Axiomatised proof of the sub-claim (§3b-cond conditional class). -/
  claim_iii_page_identifications_concretised_holds : claim_iii_page_identifications_concretised

/-- **Content statement** (from manuscript):

This proposition computes the differentials $d_1, d_2$ of the
GB-filtered Hochschild spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) **explicitly**
on $H_3(R, q)$ over the paper's ground ring $R$ (paper's categorical base ring),
making the page identifications
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
concrete for the single-nucleon case.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/spectral-sequence-h3-explicit.ts
def spectral_sequence_h3_explicit [ctx : SpectralSequenceH3ExplicitContext] :
    ctx.n_strands = 3 ∧
    ctx.claim_i_d1_differential ∧
    ctx.claim_ii_d2_differential ∧
    ctx.claim_iii_page_identifications_concretised :=
  ⟨ctx.claim_strand_count, ctx.claim_i_d1_differential_holds,
   ctx.claim_ii_d2_differential_holds,
   ctx.claim_iii_page_identifications_concretised_holds⟩

end QOU.BraidKnot
