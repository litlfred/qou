import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic

/-!
# QOU.Mass.QbetaC3Stokes — the colored-Jones / GGM-resurgence (Stokes) route to
the Q_β ladder coefficient `c_3`, and the VALUE-MISMATCH obstruction that
falsifies its bare-Stokes-constant form.

**Scope (read first).** This file records — HONESTLY — the outcome of the
**GGM colored-Jones / Gu–Mariño resurgence (Stokes)** derivation attempt for the
Q_β precision-ladder coefficient `c_3` (bean `qou-1dnr`; parallel to, and
distinct from, the DM-cubic route `QOU.Mass.QbetaC3DMCubic` and the Habiro-element
route). The attempt is a **scope-(a) NEGATIVE**, and the negative is a genuine,
sorry-free theorem.

**Door-v framing.** Q_β is the **bar-odd / sinh / decay** face = the GGM
colored-Jones / Stokes face (opposite `(−1)^m` parity to the bar-even mass face).
The natural resurgent candidate for `c_3` as an "order-3 Stokes coefficient" is
the **integer Stokes constant `3`** on the figure-eight `4₁` singularity
`ι = ±Vol(4₁)/π` (`S⁰ = [[1,0],[−3,1]]`; descendant tower
`S⁺₁₁ = 1 − 8q − 9q² + 18q³ + …`), certified exact in the corpus
(`qbeta_g3_ggm_stokes_41.py`: det W_m = 2, eq-49 q-difference, sandwich 59a).

**Why the route is obstructed (the theorems below).** A GGM Stokes constant is
the RIGHT TYPE for a derivation — it is **anchor-invariant** (a fixed integer / a
fixed convergent q-series; the two-anchor probe measures the `S⁺₁₁` tower moving
only `6·10⁻⁶ %` between the proton- and muon-pinned anchors). But its **value**
is not `c_3`:

* `stokesInt_strictly_worse_c3_than_nearMatch` — over any linear-ordered field,
  for every empirical `c_3` in the corpus bracket `[-21/10, -2]`, the raw Stokes
  integer `-3` is a **strictly worse** `c_3` than even the crude `-2` near-match:
  `|(-3) - empC3| > |(-2) - empC3|`. (sorry-free) This is the algebraic shadow of
  the probe's Q_β residuals: `c_3 = -3 → 576 ppb` (74× the 7.8 ppb 100× target)
  vs the `-2` near-match's `43 ppb`, vs the cal `-2.069`'s `0`.
* `constantStokesDatum_cannot_match_both_anchors` — a q-independent (constant)
  Stokes datum used as `c_3` is anchor-invariant, so if it value-matched the
  empirical `c_3` at BOTH anchors it would force the two empirical values equal,
  contradicting the measured cross-anchor swing. (sorry-free)

The substrate-meridian complement (numerical, `dladder-fibre-branch-stokes-
ambiguity`): on the real-q₀ meridian the Stokes jump `exp(−A/u)` is
`~10⁻²⁷`-suppressed (anchor-blind), so there is no substrate-meridian Stokes
mechanism to source a ppm-level `c_3` rung; the unsuppressed `A_ω` lives on the
fibre branch (`|q| = 1`, `u ~ O(1)`).

**What stays OPEN (the conjecture class).** The route is not that a **bare**
Stokes integer equals `c_3`, but that a **normalized** Stokes datum does — the
open **§4e quantum-modularity / 3d-index** bridge that turns the anchor-invariant
integer datum into the (smooth, bar-odd) `c_3` object via a fixed-basis
normalization. Recorded as a content-bearing **primary conjecture class** with
**no instance**.

## Honesty (AGENTS.md §Axiomatization is NOT a Proof, §3b, ck-dk-registry §8)

