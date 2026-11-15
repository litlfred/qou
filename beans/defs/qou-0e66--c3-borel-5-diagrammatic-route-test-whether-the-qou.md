---
# qou-0e66
title: 'c3-borel #5 (diagrammatic route): test whether the QOU braid-word -> (m,ℓ)/Stokes-entry selection IS the McPhail-Snyder (arXiv:2601.05136) per-edge integer state-sum k∈Z^E over crossings, specialised at q₀. This is the DIAGRAMMATIC realisation of the qnnq braid->data map (complement to Fantini-Wheeler''s NZ-datum route): k attached to the knot diagram, (µ,λ)=cusp holonomy, worked for the 5₂ Kashaev invariant. Ref mcphail-snyder2026 + McPhail-Snyder–Reshetikhin holonomy R-matrices. Parent qou-wmkb; bears on qou-qnnq. No fit, nothing wired.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T18:47:21Z
updated_at: 2026-11-15T23:50:00Z
parent: qou-avtq
---

## Re-scope (2026-08-01) — the roast walked back the title's over-claim

The title's framing ("test whether the braid → Stokes-entry selection **IS**
the k∈Z^E sum specialised at q₀") is over-optimistic. Per the roast in
`qou-t7az`, McPhail-Snyder's `k ∈ Z^E` is **summed over, not selected**
(same non-selection as FW's (m,ℓ)), the construction lives at a **root of
unity** (fibre level) not at q₀, and it **takes ρ/(µ,λ) as input** — the very
datum qnnq must derive. So the honest task is NOT "confirm the mechanism," it
is: **assess whether the archimedean q₀-evaluation of the fibre-level
McPhail-Snyder diagrammatic state-sum has any bridge to the QOU c₃ at all,
and flag the fibre↔observable category error before spending compute.** If no
bridge, record the negative. No fit, nothing wired.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Still unassessed. The likely outcome is a written negative: HabiroEvaluationTrichotomy rules out the series route at q0, and ModularDoubleReciprocity makes the state-integral route degenerate at the substrate. Close by writing that bridge-assessment up against qou-t7az. Do not probe.

Evidence: The re-scoped task (does a q0-evaluation of McPhail-Snyder's fibre-level state-sum bridge to c_3?) has no probe or witness. The negative prior is in `beans/defs/qou-t7az` (roast: ρ is an input, k∈Z^E is summed rather than selected, it is a root-of-unity object, it targets volume). Two structural results bear on it: `QOU/QBeta/HabiroEvaluationTrichotomy.lean` (an infinite Habiro series has no continuous evaluation at q>1) and `QOU/QBeta/ModularDoubleReciprocity.lean` (the state-integral dual is ~1e-165 at the substrate).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-11-15 — executed under owner ruling `Q-AVTQ-3 = 1` (PR #8063, absorbing `qou-t7az`)

- **Written Negative & Lean 4 Exclusion Module:** `folio/quantum-observable-universe/lean/QOU/QBeta/McPhailSnyderBridgeExclusion.lean` (wired into `QOU.lean`, compiled with `0` errors / `0` warnings / `0` `sorry`).
- **Four Structural Obstructions Formalized (`mcphailSnyder_archimedean_bridge_exclusion`):**
  1. **Holonomy input non-derivation (`mcphailSnyderStateSum_ne_of_mu_ne`):** The diagrammatic state-sum takes the cusp holonomy $(\mu, \lambda)$ as an external boundary parameter (`CuspHolonomyInput`) rather than deriving it from the braid word.
  2. **State summation vs. branch selection (`mcphailSnyderStateSum_shift_invariant`, `stateSum_strictly_gt_single_state`):** The edge colourings $k \in (\mathbb{Z}/N\mathbb{Z})^E$ are summed over the full finite group, making the output invariant under any translation $k \mapsto k + \delta$ and strictly larger than any single state weight when $N \ge 2$ and weights are positive.
  3. **Habiro / $q$-Pochhammer real-locus divergence (`qPoch_not_tendsto_zero_of_one_lt`):** At the archimedean pin $q_0 > 1$, the cyclotomic $q$-Pochhammer factor $(q_0; q_0)_n$ does not tend to $0$, ruling out naive real-locus series continuation of the root-of-unity state sum.
  4. **Modular-double dual suppression (`modular_reciprocity`, `dual_lt_of_y_lt_one`):** Under Faddeev's modular double ($b^2 = (\ln q_0)/(2\pi i)$), the dual parameter $\tilde{q} = \exp(-4\pi^2/\ln q_0) \approx 5.93 \times 10^{-165}$ is non-perturbatively suppressed.
- Held at `status: in-progress` pending PR #8063 merge and owner closure review.
