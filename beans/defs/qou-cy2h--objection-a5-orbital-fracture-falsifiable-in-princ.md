---
# qou-cy2h
title: 'OBJECTION: a5 orbital-fracture ''falsifiable in principle'' unaddressed against exact free-atom f-shell degeneracy'
status: completed
type: task
priority: normal
created_at: 2026-08-08T13:03:57Z
updated_at: 2026-08-15T10:37:13Z
---


Found by the SM/eightfold epistemic accounting,
`docs/audits/2026-08-08-sm-eightfold-epistemic-accounting.md` §4.3
(Finding 8, moderate — an *objection*, not a refutation).

**Site:** `content/quantum-observable-universe/appendix-standard-model/a5-orbital-degeneracy-fracture.md:14`.

**What the block gets right (verify before changing anything).** Its table is
correct — I re-derived all six rows independently by icosahedral character
arithmetic: `l=0 -> 1`, `l=1 -> 3`, `l=2 -> 5`, `l=3 -> 3' + 4`,
`l=4 -> 4 + 5`, `l=5 -> 3 + 3' + 5`. And its tier is correct: the block says
":12 standard finite-group representation theory" and ":14 conditional on the
truncation conjecture ... not a prediction wired to any computation". **No
mislabel.**

**The objection the block does not address.** The block rests its stated value
on falsifiability in principle: *"a truncated discrete symmetry cannot hold
seven states exactly degenerate, while exact SO(3) can, so the two pictures
differ at some resolution on lanthanide-scale spectroscopy."* But free-atom
f-shell degeneracy **is** observed to spectroscopic precision: free-atom states
are labelled by `J` with degeneracy `2J+1` exact by rotational invariance, and
the observed lifting is spin-orbit, in a `J` pattern — not along a `3' + 4`
seam. So either

  (i) the claim is already in observational tension with free-atom spectra, or
  (ii) the predicted splitting sits below all achieved resolution, in which
       case the claim is *untestable* rather than *falsifiable* and the block's
       stated value does not hold as written.

**The block should say which.** Scope: this is **(a)**, a scope-limited
observational tension I am raising as a referee objection — I have **not**
computed a splitting bound, and this is **not** a proved exclusion. Do not
record it as a refutation without doing that computation.

**Secondary (Finding 4, minor, same block).** `a5-orbital-degeneracy-fracture`
and `cal2-higgs-knot-coupling` are the only two blocks in either chapter with
**no `.qa.json` sidecar**, so they are invisible to every per-block checker
(`clarity-*`, one-voice, `q-usage-*`, `da-*`). Both are `remark` kind. Worth a
`qa-sweep` when either block is next touched.

---

**Verification note (2026-08-08).** For anyone picking this up: all Lean in
both audited chapters' citation graph is green and sorry-free — 11 directly
cited files plus the 9-module colour cone
(`scripts/lean-direct-cone.sh` → `ok=9, err=0, blocked=0`), 20 total, zero red.
The `a5` block has no Lean at all (it is a `remark` with no `.lean` sibling and
no `lean.ref`), and no `.qa.json` sidecar — which is the secondary finding
above. Its table is nonetheless correct; I re-derived all six rows by
icosahedral character arithmetic. So the open item here is purely the
falsifiable-vs-untestable question, not a formalisation gap.
