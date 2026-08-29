---
# qou-6u53
title: 'GAP: 6 witnesses land unstamped for q0Anchor — molien/fake-degree + gap2-he4-borromean-mu-bar'
status: completed
type: task
priority: normal
created_at: 2026-08-29T09:07:10Z
updated_at: 2026-08-29T10:01:20Z
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


## 2026-08-29 — RESOLVED. All six are genuinely q0-independent

Fixed in PR #5989, ported to #5992. Both gates green on both branches.

I reported these rather than fixing them a few hours earlier, on the grounds
that choosing between a manifest declaration and `independent` needs each
producer's import cone rather than a grep. Right about METHOD, wrong about
EFFORT — the cone trace is mechanical, and having run it, all six answer the
same way.

### Evidence, three converging lines

AST import-cone walk (transitive; asks whether q_parameter /
qou_substrate.constants / Q / Q_50_DIGIT_STR / q_at is REACHABLE at all):

  fake_degree_addable_box_recursion_probe   UNREACHABLE in the whole cone
  molien_binding_signed_dimension_probe     UNREACHABLE in the whole cone
  molien_wenzl_weight_identity_probe        UNREACHABLE in the whole cone
  gap2_he4_borromean_mu_bar                 reachable ONLY via
                                            codata_2022_source (a CODATA mass
                                            table); the file has no q_0
                                            reference at all
  molien_jones_markov_general_n_probe       reachable via the Hecke machinery,
                                            but EXACT SYMBOLIC in
                                            sp.symbols("q z") per its own
                                            docstring
  molien_jones_markov_n3_identification     reachable via an imported probe,
                                            but "everything exact in Q(q,z)"

Decisive test, applied to the ANSWER rather than the source: **none of the six
records a q_0 value anywhere in its payload.**

Reachable is not used; symbolic in q is not evaluated at a pin. Declared at
each producer with a reason (152-242 chars), never by hand-editing JSON and
never by a manifest entry that would assert a pin they do not use.

### A trap worth recording — a clean py_compile is not a clean generator

My first generator emitted the reason's continuation lines as `#` comments
INSIDE the parenthesised string expression. One file failed to compile (nested
quote); the other **five compiled fine while silently truncating
q0AnchorReason to its first line**, because Python simply dropped the
comments. Five-of-six green would have read as success. Caught by the one
syntax error, not by the five successes. Reverted and redone with real
implicit-concatenation literals.
