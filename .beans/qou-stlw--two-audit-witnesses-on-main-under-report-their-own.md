---
# qou-stlw
title: 'Two audit witnesses on main under-report their own live counts (stale-low ratchets)'
status: completed
type: bug
priority: normal
created_at: 2026-08-28T00:00:00Z
updated_at: 2026-08-28T00:00:00Z
---

Surfaced 2026-08-28 by `scripts/precision-gates.sh --changed`, which re-runs
producers to check drift and then reverts anything drift-only. The run was
killed by a 2-minute cap before the revert step, which is how two substantive
regenerations became visible instead of being tidied away.

## Measured

Both are **substantive**, not ephemeral — no `computedAt`/`environment` masking
explains them:

| witness | field | committed | live |
|---|---|---|---|
| `mpf-import-time-dps-audit` | `files_with_findings` | 11 | **12** |
| | `literal_findings` | 0 | **1** |
| `q0-value-drift-audit` | `proton-pin` | 1745 | **1749** |
| | a recorded `value` | 50 digits | **68 digits** |

Both move in the direction that matters: the committed artifact reports **fewer**
findings than the corpus currently has. A ratchet whose recorded count is
stale-low is slack the gate will not notice being taken up.

## Not caused by the branch that found it

Checked rather than assumed: stashed the only `computations/` edit in flight
(`binding_hbarq_rung_forward_test.py`), restored the witness, re-ran the
producer — the diff reproduces identically (3 insertions / 3 deletions). So this
is pre-existing on `main`.

The two stray regenerations were reverted rather than committed; they are not
this branch's to land.

## What is NOT established

- **Which** file is newly flagged. The witness records counts, not a path list
  under any `file`/`path` key the diff exposes, so the new `literal_findings: 1`
  is not identified here. Whoever picks this up should re-run the producer and
  read its stdout, which does name sites.
- Whether the `q0-value-drift` move (1745 → 1749, and a value string widening
  from 50 to 68 digits) is a real drift or a producer-precision change. The
  digit widening looks like the latter, which would make the count change a
  side effect rather than four new drifting sites. Do not quote "4 new sites"
  without checking that.

## Why it is worth a bean rather than an inline fix

Refreshing either witness is a one-command re-run, but committing a ratchet
artifact whose *cause* is unidentified is how a stale-low baseline gets blessed.
Identify the newly-flagged site first, then refresh — in that order.

---

## RESOLVED 2026-08-28 — and this bean's own framing was wrong on the first witness

Both causes identified before refreshing, which is the order this bean asked for.

### `mpf-import-time-dps-audit` — the witness was NOT stale-low. The corpus had regressed.

The bean says the committed artifact "reports **fewer** findings than the corpus
currently has… slack the gate will not notice being taken up." That reading is
backwards here. Running the producer names the site the witness could not:

    NEW files building mpf before precision is raised
      literal=1  expr=0   computations/audits/y_lambda_two_row_cap_gate.py

That file landed **today** (`25e8f8c1d9`, "assert the convention-D two-row cap at
the TABLE"), after the witness was committed. `CAP_RATIO_MAX = mp.mpf("1e-30")`
sits at module scope on line 47 while `mp.mp.dps = 60` is set on line 134 inside
`main()` — so the threshold is built at mpmath's default 15 dps and every
comparison against it uses the truncated value.

So the committed witness was the **honest record of a clean corpus**, and the
11→12 / 0→1 was a real regression arriving after it. Refreshing the witness
would have recorded the regression as the new normal — exactly what the
producer's own output forbids: *"fix AT THE SOURCE (idempotent
set_compute_dps() at module scope, ABOVE the constant). Do NOT add the file to
the baseline to silence this."*

**Fixed at the source.** `set_compute_dps(60)` at module scope above the
constant. After it: `literal 1 → 0`, `NEW files 1 → 0`, `REGRESSED 0`, and the
gate still passes with identical verdicts on all four rows. The witness is now
**byte-identical to the committed one** — no refresh needed, which is the
correct outcome and the opposite of what this bean predicted.

(Also visible in that run and worth recording: **83 files drained** since the
baseline, 185 literal findings → 0. Others have been working this hard.)

### `q0-value-drift-audit` — two different fours, and one of them is mine

The bean warns: *"Do not quote '4 new sites' without checking."* Correct, and
sharper than it knew. Isolated by running the audit against the pre-stamp
witnesses and again with them:

| | `canonical` | `proton-pin` |
|---|---|---|
| committed baseline | 167 | 1745 |
| pre-stamp, current corpus | 167 | **1749** |
| with my four `1j39` stamps | **171** | 1749 |

- **`proton-pin` 1745 → 1749 is genuine pre-existing drift** — present without
  any change of mine.
- **`canonical` 167 → 171 is entirely my own**: the four `q0Value` keys the
  `1j39` stamp added in this same branch each register as a canonical-class
  entry.

A reader diffing this witness after both changes landed would see `+4` twice and
have no way to tell them apart. Recorded here so nobody attributes the canonical
four to corpus drift.

- The digit widening the bean flagged (a recorded `value` going 50 → 68 chars,
  `ppb_vs_canonical` `4.17e-41` → `0.0`) is a **producer-precision improvement**,
  not drift: the canonical muon reference is now carried at full width, so the
  residual against itself is exactly zero rather than a truncation artifact. The
  bean guessed this correctly.

Witness refreshed, with both causes known.

---

## Status flip 2026-08-28 — this bean sat at `todo` with a RESOLVED section above it

Recorded rather than silently corrected, because the failure is the one
AGENTS.md §3 exists to catch: I wrote the resolution into the body and never
changed `status:`. A reader running `beans list` saw an open item; a reader
opening the file saw a closed one. Both halves are required and I did one.

The work itself is done and merged (#5899, and `ad65db8d49` for the
`y_lambda` half — see below). Flipping to `completed` now.

### Cross-reference, and a duplicate of mine

A sibling filed **`qou-6gdb`** for the same `docs/audits` float64 finding at
15:50, before my `qou-f64d` at ~18:00 — so **`qou-f64d` duplicates it**. Theirs
is now `scrapped` with the note *"Nothing to merge. The gate is green on main
via their fix"*, i.e. they saw mine land and stood down. The coordination
worked; the duplicate bean is the cost of my not grepping `.beans/` for the
finding before filing. That is corpus-grep path 6, which I did not run.

Their bean also records, accurately, that my `qou-stlw` *"landed only an audit
doc"* on the `y_lambda` half — correct: I dropped my code fix mid-rebase in
favour of theirs (`ad65db8d49`), which is what main carries.
