/-
  The full-bar covariance condition on the Markov parameter, and the decay
  ladder's `z_C` escape from the Temperley–Lieb forcing (bean `qou-b3nk`).

  Companion to
    computations/markov_z_full_bar_condition_probe.py        (sympy exact, 2026-08-08)
    computations/qbeta/qbeta_decay_channel_convention_status_probe.py
    docs/audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md

  Context.  Markov axiom M3, `tr(x·σ_n) = z·tr(x)`, contains `σ_n`, which the
  bar involution (q ↦ q⁻¹, σ ↦ σ⁻¹) inverts.  Since `σ⁻¹ = σ − h` exactly
  (`h = q − q⁻¹`, from the Hecke quadratic), the negative-stabilisation
  parameter is `z₋ = z − h`, and a Markov trace that commutes with the FULL
  bar involution (`tr ∘ bar = bar ∘ tr`) must have

      bar(z) = z − h.                                        (full-bar condition)

  The sympy probe (witness `markov-z-full-bar-condition.witness.json`) verified:
  convention D (`z_D = q³/(q²+1)`) satisfies it — indeed the whole integer-rank
  fibre family `z_N = q^N/[N]_q` does, symbolically in `N` — while convention C
  (`z_C = 1/(q^{1/2}+q^{-1/2})`, bar-EVEN by `QOU.QBeta.z_bar_invariant`) fails
  it whenever `q² ≠ 1`.  `QOU.Hecke.MarkovTraceOnH3A` records the condition in
  prose ("a condition this class has no field for") but nothing in Lean carried
  it.  This file formalises the z-level algebra, sorry-free:

  * `zD_full_bar_covariant` — `bar(z_D) = z_D − h`, division-free over any
    `CommRing` (cross-multiplied, `q⁻¹` carried as `qi` with `q·qi = 1`).
  * `barEven_fullBar_forces_classical` — a bar-EVEN parameter satisfies the
    full-bar condition only at `q² = 1`.  Applied to `z_C` (bar-even, proved in
    `ZBarParity`): convention C fails the full-bar condition away from the
    classical point.
  * `zC_fails_fullBar` — the `z_C`-specific field form on the substrate side
    (`s = √q > 1`), consuming `z_bar_invariant_field`.
  * `decayLadder_zC_not_jones` — for `s > 1` the decay ladder's parameter
    fails the Jones/TL pin: `z_C·([2]_q) ≠ q²`.
  * `decayLadder_zC_threeRow_ne_zero` — composite with
    `QOU.BraidsAndKnots.threeRow_ne_zero_of_ocneanu_ne`: ANY faithful
    normalised Markov trace on `H₃(q)` at the decay ladder's parameter `z_C`
    carries a NONZERO three-row weight `y_(1³)`.  So "keep the C-frame ladder"
    and "the two-row (mass-channel) forcing applies to the decay channel" are
    mutually exclusive: if the decay channel's decomposition kills the third
    row, its trace parameter is `z_D` and the existing ladder is not that
    trace; as long as the ladder keeps `z_C`, its trace does not factor
    through Temperley–Lieb.

  What this does NOT establish (conditional-proved ≠ premise-established):
  * that the decay channel's trace MUST be bar-compatible — `tr∘bar = bar∘tr`
    is the premise under which the full-bar condition excludes C; it is the
    standard Ocneanu-trace property and is what the decay channel's own
    bar-parity bookkeeping (KC13/KC18/KC19, bar-even/bar-odd splits) reads
    into the algebra, but it is asserted context, not proved here;
  * which fibre the decay functor lands in — no decay analogue of
    `lem:feynman-eigenbasis-decomposition` exists in the corpus;
  * any `c_k` value, tier, or wiring change.  The Q_β channel registration
    stays `disputed` (trace-convention registry, bean `qou-b3nk`).

  Base ring (§7c): `CommRing` for the division-free identities; the ordered
  statements (`s > 1`, substrate side of the wall) use
  `[Field F] [LinearOrder F] [IsStrictOrderedRing F]`.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import QOU.QBeta.ZBarParity
