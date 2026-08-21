---
# qou-cnbm
title: 'borromean-axial-coupling reads gram_inverse, which no longer exists: the Gram matrix is singular and the substitute is a different object'
status: todo
type: task
created_at: 2026-08-21T14:48:19Z
updated_at: 2026-08-21T14:48:19Z
---


## The break

`borromean-axial-coupling.py:93` does

    GRAM_INV = np.array(_gram_data["gram_inverse"], dtype=float)

and `gram-matrix-dual.witness.json` no longer has that key. The producer dies
with `KeyError: 'gram_inverse'`.

**Pre-existing on `main`, not caused by the q₀ proton migration** — the
migration sweep merely ran a producer nothing had run in a while, which is the
third time this arc that a sweep surfaced a long-standing break rather than
creating one. Verified: `origin/main`'s copy of the witness has no
`gram_inverse` either.

Introduced by `be59f01376` — *"gram-matrix-dual emits the quotient inverse,
and the radical exactly"* (`qou-m7py`).

## Why this is NOT a rename, and why I did not just swap the key

The obvious fix is `gram_inverse` → `gram_quotient_inverse`. Both are 6×6, so
the shape assertion at line 95 would pass and the producer would run. **That
would be wrong to do blind**, because the Gram matrix is *singular*:

    gram_radical                    [1.0, -0.900918, -0.900918,
                                      0.811654, 0.811654, -0.731234]
    radical_is_sign_representation  True

A true inverse does not exist. Whatever the old `gram_inverse` held was an
inverse of a singular matrix — i.e. dominated by the near-zero eigenvalue —
so `be59f01376` is a **correctness fix**, not a refactor. The quotient inverse
is a genuinely different object: the inverse on the quotient by the radical.

The consumer uses it at line 197 as

    G_inv_A = GRAM_INV[np.ix_(A, A)]     # G^{-1}|_{A*}

i.e. restricted to the LP active set `A`.

## The one question that decides it

**Does the active set `A` overlap the radical direction?**

- If `A` is disjoint from the radical (the sign representation), the quotient
  inverse restricted to `A` *is* the inverse there, and the substitution is
  both safe and more correct than what the file had.
- If `A` meets the radical, the old code was computing with an
  amplified-noise direction and the new object legitimately has nothing to
  say there — the consumer needs a decision about what `G^{-1}|_{A*}` should
  mean, not a key rename.

That is a question about `qou-m7py`'s intent, so it belongs to whoever owns
that change rather than to a passing migration sweep.

## Meanwhile

The producer stays failed in the sweep journal with this reason recorded,
rather than being silently skipped or blind-fixed. Its witness is therefore
NOT regenerated at the proton pin and remains muon-valued — worth knowing
before anyone reads it.

## MEASURED (2026-08-21): the deciding question has one answer, and it is "yes"

The bean above framed this as a two-branch decision — safe if the LP active
set `A` misses the radical, a real decision if it meets it. **Measured, the
first branch does not exist.**

    radical      [1.0, -0.900918, -0.900918, 0.811654, 0.811654, -0.731234]
    nonzero      indices 0,1,2,3,4,5
    support      6/6 — FULL

The radical is the sign representation and it has **full support** in the NF
basis. Every coordinate direction carries a nonzero component of it, so *no*
nonempty active set `A` is disjoint from the radical. The escape hatch is
closed for every possible `A`, not merely for the one this producer happens
to select.

So the substitution `gram_inverse` → `gram_quotient_inverse` is **never**
trivially safe here, and swapping the key would have produced numbers on
every input rather than only on unlucky ones. That is the argument for having
left it alone.

What the consumer needs is a decision about what `G^{-1}|_{A*}` should mean
when `G` is singular in a direction that meets every coordinate — quotient
inverse, pseudo-inverse, or a restriction that excises the sign
representation first. That is a question for `qou-m7py`, and it now has a
measurement attached instead of a conditional.
