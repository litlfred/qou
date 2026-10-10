---
# qou-kx04
title: 4 more witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1885 -> 1889)
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T22:39:50Z
updated_at: 2026-10-04T15:11:47Z
parent: qou-pq8k
---


The follow-on to `qou-rw91`, which is now closed. While reading the
`Q0_ANCHOR_MISSING` list-diff to identify rw91's third witness, the *next*
commit turned out to add four more:

```
7377d6624  chore(witness): refresh stale q0 audit witnesses (counts moved)
           Q0_ANCHOR_MISSING 1885 -> 1889
     + chi-numpy-dtype-fix-benchmark.witness.json
     + dt-crossknot-snappy-slope-hardening.witness.json
     + qbeta-decay-channel-convention-status.witness.json
     + qbeta-ohtsuki-nz-bridge-b6.witness.json
```

Deliberately out of scope for rw91: a different landing, and re-running four of
someone else's producers uninvited is not that bean. Left at 1886 after rw91's
three were declared.

**The vocabulary they need now exists.** `q0Anchor: "independent"` +
verdict `Q0_INDEPENDENT` landed in `b4b293fc` / `e6cc6ac5`, so a producer that
never reads q₀ can say so instead of being indistinguishable from one that
forgot. Per witness the question is only which of three is true:

- reads q₀ → declare `muon` or `proton` (proton is the standing default for new
  compute, owner directive 2026-08-07) with the matching `q0Value`;
- never reads q₀ → `w.save({"q0Anchor": "independent"})`, **no** `q0Value` (one
  there is now a `Q0_FLIP`);
- reads q₀ but the pin is undetermined → `ambiguous`.

Answer it from the **import cone**, not the top-level file. `qbeta-ohtsuki-nz-
bridge-b6` is the strongest candidate: its b4 sibling was verified q₀-free in
rw91 (π, √3, the exact Ohtsuki rungs, 4₁ geometry via `t2.V41_integrated`, whose
own imports are json/subprocess/datetime/pathlib/mpmath only), so b6 is very
likely the same — but *verify* it, do not inherit the verdict.

Trap, from `fcdefee4ed`: use `save(extra=...)`. `add_data("q0Anchor", …)` nests
under `data`, where the audit reading `body["q0Anchor"]` cannot see it — the
witness stays classified MISSING with the field visibly present.

Re-run the producer; do not hand-edit the JSON. All three rw91 producers
reproduced byte-identical numeric payloads, so a clean re-run is cheap evidence
that nothing else moved.

Also still unstamped and now expressible: `chi-deuteron-h6.witness.json` from
`qou-pin1`, a purely symbolic artifact that settled for "manifest `ambiguous`,
drop the stamp" because `independent` did not exist yet.


