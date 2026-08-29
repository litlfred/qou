# Pre-registering free-choice calls on five live candidates, before any outcome

**Date** 2026-08-27 · **Branch** `claude/prereg-free-choice-live-candidates-2026-08-27` ·
**Bean** `qou-04ub` · **Scope** (a). This settles nothing about physics.

## Why this exists

The determinacy rule merged in `f089bc13c6` scores 8/8 on the settled record, and
that number is worthless — the same agent assigned both the free-choice labels
and the outcome classes. **A rule earns a hit-rate only from candidates
classified before their outcomes are known.** This is that registration.

The rule under test, in the form that survived:

> A free choice anywhere in a candidate's specification — a **parameter**, an
> **objective**, or a **selection rule** — means it cannot be falsified, because
> it absorbs any residual into that choice. No free choice means it yields a
> definite prediction and is therefore testable. **The rule predicts
> falsifiability, never correctness.**

## The five calls

All five are live routes to the super-pairwise additive term, taken from
[`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).
Each call is read off the **specification** — the property "is a choice left
unfixed?" needs no computation.

| candidate | free choice | why, from the spec |
|---|---|---|
| **SU(4) spin-isospin antisymmetrizer** | **none — TESTABLE** | named rep `[1⁴]`, stated trace `C(4,A)`, stated support (zero for `A > 4`), existing Lean gate. Nothing unfixed. |
| Operator-valued cross-channel | **parameter** | two unbound scalars `B`, `C`. The *source* says "currently a fit unless `B,C` derived" — **that label was authored by a prior agent, not by me**. |
| Whitehead-chain higher-volume | **selection** | `Vol = 4G` is determined, so no free parameter — but which chain, of what length, attaches to which nucleus is unstated. |
| Torus-operator Bloch-Wigner | **selection** | three unbound indices in `bᵢ · β(T_{m,n}) · b_j`: the operator `(m,n)` and both flanking words. |
| Weighted isospin-even determinant | **unclassifiable** | the spec says "no construction yet". No specification, no call. |

## The sharpest entry, and what it does *not* claim

**SU(4)** is the only choice-free candidate, and it predicts the term **vanishes
for every `A > 4`** — so it cannot contribute binding to ⁶Li, ¹²C or ¹⁶O at all.
That is refutable in one measurement.

It is *not* a prediction that SU(4) is right. Per the rule, a determinate
candidate can simply be the wrong object — which is exactly what happened to the
Frobenius co-Casimir, theorem-forced with no free parameters and refuted at
−2.30 MeV. Being testable is not being correct, and this registration would be
dishonest if it implied otherwise.

## What would refute the rule

Registered explicitly, so the test can fail:

- a candidate here carrying an **unfixed free choice** shown to have been
  falsifiable in that state; or
- the **choice-free** candidate turning out to admit no definite prediction.

Neither "SU(4) is wrong" nor "the cross-channel route is right once `B,C` are
derived" would refute it — both are consistent.

## The abstention is part of the test

One candidate is **declined**, not classified. A rule that labels everything is
not discriminating, so the registry has to show it can decline — and the guard
probe asserts that it does.

## Anti-peek

Every `outcome` is `null` **by construction**, and
[`prereg_free_choice_guard_probe.py`](../../computations/meson/prereg_free_choice_guard_probe.py)
(7/7) fails if any is filled in. Back-filling an outcome into a prediction
therefore requires a commit whose diff shows it. The commit adding
[the registry](prereg-free-choice-2026-08-27.json) is the timestamp; scoring
belongs in a **new dated file**, never in an edit to this one.

The registrar's prior exposure is on the record in the registry: I have worked
the cable shift, the growing-width cut and the satellite/JSJ front in this
session — **none of these five** — and my knowledge of each is limited to the
specification text quoted, read at registration.

## No witness JSON, deliberately

There is no `*.witness.json` here. A witness records a computed quantity; this
file computes nothing about physics. Emitting one would dress bookkeeping up as
a measurement.
