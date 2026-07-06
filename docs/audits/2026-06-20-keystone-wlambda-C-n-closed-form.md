# Closed form for the W_λ defect coefficient C(n): the n=7 sign change is exact

**Date:** 2026-06-20
**Branch:** `claude/fervent-noether-zssd1k`
**Status:** Closed-form derivation (verified) — no fit, no correspondence chain
**Follows:** PR #2525 ([`2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`](2026-06-20-keystone-wlambda-Z-defect-n-scaling.md)), which left `C(n)` as an unidentified empirical sequence
**Script:** [`scripts/keystone_wlambda_C_n_closed_form.py`](scripts/keystone_wlambda_C_n_closed_form.py) (`ALL CHECKS PASS`, exit 0)
**Frontier:** q-Bessel/heat-kernel geometric realization of `W_λ = d_q(λ)²/[n]_q!` (#2503 DG plan)

## What #2525 left open

PR #2525 established `1 − Z(n) = C(n)·h² + O(h⁴)` for the partition-function defect
`Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!`, with the empirical sequence `24·C(n) = 3, 7, 10,
10, 5, −7, −28` for `n = 2..8` — and explicitly **refuted** a hook-moment ansatz,
leaving `C(n)` unidentified. This note derives the closed form.

## Derivation (perturbation theory; no fit, no correspondence chain)

Put `q = e^{x/2}`, so `[m]_q = sinh(mx/2)/sinh(x/2) = m[1 + (m²−1)x²/24 + O(x⁴)]`
and `h = q − q⁻¹ = 2 sinh(x/2)`, `h² = x² + O(x⁴)`. Then the q-hook-length formula
gives

```
d_q(λ) = dim(λ)·[1 + (x²/24)(S_n − T_λ) + O(x⁴)],
   dim(λ) = n!/∏_c h_c,   S_n = Σ_{k=1}^n (k²−1),   T_λ = Σ_{c∈λ}(h_c²−1).
```

Since `Z(n) = (1/[n]_q!) Σ_λ d_q(λ)²` and `Σ_λ dim(λ)² = n!`, the cross terms collapse to

```
1 − Z(n) = (h²/24)·[ (2/n!) Σ_λ dim(λ)² Σ_c h_c²  −  S_n ] + O(h⁴).
```

The bracket needs the **Plancherel-expected squared-hook sum**
`M(n) := (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²`. The script verifies, in exact
integer arithmetic for `n = 2..14`:

> **Lemma (identity I).** `M(n) = n(3n−1)/2`.

Substituting `M(n)` and `S_n = n(n+1)(2n+1)/6 − n` collapses the bracket to a cubic:

> **Closed form.**
> ```
> 24·C(n) = −n(n−1)(2n−13)/6,     i.e.    C(n) = −n(n−1)(2n−13)/144.
> ```

Verified against the high-precision finite-difference `C_emp(n) = (1−Z)/h²` for
`n = 2..12` (`|err| < 1e-9`).

## The n=7 sign change is exact

`24·C(n) = −n(n−1)(2n−13)/6` has its only sign-determining factor `(2n−13)`, which
vanishes at `n = 6.5`. Hence

```
C(n) > 0   for   2 ≤ n ≤ 6,      C(n) < 0   for   n ≥ 7.
```

The numerical sign flip found in #2525 (`Z(7) > 1`) is **not an artifact**: it is the
linear factor `(2n−13)` crossing zero between `n = 6` and `n = 7`. The defect's whole
`n`-profile — rise to a max near `n = 4` (the quadratic envelope), then descent and
sign flip at `n = 7` — is the cubic `−n(n−1)(2n−13)`.

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| 24·C(n) | 3 | 7 | 10 | 10 | 5 | −7 | −28 |
| −n(n−1)(2n−13)/6 | 3 | 7 | 10 | 10 | 5 | −7 | −28 |

## Why it matters

- **The #2503 target is now a formula, not a table.** Any `S¹`-equivariant index
  realizing `W_λ` must reproduce a sub-leading heat-kernel coefficient exactly equal
  to `−n(n−1)(2n−13)/144` — a single cubic, falsifiable for every `n`. A geometric
  object whose second index coefficient is *any other* cubic is refuted; one matching
  it is strong positive evidence.
- **The "mass defect" framing is further tempered.** A sub-leading coefficient that is
  a sign-indefinite cubic in `n` is not a monotone-positive heat-kernel trace; it
  reinforces #2525's reading that `Z(n)` is a normalization constant (genuine measure
  `W_λ/Z(n)`), not a geometric mass defect.
- **Bar-even.** Leading order is `h²` (invariant under `q → q⁻¹`), so `C(n)` cannot by
  itself be the bar-odd 210 ppb muon shift (consistent with 44377f33).

## Discipline

- **No fit.** `C(n)` is the `q → 1` leading data of `W_λ`; `q₀` and the 210 ppb target
  are never used (the script computes nothing from them).
- **No correspondence chain.** Pure `S_n` (Hecke-package recursion → q-hook-length
  formula). The `2I → E8 → Lawrence–Zagier` chain is never invoked.
- **Formalization opportunity.** Identity I (`M(n) = n(3n−1)/2`, the Plancherel mean
  of the squared-hook sum) is a clean candidate for a Lean lemma; deferred (the
  sandbox Lean toolchain is currently network-blocked, and this PR touches no `.lean`).
- Manifold existence stays **owner-gated**; no physical claim introduced.
