---
# fwr5
title: 'uses[] completeness gaps turned up by the forward-ref review'
status: completed
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T23:10:00Z
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

---

**Outcome: 6 of 8 candidates confirmed and added, 2 rejected.**

Rejected for the reason the skill gives: relatedness is not dependency.
`def:antineutrino-knot` → `def:crossing-energy` rests on one qualitative clause
about the *electron*, and the sibling `def:neutrino-knot` makes the same passing
reference without declaring it. `rem:breit-wheeler-observation` →
`def:crossing-energy` is mis-aimed and redundant: the quantity named is one unit
of Reeb charge ħ_q ≈ 1.25 MeV, and the block already declares (and `interprets`)
a remark that introduces crossing energy inline.

One confirmed edge **creates a declared forward reference** —
`prop:rho-k-graded-expansion` → `prop:atomic-mass-gb-nf`, 55 → 58 — and was
added deliberately. The source's boxed display is the target's identity
multiplied through by m_e·|tr_M(B_K)|, ρ_K is defined nowhere else, and the
block previously declared nothing at all. A declared ordering defect is honest;
an undeclared dependency is invisible. It also lifted a veto: this block had been
pinned against reordering precisely *because* the dependency was prose-only and
the metric could not see it.

**The pointer bug is confirmed and traced.** `em-coupling-projection-discussion.md:57`
says "See `prop:em-coupling-bring-zero-mode` for the repair routes"; that
discussion exists only in the target's `.ts` `authorNotes`, and the `AuthorNote`
contract in the platform schema is "Default render behavior: SKIP" — so the
pointer sends a reader to something they cannot see. The routes are in
`rem:alpha-em-derivation-open-problems`, which the same block already cites
twice. Left unfixed here: it is a prose edit, not a graph edit.
