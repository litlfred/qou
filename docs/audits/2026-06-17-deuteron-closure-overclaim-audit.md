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

### 3. `computations/probes/option_e_deuteron_delta_lambda_probe.py` — stale path (FIXED) + schema drift (BLOCKER)

- **Path (fixed):** the probe loaded
  `folio-assistant/computations/chi-deuteron-h6-at-q0-50dps.witness.json`,
  a path that broke in the 2026-06-02 cluster reorg (computations moved
  out of `folio-assistant/`). Repointed to `computations/...`.
- **Schema drift (residual blocker):** even with the path fixed, the
  probe crashes with `KeyError: 'dim'`. The current
  `chi-deuteron-h6-at-q0-50dps.witness.json` `by_partition` entries carry
  only `{partition, chi_lambda}`; the probe expects `{partition, dim,
  y_lambda, chi_lambda, contribution}`. The probe was written against an
  older witness format.

Because reconstructing `y_λ` / `dim` / `contribution` to force a re-run
would risk fabricating the very number under audit, the −82.9 % figure
was **not** freshly reproduced this session; it stands as documented in
the 2026-06-16 Option-E deuteron correction. The probe is now
path-correct but remains blocked on the witness schema mismatch — filed
as a follow-up (regenerate the witness with the full schema, or adapt
the probe to compute `y_λ`/`dim` from the partition).

## Net

The Lean corpus no longer presents the deuteron binding as a
topology-derived prediction where the underlying computation is either
absent (hardcoded experimental anchor) or undershoots by ≈ −82.9 %.
Closure is now consistently labeled an open target across
`DeltaLambda.lean`, `HadronicMass.lean`, and the probe docstring.

Residual: refresh `chi-deuteron-h6-at-q0-50dps.witness.json` to the
schema the probe consumes (or adapt the probe), then re-run the closure
retest.
