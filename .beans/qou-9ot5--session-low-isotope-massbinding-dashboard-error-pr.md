---
# qou-9ot5
title: 'Session: low-isotope mass+binding dashboard — error provenance, convention-D migration audit, cheat-sheet alignment, work plan'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-25T16:28:09Z
updated_at: 2026-08-25T18:20:23Z
---

## Session state 2026-08-25 (PR #5765)

### Delivered
- **Dashboard run fresh** (`--group low`, exit 0). The checked-in
  `dashboard_raw_output_low.md` was stale in both its column set and its pin;
  dated by arithmetic attribution to **pre-2026-08-08** (its header
  `pp=0.695 pn=0.534 nn=1.237` matches z_C + Reeb-override + no-writhe exactly,
  3/3; live matches z_D + writhe + trace-pn exactly). Blast radius downstream: zero.
- **`docs/audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`**
- **`docs/audits/2026-08-25-cheat-sheet-paper-alignment.md`**
- **`docs/workplans/2026-08-25-mass-binding-compute-update-workplan.md`** (5 tiers)
- **Tier 0 mechanical fixes** to `docs/canonical-derivation-cheat-sheet.md`: the
  `beats_100x_count` STRICT violation, four numerics recomputed at >=40 dps, three
  dead labels.
- **Tier 0.1**: Step 2 downgraded from "proved" with the `§2a` substantiation.

### The headline answer
Staleness is **<= 10 %** of the binding error and **0 % at 4He**; **>= 90 %** is a
missing term. The live cone is already convention-D + proton + `bring_color_weighted`
(runtime trace, three independent arithmetic confirmations). The one lever with real
leverage - convention D - is already pulled and moved A>=3 accuracy **against** the
target by 27-40 %.

### Three corrections I made to my own claims this session
Recorded because the pattern is the point, not the individual errors.

1. **GAP-1 "cheapest derivation item" - RETRACTED.** Reachability under D is real
   (d_req/h = -0.119453446, reproduced to 9 digits) but closing it by choosing `d`
   is a fit, and `content_keyed_interface_refuted` + the exact flavour-only
   3S1/1S0 degeneracy (`mu(3S1) = mu(1S0) = 0.18614164195799085217`, verified)
   bar the route. Full correction in `qou-5d6k`.
2. **Tier 2 "11 sites to migrate" - RE-SCOPED.** #5767 measured the same 11
   independently and showed it is a **floor**: 9 are in the qbeta/decay cone where a
   z-swap is invalid (`decayLadder_zC_threeRow_ne_zero`), needing `qou-cds1`.
3. **Tier 1.4 "ADJUDICATE, do not flip" - WRONG.** #5767 found
   `binding_canonical.py`'s convention line was the *symptom*; its symbolic path had
   no branch at all for the weighted interface. Leaving it alone would have been the
   error my caution invited.

Also qualified my own **`Q0_FLIP = 0`** reading: it does not establish a witness was
*computed* at its stamped anchor (the audit compares stamp fields to each other).
Verified against `q0_anchor_consistency_audit.py`; the instance #5500 named is closed
on the current tree, so cite the mechanism not the example.

### Coordination
Posted on **#5767** (mutual convention-C findings), **#4804** (deuteron + K_A
pairwise ceiling), **#5755** (the Q0_OK mechanism), **#5500** (two asks, no reply),
**#5770** (confirmed no file overlap - different cheat sheet).

### Open, needing the owner
1. Ordering: remaining Tier 0 items vs Tier 3.1 vs Tier 4.
2. Whether to open **a space index on the interface carrying L** as a construction -
   the only route past the 3S1/1S0 degeneracy, and a substantial build.

### Child beans
`qou-fdjp`, `qou-ahbz`, `qou-04cj`, `qou-5d6k` (carries the GAP-1 retraction),
`qou-ib3g`.
