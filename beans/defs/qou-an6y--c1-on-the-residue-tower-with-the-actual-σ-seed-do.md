---
# qou-an6y
title: 'C1 on the residue tower with the ACTUAL Σ seed: do the Jackson / q-d/dz towers on the branch-point expansion of the colour cubic satisfy L_K from level 2? and how underdetermined is the weight problem?'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:28:29Z
updated_at: 2026-10-04T15:12:04Z
parent: qou-8lxd
---

## Question (2026-09-04, follows qou-col1 / #6628)

#6628 made the symbol identification a computable statement on the level axis: for a derivative-only two-term tower, C1 from level 2 on the residues ⇔ `[m+4]_q s_{m+2} = s_{m+1} + s_m` on the t¹-coefficients `s_m = (Dᵐ X)(1)`, and the level-m constraint reads seed slots `a_{m+3}..a_{2m+5}` (never `a_0`). With a GENERIC seed that is always satisfiable by choosing the tail. So the content is in the SEED: the branch-point expansion `X = Σ a_k t^k` of the colour cubic `P = X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)` at `z = z_c + t²` (the simple branch `zgeometric_ramification_parity_probe.py` uses) is FIXED by Σ.

## PLAN
1. Build the seed exactly-enough: z_c the branch point (root of disc_X P), X_0 the double root, Puiseux coefficients a_k by the Newton recursion — mpmath at ≥ 60 dps (no float64), plus exact-symbolic cross-check of the recursion where feasible.
2. For the two concrete derivative-only candidates (Jackson `[e+1]_q σ` + q-d/dz `[e+2]_q σ²`, balanced and geometric) compute `r_n = (Dⁿ X)(−2)` for n = 2..6 and test `[n+2]_q r_{n+2} = r_{n+1} + r_n` at several exact rational q (identity in q ⇒ must hold at each). Report the residual size. A failure at 60 dps is a scope-(a) negative for THAT candidate on THAT seed; a pass is only evidence and would need exactness.
3. Counting: with the seed fixed, treat the weights `c₁(e), c₂(e)` as unknowns; how many new unknowns does each level introduce vs one constraint — is the weight problem underdetermined (⇒ the level-axis identification has no content until the weights are fixed by geometry)? Formalize the counting statement if it is clean.
4. Lean for whatever structural statement survives; audit doc; scope note if warranted.


## RESULT (2026-09-04, PR #6652)

**Scope-(a) negative.** On the Puiseux expansion of the colour cubic at its simple branch (z_c = −0.9748+0.2230i, X₀ = −0.0721−0.6383i; |P_X| = 1e-81 after joint Newton refinement; re-substitution 1e-79 through t²²), the Jackson + q-d/dz residue tower fails C1 from level 2 with defect |d_n|/max|r| of order 9–255 at q ∈ {11/10, 3/2, 2, q₀}, both sheets, both q-integer conventions. Not a precision artefact.

**Underdetermination (exact, generic):** level-m constraint involves 6/10/14/18 weight values (m = 0..3), of which 6/4/4/4 are new, all linear. With free weights the level-axis identification constrains nothing; the content is in where D_q's weights come from (W1, `qou-d8de`, as a counting fact). Prune: do not fit weights to the recurrence — a fit always exists.

Trap recorded: a polyroots double root is good to half the working precision (3.3e-41 at 80 dps); refine on P = P_X = 0. The zgeometric probe's |P_X| ≈ 6e-21 is the same effect.

No new Lean (the backbone is #6628's `twoOp_c1RecFrom_two_iff`); scope note on the conjecture block; audit doc `docs/audits/2026-09-04-c1-residue-tower-on-the-sw-seed.md`.

Waiting on: owner merge permission for #6652.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
