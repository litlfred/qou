---
# qou-kzjl
title: 'GAP(mathlib): the general-n Wenzl ascent needs ''nondegenerate trace form => semisimple'' for a NON-COMMUTATIVE finite-dim algebra — Mathlib has only the field-extension converse'
status: todo
type: task
priority: normal
created_at: 2026-08-26T16:31:07Z
updated_at: 2026-08-26T16:31:49Z
---

Parent theme: qou-2c4t (A1 tower induction via Wenzl). Found 2026-08-26 while
looking for the next brick after PR #5834 (four tower classes inhabited at
H2 subset H3; WenzlTowerStep dischargeable only trivially there).

## The measurement

Mathlib's trace-form criterion is:

  traceForm_nondegenerate :
    forall (K L) [Field K] [Field L] [Algebra K L] [FiniteDimensional K L]
      [Algebra.IsSeparable K L], (traceForm K L).Nondegenerate

Checked directly against the compiled environment (#check), not inferred from the
name — my first two namespace guesses (Algebra.traceForm_nondegenerate,
Algebra.traceForm_nondegenerate_tfae) were both wrong, so the name alone proves
nothing.

**It is wrong for Wenzl in TWO independent ways:**

1. **Direction.** It runs separable => nondegenerate. Wenzl's step needs the
   CONVERSE: nondegenerate trace => semisimple.
2. **Setting.** Both K and L are . H_n(q) is a NON-COMMUTATIVE
   finite-dimensional algebra. The field-extension theory does not apply.

## What this means for the ascent

The general-n WenzlTowerStep field cannot be proved by citing Mathlib. It needs,
as a prerequisite, the classical criterion for a finite-dimensional algebra over
a characteristic-0 field:

  nondegenerate trace form  =>  semisimple

which Mathlib does not have in that generality. That is a substantial standalone
Mathlib-shaped contribution, not a rider on a QOU branch.

Searched: isSemisimpleRing_* family in RingTheory (iff, iff_isArtinianRing,
iff_jacobson, iff_pi_matrix_divisionRing, of_isReduced, of_surjective) — all
structural, none trace-form based.

**Caveat on completeness:** the Mathlib SOURCE is not on disk in this container
(0 .lean files, 6990 oleans), and lean-lsp — which provides leansearch/loogle,
the right tools for this question — was disconnected. So this is a grep of olean
name tables plus direct #check, not a source search. A name I did not think to
guess could exist. Re-run with leansearch before treating the gap as certain.

## Not attempted

I did not attempt the ascent. Building it on a prerequisite Mathlib lacks would
produce either a sorry or a conditional class carrying the missing lemma as a
hypothesis — the second being exactly the assumption-relocation this stack has
been avoiding.
