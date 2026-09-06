# D-ladder resummation: the odd (S-carrier) half is fixed-order Borel-summable — the "no single Gevrey index" is even-k-driven

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


**Date:** 2026-07-17 · **Axis:** Q_β c₃ odd channel (1ppQ; m_n/Δ_pn/Q_β root cause)
· **Tier:** numerical (scope-(a) measurement) · **Discipline:** no fit to QOU
data, no c_k wired, no tier change. Parallel-context probe (owner directive:
duplication is valuable — a different context finds what another missed).

## The angle

The merged order-scan
([`qbeta_dladder_qborel_leroy_resummation_probe.py`](../../computations/qbeta/qbeta_dladder_qborel_leroy_resummation_probe.py))
found the bar-odd D-ladder `D(ũ) = Σ d_k ũ^k` has **no single Gevrey index**:
the root-test order `s* ≈ 0.20` disagrees with the log-fit divergence exponent
`C ≈ 0.06`, read as intrinsic q-Gevrey drift. The k=31 extension confirmed the
drift persists.

**Untried angle:** the 2-adic parity grading is *exact* —
`v₂(den b_k) = 0 ⟺ k odd`, with **2 the unique graded prime** (the ℤ/2
bar-involution sinh/cosh shadow; `DLadderTwoAdicGrading`). That is a
coefficient-level ℤ/2 grading. Hypothesis: the "no single index" is an artifact
of measuring **two interleaved fixed-index subseries** (even-k and odd-k) as
one.

## Result — PARTIAL, and it points at the right half

[`qbeta_dladder_parity_split_resummation_probe.py`](../../computations/qbeta/qbeta_dladder_parity_split_resummation_probe.py)
(exact ℚ(√3) `d_k` to k=31; split `A_m = d_{2m}`, `B_m = d_{2m+1}`):

| subseries | Borel–Leroy order s* | stability (drift) |
|---|---|---|
| **odd-k** `B` (bar-ODD = the **S-carrier**, the Q_β c₃ half) | **`s_B ≈ 0.0683`** | **STABLE** (0.0035) |
| even-k `A` (bar-even) | `s_A ≈ 0.355` | drifts (0.023) |

- The **odd-k half is fixed-order Borel–Leroy summable** at `s_B ≈ 0.068`, and
  that order **matches the independent merged log-fit `C ≈ 0.06`** — two
  different estimators agree on the odd half.
- The even-k half still drifts (`s_A ≈ 0.355`, unstable).

**New reading:** the combined-series "no single Gevrey index" is
**even-k-driven** — the even half's drift contaminates the combined estimator,
which is exactly why the combined root-test (`s* ≈ 0.20`) and log-fit
(`C ≈ 0.06`) disagreed (they weight the two parities differently). The
*physically relevant* odd (S-carrier) half sits cleanly at `≈ 0.068` by both.

## Actionable consequence

For the Écalle-acceleration builders (siblings #3683/#3805): the odd
(S-carrier) half — the one that carries the Q_β `c₃` bar-odd `S` — should be
resummed at a **fixed Borel–Leroy order ≈ 0.068**, not through the drifting
combined series. Only the even-k half needs the full multi-step Écalle
acceleration. This halves the hard part of the odd-channel resummation and
gives the S-carrier a concrete fixed-order transform to test against the two
S-anchors — a sharper target than "the combined ladder is q-Gevrey."

## Honest scope

Measurement, scope-(a). `s_B ≈ 0.068` is an *order* (the transform that renders
the odd half summable), **not** a c₃ value or an S-value — nothing is resummed
to a number here, nothing wired, no tier change. 16 odd-k terms is a finite
window; the odd/even stability contrast (0.0035 vs 0.023, 6.7×) and the
two-estimator agreement on the odd half are the signal. A genuine parallel-
context refinement of the sibling reading, not a contradiction of it: the
q-Gevrey drift is real, but it lives in the even (non-S) half.

## Cross-references

- Merged order-scan + 2-adic grading: [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md)
- k=31 extension (drift persists, combined): the merged `qbeta_dladder_extension_singularity_probe.py`
- Parallel-work directive: AGENTS.md §"Parallel exploration is valuable"
