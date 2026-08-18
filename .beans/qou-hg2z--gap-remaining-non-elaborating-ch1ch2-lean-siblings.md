---
# qou-hg2z
title: 'GAP: remaining non-elaborating ch1+ch2 lean siblings (reeb-derivation, categorical-jet, substrate-parameter-exists, poisson-object)'
status: todo
type: task
priority: normal
created_at: 2026-08-17T22:44:34Z
updated_at: 2026-08-18T00:06:05Z
---

Found by the ch1+ch2 elaboration sweep (qou-n4jv), 2026-08-17.
Audit: docs/audits/2026-08-17-ch1-ch2-lean-sibling-elaboration-sweep.md

Four ch1/ch2 content-block .lean siblings still do not elaborate. Error counts
as of 39f5f944 (measured with lean-direct, LEAN_PATH -> ROOT mathlib oleans,
against a freshly rebuilt CategoricalFoundations.olean):

  11  substrate-parameter-exists.lean   (was 3; the docstring-before-
      noncomputable-section parse error was fixed, unmasking the rest)
   4  categorical-jet.lean              (Preadditive import added; remaining:
      'Function expected' at 43/87, stuck typeclass at 79, and a kernel
      'declaration has metavariables' on categorical_jet_prolongation)
   2  categorical-reeb-derivation.lean  (Endomorphism import added; remaining:
      two 'failed to synthesize' at line 77 -- (reeb : End obj) ^ period = 1
      needs a Monoid End instance in scope)
   2  poisson-object.lean               ('Function expected' at 51-52 --
      looks like an arity mismatch against CategoricalConnection)

None of these were investigated past the first error. Each is likely a
different root cause; do not assume one fix covers them.

NOT IN SCOPE OF THIS BEAN (tracked separately):
  qou-mbar -- Inv R_q  (braiding-eigenvalue-extraction, categorical-q-ext-deriv)
  qou-qk51 -- degLex_wellOrdered unsound strategy (braiding-induced-ordering)

ALSO NOT A DEFECT: maximal-torus-su2.lean fails only because its dependency
QOU.ParticleInteractions.AtomicityLieRank has no olean in the partial restored
cache. The SOURCE EXISTS. Do not 'fix' it.

UPDATE 2026-08-18 (commit 6ecedec5) -- three of the four files on this bean
now elaborate. Only substrate-parameter-exists remains.

  categorical-reeb-derivation  FIXED. F9: 'reeb : obj -> obj' with the
      periodicity field written (reeb : End obj) ^ period = 1. The ascription
      is transparent (End obj is DEFEQ to obj -> obj), so elaboration unfolds
      it and instance search asks for HPow (obj -> obj) N. Typing the FIELD as
      End obj fixes it.
  categorical-jet              FIXED. F10: missing
      import QOU.QuantumObservableUniverse.CategoricalFoundations.
      One import cascaded through all four errors.
  poisson-object               FIXED. F10: needed BOTH
      ...CategoricalFoundations (FrobeniusHopfData) and
      ...GaugeTheory (CategoricalConnection).

  substrate-parameter-exists   STILL BROKEN -- and it is a half-finished
      migration, not a syntax slip. A previous R_q edit commented out the
      archimedean fields of a structure literal AND TOOK THE CLOSING BRACE
      WITH THEM, so the literal never closes. Restoring the brace does NOT
      fix it: the same edit deleted the (q0 : R_q) and (hq_pos ...) binders
      of SubstrateParameter.ofReebDecomposition while the body still uses
      both, and left a /-- -/ docstring inside a parameter list (only -- and
      /- -/ are legal between binders). Also InterpolatedDifferential.mk' is
      an unknown constant.
      TO FINISH IT you must DECIDE THE SIGNATURE -- what ofReebDecomposition
      takes now that q0/hq_pos are gone. That is a content call, which is why
      it was not guessed at.

Generalisable lesson worth keeping: commenting out the LAST field of a { ... }
literal (or the last argument of an application) silently eats the delimiter
that closes it, and the error then points at the NEXT declaration rather than
at the comment.
