/-
  The convention-D `H₃(q)` Markov weights: two-row, and both bar-EVEN.

  Companion to
    computations/qbeta/qbeta_d_frame_markov_weights_probe.py
    QOU.QBeta.MarkovZFullBarCondition        (the z-level bar algebra)
    QOU.QBeta.WenzlWeightVanishing           (the all-`n` vanishing lemma)

  Step 2 of bean `qou-cds1` (S1: re-derive the Q_β `c_k` ladder under
  convention D). Step 1 established that the ladder eigenphase
  `α = (z − 1)h/2` is bar-ODD exactly when `z` is bar-even, so
  `eigenphase_bar_involution` is a convention-C statement and under D the
  eigenphase carries an exact defect `h²/2`
  (`MarkovZFullBarCondition.eigenphase_bar_defect_of_fullBar`). The bar-odd
  projection `α − h²/4` is forced but measured insufficient. This file asks
  what bar-odd material the D-frame trace has left to build a phase from.

  Answer: none in the weights.

  Solving the three `H₃(q)` Markov equations at `z_D` (`z(q²+1) = q³`) gives

      y_(1³) = 0,   y_(2,1) = q²/(q²+1)²,   y_(3) = (q⁴+1)/(q²+1)²

  and BOTH surviving weights are bar-even (`bar(y) = y` under `q ↦ q⁻¹`).
  The `y_(1³) = 0` here is an independent re-derivation of the two-row cap
  from the Markov side — it drops out of the linear system at `z_D` rather
  than being imported from Wenzl's theorem, so the two routes corroborate
  each other.

  CONSEQUENCE FOR THE LADDER (this is the prune). The C-frame ladder's
  bar-odd content comes from `α` being bar-odd, which comes from `z_C` being
  bar-even against a bar-ODD `h`. Under D the surviving Markov data is
  bar-even throughout, so no quantity built from the D-frame weights alone
  carries a bar-odd part. A D-frame ladder phase with the C-frame's bar
  parity cannot be assembled from the weights; it must come from elsewhere
  (the `h` factor, the Kashiwara `f̃₁` shift, or the framing) or not exist.
  This says where a re-derivation must NOT look; it does not supply one.

  What this does NOT establish:
  * any `c_k` value, tier, or wiring change — the Q_β channel registration
    stays `disputed` (trace-convention registry, bean `qou-b3nk`);
  * that the decay channel's trace IS the D one — that is the owner ruling
    (2026-08-15 R1), not a result proved here;
  * uniqueness of the weights as a Lean theorem. What is proved below is
    that the stated triple SATISFIES the three Markov equations at `z_D`.
    Uniqueness is a 3×3 linear solve, verified symbolically in the
    companion probe (sympy `solve`, general `z`, then specialised); the
    Lean carries the verification direction only, and says so rather than
    overstating.

  Base ring (§7c): everything here is a polynomial identity over a generic
  `CommRing` — the equations are stated denominator-cleared, so no ordering,
  no `Real.sqrt`, and no field structure is needed.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-! ## The weights, denominator-cleared

Writing `W = (q²+1)²` for the common denominator, the convention-D weights are
carried as their numerators: `Y₃ = q⁴+1`, `Y₂₁ = q²`, `Y₁₃ = 0`, with the
Markov parameter as `Z = q³` over `q²+1`. Every statement below is the
cross-multiplied form, so it holds over any `CommRing`. -/

/-- **Normalisation.** `y_(3) + 2·y_(2,1) + y_(1³) = 1`, cleared: the three
numerators sum to `W = (q²+1)²`. Note `y_(1³)` contributes nothing — the
two-row weights alone already saturate the normalisation. -/
theorem markovWeightsD_norm (q : R) :
    (q ^ 4 + 1) + 2 * q ^ 2 + 0 = (q ^ 2 + 1) ^ 2 := by ring

/-- **First Markov equation** (`tr(σ) = z`), cleared by `W`.  With
`h = q − q⁻¹` the `q⁻¹` cancels: `(q − q⁻¹)·q² = q³ − q`, so the identity is
polynomial. Right-hand side is `z_D·W = q³(q²+1)`. -/
theorem markovWeightsD_sigma (q : R) :
    q * (q ^ 4 + 1) + (q ^ 3 - q) + 0 = q ^ 3 * (q ^ 2 + 1) := by ring

