# Coordination ledger — dilog Part-A Tauberian/DCT convergence

**Goal.** Close the one remaining open item of `conj:dilogarithm-archimedean-limit`:
the Tauberian/DCT convergence `(1−q)·log Φ_n(x;q) → Li₂(x)` for `x∈(0,1)`, i.e.
inhabit the `ArchimedeanLimit x` typeclass off `x=0`. Everything else in the dilog
thread (special values, reflection, duplication, derivative, integral rep,
Clausen, Part-A Bricks 1–2) is closed sorry-free on `main`.

## Two parallel routes (both permitted per the parallel-exploration directive)

| Route | Branch / PR | File | State (2026-07-24) |
|---|---|---|---|
| **Riemann-sum (LEADING)** | `claude/dilog-part-a-convergence-2026-07-19` / #4106 | `Archimedean/DilogPartAConvergence.lean` | B3.1–B3.4 sorry-free (target integral, convexity, `h_monotoneOn`, per-cell bounds, `riemann_error_bound`, `tail_bound`); **only B3.5 (assemble the ε-δ `ArchimedeanLimit` instance) remains.** Idle ~5 days. |
| **m-series (parallel)** | `claude/dilog-tauberian-coeff-limit-2026-07-24` / #4152 | `Archimedean/DilogPartARiemannSum.lean` | Two ingredient lemmas sorry-free: `tendsto_one_sub_div_pow_sub_one` (coeff `→ −1/(m+1)`), `tendsto_pow_mul_nhds_zero` (tail `→ 0`). **Stood down from racing to full closure** (see below). |

**No file conflict** (different modules). Naming: #4106 canonically owns "Part-A
Brick 3"; #4152's labels were renamed 2026-07-24 to "m-series termwise-limit
ingredient (1)/(2)" to remove the collision.

## Decision (converge-on-landing)

#4106's Riemann-sum route is the leading attack and ~1 lemma from closing the
whole DCT. Per the converge-on-landing directive, the m-series route (#4152)
**stands down from racing to full closure**; its two lemmas remain as
complementary independent-route ingredients (and a clean standalone coefficient
limit). The productive next step is **B3.5 on the Riemann-sum route**, not a
second full convergence proof.

## Next concrete task — close the DCT via B3.5

Assemble `instance : ArchimedeanLimit x` (for `0<x<1`) from #4106's landed bricks:
`(1−q)·log Φ_n = S_n` (Bricks 1–2) → `|S_n − ∫_{qⁿ}^1 h| ≤ (1−q)(h(1)−h(qⁿ))`
(`riemann_error_bound`) → `∫_{qⁿ}^1 h = ∫_0^1 h − ∫_0^{qⁿ} h = Li₂(x) − tail`
(`integral_zero_one_eq_LiTwo` + `tail_bound`, `|tail| ≤ qⁿ·x/(1−x)`) → the ε-δ
bound via `q^n ≤ e^{−n(1−q)} → 0` and `(1−q)(−log(1−x)) → 0`. Requires rebasing
#4106 onto current `main` first (it predates ~500 commits). Blocked on owner /
sibling sign-off on who takes B3.5 (asked on #4106).

## Consumers waiting on this

- `claude/alpha-em-zeta-anomaly-b1-2026-07-17` — the α_EM `1/π` per-mode-weight
  question reduces to this same open dilog convergence.
