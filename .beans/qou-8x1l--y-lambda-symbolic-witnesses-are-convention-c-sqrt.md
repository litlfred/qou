---
# qou-8x1l
title: 'y_lambda symbolic witnesses are convention C (sqrt-q): blocks rho_k_h3a_refinement Schur-Weyl and 5 downstream'
status: todo
type: task
priority: normal
created_at: 2026-08-10T13:25:49Z
updated_at: 2026-08-10T13:26:24Z
---


## The finding

The structural detector (test 2: nonzero `y_λ` on a 3+-row block) calls
`float(v)` and `continue`s on `ValueError`, so a weight stored as a **sympy
expression** never reaches the comparison. Same shape of blind spot as the
decimal-fingerprint scan that reopened `qou-eea0`.

**Test 3 (landed, PR #4924 `04cbe04c`):** C is `z = 1/(q^{1/2} + q^{-1/2})`;
D is `z = q³/(q²+1)`, rational and sqrt-free. A half-integer power of `q` in a
weight expression is convention C at any `n`. No maintained list.

Two witnesses, and it is not "symbolic ⇒ suspect" — three of the five holding
symbolic weights on 3+-row blocks are clean:

| witness | expressions | producer |
|---|---|---|
| `y-lambda-symbolic-witness.json` | 20 | **unknown — orphan** |
| `y-lambda-wenzl-bridge-symbolic-witness.json` | 270 | **unknown — orphan** |

Evaluated at q₀ the wenzl-bridge one gives nonzero `y_λ` where D gives exact
zero: `(4,1,1) 0.0101`, `(3,2,1) 0.0073`, `(2,2,2) 7.73e-4`,
`(3,1,1,1) -6.85e-4`, `(1⁶) -1.24e-5`.

## Why it blocks

It is the `y_λ` source for `rho_k_h3a_refinement`, whose Schur–Weyl check

    Σ_λ y_λ χ^λ(β_D) = 0.388286424074788876711537513129
    tr_M(β_D)        = 0.388286471559408882668623506562
    |residual|       = 4.74846e-8      (1.2e-7 relative)

**fails**, and which returns `exit 2` on that failure *while writing its
witness anyway* (`return 0 if sw_match else 2`). The script states the
consequence itself: *"Δ_λ extraction below is meaningless without this
identity."*

`rho_k_h3a_refinement` is the upstream of five producers —
`rho_k_co_casimir_extended`, `rho_k_h3a_co_casimir`, `rho_k_h3a_crystal`,
`rho_k_h3a_frobenius_pairing`, `rho_k_h3a_lp_dual`.

So the producer has been reporting this the whole time in the only channel it
had, and any run classifying `exit 2` as "producer failure" files it under the
wrong heading.

## What this does NOT establish

The residual is ~1.2e-7 relative, close to the ~1e-7 signature AGENTS.md
records for an ideal/experimental **anchor straddle** (muon-built `y_λ` cache
against proton-q₀ `χ_λ`). Those are two different causes with a similar
magnitude and I have **not** separated them — convention C in the `y_λ` is
established by the sqrt signature and the nonzero ℓ≥3 weights; that it is the
*whole* residual is not. Re-deriving the `y_λ` under D and re-measuring is
what decides it.

## To close

1. Find the producer for both symbolic witnesses (currently orphans — a
   re-run of the 54 does not touch them).
2. Re-derive them under D — sqrt-free, `y_λ = 0` for `ℓ(λ) ≥ 3`.
3. Re-run `rho_k_h3a_refinement`; SW check must pass at 1e-40, exit 0.
4. Then the five downstream, in dependency order.
5. Re-measure the residual against the anchor-straddle hypothesis above and
   record which cause it was.

Blocks the `qou-eea0` convergence criterion (`--stale` empty).
