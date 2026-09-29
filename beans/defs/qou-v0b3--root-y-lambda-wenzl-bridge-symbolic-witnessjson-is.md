---
# qou-v0b3
title: 'ROOT: y-lambda-wenzl-bridge-symbolic-witness.json is convention C and has no producer'
status: completed
type: task
priority: normal
created_at: 2026-08-10T15:25:53Z
updated_at: 2026-09-03T14:57:31Z
---


## The finding

`qou-eea0` is scoped as *"the producers are all convention D; their committed
outputs are not"* — so re-running each producer should close the gap. It
cannot. The convention is defined in a **symbolic** witness with **no
producer**, and every downstream number is a faithful evaluation of it.

```
y-lambda-wenzl-bridge-symbolic-witness.json     <- SYMBOLIC, convention C, NO PRODUCER
  |  regenerate_y_lambda_mpfr.py  (SOURCE, line 60 — evaluates at q0, derives nothing)
  v
y-lambda-mpfr-witness.json / y-lambda-mpfr-proton-witness.json   (223 three-row hits each)
  |  tr_m_wenzl_bridge_mpfr.load_y_lambda_for_q0
  v
chi_at_q0_via_hoefsmit_mpfr.py  ->  6 chi witnesses (p, n, D, T, 3He, 4He)
  |
  v
7 producers (aK_via_lp_dual, aK_via_lp_dual_full, rho_w_crystal_vertex_trace,
             y_lambda_at_q0_cache, e0_lambda_tryall, delta_lambda_2row_…,
             probe_pauli_young_…)
  |
  v
8 more via y-lambda-at-q0.witness.json
```

## Evidence

The symbolic entry for the 3-row partition `[1,1,1]` at `n = 3`:

```
q**6*(1 - 1/(q**(5/2)*(q**(3/2) + (1 - q**2)*(q + 1))))*(1 - 1/(sqrt(q)*(…
```

- `sympy.simplify(...).equals(0)` → **False**. Not identically zero.
- At the proton q₀ it evaluates to **0.022744942577009783…**, which is the
  registry convention-C fingerprint `0.02274491`.
- Under convention D every `y_λ` with `ℓ(λ) ≥ 3` vanishes **identically**
  (Schur–Weyl on a two-dimensional fibre).

The half-integer powers (`sqrt(q)`, `q**(3/2)`) are the convention-C Markov
parameter `z = 1/(q^{1/2} + q^{-1/2})` shape — the same `z` the C8 criterion of
`audits/weight-factor-audit` evaluates to `0.4993203341836944…`.

## Why nothing caught it

`_structural_hits` called `float()` on each `y_lambda` and swallowed the
`ValueError`. This file stores `y_lambda_symbolic` as **expression strings**, so
every entry was skipped in silence: **0 fingerprints, 0 structural hits**, for a
7 MB file that defines the convention for the entire cascade. Fixed in
PR #4928 (syntactic screen; the file now surfaces as an orphan).

The same blindness should be assumed in `scripts/convention-c-witness-audit.py`
(the "selftest 7/7" canonical detector) until checked — its structural rule has
the same shape.

## What this means for qou-eea0

**Re-running producers cannot move this corpus to convention D.** Ordering was a
real and separate defect — the first two passes ran alphabetically so
downstreams re-emitted upstream C, now fixed by `topo_order()` — but even a
perfectly-ordered pass evaluates the same convention-C symbolic source.

The migration is a **derivation**, not a regeneration: `y_λ(q)` must be re-derived
under convention D and the symbolic witness re-issued. Everything downstream then
follows mechanically from the existing harness.

## Open question for the owner

Which is the convention-D `y_λ`? This is where it stops being mechanical. The
corpus carries several candidate weight families that are explicitly *distinct*
at `q ≠ 1` (AGENTS.md §notation: `y_λ` / `w_λ` / `w̃_λ` "are **distinct** at
`q ≠ 1` — never conflate"), and `qou-u2jg` records convention D as the
Temperley–Lieb radical quotient. Deriving the D-convention `y_λ` and re-issuing
this witness is the actual remaining work.

## Close condition

`y-lambda-wenzl-bridge-symbolic-witness.json` carries `y_λ ≡ 0` for every
`ℓ(λ) ≥ 3`, is written by a named producer under version control (it currently
has none), and a dependency-ordered harness run leaves zero structurally-C
witnesses downstream. Hand-editing the symbolic file is not a close —
`qou-eea0` hard constraint: nothing hand-edited.



## RESOLVED 2026-09-03 (verified on main 440c6a164f)
computations/y-lambda-wenzl-bridge-symbolic-witness.json now carries markov_convention: D, description 'y_lambda = [n-2k+1]_q/[2]_q^n on two-row partitions, exactly 0 on three-or-more rows', scriptFile computations/regenerate_y_lambda_symbolic_convention_d.py (exists), and grep -c 'sqrt(q)' = 0 — the ROOT above (symbolic, convention C, no producer) no longer describes the file. regenerate_y_lambda_mpfr.py line ~105 documents the fix: it takes numbers from y_lambda_wenzl_bridge_numeric (D) rather than sympify'ing the JSON. Lean side: the two-row root is proved (see qou-smtg close note). Closing; the detector-blindness lesson in the body stands as history.