import QOU.BraidsAndKnots.MarkovTraceTLUniqueness

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-! ## §1. Convention D satisfies the full-bar condition `bar(z) = z − h` -/

/-- **`bar(z_D) = z_D − h`, division-free.**  With `q⁻¹` carried as `qi`
(`q·qi = 1`), the cross-multiplied form of
`qi³/(qi²+1) = q³/(q²+1) − (q − qi)`:  both sides equal `1/(q³+q)` as
fractions, and the identity below is their denominator-cleared form.  This is
the z-level content of "convention D's Markov trace commutes with the full bar
involution at the stabilisation step" — the trace-level premise
(`tr∘bar = bar∘tr`) is NOT proved here. -/
theorem zD_full_bar_covariant (q qi : R) (h : q * qi = 1) :
    qi ^ 3 * (q ^ 2 + 1) = (q ^ 3 - (q - qi) * (q ^ 2 + 1)) * (qi ^ 2 + 1) := by
  linear_combination (qi - q) * h

/-- **A bar-EVEN Markov parameter satisfies the full-bar condition only at the
classical point.**  If `bar(z) = z` (convention C's property, proved for
`z_C = √q/(1+q)` in `ZBarParity.z_bar_invariant`) and `bar(z) = z − (q − qi)`
(the full-bar condition), then `q² = 1`.  Contrapositive: away from `q² = 1`,
convention C fails the full-bar condition — the exact reverse of the
coefficient-half verdict that had been read as favouring C. -/
theorem barEven_fullBar_forces_classical (q qi z zbar : R) (hqi : q * qi = 1)
    (heven : zbar = z) (hfull : zbar = z - (q - qi)) : q ^ 2 = 1 := by
  linear_combination hqi + q * hfull - q * heven

/-! ## §1b. The ladder eigenphase inherits the parameter's bar parity

The Q_β precision ladder's `N = 1` factor is `cos(α − b·ℏ_q²/2)` with the
single-wrap eigenphase `α = (z − 1)·h/2`
(`QOU.BraidKnot.QBetaCategoricalPrecisionLadder.alpha`).  Every bar-parity
statement in the `c_k` record — (H1) `c₃^even = −Vol(4₁)`, the `S_leak`
program, `q*_S`, the KC13 prune — rests downstream of
`eigenphase_bar_involution`, i.e. on `α` being bar-ODD.

The two results below say that bar-oddness of `α` is *exactly* bar-evenness of
`z`, and compute the defect when it fails.  They are stated in the doubled
variable `2α = (z − 1)·h` so they stay division-free over any `CommRing`.

Consequence for the convention ruling (bean `qou-cds1`).  `z_C` is bar-even
(`ZBarParity.z_bar_invariant`), so `α` is bar-odd and
`eigenphase_bar_involution` holds — **as a convention-C statement**.  `z_D`
satisfies the full-bar condition instead (`zD_full_bar_covariant`), so under
convention D the eigenphase is *not* bar-odd: its defect is exactly `h²`, i.e.
`h²/2` on the undoubled `α`.  This is a structural reason the C→D move cannot
be a z-substitution: swapping `z` into the C-frame `α` keeps the formula while
breaking the bar parity the formula's downstream consumers assume. -/

/-- **Bar-even parameter ⟹ bar-ODD eigenphase.**  With `bar(h) = −h` (immediate
from `h = q − q⁻¹`), a bar-even `z` makes `2α = (z−1)h` bar-odd:
`bar(2α) + 2α = 0`.  This is the convention-C case, and it is the hypothesis
`eigenphase_bar_involution` encodes. -/
theorem eigenphase_barOdd_of_barEven (hk z zbar hbar : R)
    (heven : zbar = z) (hh : hbar = -hk) :
    (zbar - 1) * hbar + (z - 1) * hk = 0 := by
  subst heven; subst hh; ring

