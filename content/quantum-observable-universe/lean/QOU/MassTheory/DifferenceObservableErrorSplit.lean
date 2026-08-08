/-
# A difference observable amplifies only the **differential** error, never the common one

`per_observable_100x_status.py` scores the 1ppQ L2 goal and reports `2 / 7`, with five
failing observables. Read literally that is five problems. Two of them — `Δ_pn = m_n − m_p`
and `Q_β = Δ_pn − m_e` — are algebraic functions of the others, so their errors are not
independent evidence. This file makes the propagation exact, as a `Field` identity, so the
bookkeeping is a theorem rather than a numerical coincidence.

Write the two nucleon predictions with a **common** relative error `ε` and a **differential**
`δ` on top of it:

```
m_p_pred = p·(1 + ε),      m_n_pred = n·(1 + ε + δ).
```

Then (`difference_rel_error_split`)

```
(Δ_pred − Δ) / Δ  =  ε  +  δ · n / (n − p).
```

Two consequences, and they point in opposite directions:

* **A shared systematic is harmless.** Setting `δ = 0` gives exactly `ε`
  (`common_mode_passes_through`): a bias common to the proton and the neutron passes into the
  difference at `1×`, unamplified.
* **A differential is amplified by `n / (n − p)`.** For the nucleons that factor is
  `939.565 / 1.293 ≈ 726.5` (`differential_is_amplified`).

**What that settles for the L2 scoreboard.** `Δ_pn` misses by 163.3× while `m_p` misses by
1.35 ppb. The first consequence rules out the reading that a shared mass-scale bias is
inflating the difference — a common `ε` cannot do it, so no amount of common systematic
explains `Δ_pn`.

The chain then supplies the actual direction. `m_n = m_p + Q_β + m_e` makes `Δ_pn = Q_β + m_e`
identically, so `Q_β` is the *input* and `Δ_pn` and `m_n` are its consequences — not the other
way round. `q_beta_is_not_independent` records the resulting proportionality: the relative
errors of `Q_β` and `Δ_pn` differ only by `Δ / (Δ − e) ≈ 1.653`, fixed by geometry with no
framework input. That is the whole of the gap between their 164.0× and 163.3× miss factors,
and it means counting both as failing observables double-counts one defect.

Numerically (`l2_gap_independence_decomposition.py`, all ratios ≤ 0.03 % from unity):
`m_n`'s error is `m_p`'s plus `Q_β`'s (ratio 1.00004); `Δ_pn`'s absolute error equals `Q_β`'s
(ratio 1.00031); and `m_μ`'s 209.8 ppb is exactly the 11.537 ppb q₀ layer separation times its
pin sensitivity 18.185 (ratio 1.0000), so it is a pin artifact rather than a derivation gap.
Of the five failing observables only `Q_β` is unexplained — its own pin sensitivity accounts
for 2.4 % of its miss.

**Relation to `BindingErrorAmplification.binding_rel_error`.** That theorem is the *one-sided*
case — one term carries the error and the other is exact. Setting `ε = 0` here recovers that
shape for a difference; the content added is the two-sided common/differential split, which is
what separates "both are inaccurate" from "they disagree with each other".

Numerical companion: `computations/l2_gap_independence_decomposition.py`.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU
namespace MassTheory
namespace DifferenceObservableErrorSplit

variable {K : Type*} [Field K]

/-- The amplification factor of a difference observable `n − p`: the larger term over the
difference. For the nucleons this is `m_n / Δ_pn ≈ 726.5`. -/
noncomputable def amplification (n p : K) : K := n / (n - p)

/-- **Common/differential error split for a difference observable.**

With `p_pred = p·(1+ε)` and `n_pred = n·(1+ε+δ)` — a *common* relative error `ε` on both and
a *differential* `δ` on the second — the difference `Δ = n − p` carries relative error

  `ε + δ · n/(n − p)`.

The common part passes through at `1×`; only the differential is amplified. -/
theorem difference_rel_error_split (n p ε δ : K) (h : n - p ≠ 0) :
    ((n * (1 + ε + δ) - p * (1 + ε)) - (n - p)) / (n - p)
      = ε + δ * amplification n p := by
  unfold amplification
  field_simp
  ring

/-- **A shared systematic is not amplified.** With no differential (`δ = 0`) the difference
inherits exactly the common relative error. So a difference observable that is orders of
magnitude worse than its constituents is evidence of *disagreement between them*, never of a
bias they share. -/
theorem common_mode_passes_through (n p ε : K) (h : n - p ≠ 0) :
    ((n * (1 + ε) - p * (1 + ε)) - (n - p)) / (n - p) = ε := by
  have := difference_rel_error_split n p ε 0 h
  simpa using this

/-- **Pure differential.** With no common part (`ε = 0`) the whole error is the differential
times the amplification factor — the term that dominates for the nucleons (99.8 %). -/
theorem differential_is_amplified (n p δ : K) (h : n - p ≠ 0) :
    ((n * (1 + δ) - p) - (n - p)) / (n - p) = δ * amplification n p := by
  have := difference_rel_error_split n p 0 δ h
  simpa using this

/-- **Second hop: subtracting an exact anchor rescales the relative error.**

`Q_β = Δ − e` with `e` exact (the CAL-1 electron anchor). An absolute error `a` on `Δ` is
inherited unchanged by `Q_β`, so the *relative* errors differ exactly by `Δ / Q_β`:

  `(Q_pred − Q)/Q = ((Δ_pred − Δ)/Δ) · (Δ / (Δ − e))`.

For the nucleons `Δ_pn / Q_β ≈ 1.653`, which is the whole of the gap between `Q_β`'s 164.0×
miss and `Δ_pn`'s 163.3×. -/
theorem q_beta_rel_error (Δ e a : K) (hΔ : Δ ≠ 0) (hQ : Δ - e ≠ 0) :
    ((Δ + a) - e - (Δ - e)) / (Δ - e) = (a / Δ) * (Δ / (Δ - e)) := by
  field_simp
  ring

/-- **`Q_β` and `Δ_pn` are one gap, not two.** Their relative errors are proportional, with
the ratio fixed by the geometry `Δ / (Δ − e)` alone — no framework input. Hence closing one
closes the other, and counting both as failing observables double-counts a single defect. -/
theorem q_beta_is_not_independent (Δ e a : K) (hΔ : Δ ≠ 0) (hQ : Δ - e ≠ 0) :
    ((Δ + a) - e - (Δ - e)) / (Δ - e)
      = (((Δ + a) - Δ) / Δ) * (Δ / (Δ - e)) := by
  field_simp
  ring

end DifferenceObservableErrorSplit
end MassTheory
end QOU
