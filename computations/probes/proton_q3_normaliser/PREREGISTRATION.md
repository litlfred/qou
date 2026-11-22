# Pre-registration: q₀, m_p and Q_β under alternative `/q³` normalisers

**Date:** 2026-11-21, written and committed before the probe was run.
**Thread:** "Justify the proton's /q³ normalisation"; PR #8964, issue #8963.
**Lean:** `QOU/MassTheory/ProtonQ3SchurElement.lean`.

## Question

The proton identity is `m_p/m_e = 2(Vol(4₁)/ℏ_q²)·|tr_M(β_Bor)|·N(q) − 12`, with
production `N = [3]_q!/q³ = c_sign`. The Lean file shows that `N` is asserted,
not derived, and lists the principled alternatives. This probe reports what each
alternative does to the numbers downstream. It does **not** choose one.

## Arms (fixed before running)

| arm | N(q) | where it comes from |
|---|---|---|
| A0 | `[3]_q!/q³` | production; sign Schur element; `−∂_z tr_z(x₋)` coordinate |
| A1 | `[3]_q!` | bar-symmetric (k = 0) |
| A2 | `q³[3]_q!` | trivial Schur element (k = +3) |
| A3 | `[2]_q[3]_q!/q³` | `|∂_t tr(x₋)|` in the idempotent coordinate `t = τ(P₋)` |
| A4 | `[3]_q!/(q⁴(q²−1)(q²+1)²)` | `|∂_a tr(x₋)|` in Wenzl's `a = q^{2r}` |

## Outputs (per arm)

1. `q₀(N)`: the root near 1.11 of the proton identity at CODATA `m_p/m_e` (the
   `constants.q_at` solve with `N` swapped in). Report "no root in (1, 2)" if
   there is none.
2. `Δq₀` against A0, in ppb.
3. `m_p` predicted at the frozen **muon** pin `Q_MUON_50_DIGIT_STR`, and its error
   against CODATA in %.
4. The scored `Q_β = m_e·R(q)`, with
   `R(q) = −(q+1)P(q)/(q³(2q−1)(q²+1)³)` and `P = q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1`
   (`qbeta_error_budget_probe.py` B1), at `q₀(N)`, and against the CODATA
   comparison value 0.78233 MeV in %.

Arithmetic in mpmath at 50 dps, with no float64.

## Decision rule (fixed now)

- These numbers are **diagnostics only**. No arm is adopted, promoted or
  demoted because it lands closer to CODATA, since that would be selection
  against the target (AGENTS.md §NO FITTING).
- A0 must reproduce `q_at()` to ≥ 40 digits and the scored Q_β = 0.325433929 MeV.
  If not, the probe is wrong and nothing else is reported.
- Whatever comes out is reported in full, including arms with no root.
