---
# qou-h6mq
title: 'MAIN RED: QIntegerCanonical references qIntPoly, removed from QHookDimension'
status: completed
type: task
created_at: 2026-08-30T07:42:27Z
updated_at: 2026-08-30T07:42:27Z
---

Found by running /prepare-merge on PR 6096 (the Roth arc). NOT caused by that branch: it changes
20 files, none of them in this cluster, and the breaking commit is on main.

THE BREAK. QOU/MathlibExt/QIntegerCanonical.lean:117 has

    abbrev qIntGeo {R} [CommRing R] (q : R) (n : ℕ) : R := QOU.Mass.QHookDimension.qIntPoly q n

and QHookDimension no longer defines qIntPoly. It did: git log -S puts it in 7f7814984f and
1646b5d6d3, and main's d397d7a9a2 ("QHookDimension: derive the c=3 anchor from the hook lengths",
2026-08-29) is the commit after which it is gone. QHookDimension now exports qInt, qFact,
conjugate, hookAt, hooks, dimQ and the dimQ_* lemmas -- no qIntPoly.

The intended content is pinned by the very next declaration, which asserts it as rfl:

    @[simp] theorem qIntGeo_def (q n) : qIntGeo q n = sum_{i in range n} q^i := rfl

so whatever replaces qIntPoly has to be DEFINITIONALLY the geometric sum, not merely equal to it.

BLAST RADIUS, measured rather than guessed. Of the 25 modules in the lean-axiom-guard registry,
18 build and 7 do not, and all 7 fail on this single reference:
  QOU.Archimedean.BorromeanVolumeCatalan, QOU.Archimedean.CatalanClausenBridge,
  QOU.HeckeAlgebra.JonesMarkovWenzl, QOU.HeckeAlgebra.MarkovTrace,
  QOU.MathlibExt.MacdonaldTelescope, QOU.MathlibExt.QPartitionCombinatorics,
  QOU.MathlibExt.WenzlSchurElement.
QOU.Mathlib.Summary also fails here, which SUPERSEDES the older report (bean qou-1lb8) that it was
red at Summary.lean:100 on IwahoriHeckeAlgebra -- it no longer gets that far, so whether that
second defect is still present is currently unknown and should not be quoted either way.

CONSEQUENCE FOR THE AXIOM GATE. lean-axiom-guard refuses a verdict while any registry olean is
missing, and correctly so -- a verdict off a stale olean set is the axiom status of an old
snapshot. So the keystone #print axioms gate cannot run on main at all until this is fixed. That
is the second time in this repo's history that a gate has been silently not-running; the first
(qou-agrd) was a gate nothing invoked, this one is a gate nothing can satisfy.

NOT FIXED HERE, deliberately. The fix is one declaration, but which one depends on what the qInt
migration intends qIntGeo to be, and that is the qou-qint cluster's call, not the Roth arc's. A
guess that type-checks would be worse than the red, because the rfl above means a wrong choice
propagates definitionally.

Related: qou-qint (reconcile the eight q-integer definitions), qou-q7cm, qou-pv3a, qou-1lb8.

## 2026-08-30, same day -- FIXED ON MAIN, by main. Closing.

main's 68dc39ba72 ("fix: QIntegerCanonical is the second consumer of a namespace that moved")
lands the repair. Re-verified on the merged tree:
  * QOU.MathlibExt.QIntegerCanonical builds;
  * all 7 previously-failing axiom-guard registry modules build;
  * lean-axiom-guard reports ALL 217 REGISTRY DECLARATIONS MATCH their recorded axiom status.

So the keystone gate is running again. Its last recorded state before this was ~4 months of not
running at all (the workflow-dispatch history in .github/workflows/lean-axiom-guard.yml), and this
episode added ~1 day of not-being-satisfiable on top.

## Summary of Changes

None by this bean -- it was a report, and main fixed the defect. What the bean contributed was the
measurement: 18 of 25 registry modules building and 7 failing on one reference, and the finding
that QOU.Mathlib.Summary now fails at the same place rather than at Summary.lean:100, which
SUPERSEDED the standing claim in qou-1lb8.

## Still open, and inherited from this

qou-1lb8 claims main is red at QOU/Mathlib/Summary.lean:100 on IwahoriHeckeAlgebra R 2 q. While
QIntegerCanonical was broken, Summary could not reach that line, so the claim was unverifiable.
Now that the import chain is repaired, whether that defect survives is CHECKABLE AGAIN and
nobody has checked it. Left to qou-1lb8's owner rather than silently re-asserted.

## Correction to my own report

My first attempt at the axiom guard failed twice for two different reasons and I reported only
the first. The first failure was genuine -- missing oleans, caused by main's red. After building
those, the second failure was mine: I ran the guard without sourcing scripts/lean-direct-env.sh,
which the workflow does and which its own header documents, so lean had no LEAN_PATH and reported
"unknown module prefix 'QOU'". A gate that fails because the caller did not read its invocation
is not a gate failure, and reporting it as one would have been the same mistake as quoting a
stale olean set.

