# P2.5 — Symbolic-in-q migration plan

**Workplan task**: P2.5 (paper-wide refactor: every sympy-capable
script emits both a `polynomial_q` symbolic form and a numerical
evaluation at $q_0$).
**Branch**: `claude/tier3-math-audit-B0wyO`.
**Helper**:
[`computations/witness_polynomial.py`](../../computations/witness_polynomial.py)
(cherry-picked from parent's `ab064d7d1`).

## Survey

A walk over `computations/*.py` for sympy-using
scripts classifies them by ease of `expose_polynomial` adoption:

| Category | Count | Definition |
|----------|------:|------------|
| **Already migrated** | 4 | Already emits `polynomial_q` field |
| **Trivial** | 51 | Writes a witness JSON and constructs `sp.Symbol("q")` — drop-in `expose_polynomial(expr, q)` call |
| **Moderate** | 37 | Writes a witness JSON but builds the symbolic expression indirectly (no top-level `q` symbol) — needs introducing the symbol + tracing the symbolic path |
| **Complex** | 33 | No witness JSON output, or builds symbolic expressions with non-trivial control flow (multiple q's, parameter sweeps) — needs per-script design |

Total sympy-capable: **125 scripts**.

## Recommended phasing

### Tier A (already migrated — no-op)

`bw_wenzl_shadow_equivalence.py`, `chi_std_pernucleon_derivation.py`,
`schur_weyl_low_a_witness.py`, plus the helper
`witness_polynomial.py` itself.

### Tier B (trivial — 51 scripts, codemod-able)

For each script:

```python
import sympy as sp
from witness_polynomial import expose_polynomial
q = sp.Symbol("q", positive=True, real=True)
# ... existing symbolic computation produces `expr` ...
witness["my_quantity"] = expose_polynomial(expr, q)
```

This phase is mechanical and safe. A small codemod
(`pipeline/codemod-witness-polynomial.ts` — not yet written, planned
in this doc) can apply the pattern across all 51 with one PR.

### Tier C (moderate — 37 scripts)

Each script needs:

1. Trace where the symbolic value originates (sometimes inside a
   helper module).
2. Hoist a top-level `q` Symbol and refactor calls to pass it
   through.
3. Add the `expose_polynomial` call at the witness-emit site.

Estimated 0.5–1 day per script; ~3 weeks total. Best done in
batches by chapter / topic (mass-derivation scripts, BW scripts,
alpha-derivation scripts, etc.).

### Tier D (complex — 33 scripts)

Per-script analysis:

- Some scripts may be terminal endpoints with no consumers — drop
  rather than migrate.
- Some are diagnostic / scan scripts that don't need a stable
  witness output — document `does_not_emit_witness: true` or
  `polynomial_q_not_applicable: true`.
- Some build a symbolic expression that should be split into two
  scripts: the symbolic step (emits polynomial_q) and the numeric
  evaluation step (consumes polynomial_q). Refactor into pairs.

This phase is research-grade and depends on the per-script
intent. Defer to a focused follow-up branch.

## Mapping to deep audit §3·E

The deep audit's
[§3·E "Symbolic-in-$q$ throughout"](2026-05-01-math-framework-deep-audit.md)
calls out that scripts substitute $q_0$ early, producing 50-digit
floats that "read as fitted". The migration targets that flag
directly:

- **Tier A + B done** → 55 scripts of 125 (44%) emit symbolic +
  numerical. Substantial coverage of the BW / alpha / Wenzl-bridge
  pipeline.
- **Tier C done** → 92 scripts of 125 (73%). Most of the mass-
  derivation pipeline migrated.
- **Tier D done** → 100% (≤ exclusion list).

Per audit: 100% migration is required for the §6 scorecard item 8
to flip from ❌ to ✅.

## Recommendation for follow-up

1. **Phase 1 (this branch or near successor)**: pick 5-10 high-
   visibility scripts from Tier B (e.g., the alpha-derivation
   chain: `alpha_k_via_wenzl_bridge.py`, `alpha_derivation_probe.py`,
   `chi_std_pernucleon_derivation.py` — already done) and migrate
   them as exemplars. Establish that the `expose_polynomial`
   pattern works end-to-end against the build / validation
   pipeline.

2. **Phase 2 (separate codemod branch)**: write
   `pipeline/codemod-witness-polynomial.ts` that detects the
   "trivial" pattern (sympy-capable + `sp.Symbol('q')` + writes
   witness JSON) and applies the `expose_polynomial` call
   automatically. Run codemod across the 51 Tier B scripts in a
   single PR; review for false positives.

3. **Phase 3 (per-chapter)**: walk Tier C scripts in batches of
   ~10 by chapter. Each batch is a separate PR for review.

4. **Phase 4 (Tier D)**: per-script triage. Some will become
   `polynomial_q_not_applicable`; others will be split into
   symbolic / numerical pairs.

## Output

This audit doc. The actual migration is queued for
follow-up branches; this doc is the inventory.

## Status

🟡 **Scoped, not implemented.** P2.5 touches 121 scripts paper-wide
and is best done as a focused codemod + per-chapter batch
migration, not as part of the math-framework audit pass. The
helper (`witness_polynomial.py`) is in place; two exemplars
(`bw_wenzl_shadow_equivalence.py`, `chi_std_pernucleon_derivation.py`)
demonstrate the pattern.
