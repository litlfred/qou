---
# qou-0z4i
title: 'GAP: AGENTS.md L1 row states 65/50 dps; live default is 70/60'
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:21:27Z
updated_at: 2026-09-11T15:49:50Z
---

Measured 2026-08-30 on branch claude/srvu-drain-a-2026-08-30, no QOU_* env
vars set:

    python3 -c "import qou_substrate.precision as P; print(P.COMPUTE_DPS, P.OUTPUT_DPS, P.PRECISION_GUARD)"
    -> 70 60 10

AGENTS.md, table under "Precision goals (STRICT)", L1 row, still reads:

    met -- `_precision.py` default is 65 dps compute / 50 dps serialization
    (10^-50 absolute truncation)

Live is 70 dps compute / 60 dps serialization / 1e-60 truncation. All three
numbers in that parenthetical are stale.

NOT a regression: the change is strictly a tightening, and it is visible in
witness diffs as `precisionMetadata` 65/50/15/1e-50 -> 70/60/10/1e-60 when an
old producer is re-run. Recomputed values agree with the committed ones over
their entire shared prefix, so no recorded result is invalidated -- only the
documented figure is wrong.

Surfaced by re-running two producers under bean qou-srvu:
  computations/cyclotomic_depth3_dimension_pslq.py   (witness dated 2026-05-11)
  computations/bring_trilog_zeta5_depth_3.py         (witness dated 2026-05-29)

Not edited in that PR because AGENTS.md is contested across sibling branches
and a one-line doc fix there would conflict with four concurrent srvu agents.

## Still live, and it cost a PR body (2026-09-06)

Re-measured today, unchanged: `COMPUTE_DPS 70 OUTPUT_DPS 60 GUARD 10`.

Concrete cost of leaving the AGENTS.md row stale: PR #6937 (window transfer
speedup, merged) states "65 dps" twice in its body and names "the 50-dps
floor" as the target of the one remaining optimisation lever. Both came from
reading the stale L1 row rather than the module. The wall-clock measurements
in that PR are unaffected, but the *size of the unexplored lever* is
understated: 70 -> 60 is more headroom than 65 -> 50.

This is the second documented instance of the stale row propagating into a
durable artifact. It is a three-number edit to one table row.

## DRAINED — PR #6945 (2026-09-06)

Four sites, all fixed. The population is much smaller than the symptom count,
and recording that is the point:

| | count |
|---|---|
| files matching `65 dps` / `50 dps` | ~60 |
| **actual defects (a claim about the live DEFAULT)** | **4** |

The ~56 non-defects are 'computed at 50 dps' describing a SPECIFIC
computation — correct, and it STAYS correct, because 50 is the floor and the
default moved above it. Plus filenames (`atomic_tr_m_mpfr_50dps.py`),
deliberate explicit `mp.dps` settings, and dated audit records.

The four:
- `AGENTS.md` L1 row
- `docs/precision-goals.md` (the code block AND the prose beneath it)
- `content/.../appendix-mass-binding-algorithms/mba-sidecar-witness-json-pipeline.md`
- `content/.../appendix-mass-binding-algorithms/mba-step08-jet-prefix.md`

The last two matter most: that appendix is the maintenance contract AGENTS.md
requires to stay in sync with the actual compute, and a docs-only sweep would
not have reached them.

Each site now carries the measuring command rather than only a number, and the
AGENTS.md row names the retired figures explicitly so the next agent who finds
65/50 in a dated audit doc does not 'correct' it back.


## 2026-09-11 — CLOSED, and a FIFTH site existed in one of this bean's own named files

Off the `qou-bstl` queue. Verified the drain, and found one more.

**The four named sites are correct.** AGENTS.md's L1 row carries
`70 dps compute / 60 dps serialization`, names the retired 65/50 explicitly so
the next reader does not "correct" it back, and gives the measuring command.
`docs/precision-goals.md:168` carries `COMPUTE_DPS_DEFAULT = 70`. Live values
confirmed by import: **`COMPUTE_DPS 70  OUTPUT_DPS 60  GUARD 10`**.

