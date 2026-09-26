---
# qou-6mij
title: witness-raw-float64-audit.witness.json is stale on main by 8 drain commits — the drain arc's own scoreboard understates its progress
status: completed
type: bug
priority: normal
created_at: 2026-09-07T16:57:58Z
updated_at: 2026-09-13T09:09:17Z
---

MEASURED 2026-09-07 on origin/main d8cf8983c, incidentally, while re-running the ratchet after merging main into PR #7077. Not that PR's to fix — recording rather than widening it.

COMMITTED (computations/witness-raw-float64-audit.witness.json):
  dirty_witnesses 1009, total_fields 31226, baseline_files 1009, baseline_fields 31226
FRESH RUN (python3 computations/witness_raw_float64_audit.py --strict, exit 0):
  dirty_witnesses  996, total_fields 28152
  NEW dirty 0, REGRESSED 0, drained since baseline 12 files / +2838 fields

So the committed scoreboard UNDERSTATES the arc's own progress by 13 witnesses and ~3074 fields.

PROVENANCE, and this is the part that makes it a bug rather than normal derived-artifact lag: the file was last written at ee4367aea (merge of #7060). EIGHT drain commits have landed on main since, without regenerating it —
  d8cf8983c  clear the three raw-float64 regressions that landed on main today
  2bd43761d  stop narrowing the accumulator's log to float64
  ac4a08bb7  the channel sums themselves were f64
  000ddda97  channel_product_mass rounded residuals to 4 decimals
  fa7ec3da3  the six-term sweep, 331 raw floats -> 0
  d61c1ddce  restore atomic_chirality_residue
  f2b1cbae1  the k-star search computed in float64
  09895fc01  exact coefficients truncated below float64 into Rust

WHY IT MATTERS. The ratchet's contract is that baselines DRAIN and never grow, and this witness is where that is read off. A reader taking the committed file as current sees 1009 where the tree is at 996, i.e. the arc looks stalled while it is in fact working — the inverse of the usual staleness risk and easier to miss for exactly that reason. Also the drained list names files whose own commits are in the eight above (complex-volume-unification, qbeta-reeb-tower-jacobi-anger, atomic-chirality-residue, channel-product-mass), so the evidence that they drained is present in the repo and absent from the scoreboard.

NOT ESTABLISHED: whether the arc's owner regenerates this deliberately at arc close rather than per-commit, in which case this is a cadence choice and not a defect. Ask before sweeping. FIX IF WANTED: re-run the producer and commit, one chore(witness) commit; it is seconds of compute.

Owners of the touching arcs: qou-r47m, qou-kfeg, qou-sv7h.


---

## RESOLVED 2026-09-13 — premise superseded, and the open question is ANSWERED: it is cadence, not a defect

**Do not act on this bean's figures.** Every number in it is superseded.

### The specific staleness was fixed by a sibling, six days ago

`5963642c40` (author 2026-09-11 14:51, bean **qou-n5kp**) — subject line:
*"gate(qou-n5kp): raw-float64 ratchet GREEN -- regressed 3 -> 0, and the audit
witness was itself stale"*. An independent agent reached the same finding from
the other direction and regenerated the file. The exact figures this bean
recorded as COMMITTED (dirty 1009, total 31226, baseline 1009/31226,
computedAt 2026-09-06) are that pre-fix state.

### The open question — "cadence choice or defect?" — is answered: CADENCE

This bean said *"NOT ESTABLISHED: whether the arc's owner regenerates this
deliberately at arc close rather than per-commit ... Ask before sweeping."*

The evidence now exists: **the arc owner DOES regenerate it, at a gate commit.**
So the answer is **do not sweep**, and the AGENTS.md 2026-09-07 ask-first rule
resolves the same way — regenerating it is neither a precision increase nor
corpus-derived, so it is not exempt, and the cadence is somebody else's call.

### Current state, measured today (main + this branch's 2 commits)

| | committed (`4a02360480`, computedAt 2026-09-11) | fresh run |
|---|---|---|
| dirty_witnesses | 992 | — |
| total_fields | 28,127 | **27,128** |
| baseline_files / fields | 1004 / 30,990 | 1003 / 30,985 |
| drained since baseline | — | 21 files, +3,857 fields |
| NEW dirty | — | **0** |
| REGRESSED | — | **0** |

So it is **behind again, by 999 fields, two days later** — in the same benign
direction the bean identified (it UNDERSTATES the arc's progress). That
recurrence is *evidence for* the cadence reading, not against it. The baseline
itself moved 1004 -> 1003 / 30990 -> 30985, consistent with the drain-only
contract.

### The reusable part: an ancestor check separated two true statements

Earlier today I ran this same ratchet while gating PR #7260 and reported **NEW
0 / REGRESSED 3** — `bar-pairing-binding-observable-extension`,
`binding-rotation-phase-lead`, `chi-free-via-lr` — as *"pre-existing on main,
none is mine"*, and published that in a PR comment. A fresh run hours later
gives **REGRESSED 0**.

Both are correct, about different trees, and the check that establishes it is
one command:

    git merge-base --is-ancestor 5963642c40 b25fa2b0b9   -> NO

`5963642c40` was NOT in the tree I gated. Its COMMIT date is 2026-09-11 (so it
was not rebase-rewritten on landing), yet it reached `main` between my two
fetches this morning — i.e. it sat on a sibling branch for two days and merged
today. Those three files are literally the "regressed 3 -> 0" of its subject
line.

**The lesson is the ordering.** The tempting reading of "I said 3, now it is 0"
is that my earlier measurement was wrong, and a correction published on that
assumption would itself have been false. Check whether the TREE moved before
concluding the MEASUREMENT was wrong — and note that a commit date alone does
not tell you when something landed, because a long-lived branch preserves it.
