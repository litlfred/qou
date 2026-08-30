---
# qou-dbau
title: 'GAP: barodd HS matrix-resolvent probe — scope-(a) refutation was derived from the buggy TR_M[5]; bar-parity argument needs redoing'
status: todo
type: task
created_at: 2026-08-30T12:46:31Z
updated_at: 2026-08-30T12:46:31Z
---


## What was found

`qbeta_c3_barodd_hs_matrix_resolvent_probe.py` carried the **2026-05-19 TR_M[5]
Markov bug** — the third instance found, after `pyhecke/gram.py` (fixed
2026-05-19) and `compound_shift_nf` (fixed on #6058, `qou-looi`).

    NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]     # identical to gram.py
    TR_M[5] was  z**3        <- wrong
    TR_M[5] is   h*z**2 + z  <- Markov recursion, any z

Verified before fixing: the basis is character-identical to `gram.py`'s, and the
pre-fix re-run reproduced the committed witness with **zero computed fields
moved** (the only two differences were `scriptCommitSha` and
`environment/pyhecke_native_build`, both provenance — the first is the field
AGENTS.md says is stale-on-arrival after rebase-merge and must never be read as
staleness).

## Why it matters here specifically

Correcting the weight moves **18 computed fields** and fails two of three
assertions:

| | before | after |
|---|---|---|
| `HS(mu=0, proton)` | 5.5635149 | 12.619583 (**×2.27**) |
| `pairing_is_bar_even` | True | **FALSE** |
| `gram_eigenvalues_do_not_cross` | True | **FALSE** |

The probe's recorded RESULT — *"real matrix Gram-resolvent route CLOSED by
bar-parity (scope-a)"* — rests on `pairing_is_bar_even`, which is one of the two
that now fail. **A scope-(a) refutation in the corpus was derived from a Gram
matrix built on a wrong Markov weight.**

## Scope of the claim (read before citing this)

This does **NOT** establish that the matrix Gram-resolvent route is open. That
would be the mirror over-claim the AGENTS.md refutation-scoping rule forbids,
and nothing here has re-derived anything. It establishes exactly one thing: the
probe's own evidence no longer supports its own conclusion.

Whether bar-parity still closes the route under the correct weight is **open**
and needs the bar-parity argument redone, not just a re-run.

## State left in the tree

The fix is committed and the assertions are left **failing**, deliberately.
They fail truthfully; retuning them to pass would encode the bug in the
expectations — the "never make a red run green by widening a baseline" defect.
The file carries a header saying so, pointing here.

## Also noted, not fixed — and the ratchet does NOT see it

The probe emits **6 raw float64 fields** into its witness. Verified on the
committed file rather than inferred from the runtime warning — all six are
Python `float`:

    assertions[0].computed 1.0  expected 1.0
    assertions[1].computed 0.0  expected 1.0
    assertions[2].computed 0.0  expected 1.0

**The raw-float64 ratchet does not flag any of them**, and the witness is not in
`raw-float64-baseline.json` either. The only thing that reports it is the
probe's own runtime warning, which is a *pre-write* message about what the code
passes — so a reader who trusts the ratchet alone would conclude this witness is
clean, and it is not.

Why the ratchet misses it is **undetermined** and should not be guessed: these
are exactly-representable values (1.0 / 0.0), which may be scoped out
deliberately, or may be a blind spot for float-typed booleans. Establishing
which needs a read of the ratchet's own predicate — worth doing, because if it
is a blind spot then every assertion-shaped `passed`-as-float in the corpus is
invisible to it.

The fix at this producer is unchanged: carry `mpmath.mpf` from source and
serialize with `_precision.fmt`.

## Next step

Redo the bar-parity argument on the corrected Gram matrix and determine whether
the scope-(a) closure survives. Then either restore the conclusion with correct
evidence, or re-scope it.
