---
# qou-zmw4
title: 'GAP: wlambda probe records qplancherel_sum_dq2_eq_qfact=False and has reported allPassed=true over it since 2026-07-02'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:34:13Z
updated_at: 2026-08-30T14:34:31Z
---

Surfaced while draining `qou-srvu` slice E (subdirectory witnesses).

## The measurement

`computations/substrate/wlambda-identity-i-structure-probe.witness.json` on
`main`, computed **2026-07-02**, carries in its own `results`:

    qplancherel_sum_dq2_eq_qfact: false
    allPassed: true
    assertions: []

A recorded FAILED identity check, inside a witness reporting green, for two
months. Nothing noticed because `all([]) is True` and no consumer reads the
flag. Draining the witness (PR branch `claude/srvu-drain-e-2026-08-30`) made it
visible: the probe now emits 5 assertions, 4 pass, this one fails, and
`allPassed` is honestly `false`.

The check is `sum_lambda d_q(lambda)^2 = [n]_q!` — the identity that makes
`sum_lambda W_lambda = 1`, i.e. that `W_lambda` is a probability measure at
all. The probe is `auditOnly: docs/coordination/s5-so3-keystone.md`.

## What is MEASURED, and what is NOT

**Measured.** The flag is false; it has been false on `main` since 2026-07-02;
and from the witness's OWN recorded `W_lambda` at n = 3, exact sympy gives

    sum_lambda W_lambda = q(q^4 + 4q^2 + 1)/((q^2+1)(q^2-q+1)(q^2+q+1))

which is exactly **1 at q = 1** but **22/35 at q = 2** — not identically 1.

**NOT established.** Whether this refutes the q-Plancherel identity, or whether
this probe's `dim_q`/`qfact` normalisation is off by a power of `q`. The second
is a common slip and is *consistent with* the value being exactly 1 at q = 1,
but it is **not confirmed**. This is a scope-(a) observation about ONE probe,
not a claim about the mathematics, and it is deliberately not written into any
durable verdict.

## The actionable pointer (corpus-grep path 6)

Bean `z3a2` records that on 2026-06-28 this probe was migrated to take
`qint`/`qfact`/`dim_q` from the shared `young_qdim` module, keeping the
classical SYT/hook combinatorics local, and states the witness came out
**BYTE-IDENTICAL**. This witness's `computedAt` is 2026-07-02, i.e. AFTER that
migration — so the false flag is **not** a regression introduced by it; it
predates and survives it.

So the first place to look is `young_qdim.dim_q`'s normalisation convention
against the `[n]_q!` that `qfact` returns, and against the classical `f_lambda`
this probe kept local. The n = 3 arithmetic above is a two-line reproduction.

## Next honest step

Decide which of the two it is, then either fix the normalisation (and the flag
goes true) or record a scoped negative naming the invariant that fails. Do NOT
close it by deleting the check.
