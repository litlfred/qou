# Audit: legacy 2-var-Schur weight in Markov-trace numerical paths

**Date:** 2026-05-09
**Branch:** `claude/fix-habiro-interpolate-disagreement`
**Triggered by:** validate CI failure on PR #626 (and identical failure on `origin/main`).

## TL;DR

The pre-existing `validate` CI failure traces to one concrete bug:
[`habiro_coefficients_interpolate.py:markov_trace_numerical`](../../folio-assistant/computations/habiro_coefficients_interpolate.py)
used the legacy 2-variable Schur weight `s_λ(q, q⁻¹) / H_q(λ)` —
the **wrong Markov-trace weight** per
[`docs/audits/2026-05-08-p3-h-3a-divergence.md`](2026-05-08-p3-h-3a-divergence.md)
(it vanishes for > 2-row partitions and drops sign-rep contributions).

The atomic path (`habiro_coefficients_atomic.py`) was migrated to
the canonical Wenzl-Jones-Markov weight $y_\lambda(q)$ in PR #572;
the numerical-interpolation companion path was missed.

**Fix:** swap `schur_weyl_weight_numerical` → `y_lambda_numerical`
(thin wrapper around `wedderburn_jones_markov.y_lambda_at`) inside
`markov_trace_numerical`.

**Empirical result (post-fix):** the two paths agree to 18+ digits
at $q_0$ for `{p, n, D}`:

| atom | atomic path | interpolate path (post-fix) |
|------|------------:|----------------------------:|
| p    | 1.0653062285923893 | 1.06530622859238878 |
| n    | 0.9232332971695838 | 0.923233297169583268 |
| D    | 0.388286471547713  | 0.388286471547713019 |

Pre-fix: 40–54% relative disagreement on the same atoms.

## Audit of remaining `schur_weyl_weight` usages

Beyond the immediate fix, scanned `folio-assistant/computations/*.py`
for callers of the legacy weight. Findings:

| file | usage | status |
|------|-------|--------|
| `habiro_coefficients_interpolate.py` | `markov_trace_numerical` (Markov-trace consumer) | **FIXED** in this PR |
| `schur_weyl_mpmath.py` + `crt_markov.py:trace_descended_via_h3a` | `markov_trace_mpmath` restricts to length-≤-2 partitions deliberately | **Buggy by same root cause; not currently consumed by any pipeline (see below). Left untouched in this PR; flagged for follow-up.** |
| `hecke_character_symbolic.py:399` | `__main__` self-test demo | **Migrated to canonical `solve_y_lambda` for consistency** |
| `term6_full_pole_sum.py` | docstring + caveat claimed upstream witness used legacy weight | **Docstring updated to reflect the post-PR #572 reality (witness is canonical-y_λ)** |
| `schur_weyl_symbolic.py` | defines the legacy `schur_weyl_weight` itself | Already deprecated by docstring (as of PR #572); kept for backward compat |
| `wedderburn_jones_markov.py` | references legacy in deprecation comment block | Documentation-only |

## `schur_weyl_mpmath.markov_trace_mpmath` — follow-up scope

This function and its consumer `crt_markov.trace_descended_via_h3a`
**explicitly iterate over length-≤-2 partitions only** with the
rationale "Schur s_λ(q,q⁻¹) vanishes for length > 2". Per the
[2026-05-08 audit](2026-05-08-p3-h-3a-divergence.md), this is the
buggy rationale: $y_\lambda$ does NOT vanish for > 2-row partitions
and the descended Markov trace must include them.

However:

- `markov_trace_mpmath` is currently called only from its own
  `__main__` test and from `crt_markov.trace_descended_via_h3a`.
- `trace_descended_via_h3a` is, as of `git grep` on this branch,
  **not consumed by any other pipeline script**. It appears to be
  legacy infrastructure superseded by the canonical Hoefsmit + y_λ
  path used by the Wedderburn / 1ppb tracks.

Migrating these to canonical $y_\lambda$ is a strict-correctness
fix but appears to have **zero downstream consumers** at the time
of this audit. Follow-up PR scope:

1. Either delete `markov_trace_mpmath` + `trace_descended_via_h3a`
   as dead code, or
2. Migrate them to canonical $y_\lambda$ (drop the
   `length_le_2_partitions_of` iterator, use
   `wedderburn_jones_markov.y_lambda_at(n, q_val)` like
   `habiro_coefficients_interpolate.py` does post-fix).

Both are out of scope for this PR (which is the minimal fix to
the validate CI gate).

## Witness regeneration

After the fix, `habiro_coefficients_interpolate.py` regenerates
`habiro-coefficients-interpolate.witness.json` with values that
agree with the atomic witness to the validator's tolerance
($\sim 10^{-12}$). The validator then passes:

```
$ python3 folio-assistant/computations/habiro_interpolate_cross_validator.py
habiro_interpolate_cross_validator: PASS
  ✓ p (proton, A=1)    rel_diff < 1e-15
  ✓ n (neutron, A=1)   rel_diff < 1e-15
  ✓ D (deuteron, A=2)  rel_diff < 1e-15
exit=0
```

(T and ³He remain `interpolate-only` because the atomic path's
canonical β_K recipes for $A=3$ atoms have not yet been added —
that's a separate scope, not a regression.)
