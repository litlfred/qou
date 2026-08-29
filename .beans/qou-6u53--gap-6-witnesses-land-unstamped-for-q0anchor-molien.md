---
# qou-6u53
title: 'GAP: 6 witnesses land unstamped for q0Anchor — molien/fake-degree + gap2-he4-borromean-mu-bar'
status: todo
type: task
priority: normal
created_at: 2026-08-29T09:07:10Z
updated_at: 2026-08-29T09:07:38Z
---

Surfaced while merging main into claude/cds3-muon-proton-drain-2026-08-29
(PR #5989). **This is main's failure, not that PR's** — verified on a pristine
origin/main worktree, which reproduces the identical six and exit 1.

## What fails

    python3 computations/audits/q0_anchor_ratchet.py --strict
    -> FAIL: 6 witness(es) newly unstamped

    + computations/gap2-he4-borromean-mu-bar.witness.json
    + computations/qbeta/fake-degree-addable-box-recursion.witness.json
    + computations/qbeta/molien-binding-signed-dimension.witness.json
    + computations/qbeta/molien-jones-markov-general-n.witness.json
    + computations/qbeta/molien-jones-markov-n3-identification.witness.json
    + computations/qbeta/molien-wenzl-weight-identity.witness.json

Five of the six are the molien / fake-degree cluster (qou-3quc territory),
landed 2026-08-29. The tree has DRAINED 48 since the baseline and refilled 6 —
so the ratchet is working; this is the refill it exists to catch.

## Why I did not fix it

The remedy is per-producer and the choice is not mechanical:

    reads q0       -> declare the stem in computations/q0_anchor_manifest.json
                      (physical_proton is the standing default for new compute).
                      NOTE: inert unless the producer uses WitnessBuilder.
    never reads q0 -> w.save({'q0Anchor': 'independent', 'q0AnchorReason': ...})
    undetermined   -> 'ambiguous' + a reason naming what is undetermined

Deciding between those requires reading each producer's IMPORT CONE, not
grepping it for "q0". **I got exactly this wrong earlier in the same session**:
counted `q0` occurrences across nine producers, concluded they "use q0", added
them to the manifest — and a sibling's `qou-4un2` had already done the real
cone analysis and marked them q0-independent. Reverted. A wrong manifest
declaration is worse than an unstamped witness: it asserts a layer the numbers
may not belong to, which is the straddle AGENTS.md forbids regardless of size.

So: whoever owns the molien / fake-degree producers should declare these,
since they know whether the compute is q-symbolic (very likely `independent`
for Molien-series / fake-degree combinatorics) or evaluates at the substrate.

Reported on PR #5989 rather than guessed at.
