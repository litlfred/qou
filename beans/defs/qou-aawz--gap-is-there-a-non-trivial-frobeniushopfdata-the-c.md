---
# qou-aawz
title: 'GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T19:59:47Z
updated_at: 2026-11-20T09:00:00Z
parent: qou-ddmn
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


## 2026-09-15 — ANSWERED for the linear case: there is NO non-trivial model

This bean listed two acceptable outcomes. **The second one landed**: a proof
that the current axioms already force `A = 1`, restricted to the linear
setting. PR #7413, issue #7412.

`QOU.FrobeniusHopfData.dichotomy_of_scalars_field` (sorry-free): in a
preadditive monoidal category whose scalars `End(1_C)` form a field, every
`FrobeniusHopfData` has `A` a ZERO OBJECT or a RETRACT OF `1_C`. Over
`ModuleCat k` that is `dim A <= 1`.

Write `sigma = eta >> eps` for the scalar `eps(1)`.

  frobeniusLoop_counit_unit       Delta >> (A <| (eps >> eta)) >> mu = id_A
                                  -- counit + unit law only, NO antipode
  id_factors_through_unitCounit   id_A factors through a map carrying sigma
                                  -- NO hypothesis at all
  retract_of_unit_of_isIso        sigma invertible  ==> A retract of 1_C
  id_eq_zero_of_unitCounit_eq..   sigma = 0         ==> id_A = 0, A is zero
  dichotomy_of_scalars_field      scalars a field   ==> no third case

### This CORRECTS my own 2026-09-15 entry above

That entry said a non-trivial witness "must have `eps(1) != 1`", and treated a
non-unital counit as the surviving corner. **The corner is empty over a
field**: a non-trivial model needs `eps(1)` neither invertible nor zero, and a
field has no such element. Describing the complement of one point understated
a constraint whose admissible set is empty.

The candidate this bean named is excluded twice over. Beyond `eps(1) = 1`, the
probe `computations/probes/frobenius_hopf_no_nontrivial_model_probe.py` tests
the SHARP prediction -- for `|G| > 1` NO linear `S'` at all satisfies the left
antipode axiom against the Frobenius comultiplication -- by solving the whole
`|G|^2` system exactly over Q. 5/5 agree (trivial, Z/2, Z/3, Z/4, S_3):
consistent exactly at `|G| = 1`.

### STAYS OPEN, and precisely why

The zero branch needs `MonoidalPreadditive`. Over a BARE monoidal category
`sigma = 0` is not statable and nothing here proves anything. **Whether a
non-linear monoidal category admits a non-trivial `FrobeniusHopfData` is
unresolved**, and that is now the whole of this bean.

Second, weaker limit: "retract of `1_C`" is not "`= 1_C`" unless the unit is
indecomposable. That holds in `ModuleCat k`; it is not assumed in the theorem.

### What would close it

Either exhibit a non-trivial `FrobeniusHopfData` in a monoidal category that is
not preadditive, or extend the zero branch to a setting without zero morphisms
(if that is even possible -- the argument as it stands is genuinely additive).

Audit: `docs/audits/2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md`.


## 2026-09-15 — the axiom that had no models is GONE, and this bean is STILL OPEN

On owner decision the convolution antipode condition was replaced by the
anti-automorphism package (`qou-c64q`). So the definition now HAS non-trivial
models: `k[G]` with the Frobenius comultiplication and `S(g) = g^-1`, measured
7/7 over Z/1..4, V_4, S_3, D_4 by exact integer arithmetic.

**That does NOT close this bean, and the distinction matters.** This bean asks
whether a non-trivial `FrobeniusHopfData` exists IN THE CORPUS. `k[G]` is a
model *in Python*. `QOU.TrivialWitness.unitFrobHopf` (`A = 1`) is still the
ONLY record-literal construction in Lean. The literal claim this bean was
opened on is therefore unchanged.

### What would close it now

Formalise `k[G]` as a `FrobeniusHopfData (ModuleCat k)` in Lean -- the
Frobenius comultiplication from the dual basis, `S(g) = g^-1`, the six new
antipode laws discharged. The Python probe says every one of them holds, so
this is transcription rather than research, but it is real work and it is not
done.

Until then the corpus's consistency proof for this definition still rests
entirely on the trivial object, exactly as when this bean was opened.

## Progress (PR #8448)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/CuspLatticeUncertaintyTruncationDigitSlopeJetHorizonProjectionSubstrateModelScalarTrace.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_4kgh_5u0i_a2d7_aawz_nnyn_probe.witness.json` (`Commit 1` = `03aab630aaf498438c097ced372d1b9624239334`, `HEAD` = `9712a8a7c54237632ba55faa0a1e31fdd3332e05`).

## Note from W12 (2026-11-20, PR #8537) — informational, status untouched
`QOU.IdemLine.model` (in `FrobeniusHopfNilpotentAndNonFieldModel.lean`) is a sorry-free `FrobeniusHopfData` — all six antipode laws, Frobenius relation, snakes — on an object A = eR that is NOT isomorphic to 𝟙 and not zero (any commutative ring with an idempotent e ∉ {0,1}, e.g. S × S). So "the corpus only exhibits A = 1" no longer holds literally. It does not close this bean's intent: A is a proper summand of 𝟙, and `retract_of_unit` proves every model satisfying `ConvolutionLeft` is a retract of 𝟙. The `k[G]` question (anti-automorphism package without ConvolutionLeft) is untouched.
