---
# qou-nm6y
title: pyhecke_native in this container is a 2026-08-09 wheel, two weeks behind source — it still exports the deleted gram_inverse
status: completed
type: task
priority: normal
created_at: 2026-08-23T16:43:53Z
updated_at: 2026-09-08T08:25:59Z
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



---

## RESOLVED — wheel rebuilt, and the diagnosis is confirmed exactly

`scripts/build-pyhecke-native.sh` succeeded in this container (~4 min; the script
is written for this sandbox and handles the Clarabel git-fork rewrite itself).

    before rebuild:  hasattr(pyhecke_native, 'gram_inverse') -> True
    after  rebuild:  hasattr(pyhecke_native, 'gram_inverse') -> False

The rebuilt wheel no longer exports the function the source deleted on 2026-08-15,
which is the intended AttributeError behaviour. That confirms the whole chain: the
old wheel was stale, `delta_lambda_full_variance_phase5e_1` really was calling a
removed function and receiving a 6x6 'inverse' of a singular form, and the 12
reverts in 7ce3014c3 were correct.

**Native-backed regeneration is unblocked from here** — anything re-run in this
container after this point uses native code matching the source.


---

## CLOSED 2026-09-08 — the container fact is resolved and holds in a SECOND container. The durable gap it names is split out to `qou-3jdl`.

Its subject is a specific container's stale wheel. Verified independently here,
in a different container from the one that wrote the resolution:

```
pyhecke_native.__version__                      : 0.9.0
hasattr(pyhecke_native, 'gram_inverse')         : False   <- the stale marker, ABSENT
```

`gram_inverse` was deleted from source on 2026-08-15; a wheel still exporting it
is stale by definition. This container does not, so its native code matches
source, exactly as the bean's own after-rebuild measurement recorded. Two
independent containers now agree, which is worth more than one.

### The durable half is NOT done, and I measured why it cannot be done with what exists

The bean's forward recommendation:

> *"Worth a version/commit stamp on the wheel, checked at import, so a producer
> using native code against a mismatched build fails loudly instead of quietly
> computing the wrong thing."*

There is no such gate. And the only stamp currently exposed — `__version__` —
**provably cannot serve as one**:

| | |
|---|---|
| `Cargo.toml` / `pyproject.toml` / installed | all `0.9.0` |
| last source change under `tools/pyhecke-native/` | `096f0d89b9b`, **2026-08-31** |
| last commit touching `version` in `Cargo.toml` | `b831ff34c3d`, **2026-08-29** |

The version did not move when the source did, so a wheel built either side of
2026-08-31 reports the same string. That 08-31 commit is *"the binding path's
seminormal matrices are NOT a representation of `H_n(q)`"* — substantive
mathematics in the binding path, invisible to the one signal a consumer can read.

### The class has fired three times

`qou-j6il` (**completed**) is the same TRAP one convention over — *"installed
`pyhecke_native` .so is STALE and returns convention C — any producer run
silently reintroduces C"*. This bean is the second. Each was diagnosed correctly
and fixed **in one container**, leaving nothing behind to catch the next.

That is the shape `qou-oyde` named this same morning for the 0-byte witness:
*"an instruction to the AGENT instead of a fix to the PRODUCER"* — and there too
it fired again three days later. Split out as **`qou-3jdl`** so the third
recurrence has somewhere to land other than a fourth per-incident bean.

### Verdict

Closed on its subject. The 12 reverts in `7ce3014c3` and the confirmation chain
recorded here stand; nothing in this closure disturbs them.
