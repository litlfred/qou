/-
  # p-n interface averaging: which bar-invariant forms exist

  The QOU mass identity at $A \geq 2$ contracts a per-interface
  averaging functional σ_{pn} across the p-n boundary slice.  Two
  candidate forms are on record:
    (i)  the uniform form `σ_avg = z − h/2 = (z + z̄)/2`, the
         bar-symmetriser of the p-p factor under convention D;
    (ii) the Bring colour-tube weighted form `z − h·(1/2 − δ/4)`,
         where the flavour split δ is bar-mixed (δ̄ = −q²δ).

  Only (i) is bar-invariant; (ii) is not
  (`computations/probes/pn_interface_bar_structure_probe.py`).

  This file proves two things.
  * `pn_averaging_bar_iff`: within the family σ_c = z − c·h with
    `z = q³/(q²+1)` (convention D), σ_c is bar-invariant at `q` iff
    `(c(q) + c(q⁻¹) − 1)·h = 0`.
  * `pn_averaging_unique`: for a constant `c`, bar-invariance at any
    `q` with `h(q) ≠ 0` forces `2c = 1`, so the uniform form is the
    unique bar-invariant member with constant `c`.  For a
    `q`-dependent `c` there is no uniqueness: every `c` with
    `c + c̄ = 1` qualifies.

  An earlier version proved "uniqueness" from a class field pinning
  σ_{pn} pointwise to `z`.  That was a tautology, and under convention
  D it was vacuous, since `z` itself is not bar-invariant
  (`z̄ = z − h`).  It is replaced by the statements above.

  The 9-pair colour decomposition below is kept: it shows that two
  averagings with the same colour-pair weight agree.  Choosing that
  weight is open.

  Ref: [leitner2026] prop:pn-averaging-uniqueness
-/
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Field.Basic

namespace QOU.BraidKnot

universe u

/-! ### Base ring (AGENTS.md §7c)

Nothing in this file needs a field.  The ground ring is a bare
`CommRing R`; the substrate parameter is carried as a **unit** `q : Rˣ`
wherever the bar-involution `q ↔ q⁻¹` is invoked, so the inverse is the
units inverse and never a field inverse.  The one genuine division —
the `1/9` of the 9-pair colour average — is carried by the R[h]
pattern: the class supplies the element `ninth` together with its
defining *multiplicative* relation `9 · ninth = 1`, and uniqueness of a
two-sided inverse makes it agree across instances.  The pre-Archimedean
home is `ℤ[1/9][q, q⁻¹]`; Archimedean realisation is post-τ. -/

/-- A p-n interface averaging functional acts as a `q`-rational
    expression: it takes the substrate parameter `q` and returns the
    averaging weight in the ground ring `R`.  Pre-Arch: `R`
    abstract; Archimedean realisation is post-τ. -/
def PnAveragingForm (R : Type u) [CommRing R] : Type u := R → R

/-- **Bar-invariance.**  σ_{pn} is fixed under the substrate
    bar-involution q ↔ q⁻¹.  This is the structural floor that any
    Hecke-algebra averaging functional respecting the Skein
    self-duality must satisfy.

    The substrate parameter ranges over the **units** `Rˣ`, which over
    a field is exactly the old `q ≠ 0` side condition. -/
class BarInvariant (R : Type u) [CommRing R] (σ_pn : PnAveragingForm R) where
  bar : ∀ q : Rˣ, σ_pn (q : R) = σ_pn (↑q⁻¹ : R)

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
abbrev ColorPairWeight (R : Type u) [CommRing R] : Type u :=
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
class ColorFlavorCompatible (R : Type u) [CommRing R] (σ_pn : PnAveragingForm R) where
  /-- The per-pair color-tube weighting function.  Pinning this to
      the canonical Bring color-tube form is the open math. -/
  weight : ColorPairWeight R
  /-- The reciprocal of the 9-pair count, carried as ring data (§7c
      R[h] pattern) rather than as a field division `1/9`. -/
  ninth : R
  /-- …pinned by its defining multiplicative relation.  A two-sided
      inverse is unique, so `ninth` is determined by `R`, not chosen. -/
  ninth_spec : (9 : R) * ninth = 1
  /-- σ_{pn}(q) decomposes as the 9-pair weighted average across the
      p-n boundary with the quark-type-pair multiplicities forced by
      p = uud × n = udd. -/
  factors : ∀ q : R, σ_pn q = ninth * (
      2 * weight QuarkType.u QuarkType.u q +
      4 * weight QuarkType.u QuarkType.d q +
      1 * weight QuarkType.d QuarkType.u q +
      2 * weight QuarkType.d QuarkType.d q)

