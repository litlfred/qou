---
# qou-3exu
title: Drain the 25 sites that posit the two-row cap onto the proved lemma
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:41:44Z
updated_at: 2026-08-16T13:42:16Z
---

25 sites assert/posit the two-row cap rather than deriving it. Full inventory in
docs/audits/2026-08-16-two-row-cap-proved-and-deltalambda-magnitude.md (PR #5242).

Now derivable from QOU.QBeta.WenzlWeight.{schurPrincipal_eq_zero_iff, wenzlLevel_conventionD}
and the sum-level statements in QOU.MassTheory.TwoRowCap (PR #5242).

Highest value:
  mass-theory/markov-trace-frobenius-selection.{md,ts,lean} -- cap is numbered hypothesis 1
  mass-theory/convention-d-kills-antisymmetriser.md:81 -- 'impose' becomes 'invoke'
  mass-theory/two-row-projection.md:12 -- splits tr_M with a LIVE complement that is now
      identically zero (traceSum_eq_twoRow_of_wenzl)
  lean/QOU/BraidKnot/TwoRowStratum.lean:124 -- class HasTwoRowProjection, 'axiomatised here'
  lean/QOU/MassTheory/ThreeRowExtensiveCumulant.lean:49 -- sRow3 hand-entered table
  docs/audits/2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md -- title asserts
      binding is >=3-row DOMINATED; contradicted, needs a superseded banner
  docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md:38 -- '13.4% projected to
      zero, measured' is convention-C

NOT drained in #5242 by scope (no mass content-block edits) and because .md edits stale the
.qa.json sidecars, which need qa-sweep / folio-assistant.
