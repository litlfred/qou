---
# qou-q7cm
title: '§7c: two files mix generic + archimedean — surfaced (not caused) by the qou-qint migration'
status: todo
type: task
priority: normal
created_at: 2026-08-08T17:55:00Z
updated_at: 2026-08-08T17:55:00Z
---

scripts/check-sidecars.sh flags two files with
  "§7c MIXED generic + archimedean -> split into two files per §7c"

  content/quantum-observable-universe/lean/QOU/GaugeFieldFluidDynamics.lean
      theorem qInteger_zero (q : R)          [R = the reals]
      theorem pow_gt_inv_pow (q : R) (hq : q > 1)   -- ordering => archimedean
  content/quantum-observable-universe/lean/QOU/MassComputationChainRoadmap.lean
      class MRatioInversionMonotone (M_ratio_codata : R)
      def wedderburnStep (H_A : R) ...

## PRE-EXISTING, verified -- NOT introduced by the migration

All flagged lines are present in origin/main. Checked with
`git show origin/main:<file> | grep -F "<line>"` -- all four PRE-EXISTING.

The qou-qint migration's diff on these files is ONLY:
  + import QOU.MathlibExt.QIntegerCanonical
  - noncomputable def <local> ... := (q^n - q-inv^n)/(q - q-inv)
  + noncomputable abbrev <local> ... := QOU.QInteger.qIntBal q n
  - unfold <local>
  + simp only [<local>, QOU.Mass.QHookDimensionBalanced.qIntBal]

No archimedean content added. What happened is that check-sidecars only
evaluates CHANGED files, so these two had never been evaluated before; touching
them brought a pre-existing condition into scope for the first time.

This is worth noting as a general property of the preflight: it is a
CHANGED-FILE checker, so its clean runs are not evidence that untouched files
comply. Same structural blind spot as the orphan-module class (qou-orph): with
CI auto-triggers off, an untouched file is checked by nothing.

## The actual work

Split each file per §7c: generic content over `{R : Type*} [Field R]` in one
file, the archimedean specialisation (ordering, `q > 1`, CODATA reals) in a
sibling that imports it. Deliberately NOT done inside the qint migration --
that would have turned a mechanical consolidation into a two-file
restructure of someone else's module.

Check first whether either file is already covered by a sibling PR; the
wall-side §7c sweeps (qou-3bcc, med65) have been working this exact axis.
