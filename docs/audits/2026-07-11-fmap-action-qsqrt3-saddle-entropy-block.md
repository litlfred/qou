# The 4₁ resurgence action over ℚ(√−3): the numerical Kashaev-ladder route is entropy-blocked

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (even channel, action A) ·
**Tier:** numerical (decisive negative) · **Discipline:** no fit, no c_k value, no
wiring, no tier change. Follow-up to
[`2026-07-11-fmap-action-pin-and-hexagonal-prune.md`](2026-07-11-fmap-action-pin-and-hexagonal-prune.md)
(#3508: A ≈ 0.688 real, not a clean framework constant).

## The lead and the test

The prior action-pin audit concluded the route to a *closed form* for the
even-channel resurgence action is "the exact saddle expansion of the Kashaev sum
(rationals over ℚ(√−3)), not a higher-order numerical fit." ℚ(√−3) is the
**invariant trace field of the figure-eight knot 4₁** (the arithmetic hyperbolic
knot; the Eisenstein / hexagonal field), so it is the correct arithmetic home for
the 4₁ perturbative expansion.

Formalize-first, this audit ran the cheap decisive check *before* committing to
the expensive exact computation: **can the ℚ(√−3) arithmetic be recovered by PSLQ
on the numerical Kashaev-ladder coefficients?**

Method: high-precision (dps 200–220) `log J_N(4₁)` on `N = 300…1180`, QR
least-squares fit of `log J_N − (3/2)log N` against `{N, 1, 1/N, …, 1/N^K}` (Vol
recovered to `~2×10⁻²³`), giving the 1/N^m ladder coefficients `c_m` (the
coefficient of `1/N^m`, `m = 1…K`). Each `c_m` (and the Ohtsuki-convention
rescalings `c_m·m!·(2π)^m`) was PSLQ-tested for rationality under torsion
normalizations `3^{a·m}`, `a ∈ {0, ¼, ½, 1, −½}`.

## Result — REFUTED (scope-(a)): the numerical route does not reach the arithmetic

No `c_n` (n = 1…9) is a clean rational under any tested ℚ(√−3) torsion
normalization. Two structural reasons, both expected:

1. **The coefficients are a divergent (resurgent) asymptotic series.** `c_n` grows
   **factorially**, `c_n ~ C·n!/A^n` with `A ≈ 0.688` — this is exactly the Borel
   singularity the #3508 large-order ratios `A_k = k·c_{n−1}/c_n → A` measured.
   `c_n·n!·(2π)^n` therefore grows like `(n!)²·(2π)^n` (4.6, 210, 1.9×10⁴,
   3.2×10⁶, …), far outside PSLQ's reach.
2. **Fit contamination at high n.** Only `Vol` and the first few `c_n` are
   ~25-digit accurate; the finite-`N` truncation + least-squares basis
   contaminate `c_{n≥5}`, below the precision PSLQ needs for a rational with a
   nontrivial denominator.

This is the **same entropy-block class** as the c_k PSLQ result (#3536 P4:
"empirical c₃ carries ≤2.2 digits"): a numerically-extracted coefficient cannot
be identified with its exact arithmetic form when the extraction precision is
below the height of the target rational.

## What stands, and the exact route

- **Solid arithmetic fact (not chased numerically):** the 4₁ invariant trace
  field **is** ℚ(√−3); the complex volume is `CVol(4₁) = 2i·Λ(π/3)` with `CS = 0`
  (`𝔙` real, #3482). ℚ(√−3) is the arithmetic home of the expansion — this is
  classical, not in question.
- **The exact route is NOT a fit:** the perturbative coefficients must be computed
  *exactly* from the **Ohtsuki state-integral saddle recursion** (the
  Feynman-diagram / Gaussian-moment expansion around the geometric saddle of the
  4₁ Andersen–Kashaev state integral), which produces the `c_n` as exact elements
  of ℚ(√−3) by construction. That is a research-grade symbolic computation, not a
  PSLQ on numerics — and it is what a genuine closed form for `A` requires.

## Net

The even-channel action `A ≈ 0.688` stays a real categorical invariant of the
amphichiral 4₁ sector whose **arithmetic home is ℚ(√−3)** (the trace field), but
its exact form is **not** recoverable by numerical identification — the
Kashaev-ladder coefficients are a fit-contaminated divergent series. The exact
saddle recursion is the only route; the numerical PSLQ avenue is closed
(entropy-blocked), recorded here so it is not re-chased. No fit; no c_k value; no
wiring; no tier change.

## Cross-references

- Action real/amphichiral, not a clean constant (#3508): [`2026-07-11-fmap-action-pin-and-hexagonal-prune.md`](2026-07-11-fmap-action-pin-and-hexagonal-prune.md)
- c_k PSLQ entropy block (same class, #3536 P4): [`2026-07-11-qbeta-ck-untested-avenues-and-literature.md`](2026-07-11-qbeta-ck-untested-avenues-and-literature.md)
- Odd-channel companion (merged this session): [`2026-07-11-wn-residue-weight-kernel-derive-refute.md`](2026-07-11-wn-residue-weight-kernel-derive-refute.md); KC17 dichotomy PRs #3556 / #3563
