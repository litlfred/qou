---
# qou-fmfw
title: Volume-only beats Vol*tr_M on the T/3He mirror pair (2.90%, zero free params) — extend to all four L2 targets
status: todo
pr: 8306
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:02:18Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Derived from PR #4610's OWN data. #4610 concludes 'rho = tr_M radial handle refuted under every volume reading' -- correct, but the data shows the refutation is of tr_M, not of volume. A=3 mirror pair, volume alone, ZERO free parameters (constant cancels in the ratio): B(T)/B(3He) = 1.0990 (AME2020); Vol(T)/Vol(3He) = 1.1308 (#4610 SnapPy, 8_11 = 8.2863168 and L6a4 = Borromean = 7.3277248); ratio-of-ratios 1.0290 => 2.90% miss. Compare #4610's Vol*tr_M prediction 0.570 against C_knot ratio 1.350 -- ANTI-correlated, wrong side of 1. E0*Vol/B = 3.9743 (3He) and 4.0895 (T), a near-constant ~4 with 2.90% spread. DISCIPLINE FLAGS: two-point observation on ONE mirror pair; the ~4 constant is fitted to two numbers and means NOTHING until it holds across D/T/3He/4He; scratch float64, NOT witness-grade. Only the RATIO claim is parameter-free and only it counts. TASK: extend to all four L2 binding targets under Reading 2, ratio-only. BLOCKED on the author's Reading-1-vs-Reading-2 ruling (#4610 measured the literal mass-braid H_9 closures NON-HYPERBOLIC, Vol=0; the corpus-canonical SDP-registry links ARE hyperbolic).

RETRACTED 2026-08-07: not a new result. Corpus already has B = 2*m_e*Vol(K) as the bond-count law (a3_mirror_residual_reconciliation.py L59-64) and the 'Kashaev law B = rho_F * m_e * Vol_hyp(K); historical knot IDs (6_2, 8_11, L6a4)' (b_over_a_v5_unified.py L327). E0 = 8.1918*m_e so E0*Vol/B ~ 4 IS B ~ 2.05*m_e*Vol -- the same law with a 2.4% offset. My corpus-grep failure, the #1515/#1532/#1543 pattern. What survives as mine: only that #4610's refutation is of tr_M specifically and the EXISTING pure-Vol law beats Vol*tr_M on the mirror pair. Corpus also already recorded the negative I was walking toward: binding_link_volumes.py says B = m_e*Vol*Delta_tr gives -60% at both 3H and 3He and 'the A-dependence cannot live in a single binding-link volume'. DEUTERON BLOCKER (both readings): 2H -> Hopf L2a1 is Seifert-fibred, Vol=0; the corpus's +0.2% deuteron match came from SUBSTITUTING Vol(B_3) for Vol(Hopf), an unjustified substitution. B_D is the loosest L2 target (4.5 ppb), so a route that cannot reach the deuteron is not a route to the L2 binding targets.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8306, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