UPDATE 2026-08-16 (PR #5164, post-rebase). A full unscoped precision-gates run after rebasing onto 61 new main commits shows Q0_ANCHOR_MISSING 1886 -> **1888**: two MORE no-anchor witnesses landed on main in that window, on top of the four this bean already names. The count is growing faster than it is being drained, which is an argument for the anchor declaration being enforced at WitnessBuilder rather than chased per-witness after the fact. Q0_INDEPENDENT holds at 3, Q0_FLIP at 0.

Claimed 2026-08-16 by claude/agent-discussions-queue-gibk4e (session qou-pq8k).


## PROGRESS 2026-08-16 (PR #5164) — 3 of 6 declared

Verdicts from a transitive import cone (ast-based, follows ImportFrom through
computations/ probes/ qbeta/ substrate/), per this bean's instruction to answer
from the cone rather than the top-level file:

| witness | cone | verdict | re-run |
|---|---|---|---|
| dt-crossknot-snappy-slope-hardening | 3 mods, no q0 | **independent** | exit 0 |
| qbeta-ohtsuki-nz-bridge-b6 | 4 mods, no q0 | **independent** | exit 0 |
| qbeta-decay-channel-convention-status | reads q_at(DPS) | **proton** | exit 0 |

Counts: Q0_ANCHOR_MISSING **1888 -> 1885**, Q0_INDEPENDENT **3 -> 5**,
Q0_OK **649 -> 650**, Q0_FLIP 0. The -3 splits exactly 2 independent + 1 OK.

**b6 was verified, not inherited** — the cone agrees with the b4 expectation this
bean flagged, but the expectation was not the evidence.

**convention-status was not neglect.** It already recorded a q0_pin parameter
naming the proton pin; that lands under `data`, where the audit reading
body q0Anchor cannot see it — the fcdefee4ed trap, confirmed live.

**Method note for whoever takes the rest:** the cone is asymmetric. NO q0 in the
cone is conclusive. q0 IN the cone is only an over-approximation — a module may
import Q on a path the producer never evaluates. Both independents above rest on
the conclusive direction; the two below need the weaker direction resolved by
hand.

### STILL OPEN (2 of the named 4+1, plus the +2 drift)
- **chi-numpy-dtype-fix-benchmark** — cone 22 mods, reaches q_parameter
  Q_50_DIGIT_STR *directly* in the producer itself, so it plainly reads q0; the
  open question is only muon-vs-proton (computations-layer q_parameter is the
  muon witness, so likely **muon**, but that must be confirmed, not assumed).
- **chi-deuteron-h6** (from qou-pin1) — cone 19 mods, reaches q_parameter Q via
  hoefsmit_symbolic / hecke_core / mass_at_3A_proper. NOTE this contradicts
  qou-pin1's framing of it as 'a purely symbolic artifact': it is not obviously
  q0-free, and 'independent' is NOT the answer to reach for. Needs the
  over-approximation resolved before any declaration.
- The +2 that landed on main during the 61-commit window are still unidentified
  by name.

ENVIRONMENT: sympy (needed by convention-status) pins mpmath<1.4 and silently
downgraded 1.4.1 -> 1.3.0 on install. Restored to 1.4.1; all three witnesses
here produced under it. snappy installed for dt-crossknot.


UNCLAIMED 2026-08-16: progress above (3 of 6) is landed on main via PR #5164.
Set back to todo rather than left in-progress, since no agent is currently on
it — an in-progress bean with nobody working it is the state the work-plan
policy exists to prevent. The remaining two are described above; read the
method note on cone asymmetry before starting.


## PROGRESS 2026-08-16 (PR #5194) — the last two ANALYSED; artifacts withheld

**Correction to my own note above.** I wrote that `chi-numpy-dtype-fix-benchmark`
was "likely **muon**, since computations-layer q_parameter is the muon witness."
That is wrong. `computations/substrate/q_parameter.py` is not unconditionally
muon — it is manifest-driven: `QOU_Q0_ANCHOR` override, else the producer's stem
under `ideal_muon` in `q0_anchor_manifest.json`, else **proton**. Resolved
authoritatively with `resolve_q0_anchor` rather than inferred:

| producer | resolves | why |
|---|---|---|
| `chi_numpy_dtype_fix_benchmark` | **proton** | stem absent from the manifest -> 2026-08-07 standing default |
| `per_irrep_pole_deuteron_h6` | **ambiguous** | stem IS listed under the manifest's `ambiguous` set: both pin signatures present |

**And a correction in the other direction.** I wrote that the h6 cone
"contradicts qou-pin1's framing of it as a purely symbolic artifact". Half right:
q0 IS reachable (19-module cone), so `independent` would be false — but qou-pin1
had already settled on **`ambiguous`**, which is exactly what the manifest says.
Its instinct was right; my note was harsher than the evidence.

Both source declarations are committed. `ambiguous` here is a QUEUE ENTRY, not a
ruling: it moves h6 out of `Q0_ANCHOR_MISSING` (indistinguishable from a producer
that forgot) into the set that says a human must decide which pin the H6
per-irrep pole extraction evaluates at. No `q0Value` — one there would claim the
ruling has been made.

**The two witnesses were NOT regenerated, deliberately.** Both re-runs were
compromised by this sandbox's stack, not by the edits:

- `chi-numpy-dtype-fix-benchmark`: numpy 2.4.6 (installed in this session) flips
  `allPassed true -> false` and an assertion to `computed: false`, with
  durationMs 408402 -> 32485. The benchmark stops computing. Bean **qou-nz8e**.
- `per-irrep-pole-deuteron-h6`: committed under sympy 1.12 + scipy 1.17.1; this
  sandbox has sympy 1.14 and no scipy. Assertions did not move (the failing one
  is pre-existing on main), but a symbolic producer on a different symbolic
  stack is not evidence.

So the counts are unchanged from the mw1p end state (`Q0_ANCHOR_MISSING 1885`);
the stamps land on the next run in a sound environment. Withholding them is the
point: committing either would have shipped an environment artifact as a result.


## 2026-08-16 — a standing commitment on the b4/b6 reason wording (PR #5210 churn cone)

#5210 (`qou-cwin`) is authorised to re-express the Q_β precision ladder in
**h = q − 1/q** instead of **u = b·ℏ_q²**, and named `qbeta_ohtsuki_nz_bridge_b4/b6`
as in scope. They are explicitly **not** touching these witnesses.

Both `q0AnchorReason` strings name the coordinate:

- b4 — *"Taylor coefficients in a FREE parameter **u** against proved constants…"*
- b6 — *"Same free-parameter-**u** construction as the b4 sibling…"*

**Not changed, and deliberately.** After a u → h reframe these become mildly
anachronistic, not false: the audit-relevant claim is *"no substrate value is
read"*, and that is untouched by a change of coordinate. b4 is robust either way
— it carries the actual evidence (the proved constants, and the import-cone fact
that `sdeformed_channel_signflip_probe` imports only json/subprocess/datetime/
pathlib/mpmath, so the `y_lambda_at` muon-cache straddle is unreachable). b6 is
the thinner one, being largely by-reference to b4.

Regenerating two witnesses to correct wording that is still true would contradict
the discipline the rest of this bean was run under (see the two withheld
witnesses above). **Commitment posted publicly on #5194: if the reframe lands, I
fix the wording then.** Recorded here so it survives the session.

**The general lesson, which is the part worth keeping.** A free-text reason should
state the *invariant* — what is or is not read — and not the *incidental
coordinate*. b4 does this almost by accident (the evidence dominates the variable
name); b6 does not. Passed to #5210 because a `ladder_frame` reason field would be
far more exposed: its entire subject *is* the coordinate.


### 2026-08-16 15:1x — the commitment did NOT fire; strings stand

The #5210 work landed (`#5235 → e2d68dcdc`, `#5210 → 4f542c4d4`) with **much
reduced scope**: `LADDER_FRAME = "u"` in `qbeta_utils` plus a `ladder_frame` key
on `substrate_ladder_quantities`. **No `c_k` value changed and no witness was
regenerated** — the `c₄…` churn that PR originally warned about does not exist,
and `greedy_later_rungs_vanish` now proves it sorry-free.

So the frame **stayed `u`**. It landed a *declaration of* the u-frame, not a
move to h. The b4/b6 `q0AnchorReason` strings naming *"a FREE parameter u"*
describe a variable the producers still have; they are accurate and there is
nothing to fix.

The commitment stays live for a future PR that actually moves the rungs to h.
Recorded as a checked non-event rather than left looking pending — a standing
commitment nobody re-checks is indistinguishable from one nobody honoured.


## Re-checked 2026-09-06 — 3 of 4 done; the 4th is NOT refreshable here, and I am not committing it

Found by `scripts/bean-staleness-triage.py` (ranked 5th of 284 artifact beans,
71 commits over 2 paths). Measured per witness:

| witness | `q0Anchor` today |
|---|---|
| `dt-crossknot-snappy-slope-hardening` | **`independent`** ✅ |
| `qbeta-decay-channel-convention-status` | **`proton`** ✅ |
| `qbeta-ohtsuki-nz-bridge-b6` | **`independent`** ✅ |
| `chi-numpy-dtype-fix-benchmark` | **ABSENT** ❌ |

**The fourth's producer is already correct.**
`computations/chi_numpy_dtype_fix_benchmark.py:173` does
`w.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})`, under a comment
citing this bean and reasoning it out (it *does* read q₀ via `Q_50_DIGIT_STR`;
`q_parameter` is manifest-driven, and this stem is not under `ideal_muon`, so
proton). Only the **witness on disk** is stale — the same shape as the two
`Q0_ANCHOR_UNRECOGNISED` stragglers from #6699.

### Why I ran it and then threw the result away

Re-running does stamp the anchor correctly (`proton`, `1.10997858275138080759…`).
It also **flips the second assertion from passing to failing**:

> *"the pre-fix path is strictly slower on every partition — the leak cost real
> time rather than being a theoretical concern"* → **False**

Committing that would put a failing assertion into the corpus on the strength
of a measurement this container cannot be trusted to make. Reverted; not
committed. **Whoever closes this needs a machine where the benchmark's premise
holds** — one run there fixes it.

### Three hypotheses, two of them mine and disproved

Recorded so the next agent does not repeat them.

1. **Timing noise.** *Disproved.* Three consecutive runs give **identical**
   speedups — `0.7x 0.2x 0.3x` every time — and identical `allPassed=False`.
   Reproducible, not noise. I had called this "almost certainly" the cause.
2. **mpmath 1.3.0 → 1.4.1 broke the promotion.** The environments differ in
   exactly one entry (python 3.11.15 and numpy 2.4.6 match; the witness
   records mpmath **1.3.0**, this container has **1.4.1**), and the whole fix
   is about an `mpf` promoting a numpy product to `dtype=object`. *Disproved
   directly:* under 1.4.1, `np.ones((3,3)) * mp.mpf('1.5')` still yields
   `dtype: object`, and so does a matmul against it. The mechanism is intact.
3. **Import-cone drift** — the class AGENTS.md says actually bites.
   **Undecidable here:** the witness's `commitSha`
   `73f8fafac4a8a7369e0d1c7e4996e13e6270e50e` is **not in this shallow clone**,
   so the cone cannot be diffed. That is the `qou-wsha` "rewritten" class, and
   it is the standing reason "diff the producer first" is unrunnable for
   roughly half the witness corpus.

What the run *does* show, and what a fuller check should start from: the
benchmark prints `first non-float crossing at index None of 35` — i.e. **the
leak the fix targets is not occurring on this path at all**, which is why the
"fixed" route is pure overhead here. Whether that is the cone or something in
`d_for_ctype`'s callers is the open half.

**Bean stays open on the fourth witness only.** Three of its four are closed.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Reasons for Scrapping

Duplicate of `qou-6irj` (work-plan reorganisation 2026-10-04). Evidence: [B] increment of the same count (Q0_ANCHOR_MISSING 1885->1889) | STALLED in-progress, last update 2026-09-08 [M]
Content is untouched; only this work item is closed.
