---
# qou-9ot5
title: 'Session: low-isotope mass+binding dashboard — error provenance, convention-D migration audit, cheat-sheet alignment, work plan'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-25T16:28:09Z
updated_at: 2026-09-07T10:22:57Z
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


## 2026-09-07 — the blocking q0-anchor gate is RED on main, and re-running one witness surfaced a 45 % drift

Re-measured this bean's `Q0_FLIP` reading. Live: **`Q0_OK 1429`, `Q0_FLIP 1`,
`Q0_ANCHOR_UNRECOGNISED 4`** — and `q0_anchor_consistency_audit.py --strict`
**exits 1** on either, with `precision-gates.sh` registering that gate
**blocking**. So the gate is red on `main` today.

**Root cause of the 4: two vocabularies for one concept.** `physical_proton`
is the **manifest** token (`q0_anchor_manifest.json`); the witness field wants
`proton`. A producer author writing the manifest spelling does the natural
thing and fails the gate.

**Two wrong hypotheses of mine, recorded because the shape recurs.** I first
supposed `stamp_staleness_metadata` concatenated anchor+reason — it writes the
argument verbatim. Then that a payload `q0Anchor` won — no such key exists in
the producers. `git log` settled it: at `2e68bb647d` (09-03) two producers
literally passed `q0_anchor="proton (experimental pin)"`, and `c415d81fe7`
(09-04, *"fix the 13 producers, not the witnesses"*) fixed those two and
**missed the other two**, which still passed `physical_proton`. That miss is
why the drain refilled.

**Also recorded: a re-run that timed out is not a measurement.** My first
attempt returned `exit=124` at 900 s having written nothing, and the
`q0Anchor` I read back was the unchanged on-disk value. I nearly reported it
as fresh.

### Outcome, 4 witnesses

| witness | result |
|---|---|
| `d-eigenphase-projection-through-ladder` | producer fixed, re-run **allPassed**, diff **anchor-only** — committed |
| `habiro-pochhammer-convention` | producer fixed; **witness re-run REVERTED, see below** |
| `derived-w-overdetermined-test` | **cannot re-run** — `RuntimeError: tr_m_word_lq: Case C (multiple top-1 in segment) not implemented; word=[1,0,0,1], n=3` |
| `interface-w-deciding-test` | long-compute (>15 min), still running |

**The `habiro` finding is the substantive one.** Its re-run moved every number
by 45–52 % — `witness_tr_M_at_q0` proton `1.145759692457300816435` →
`0.6293284022029219051444`, neutron `0.987743688115809530983` →
`0.4751335171556822112807`; `rel_err_1_minus_u_2k` `5.075 → 3.596` and
`3.622 → 2.015`. **My edit was one line of metadata and cannot do that.** So
the committed witness (computed 2026-09-06) disagrees with today's import cone
— textbook `cosmetic_import_cone_drift`, the one bucket measured growing 4 → 9
this same session (`qou-e9pp`).

Worse, the witness's own assertion prose is hardcoded: it still reads *"Not a
rounding question: **507 % and 362 %**"* beside recomputed values of **359.6 %
and 201.5 %**. The qualitative conclusion survives; the quoted figures do not.

**So its witness was REVERTED and only its producer fix committed** — the same
producer-without-witness split I criticise above, taken deliberately here
because baking a 45 % undiagnosed move into a metadata PR would be laundering.
That witness stays `Q0_ANCHOR_UNRECOGNISED` for a **documented** reason.

**Not drainable, and do not try:** the remaining `Q0_FLIP: 1` is
`hadron-knot-table.witness.json` on the retired muon anchor; AGENTS.md records
that producer needs >50 min for one bound atom of nineteen and will not finish.

**Follow-ups (none attempted):** adjudicate the habiro drift; implement or
guard `tr_m_word_lq` Case C; reconcile the manifest vs witness anchor
vocabulary at the source so the two spellings cannot diverge again.
