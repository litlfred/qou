---
# qou-aawz
title: 'GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1'
status: todo
type: task
priority: high
created_at: 2026-09-14T19:59:47Z
updated_at: 2026-09-15T02:14:34Z
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


## 2026-09-15 — NARROWED, still open. A non-trivial witness must have eps(1) != 1

This bean listed two outcomes: exhibit a non-trivial witness, or prove the
current axioms already force `A = 1`. **The result below is NEITHER**, and it
is worth saying so plainly rather than filing it under the second.

`QOU.FrobeniusHopfData.scalar_id_eq_counit_unit` (sorry-free, `#print axioms`
= `[propext, Quot.sound]`) proves, with no hypothesis beyond the structure's
own fields:

    eps(1) . x  =  eps(x) . 1     for every x

`eps(1) = 1` is NOT a field of `FrobeniusHopfData`, so this does not force
`A = 1`. What it does is close off the natural candidates:
`counit_not_unital_of_nontrivial` says a non-trivial `FrobeniusHopfData` has a
**non-unital counit**.

### The candidate this bean named is now excluded

`k[G]` with the Frobenius (dual-basis) comultiplication and `S(g) = g^-1` has
`eps(1) = 1` under the usual normalisation `eps(sum a_g g) = a_e`, so by the
theorem it cannot satisfy `antipode_left` unless `|G| = 1`. A hand check agrees
and shows why: the Frobenius `Delta(1) = sum_h h (x) h^-1`, so
`(S * id)(1) = sum_h S(h) . h^-1 = sum_h h^-2`, which is `1` only for the
trivial group.

The only visible escape is to rescale `eps` by a constant, which is exactly the
corner the theorem says a non-trivial witness has to sit in -- an `eps` that is
not a counit in the normalised sense.

### What would close this bean

Unchanged in kind, narrower in target: a `FrobeniusHopfData C` with
`eps >> eta != id_A`, which now additionally must have `eta >> eps != id_1`.
Search among Frobenius algebras with a deliberately non-normalised Frobenius
form, or accept that the definition wants one and record that as a property of
the substrate rather than an accident.

**STAYS OPEN.** The question this bean asks is unanswered; only the search
space moved.

Audit: `docs/audits/2026-09-14-frobenius-bialgebra-collapse.md` (leading
section). PR #7405.
