---
# qou-nm6y
title: pyhecke_native in this container is a 2026-08-09 wheel, two weeks behind source — it still exports the deleted gram_inverse
status: completed
type: task
priority: normal
created_at: 2026-08-23T16:43:53Z
updated_at: 2026-08-23T22:14:10Z
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

## RESOLVED 2026-08-23 — wheel rebuilt, gate landed, twelve regenerated

**The wheel.** Rebuilt in this container. `hasattr(pyhecke_native,
'gram_inverse')` is now `False`, 57 callable exports matching the 57
registered in `lib.rs`. This container can produce native-backed witnesses
again.

**The durable half, because a container rebuild is ephemeral.** New blocking
gate `scripts/check-pyhecke-native-staleness.py` (360a9ae0c), registered in
`scripts/staleness-gates.sh`. It parses the `#[pymodule]` block of
`tools/pyhecke-native/src/lib.rs` — the authority on the export list — and
compares it against `dir()` on the installed module. Only one direction
blocks: an export the installed module has that the source does not declare.
A build cannot invent an export, so that can only be a wheel predating a
deletion, and the call SUCCEEDS with a wrong number. The reverse is advisory
(AttributeError is loud, and `operator_selection_lp` is legitimately absent
wherever the clarabel-lp fork is unreachable). Module not importable exits 0.

Verified to fire on the real case rather than merely pass on the fixed one:
the pre-deletion `lib.rs` registers 56 exports against today's 57, and the set
difference is exactly `{gram_inverse}` — so a wheel built from that source
trips the blocking direction by name, and would also have flagged
`gram_quotient_inverse` and `gram_radical` as advisory-absent.

**The twelve.** All regenerated (9a5d18462), all rc=0.
`delta_lambda_full_variance_phase5e_1` now logs `Gram inverse load failed:
module 'pyhecke_native' has no attribute 'gram_inverse'` — the outcome
lib.rs:53 calls intended — its try/except fires as designed, the two
`gram_inverse_*` fields are correctly absent, and its raw-float64 count returns
to the 445 baseline from the stale wheel's 482.

**Blast radius confirmed complete.** A sibling classified all 557 producers in
its self-staleness set: 44 import `pyhecke_native` directly, 32 of those are
outside these twelve, and intersecting those 32 against the witnesses actually
rewritten by a0ee2ac5e gives ZERO overlap. The twelve really are the whole
blast radius.

**One correction to this bean's own text.** It said "Python callers of
`pyhecke_native.gram_inverse` now get AttributeError" as though many existed.
There is exactly ONE live call site in the tree —
`delta_lambda_full_variance_phase5e_1.py:317` — and it is one of the twelve.
The Python side was migrated when the Rust side was: `pyhecke/gram.py:542`
and `:817` are deliberate migration stubs that raise with an explanation, and
three tests (`test_native.py:97`, `test_gram_values.py:169`,
`test_rust_gram.py:69`) already ASSERT the removal. Those tests would have
failed on the stale wheel. A second detector existed and nobody ran it.

**One assertion flip, bisected not reverted.**
`qbeta-jacobi-anger-tower-general` went PASS -> FAIL, and it was NOT the wheel:
holding the tree at HEAD and reverting only this branch's edit to the file
reproduces HEAD bit for bit. The cause is the convention C -> D excision
(2026-08-09). The reconciliation itself is intact — the reference producer run
today gives exactly the same 0.142709 — only the frozen convention-C literal
had rotted. Fixed by reading the reference live instead of copying its output.

**Follow-on defect found and fixed:** three of the twelve came back with no
`scriptHash`, a FALSE drain. See de678968d and 5ee66d05a. 29 raw-JSON
producers repo-wide share that defect; handed to the drain in flight.
