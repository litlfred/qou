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

## Producers identified — both are DEPRECATED, and that is the point

| witness | producer |
|---|---|
| `y-lambda-symbolic-witness.json` | `computations/_deprecated/y_lambda_symbolic.py` |
| `y-lambda-wenzl-bridge-symbolic-witness.json` | `computations/_deprecated/y_lambda_wenzl_bridge_extended.py` |

`qou-eea0` already ruled on this class:

> their producers are in `_deprecated/`. The witness outlived the script.
> These cannot be regenerated without un-deprecating, and probably should be
> **retired rather than regenerated**: a witness whose producer was
> deliberately retired is history, and history is allowed to be convention C
> provided it says so.

**That disposition does not hold for these two.** It assumed such witnesses
are no longer consumed. These are read — as live input — by six live
producers:

    delta_lambda_empirical_tabulation.py
    per_irrep_pole_atom_crystal.py
    phase5/phase1c_proton_h3_symbolic_decomposition.py
    rho_k_co_casimir_extended.py
    rho_k_h3a_refinement.py
    sigma_shell_from_beta_chain.py

(13 live files name them; the other 7 only in docstrings/comments. The six
above do `read_text`/`json.load` on them.)

So the deprecation boundary has been crossed in the direction that matters: a
**retired** producer's convention-C output is current input to live compute,
and `rho_k_h3a_refinement`'s Schur–Weyl check is the alarm that has been
going off about it.

This also means the campaign's orphan triage undercounted: "producer in
`_deprecated/` → retire" is only safe once the witness has no live readers,
and that condition was never checked.

## Revised close condition

Step 1 of the plan above is not "find the producer" — it is a decision the
owner may want to take:

1. **Un-deprecate and migrate** `y_lambda_wenzl_bridge_extended.py` to D
   (sqrt-free, `y_λ = 0` for `ℓ(λ) ≥ 3`), regenerate, or
2. **Re-point the six live readers** at a D-convention `y_λ` source that
   already exists, if one covers n = 6 symbolically, or
3. **Retire for real** — delete the witness and fix the six readers.

Not chosen here; each has a different blast radius and (1) resurrects a file
someone deliberated over retiring.

## A FOURTH class the detectors cannot see: derived-value witnesses

Migrating the `y_λ` producer to D (done, cross-validated against the Rust
engine to 1.2e-15) did **not** fix `rho_k_h3a_refinement`. The Schur–Weyl
residual got *worse*: 4.75e-8 → 0.1868.

That is informative rather than disappointing. `χ^λ` is a Hecke character —
it depends on `q` but not on `z`, so it is convention-independent. Only `y_λ`
and `tr_M` carry the convention. C's `y_λ` agreed with the stored `tr_M` to
1.2e-7; D's `y_λ` against the *same* stored `tr_M` is off by 0.19. So the
stored `tr_M` is the **C partner**, and the original 4.75e-8 was never mostly
convention — it is a separate, smaller defect (the anchor-straddle hypothesis
is still live for it).

`computations/atomic-tr-m-mpfr-50dps.witness.json` is convention C **by
construction** — its own description says `tr_M` is computed "via the Hoefsmit
+ Wenzl bridge (Σ_λ y_λ · χ_λ)", i.e. over the C weights. But it stores only
trace *values*: no partitions, no weights, no sqrt. All three detectors clear
it:

    _is_convention_c -> False     fingerprint -> False
    structural       -> False     symbolic    -> False

It is not in the work list and never was.

**The general defect:** convention propagates through the *dependency graph*,
while every detector so far is *content-based*. A witness that merely records
a number derived from convention-C inputs is undetectable from its own bytes.
The fix has to be provenance-based — taint a witness if its producer reads a
tainted witness — which the ordering graph already built for `--stale` can
supply.

## And the producer has been printing a 48% internal disagreement

Re-running `atomic_tr_m_mpfr_50dps.py` (whose bridge module
`tr_m_wenzl_bridge_mpfr.py:573` *already* reads `z = q**3/(q**2+1)`, i.e. the
code is D while the committed witness is stale C) prints, for the deuteron:

    [peel]  tr_M(q_0)   = 0.57517233101788385191979179668715365887545302563801
    |bridge - peel|     = 0.18681514229410284461801930172180759299709038862953

So its two internal paths disagree by 48%, every run, and the witness records
the bridge (C-side) one. My convention-D sum `Σ_λ y_λ^D χ^λ = 0.5750909`
lands on the **peel** side.

**Unresolved, and I am not asserting otherwise:** peel gives 0.5751723 vs my
D sum 0.5750909 — a 1.4e-4 relative gap that is far too large to be precision
and is not explained. Candidates: a different braid normalisation in the peel
path, a writhe/framing factor, or a third convention. Which of peel / bridge /
Σ y^D χ is canonical D is **not** established here.
