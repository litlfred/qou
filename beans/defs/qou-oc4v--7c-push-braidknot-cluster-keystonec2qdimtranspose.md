---
# qou-oc4v
title: '§7c push: BraidKnot cluster (KeystoneC2QDimTranspose, DepthStratifiedFrobeniusReciprocity, knot_mass_unified, hoefsmit_*, KnotFactor*, QBetaWenzlDecomposition, six_term_mass_formula) to generic R'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:07:46Z
updated_at: 2026-11-17T06:35:30Z
parent: qou-rtxm
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | wall | verdict |
|---|---|---|---|---|---|
| `KeystoneC2QDimTranspose` | 6 | n | n | pass | **CANDIDATE** |
| `DepthStratifiedFrobeniusReciprocity` | 5 | Y | Y | **fail** | **MIXED** — generic + archimedean in one file; review split per §7c |
| `knot_mass_unified` | 0 | Y | Y | pass | **DONE** — `(R : Type*) [AddCommGroup R]`, no code ℝ |
| `QBetaWenzlDecomposition` | 9 | n | n | pass | **CANDIDATE** |

`hoefsmit_*` / `KnotFactor*` / `six_term_mass_formula` from the title were not resolved to single files — enumerate before starting. 1 of the named files is already done.


### RESOLVED: `DepthStratifiedFrobeniusReciprocity` MIXED → split (2026-08-15)

The one **MIXED** entry in the table above is fixed. Split per §7c into an algebraic module + an archimedean sibling:

| module | content | wall-side | compile |
|---|---|---|---|
| `QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean` | all FR-weight algebra, already over `{R : Type*} [Field R]` | **FAIL → PASS**, regimes now `[generic-R,symbolic]` | `ok=1` |
| `QOU/BraidKnot/DepthStratifiedFrobeniusReciprocityVariance.lean` *(new)* | the two empirical decimal variance-record theorems (ordered `ℝ` literals) | PASS | `ok=1` |

**Why a split was right here, when `HeckeAlgebra` was correctly left alone:** blast radius is **zero** — no `.lean` imports this module, and the single `.ts` `lean.ref` (`qou:QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity`, from `mass-theory/depth-stratified-frobenius-reciprocity.ts`) points at the **class**, which stays in the algebraic module, so ref resolution is untouched. The archimedean part was exactly two self-contained `norm_num` theorems over decimal literals with no dependency on the algebra. That is the cleanest possible split, not a 2003-line restructure with many importers.

Verified by compiler **and** by the canonical `wall-side-correct` checker, not by reading.

⚠ **Pre-existing, not introduced:** neither module is reachable from `QOU.lean`, so `lake build QOU` never elaborates either (both are in the 795-module orphan set of `qou-kljb`). The new sibling imports the algebraic module, so the two are linked to each other; wiring them into the umbrella is `qou-kljb`'s scope and was deliberately not attempted here.

## 2026-11-17 — §7c Generic-Ring Braid–Knot Cluster Foundations (`litlfred/qou#8227`)
- Formalized `keystone_c2_transpose_antisym`, `qbeta_wenzl_level_two_decomp`, and `six_term_mass_paired_decomposition` over generic `CommRingOps R` (zero `ℝ` occurrences) in `folio/quantum-observable-universe/lean/QOU/Foundations/Zeta4GenericRingPlancherel.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `6ea0f626b6fd6e4a73ad6fb742931324e3efe377`, PR [https://github.com/litlfred/qou/pull/8227](https://github.com/litlfred/qou/pull/8227)).
- Kept `status: in-progress` per no-unilateral-closure policy.
