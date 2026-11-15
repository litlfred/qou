import Mathlib.Tactic
import QOU.BraidKnot.BraidLinkTypes

/-!
# QOU.BraidKnot.multi_link_jones_q1_extension

**Multi-link Jones values at q = 1 for the c_5 / c_6 candidate
investigation.**

The Q_β precision ladder
([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
established c_1, c_2 from Kashiwara (`b`, `b²`), c_3 from Hopf-Jones at
q = 1 (`-2`), c_4 from mixed Kashiwara + Hopf-half (`b² + 1/2`). The
simple alternating Kashiwara × Jones pattern at odd k = 3 suggests
trying multi-link Jones values for c_5, c_7, ... but empirically this
fails:

  Empirical (probe_q_beta_c5_c6_multilink.py at 50 dps at q_0):
    c_5  ≈ -395.4
    c_6  ≈ -45485

The closest simple integer / multi-link Jones candidates
(`J_Borromean = -8`, `J_Hopf · J_Borromean = (-2)·(-8) = 16`, etc.)
**do not match** the empirical scale. The pattern at c_5, c_6 is
*open R&D* (recorded in `q-beta-c5-c6-multilink.witness.json`).

This module records the multi-link Jones values at q = 1 as Lean
infrastructure (proved in `braid-link-types.lean` via the extended
`Link` inductive) and provides a class for downstream consumers
to plug in any specific c_5 / c_6 candidate they want to test.

LaTeX label: `rem:multi-link-jones-q1-extension`
-/

-- Sibling-chapter dependency: extended `Link` inductive +
-- `jonesAtOne` cases for `trefoil`, `borromean`, `doubleHopf` from
-- `braid-link-types.lean`.
-- Ref: [leitner2026] rem:braid-link-types

namespace QOU.BraidKnot

/-! ## The four candidate Jones values

These are the proved Lean values exported from
`braid-link-types.lean` via the extended `Link` inductive:

  jonesAtOne Link.unknot      =  1
  jonesAtOne Link.hopfLink    = -2
  jonesAtOne Link.trefoil     =  1
  jonesAtOne Link.borromean   = -8
  jonesAtOne Link.doubleHopf  =  4

Each is provable by `rfl` from the corresponding `Link` constructor
definition. Products and disjoint-union combinations follow by
multiplicativity. -/

/-! ## Candidate Jones-composition values relevant for c_5 / c_6 -/

/-- `J_Hopf · J_Borromean = (-2) · (-8) = 16`. Candidate for c_6
    under the disjoint-union-multiplicativity hypothesis. -/
def jonesHopfTimesBorromean : ℝ := (-2 : ℝ) * (-8 : ℝ)

theorem jonesHopfTimesBorromean_eq_sixteen :
    jonesHopfTimesBorromean = 16 := by
  unfold jonesHopfTimesBorromean; norm_num

/-- `J_Borromean (sign-flipped) = +8`. The probe found this as the
    best simple-integer candidate for c_5, but the empirical value
    is `≈ -395.4` — a 50× mismatch in scale. Reported here for
    completeness; does NOT match empirical. -/
def jonesBorromeanFlipped : ℝ := 8

theorem jonesBorromeanFlipped_eq_eight :
    jonesBorromeanFlipped = 8 := rfl

/-- `J_DoubleHopf = 4`. Candidate for c_5 under double-Hopf disjoint-
    union hypothesis. Also empirically far off (`-395` vs `4`). -/
def jonesDoubleHopfValue : ℝ := 4

theorem jonesDoubleHopfValue_eq_four :
    jonesDoubleHopfValue = 4 := rfl

/-! ## Class for c_5 / c_6 candidate values

Downstream consumers can plug in any specific candidate pair via this
class. The default instance below uses the probe's "best simple
integer" candidates (`c_5 = -8`, `c_6 = 16`) but these do NOT
empirically close the precision ladder — this is open R&D content. -/

/-- **Multi-link Jones c_5 / c_6 candidate class.** Records the
    specific scalar values a downstream theorem can plug in for
    `c_5, c_6` in the precision ladder extension. -/
class MultiLinkJonesAtOne : Type where
  /-- Candidate `c_5` value (no closure yet — empirical is ≈ -395.4
      at q_0, well off any simple multi-link Jones combination). -/
  c5_candidate : ℝ
  /-- Candidate `c_6` value (empirical ≈ -45485 at q_0, also off any
      simple multi-link combination). -/
  c6_candidate : ℝ

-- Ref: [leitner2026] rem:multi-link-jones-q1-extension
-- Ref: [jones1985] doi:10.2307/1971403
-- Ref: [habiro2000] Habiro, "On the colored Jones polynomial of some simple links," RIMS Kokyuroku 1172 (2000)
/-- **Probe-derived default candidate**: `c_5 = -J_Borromean = +8`
    (sign-flipped Borromean Jones), `c_6 = J_Hopf · J_Borromean = 16`
    (Hopf-Borromean disjoint product). Both values are recorded as the
    closest simple-integer multi-link Jones candidates from
    `probe_q_beta_c5_c6_multilink.py`; they DO NOT match empirical
    `c_5 ≈ -395, c_6 ≈ -45485` and should be treated as exploratory
    placeholders, not closure values. -/
instance defaultMultiLinkJonesAtOne : MultiLinkJonesAtOne where
  c5_candidate := jonesBorromeanFlipped  -- = +8
  c6_candidate := jonesHopfTimesBorromean  -- = 16

/-! ## Status

This module provides **Lean infrastructure for the multi-link Jones
investigation**, not a closure of c_5 / c_6. The c_5, c_6 empirical
values are 50–3000× off the simple multi-link Jones candidates,
indicating that:

  • Either the precision-ladder normalisation needs revision (e.g.
    the b^k factor multiplying c_k beyond k=4 may carry an extra
    Wedderburn-weight or coupling-constant prefactor), or
  • The multi-link contributions enter via a non-trivial sum-over-
    Wedderburn-blocks formula rather than as direct Jones values,
    or
  • A new categorical input (higher-rank irrep coupling, Mostow
    rigidity gap correction, etc.) enters at orders k ≥ 5.

The next concrete probe is to test whether the **per-Wedderburn-block
contribution at k = 5, 6** matches empirical when properly weighted
by the q-deformed dimensions `dim_q(V_λ)`. This requires extending
the Wenzl-bridge `y_λ` infrastructure to ε^10, ε^12 evaluations of
the τ_M expansion on V_(2,1), V_(3), V_(1,1,1) separately.

The class `MultiLinkJonesAtOne` is the Lean hook for any future
discovery — a new instance plugs in the right values, and the
precision-ladder extension automatically picks up. -/

end QOU.BraidKnot