/-- The carried reciprocal of `9` is unique: any two `ColorFlavorCompatible`
    instances over the same ring supply the same `ninth`.  (A two-sided
    inverse in a monoid is unique — this is the reason the R[h] carrying
    loses nothing relative to a field's `1/9`.) -/
theorem ninth_eq_ninth {R : Type u} [CommRing R]
    {σ_pn σ_pn' : PnAveragingForm R}
    (hcf : ColorFlavorCompatible R σ_pn) (hcf' : ColorFlavorCompatible R σ_pn') :
    hcf.ninth = hcf'.ninth :=
  calc hcf.ninth
      = hcf.ninth * ((9 : R) * hcf'.ninth) := by rw [hcf'.ninth_spec, mul_one]
    _ = (9 : R) * hcf.ninth * hcf'.ninth := by ring
    _ = hcf'.ninth := by rw [hcf.ninth_spec, one_mul]

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
    {R : Type u} [CommRing R]
    {σ_pn σ_pn' : PnAveragingForm R}
    [hcf : ColorFlavorCompatible R σ_pn]
    [hcf' : ColorFlavorCompatible R σ_pn']
    (hw : hcf.weight = hcf'.weight) :
    σ_pn = σ_pn' := by
  funext q
  rw [hcf.factors q, hcf'.factors q, hw, ninth_eq_ninth hcf hcf']

/-! ### Bar-invariant averagings under convention D

Over a field, with `z = q³/(q²+1)` and `h = q − q⁻¹`, the bar involution
`q ↦ q⁻¹` sends `z` to `z − h` and `h` to `−h`.  So the averaging
`z − c·h` is bar-invariant exactly when `c + c̄ = 1`. -/

section ConventionD

variable {R : Type u} [Field R]

/-- The convention-D Markov parameter `z = q³/(q²+1)`. -/
def pnZD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke parameter `h = q − q⁻¹`. -/
def pnH (q : R) : R := q - q⁻¹

theorem pnH_inv (q : R) : pnH q⁻¹ = - pnH q := by
  unfold pnH; rw [inv_inv]; ring

/-- `z̄ = z − h` under convention D. -/
theorem pnZD_inv (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    pnZD q⁻¹ = pnZD q - pnH q := by
  unfold pnZD pnH
  have h' : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    rw [inv_pow]
    intro h
    apply hq2
    have hq2' : q ^ 2 ≠ 0 := pow_ne_zero 2 hq0
    have := congrArg (· * q ^ 2) h
    simp only [add_mul, inv_mul_cancel₀ hq2', zero_mul, one_mul] at this
    linear_combination this
  field_simp
  rw [add_comm 1 (q ^ 2), div_self hq2]
  ring

/-- **Bar-invariance criterion.**  The averaging `z − c·h` takes the same
    value at `q` and `q⁻¹` iff `(c(q) + c(q⁻¹) − 1)·h(q) = 0`. -/
theorem pn_averaging_bar_iff (c : R → R) (q : R) (hq0 : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    pnZD q - c q * pnH q = pnZD q⁻¹ - c q⁻¹ * pnH q⁻¹ ↔
      (c q + c q⁻¹ - 1) * pnH q = 0 := by
  rw [pnZD_inv q hq0 hq2, pnH_inv]
  constructor
  · intro h; linear_combination -h
  · intro h; linear_combination -h

/-- **Uniqueness among constant coefficients.**  If `z − c·h` with a
    constant `c` is bar-invariant at some `q` with `h(q) ≠ 0`, then
    `2c = 1`: the uniform form `z − h/2` is the only one.  This says
    nothing about a `q`-dependent `c`, such as the colour-weighted form. -/
theorem pn_averaging_unique (c q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hh : pnH q ≠ 0)
    (hbar : pnZD q - c * pnH q = pnZD q⁻¹ - c * pnH q⁻¹) :
    2 * c = 1 := by
  have := (pn_averaging_bar_iff (fun _ => c) q hq0 hq2).1 hbar
  have h2 : c + c - 1 = 0 := (mul_eq_zero.1 this).resolve_right hh
  linear_combination h2

/-- The uniform form is bar-invariant (existence half). -/
theorem pn_averaging_uniform_bar (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (two : (2 : R) ≠ 0) :
    pnZD q - 2⁻¹ * pnH q = pnZD q⁻¹ - 2⁻¹ * pnH q⁻¹ := by
  refine (pn_averaging_bar_iff (fun _ => (2 : R)⁻¹) q hq0 hq2).2 ?_
  have : (2 : R)⁻¹ + 2⁻¹ - 1 = 0 := by field_simp; ring
  simp [this]

end ConventionD

end QOU.BraidKnot
