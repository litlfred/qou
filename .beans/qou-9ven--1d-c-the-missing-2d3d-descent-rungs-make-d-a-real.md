---
# qou-9ven
title: '1D-C: the missing 2D/3D descent rungs — make d a real binder'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T16:44:07Z
updated_at: 2026-09-14T17:56:39Z
parent: qou-ifto
---

DONE 2026-09-14 (adc31649e): the dim 2 and dim 3 rungs are WRITTEN — descent-{reduction,physical}-{two,three}, wired into ssec:descent, descent-fixed-point.md and its uses[] now index all four. Corpus validates clean against the PINNED platform df28d02: 'Valid, 2 issue(s)', both pre-existing and neither mine.

The rungs were NOT open. descent-fixed-point.md ('each step removes a space-like dimension through the SU(2) rotation') plus brings-is-qou-verification.md's chain M_S --Reeb--> Sigma_4 --pi--> P(V) --branch--> {6 points} with dim M_S = 3 already fix them: M_S --Reeb--> Sigma_4 IS the 3->2 step. My earlier partial-Sigma proposal was not needed.

CONTENT (derived, not asserted): dim 3 has Sigma WITH BOUNDARY, a genuine choice, whose boundary is codim-2 in a 3-manifold and so can KNOT -- the 2-holonomy keeps non-abelian content and that content IS the knot. dim 2 has Sigma = the base, CLOSED, so the boundary holonomy is trivial and the surface holonomy is central by CrossedModuleSurfaceHolonomy.ker_le_center. Descending 3->2 closes the surface, and closing the surface is exactly what removes the non-abelian part of the mass.

NO new Lean, deliberately: the dim-2 claim rests on ker_le_center, already sorry-free; a wrapper would be padding (cf. the threeCell_weight_vanishes deletion, 626574873).

STILL OPEN -- the bean's SECOND half: 'make d a real binder'. d is still not a Lean binder anywhere; q-navier-stokes.lean keeps dim : Nat := 3 as a default field no theorem varies. The rungs are prose+existing-Lean; a genuinely d-indexed Lean family is not written and is a separate piece of work.

TRAP recorded: I shipped tl-is-the-xxz-chain.ts claiming 'render-QA grep battery clean' and it WAS -- but the battery never parses the .ts, so it structurally cannot see a schema violation. That block was missing the required computation.engine/status and had held the whole corpus at 'Invalid' for 15 commits. 'Hand-validated, not machine-validated' is a reason to go get the machine, not a caveat to ship with.
