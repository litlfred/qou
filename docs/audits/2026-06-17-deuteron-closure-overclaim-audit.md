# Deuteron-closure over-claim audit (2026-06-17)

**Branch:** `claude/deuteron-closure-overclaim-audit-2026-06-17`
**Scope:** critical-distance / formalize-first corpus verification of
the Option-E deuteron Δ_λ "closure" claims in the Lean corpus, following
the 2026-06-16 Option-E deuteron correction (per-λ weighted sum
undershoots the deuteron binding by ≈ −82.9 %; it does **not** close).

This is a Lean-comment-only audit (no theorem statements changed, no
build impact). Three stale over-claims were found and corrected; one
residual blocker is recorded.

## Findings

### 1. `QOU/OptionE/DeltaLambda.lean` — docstring closure over-claim (FIXED)

The module docstring stated:

> The substantive content of Option E is the **specific choice** of
> `weight_k` and `value` such that the resulting Δ_λ closes the AME
> binding energies.

This presents closure as **achieved**. It is not: the canonical Option E
weights undershoot the deuteron by ≈ −82.9 %. Corrected to state that
closure is an **open target**, that the file provides the framework
signature only, and that `DeuteronVerification.lean` carries the
`closes_within_10pct` predicate as a *hypothesis* (no proved closure
instance).

### 2. `QOU/HadronicMass.lean` — Row 3/4 mass-deficit circularity (FIXED, docstrings)

`binding_energy_QOU : ℝ := 2.224` was docstring-labeled "QOU-predicted
binding energy from the Skein polynomial". In fact `2.224` is the
**experimental** mass deficit `(m_p + m_n) − m_D = 2.22456637 MeV`
rounded to 4 significant figures.

Consequences (the theorems are *true* but are consistency identities,
not predictions):

- `deuteron_topological := proton_topological + neutron_topological −
  binding_energy_QOU`.
- `row3_deuteron_matches_CODATA : |deuteron_topological −
  deuteron_mass_MeV| < 1e-3` reduces to `m_p + m_n − B_exp ≈ m_D` — true
  because `B_exp` *is* `(m_p + m_n) − m_D` to 4 sig figs. Tautological
  mass-deficit identity.
- `row4_binding_from_skein : (m_p + m_n) − deuteron_topological =
  binding_energy_QOU` is proved by `ring`; it holds for **any** anchor
  value because `deuteron_topological` is *defined* with that anchor. It
  computes nothing from the Skein polynomial. Its docstring claimed "the
  deuteron binding energy is computed as the Skein polynomial variation".

Fixed the three docstrings (`binding_energy_QOU`, the Row-3 def, the
Row-4 theorem) to state plainly that the binding term is the
experimental deficit anchor, that the consuming theorems are consistency
identities, and that a genuine topological prediction of the deuteron
binding remains open (Option E undershoots ≈ −82.9 %). Theorem
statements were left intact (they are correct as identities).

### 3. `computations/probes/option_e_deuteron_delta_lambda_probe.py` — stale paths + schema drift (FIXED, re-run)

- **Stale paths (fixed):** the probe loaded its χ^λ witness and wrote its
  output under `folio-assistant/computations/...`, paths that broke in the
  2026-06-02 cluster reorg (computations moved out of `folio-assistant/`).
  Repointed both to `computations/...`.
- **Schema drift (fixed):** the current
  `chi-deuteron-h6-at-q0-50dps.witness.json` `by_partition` entries carry
  only `{partition, chi_lambda}` (slimmed in the native-Rust χ^λ
  refactor); the probe expected `{partition, dim, y_lambda, chi_lambda,
  contribution}`. Rather than invent the missing fields, the probe now
  joins `y_λ(q_0)` from the **canonical cache**
  `y-lambda-at-q0.witness.json` (producer `y_lambda_at_q0_cache.py`),
  computes the rep dimension `dim` via the standard **hook-length
  formula**, and forms `contribution = y_λ · χ^λ`. No audited number is
  fabricated — every input traces to canonical infra.

**Re-run (2026-06-17):** the probe is now runnable end-to-end and
**re-confirms non-closure**. None of the 7 candidate Δ_λ rules closes the
deuteron AME binding within 10 %:

| rule | rel. error |
|------|-----------:|
| `largest_minus_one` (best) | 65.6 % |
| `n_minus_length_over_n` | 93.6 % |
| `uniform_minus_one` | 91.1 % |
| `depth_inverse_length` | 94.4 % |
| `dim_inverse` | 96.6 % |
| `depth_inverse_largest` | 98.1 % |
| `sign_alternating` | 105.7 % |

These ad-hoc probe rules are even further from closure than the canonical
Option E weights (≈ −82.9 % undershoot); the conclusion is the same in
both: **the deuteron binding does not close from these Δ_λ choices.** The
residual blocker noted earlier is resolved — the closure retest is once
again reproducible.

## Net

The Lean corpus no longer presents the deuteron binding as a
topology-derived prediction where the underlying computation is either
absent (hardcoded experimental anchor) or undershoots by ≈ −82.9 %.
Closure is now consistently labeled an open target across
`DeltaLambda.lean`, `HadronicMass.lean`, and the probe docstring.

Residual: refresh `chi-deuteron-h6-at-q0-50dps.witness.json` to the
schema the probe consumes (or adapt the probe), then re-run the closure
retest.
