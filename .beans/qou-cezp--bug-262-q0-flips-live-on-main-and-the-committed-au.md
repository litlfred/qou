---
# qou-cezp
title: 'BUG: 262 Q0_FLIPs live on main, and the committed audit witness reports a false green'
status: completed
type: bug
priority: normal
created_at: 2026-08-19T17:46:48Z
updated_at: 2026-08-24T12:40:38Z
---

Found while running precision-gates for an unrelated probe (qou-unqc).

    computations/audits/q0_anchor_consistency_audit.py --strict   ->  exit 1
        Q0_FLIP      : 262      (anchor != value -- the flip-flop bug)
        Q0_AMBIGUOUS : 13

VERIFIED INHERITED, not mine: stashed every local change and re-ran on a clean
main checkout -- IDENTICAL 262 / 13. main is red on this BLOCKING gate now.

WORSE: the committed witness reports a false green.

    committed on main   "computed": 0,    "passed": true
    live tree            "computed": 262,  "passed": false

So the gate's own recorded output claims it passes while it fails. Anyone
reading the witness instead of running the audit sees green. That is the same
defect shape as the stale-audit-witness class already recorded elsewhere in the
corpus, but on the anchor gate, which is the one AGENTS.md singles out as the
recurring flip-flop hazard.

NOT DIAGNOSED HERE. 262 flips across many arcs is not a drive-by fix, and the
likely source is the convention-D / anchor-migration churn (qou-1c4y, qou-cds*).
Filed so it is visible and owned rather than silently red.

The regenerated witness IS committed on the qou-unqc branch, so the false green
is at least corrected -- per the precision-gates rule that a moved COUNT means
the committed witness was stale.


## FIXED 2026-08-19 — one file, not 262. NO SWARM WAS NEEDED. (PR #5328, merged 11021cd62a)

ROOT CAUSE, single commit: 9a9c6b31c7 'sweep(tnjb): first 25 witnesses
regenerated at the proton pin' re-pinned
computations/q-pinning-50-digit.witness.json to proton.

That file is NOT an ordinary consumer witness. It DEFINES the muon anchor:
qou_substrate.witness._q0_value_for_anchor('muon') reads its derived_50_digit.q,
and computations/substrate/q_parameter.py reads it to build the entire
ideal/muon q-closure family. Re-pinning it redefined what 'muon' MEANS, so all
262 muon-anchored witnesses were compared against the proton value. Every one of
them was CORRECT.

BLAST RADIUS wider than the audit: QOU_Q0_ANCHOR=ideal and =muon both
hard-failed with RuntimeError on main, so every muon-anchored producer was
unrunnable -- including the five validators /prepare-merge's step-1a recipe runs
with QOU_Q0_ANCHOR=ideal. q_parameter's guard did its job; nothing computed
silently wrong.

FIX: restored from 9a9c6b31c7^ (muon value, q0Anchor=muon). The sweep's other 26
witnesses are genuine consumer migrations, left alone -- q-pinning-50-digit is
the ONLY anchor source of truth in the tree (grepped).

  Q0_FLIP 262 -> 0. All blocking precision gates green.

TWO GUARDS so it cannot recur silently:
1. q0_repin_sweep.py refuses to touch ANCHOR_DEFINITIONS.
2. q0_anchor_consistency_audit.py checks its OWN reference first and, on
   corruption, prints the root cause and exits 1 WITHOUT emitting a single
   consumer row. Verified both ways.

Guard 2 is the one that matters: the audit could not distinguish '262 witnesses
are wrong' from 'my definition of muon is wrong', and reported the first when the
second was true -- output that invites fixing 262 correct files.


## Residual taken to ZERO (2026-08-24, PR #5622 commit aefc2489cd)

This bean closed at **262** flips. Re-measured today on the merged tree: **3**.
Now **0**.

    Q0_FLIP           3  ->  0
    Q0_INDEPENDENT   44  -> 47      (the same 3, correctly reclassified)
    Q0_COMPARISON     1  ->  1      (no regression)
    Q0_OK           746  -> 746

**Root cause — a guard skipped exactly when it was needed.** `witness.py`
already forbade a bare `q0Value` beside `q0Anchor: "independent"` /
`"comparison"`, but the pop was nested inside the `if not _stale:`
carry-forward branch. Forbidding is a property of the *new* declaration, not of
whether the *old* record was stale, and the two are anticorrelated: when the
existing witness already said `independent` and the new payload carried anchor
evidence, `_stale` went True, the branch was skipped, and the value rode
through. Hoisted the pop out of the branch.

**A caution for anyone reading this gate's output.** The audit's message —
*"anchor=independent but a q0Value is recorded — the producer reads q₀ after
all"* — is a **false inference**. All three producers had a deliberate
`independent` declaration from `qou-o922` with a stated proof, so I re-verified
rather than trusting either side: running `qbeta_c3_rung_structure_analysis`
under `QOU_Q0_ANCHOR=muon` vs `=proton` and diffing gives **one** differing
non-ephemeral leaf, `.q0Value` itself, everything else byte-identical. The
producers do not read q₀. The audit's *finding* was still correct — that state
violates the module's own documented vocabulary — but its stated reason would
send the next reader to fix the wrong file.

Whether the 262 → 3 drop came from the anchor-migration work or elsewhere is
**not** established here; only the last 3 are attributed.
