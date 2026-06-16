> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# P2.5 Tier B kickoff — `witness_polynomial` helper + first migration

**Pair**:
[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md) §P2.5
**Branch**: `claude/audit-math-framework-FXlp2`

## Headline

🟢 Helper module landed; first exemplar migrated; pattern documented.

## Files

- [`computations/witness_polynomial.py`](../../computations/witness_polynomial.py)
  — small helper with two API entries:
  - `expose_polynomial(expr, q, q0=None, digits=50, simplify=True) -> dict`
  - `expose_polynomial_dict(exprs, q, ...) -> dict`
  Both produce a `{polynomial_q, polynomial_q_latex, value_at_q0}` triple.
- [`computations/bw_wenzl_shadow_equivalence.py`](../../computations/bw_wenzl_shadow_equivalence.py)
  — first exemplar; witness JSON now includes a `polynomial_forms`
  field with seven entries (each $w_\lambda$, $\beta_\lambda$,
  $C_\lambda$, $y_\lambda$ for $\lambda = (2,2)$ and $(3,2,1)$).

## Refined scope (post-survey)

The original P2.5 estimate was 110 scripts. Re-survey shows:

- **81 scripts** (not 110) actually have both `sp.Symbol` and a
  witness-JSON output — the precise Tier B target set.
- **0 of 81** currently expose any polynomial form.

## Migration pattern (3-line refactor per script)

```python
# before
witness = {..., "value": str(sp.N(expr.subs(q, q_0)))}

# after
from witness_polynomial import expose_polynomial
witness = {..., "polynomial_forms": expose_polynomial(expr, q, q0=q_0)}
```

For scripts emitting many expressions, use `expose_polynomial_dict`
to batch them.

## Recommended ordering for the remaining 80

Migrate in priority order:

1. **High-value (mass / BW / LP / 1/α):** `shadow_price_c_321_q0.py`,
   `paper_six_term_shadow_price_sweep.py`,
   `alpha_em_q9_q10_derivation.py`,
   `chi_std_pernucleon_derivation.py`,
   `chi_sym_alt_closed_form.py`,
   `atom_per_generator_volumes_sym.py`,
   `atom_mass_exact.py`,
   `atomic_tr_m_mpfr_50dps.py`,
   `binding_per_block_log.py`.
   ~10 scripts, 1 day total.
2. **Medium-value (witnesses cited in audits):** the rest of the 81.
   ~70 scripts, 2–3 days.

Each migration is mechanical (1 import + 1 line of dict construction)
and can be batched with a small Python rewriter if needed.

## Status

🟢 Helper landed and tested.
🟢 First exemplar (`bw_wenzl_shadow_equivalence.py`) migrated and
   re-run; witness JSON now exposes seven polynomial forms with
   their LaTeX rendering and 50-digit numerical evaluation.
🟡 Remaining 80 scripts queued; per-script migration is bounded
   and doesn't touch any mathematical content.

## Adjacent finding from P2.1a

The witness for `tower_mass_symbolic_eval` at H_3 weights produced
catastrophically divergent Φ_q values
([2026-05-01-p2-1a-tower-vs-descended.witness.json](2026-05-01-p2-1a-tower-vs-descended.witness.json)).
Per user input ("probably H_3 weights are wrong at H_{3A}"),
**P2.2 is now elevated**: it's a structural-mismatch fix to restore
convergence, not just an accuracy improvement. The Tier B
refactor doesn't change this — but the eventual P2.2 corrected
weights should also flow through `expose_polynomial` so the audit
trail captures the symbolic form.
