---
# qou-aawz
title: 'GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1'
status: todo
type: task
priority: high
created_at: 2026-09-14T19:59:47Z
updated_at: 2026-09-14T20:00:23Z
---

## Surfaced 2026-09-14 while proving the bialgebra collapse

`QOU.FrobeniusHopfData` — the structure the categorical Lagrangian consumes as
`fh`, and the Lean encoding of `def:frobenius-hopf-substrate` — has **exactly
one record-literal witness in the corpus**, and it is the trivial one:

    QOU.TrivialWitness.unitFrobHopf : FrobeniusHopfData C     -- obj := 1_C

Everything else that mentions the type is a *consumer* (`(fh : FrobeniusHopfData
C)`) or a field. So "the axioms are mutually consistent" is established **only
by `A = 1`**, and has been since `unitFrobHopf` was written — this is not a
regression from today's antipode-axiom addition, which `unitFrobHopf` discharges
by `coherence` like everything else.

### Why this matters now

`TrivialWitness`'s own docstring is careful that it does not produce a
`QuantumObservableUniverse` (at `A = 1` the augmentation ideal is zero, so
`adjoint_nontrivial` fails). But nothing in the corpus exhibits a **non-trivial
`FrobeniusHopfData`** either, so the substrate's axioms have never been tested
against an object with content.

Today's collapse result sharpens the question rather than answering it:
`counit_comp_unit` shows that ADDING the bimonoid unit axiom forces `A = 1`. It
does NOT show the current axioms do. But the two facts sit uncomfortably
together — a definition whose only model is the trivial object, one axiom away
from a proof that the trivial object is the only model.

### What would close it

Exhibit a `FrobeniusHopfData C` with `epsilon >> eta != id_A`, for some concrete
`C`. The natural candidate is a group algebra / `k[G]` as a symmetric Frobenius
algebra in `ModuleCat k`, with `Delta` the Frobenius comultiplication (dual
basis), NOT the Hopf one — per the collapse result the Hopf `Delta` is exactly
what must be avoided. The antipode field then wants the standard `g -> g^{-1}`,
and the two antipode axioms need checking against the FROBENIUS `Delta`, which
is where it may or may not work out.

### What would also be a result

A proof that the current axioms ALREADY force `A = 1` — i.e. that the collapse
does not need the bimonoid axiom at all. That would be a serious finding about
the framework and is the reason this is priority high rather than normal.

Neither outcome is assumed here. The honest current state is: **unknown, and
untested**.

Context: `docs/audits/2026-09-14-frobenius-bialgebra-collapse.md`; parent bean
`qou-c64q`.
