# I11 AST-dataflow classifier + two-method cross-check

**Date:** 2026-06-16
**Branch:** `claude/i11-ast-dataflow-2026-06-16`
**Context:** The substring I11 audit (`validation_as_input_audit.py`) was
refined 39 → 19 over several PRs (#2374/#2377/#2383). This adds the
**AST-dataflow** approach that was flagged as the "real fix", and reports
what it actually buys.

## What the AST classifier does

`computations/audits/i11_ast_dataflow.py` parses each script and, for every
use of a `_VALIDATION` anchor (and values transitively derived from it),
walks **up** through carrier conversions and arithmetic to the *sink*. A use
is **clean** iff it reaches a comparison (`Compare` / `x − …`), a display
(`nstr`/`print`/f-string), a recording (`add_parameter`/dict value), a
boolean guard, or an assignment to a variable that is itself clean
(recursive, memoised). It is a **violation** iff the derived value is
returned or passed to a compute function — i.e. flows forward as a
prediction.

This correctly handles cases the line-local substring audit cannot, e.g.
`m_obs = Z·m_p + N·m_n − B_AME` (a comparison **reference**, only ever
subtracted) and `delta/M_P_CODATA·1e6` inside `nstr(...)` (ppm display).

## The irreducible limit (the real finding)

The AST classifier is **not strictly better** than the substring one. The
core I11 question — does an anchor-derived value that is *passed to a
generic function or returned* act as a comparison reference or as a
prediction? — is **semantic, not syntactic**. Both look identical in the
AST. So the AST method (21 scripts) and the substring method (19) trade a
different false-positive / false-negative profile; neither is ground truth.

## The value: a two-method cross-check

Run independently, the two methods **agree on 7 scripts** — these are the
**high-confidence genuine I11 candidates** (both an independent line-local
and an independent dataflow analysis flag them). The original 39 → **7 for
human review**:

| High-confidence (both methods) | kind |
|---|---|
| `applied_uniqueness_mass_table.py` | production |
| `binding_K_direct.py` | production |
| `gamma_gamma_pair_production_decomposition.py` | production |
| `mp_dk_decisive_test.py` | production |
| `phase2a2_flavor_split_exact_correction.py` | production |
| `proton_brane_tower_correction_probe.py` | `_probe` (exploratory) |
| `subgoal_1_per_knot_mass_table_probe.py` | `_probe` (exploratory) |

The **12 substring-only** and **14 AST-only** scripts are the
semantic-ambiguity set — each needs a human to decide comparison-ref vs
prediction; do not auto-act on them.

## Disposition

- The AST tool ships as a **standalone second opinion** (`--cross-check`),
  **not** a replacement for the validated substring audit. Swapping the
  default would trade one approximation for another and risk hiding real
  violations.
- **Actionable next step (owner):** review the 5 production high-confidence
  scripts above for a genuine hidden-calibration input (anchor feeding a
  predicted mass), distinct from a comparison reference. The 2 `_probe`
  files are exploratory and lower priority.
- The cross-check is the right standing pattern for I11: confidence comes
  from two independent methods agreeing, not from either heuristic alone.
