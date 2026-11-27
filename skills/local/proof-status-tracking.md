---
name: proof-status-tracking
roles: [reader, collaborator, owner]
description: >
  Track formalization status, per-block QA sidecars (<block>.qa.json), Lean
  static declaration/sorry/axiom censuses, KG import-DAG & Reservoir library
  readiness, and Python computation witness staleness across folio/.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Proof Status Tracking

## Overview

This skill tracks live formalization and verification status across content object triples (`<block>.ts` + `<block>.md` + `<block>.lean`) and library modules in `folio/quantum-observable-universe/lean/`:

1. **Per-block QA sidecars (`<block>.qa.json`)**: authoritative per-block QA pass/fail/score records (`proof-no-bare-sorries`, `proof-no-axiom-growth`, `proof-lean-compiles`, `proof-narrative-lean-equiv`, `proof-substantive`, `proof-no-self-assuming-projection`, `proof-no-trivial-true`, etc.).
2. **Static declaration & sorry/axiom census (`scripts/lean-static-census.py`)**: fast zero-elaborator inventory across all `.lean` files.
3. **Knowledge-graph & Reservoir `lean_lib` audit (`scripts/lean-kg-detangler.py`)**: import DAG, directory-level SCCs, orphans from `QOU.lean`, §7c ring-generality regimes, and Tier-A (`Mathlib4`) / Tier-B (6 Lean Reservoir `lean_lib` packages) cone purity.
4. **Best-practices & vacuity hygiene (`scripts/lean-best-practices-lint.py`)**: `BP001`–`BP009` checks (`--diff` and `--package`).

> **Architecture note:** Legacy monolithic `proof-objects.json` and `.github/scripts/{extract_proof_objects,generate_lean_stubs,update_proof_status}.py` have been retired. Formalization status is tracked via per-block `<block>.qa.json` sidecars and live deterministic scripts under [`scripts/lean/README.md`](../../scripts/lean/README.md).

## CPU Throttling Rule (Mandatory)

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
```

Prefix all `python3`, `bun`, and `./scripts/lean-*` invocations with `nice -n 15`. Never run bare `lake build` locally (see [`lean-build-hygiene.md`](lean-build-hygiene.md)).

## Lean MCP Tools (`lean-lsp`)

When the MCP server is available, prefer MCP tools for per-file live status:

| Task | MCP tool | CLI / static equivalent |
|------|----------|-------------------------|
| Per-file sorry/error counts | `lean_diagnostic_messages` | `nice -n 15 python3 scripts/lean-static-census.py` |
| Declaration inventory | `lean_file_outline` | `scripts/lib/lean_decl_scan.py` |
| Axiom audit per theorem | `lean_verify` | `LEAN_NUM_THREADS=1 nice -n 15 ./scripts/lean-verify.sh <Decl>` |
| Verify `lean.ref` target type | `lean_hover_info` | `nice -n 15 bun run folio/pipeline/block-manifest-audit.ts` |

## Live Status Commands

| Check | Command |
|-------|---------|
| Corpus declaration, `sorry`, and `axiom` census | `nice -n 15 python3 scripts/lean-static-census.py` |
| Full Lean KG, orphan, §7c ring, & Reservoir `lean_lib` summary (`< 15s`) | `nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only` |
| Changed-file Mathlib4 / Reservoir / vacuity lint | `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` |
| Vacuity & axiom ledger audit | `nice -n 15 bun run folio/pipeline/lean-vacuity-axiom-audit.ts` |
| Per-block `.qa.json` sidecar integrity | `nice -n 15 bun run folio/pipeline/qa-evidence-audit.ts` |
| Orphaned Lean module audit | `nice -n 15 bun run folio/pipeline/lean-orphan-audit.ts` |
| Python computation witness staleness & reproducibility | `nice -n 15 python3 computations/witness_staleness_triage.py` / `nice -n 15 python3 computations/witness_reproducibility_check.py` |

## Content Object Integration

Formalization status is tracked through **content object triples** under `folio/<paper>/<chapter>/`:

- `definition`: `.ts` + `.md` + `.lean` (or `lean.ref` into `folio/<paper>/lean/`) required; label prefix `def:`.
- `theorem` / `lemma` / `proposition` / `corollary`: `.ts` + `.md` + `.lean` expected; label prefixes `thm:` / `lem:` / `prop:` / `cor:`.
- `example` / `remark` / `conjecture`: `.ts` + `.md` required; `.lean` optional (conjectures use `§3b-cond` hypothesis classes when formalized).
- `prose` / `equation` / `diagram` / `algorithm`: `.ts` + `.md` only; no Lean required.

**Do not** store mutable build/review status inside `<block>.ts` manifests or maintain hand-edited static count snapshots inside skill files — run `scripts/lean-static-census.py` and `scripts/lean-kg-detangler.py --summary-only` for live numbers, and store per-block QA evidence in `<block>.qa.json` (`schemas/qou-types.ts`, `schemas/lean-packages.ts`).

## Witness Tracking

Each Python computation script under `computations/` emits a `<name>.witness.json` sibling stamped via `WitnessBuilder` (`qou_substrate.witness` / `witness_base`):
- `commitSha`: Git HEAD at computation time
- `scriptHash`: SHA-256 of the producer script (authoritative staleness check)
- `assertions`: structured high-precision (`mpmath` ≥ 50 dps, zero `float64`) pass/fail checks linked via `contentBlock`

Verify witness health with:
```bash
nice -n 15 python3 computations/witness_staleness_triage.py
nice -n 15 python3 computations/witness_reproducibility_check.py
```

## Checklist

- [ ] `scripts/lean-static-census.py` matches expected zero-uncited-`sorry` / zero-unauthorized-`axiom` invariants
- [ ] `scripts/lean-best-practices-lint.py --diff` passes with zero errors (`BP001`–`BP009`)
- [ ] `folio/pipeline/lean-vacuity-axiom-audit.ts` passes
- [ ] `folio/pipeline/qa-evidence-audit.ts` passes on touched `<block>.qa.json` sidecars
- [ ] Every `lean.ref` URI in touched `.ts` manifests resolves (`schemas/lean-packages.ts`)
- [ ] Touched Python witnesses pass `computations/witness_staleness_triage.py`
