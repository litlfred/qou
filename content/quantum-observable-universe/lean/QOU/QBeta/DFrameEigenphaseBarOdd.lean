/-
  # The convention-D ladder eigenphase: bar-oddness pins it, uniquely

  Bean `qou-cds1` (tranche S1 of the 2026-08-15 convention-D ruling).
  Companion probe `computations/qbeta/qbeta_d_frame_eigenphase_window_probe.py`
  (exact `sympy` §1 mirrors every identity below).

  ## The problem this solves

  The Q_β precision ladder carries the single-wrap eigenphase
  `α = (z − 1)·h/2` (`QOU.BraidKnot.alpha`, doubled here as `(z−1)·h` so the
  parity bookkeeping needs no division). Every bar-parity statement downstream
  of it — (H1) `c₃^even = −Vol(4₁)`, the `S_leak` program, `q*_S`, the KC13
  prune — rests on `α` being bar-**ODD**.

  Under convention C that holds, because `z_C` is bar-EVEN
  (`QOU.QBeta.z_bar_invariant`) and
  `QOU.QBeta.eigenphase_barOdd_of_barEven` then gives bar-oddness.

  Under convention D it **fails**. `z_D = q³/(q²+1)` satisfies the full-bar
  condition `bar(z) = z − h` (`QOU.QBeta.zD_full_bar_covariant`), and
  `QOU.QBeta.eigenphase_bar_defect_of_fullBar` shows the bar defect is then
  exactly `h²` — the same for every parameter in that family. So one cannot
  reach a bar-odd D-frame phase by choosing a different full-bar `z`.

  ## What is proved here

  The defect can instead be removed by SHIFTING the parameter, and the shift is
  **forced**. Only an `h`-proportional shift can change a bar parity at all (a
  bar-even shift is invisible to the involution), so consider

      α_t := (z + t·h − 1)·h/2,   t a bar-even scalar.

  * `shiftedPhase_bar_defect` — the defect is `(2t + 1)·h²`. The proof consumes
    `bar(z) = z − h` and **nothing else**: `z` does not appear in the result.
    So this is a statement about the whole full-bar family, not about `z_D`.
  * `naivePhase_not_barOdd` — at `t = 0` (the bare substitution) the defect is
    `h² ≠ 0`. This is the parity half of why the C→D move is not a `z`-swap:
    `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` blocks it from the
    Temperley–Lieb side, and this blocks it from the bar-parity side.
  * `barOdd_shift_unique` — bar-oddness holds **iff `t = −1/2`**, uniquely.
  * `zD_sub_halfH_eq` / `zD_even_barEven` — the surviving parameter has the
    closed form `z_D − h/2 = (q⁴+1) / (2q(q²+1))`, and it is bar-even.
  * `barOddPhase_eq_moment_form` — that parameter is exactly the
    weight-determined half of the Markov parameter: combining with
    `QOU.QBeta.loopMean_eq_twoQ_mul_moment` (`2z − h = [2]_q·Ξ`, valid in ANY
    convention) the unique bar-odd phase is `([2]_q·Ξ − 2)·h/2`.

  So the D-frame bar-odd eigenphase is **derived**, carries no free parameter,
  and is built from the convention-D Wedderburn weights together with the `h`
  that `QOU.QBeta.MarkovWeightsConventionD` already names as the permitted
  bar-odd source.

  ## What this does NOT establish

  * It does **not** contradict
    `QOU.QBeta.LadderPhaseFromWeights.no_weight_function_gives_phase`, which
    excludes the weights determining the FULL `α`. The bar-odd **projection**
    is a strictly weaker object, and it is that projection which is pinned here.
  * It does **not** derive the ladder's *shape* — that `α` enters as
    `cos(α − u/2)`, or that the rungs are `(1 + c_k u^k)`, is asserted upstream
    in both frames and is untouched.
  * It supplies **no `c_k` value, tier, or wiring change**. Measured, the
    resulting ladder gives an implied `c₂ = −1.733` against the structural
    `−1` — an 11× improvement on the bare substitution's `−9.299`, and a
    restoration of rung convergence (`|r₂/r₁| = 0.423 < 1` against `0.893`),
    but **not** a closure. That negative is scope-(a) per AGENTS.md
    §"Before declaring refuted": this construction alone does not reproduce
    the band; no proved invariant excludes the ladder shape.

  Base ring (§7c): `CommRing` for the division-free parity algebra; the
  uniqueness and the closed form need inverses and so take `[Field F]`, with
  `(2 : F) ≠ 0` carried as an explicit hypothesis rather than assumed. Nothing
  archimedean — no ordering, no `Real.sqrt` — so the substrate→archimedean wall
  is not crossed.

  -- Ref: [manuscript] bean `qou-cds1`; `docs/audits/2026-08-25-qbeta-ck-ladder-convention-d-eigenphase-window.md`
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.QBeta.DFrameEigenphaseBarOdd

