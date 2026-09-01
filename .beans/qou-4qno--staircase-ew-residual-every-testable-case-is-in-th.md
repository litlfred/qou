---
# qou-4qno
title: 'Staircase EW-residual: every testable case is in the TL kernel — rho_k has k rows, so only k=2 is physical at N=2, and the block calls that case untestable'
status: todo
type: task
created_at: 2026-09-01T07:53:25Z
updated_at: 2026-09-01T07:53:25Z
---

Found while auditing the Standard-Model work against the full tower (owner request, 2026-09-01). Probe: `computations/qbeta/qbeta_staircase_ew_lives_in_the_tl_kernel_probe.py` (4/4).

## The observation

`content/quantum-observable-universe/mass-theory/staircase-ew-residual.md`
conjectures, for the staircase partition `rho_k = (k, k-1, ..., 1)`, an
eigenvalue ratio `q^{1/(2k-1)}` on the Specht module `V_{rho_k}` of
`H_{n_k}(q)`. **`rho_k` has exactly `k` rows**, so the Schur-Weyl row cap
(`dim V_lambda = 0` when `l(lambda) > N`) gives `N_min(rho_k) = k`.

The framework's fibre is `N = 2` — `lem:feynman-eigenbasis-decomposition`
puts the cap `l(lambda) <= 2` **in the index set** of the mass channel's
decomposition. So of the conjecture's "for every `k >= 2`", **exactly one
instance is physical: `k = 2`.**

And `k = 2` is the case the block itself calls **untestable** — *"the word
collapses to length 0 ... renders the case untestable"*.

| k | rho_k | rows | dim | N_min | physical at N=2? | block's empirical content |
|---|---|---|---|---|---|---|
| 2 | (2,1) | 2 | 2 | 2 | **yes** | **untestable** (word length 0) |
| 3 | (3,2,1) | 3 | 16 | 3 | no | closes `cot theta_W` 2.19 % -> 0.13 % |
| 4 | (4,3,2,1) | 4 | 768 | 4 | no | pairwise ratio, 0.14 % rel. error |
| 5 | (5,4,3,2,1) | 5 | 292864 | 5 | no | — |

**Measured**, n = 6, convention D: `|omega_(3,2,1)| = 1.87e-16` against a
minimum `7.56e-2` over the `<=2`-row shapes; `720 = 6!` total against
`132 = Catalan(6) = dim TL_6` visible. So `(3,2,1)` is in the **kernel** of
`H_6(q) -> TL_6(q) = End_{U_q(sl_2)}(V^{(x)6})` and contributes nothing to any
trace the framework computes.

## What this is NOT

**Not a refutation.** The conjecture is about Specht modules of `H_{n_k}(q)`
as an abstract algebra; those exist for every `k` and the eigenvalue ratio is
not challenged here. **Downstream Lean is unaffected** — the block axiomatises
the conjecture as a hypothesis-only `class`, so its consumers are
rigorous-conditional and stay so.

What is in question is what the **empirical content** can mean. `cot theta_W`
is a physical observable, and the `k = 3` bullet reads it off a module the
framework's own fibre gives dimension zero.

## Why it matters beyond this block

This is the same defect `qou-i9gk` closed against Step 27 of `qou-cds1` on
2026-09-01 — reading physical content out of the trace-blind sector — surfacing
**independently in the electroweak sector**, where it has not been recognised.
It is a second instance, so the pattern is worth a sweep rather than a one-off
fix.

Related: `qou-e9le` (the two-row cap is proved in Lean and unused in compute)
is the compute-waste face of the same fact; `qou-fvzm` proves `N = 2` is
locked for the mass pipeline and that moving to `N = 3` re-weights channels the
pipeline already evaluates.

## Todo

- [ ] Decide with the owner whether the block should carry a row-cap caveat. It
      already disowns the number in other ways; this is an additional and
      structural ground, and editing a content block with a QA sidecar is an
      owner-facing editorial call, not an agent one.
- [ ] Sweep for other physical numbers read off `l(lambda) > 2` blocks. Two
      instances found so far without looking; there may be more.