* The two obstruction theorems are genuine sorry-free ordered-field algebra/logic.
* The conjecture class is content-bearing (parameter-quantified fields, no `True`,
  no empty marker) and has **NO instance** — the honest open state; matching two
  `-3`'s (the GGM constant and, e.g., `disc ℚ(√−3)`) is NOT a derivation.
* Nothing is wired to production; `c_3` stays EMPIRICAL. This file does not change
  any rung's tier — it records why the GGM-Stokes route does not promote `c_3` in
  its bare form and pins the open normalization bridge.

## Base ring (§7c)

The value-mismatch theorem compares magnitudes of derived numeric candidates, so
it needs an ordering: generic `{R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]` — no `ℝ`, no
`Real.*`. The archimedean substrate evaluation (the actual `q₀ ≈ 1.10998`, the
`u³ = 6.18·10⁻⁷` rung) lives downstream in the probe, past the
substrate→archimedean wall.

## References

- [garoufalidis-gu-marino2021] https://arxiv.org/abs/2011.07617 (Stokes constants
  = DT integers; the `4₁`/`5₂` peacock patterns).
- [manuscript] `conj:binding-qbeta-complex`; `conj:qdifference-kernel-prolongation-symbol`;
  `docs/coordination/ck-dk-canonical-registry.md` §9;
  `docs/audits/2026-07-20-c3-stokes-route.md`;
  probes `computations/probes/qbeta_c3_stokes_ggm_order3_probe.py`,
  `computations/probes/qbeta_g3_ggm_stokes_41.py`,
  `docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`.
-/

namespace QOU.Mass.QbetaC3Stokes

/-! ### (1) The value-mismatch obstruction (sorry-free)

The raw GGM order-3 Stokes constant is the integer `-3`. We show that, against
any empirical `c_3` in the corpus bracket, `-3` is a strictly worse candidate
than even the standing `-2` near-match — the algebraic core of the probe's
`576 ppb` vs `43 ppb` Q_β residuals. -/

/-- **THE VALUE MISMATCH (sorry-free).** For every empirical `c_3` value `empC3`
in the corpus bracket `-21/10 ≤ empC3 ≤ -2` (the two-anchor extraction sits at
`≈ -2.069`), the raw GGM order-3 Stokes integer `-3` is a **strictly worse**
`c_3` than the crude `-2` near-match:
`|(-3) - empC3| > |(-2) - empC3|`.
Consequently the bare Stokes integer cannot be `c_3`: it does not even beat the
near-match it would have to improve on. -/
theorem stokesInt_strictly_worse_c3_than_nearMatch {R : Type*}
    [Field R] [LinearOrder R] [IsStrictOrderedRing R] (empC3 : R)
    (hlo : -21/10 ≤ empC3) (hhi : empC3 ≤ -2) :
    |(-3 : R) - empC3| > |(-2 : R) - empC3| := by
  have h3 : |(-3 : R) - empC3| = -(-3 - empC3) :=
    abs_of_nonpos (by linarith)
  have h2 : |(-2 : R) - empC3| = -2 - empC3 :=
    abs_of_nonneg (by linarith)
  rw [h3, h2]; linarith

/-- **Anchor-invariance corollary (sorry-free).** A q-independent (constant)
Stokes datum used as a `c_3`-candidate is anchor-invariant. If it value-matched
the empirical `c_3` at BOTH the proton anchor `qp` and the muon anchor `qm`, the
two empirical values `empP, empM` would be forced equal — contradicting the
measured cross-anchor swing (`hSwing`). So even setting the value aside, a bare
constant Stokes datum matches at most one anchor. -/
theorem constantStokesDatum_cannot_match_both_anchors {R : Type*}
    [Field R] [LinearOrder R] [IsStrictOrderedRing R] (stokesConst empP empM : R)
    (hMatchP : stokesConst = empP)
    (hMatchM : stokesConst = empM)
    (hSwing : empP ≠ empM) : False := by
  exact hSwing (hMatchP ▸ hMatchM)

