# Topic 2 — m_p linking_weight operator-valued probe: target bracketed but no canonical weight closes

**Date:** 2026-06-02
**Branch:** `claude/m-p-linking-weight-and-binding-link-2026-06-02` (PR #1712)
**Trigger:** Topic 2 of PR #1698 follow-up — find a categorical-canonical weighted sum that lands at the CODATA-implied linking_weight `2.461648` (instead of Family A's `2.532780`).

## Setup

PR #1698 isolated the +2.89 % m_p gap as living entirely in the proton's `linking_weight_family_a`:

```
linking_weight_family_a(q_0) = (3q² + 4 + 3q⁻²)/4 = 2.532780  ← uniform H_4 sum / n
CODATA-implied (round-trips m_p)                  = 2.461648
GAP = +28900 ppm = +2.89 %
```

Family A is the **proved** H_4 categorical-identity `(Σ_{λ⊢4} dim_q V_λ) / n` per `lambda-scale-substrate-form.lean`. The +2.89 % is acknowledged CAL-4 (per `linking_weight_canonical_object_lwfix.witness.json`).

## What was tested

Six **canonical, parameter-free** Wedderburn weight functions on partitions of n ∈ {3, 4, 5}:

| name | formula | meaning |
|---|---|---|
| `uniform` | w = 1 | Family A baseline (divide by n) |
| `dim_q` | w = dim_q(λ) | self-weighted (first moment) |
| `dim_q²` | w = dim_q²(λ) | q-Plancherel measure |
| `1/dim_q` | w = 1/dim_q(λ) | Frobenius co-Casimir reciprocal (T4 prefactor) |
| `[hook]_q⁻¹` | w = Σ_h 1/[h]_q | q-deformed hook density |
| `y_λ` | w = dim_q²(λ)/[n]_q! | Wenzl weight (mass-formula T1) |

All six × three n-values = 18 candidates. **No fits.**

## Result

**0 PROVED, 0 NEAR-MATCH, 2 WEAK, 16 REFUTED.**

| n | weight | L(n, w; q_0) | err vs 2.461648 | tier |
|---|---|---|---|---|
| 4 | `uniform` (= Family A) | 2.532780 | **+2.89 %** | WEAK |
| 4 | `dim_q` (self-weighted) | 2.438529 | **−0.94 %** | WEAK |
| 4 | `dim_q²` (q-Plancherel) | 2.709193 | +10.06 % | REFUTED |
| 4 | `y_λ` (Wenzl) | 2.709193 | +10.06 % | REFUTED (= dim_q² · const) |
| 4 | `[hook]_q⁻¹` | 2.141007 | −13.03 % | REFUTED |
| 4 | `1/dim_q` | 1.589117 | −35.44 % | REFUTED |
| 5 | `1/dim_q` | 2.309830 | −6.17 % | WEAK |
| (other 11 entries: all REFUTED at > 10 % off) | | | | |

## Key observation — the target is BRACKETED

| weight at H_4 | value | err |
|---|---|---|
| Family A (uniform) | 2.532780 | **+2.89 % above** target |
| **TARGET (CODATA)** | **2.461648** | — |
| dim_q-weighted | 2.438529 | **−0.94 % below** target |

The target sits **between** two canonical weights on the same H_4 partition lattice. A linear combination would close it empirically (`α ≈ 0.234` gives exact match), **but that's a fit** — explicitly forbidden per AGENTS.md §"Δ_λ gate" / "Before declaring 'open' math".

## What this rules out

- ❌ None of the **seven** standard categorical weights (uniform, dim_q, dim_q², 1/dim_q, hook-density, Wenzl y_λ, **abs-content**) at H_3, H_4, or H_5 is the canonical proton linking_weight. (abs_content added per sibling PR #1709's Δ_λ binding-measure scan — refuted here at all three n.)
- ❌ The 2.461648 target is NOT a clean weighted sum over a single H_n partition basis with a categorical weight; if it were, one of these would have hit within ~1 ppm.
- ❌ Mixed-H_n test with canonical α values (1/2, 3/4, 1/4, h_q², [3]_q/[4]_q, dim_(2,1)/Σ_H4): closest is `α = h_q² ≈ 0.0437` giving +7664 ppm (WEAK). NOT a closure; coincidence at the 1-parameter-fit level, not a structural finding.

## What this opens

The fact that Family A (over-weights toward LARGER-dim partitions) and `dim_q`-weighted (further over-weights toward larger-dim) BOTH miss in opposite directions on the n=4 sum suggests the canonical linking_weight is **not a single-H_n object** at all. Two not-yet-tested directions:

1. **Mixed H_n contribution** — sum over multiple n's (e.g. `α · Family A(H_3) + β · Family A(H_4)`) with categorical α, β. The proton's actual strand count is 3, but the Family A convention uses H_4; a natural mix would be `Family A at H_3 + correction from H_4`.
2. **Operator-valued (not scalar) linking_weight** — the canonical Wenzl branching combiner (PR #1698 Phase C `WenzlAOperator`) takes per-atom (Z, N) input; its action on `linking_weight` may be a non-commutative operator whose eigenvalue at the proton state is 2.461648, not a scalar.

Direction (2) is the substantive Subgoal-1 next step — the operator-valued path mentioned in `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`. Direction (1) is a smaller-scope test that's worth running first if cheap.

## Coordination

- **#1503** α_em subgoal-1 closure precedent — the α_em case landed at a structural form with a Schwinger factor `(1 − h²α)` modifying the leading [2]_q/(8π). The analog here would be a `(1 + ε(q))`-correction modifying the Family A baseline; **no such categorical ε(q) yet identified**.
- **#1521** α_em Habiro categorical ID — the α_em Habiro element is `[2]_q · (1 − h²α)`. The Q_β analog (Topic 1, sibling branch PR #1713) just showed Q_β's Habiro element has radius-of-convergence = u_substrate. If the m_p linking_weight has analogous "evaluation at the boundary of analyticity" structure, the categorical ε(q) might be a residue near such a singularity.

## What this PR does NOT claim

- Does NOT close the m_p +2.89 % gap.
- Does NOT propose a fit (the 0.234 linear combination is empirical-only, not a structural finding).
- Does NOT refute the operator-valued path — that path requires the Wenzl branching combiner from PR #1698 (Phase C `WenzlAOperator` class), which was deferred there pending universal H_9+ extracts.

## Files

- Probe: [`computations/m_p_linking_weight_operator_valued_probe.py`](../../computations/m_p_linking_weight_operator_valued_probe.py)
- Witness: [`computations/m-p-linking-weight-operator-valued-probe.witness.json`](../../computations/m-p-linking-weight-operator-valued-probe.witness.json)

## Cross-references

- Scope: [`docs/coordination/2026-06-02-m-p-linking-weight-and-binding-link-scope.md`](../coordination/2026-06-02-m-p-linking-weight-and-binding-link-scope.md)
- PR #1698 final verdict: [`docs/audits/2026-06-02-subgoal-1-final-verdict.md`](2026-06-02-subgoal-1-final-verdict.md)
- Canonical reference (refuted routes): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- Q_β Habiro radius-of-convergence finding (sibling Topic 1): [`docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`](2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md)
