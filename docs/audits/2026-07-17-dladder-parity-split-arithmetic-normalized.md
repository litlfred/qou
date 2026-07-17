# D-ladder W9 first increment: the parity split resolves half the Gevrey-index drift; the 3-adic normalization worsens it

**Date:** 2026-07-17
**Branch:** `claude/alien-calculus-resurgence-nvvezn` · **PR:** [#3817](https://github.com/litlfred/qou/pull/3817)
**Bean:** `qou-dri7` (W9 — q-Borel/Écalle acceleration of the bar-odd D-ladder; the
[1ppq reassessment](2026-07-17-1ppq-path-reassessment.md)'s unowned Option 1)
**Probe:** [`computations/qbeta/qbeta_dladder_parity_split_arithmetic_normalized_probe.py`](../../computations/qbeta/qbeta_dladder_parity_split_arithmetic_normalized_probe.py) (exit 0)
**Witness:** `computations/qbeta/qbeta-dladder-parity-split-arithmetic-normalized.witness.json`
**Complements:** Track 1 of the [three-front attack](2026-07-17-1ppq-three-front-attack.md)
(extension k>21, same *mixed* estimators) and #3683 (even κ-tower); neither runs these splits.

## The question

The exact D-ladder `d_k = a_k + b_k√3` (k ≤ 21) is super-exponentially divergent with **no
single Gevrey index** — log-fit `C ≈ 0.06` vs Borel–Leroy `s* ≈ 0.20`, drift by three methods
([07-13 audit](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)). All prior
estimators ran on the **mixed** ladder. The corpus has two **proved** arithmetic gradings —
(G2) the 2-adic bar-parity grading (`v₂(den b_k)=0 ⟺ k` odd, Lean-anchored) and (G3) the
3-adic `v₃(den d_k) ~ 1.5k` growth. Fit-free question: is the index drift a **superposition
artifact of the arithmetic channels**?

## Findings (scope-(a); exact d_k, local index `C_k = Δln|d_k|/Δln k!`)

Both gradings reproduced on this data (G2 exact; G3 slope 1.50).

| estimator | local-index drift (stable window) |
|---|--:|
| mixed (control) | 0.914 |
| **odd channel** (step-2 within parity) | **0.344** |
| **even channel** | **0.260** |
| 3-adic-normalized (`d_k·3^{v₃}`) | 2.844 |
| 3-norm + parity | 0.789–1.083 |

1. **The parity split resolves ≥ half the drift.** Within each parity channel the local
   index is smooth and monotone (even: 1.256 → 0.638; odd: 1.839 → 0.628), and the two
   channels **converge toward each other** (0.628 vs 0.638 at k = 20–21) — the wild mixed
   drift is largely cross-parity interleaving. The bar-parity grading is not only
   arithmetic (G2) but **analytic**: the divergence class is cleanest per parity channel.
2. **Still no fixed index.** Both channels keep falling through `C ≈ 0.63` at k = 21 with
   no plateau — the q-Gevrey "drifting index" verdict survives the split (now measured
   cleanly, without the interleaving noise). Whether `C_k` plateaus (a genuine Gevrey
   order) or falls to the mild `C ≈ 0.06` log-fit scale is exactly what Track 1's
   extension (k → ~31) can decide with these per-channel estimators.
3. **The 3-adic normalization is anti-productive** (drift 2.84 ≫ mixed): the `3^{~1.5k}`
   denominators are **load-bearing smooth structure** of the growth, not an arithmetic
   artifact to be removed. This kills the "denominator-cleaning" acceleration ansatz
   (scope-(a): at k ≤ 21, as a standalone normalization).

## Handoff

The per-channel local-index estimator is the recommended re-measurement for Track 1's
extended rungs (drop-in: same probe, higher ORD). No instanton action claimed (the 07-13
honest boundary stands); no c₃ value; nothing wired; the c_k flip-flop discipline untouched.

## Discipline

Both splits forced by proved gradings (fit-free, pre-registered in the probe docstring
before running); exact ℚ(√3) rungs from the canonical `build_d_ladder` chain
(`odd_ok` over-determination asserted); mpmath 60 dps for the logs only. Scope-(a).
