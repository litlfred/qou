---
# qou-0jcd
title: 'Step-2 plan: close cheat-sheet §2a (the stipulated Hecke curvature) — conjecture class + Picard–Lefschetz classical shadow + KZ real-q prune'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T06:45:49Z
updated_at: 2026-10-04T15:13:59Z
parent: qou-m6dn
---

2026-09-06: plan written — docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md. Options A (§3b conjecture class HeckeMonodromy), B (Picard–Lefschetz classical shadow of the colour cubic: local monodromy = transposition/reflection, σ²=1 = q=1 shadow of the Hecke quadratic), C (KZ real-q prune first, construction as research), D (nothing). Recommendation A+B+C-prune in one PR. Awaiting the owner's pick.

2026-09-06: A, B and the C-prune executed on the owner's 'Continue' (qou-ba73, qou-xipk, qou-74ip). Remaining: the conj: content block (A, content side), the content-prose edits the C-prune implies (lifted-crossing-locality.md:15, vertex-operator-dictionary.md:1,3), and C's construction (research).

2026-09-06 chips on conj:hecke-monodromy-step-two, all lean-direct exit 0, axioms propext/Classical.choice/Quot.sound: HeckeMonodromy.shadow_braid / shadow_far_comm / shadow_isUnit / shadow_coxeter (the shadow is a Coxeter representation of S_n); ColourCubicDiscriminant.colourDiscriminant_sos (D = (4z³+3z²+3z+4)² + 2z²(z²+1)), _reciprocal (z⁶D(1/z)=D(z)), _root_iff_inv; ColourCubicDiscriminantReal.no_real_branch_point. Two of the probe's 11 assertions (reciprocal; none real) are now theorems. Conjecture itself unchanged, open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