/-! ## §1. The shifted phase and its bar defect -/

variable {R : Type*} [CommRing R]

/-- **The bar defect of the shifted eigenphase is `(2t + 1)·h²`.**

    With the parameter shifted to `z + t·h` (`t` bar-even), the doubled phase is
    `2α_t = (z + t·h − 1)·h`, whose bar-image is `(bar z + t·bar h − 1)·bar h`.
    Feeding the full-bar condition `bar z = z − h` and `bar h = −h`:

        bar(2α_t) + 2α_t = (2t + 1)·h².

    Two things about the right-hand side carry the content. It does not mention
    `z` — so the defect is a property of the *whole* full-bar family, and no
    choice of parameter within that family can change it. And it is not
    identically zero — so bar-oddness is a genuine constraint on `t`. -/
theorem shiftedPhase_bar_defect (z zbar hk hkbar t : R)
    (hfull : zbar = z - hk) (hh : hkbar = -hk) :
    (zbar + t * hkbar - 1) * hkbar + (z + t * hk - 1) * hk = (2 * t + 1) * hk ^ 2 := by
  subst hfull; subst hh; ring

/-- **The bare substitution is never bar-odd.**  At `t = 0` — that is, using
    `z_D` itself in the C-frame formula — the defect is `h²`, which is nonzero
    away from the classical point.  Together with
    `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (which blocks the same move from
    the Temperley–Lieb side) this is why the convention change is a
    re-derivation and not a `z`-swap. -/
theorem naivePhase_not_barOdd {F : Type*} [Field F] (z zbar hk hkbar : F)
    (hfull : zbar = z - hk) (hh : hkbar = -hk) (hk0 : hk ≠ 0) :
    (zbar - 1) * hkbar + (z - 1) * hk ≠ 0 := by
  have hd : (zbar - 1) * hkbar + (z - 1) * hk = hk ^ 2 := by
    subst hfull; subst hh; ring
  rw [hd]
  exact pow_ne_zero 2 hk0

/-! ## §2. Uniqueness of the bar-odd shift -/

variable {F : Type*} [Field F]

/-- `2·(−1/2) + 1 = 0`, given that `2` is invertible.  Factored out because both
    directions of `barOdd_shift_unique` need it, and because it is exactly the
    place the argument would fail in characteristic 2 — where `−1/2` is not a
    scalar at all and the bar-odd shift does not exist. -/
private lemma two_mul_negHalf_add_one (h2 : (2 : F) ≠ 0) :
    (2 : F) * -(1 / 2) + 1 = 0 := by
  have hinv : (2 : F) * (2 : F)⁻¹ = 1 := mul_inv_cancel₀ h2
  rw [one_div]
  linear_combination -hinv

/-- **Bar-oddness holds iff `t = −1/2`.**  The shift that restores the parity
    every downstream consumer assumes is unique, and it is a pure number: no
    dependence on `q`, on the anchor, or on which full-bar parameter one
    started from.  This is the pruning step — the hypothesis class of D-frame
    eigenphases `α_t` collapses to a single member before any number is
    computed. -/
theorem barOdd_shift_unique (z zbar hk hkbar t : F)
    (hfull : zbar = z - hk) (hh : hkbar = -hk) (hk0 : hk ≠ 0) (h2 : (2 : F) ≠ 0) :
    (zbar + t * hkbar - 1) * hkbar + (z + t * hk - 1) * hk = 0 ↔ t = -(1 / 2) := by
  rw [shiftedPhase_bar_defect z zbar hk hkbar t hfull hh]
  constructor
  · intro hzero
    have h1 : 2 * t + 1 = 0 := by
      rcases mul_eq_zero.mp hzero with h | h
      · exact h
      · exact absurd (pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h) hk0
    field_simp
    linear_combination h1
  · intro ht
    subst ht
    rw [two_mul_negHalf_add_one h2, zero_mul]

/-- **The unique bar-odd parameter is `z − h/2`.**  Restating
    `barOdd_shift_unique` in terms of the parameter rather than the shift: the
    surviving member of the family is the bar-EVEN projection of `z`. -/
theorem barOdd_parameter_eq (z zbar hk hkbar : F)
    (hfull : zbar = z - hk) (hh : hkbar = -hk) (h2 : (2 : F) ≠ 0) :
    (zbar + (-(1 / 2) : F) * hkbar - 1) * hkbar + (z + (-(1 / 2) : F) * hk - 1) * hk = 0 := by
  rw [shiftedPhase_bar_defect z zbar hk hkbar _ hfull hh,
      two_mul_negHalf_add_one h2, zero_mul]

/-! ## §3. The convention-D parameter's bar-even projection, in closed form -/

/-- **`z_D − h/2 = (q⁴ + 1) / (2q(q² + 1))`.**  The closed form of the unique
    bar-odd parameter under convention D.  Stated over a field with the two
    nonvanishing hypotheses made explicit. -/
theorem zD_sub_halfH_eq (q : F) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : F) ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) / 2 = (q ^ 4 + 1) / (2 * q * (q ^ 2 + 1)) := by
  field_simp
  ring

/-- **`z_D − h/2` is bar-EVEN**, division-free: with `q⁻¹` carried as `qi`
    (`q·qi = 1`), the cross-multiplied form of
    `(qi⁴+1)/(2·qi·(qi²+1)) = (q⁴+1)/(2·q·(q²+1))`.

    This is what makes the shifted parameter a legitimate eigenphase source:
    a bar-even parameter yields a bar-odd phase by
    `QOU.QBeta.eigenphase_barOdd_of_barEven`, which is exactly the property the
    C frame had for free and the naive D substitution loses. -/
theorem zD_even_barEven (q qi : R) (h : q * qi = 1) :
    (qi ^ 4 + 1) * (2 * q * (q ^ 2 + 1)) = (q ^ 4 + 1) * (2 * qi * (qi ^ 2 + 1)) := by
  linear_combination (-2 * (q - qi) *
      (q ^ 2 * qi ^ 2 + q ^ 2 + 2 * q * qi + qi ^ 2 + 1)) * h

/-! ## §4. The bar-odd phase in terms of the Wedderburn weights -/

/-- **The unique bar-odd eigenphase is `([2]_q·Ξ − 2)·h/2`.**

    `QOU.QBeta.loopMean_eq_twoQ_mul_moment` gives `2z − h = [2]_q·Ξ` in ANY
    convention, with `Ξ = Σ_λ χ^λ(τ)·y_λ` the transposition moment of the
    Wedderburn weights (n-independent, and bar-even under D because every
    convention-D weight is — `markovWeightsD_y21_barEven`).

    Combining with §2: the bar-even half of the Markov parameter is `[2]_q·Ξ/2`
    and its bar-odd half is the universal `h/2`.  So the bar-odd projection of
    the eigenphase is determined by the weights, even though — per
    `no_weight_function_gives_phase` — the full phase is not.

    Stated division-free in the doubled phase: `2·α^odd = (2z − h − 2)·h/2 · 2`,
    i.e. `(2z − h − 2)·h`, so no inverse of `2` is needed and the identity holds
    over any `CommRing`.

    This is the sense in which the D-frame eigenphase is RE-DERIVED rather than
    substituted: its bar-even multiplier comes from the D weights, and its
    bar-odd factor is the `h` those weights cannot supply. -/
theorem barOddPhase_eq_moment_form (z hk twoQ Xi : R)
    (hmom : 2 * z - hk = twoQ * Xi) :
    (2 * z - hk - 2) * hk = (twoQ * Xi - 2) * hk := by
  linear_combination hk * hmom

end QOU.QBeta.DFrameEigenphaseBarOdd
