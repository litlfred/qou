---
# qou-82ur
title: 'q0-anchor-consistency audit witness is stale on main: counts moved'
status: todo
type: task
created_at: 2026-08-16T12:56:54Z
updated_at: 2026-08-16T12:56:54Z
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
