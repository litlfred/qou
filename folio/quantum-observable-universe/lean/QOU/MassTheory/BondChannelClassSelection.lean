/-
  CAL-3 class selection on the inter-nucleon bond channel — Lean formalization
  of GAP-1 closure path 1 of
  docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md (R2-e).

  Small algebraic model (generic commutative ring throughout, AGENTS.md §7c —
  nothing archimedean, no ordering, no numeric literals beyond ring 0):

    * `CalClass` — the three calibration classes of the canonical triple
      (CAL-1 = m_e W-plane scale, CAL-2 = P_skew^β / q₀ W-plane modulus
      (dimensionless), CAL-3 = P_avg^π / m_π orthogonal meson class).  The
      count-alignment of the triple with the three H¹(Bring) degrees of
      freedom is the conjecture `conj:calibration-cohomology-alignment`
      (content block `mass-theory/calibration-cohomology-alignment`; no Lean
      carrier since 2026-11-20); this file needs only
      the three-element class inventory.
    * `BondChannelModel` — the two dimensionful scales m_e, m_π, a
      dimensionless q₀-rational factor per class (CAL-2's entire
      contribution is such a factor: q₀ is dimensionless), the hyperbolic
      volume of the bond channel with the geometric input
      `volBond_eq_zero` (the inter-nucleon bond of the bond-count law is a
      2-body sub-link = Hopf, and Vol(Hopf) = 0 — SnapPy-verified
      non-hyperbolic; ledger row
      docs/coordination/binding-scale-is-hyperbolic-volume.md), and the
      dimensionful `support` each class contributes to the bond channel.

  Proved OUTRIGHT (`wplane_term_eq_zero_of_vol_eq_zero`,
  `BondChannelModel.wPlaneTerm_eq_zero`): the W-plane per-link term
  m_e·Vol(K)·Q vanishes identically on a Vol = 0 channel.  A trivial
  multiplication — but the structurally load-bearing step of the
  class-selection argument (the audit's (a2)).

  CONDITIONAL part (AGENTS.md §3b-cond).  The conditional hypothesis is the
  `B = m_e·Vol` LEDGER IDENTIFICATION: that the W-plane classes enter
  per-link binding only through the term m_e·Vol(K) times a dimensionless
  q₀-factor, and CAL-3 only through the meson scale m_π.  It is carried as
  the content-bearing Prop class `BindingVolumeLedger` (fields = the three
  support identifications — hypotheses, not conclusions).  NO instance is
  declared anywhere in the corpus: fabricating one would launder the ledger
  conjecture (AGENTS.md §Axiomatization is NOT a Proof).  Conditional on the
  class, `eq_cal3_of_support_ne_zero_of_ledger` proves the uniqueness
  statement — CAL-3 is the unique calibration class with (possibly) nonzero
  support on the Vol = 0 bond channel — the categorical face of the
  Yukawa-range insight, upgrading the audit's (a) from
  corpus-identification-composition to a §3b-cond conditional result.

  -- Ref: [leitner2026] docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md §GAP 1 (a)
  -- Ref: [leitner2026] docs/coordination/binding-scale-is-hyperbolic-volume.md
-/

import Mathlib.Algebra.Ring.Defs

namespace QOU.Mass.BondChannelClassSelection

/-- The three calibration classes of the canonical triple (the ideal
    mathematical calibrations; AGENTS.md cheat-sheet table). -/
inductive CalClass : Type
  /-- CAL-1: the leptonic mass scale `m_e` — the W-plane *scale*. -/
  | cal1
  /-- CAL-2: the β-decay width `P_skew^β`, numerically pinned via `m_μ/m_e` — the
      W-plane *modulus* `q₀`, a dimensionless quantity. -/
  | cal2
  /-- CAL-3: the pion-sector bar-even channel `P_avg^π` / meson scale `m_π` — the
      cohomologically orthogonal `Vol(Hopf) = 0` class. -/
  | cal3
  deriving DecidableEq

variable {R : Type*} [CommRing R]

/-- **The W-plane term vanishes on `Vol = 0` channels.**  The per-link
    W-plane contribution is `m_e·Vol(K)·Q` with `Q` a dimensionless
    q₀-factor; on a channel of vanishing hyperbolic volume it is zero
    identically — for every scale `m_e` and every factor `Q`.  Trivial
    multiplication, structurally load-bearing: this is the annihilation
    step (a2) of the class-selection argument. -/
theorem wplane_term_eq_zero_of_vol_eq_zero (me vol Q : R) (h : vol = 0) :
    me * vol * Q = 0 := by
  rw [h, mul_zero, zero_mul]

/-- Small algebraic model of the three calibration classes and their
    length-scale support on the inter-nucleon bond channel.  The field
    `volBond_eq_zero` records the geometric input: the bond channel is the
    2-body Hopf class, whose complement is non-hyperbolic, `Vol(Hopf) = 0`
    (SnapPy-verified; ledger
    `docs/coordination/binding-scale-is-hyperbolic-volume.md`). -/
structure BondChannelModel (R : Type*) [CommRing R] where
  /-- CAL-1 scale `m_e` (the W-plane scale / dimensional unit). -/
  me : R
  /-- CAL-3 scale `m_π` (the orthogonal meson scale). -/
  mpi : R
  /-- Dimensionless q₀-rational factor attached to each class — CAL-2's
      entire contribution enters through such factors (q₀ is dimensionless,
      so CAL-2 carries no length scale of its own). -/
  qFactor : CalClass → R
  /-- Hyperbolic volume of the bond (Hopf, 2-body) channel. -/
  volBond : R
  /-- Dimensionful support of each calibration class on the bond channel. -/
  support : CalClass → R
  /-- Geometric input: `Vol(Hopf) = 0` (the Hopf complement is
      non-hyperbolic). -/
  volBond_eq_zero : volBond = 0

namespace BondChannelModel

variable (M : BondChannelModel R)

/-- The W-plane per-link term on the bond channel: `m_e·Vol(bond)·Q(c)`. -/
def wPlaneTerm (c : CalClass) : R := M.me * M.volBond * M.qFactor c

/-- **Proved outright:** the W-plane term is identically zero on the bond
    channel, for every class's q₀-factor — `m_e·Vol(Hopf)·Q = 0` since
    `Vol(Hopf) = 0`. -/
theorem wPlaneTerm_eq_zero (c : CalClass) : M.wPlaneTerm c = 0 :=
  wplane_term_eq_zero_of_vol_eq_zero M.me M.volBond (M.qFactor c)
    M.volBond_eq_zero

end BondChannelModel

/-- **Conditional carrier (§3b-cond) — the `B = m_e·Vol` ledger
    identification.**  The fields axiomatise the HYPOTHESES of the
    class-selection argument, not its conclusion: the W-plane classes
    (CAL-1, CAL-2) enter per-link binding only through the W-plane term
    `m_e·Vol·Q` (the per-link volume-conjecture instances of the
    binding-scale ledger), and CAL-3 only through the meson scale `m_π`
    times a dimensionless factor.  The vanishing and uniqueness statements
    are DERIVED from these fields together with `volBond_eq_zero` — the
    class does not carry them.

    This is a primary conjecture carrier: NO instance is declared anywhere
    (an unproved premise is honestly represented by a content-bearing class
    with no instance; fabricating an instance would launder the ledger
    identification, AGENTS.md §Axiomatization is NOT a Proof).

    -- @conjecture: primary
    -- Ref: [leitner2026] docs/coordination/binding-scale-is-hyperbolic-volume.md -/
class BindingVolumeLedger (R : Type*) [CommRing R]
    (M : BondChannelModel R) : Prop where
  /-- CAL-1 supports the bond channel only through the W-plane term. -/
  support_cal1_eq : M.support CalClass.cal1 = M.wPlaneTerm CalClass.cal1
  /-- CAL-2 supports the bond channel only through the W-plane term (its
      modulus q₀ being dimensionless). -/
  support_cal2_eq : M.support CalClass.cal2 = M.wPlaneTerm CalClass.cal2
  /-- CAL-3 supports the bond channel through the meson scale. -/
  support_cal3_eq :
    M.support CalClass.cal3 = M.mpi * M.qFactor CalClass.cal3

section Conditional

variable (M : BondChannelModel R) [BindingVolumeLedger R M]

/-- Conditional on the ledger identification: CAL-1's bond-channel support
    vanishes identically (`m_e·Vol(Hopf)·Q = 0`). -/
theorem support_cal1_eq_zero_of_ledger : M.support CalClass.cal1 = 0 := by
  rw [BindingVolumeLedger.support_cal1_eq (M := M)]
  exact M.wPlaneTerm_eq_zero CalClass.cal1

/-- Conditional on the ledger identification: CAL-2's bond-channel support
    vanishes identically. -/
theorem support_cal2_eq_zero_of_ledger : M.support CalClass.cal2 = 0 := by
  rw [BindingVolumeLedger.support_cal2_eq (M := M)]
  exact M.wPlaneTerm_eq_zero CalClass.cal2

/-- **Uniqueness (conditional on the ledger identification).**  CAL-3 is the
    unique calibration class with (possibly) nonzero support on the Vol = 0
    bond channel: any class with nonzero bond-channel support is CAL-3.
    This is the 0-bit class selection of the audit's finding (a). -/
theorem eq_cal3_of_support_ne_zero_of_ledger {c : CalClass}
    (hc : M.support c ≠ 0) : c = CalClass.cal3 := by
  cases c with
  | cal1 => exact absurd (support_cal1_eq_zero_of_ledger M) hc
  | cal2 => exact absurd (support_cal2_eq_zero_of_ledger M) hc
  | cal3 => rfl

/-- Conditional factoring: the bond-channel support of every class is either
    zero or the CAL-3 value `m_π·Q(cal3)` — the bond length unit factors
    through the CAL-3 class. -/
theorem support_eq_ite_of_ledger (c : CalClass) :
    M.support c =
      if c = CalClass.cal3 then M.mpi * M.qFactor CalClass.cal3 else 0 := by
  cases c with
  | cal1 =>
    rw [if_neg (by exact fun h => CalClass.noConfusion h)]
    exact support_cal1_eq_zero_of_ledger M
  | cal2 =>
    rw [if_neg (by exact fun h => CalClass.noConfusion h)]
    exact support_cal2_eq_zero_of_ledger M
  | cal3 =>
    rw [if_pos rfl]
    exact BindingVolumeLedger.support_cal3_eq (M := M)

/-- Conditional corollary: a nonzero bond-channel scale is necessarily
    `m_π`-valued — the categorical face of the Yukawa-range statement (the
    bond length unit is `ℏc/(m_π·Q(q₀))`). -/
theorem support_eq_mpi_mul_of_support_ne_zero_of_ledger {c : CalClass}
    (hc : M.support c ≠ 0) :
    M.support c = M.mpi * M.qFactor CalClass.cal3 := by
  have h3 := eq_cal3_of_support_ne_zero_of_ledger M hc
  subst h3
  exact BindingVolumeLedger.support_cal3_eq (M := M)

end Conditional

end QOU.Mass.BondChannelClassSelection
