---
# qou-dgpz
title: 'Option B: a DERIVED atom→knot rule at A ≥ 4 (conj:canonical-knot-id-sdp) — the one route that unblocks the EM-linking exponent p'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:17:09Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

From the qou-17mq front: the corpus carries exactly ONE distinct A with hyperbolic geometry (8_11 and L6a4 both at A=3), so the separation exponent p in the EM-linking kernel is unfittable; the only live route is a DERIVED atom->knot rule at A>=4. Prior: qou-vd7j (canonical knot-assignment SDP admits 0/3558 at Frobenius level), PR #1421 ('no derived atom->knot rule'), the 2026-09-05 census-route retirement (selection against the target is a fit). Owner ruling A (2026-08-29): the deuteron knot is the canonical braid closure. A DISTINCT ANGLE must be stated before starting (AGENTS.md measured-overlap rule): candidate — take the per-(Z,N) canonical Hecke word (atom_canonical_crossings) and ask what its CLOSURE is as a link (braid closure -> link type via SnapPy identify()), i.e. derive the knot from the word already in production instead of selecting from a census. Multi-session; not started until the owner says 'start B'.



**ROAST 2026-09-07 (qou-pbwj) — verdict: KILL as posed; do not start on 'start B' with this angle.** The stated DISTINCT ANGLE — take the per-(Z,N) canonical word and identify its closure via SnapPy identify() — is refuted at scope (b) by docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md: the word is not a braid (2A+1 averaged letters); each of its 2^(2A+1) branches closes to a connected sum of (2,k) torus links; Vol = 0 for every branch at every A ≤ 24 (verified 32/32 against SnapPy deconnect_sum, SnapPy installed). 2026-07-04-he4-link-volume-braid-closure-refuted.md already ran the component-count version (³H closure is 4-component; 8_11 is a knot). identify() on a connected sum of torus links returns no census knot and no volume — nothing the EM-linking exponent p could be measured on, which is the blocker qou-17mq says Option B exists to remove. Underneath, 2026-08-25-knot-id-is-an-admitted-fit.md shows the A ≤ 3 assignments were chosen by proximity of Vol to B_AME/(ρ m_e) (the producer says so verbatim), the SDP 'selector' is a feasibility check with no objective, and the 'closure identifies as 6₂' check round-trips SnapPy's own stored braid word — there is no derived map at A ≤ 3 to extend. Fit exposure: maximal — every way past the scope-(b) obstruction is a selection (branch, sign resolution, letter subset, census manifold), i.e. the exact mechanism the 2026-09-05 census-route retirement names; owner ruling A (2026-08-29) already concedes Vol = 0 at A = 2. Arity: 'the one route that unblocks p' reads an absence (no derived map) as a pointer to a route. Already answered negatively three times (the two audits, PR #1421, qou-vd7j, 2026-07-13-atom-knot-rule-a5plus-constraints.md; completed bean qou-5vhf). L2 relevance: none. What would be worth one paragraph in conj:canonical-knot-id-sdp: any atom→knot map must be a map OTHER than Markov closure of the production word, because closure is structurally volume-trivial. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 6.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8332, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
