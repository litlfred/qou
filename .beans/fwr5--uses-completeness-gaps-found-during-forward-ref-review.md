---
# fwr5
title: 'uses[] completeness gaps turned up by the forward-ref review'
status: open
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T21:35:00Z
parent: fwr1
---
The `fwr1` reviewers were scoped to *removing* edges and could not add any.
Reading 274 blocks turned up the opposite defect repeatedly — this is the
`uses-editorial-completeness` axis, not `detangler`, so it needs its own pass.

**The systemic observation.** Ten of the 32 deletions leave the block with
`uses: []`, and in most of those the block has genuine undeclared prerequisites
that the deleted forward entry was never covering. The starkest:
`def:q-navier-stokes` links **eight** prior blocks inline and declared none of
them — its only `uses[]` entry was the one forward reference, which was
spurious. That pattern suggests these single-entry lists are import artefacts
rather than authored editorial judgements, which supports the deletions but
means the completeness question for those blocks has never actually been asked.

**Specific missing edges named by reviewers** (each needs confirming before
adding — these are reader reports, not verdicts):

- `prop:mass-formula-regime-switching` consumes the chirality factor in its
  "BW+χ" regime without listing `prop:chirality-from-frobenius-self-pairing`
- `prop:weak-symmetric-normalization` names `conj:weak-spectral-completeness` in
  its `authorNotes` with no `uses[]` edge
- `prop:rho-k-graded-expansion` carries no `uses[]` at all while citing
  `prop:atomic-mass-gb-nf` inline (the correct reverse edge)
- `def:isotope-knot` needs `def:atom-knot`
- `def:antineutrino-knot` needs `def:crossing-energy`
- `prop:joint-galois-braid-figure-8-verified` needs `conj:joint-galois-braid-action`
  and `def:hq-bi-filtration`
- `rem:breit-wheeler-observation` likely needs `def:crossing-energy` — the block
  names "crossing energy" as a quantity; the edge that was removed pointed at
  `prop:crossing-energy-decomposition`, a different thing

**One content bug, not a graph bug:** `rem:em-coupling-projection-discussion`
says "See `prop:em-coupling-bring-zero-mode` for the repair routes"; the repair
routes are in `rem:alpha-em-derivation-open-problems`. The pointer is mis-aimed.

Adding an edge is a stronger claim than removing one — it asserts a reader must
go read that block first. Use the `uses-editorial-review` workflow (read the
`.md` cold, list what the narrative leans on, then compare) rather than
back-filling from these notes.
