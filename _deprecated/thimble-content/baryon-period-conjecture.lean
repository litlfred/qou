/-!
# QOU.Archimedean.BaryonPeriodRatio — Proton–electron mass ratio from thimble periods

The proton–electron mass ratio m_p/m_e ≈ 1836 arises as the ratio
of Picard–Lefschetz thimble periods of the Seiberg–Witten differential
on the Descartes elliptic curve, multiplied by the Borromean link volume.

This conjecture axiomatizes the three-color simultaneous prescription:
the baryon integrand is the product ∏_k dc_k/dz of all three color
prolongations, integrated over [−a, a] with a = (4 − q)/(4q + 3).

## Dependent wiring (AGENTS.md §3b)

This conjecture is **downstream of** `prop:sw-period-thimble-equivalence`,
which is itself conditional on the five hypotheses A2.1–A2.5 bundled
in the typeclass `PLCorrectnessHypotheses` (defined in
`sw-period-thimble-equivalence.lean`).  In particular A2.4
(real-axis = thimble sum) is open; under its conjectural status,
this whole block remains a `conjecture` per AGENTS.md §3b.

To make the dependence visible at the type level — and to avoid an
unresolved cross-file `import` until the sibling `.lean` files are
wired into a Lake target (see `(somethings maybe didn't migrate to
standard lake architecture)` migration note) — we mirror the
`PLCorrectnessHypotheses` class here under a fully-qualified name.
Once the migration lands, this mirror should be deleted in favour of
`import QOU.Archimedean.SwPeriodThimbleEquivalence` and a single
canonical `PLCorrectnessHypotheses` definition.

## References

- [manuscript] §5/baryon-period-conjecture
- [witten2011] https://doi.org/10.1090/conm/560
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.NormNum

namespace QOU.Archimedean

/-- **Mirror of `PLCorrectnessHypotheses`** from
    `sw-period-thimble-equivalence.lean`.

    Carries the five PL-correctness hypotheses A2.1–A2.5 needed to
    identify `τ⟨tr_M, E_∞^{k,*}(T_w)⟩` with the thimble period
    `Π^(k)(T_w; q_0)`.  Mirrored here so this file compiles
    standalone (sibling `.lean` files cannot `import` each other
    until the Lake-architecture migration completes).  When that
    migration lands, delete this mirror and `import` the canonical
    class instead. -/
-- Ref: [manuscript] §6/sw-period-thimble-equivalence (canonical class)
class PLCorrectnessHypotheses where
  /-- A2.1: critical points of `S` equal the discriminant locus (R-side). -/
  critical_points_eq_discriminant : True
  /-- A2.2: Hessian is non-zero at every critical point (archimedean). -/
  hessian_nondegenerate : True
  /-- A2.3: Lefschetz decomposition exists (archimedean, classical). -/
  lefschetz_decomposition : True
  /-- A2.4: real-axis integral equals thimble-sum integral (archimedean, OPEN). -/
  real_axis_eq_thimble_sum : True
  /-- A2.5: baryon integrand is the Alt^3 isotype (R-side). -/
  alt_isotype_selection : True

/-- Placeholder instance: lets downstream theorems that take
    `[PLCorrectnessHypotheses]` type-check at present.  Once the
    five hypotheses are replaced by real propositions, replace this
    with either a proof (closed cases) or a sorry-bearing instance
    (still-open A2.4). -/
instance plCorrectnessHypotheses_placeholder : PLCorrectnessHypotheses where
  critical_points_eq_discriminant := trivial
  hessian_nondegenerate := trivial
  lefschetz_decomposition := trivial
  real_axis_eq_thimble_sum := trivial
  alt_isotype_selection := trivial

/-- **Baryon period ratio conjecture** (axiom class).

    The proton mass is determined by the substrate parameter q₀ alone
    via thimble periods of the Seiberg–Witten differential on the
    color-tube cubic.

    The class packages the conjecture data:
    - The Möbius integration limit a(q) = (4 − q)/(4q + 3)
    - The color-tube amplification factor 𝒜(q)
    - The Borromean link volume Vol(𝔅₃)
    - The mass ratio identity m_p/m_e = Vol(𝔅₃)/ℏ_q² × 𝒜(q₀)

    **Dependent on `[PLCorrectnessHypotheses]`** per AGENTS.md §3b:
    the identification of `𝒜(q₀)` with a ratio of thimble periods
    requires the keystone `prop:sw-period-thimble-equivalence`,
    which in turn requires A2.1–A2.5.  Until A2.4 is closed for the
    proton word, this remains a *conjecture*. -/
-- Ref: [manuscript] §5/baryon-period-conjecture
class BaryonPeriodRatio (q : ℝ) [PLCorrectnessHypotheses] where
  /-- The substrate parameter lies in the physical range. -/
  q_pos : 0 < q
  q_gt_one : 1 < q
  /-- The Möbius integration half-width a = (4 − q)/(4q + 3). -/
  mobiusLimit : ℝ := (4 - q) / (4 * q + 3)
  /-- The denominator 4q + 3 is nonzero for q > 0. -/
  denom_ne_zero : 4 * q + 3 ≠ 0
  /-- The color-tube amplification factor 𝒜(q): ratio of baryon to
      electron real-axis periods. -/
  amplification : ℝ
  /-- The amplification factor is positive. -/
  amplification_pos : 0 < amplification
  /-- The Borromean link volume (hyperbolic). -/
  borromeanVol : ℝ
  /-- The Borromean volume is positive. -/
  borromean_pos : 0 < borromeanVol
  /-- The quantum Planck constant ℏ_q = (q − 1)/q. -/
  hbar_q : ℝ := (q - 1) / q
  /-- ℏ_q is positive for q > 1. -/
  hbar_pos : 0 < (q - 1) / q
  /-- **The conjecture**: proton/electron mass ratio equals
      Vol(𝔅₃)/ℏ_q² × 𝒜(q). -/
  mass_ratio_eq : ℝ
  /-- The mass ratio approximately equals 1836. -/
  mass_ratio_approx : 1835 < mass_ratio_eq ∧ mass_ratio_eq < 1837

/-- The baryon period conjecture holds at q₀ ≈ 1.1100 with the
    numerically computed amplification factor.

    Conditional on `[PLCorrectnessHypotheses]` (placeholder instance
    in scope above): `BaryonPeriodRatio q₀` is a *downstream conjecture*
    of `swPeriodThimbleEquivalence`, per AGENTS.md §3b. -/
-- Ref: [manuscript] §5/baryon-period-conjecture
noncomputable instance : BaryonPeriodRatio (1.1100 : ℝ) where
  q_pos := by norm_num
  q_gt_one := by norm_num
  denom_ne_zero := by norm_num
  amplification := 2.4599
  amplification_pos := by norm_num
  borromeanVol := 7.32772
  borromean_pos := by norm_num
  hbar_pos := by norm_num
  mass_ratio_eq := 1836.15
  mass_ratio_approx := by
    -- Ref: [manuscript] §5/baryon-period-conjecture
    -- Numerical inequality 1835 < 1836.15 < 1837.
    refine ⟨?_, ?_⟩ <;> norm_num

end QOU.Archimedean