/-- **Full-bar parameter ⟹ eigenphase bar defect exactly `h²`.**  If instead
`bar(z) = z − h` (the full-bar condition, which `z_D` satisfies and a bar-even
`z` cannot away from `q² = 1` — `barEven_fullBar_forces_classical`), then
`bar(2α) + 2α = h²` rather than `0`.

So the failure is not a perturbation to be estimated: it is an exact,
`z`-independent remainder.  Every parameter satisfying the full-bar condition
has the SAME defect, so no choice within that family restores bar-oddness. The
bar-odd projection of the D-frame eigenphase is therefore `α − h²/4`
(undoubled), which is a derived correction carrying no free parameter. -/
theorem eigenphase_bar_defect_of_fullBar (hk z zbar hbar : R)
    (hfull : zbar = z - hk) (hh : hbar = -hk) :
    (zbar - 1) * hbar + (z - 1) * hk = hk ^ 2 := by
  subst hfull; subst hh; ring

section Ordered

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- **`z_C` fails the full-bar condition on the substrate side.**  In the
half-power coordinate `s = √q` with `s > 1` (every substrate anchor has
`q > 1`):  `bar(z_C) ≠ z_C − h`, written out with `bar` acting as `s ↦ s⁻¹`
and `h = q − q⁻¹ = s² − s⁻²`.  Uses `z_bar_invariant_field` (bar-evenness of
`z_C`); the failure is then exactly `h ≠ 0`. -/
theorem zC_fails_fullBar (s : F) (hs : 1 < s) :
    s⁻¹ / (1 + s⁻¹ ^ 2) ≠ s / (1 + s ^ 2) - (s ^ 2 - s⁻¹ ^ 2) := by
  have hs0 : (0 : F) < s := lt_trans one_pos hs
  have hsne : s ≠ 0 := ne_of_gt hs0
  rw [z_bar_invariant_field s hsne]
  intro hcontra
  have hx : s ^ 2 = s⁻¹ ^ 2 := by linarith
  have hinv : s * s⁻¹ = 1 := mul_inv_cancel₀ hsne
  have h4 : s ^ 4 = 1 := by
    calc s ^ 4 = s ^ 2 * s ^ 2 := by ring
      _ = s ^ 2 * s⁻¹ ^ 2 := by rw [← hx]
      _ = (s * s⁻¹) ^ 2 := by ring
      _ = 1 := by rw [hinv, one_pow]
  have h2 : 1 < s ^ 2 := by nlinarith
  have hlt : 1 < s ^ 4 := by nlinarith
  rw [h4] at hlt
  exact lt_irrefl 1 hlt

