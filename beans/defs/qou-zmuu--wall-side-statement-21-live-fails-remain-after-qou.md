---
# qou-zmuu
title: 'wall-side-statement: 21 live fails remain after qou-7q0a''s five — 4 templated, 15 ''missing Lean sibling'', 2 ''Lean fails'' — re-adjudicate / n-a'
status: completed
type: task
priority: normal
created_at: 2026-09-03T05:32:27Z
updated_at: 2026-09-03T20:43:22Z
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

2026-09-03 10:5x: owner: 'next qou-zmuu class A — the four remaining templated'. Branch claude/wall-side-class-a-2026-09-03 off main c10071d7f73. Dispatching 4 read-and-judge agents (q-energy, gram-weighted-qvalue, parity-regime-selection, frobenius-positivity-filter); parent is scribe. Classes B/C untouched this tranche.

2026-09-03 10:5x CLASS A RESULT: 4/4 pass, 4/4 prior_verdict_was_correct=false, all archimedean regime. Appended on claude/wall-side-class-a-2026-09-03; qa-sweep --only wall-side-statement clean on all four. Grounds: q-energy has ZERO archimedean tokens in its .md (generic H_n(R,q) definition; chapter profile admits generic-R) — a different false-positive shape from the other eight; gram-weighted-qvalue's prior fail was issued against a version that carried the s7c banner RENDERED in prose, so it was wrong on its own terms; parity-regime-selection declares 'for all q>1' at md:6 and its prior field_hash did not match the md at the prior sha either (stale on arrival); frobenius-positivity-filter inherits the ordering from parity-regime-selection one uses[] hop away. Class A is now DRAINED: 9/9 templated 2026-07-07T14:26:5x fails re-adjudicated pass across #6475 + this branch. Classes B (15) and C (2) remain — owner decision: adjudicate on merits vs mechanical n/a.

2026-09-03 20:3x: CLASS A MERGED — #6499 -> main ec7d81458d3 (rebase). All 9 templated fails from the 2026-07-07T14:26:5x batch now pass on main. Owner: 'merge and go' -> classes B+C adjudicated ON THE MERITS (option 1). First dispatch of 17 agents at 11:45Z died on a session rate limit (429, all 17); re-dispatched 20:3x in batches of 6 on branch claude/wall-side-class-bc-2026-09-03 off main ec7d81458d3. reviewed_sha for the B/C verdicts is 4a4e5ce3d2c (the pre-merge class-A head; the 17 blocks are byte-identical there and on main).

2026-09-03 20:4x CLASSES B+C DONE: 17/17 pass, 17/17 prior_verdict_was_correct=false. Regimes: 6 generic (ramified, chartable, knotop, markovid, eigen, crossed, tmli=7 actually: ramified/chartable/knotop/markovid/eigen/crossed/tmli), 10 archimedean. Corpus tally after: see PR #6529. KEY SIDE FINDING for the lean-completeness follow-up: of the 14 mass-theory blocks with no sibling .lean, at least 11 have a .ts lean.ref that RESOLVES to a library declaration under lean/QOU/ (s0a candidate 2, no-shadowing-stub rule) — the 'missing Lean' premise was a resolution non-issue, not a missing formalisation (agents confirmed: ramified, descent, chartable, skeinlink, dilog, cattrace, volpert, markovid, scaling, eigen, tmli, crossed; tracecollapse/knotop report validation: not_checked). Other-criteria findings the agents surfaced, NOT actioned: volume_perturbation.lean uses convention-C z (1/(sqrt q+1/sqrt q)) while its .md states D — qou-cds1/t9r1 excision surface; markov_identification theorem body projects its class field (s3b-cond item 5, proof-statement-integrity); content-scaling's lean.ref names a def (boxContent), not the correspondence; feynman-categorical-trace tr_M=|tr_M| assumes non-negativity silently; eigenbasis_decomposition docstring says 'Sorry retained' over a sorry-free body; q-value-transition .md defines a MASS difference while .lean/title define an ACTION difference (proof-statement-integrity); volume-perturbation md:5 uses '=' for a derived value (s7ab). Bean closed; the wall-side-statement drain is complete on this branch.
