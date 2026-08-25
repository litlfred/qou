---
# qou-82ur
title: 'q0-anchor-consistency audit witness is stale on main: counts moved'
status: todo
type: task
priority: normal
created_at: 2026-08-16T12:56:54Z
updated_at: 2026-08-25T17:47:38Z
---

Surfaced by running scripts/precision-gates.sh on a clean checkout of main (PR #5229 branch, no relevant changes of my own — my new file is not even scanned; 'wenzl' appears 0 times in the diff). So this is PRE-EXISTING staleness on main, not branch drift.

Three committed audit witnesses regenerate differently from their committed copies:
  computations/audits/q0-anchor-consistency-audit.witness.json
  computations/q0-value-drift-audit.witness.json
  computations/witness-raw-float64-audit.witness.json

COUNTS moved, not just computedAt/commitSha/durationMs — so per the gate's own
rule this is genuine staleness, not the ignorable drift class:
  Q0_OK              653 -> 652
  Q0_ANCHOR_MISSING 1885 -> 1886
  Q0_INDEPENDENT       5 -> 6
  (total scanned 2543 -> 2544, i.e. one newly-scanned file plus one
   reclassification)

The two entries that moved are chi-tritium-h9.witness.json — which LOSES
"class": "proton-pin" and its ppb_vs_canonical: -11.537117889987831 — and
markov-identity-symbolic.witness.json, which is newly listed.

DELIBERATELY NOT FIXED on PR #5229. That PR is a science PR the owner is
reviewing (Wenzl level family); landing an unexplained q0-anchor
RECLASSIFICATION inside it would be noise at best and a hidden change at worst.
The chi-tritium-h9 line in particular touches the muon/proton pin bookkeeping
(-11.537 ppb is the mu-p substrate tension) and deserves its own look rather
than riding along in a diff about Hecke traces.

Next step: work out which upstream commit changed chi-tritium-h9's anchor
classification, confirm the new counts are correct, then commit the regenerated
witnesses as a chore(witness) commit naming the counts.


## Re-measured 2026-08-25 on `main` @ 5483aa95f — and the "confirm the counts" blocker is partly discharged

Reached independently while merge-verifying #5754, before finding this bean.
The staleness persists nine days on, and the corpus has moved underneath it, so
the 2026-08-16 figures above are themselves stale — do not chase them:

    2026-08-16 (this bean)  Q0_OK  653 -> 652    total scanned 2543 -> 2544
    2026-08-25 (today)      Q0_OK  963 -> 970    total scanned ~2758

### The next step asks to "confirm the new counts are correct". Here is that confirmation, for one dimension.

A sibling agent on PR #5770 reached `Q0_OK = 970` from an unrelated branch and
**reverted** the regenerated witnesses, on the reading that a bare container had
contaminated them (no `numpy`/`scipy`/`sympy`/`clarabel` installed, `mpmath
1.4.1` against the corpus's `1.3.0`).

That reading is right about the `environment` block and **wrong about the
counts**, which is the half that matters here. My container has a materially
different profile — `mpmath 1.3.0`, plus `numpy 2.4.6` / `scipy 1.17.1` /
`sympy 1.14.0` all present — and reproduces **970** exactly. Two containers
disagreeing on four packages and an mpmath minor version, same number.

Structurally they must, and this is the part worth keeping:

  * `witness_raw_float64_audit.py` imports `argparse`, `json`, `sys`,
    `pathlib`. Nothing else, no `subprocess`, no `importlib`.
  * `q0_anchor_consistency_audit.py` imports the same four, plus
    `witness_base.WitnessBuilder` and `qou_substrate.witness` to emit.

Neither imports a numerical library; neither invokes a producer. They **scan
committed JSON and count**. A count produced that way cannot vary with the
installed package set, so the counts are corpus facts and `963` is simply
stale.

### What this changes about the fix

The instinct to revert from a bare container is backwards for these files.
Reverting preserves a wrong count, and every future bare container will keep
re-deriving the same correct-but-unclaimable number. The right move is the one
already written above — regenerate and commit as `chore(witness)` naming the
counts — with one added constraint: do it from a container whose `environment`
block is faithful, so the counts land without the provenance lying beside them.

### Still open, and deliberately not claimed

I did not identify *which* 7 witnesses moved, and did not check whether
`STALE 229 -> 228` shares the explanation. Both look like the same staleness;
neither is measured. The `chi-tritium-h9` anchor-reclassification question in
the original finding is untouched and remains the substantive part of this
bean — the environment argument above says the counts are trustworthy, not
that the reclassification is understood.
