# D-ladder single-level resurgence parameters are LENGTH-BLOCKED at k=41 — the growth form is unresolved

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (D-ladder Écalle,
sibling #3818) · **Tier:** numerical scope-(a) negative (a length limitation, plus a
growth-form diagnosis) · **Discipline:** no fit (nothing tuned to CODATA), no c_k
wired, nothing to production, no tier change.

## Setup

The [two-action probe](2026-07-18-dladder-fibre-two-action.md) ruled out two-level
structure (the two k-parity halves share one common Borel action). That makes the
single-instanton asymptotic

    |d_k|  ~  C · (k!)^κ / A^k

**well-posed in principle** — one Gevrey order `κ`, one action `A`. This probe
attempts to extract them and reports the honest outcome.

## Result — the growth FORM does not resolve at k=41

[`qbeta_dladder_single_instanton_extraction_probe.py`](../../computations/qbeta/qbeta_dladder_single_instanton_extraction_probe.py)
(exact ℚ(√3) `d_k` to k=41, ORD=83):

| diagnostic | k=20 → k=40 | tail slope in 1/k | plateau? |
|---|---|---|---|
| `log‖d‖/(k·log k)` → κ (ordinary Gevrey) | `0.591 → 0.499` | `4.16` | **no** |
| `log‖d‖/k²` → c (q-Gevrey) | `0.0885 → 0.0460` | `1.74` | **no** |
| local `κ_k` (5-pt fit) | `0.064 → 0.026` | — | **no** (drifts down) |
| `Δ² log‖d‖` intercept (1/k→0) | — | — | `≈ −8·10⁻⁴ ≈ 0` |

- **Neither** growth-form ratio plateaus: `log‖d‖/(k·log k)` is not settling to a
  Gevrey order `κ`, and `log‖d‖/k²` is not settling to a q-Gevrey constant `c`.
- The second difference `Δ² log‖d‖` extrapolates to `≈ 0` (intercept `−8·10⁻⁴`),
  which **mildly favours ordinary Gevrey** (`Δ² ~ κ/k → 0`) over q-Gevrey
  (`Δ² → 2c > 0`) — and is quantitatively consistent with `κ/k` for the *small*
  local `κ ≈ 0.03` at `k ≈ 38`.
- But the local `κ_k` is **still decreasing** (`0.064 → 0.026`, no plateau), so no
  settled Gevrey order can be read off.

A naive Neville/Richardson extrapolation of the non-converged local `κ_k` sequence
overshoots to nonsense (`κ_inf ≈ −11`, `A_inf ≈ 10⁻¹⁹`) — the **symptom** of
extrapolating an unresolved form, not a result. (That garbage output was caught and
is reported as the diagnostic it is, not committed as a parameter.)

## Reading

The D-ladder is **single-level** (established) and **ordinary-Gevrey-like**
(`Δ² → 0`, mildly favoured over q-Gevrey), but its **Gevrey order `κ` is small and
unsettled at k=41** — the asymptotic regime has not set in over the 41 exact rungs.
This is the growth-form face of the merged "no single Gevrey index / structural
q-Gevrey drift" (#3839): the effective exponent keeps drifting because 41 terms do
not reach the tail.

**Consequence:** the single-level resurgence parameters `(κ, A)` are **length-blocked
at k=41** — a parametrized single-instanton route to the c₃ value cannot be pinned
here. It needs far more exact rungs (well past ORD=83), or must be **bypassed** by the
length-robust handle already in hand: the **direct optimal-truncation Stokes floor**
on the fibre, `δ_np = min_k |d_k ũ^k|`, which needs no Gevrey exponent and is
measured in the [companion probe](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
(unsuppressed above `r* = |d₃₀/d₃₁|`).

## Scope (anti-laundering)

A genuine *negative*: records that `(κ, A)` are not extractable at k=41 and diagnoses
why (growth form unresolved, mildly ordinary-Gevrey-like). Derives no c₃ value; the
`κ_inf ≈ −11` Neville output is explicitly flagged as an artifact, **not** a parameter.
Wires nothing; no tier change; no fit; no c_k.

## Cross-references

- Single-level (the premise): [`2026-07-18-dladder-fibre-two-action.md`](2026-07-18-dladder-fibre-two-action.md)
- Length-robust handle (the bypass): [`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
- "No single Gevrey index" (independent, from the singularity side): extension-singularity #3839
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
