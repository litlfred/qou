---
# qou-kx04
title: 4 more witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1885 -> 1889)
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T22:39:50Z
updated_at: 2026-08-16T00:24:17Z
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
