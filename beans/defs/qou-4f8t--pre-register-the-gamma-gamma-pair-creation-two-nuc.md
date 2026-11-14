---
# qou-4f8t
title: Pre-register the gamma-gamma pair-creation / two-nucleon tower vertex (owner ask 2026-10-11, undelivered)
status: todo
type: task
priority: high
created_at: 2026-11-14T07:02:23Z
updated_at: 2026-11-14T09:00:13Z
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
