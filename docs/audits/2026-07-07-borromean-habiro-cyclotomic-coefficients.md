# Borromean Habiro cyclotomic coefficients C_l(q) — extracted + verified

**Date:** 2026-07-07
**Branch:** `claude/aj-conjecture-qou-uz5m6x` (PR #3470)
**Bean:** `n920`
**Script:** [`computations/habiro_borromean_cyclotomic_coefficients.py`](../../computations/habiro_borromean_cyclotomic_coefficients.py)
**Witness:** `computations/habiro-borromean-cyclotomic-coefficients.witness.json`

## What this delivers

The corpus had the Borromean diagonal colored Jones `J_{B,n}` in Habiro's
closed form (verified, 4/4 anchors) but had **never extracted the
cyclotomic coefficients** `C_l(q)` themselves. This closes bean `n920`'s
headline input: the `C_l` are the canonical object any `c_k`↔Borromean
cross-check must consume.

Habiro's cyclotomic expansion

    J_{B,n} = sum_{l>=0} C_l(q) · B_l(n),   B_l(n) = prod_{j=1}^l {n+j}{n-j}

with `{a} = q^{a/2} − q^{-a/2}`. The basis is **exactly** Habiro's standard
one, since `{n+j}{n-j} = (qⁿ+q⁻ⁿ) − (qʲ+q⁻ʲ)`.

## The coefficients (C_0 … C_6)

```
C_0 = 1
C_1 = -(q²-3q+1)(q²-q+1) / [q(q-1)²]
C_2 = (q⁶-2q⁵-2q⁴+3q³-2q²-2q+1) / q³
C_3 = -(deg-16 palindrome) / [q⁶(q-1)²(q+1)²]
C_4 = (deg-30 palindrome) / [q¹⁰(q-1)⁴(q+1)²(q²+q+1)²]
C_5 = -(deg-36 palindrome) / [q¹⁵(q-1)²(q²+q+1)²]
C_6 = (deg-56 palindrome) / [q²¹(q-1)⁴(q+1)²(q²+1)²(q²+q+1)²]
```

Full expressions in the witness (`cyclotomic_coefficients_q`).

## How it is verified (exact, over-determined — not a fit)

- **Triangular isolation.** `B_l(n)=0` for `l≥n`, so each `C_l` is
  isolated at its diagonal `n=l+1`:
  `C_l = (J_{B,l+1} − Σ_{m<l} C_m B_m(l+1)) / B_l(l+1)`.
- **Over-determination (the real check).** Each `C_l` is fixed at `n=l+1`,
  then the **same** `C_l` must rebuild `J_{B,n}` at every larger `n`. The
  script confirms `Σ_{l<n} C_l(q) B_l(n) == J_{B,n}` **exactly for
  n=1..7** — a genuine, non-circular test of Habiro's n-independence (a
  wrong or n-dependent `C_l` would break the reconstruction).
- All arithmetic stays in `s` (clean Laurent objects); `s²→q` is a direct
  monomial term-walk (no `sqrt`, no `simplify` — both blow up on the
  cube-summand expressions).

## Structural observations (recorded, not identified)

- **Poles at roots of unity.** Every `C_l` (l≥1) has a genuine denominator
  supported on cyclotomic factors `(q-1), (q+1), (q²+q+1), (q²+1)` — i.e.
  the `C_l` live in the **Habiro ring** (cyclotomic completion), not in
  `ℤ[q^{±1}]`. This is the expected and correct structure for a link
  (vs. the polynomial coefficients Habiro proved for knots), not an
  anomaly.
- **Palindromic numerators.** Each numerator is `±`-palindromic under
  `q→1/q`, consistent with the amphichirality of the Borromean rings
  (bar-symmetry anchor of the tower).

## Epistemic status / c_k

**No c_k identification is asserted.** The corpus precision-ladder `c_k`
are Q_β / meson / m_p **truncation** coefficients (near-matches to Hopf
Jones; only `c_2` Taylor-exact — see the AGENTS.md c_k banner). The `C_l`
here are the Borromean **cyclotomic** coefficients — a distinct object.
This audit provides them as the clean, verified input; it does **not**
open, close, or wire any `c_k` claim. Per the formalize-first /
critical-distance disciplines, forcing a numerical `C_l(q_0)`↔`c_k`
coincidence would be exactly the numerology this repo guards against.

## Disposition

Audit-only. Wires into nothing. Advances bean `n920` by supplying the
long-missing cyclotomic coefficients with an exact over-determined
verification.
