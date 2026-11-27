---
# qou-4f8t
title: Pre-register the gamma-gamma pair-creation / two-nucleon tower vertex (owner ask 2026-10-11, undelivered)
status: todo
type: task
priority: high
created_at: 2026-11-14T07:02:23Z
updated_at: 2026-11-27T15:10:00Z
parent: qou-cxh0
---

Owner, 2026-10-11 verbatim: "let's go through gamma-gamma production step by step to get to one and two nucleons. each collision/interaction shifts things up the tower." NOT delivered: the gg_ntower probe has no quark letters and only one nucleon's worth of collisions, and says so.

Its results doc lists what was not tested: "placements that are not a rigid shift, closing from the bottom, pair creation by Jones projections (two strands per collision), quark letters, gluons, or two nucleons."

Outcome (ii) stands for every placement that climbs: no shift but s=0 (which does not climb) admits for any k up to n=9. For s=-1, +-2, +3 the (2,1) character is already negative AT q=1, so that failure is an order-zero permutation fact, not a q-deformation effect.

Binding rulings: gluon tail ALLOWED (2026-10-11); "every level" = every strand count m=3..n (2026-10-12); quark sign map option 4, "derive it, do not pick it" (2026-10-12).

NO FITTING: F_required = 1.75923699418 is a post-hoc CHECK only, never a search target and never a tie-breaker. The gluon family straddles the target, so closeness cannot select.



## 2026-11-14 — MECHANISM half done, DELIVERABLE half still open

The pair-creation vertex is now settled and it is a **negative with a named
invariant**: `gg_scalar_per_step_probe.py` (8/8), scope (b). Every "fresh strands
per collision" construction joined by a chain or a cabled double singlet gives a
scalar per step, so its step index is an unbounded knob and reading 3 — which
admits every value of it — cannot bound magnitude. Details on `qou-cds1`.

**Still open, and it is what the owner actually asked for on 2026-10-11:** one
nucleon (H_6 → H_3) and two nucleons (H_12 → H_6), with quark letters and
flavour, reading 3 at every strand count. The probe above delivers no nucleon by
construction. A sibling design for exactly that ladder was reviewed and its
central premise measured FALSE — it argued the convention-D trace is the two-term
sum `y_(3)χ_(3) + y_(2,1)χ_(2,1)`, but `χ_(3)(R_3) = 0` exactly for all 12 of its
configurations, so it collapses to one scalar anyway; and its widest admissible
difference was 0.0131 against a required 0.1869, with its parameters exhausted.
So do not rebuild that design as specified — the level structure (H_6→H_3,
H_12→H_6) is worth grafting, the magnitude expectation is not.

## 2026-11-27 — salvaged from closed #7817; owner ruled routes A + C

PR #7817 was closed unmerged on 2026-11-27 in the old-PR cleanup. Its probe, witness and results note are re-landed on `main` by PR litlfred/qou#9464, where the probe was re-run on current main with 8/8 passing and a byte-identical witness. The bean notes above (dated 2026-11-14) are copied here from that branch, because they never reached the beans branch.

Owner ruling, 2026-11-27, via a decision card in the project thread "C to D migration": **A + C**.
- **A**: rule a second structural criterion beside reading 3 that bounds magnitude. It must come from the decay channel's particle content, not from the residual, because a ceiling chosen so that the target survives would be a fit.
- **C**: build the H₆→H₃ (one nucleon) and H₁₂→H₆ (two nucleon) ladder with quark letters, and record the γγ residue with no magnitude expectation.
B (reopening the z_D base) is held.


## 2026-11-27 — routes A and C done (PR litlfred/qou#9530)

**A (scope b, invariant = writhe).** `QOU.MassTheory.ClimbingFamilyNeutralExclusion.not_neutral_support`, core Lean, sorry-free: every braid word of e₀e₂Σ₁ᶜ has writhe in [4c, 4c+2], and a linking-neutral word has writhe 0. So for c ≥ 1 the term-by-term neutrality rule (owner 2026-11-25) removes the whole family, and at c = 0 only the identity term survives. This holds in the braid group algebra of B₄, before the Hecke quotient (in H₄, e₀e₂Σ₁ = q²e₀e₂). The Nov 14 finding "the magnitude is free, it can only be picked" therefore does not survive the ruled filter: the climbing family is excluded, not free. Probe `climbing_family_neutral_exclusion_probe.py`, all checks pass.

**C.** `docs/audits/2026-11-27-cds1-route-c-gamma-gamma-ladder-gaps.md`. The H₃ endpoint V³ is selected, but only inside H₃. Still open: the H₆→H₃ and H₁₂→H₆ descents, derived quark letters, and a per-step residue for the ruled photon grammar on ≥ 4 strands. The audit lists three steps to close C.

Q_β magnitude remains OPEN; this bean stays open.

## 2026-11-27 — route C step 1: six-strand neutral selection (litlfred/qou#9536)

On six strands, V-words of length ≤ 6 (V_i = σ_iσ_{i+1}⁻¹, i=0..3): 5460 enumerated, 1906 neutral, 58 pass reading 3 at q₀, 11/10, 23/20 (exact, convention D). Every survivor uses each vertex a multiple of 3 times; minimal survivors are exactly V_i³; the rest are products of two cubes (overlapping non-commuting triples must be in blocks). Scope (a), length ≤ 6. No magnitude information; the Q_β gap stays open. Next: H₆→H₃ residue of the survivors (route C step 2). Audit: docs/audits/2026-11-27-cds1-six-strand-neutral-selection.md.