/-- **Second Markov equation** (`tr(σ²) = z²`), cleared by `W`.  The
`y_(2,1)` eigenvalue is `−1` and `y_(1³)` drops, leaving `q⁶ = (z_D·W)²/W`. -/
theorem markovWeightsD_sigmasq (q : R) :
    q ^ 2 * (q ^ 4 + 1) - q ^ 2 + 0 = q ^ 6 := by ring

/-- **`z_D` squared is consistent with the cleared right-hand side above.**
`(z·(q²+1))² = (q³)²` expands to `z²·W = q⁶`, matching
`markovWeightsD_sigmasq`. -/
theorem markovWeightsD_zsq (q z : R) (hz : z * (q ^ 2 + 1) = q ^ 3) :
    z ^ 2 * (q ^ 2 + 1) ^ 2 = q ^ 6 := by
  linear_combination (z * (q ^ 2 + 1) + q ^ 3) * hz

/-! ## Bar parity of the surviving weights

`bar` sends `q ↦ q⁻¹`. Carrying `q⁻¹` as `qi` with `q·qi = 1`, a weight
`Y/W` is bar-even iff `bar(Y)·W = Y·bar(W)`, which is the form proved below.
Both surviving weights are bar-EVEN — there is no bar-odd part anywhere in
the D-frame weight data. -/

/-- **`y_(2,1)` is bar-EVEN.**  `bar(q²/(q²+1)²) = q²/(q²+1)²`, in the
cross-multiplied form `qi²·(qi²+1)⁻¹`-free: `qi² · (q²+1)² = q² · (qi²+1)²`. -/
theorem markovWeightsD_y21_barEven (q qi : R) (h : q * qi = 1) :
    qi ^ 2 * (q ^ 2 + 1) ^ 2 = q ^ 2 * (qi ^ 2 + 1) ^ 2 := by
  -- With `t = q·qi`, the difference is `(q² − qi²)(t² − 1) = (q² − qi²)(t−1)(t+1)`,
  -- so the certificate is `(q² − qi²)(t+1)` against `h : t − 1 = 0`.
  linear_combination (q ^ 2 - qi ^ 2) * (q * qi + 1) * h

/-- **`y_(3)` is bar-EVEN.**  `bar((q⁴+1)/(q²+1)²) = (q⁴+1)/(q²+1)²`, i.e.
`(qi⁴+1)·(q²+1)² = (q⁴+1)·(qi²+1)²`. -/
theorem markovWeightsD_y3_barEven (q qi : R) (h : q * qi = 1) :
    (qi ^ 4 + 1) * (q ^ 2 + 1) ^ 2 = (q ^ 4 + 1) * (qi ^ 2 + 1) ^ 2 := by
  -- Same shape as `y21`, doubled: the difference is `2(qi² − q²)(t² − 1)`.
  linear_combination 2 * (qi ^ 2 - q ^ 2) * (q * qi + 1) * h

/-- **The prune, as a statement about what is available.**  Every D-frame
weight is bar-even (the two above; the third is `0`, which is bar-even
trivially). So any `R`-linear combination of the D-frame weights is bar-even,
and in particular no such combination supplies the bar-ODD eigenphase the
C-frame ladder uses.

Stated as: if `f` is built from the weights by a map that commutes with
`bar` — here, any linear combination with bar-even coefficients — then `f` is
bar-even. The content is the two lemmas above; this records the conclusion
they are for. -/
theorem markovWeightsD_barEven_combination (a b abar bbar Y₃ Y₂₁ Y₃bar Y₂₁bar : R)
    (ha : abar = a) (hb : bbar = b)
    (h3 : Y₃bar = Y₃) (h21 : Y₂₁bar = Y₂₁) :
    abar * Y₃bar + bbar * Y₂₁bar = a * Y₃ + b * Y₂₁ := by
  subst ha; subst hb; subst h3; subst h21; ring

end QOU.QBeta
