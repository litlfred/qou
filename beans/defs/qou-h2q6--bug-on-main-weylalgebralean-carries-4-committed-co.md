---
# qou-h2q6
title: 'BUG on main: WeylAlgebra.lean carries 4 committed conflict markers'
status: completed
type: task
priority: normal
created_at: 2026-08-07T10:33:55Z
updated_at: 2026-09-06T12:03:21Z
---

Found 2026-08-07 while rebasing the Cluster A consolidation onto main. content/quantum-observable-universe/lean/QOU/Mathlib/WeylAlgebra.lean on ORIGIN/MAIN contains 4 raw conflict markers -- '<<<<<<< Updated upstream' / '>>>>>>> Stashed changes' -- i.e. an unresolved git STASH conflict was committed verbatim. Introduced 2026-08-03 in commit 4ca67a3d 'feat(lean): prove theorems via class hypothesis enrichment'.\n\nWHY IT WENT UNNOTICED: NOTHING imports it. It is absent from the QOU.lean umbrella and no other module imports QOU.Mathlib.WeylAlgebra, so the library build never touches it and CI never flagged it. Zero blast radius today -- but any future import makes the whole library fail to parse.\n\nTRIVIAL TO FIX: the two conflict sides are SEMANTICALLY IDENTICAL. Both define\n  def X : WeylAlgebra K := (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.iota K WeylGen.X)\nwith the same body; only the DOCSTRING wording differs ('via mkAlgHom for liftAlgHom compatibility' vs 'defined via mkAlgHom so liftAlgHom_mkAlgHom_apply fires'). So the resolution is: delete the markers, keep either docstring (the second is more specific and names the lemma). Same pattern at the second marker pair near line 126 -- verify it is also docstring-only before resolving.\n\nDELIBERATELY NOT fixed inside the Cluster A consolidation PR #4675: unrelated domain, and mixing a main-bug fix into a consolidation is the scope creep that makes review harder. Wants its own one-commit PR.\n\nALSO WORTH CHECKING as a class: grep the whole Lean tree (and content/) for committed conflict markers -- if one slipped in unnoticed, others may have too, and the un-imported orphan files are exactly where they hide.


## 2026-09-06 — RESOLVED. Both the instance and the class check are clean.

Measured on `origin/main` `187cbddbff`:

- **The instance is fixed.**
  `content/quantum-observable-universe/lean/QOU/Mathlib/WeylAlgebra.lean`
  exists (137 lines) and carries **0** conflict markers.
  `git show origin/main:<file> | grep -c '^<<<<<<<\|^>>>>>>>'` → `0`.
- **The class check this bean asked for is also clean.** Its closing line was
  *"ALSO WORTH CHECKING as a class: grep the whole Lean tree (and `content/`)
  for committed conflict markers — if one slipped in unnoticed, others may
  have too, and the un-imported orphan files are exactly where they hide."*
  Run tree-wide, all file types: `git grep -c '^<<<<<<< ' origin/main` matches
  **0 files**. So the hypothesis that others slipped in is measured and
  negative, not merely unexamined.

**Distinguishing the two negatives, because they are not the same claim.** A
first pass here returned empty for both greps, which is equally consistent with
*"no markers"* and *"no such file"*. `git cat-file -e` confirms the file is
present, so this is the former. Recorded because absence-of-output is exactly
the evidence class this corpus keeps having to re-measure.

**Closing under AGENTS.md §13a** (owner, 2026-09-06 — never close a bean whose
subject is an open conjecture): this bean's subject is **mechanical** — literal
conflict markers committed to a file — which is the category §13a explicitly
permits completing. No conjecture, no identification, no epistemic tier.

Not measured: *when* or *in which commit* the markers were removed. The bean's
value was the live defect and the class check; both are answered.
