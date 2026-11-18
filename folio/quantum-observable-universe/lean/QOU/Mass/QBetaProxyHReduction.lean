import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.QBetaProxyHReduction — the CAL-2 proxy `1/h`-scale exact reduction

Formalize-first result behind the deuteron "`1/h` scale" probe
(`computations/probes/probe_d_qbeta_h_invariant.py`, part (i); audit
`docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md`).

With the bandwidth `h = q − q⁻¹`, the categorical scale `E₀ = 1/(q(q−1))`
(in `m_e` units, cheat-sheet step 11), and the CAL-2 proxy closed form
`Q_β = m_e·|q²−2q−1|(q+1)/(2q³)` — whose numerator resolves to
`2q − q² + 1` on the substrate branch `1 < q < 1+√2` — the following is an
**algebraic identity in the fraction field** (sympy-proved in ℚ(q); here
proved over a generic `[Field R]` per AGENTS.md §7c, no `ℝ`-specific
construct):

```
  Q_β_proxy = E₀ · h · (2 − h) / 2        ⟺        Q_β_proxy / h = E₀ · (2 − h)/2.
```

Structural reading (observation tier, not wired — Δ_λ gate): the mysterious
`1/h` binding scale is exactly `E₀` dressed by `(1 − h/2)`, the bar-average
of the smoothed crossing pair `{1, 1−h}` (from `σ⁻¹ = σ − h`) at the
deuteron's single p–n interface.

-- Ref: [leitner2026] quantum-observable-universe — CAL-2 proxy cheat-sheet (step 11)
-/

namespace QOU.Mass.QBetaProxyHReduction

variable {R : Type*} [Field R]

/-- The bandwidth `h = q − q⁻¹`. -/
noncomputable def hOf (q : R) : R := q - q⁻¹

/-- The categorical scale `E₀ = 1/(q(q−1))` (in `m_e` units). -/
noncomputable def E0 (q : R) : R := (q * (q - 1))⁻¹

/-- The CAL-2 proxy `Q_β` closed form (numerator resolved on the substrate
    branch `1 < q < 1+√2`, where `|q²−2q−1| = 2q − q² + 1`), in `m_e` units. -/
noncomputable def QbetaProxy (q : R) : R := (2 * q - q ^ 2 + 1) * (q + 1) / (2 * q ^ 3)

/-- **Exact reduction.** The CAL-2 proxy `Q_β` equals the categorical scale
    `E₀` times the smoothed bar-average `h·(2−h)/2` of the single interface
    crossing — an algebraic identity in the fraction field. -/
theorem qbeta_proxy_eq_E0_h_reduction (q : R)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    QbetaProxy q = E0 q * hOf q * (2 - hOf q) / 2 := by
  unfold QbetaProxy E0 hOf
  field_simp
  ring

/-- **Scale form.** Dividing by the bandwidth `h ≠ 0`: the `1/h`-scale is
    `E₀·(2−h)/2 = E₀·(1 − h/2)`. -/
theorem qbeta_proxy_over_h_eq_E0_reduction (q : R)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : (2 : R) ≠ 0) (hh : hOf q ≠ 0) :
    QbetaProxy q / hOf q = E0 q * (2 - hOf q) / 2 := by
  rw [qbeta_proxy_eq_E0_h_reduction q hq hq1 h2]
  field_simp

/-- **Cleared-denominator form of the CAL-2 proxy reduction (`qou-v2om`).**
For `q ≠ 0`, `q - 1 ≠ 0`, and `(2 : R) ≠ 0`, `2 * QbetaProxy q = E0 q * hOf q * (2 - hOf q)`. -/
theorem qbeta_proxy_mul_two_eq_E0_h_two_sub_h (q : R)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    2 * QbetaProxy q = E0 q * hOf q * (2 - hOf q) := by
  rw [qbeta_proxy_eq_E0_h_reduction q hq hq1 h2]
  field_simp

end QOU.Mass.QBetaProxyHReduction
