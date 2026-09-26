---
# qou-9ot5
title: 'Session: low-isotope mass+binding dashboard — error provenance, convention-D migration audit, cheat-sheet alignment, work plan'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-25T16:28:09Z
updated_at: 2026-09-07T19:11:30Z
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


### Correction, same day — the Case-C crash is DOCUMENTED, and my proposed fix was wrong

I recorded `derived-w-overdetermined-test` as *"cannot re-run"* with the
`RuntimeError`, and proposed *"implement or guard `tr_m_word_lq` Case C"*.
Corpus-grep (path 6 + the producer's own source) says otherwise on both counts.

**Not a discovery.** The probe's own docstring carries a heading —
`*** 🛑 THE DECIDING TEST IS BLOCKED, AND NO CONCLUSION IS DRAWN FROM ONE ATOM ***`
— and states that `tr_m_atomic_mpfr` raises exactly this on interface-suffixed
words at `n = 9`, so 3H and 3He cannot be evaluated on the fast exact path, and
*"2H alone is one atom and one free constant: fitted by construction, and it
proves nothing."* The crash stands as the reason the witness cannot be
regenerated; it is not a new defect.

**And the fix I proposed is the wrong one.** The probe names the right one:
*"The seminormal-matrix route has no Case C and would settle it at `n = 9`;
that is the next step."*

**A near-miss worth keeping.** The message originates in Rust
(`tools/hecke-engine/src/tr_m_word_lq.rs:325`) and PyO3 surfaces it as
`RuntimeError`, while the documented Case-C contract names
`NotImplementedError` — `laurent_q_trace.py:25` (*"callers route the WHOLE
element through `markov_trace_canonical.tr_M_element`"*) and
`markov_peel_rust_bridge.py:349` (*"caller routes to
`markov_peel.tr_M_atomic`"*). I nearly filed that exception-type mismatch as a
defect silently disabling a designed fallback. It is a real hazard in the
abstract and is **not** what is happening here: that contract governs those two
paths, not `tr_m_atomic_mpfr`, and no handler on this path attempts the catch.
Corrected on the PR before it could mislead.


### Correction 2026-09-07 (2) — my reason for leaving the last `Q0_FLIP` alone was REFUTED by a sibling, before I wrote it

I recorded the residual `Q0_FLIP: 1` as *"`hadron-knot-table.witness.json` on
the retired muon anchor; AGENTS.md records that producer takes > 50 min for one
bound atom of nineteen and will not finish."* **The conclusion (do not re-run
it) is right. Both halves of the reason are wrong**, and `qou-i7ju` had already
established that.

1. **The anchor attribution is refuted.** `qou-i7ju` §"RESOLVED 2026-09-05":
   *"the anchor hypothesis is REFUTED. It is a stale extension build."* The
   11.6 ppb anchor move does not explain the disagreement; a stale
   `pyhecke_native` kernel does.
2. **"Cannot finish" is obsolete.** `0c957c179b` (2026-09-05) made the producer
   **checkpoint per atom** — its own message names my reason and retires it:
   *"The witness was written ONCE, after all 19 atoms, so a run that did not
   reach the end produced NOTHING … That — not the difficulty of the numbers —
   is why it sat stale on main."*

**And the real reason not to touch it is stronger than either.** `qou-i7ju`
records that the producer currently yields a quantity **of the wrong sign**, at
~840 s per bound atom, so a bounded run would replace a **complete** committed
table — verified today: 19 atoms, 23 assertions, `computedAt 2026-06-17` — with
a partial one flagged `NON-CANONICAL ROSTER`, publishing *"19 wrong-signed
numbers that look freshly computed."*

So: **not mine to drain, and not drainable by re-running.** `qou-i7ju` (high,
todo) owns it; this is settled mechanical work with one owner and I am recording
the correction, not duplicating the analysis.

Live counts on `main` `2a6e0828b2` after the session's merges plus sibling
drain: `Q0_OK` **1451**, `Q0_ANCHOR_UNRECOGNISED` **1**, `Q0_FLIP` **1**.