/-- **The decay ladder's parameter fails the Jones/TL pin.**  For `s > 1`, a
parameter `z` with `z·(s + s⁻¹) = 1` (i.e. `z = z_C = 1/(√q + 1/√q)`, the
value hard-coded in `qbeta_utils.markov_parameter` and the KC21/KC22 ladder
core) does NOT satisfy `z·[2]_q = q²` (`q = s²`).  Denominator-cleared, the
coincidence locus is `s⁷ + s⁵ = s⁴ + 1`, which is impossible for `s > 1`
(each `s > 1` has `s⁷ > s⁴` and `s⁵ > 1`). -/
theorem decayLadder_zC_not_jones (s z : F) (hs : 1 < s)
    (hz : z * (s + s⁻¹) = 1) :
    z * (s ^ 2 + s⁻¹ ^ 2) ≠ (s ^ 2) ^ 2 := by
  have hs0 : (0 : F) < s := lt_trans one_pos hs
  have hsne : s ≠ 0 := ne_of_gt hs0
  have hinv : s * s⁻¹ = 1 := mul_inv_cancel₀ hsne
  intro hcontra
  -- Multiply the coincidence by `(s + s⁻¹)` and use `hz` to eliminate `z`.
  have h1 : s ^ 2 + s⁻¹ ^ 2 = s ^ 4 * (s + s⁻¹) := by
    have hmul : z * (s + s⁻¹) * (s ^ 2 + s⁻¹ ^ 2) = s ^ 4 * (s + s⁻¹) := by
      calc z * (s + s⁻¹) * (s ^ 2 + s⁻¹ ^ 2)
          = (z * (s ^ 2 + s⁻¹ ^ 2)) * (s + s⁻¹) := by ring
        _ = (s ^ 2) ^ 2 * (s + s⁻¹) := by rw [hcontra]
        _ = s ^ 4 * (s + s⁻¹) := by ring
    rw [hz, one_mul] at hmul
    exact hmul
  -- Clear the residual inverses: the coincidence locus is `s⁴ + 1 = s⁷ + s⁵`.
  have h3 : s ^ 4 + 1 = s ^ 7 + s ^ 5 := by
    linear_combination s ^ 2 * h1 + (s ^ 5 - 1 - s * s⁻¹) * hinv
  -- Impossible for `s > 1`.
  have h2 : 1 < s ^ 2 := by nlinarith
  have h3' : 1 < s ^ 3 := by nlinarith
  have h5' : 1 < s ^ 5 := by nlinarith
  have h7' : s ^ 4 < s ^ 7 := by nlinarith [mul_pos (pow_pos hs0 4) (sub_pos.mpr h3')]
  linarith

/-- **Mutual exclusivity: the C-frame decay ladder and the two-row forcing.**
ANY faithful normalised Markov trace on `H₃(q)` (the three Markov equations
against the `H₃(q)` character table, `y_(2,1) ≠ 0`) whose Ocneanu parameter is
the decay ladder's `z_C` (`z·(s + s⁻¹) = 1`, `q = s²`, `s > 1`) carries a
NONZERO three-row weight `y_(1³)` — it does not factor through Temperley–Lieb.

Consequence for bean `qou-b3nk`: the mass channel's forcing
(`y_(1³) = 0 ⟹ z = z_D`, `markovWeights_eq_jones_of_threeRow_eq_zero`) cannot
"transfer" to the Q_β channel while the ladder keeps `z_C` — if the decay
decomposition kills the third row, the decay trace is `z_D` and the existing
C-frame ladder is not that trace (re-derivation, not substitution); if the
ladder's parameter is retained, the third row is forcibly present.  Which horn
is the decay channel's is NOT decided here: no corpus block derives the decay
fibre, and the channel is registered `disputed`. -/
theorem decayLadder_zC_threeRow_ne_zero (s z y₃ y₂₁ y₁₃ : F) (hs : 1 < s)
    (hz : z * (s + s⁻¹) = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : s ^ 2 * y₃ + (s ^ 2 - s⁻¹ ^ 2) * y₂₁ + (-(s⁻¹ ^ 2)) * y₁₃ = z)
    (hsigmasigma :
      (s ^ 2) ^ 2 * y₃ + (-1) * y₂₁ + (s⁻¹ ^ 2) ^ 2 * y₁₃ = z ^ 2)
    (hfaith : y₂₁ ≠ 0) : y₁₃ ≠ 0 := by
  have hs0 : (0 : F) < s := lt_trans one_pos hs
  have hsne : s ≠ 0 := ne_of_gt hs0
  have hqqi : s ^ 2 * s⁻¹ ^ 2 = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hsne, one_pow]
  exact QOU.BraidsAndKnots.threeRow_ne_zero_of_ocneanu_ne
    (s ^ 2) (s⁻¹ ^ 2) z y₃ y₂₁ y₁₃ hqqi hnorm hsigma hsigmasigma hfaith
    (decayLadder_zC_not_jones s z hs hz)

end Ordered

end QOU.QBeta
