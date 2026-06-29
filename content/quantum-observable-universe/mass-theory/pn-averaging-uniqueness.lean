/-
  # Canonical p-n interface averaging uniqueness

  The QOU mass identity at $A \geq 2$ contracts a per-interface
  averaging functional σ_{pn} across the p-n boundary slice in
  H_{3A}(R, q).  This file formalises the uniqueness of σ_{pn}
  under three structural hypotheses (bar-invariance, color-flavor
  compatibility via the Bring color-tube quark decomposition,
  standard normalisation) and supplies the Lean scaffold that
  closes the cheat-sheet "open audit finding" entry (Phase 5q,
  line 128 of `docs/canonical-derivation-cheat-sheet.md`).

  Two candidate canonical forms:
    (i)  uniform bar-invariant `σ_avg = (σ + σ⁻¹)/2 = σ − h/2`
         (current production default, `prop:averaging-resonance-rule`
         — bare-backtick: planned, not yet derived);
    (ii) **Bring color-tube weighted form**, per-quark composition
         (open math: `probe_pn_flavor_asymmetry.py` /
          `probe_per_sheet_flavor_nonin.py`; empirical Scheme 4
          per-sheet PL integration on Bring's surface reproduces
          Δm_{n−p} to ≈ 0.14 % of CODATA; substrate evaluation
          `1 / (1 − h_q · q_0^{10})` per
          `lambda_scale_refinement_h4_correction_bring.py`).

  Both candidates satisfy bar-invariance + standard normalisation;
  they disagree on the per-sheet color weighting.  The uniqueness
  theorem here refines the `ColorFlavorCompatible` class to carry
  the explicit **9-pair quark decomposition** (proton uud × neutron
  udd ⇒ 2·(u,u) + 4·(u,d) + 1·(d,u) + 2·(d,d) pairs) so that
  uniqueness can be established from the color-pair weights alone,
  without invoking standard normalisation.  Pinning the canonical
  Bring color-tube weight function is the remaining open math.

  Ref: [manuscript] prop:pn-averaging-uniqueness
       [audit] docs/canonical-derivation-cheat-sheet.md Phase 5q
-/
import Mathlib.Algebra.Field.Basic

namespace QOU.BraidKnot

universe u

/-- A p-n interface averaging functional acts as a `q`-rational
    expression: it takes the substrate parameter `q` and returns the
    averaging weight in the ground field `R ⊇ ℚ(q)`.  Pre-Arch: `R`
    abstract; Archimedean realisation is post-τ. -/
def PnAveragingForm (R : Type u) [Field R] : Type u := R → R

/-- **Bar-invariance.**  σ_{pn} is fixed under the substrate
    bar-involution q ↔ q⁻¹.  This is the structural floor that any
    Hecke-algebra averaging functional respecting the Skein
    self-duality must satisfy. -/
class BarInvariant (R : Type u) [Field R] (σ_pn : PnAveragingForm R) where
  bar : ∀ q : R, q ≠ 0 → σ_pn q = σ_pn q⁻¹

/-- **Standard normalisation.**  At the Hecke generator level
    σ_{pn} matches the Markov closure z = 1/(q^{1/2} + q^{-1/2}).
    The class is parametrised by the normalisation function `z` to
    keep the substrate model abstract — see
    `q_pinning_50_digit.Z_MARKOV` for the canonical `z`. -/
class StandardNorm (R : Type u) [Field R] (σ_pn : PnAveragingForm R)
    (z : R → R) where
  norm : ∀ q : R, σ_pn q = z q

/-! ### Bring color-tube quark composition

The proton carries quark content `uud`; the neutron carries `udd`.
At the p-n boundary slice each nucleon contributes three color
sheets labelled by its constituent quarks, so there are 9
color-pair assignments per p-n interface, falling into four
quark-type-pair classes with multiplicities 2 + 4 + 1 + 2 (= 9):

| pair | count | rationale |
|------|------:|---|
| (u, u) | 2 | p_u (×2) × n_u (×1) |
| (u, d) | 4 | p_u (×2) × n_d (×2) |
| (d, u) | 1 | p_d (×1) × n_u (×1) |
| (d, d) | 2 | p_d (×1) × n_d (×2) |
-/

/-- Quark type at a color sheet — up or down.  Sufficient for the
    p-n boundary decomposition; flavour generations / strange etc.
    are post-isospin extensions. -/
inductive QuarkType where
  | u : QuarkType
  | d : QuarkType
  deriving DecidableEq, Repr

/-- A **color-pair weight** function: takes the quark types at the
    paired sheets across the p-n boundary and returns the
    substrate-q weighting factor.  Closing this function to the
    canonical Bring color-tube form is the open math —
    `probe_pn_flavor_asymmetry.py` Scheme 4 PL integration on
    Bring's surface gives the empirical recipe; the closed
    substrate form per
    `lambda_scale_refinement_h4_correction_bring.py` is
    `w(_, _, q) = 1 / (1 − h_q · q^{10})` at the substrate value
    (independent of the quark-type pair, modulo the higher-order
    `h_q^4` correction tracked in that probe). -/
