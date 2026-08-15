---
# qou-kx04
title: 4 more witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1885 -> 1889)
status: todo
type: task
created_at: 2026-08-15T22:39:50Z
updated_at: 2026-08-15T22:39:50Z
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
