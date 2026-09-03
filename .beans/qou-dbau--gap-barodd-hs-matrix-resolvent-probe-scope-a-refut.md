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

## RE-ANALYSIS 2026-08-30 — the negative survives, the stated mechanism does not

Measured on the corrected weight. All three legs of the recorded verdict:

| leg | status | evidence |
|---|---|---|
| **[1] sign flip** | **SURVIVES** | no flip at any geometric μ; HS ratio at μ=0 is `1.0000001` against target `S(p)/S(m) = -3.93692` |
| **[2] bar-parity** | **REFUTED** | μ=0: `18.38` vs `6.856` → **BAR-ODD**; μ=1: `13.45` vs `33.53` → BAR-EVEN |
| **[3] no eigen-crossing** | **REFUTED** | corrected Gram has an eigenvalue at **2.717e-71** — singular to working precision — against a between-anchor shift of `6.043e-8` |

### The answer to this bean's question

**The scope-(a) negative holds. The mechanism named in the RESULT line does not.**

The closure argument was *"HS is bar-even, S is bar-odd, so a real bar-even
resolvent cannot carry it"*. It required bar-even at **every** geometric μ. Under
the corrected weight the parity is **μ-dependent**, and at μ=0 the resolvent has
the **same** parity as S — so the obstruction is simply absent there.

What still closes the route is finding 1: it does not produce the flip. That is a
real negative and is untouched by the weight correction.

### Scope — read before citing

- This does **not** open the route. Finding 1 stands.
- This does **not** show the route works.
- It shows **two of the three legs** the verdict was built on do not survive, and
  that the surviving leg is not the one the RESULT line cites.

### Left undone deliberately

Re-scoping the RESULT string and the witness verdict to cite finding 1 rather
than bar-parity is a change to a **recorded conclusion**. That belongs to the
owner or a dedicated pass, not to an inline edit in a drain PR — so the probe
header now carries the full re-analysis and says what the next agent should
change.

### Worth relating to another open item

The near-singular Gram eigenvalue (**2.717e-71**) may be the same phenomenon as
the convention-D Gram singularity tracked in `qou-cds2`. Not asserted — the
frames differ and I have not checked whether the mechanism is shared. Flagged
because two independent near-singular Gram reports in the same corpus should not
sit unconnected.