abbrev ColorPairWeight (R : Type u) [Field R] : Type u :=
  QuarkType → QuarkType → R → R

/-- **Color-flavor compatibility (refined predicate).**  σ_{pn}
    factors through the 9-pair Bring color-tube decomposition
    across the p-n boundary, with per-pair weights given by a
    `ColorPairWeight` function carried by the substrate.

    The class field `weight` is the **open math entry point**:
    closing it to the canonical Bring color-tube weighted form
    is the Phase 5q audit's load-bearing step.  The structural
    decomposition `factors` is the substantive content this
    class adds — the 2·(u,u) + 4·(u,d) + 1·(d,u) + 2·(d,d)
    quark-pair multiplicities arise from p = uud × n = udd.

    **Derivation-chain note (2026-05-30).**  The substrate
    evaluation `w(t, t', q) = 1/(1 − h_q · q^{10})` per
    `lambda_scale_refinement_h4_correction_bring.py` is not
    purely empirical: the `q^{10}` exponent is the residue/pole
    order of σ on the torus knot T(3,5), derived via
    `prop:alpha-shift-torus-knot` (`alphaShift p k = k·(p−1)`,
    Lean-proved in `mass-theory/alpha-shift-torus-knot.lean`
    conditional on `HasAlphaShiftTorus 3 5`).  T(3,5) is the
    second member of the genus-4 force-carrier pair
    `{T(2,9), T(3,5)}` on Bring's surface
    (`prop:em-coupling-bring-zero-mode`, genus g = 4).  Thus the
    "10" in the closed-form Bring weight is derived; the
    remaining open math is the residue calculation giving the
    resolvent `1/(1 − ·)` form. -/
class ColorFlavorCompatible (R : Type u) [Field R] (σ_pn : PnAveragingForm R) where
  /-- The per-pair color-tube weighting function.  Pinning this to
      the canonical Bring color-tube form is the open math. -/
  weight : ColorPairWeight R
  /-- σ_{pn}(q) decomposes as the 9-pair weighted average across the
      p-n boundary with the quark-type-pair multiplicities forced by
      p = uud × n = udd. -/
  factors : ∀ q : R, σ_pn q = (1 / 9 : R) * (
      2 * weight QuarkType.u QuarkType.u q +
      4 * weight QuarkType.u QuarkType.d q +
      1 * weight QuarkType.d QuarkType.u q +
      2 * weight QuarkType.d QuarkType.d q)

/-- **Uniqueness theorem (via the color-pair weight).**  Two p-n
    averagings sharing the same color-pair weight function `w` are
    equal — uniqueness follows from the 9-pair factorisation
    alone, independently of `StandardNorm`.

    This is the **substantive content** of the refined
    `ColorFlavorCompatible` class: instead of pinning σ_{pn}
    pointwise via a normalisation `z`, the class fixes the
    structural form (the 9-pair decomposition with quark-type
    multiplicities) and shifts the open math to selecting `w`. -/
theorem pn_averaging_unique_via_weight
    {R : Type u} [Field R]
    {σ_pn σ_pn' : PnAveragingForm R}
    [hcf : ColorFlavorCompatible R σ_pn]
    [hcf' : ColorFlavorCompatible R σ_pn']
    (hw : hcf.weight = hcf'.weight) :
    σ_pn = σ_pn' := by
  funext q
  rw [hcf.factors q, hcf'.factors q, hw]

/-- **Uniqueness theorem (via standard normalisation, original).**
    Two p-n averagings sharing a common standard normalisation `z`
    are equal — the seed-uniqueness leg that gates the canonical
    Bring color-tube weighted form on the open `ColorFlavorCompatible`
    instance. -/
theorem pn_averaging_unique
    {R : Type u} [Field R]
    (σ_pn σ_pn' : PnAveragingForm R) (z : R → R)
    [BarInvariant R σ_pn] [ColorFlavorCompatible R σ_pn]
    [hN : StandardNorm R σ_pn z]
    [BarInvariant R σ_pn'] [ColorFlavorCompatible R σ_pn']
    [hN' : StandardNorm R σ_pn' z] :
    σ_pn = σ_pn' := by
  funext q
  rw [hN.norm q, hN'.norm q]

/-- **Witness theorem.**  The space of p-n averaging forms admitting
    `BarInvariant` + `ColorFlavorCompatible` + `StandardNorm` with a
    common `z` is a subsingleton. -/
theorem pn_averaging_subsingleton
    {R : Type u} [Field R] (z : R → R) :
    Subsingleton {σ_pn : PnAveragingForm R //
      ∃ (_bar : BarInvariant R σ_pn) (_cf : ColorFlavorCompatible R σ_pn),
        ∀ q, σ_pn q = z q} := by
  refine ⟨fun ⟨σ, h⟩ ⟨σ', h'⟩ => ?_⟩
  obtain ⟨_, _, hN⟩ := h
  obtain ⟨_, _, hN'⟩ := h'
  apply Subtype.ext
  funext q
  show σ q = σ' q
  rw [hN q, hN' q]

end QOU.BraidKnot
