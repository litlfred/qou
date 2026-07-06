# P2.5 audit — symbolic-in-q scope 2026-05-02

**Pair**: [`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§3·E + [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
P2.5.

**Branch**: `claude/tier-4-math-audit-EkI7a`

## Sweep result (610 Python scripts)

[`computations/audits/p2_5_symbolic_q_audit.py`](../../computations/audits/p2_5_symbolic_q_audit.py)
triages every Python file under `computations/`.

| Category | Count | Share | Notes |
|:---------|------:|------:|:------|
| **mpmath-only** | 170 | 28% | Uses canonical `Q_MP` precision; no separate fit. **Functionally compliant.** |
| `uncategorised` | 307 | 50% | Mostly scripted utilities, AME data loaders, module imports without clear q-handling pattern. Out of scope. |
| **compliant** | 40 | 7% | Uses `sympy.Symbol('q')` and substitutes $q_0$ only at final reporting. **Reference pattern.** |
| **early-substitution** | 41 | 7% | Substitutes a float $q_0$ near the top, computes numerically afterwards. **Real refactor target.** |
| `partial` | 19 | 3% | Already uses symbolic q but doesn't emit a polynomial field in witness JSON. **Easy wins.** |
| `no-q-dependence` | 33 | 5% | Doesn't reference q. Out of scope. |

**Real refactor scope: 41 early-substitution + 19 partial = 60 scripts (~10% of the pool).**

The workplan's "1 week paper-wide" estimate was based on the
naïve 449-script count of all witness emitters, including the
~210 already functionally compliant (40 compliant + 170 mpmath-
only). The actual scope is **~60 scripts at ~10 minutes per
mechanical refactor = ~10 hours = 1.5 days**.

## Reference pattern (already in 40 scripts)

Cleanest example:
[`schur_weyl_mn_witness.py`](../../computations/schur_weyl_mn_witness.py).
The pattern is:

```python
import sympy as sp
from q_parameter import Q as _Q_CANONICAL

def witness_atom(...):
    q = sp.Symbol('q', positive=True, real=True)
    q0 = sp.Rational(int(_Q_CANONICAL * 10**16), 10**16)

    # ... computation in symbolic q ...
    total = global_wedderburn_sum_symbolic(A, q, ...)

    # Substitute at the END
    total_at_q0 = float(total.subs(q, q0).evalf(30))

    return {
        # Both fields in the witness JSON:
        "total_symbolic": str(sp.simplify(total)),
        "total_at_q0":    total_at_q0,
        # ...
    }
```

The two key invariants:

1. `q = sp.Symbol('q')` declared at function start; all
   intermediate computations are sympy expressions.
2. Witness JSON emits **both** the symbolic form (`*_symbolic`
   field) and the numerical value (`*_at_q0` field).

## Top 20 refactor targets (early-substitution, by witness visibility)

| Lines | Path |
|------:|:-----|
| 487 | [`garside-irrep-qvalues.py`](../../computations/garside-irrep-qvalues.py) |
| 468 | [`gram-matrix-dual.py`](../../computations/gram-matrix-dual.py) |
| 364 | [`probe_proton_mass_scale.py`](../../computations/probe_proton_mass_scale.py) |
| 358 | [`hecke_engine.py`](../../computations/hecke/hecke_engine.py) |
| 343 | [`electron-proton-skein-weight.py`](../../computations/electron-proton-skein-weight.py) |
| 327 | [`beta-decay-matrix.py`](../../computations/beta-decay-matrix.py) |
| 319 | [`t35-generator-volumes.py`](../../computations/t35-generator-volumes.py) |
| 300 | [`jet_tower_proton_explore.py`](../../computations/jet_tower_proton_explore.py) |
| 294 | [`level1_vhat_brane_tower.py`](../../computations/level1_vhat_brane_tower.py) |
| 288 | [`knot-operator-table.py`](../../computations/knot-operator-table.py) |
| 286 | [`hbar_vs_q_parametrization.py`](../../computations/hbar_vs_q_parametrization.py) |
| 270 | [`markov_convention_parallel.py`](../../computations/markov_convention_parallel.py) |
| 269 | [`mass_table_best.py`](../../computations/mass_table_best.py) |
| 264 | [`jet_level1_and_residual_search.py`](../../computations/jet_level1_and_residual_search.py) |
| 260 | [`p_n_error_isolate.py`](../../computations/p_n_error_isolate.py) |
| 252 | [`jet_level_geometric_series.py`](../../computations/jet_level_geometric_series.py) |
| 247 | [`probe_atom_shell_self_duality.py`](../../computations/probe_atom_shell_self_duality.py) |
| 245 | [`atomic_chirality_residue.py`](../../computations/atomic_chirality_residue.py) |
| 218 | [`explicit_alpha_k_h3.py`](../../computations/explicit_alpha_k_h3.py) |
| 218 | [`probe_per_nucleon_self_duality.py`](../../computations/probe_per_nucleon_self_duality.py) |

Full list of 41 early-substitution scripts in
[`p2-5-symbolic-q-audit.witness.json`](../../computations/p2-5-symbolic-q-audit.witness.json).

## Caveat: not every script can go fully symbolic

Some scripts use **numpy linear algebra** at scale (large block-
diagonal matrices, eigenvalue computations) that sympy doesn't
handle efficiently. For those, the right refactor is to:

- Stay numpy/mpmath-internal, but
- **Emit the algebraic structure** in the witness JSON (e.g., the
  Wedderburn weight $w_\lambda(q)$ as a string Laurent polynomial
  even if the per-irrep matrix computation is numerical), and
- Document explicitly why the script is mpmath-internal (which
  reframes it from "early-substitution" to "mpmath-only" — a
  change of category, not of code).

Roughly half of the 41 early-substitution scripts (those using
numpy block-matrix algebra) likely need this lighter refactor;
the other half can go fully symbolic.

## Heuristic caveat (added after sampling 4 partial scripts, 2026-05-02)

The "partial" classification is based on a regex looking for
`*_polynomial_q` / `*_symbolic` field-name conventions in the
witness JSON. Sampling 4 of the 19 scripts revealed two
patterns the heuristic miscategorises:

- **False positives**: scripts that already emit symbolic forms
  under different field names (e.g.,
  [`schur_element_symmetrising.py`](../../computations/schur_element_symmetrising.py)
  emits `schur_element` strings — fully symbolic, no q-substitution
  needed). **Audit fix would be to broaden the heuristic; no code
  change needed.**
- **Sympy-as-matrix-stepping-stone**: scripts like
  [`std_matrix_trace_closed_form.py`](../../computations/std_matrix_trace_closed_form.py)
  and [`wedderburn_per_isotope.py`](../../computations/wedderburn_per_isotope.py)
  use `sympy.Symbol('q')` to *build* Hoefsmit seminormal matrices
  via `build_seminormal_matrices`, then immediately substitute
  $q_0$ to get numpy arrays for matrix-product trace. The
  algebraic side of these computations IS symbolic (the
  per-irrep matrices); the per-trace output is numerical only
  because sympy doesn't scale for large block-matrix products.
  **These need lighter-touch refactor**: add a metadata note in
  the witness JSON declaring "Hoefsmit matrices symbolic-in-q
  via `build_seminormal_matrices`; per-trace output is numpy
  evaluation at $q_0$".

After sampling, the 19 partial scripts split roughly as:

- ~3–5 fully-symbolic-already (false positives — heuristic
  refinement only).
- ~5–8 add-`polynomial_q`-field straightforward (the
  `full-tower-mass.py` and `probe_term4_conventions.py` pattern).
- ~6–10 sympy-as-matrix-stepping-stone (lighter-touch metadata
  refactor).

## Recommended ordering

1. **First-batch refactors** (1 day): execute the
   add-`polynomial_q`-field pattern on the ~5–8 cleanly-typed
   partial scripts. **Two demonstration commits already in this
   branch**:
   - `95f9d396` — `full-tower-mass.py` (refactored, witness JSON
     gains `symbolic_q_form` with V̂ polynomials per generator).
   - This commit — `probe_term4_conventions.py` (refactored,
     witness JSON gains `sigma_inv_dim_q_polynomial_q` for n=3,
     6, 9, 12).
2. **Heuristic refinement** (0.25 day): broaden the audit's
   `EMITS_SYMBOLIC` regex to recognise field names like
   `*_element`, `*_expression`, `*_form`, etc., reducing false
   positives.
2. **The light-refactor early-substitution scripts** (1 day):
   ~20 scripts where adding `q = sp.Symbol('q')` + late
   substitution is mechanical.
3. **The heavy-refactor early-substitution scripts** (3+ days):
   the numpy / large-matrix cases where the witness JSON gets the
   symbolic structure as a string field while the internal
   computation stays numerical.
4. **Validation** (0.5 day): re-run all updated witnesses, confirm
   `polynomial_q` fields populate, no numerical drift in
   `*_at_q0` fields.

Total realistic scope: **~5 days mechanical work**, not 1 week.

## Reproducibility

```bash
python3 computations/audits/p2_5_symbolic_q_audit.py
# → computations/p2-5-symbolic-q-audit.witness.json
```
