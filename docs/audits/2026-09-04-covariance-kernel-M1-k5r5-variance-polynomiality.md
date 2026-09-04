# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: `V_A` has no polynomial closed form; `V_W` does, exactly

**Date:** 2026-09-04 · **Branch:** `claude/m1-k5r5-variance-polynomiality-2026-09-04` ·
**Tier:** measurement (one negative with a passing control, one small positive) · **Epic:** `qou-x631`; gap `qou-k5r5`.

## Why this was checked before the analytic attack

PR #6602 narrowed the remaining work to one target: a rigorous finite-`n` bound on
`δ_A = (V_A/n² − v_A)/v_A`. That is a Kerov-CLT-with-explicit-error project. Formalize-first says
check first whether the object has an exact closed form — a polynomial `V_A(n)` would not merely
*bound* `δ_A`, it would give it exactly at every `n`, and the `n ≥ 79` tail with it.

## The objects, named precisely

From the C-landscape probe's `stats()` — worth stating because the epic's names are opaque:

| symbol | is | shifted-symmetric? |
|---|---|---|
| `A` | `Σ_cells |c|`, the first **absolute** moment of the content distribution (`c = j − i`) | no (`|·|` is not a polynomial) |
| `D` | `Σ_u d_u²`, `d_u = #{cells of content u}` — squared diagonal multiplicities | no |
| `W` | `Σ_cells c² − C(n,2)`, the second moment, recentred | **yes** |

## Result ([`…_variance_polynomiality.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_variance_polynomiality.py), exit 0, exact `Fraction` over every partition of n, `n = 2…30`, NO float64)

| quantity | smallest exact polynomial degree ≤ 10 |
|---|---|
| `V_W = Var(W)` | **3** — reproduces all 25 held-out `n` exactly |
| `P = Cov(A, W)` | **NONE** |
| `V_A = Var(A)` | **NONE** |
| `V_D = Var(D)` | **NONE** |

> **`V_A` is not an exact polynomial in `n`.** `δ_A` has no closed form by this route, and the
> rigorous finite-`n` bound remains the only way through.

The denominators corroborate it directly: `V_A(12) = 339037063642199/29628426240000`, and by `n = 30`
the denominator is ~2.7 × 10⁵⁶. A polynomial in `n` with rational coefficients has bounded
denominators.

### The control is what makes the negative worth anything

`Σc²` **is** shifted-symmetric, so `V_W` should come out polynomial — and it does, at degree 3,
through the same fitter and the same data pipeline. **A negative from an unvalidated detector is the
failure mode this corpus has paid for repeatedly** (the detector-blindness taxonomy is 26 rows), so
the design puts a known positive through the identical path. Had `V_W` also read NONE, no verdict here
would be quotable.

Method note: the fit is exact Lagrange interpolation through the **first** `d+1` points, evaluated at
every **remaining** point. A fit that reproduces its own interpolation nodes proves nothing — the
held-out set is the verdict, and the nodes are excluded from it.

## A small positive: `V_W` in closed form

Checked exactly at all 29 tabulated `n` (asserted in the probe, not read off the table by eye):

> **`V_W = Var(Σ_cells c²) = n(n−1)(n−2)/3 = 2·C(n,3)`**

Since `ρ_P = P / √(V_A · V_W)`, **one of the three ingredients of `ρ_P` carries no finite-`n` error at
all**. Only `P` and `V_A` do. That is a simplification of the open target, not a step toward closing
it. Classical for a shifted-symmetric weight; confirmed here, not claimed as new.

## What this negative does *not* settle

It rules out a polynomial in `n` of degree ≤ 10 over `n ≤ 30`. It does **not** rule out a closed form
of another shape — a polynomial over a falling factorial, a harmonic-augmented form, a two-term
recursion. The corpus has already tried several such shapes **for `M₁`** and found none
([`…-antidiagonal-reformulation.md`](2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md):
`poly₄` and `n²H_n + poly₃` both fail). This probe neither repeats those nor extends them to `V_A`.

## What the corpus already held, and is not re-derived here

The non-polynomiality *mechanism* for the covariance family is established:

- [`…-A2-odd-moment-structure.md`](2026-07-25-covariance-kernel-A2-odd-moment-structure.md): for even
  `k` both weights are shifted-symmetric and `M_{2j}` is an exact polynomial in `n`; the odd weight
  `Σ_□ h^{2j+1}` is not, so `M_{2j+1}` is non-polynomial.
- [`…-antidiagonal-reformulation.md`](2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md):
  "the non-polynomiality of `M₁` is carried entirely by the non-shifted-symmetric" part.

Those are statements about the **covariance** family `M_k`. `V_A = Var(Σ|c|)` is a different object
and nothing in the corpus measured it — which is why the check was run rather than inferred by
analogy. The analogy turned out to hold; that it *would* was not evidence.

## Status of `qou-k5r5`

Gap **OPEN**, and the target is unchanged: a rigorous finite-`n` bound on `δ_A`, at `C ≤ m_∞√79 =
2.6681` on the proved `n^{-1/2}` shape (empirical envelope 0.0580; `n ≤ 78` certified exhaustively by
`b1-kappa-window-extension.witness.json`). What this adds is that the closed-form shortcut is closed,
and that `V_W` is exact so the bound has one fewer moving part.

## Cross-references

- The target: [`…-ratio-is-a-constant-not-a-rate.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-is-a-constant-not-a-rate.md) (#6602)
- The budget: [`…-ratio-route-is-the-target.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md) (#6576)
- Epic `qou-x631`; gap `qou-k5r5`.
