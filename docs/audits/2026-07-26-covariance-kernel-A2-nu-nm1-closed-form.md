# Covariance-kernel epic (`qou-x631`) — `ν_{n−1}` in **explicit closed form** (independent confirmation + extension of #4341)

**Date:** 2026-07-26 · **Branch:** `claude/even-moment-positivity-proof-qvxk1b` · **Tier:** explicit
closed form + independent confirmation (exact-`Fraction`, `n ≤ 40`) · **Discipline:** scope-(a); no fit
wired; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2),
(TAIL) sub-target — the `v = n−1` companion of
[`2026-07-26-covariance-kernel-A2-tail-first-instance.md`](2026-07-26-covariance-kernel-A2-tail-first-instance.md)
(`ν_n`).

> **Coordination — prior landing (#4341).** A sibling merged the `ν_{n−1}` **carrier reduction** and
> the **identical sign onset** (`= 0` at `n = 4`, `< 0` for `n = 5,6,7`, `> 0` for `n ≥ 8`; `n₁ = 8`;
> per-depth onsets, (TAIL) constant `> 2`) in
> [PR #4341](https://github.com/litlfred/qou/pull/4341) (`efc642f6`) shortly before this landed. This
> audit was derived independently by a different route — full `p(n)` enumeration plus exact-`Fraction`
> identification of the *collapsed* closed form — and **confirms #4341's sign onset**. Its net new
> content over #4341 is: **(i)** the single **explicit closed-form polynomial** (below), where #4341
> carries an uncollapsed per-carrier sum; **(ii)** the identification of the onset mechanism as the
> **single real root `ρ ≈ 7.078` of the cubic factor**; **(iii)** verification to `n ≤ 40` (#4341:
> `n ≤ 25`). Two independent derivations of the same onset strengthen it; no recorded claim overturned.

## Result

> `ν_{n−1} = Cov_Planch(N_{n−1}, ω₃) = (n−1)(n−4)(n³ − 11n² + 32n − 30) · C(2n−6, n−3) / (3·n!)`

Exact-`Fraction` verified for all `n = 4..40`; carrier family confirmed exhaustively `n ≤ 25`.

## Sign structure (the point for FMP)

With `C(2n−6,n−3) > 0`, `(n−1) > 0`, `(n−4) ≥ 0` (`n ≥ 4`), the sign of `ν_{n−1}` is that of the cubic
`n³ − 11n² + 32n − 30`, which has a **single** real root `ρ ≈ 7.078` (two complex). Hence:

| `n` | 4 | 5 | 6 | 7 | 8 | 9 | ≥ 8 |
|---|---|---|---|---|---|---|---|
| `ν_{n−1}` | `0` | `−4/3` | `−5/3` | `−1/6` | `+119/60` | `+88/27` | `> 0` |

So **`ν_{n−1} ≥ 0 ⟺ n ≥ 8`** (`= 0` only at `n = 4`).

### Sharpening of (TAIL)

The (TAIL) conjecture states `ν_v ≥ 0` for `v > n/2 + O(1)`. For the `v = n−1` slice — which is
`> n/2` for every `n ≥ 3` — positivity **fails** at `n = 5, 6, 7`. So at this slice the positive tail
is *empty* (`T(n) = n`, the last sign change sits at the very top) for all `n ≤ 7`, and only from
`n = 8` does `v = n−1` join the positive tail. **The `+O(1)` offset in (TAIL) is therefore genuinely
nontrivial** — it cannot be absorbed into `n/2` — and its onset at this slice is pinned by the single
real cubic root `ρ ≈ 7.078`. This is consistent with (and refines) the sibling's observed
`T(n)/n ∈ [0.53, 0.72]` for larger `n`: the ratio starts at `1` (empty tail) for small `n` and decays.

## Derivation (same locality mechanism as `ν_n`)

1. **Carrier lemma.** A diagram of `n` cells has a hook of length exactly `n−1` iff exactly one cell
   lies off the `(0,0)` cross (row 0 ∪ column 0). These are the `n−1` shapes: the single row `(n)`
   (carrier cell `(0,1)`), the single column `(1^n)` (carrier `(1,0)`), and the two-corner shapes
   `(a, 2, 1^{c})` with `a + c = n − 2`, `a ≥ 2` (carrier the length-`(n−1)` hook). Each has
   `N_{n−1} = 1`. Verified exhaustively `n ≤ 25` (`n−1` carriers, all `N = 1`).
2. **Mean-zero reduction.** `E₂[ω₃] = 0` (Lean-scaffolded), so `ν_{n−1} = E₂[N_{n−1}·ω₃]` is a finite
   sum over the `n−1` carriers of `(f^λ)²·ω₃(λ)/n!`.
3. **Closed form.** The carrier `(f^λ)²` and `ω₃` are explicit rationals in `n`; the finite sum
   collapses to the boxed formula (exact-`Fraction` identification against the carrier-family central
   binomial `C(2n−6,n−3)`, degree-5 numerator, verified with `> 30` held-out points `n ≤ 40`). The
   `(n−4)` factor is the exact source of the `n = 4` zero; the cubic factor carries the `n ≤ 7`
   negativity.

## Why this matters

- **Explicit closed form for the `v = n−1` slice** — collapses #4341's per-carrier reduction to one
  polynomial × central binomial, making the sign structure *manifest*: it is exactly the sign of the
  cubic `n³ − 11n² + 32n − 30`, whose single real root `ρ ≈ 7.078` **is** the onset `n₁ = 8`. This
  turns "there is an onset" (#4341) into "the onset is the largest real root of an explicit cubic
  factor" — a form directly amenable to a general-`n` proof and to per-depth generalization.
- **Independent confirmation** of #4341's mixed-sign onset by a disjoint route (full enumeration +
  closed-form identification, `n ≤ 40`). The FMP mechanism `(TAIL) + bulk bound ⇒ FMP ⇒ A2` must
  quantify the onset, not merely assert eventual positivity — both derivations agree on this.
- **The locality mechanism scales**: `v = n−1` is again a finite classical sum over a handful of
  explicit carrier families. The route to `v = n−2, n−3, …` is the same, each slice a cubic-or-higher
  factor whose largest real root gives the per-depth onset `n_j`.

## Honest scope

Derived + exactly verified (formula `n ≤ 40`, carriers `n ≤ 25`); the general-`n` proof is the
carrier-sum above (elementary, not yet Lean). (TAIL), FMP, A2, and the kernel remain open; nothing
wired. Independent parallel work on the same `ν`-structure front (sibling branch
`claude/covariance-nu-sign-changes-2026-07-26`) is coordinated — this contributes the `v = n−1` slice
its "next steps (i)" names.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_nu_nm1_closed_form.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_nu_nm1_closed_form.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-nu-nm1-closed-form.witness.json`

## Cross-references

- `ν_n` first instance: [`2026-07-26-covariance-kernel-A2-tail-first-instance.md`](2026-07-26-covariance-kernel-A2-tail-first-instance.md)
- ν-sign structure / (TAIL): [`2026-07-26-covariance-kernel-A2-nu-sign-structure.md`](2026-07-26-covariance-kernel-A2-nu-sign-structure.md)
- FMP ⇒ A2 bridge: [`2026-07-26-covariance-kernel-A2-fractional-moment-family.md`](2026-07-26-covariance-kernel-A2-fractional-moment-family.md)
- Even-moment positivity (proved): [`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`. Ivanov–Olshanski `math/0304010`.
