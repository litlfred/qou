---
# qou-nm6y
title: pyhecke_native in this container is a 2026-08-09 wheel, two weeks behind source — it still exports the deleted gram_inverse
status: todo
type: task
created_at: 2026-08-23T16:43:53Z
updated_at: 2026-08-23T16:43:53Z
---

`pyhecke_native` installed in this container is **version 0.9.0, built 2026-08-09**.
The repository source is two weeks ahead of it. The gap is not cosmetic — at least
one function was deliberately DELETED in between.

## The concrete case

`tools/pyhecke-native/src/lib.rs:53`:

> REPLACES `gram_inverse`, which is gone (2026-08-15). With the correct
> `TR_M[5] = h*z^2 + z` the Markov-Gram form is singular under convention D, so a
> 6x6 inverse does not exist. ... Python callers of `pyhecke_native.gram_inverse`
> now get AttributeError, **which is the intended outcome**.

But in this container:

    hasattr(pyhecke_native, 'gram_inverse')   -> True

So `delta_lambda_full_variance_phase5e_1.py:317` calls a function the source
deleted, gets a 6x6 "inverse" of a matrix that **has no inverse**, and writes 37
float64 values into its witness. On a correctly-built machine the call raises
AttributeError, its `try/except` catches it, and the fields are correctly absent —
which is exactly why main's committed witness lacks them.

I initially read main's witness as stale and mine as the correction. It is the
other way round.

## Blast radius

**12 witnesses** regenerated in `a0ee2ac5e` come from producers importing
`pyhecke_native`, so every one was computed against native code two weeks behind
the source:

    atom-vhyp-bar-trace-test              chi-lambda-he4-full-partition-table
    atomic-chirality-residue              chi-lambda-multi-block-first-measurement
    cap-free-trm-prototype                delta-lambda-fr-identity-phase5c
    delta-lambda-full-variance-phase5e-1  he4-stage2-ranking-seminormal-xcheck
    option-e-a4-full-reconciliation       qbeta-jacobi-anger-tower-general
    torus-knot-markov-trace-generalized   yekutieli-volume-join

All twelve are reverted to their pre-regeneration content. Only `gram_inverse` is
confirmed removed; the other native entry points may or may not have changed, and
without a rebuild there is no way to tell which results are trustworthy — so the
conservative move is to trust none of them.

## The real fix

`cargo` and `scripts/build-pyhecke-native.sh` are both present here, so the wheel
CAN be rebuilt from source. That should happen before any witness touching
`pyhecke_native` is regenerated again. Until then, treat this container as unable
to produce native-backed witnesses.

## Why nothing caught it

No gate compares the installed native wheel against the source it was built from.
A stale wheel produces plausible numbers from stale mathematics, and every ratchet
reads those as ordinary values. The `try/except` around the call makes it worse:
on a correct machine the removal is silently swallowed, so neither configuration
announces itself.

Worth a version/commit stamp on the wheel, checked at import, so a producer using
native code against a mismatched build fails loudly instead of quietly computing
the wrong thing.
