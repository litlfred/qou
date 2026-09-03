---
# qou-zmuu
title: 'wall-side-statement: 21 live fails remain after qou-7q0a''s five — 4 templated, 15 ''missing Lean sibling'', 2 ''Lean fails'' — re-adjudicate / n-a'
status: todo
type: task
priority: normal
created_at: 2026-09-03T05:32:27Z
updated_at: 2026-09-03T05:33:05Z
---

MEASURED 2026-09-03 on branch claude/wall-side-readjudicate-2026-09-03 @ 01dfbca94f0 (after the five of qou-7q0a flipped to pass). Corpus tally of the LATEST wall-side-statement entry per block: 545 pass / 21 fail / 20 n/a / 1 warn.

The 21 fails split into THREE classes by their evidence string, and only the first is a wall-side question at all:

(A) 4 TEMPLATED, same batch stamp 2026-07-07T14:26:57 gemini-3.1-pro, evidence 'Substrate statement contains archimedean constructs.', no token named -- the class qou-7q0a just overturned 5/5:
    climax-volume-mass/q-energy                      (hash current)
    nuclear-interactions/gram-weighted-qvalue        (STALE)
    nuclear-interactions/parity-regime-selection     (STALE)
    nuclear-interactions/frobenius-positivity-filter (STALE)
  Owed: the same dispatched read-and-judge adjudication. Prior from qou-7q0a: 5/5 were false positives.

(B) 15 'The sibling Lean file ... is missing entirely', batch 2026-07-07T14:26:56 (11) and 2026-06-28T05:50 local/qa-agent-drain (4), ALL in mass-theory:
    ramified-disc-fusion, feynman-trace-collapse, skein-mass-from-linking, symbolic-character-table, knot-operator-transition, mass-categorical-descent, quantum-dilog-convergence, feynman-categorical-trace, volume-perturbation-formula, q-reeb-flow-on-color-coords, feynman-markov-identification, content-scaling-correspondence, feynman-eigenbasis-decomposition, crossed-module-euler-characteristic, tmli-constituent-composite-agreement
  These are NOT wall-side verdicts. wall-side-statement has depends_on: ['md'] -- it judges the narrative statement's regime, and a missing .lean does not make the .md statement straddle the wall. The evidence-provenance rule (n/a, not fail, when unable to check) applies, and the reviewer did not even attempt the .md. Same class as qou-zkia (887 entries claiming a Lean sibling fails). Owed: either (i) adjudicate the .md on the merits like class A, or (ii) mechanically re-stamp n/a with the reason 'reviewer refused on missing Lean; criterion depends_on md only'. (ii) is mechanical and cheap; (i) is honest and gives a real verdict. Recommend (i) for blocks that are theorem/proposition kind (a missing Lean on a provable kind is a separate, real finding for lean-completeness, not this criterion), dispatched in one batch of 15.
  Check first whether any of the 15 have gained a .lean since 2026-07-07 (measured at bean creation -- see the qou-7q0a session log).

(C) 2 'The Lean sibling fails compilation, preventing statement verification', predicted-spectra/hadron-half-life and predicted-spectra/q-value-transition (linarith failure at hadron-half-life.lean:74). Same misclassification as (B): a Lean build failure is a lean-build-fix finding, not a wall-side fail. Owed: adjudicate the .md on the merits + file/confirm the Lean build failure separately (may already be fixed -- check lean-direct).

All 21 with stamps, model, staleness and evidence class are in the parent session's transcript; regenerate with the one-liner in qou-7q0a's log rather than trusting this list, since sidecars move.

Not done here because the owner asked for the five and 'what next'; this bean IS the what-next candidate.

MEASURED at creation: of the 15 class-(B) blocks, 14 still have NO .lean; q-reeb-flow-on-color-coords now HAS one (its 'missing Lean' fail is doubly stale). Both class-(C) .lean files exist; build status not re-checked.
