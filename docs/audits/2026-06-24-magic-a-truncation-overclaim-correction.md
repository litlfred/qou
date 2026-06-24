# Correction — the magic-A ⁴He +5.87% is NOT a body-order truncation residual

**Date:** 2026-06-24
**Branch:** `claude/correct-magic-a-truncation-overclaim-2026-06-24`
**Corrects:** [`2026-06-24-binding-recurrence-spectral-bridge.md`](2026-06-24-binding-recurrence-spectral-bridge.md)
(PR #2718) §"Honest scope".

## The over-claim

PR #2718's audit asserted, in passing, that the magic-A ⁴He **+5.87%** miss "is the
finite-truncation residual of the geometric series." Self-audit (per the
refuted/ruled-out discipline) finds this **wrong** — it conflated two distinct objects.

## The two objects (0 fit)

| object | value | vs AME 28.296 |
|---|---:|---:|
| **(1) magic-A formula** `2·m_e·A·8G` (8G = Borromean L6a4 volume) | 29.956 MeV | **+5.87%** ← *this* is the +5.87% |
| **(2) body-order jet-sum** `m_e·Σ_{n=2}^{4} a_D⁽ⁿ⁾` (physical `n ≤ A=4`) | 2.488 MeV | −91% (≈ 11× too small) |

The body-order series partial sums are 2.49 (n≤4), 5.23 (n≤5), 11.2 (n≤6), 24.1
(n≤7), 52.4 (n≤8): it only crosses 28 MeV near **n=7–8**, unphysical for a 4-nucleon
system and accidental. And since `λ₊ = 2.185 > 1` the series **diverges** — there is
no finite total to "truncate." So the +5.87% cannot be a truncation residual of the
body-order series; it is the residual of the *separate* doubly-magic formula.

## Scope of the correction (what changed, what stands)

- **Re-scoped:** the sentence tying the +5.87% to a body-order truncation. The two
  are distinct objects (magic-A formula gap vs body-order series).
- **Stands (unaffected):** the spectral-bridge result of PR #2718 — the depth-2
  kernel's dominant root `λ₊ = 2.185 > 1` gives extensive *body-order growth*, and
  `lambdaPlus_gt_one` (Lean, sorry-free). That concerns the body-order series'
  growth rate, not the magic-A gap, and is correct as stated.

Per the discipline, the numerical finding (the magic-A gap is real, +5.87%) is not
deleted — only the wrong *scope* (calling it a series-truncation residual) is fixed.

→ `computations/probes/magic_a_truncation_overclaim_correction_probe.py` ·
`computations/magic-a-truncation-overclaim-correction.witness.json`