**🛑 But `docs/precision-goals.md` contradicted itself.** This bean lists that
file as drained *"(the code block AND the prose beneath it)"*. The code block at
`:168` was fixed; the **prose at `:105` was not**, and it carried a **third**
figure:

    :105   `_precision.COMPUTE_DPS_DEFAULT = 50` gives ~35 digits of headroom
    :168    COMPUTE_DPS_DEFAULT  = 70

So one file asserted 50 and 70 sixty lines apart, and the stale half is the one
in running prose — the half a reader meets first. Fixed here to `70` / `~55`,
with the measuring command inline and a note naming the retired figure.

**Why the drain missed it, and it is the familiar shape.** The search was "by
symptom" for the retired figures, and this site does not spell `50` as a *dps
figure* — it spells it as a **code assignment**, `COMPUTE_DPS_DEFAULT = 50`,
inside prose. A scan keyed on "65" / "50 dps" / "10⁻⁵⁰" does not match it. Same
family as everything else in this corpus's blindness taxonomy: the value was
present under a rendering the detector did not enumerate.

Authority for fixing rather than filing: **exemption 1** (it makes a wrong
precision figure impossible) and **exemption 2** (the corpus decides it —
`qou_substrate.precision.COMPUTE_DPS` is 70, and the same file's own code block
already said so, so a reviewer checks my edit against the module rather than
against my reasoning).

Preflight: `scripts/check-sidecars.sh` clean, fences balanced, no math added.
`docs/` carries no `.qa.json` sidecar, so no `qa-sweep` applies.

**qou-0z4i closes.**


## 🛑 CORRECTION 2026-09-11, on rebase: a sibling fixed that line THREE DAYS BEFORE me

The section above says I found and fixed a fifth site, `docs/precision-goals.md:105`,
reading `COMPUTE_DPS_DEFAULT = 50`. **The finding was correct on my branch and
wrong about `main`.** Rebasing onto `main` (74 commits ahead) conflicted on
exactly that line, because the 2026-09-08 currency pass had already fixed it —
and cited this bean while doing so:

    `_precision.COMPUTE_DPS_DEFAULT = 70` (60 output + guard 10; read `50`
    here until 2026-09-08 — live value per `qou_substrate.precision`,
    bean `qou-0z4i`)

So the drain was *not* incomplete; my branch was 74 commits stale. **Their version
is kept, mine dropped** — it is better sourced, and overwriting a landed sibling
fix with a duplicate is the wrong move regardless.

**One real difference survived, and it is worth stating rather than silently
picking a number.** The two versions disagree on the headroom:

    theirs   70 (60 output + guard 10)  ->  ~45
    mine     70                         ->  ~55

Both are right about different quantities. Headroom below 1 ppQ (10⁻¹⁵) is
`60 − 15 = 45` from the **serialized** output — what actually reaches a consumer
— and `70 − 15 = 55` from the **compute** precision. The pre-2026-09-08 text
(`= 50` → `~35`) used the *compute* figure, so the currency pass silently changed
the convention as well as the number. Kept theirs and added one sentence saying
which is which, so the next reader does not "correct" 45 back to 55 or vice
versa. That is the same normalisation-vs-discrepancy confusion AGENTS.md flags
for the `c₃` 3.47 %/3.35 % pair.

**This is the THIRD staleness artifact from this branch this session** — after a
`Q0_PARSE_ERROR` on a witness that is 0 bytes here and 6018 on `main`, and a
`--help` crash fixed on `main` by `76ecd01eebb`. All three read as live findings
and none was. The bean stays **completed** (the four named sites are genuinely
drained), but the "fifth site" claim is withdrawn: there were four, and the fifth
was my tree.
