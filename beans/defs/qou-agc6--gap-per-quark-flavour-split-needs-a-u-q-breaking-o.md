---
# qou-agc6
title: 'GAP: per-quark flavour split needs a U_q-breaking object with a triple zero at q=1'
status: todo
type: task
created_at: 2026-11-21T18:48:13Z
updated_at: 2026-11-21T18:48:13Z
---

Owner chose this on 2026-11-21 (card in the per-quark flavour split thread). Issue #8922, PR #8931.

## What is open
Step 2 of prf:flavor-split-substrate posits (μ_d − μ_u)/μ_avg ≈ h²·ħ_q/√q. No derivation is on record.

## What is excluded (scope b, Lean)
QOU.FlavorDressing.PivotSplitOrder.ansatz_ne_pivotSplit: with additive strands and m_p/m_n a nonzero power of q, the split is c(t^m−1)/(t^m+1) with t = √q. It has a simple zero at t = 1, and the ansatz has a triple zero. ansatz_bar: f(q⁻¹) = −q² f(q), so the ansatz is not bar-odd, while every derived differentiator is exactly bar-odd.

## Structural note (not a proposal)
ansatz = h²(√q − 1/√q)/q. The prefactor is exactly bar-odd with the same triple zero. Swapping the target to it would be a selection against the target (about 11% at q0) and was not offered.

## Next honest step
Look for an object that breaks U_q(sl2), for example a boundary datum on the Bring colour tube, a sea strand, or a non-additive strand rule, whose p/n differentiator starts at (q−1)³. A natural shape is a third-order product of first-order differentiators (h·h·ħ_q). Bridge B audit (2026-11-16) records none in the corpus.
