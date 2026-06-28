# W_λ defect ladder — degree-3k law confirmed exactly through k=5 (Kerov route)

**Date:** 2026-06-28
**Branch:** `claude/wlambda-ladder-higher-rungs-2026-06-28`
**Status:** Numerical-exact confirmation (not a proof). Extends PR #2965.
**Check:** [`computations/keystone_wlambda_ladder_higher_rungs.py`](../../computations/keystone_wlambda_ladder_higher_rungs.py) (parameter-free, exit 0).
**Witness:** [`computations/wlambda-ladder-higher-rungs.witness.json`](../../computations/wlambda-ladder-higher-rungs.witness.json).
**Keystone bean:** `s5bb`; ledger [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).

## What was tested

The q-Plancherel defect expands as

$$
  1 - Z(n) \;=\; \sum_{k\ge 1} c_{2k}(n)\, h^{2k}, \qquad h = q - q^{-1},
$$

with each rung `c_{2k}(n)` a polynomial in `n`. The first two are settled:

| rung | closed form | degree | status |
|------|-------------|--------|--------|
| `c_2(n)` | `−n(n−1)(2n−13)/144` | 3 | **Lean-proved** (`n144C_closed_form`) |
| `c_4(n)` | `D(n)` | 6 | exact (PR #2965) |

The empirical pattern is **`deg c_{2k}(n) = 3k`**. PR #2965 confirmed it for
`k ≤ 3` via the new Kerov–Plancherel moment route (exact `Fraction`
arithmetic, no Taylor extraction). This probe extends the check to `k ≤ 5`.

## Result

Computing `c_2..c_10(n)` exactly over `n = 2..19` via `exact_ladder(n, 5)`
and reading off the polynomial degree by finite differences:

```
c_2(n):  degree 3   (3k = 3)   held-out ✓
c_4(n):  degree 6   (3k = 6)   held-out ✓
c_6(n):  degree 9   (3k = 9)   held-out ✓
c_8(n):  degree 12  (3k = 12)  held-out ✓
c_10(n): degree 15  (3k = 15)  held-out ✓
```

**Degree-3k law holds exactly through k = 5.**

### Held-out predictive check (not an interpolation tautology)

A degree match alone is weak — any `3k+1` points define *some* degree-`3k`
polynomial. So for each rung we fit the polynomial on the **minimal window**
`n = 2..(3k+2)` (`3k+1` points), then *predict* `c_{2k}(n)` at every larger
`n` up to 19 and confirm the prediction equals the independently-computed
Kerov value **exactly** (Fraction equality). All five rungs pass — the
degree-`3k` law is genuinely predictive.

### Cross-check against the Lean closed form

`c_2(n)` computed by the Kerov route equals `−n(n−1)(2n−13)/144` for all
`n = 2..19` — agreeing with the sorry-free Lean theorem
`QOU.BraidKnot.WLambdaDefectClosedForm.n144C_closed_form`.

## Scope (what this is and is not)

- This is **numerical-exact evidence** (exact rational arithmetic over a
  finite `n`-range with a held-out predictive check), **not** a proof of the
  degree-`3k` law for all `k`. A proof would bound the degree of the Kerov
  moment-series composition `Z = E∘T` rung-by-rung; that remains open.
- Scope unchanged from PR #2928/#2965: this is the **q-Plancherel `W_λ`
  combinatorics** (Hecke-dual side), not the `V_λ`/geometry side, and does
  not touch the open `η ↔ w` resolvent step of the Klein bridge.