/-- **Miss-by-the-full-swing form (sorry-free).** A constant Stokes datum pinned
to the empirical `c_3` at the proton anchor misses the muon anchor by exactly the
full cross-anchor swing `empP - empM`. -/
theorem constantStokesDatum_misses_other_anchor_by_full_swing {R : Type*}
    [Field R] [LinearOrder R] [IsStrictOrderedRing R] (stokesConst empP empM : R)
    (hMatchP : stokesConst = empP) :
    stokesConst - empM = empP - empM := by
  rw [hMatchP]

/-! ### (2) The open target — a NORMALIZED Stokes datum (conjecture, no instance)

The GGM-Stokes route is not closed by a bare integer. The open form is that a
**normalized** anchor-invariant Stokes datum equals the smooth bar-odd `c_3`
object, via a fixed-basis §4e quantum-modularity normalization. We record it as a
content-bearing primary conjecture class with no instance. -/

/-- Substrate datum for the GGM-Stokes `c_3` bridge: the anchor-invariant raw
Stokes datum `stokesDatum` (the certified integer `-3` / `S⁺₁₁` tower value), the
smooth bar-odd `c_3` object `smoothC3` it must map onto, and the (open)
normalization scalar `norm` from the fixed §4e basis. Data — asserts nothing. -/
structure StokesBridgeDatum (R : Type*) [Field R] [LinearOrder R] [IsStrictOrderedRing R] where
  /-- The anchor-invariant raw GGM Stokes datum (`-3` / the `S⁺₁₁` tower). -/
  stokesDatum : R
  /-- The smooth bar-odd `c_3` object the datum must be normalized onto. -/
  smoothC3 : R
  /-- The open §4e quantum-modularity / 3d-index normalization scalar. -/
  norm : R

/-- **§3b primary conjecture class — the normalized GGM-Stokes `c_3` bridge.**

    `@conjecture: primary`

    The honest OPEN target of the GGM colored-Jones / resurgence route. It asserts
    that a **normalized** anchor-invariant Stokes datum reproduces the smooth
    bar-odd `c_3` object — `norm * stokesDatum = smoothC3` — with the bridge
    **nontrivial** (`norm ≠ 1`), i.e. the bare Stokes integer is NOT already `c_3`
    (`stokesInt_strictly_worse_c3_than_nearMatch` above shows `-3` is a strictly
    worse `c_3` than `-2`, so `norm = 1` is excluded). The content is the existence
    of the fixed §4e normalization taking the certified integer datum to the
    observable coefficient; **no instance is supplied** — the honest open state
    (per KC22 the bar-odd object is resurgent/transcendental, so `norm` is not a
    low-order (q-)holonomic scalar to be read off). -/
-- Ref: [garoufalidis-gu-marino2021] https://arxiv.org/abs/2011.07617
-- Ref: [manuscript] conj:binding-qbeta-complex; conj:qdifference-kernel-prolongation-symbol;
--      docs/coordination/ck-dk-canonical-registry.md §9;
--      docs/audits/2026-07-20-c3-stokes-route.md
class NormalizedStokesC3Bridge {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (d : StokesBridgeDatum R) : Prop where
  /-- The normalized Stokes datum reproduces the smooth bar-odd `c_3` object:
      `norm * stokesDatum = smoothC3`. The content of the conjecture — the §4e
      normalization is the whole open problem. -/
  normalized_stokes_is_smoothC3 : d.norm * d.stokesDatum = d.smoothC3
  /-- The bridge is nontrivial: the bare Stokes integer is not already `c_3`
      (`norm ≠ 1`), consistent with `-3` being a strictly worse `c_3` than `-2`. -/
  bridge_nontrivial : d.norm ≠ 1
  /-- There IS a bar-odd channel to derive — the decay-face object is nonzero. -/
  smoothC3_nonzero : d.smoothC3 ≠ 0

end QOU.Mass.QbetaC3Stokes
