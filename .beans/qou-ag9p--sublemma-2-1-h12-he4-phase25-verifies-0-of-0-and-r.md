---
# qou-ag9p
title: sublemma_2_1_h12_he4_phase25 verifies 0 of 0 and reports success — its Path A cache key has never existed
status: todo
type: bug
created_at: 2026-08-23T17:05:55Z
updated_at: 2026-08-23T17:05:55Z
---

Surfaced by fixing the `qou-pag7` dimension loop: with that 67 h loop out of
the way the producer runs in 2 s, and what it does in those 2 s is nothing.

    Path A loaded from F1 cache: 0 λ ⊢ 12
    Processing 8 / 77 λ ⊢ 12 (dim ≤ 80)
    Verified: 0/0  max rel residual: 0.00e+00
    ✓ Witness: … (1 assertions, all passed)

**A gate that reports success without examining anything.** It writes a witness
whose single assertion passes on an empty comparison set.

## Cause

`load_f1_cache()` reads

    data["per_partition_contributions"]  ->  c["chi_q_at_q0"]

from `he4-canonical-tr-m-block-fingerprint.witness.json`. **That key has never
existed in that file** — checked every one of the 5 commits that have ever
touched it; zero occurrences in all of them. `.get(..., [])` swallows it, so
Path A is `{}` and every comparison is skipped silently.

## The obvious fix is WRONG — measured, not assumed

The same witness carries `data["per_block_ranked"]`, 77 entries, one per λ ⊢ 12,
each with `partition`, `dim`, `y_lambda`, `chi_lambda`. It looks like the
intended source (and `y_lambda × chi_lambda = contribution` checks out, so
`chi_lambda` really is a character value).

Repointing the loader at it and running:

    λ                dim    χ^λ(F1)        χ^λ(Path B)      |rel|
    (12,)              1   +2.41983670     +2.41966370      7.15e-05
    (11, 1)           11   +7.39103260     -1.48213080      1.20e+00
    (10, 2)           54   +1.04629870     +0.54325297      9.48e-01
    (10, 1, 1)        55   +2.04228950     -1.52797235      1.75e+00
    (1^12)             1   -0.45571190     -0.45574449      7.15e-05
                                            Verified: 0/8

The two **rank-1** shapes agree to 7.15e-05 — which is just the 8-significant-
digit storage of `chi_lambda`. Every dim > 1 shape disagrees at O(1), with sign
flips. So `per_block_ranked.chi_lambda` is **not** the quantity Path B computes:
different braid word, convention, or normalisation. The agreement at dim 1 is
the case where χ is convention-insensitive, which is exactly why it is not
evidence.

**The repointing was reverted and NOT committed.** Committing it would replace
a vacuous 0/0 "pass" with a confidently wrong 0/8 "FAILURES" — worse, because
it looks like a real result.

## What is actually needed

Someone who knows which object Path A is supposed to be. Either the F1 producer
should emit `per_partition_contributions` / `chi_q_at_q0` (and does not), or
`load_f1_cache` should read a different quantity, or Path B's braid/convention
needs aligning with `per_block_ranked`. That is a derivation question, not a
key rename.

Interim, cheap and honest: make `load_f1_cache` **raise** on a missing key
instead of returning `{}`, and make the producer refuse to write a passing
witness when the comparison set is empty. A 0/0 pass is the defect that hid
this.

## Note for the audit doc

`docs/audits/2026-08-23-pr5517-downstream-witness-attribution.md` lists this
producer as writing `he4-canonical-tr-m-block-fingerprint.witness.json`. It does
not — it **reads** that one and writes
`sublemma-2-1-h12-he4-phase25-verify.witness.json`, which is **untracked**. Same
read-vs-write conflation the doc's own §7 correction describes, one instance
further on. Correcting it there.
