# Proposal — subdirectory refactor of `computations/`

**Status:** ACCEPTED 2026-06-02 (see "Owner decisions" at bottom).
**Branch:** `claude/computations-subdirectory-refactor-2026-06-02`
**Sibling context:** Task 3 of the [PR #1674 follow-up backlog](https://github.com/litlfred/qou/pull/1674#issuecomment-4596887754).

## Problem

`computations/` ships **794 `.py` files at a single
flat level** (post the 2026-05-30 purge; was 901 before). Browsing
the directory in a file picker or `ls` is unworkable; the audit
docs / handover notes (`AUDIT-*.md`, `DERIVATION-*.md`,
`HANDOVER-STATUS.md`) sit alongside script source; the
`_deprecated/` peer holds another ~875 artifacts.

Even after the curated purge, discoverability is genuinely bad:

| Sub-cluster | Count | Self-labelled |
|---|---:|---|
| `_probe.py` | 99 | yes |
| `_audit.py` | 27 | yes |
| `_sweep.py` | 7 | yes |
| `phase*.py` | 16 | yes (phase-5 research) |
| `habiro_*.py` | 25 | yes (Habiro element series) |
| `markov_*.py` | 14 | yes (Markov-trace pipeline) |
| `hecke_*.py` | 16 | yes (Hecke + symbolic) |
| `qbeta_*.py` | 21 | yes (Q_β / α_EM derivations) |
| `alpha_*.py` | 22 | yes (α_EM / α-cluster) |
| `A_operator_*.py` | 6 | yes (A-operator extracts) |
| **labelled** | **253** | |
| `(other)` — canonical compute, witness scripts, infra | ~541 | no |

## Why this is high-risk

Three constraints make a naïve `git mv` dangerous:

1. **Flat-namespace cross-imports.** Scripts cross-reference each
   other as top-level modules:
   ```python
   from A_operator_extract_general import ...
   from hecke_characters import build_seminormal_matrices
   from q_parameter import Q as Q0
   from witness_base import WitnessBuilder
   ```
   Moving any file into a subdirectory breaks every importer unless
   we either (a) preserve the flat namespace via `sys.path`
   manipulation, or (b) rewrite every `from X import Y` site.

2. **CI workflows hardcode script paths** —
   `.github/workflows/witness-pipeline.yml` has 15+ explicit
   `computations/<script>.py` references in its
   `paths:` filter and per-step `run:` lines.

3. **287 distinct scripts are referenced from `content/`** — content
   blocks cite a `.py` path in `computation:` / `witness:` / `:val[…]`
   fields. Any rename breaks those refs and the PDF build.

Per the diagnostic in PR #1674, **a wholesale flat-to-tree move is
session-scale and breaks the paper build the moment any path is
wrong**. This proposal is the safe ramp.

## Proposed scheme

```
computations/
  __init__.py                    # makes the dir a package
  _path_bridge.py                # adds parent dir to sys.path on import
                                 #   (preserves `from X import Y`
                                 #    flat-namespace for all subdirs)
  README.md                       # unchanged
  AUDIT-*.md, DERIVATION-*.md     # unchanged (audit docs stay at root)

  # ── infra: substrate + witness emitters (stay flat for now) ──
  q_parameter.py
  witness_base.py
  witness_constant_staleness.py
  _precision.py
  experimental_constants.py
  codata_constants.py
  knot_volumes.py
  hecke_core.py
  hecke_core_legacy.py
  hecke_core_symbolic.py
  # (~30 modules — the substrate / canonical layer; high incoming
  #  fan-in from probes + sweeps; deferred to a later commit)

  # ── new subdirectories (mechanical moves, batched per cluster) ──
  probes/__init__.py
    A_operator_per_interface_probe.py
    additive_composition_categorical_probe.py
    adjacent_vs_full_probe.py
    ...                          # 99 _probe.py files

  audits/__init__.py
    e0_calibration_audit.py
    brundan_kleshchev_audit.py
    cross_check_trM_1ppb.py
    ...                          # 27 _audit.py files + audit-style probes

  sweeps/__init__.py
    paper_six_term_isotope_sweep.py
    canonical_mass_table_extended.py
    ...                          # 7 _sweep.py + canonical sweeps

  phase5/__init__.py
    phase3_*.py, phase5*.py     # 16 phase-research scripts

  habiro/__init__.py
    habiro_*.py                  # 25 habiro-element files

  markov/__init__.py
    markov_*.py                  # 14 markov-trace pipeline files

  hecke/__init__.py
    hecke_symbolic.py
    hecke_division.py
    hecke_*.py                   # 16 hecke-extension files
    (NOT hecke_core.py — stays in root, it's substrate)

  qbeta/__init__.py
    qbeta_*.py                   # 21 Q_β / α_EM derivations

  alpha/__init__.py
    alpha_*.py                   # 22 α_EM / α-cluster files
```

After this carve-out:
- **794 → ~280 files at the root** (mostly substrate + uncategorised)
- 8 new subdirectories, each ~10–100 files
- Audit / handover .md files stay at root (they navigate the whole tree)

## Implementation — phased rollout

Each phase is a **separate commit** on this branch + a CI green-light
checkpoint. **No phase moves more than its own cluster.** Each phase
follows the same recipe:

1. Move the cluster's files into the new subdir (`git mv`).
2. Add `__init__.py` to the new subdir (re-exports nothing —
   modules stay importable by bare name via the path bridge).
3. Drop a `_path_bridge.py` into `computations/` (one-time, in
   Phase 0) that inserts `computations/` into
   `sys.path` if it isn't already, so flat-namespace
   `from X import Y` continues to work from any subdir.
4. Add `from . import _path_bridge  # noqa: F401` as the FIRST
   import in every moved script. This survives `python3
   path/to/script.py` invocation (the workflow's actual pattern)
   AND `python3 -m folio-assistant.computations.probes.X`.
5. Update CI workflow paths in
   `.github/workflows/witness-pipeline.yml`,
   `.github/workflows/publish.yml`, `.github/workflows/blueprint.yml`.
   The `paths:` filter is glob-friendly:
   `computations/**/*.py` covers all sub-dirs.
6. Update `content/` references via a single codemod script (see
   `scripts/migrate-computation-paths.ts` — to be added in Phase 0).
7. Re-run `bun run validate quantum-observable-universe/` and the
   witness-pipeline smoke locally before push.

### Phase 0 — path bridge + `__init__.py` (NO file moves)

Lay the substrate that makes subsequent moves zero-risk:

- Add `computations/__init__.py` (empty).
- Add `computations/_path_bridge.py`:
  ```python
  """Ensures `computations/` is on sys.path,
  preserving flat-namespace imports after the subdirectory
  refactor (see docs/proposals/computations-subdirectory-refactor.md)."""
  import sys
  from pathlib import Path
  here = Path(__file__).resolve().parent
  if str(here) not in sys.path:
      sys.path.insert(0, str(here))
  ```
- Add `scripts/migrate-computation-paths.ts` (the path-rewriter).
- **No moves yet** — verify CI is still green.

### Phase 1 — `probes/` (99 files)

The lowest-risk cluster:
- Self-labelled with `_probe.py` suffix.
- Reviewer can visually verify scope at a glance.
- Most probes are not cited from content blocks (per the
  audit-wiring report, most are wired only via their `*.witness.json`).

### Phase 2 — `audits/` + `sweeps/` (34 files)

Same rationale; small batch.

### Phase 3 — `phase5/` (16 files)

The phase-5 research cluster — most likely to be transient /
deprecated soon. Carving them out makes their lifecycle explicit.

### Phase 4 — `habiro/` + `markov/` + `hecke/` (55 files)

Domain clusters. These have MORE cross-references and MORE content-
block citations, so the migration script + CI must be exercised
heavily here.

### Phase 5 — `qbeta/` + `alpha/` + `A_operator/` (49 files)

Final domain clusters.

### Phase 6 — root cleanup

After Phases 1-5, the root has ~540 → ~280 files. The remaining
gradient between "substrate" and "everything else" is harder to
draw cleanly; Phase 6 is intentionally TBD pending review of what
the root-level inventory looks like by then.

## What this proposal explicitly does NOT do

- **Does not rename any file.** Only relocates. Imports continue to
  work via the path bridge.
- **Does not touch `_deprecated/`.** That is its own
  archive-directory cleanup, tracked separately.
- **Does not consolidate "optimized vs non-optimized" siblings**
  (e.g. `hecke_core.py` numerical + `hecke_core_symbolic.py` symbolic
  + `hecke_symbolic.py` extended symbolic). Per
  `.claude/skills/local/compute-author.md` these are deliberate
  precision-tier splits and must NOT be merged.
- **Does not move the substrate cluster** (`q_parameter`,
  `witness_base`, `_precision`, `experimental_constants`,
  `codata_constants`, `hecke_core`, `hecke_core_legacy`,
  `hecke_core_symbolic`, `knot_volumes`, …). Those carry the highest
  fan-in (~70% of the 794 scripts depend on at least one) and live
  cleanly at the root.

## Cost / blast-radius estimate

| Phase | Files moved | Content-block refs touched | CI workflow paths touched | Risk |
|---|---:|---:|---:|---|
| 0 (bridge) | 0 | 0 | 0 | none |
| 1 (`probes/`) | 99 | ~30 | 0 (glob) | low |
| 2 (`audits/`, `sweeps/`) | 34 | ~15 | ~5 | low |
| 3 (`phase5/`) | 16 | ~5 | 0 | low |
| 4 (`habiro/`, `markov/`, `hecke/`) | 55 | ~80 | ~10 | medium |
| 5 (`qbeta/`, `alpha/`, `A_operator/`) | 49 | ~30 | ~5 | medium |
| 6 (substrate cleanup) | TBD | TBD | TBD | high — review |
| **Total** | **~253 / 794** | **~160 / 287** | **~20** | mixed |

Estimated effort: **6 commits, 6 CI checkpoints, 1–2 review cycles**.
Comfortably within a single working tranche if PR doesn't churn.

## Open questions for the owner

1. **Path-bridge mechanism — top-of-script vs `__init__.py`?**
   Top-of-script `from . import _path_bridge` is the most defensive
   (works whether the script is run as `python path/X.py` or
   `python -m computations.probes.X`). Slightly noisy. Alternative:
   make the `__init__.py` of each subdir do the bridge insertion;
   relies on Python implicitly executing `__init__.py` for top-level
   script runs, which it does NOT do by default. Recommend the
   top-of-script line.

2. **`content/` reference migration — codemod vs hand-edit?**
   The 287 references are mechanical
   (`computations/X.py` → `computations/probes/X.py`).
   A TypeScript codemod with the move table is < 50 LOC.
   Recommended.

3. **Naming convention for cluster directories**.
   Proposed: short lowercase nouns matching the script-prefix
   (`probes`, `audits`, `sweeps`, `phase5`, `habiro`, `markov`,
   `hecke`, `qbeta`, `alpha`). Open: `A_operator/` or `a_operator/`
   or `aop/`? Recommend `a_operator/` for consistency.

4. **Should the substrate cluster also move (Phase 6)?**
   E.g. `substrate/` containing `q_parameter`, `witness_base`,
   `_precision`. **Caution:** these are imported by ~70 % of all
   compute. Moving them is the biggest single-cluster blast radius
   in the whole refactor. Recommend deferring to a separate PR.

5. **Should we co-move `*.witness.json` next to their producer scripts?**
   E.g. `probes/A_operator_per_interface_probe.py` +
   `probes/A_operator_per_interface_probe.witness.json` side by
   side. **Pro:** keeps the producer + sidecar coherent. **Con:**
   doubles the move count and complicates the audit-wiring scan,
   which currently globs `computations/*.witness.json`.
   Recommend deferring — script moves first, witness moves only if
   the audit script gets a corresponding glob upgrade.

## Owner decisions (2026-06-02)

| # | Question | Decision |
|---|---|---|
| 1 | Path-bridge mechanism | **Top-of-script `from . import _path_bridge`** (recommended default accepted) |
| 2 | content/ ref migration | **Codemod** (recommended default accepted) |
| 3 | Naming for `A_operator_*` | **`a_operator/`** lowercase |
| 4 | Substrate cluster | **Move now** (overrides "defer to separate PR") — `substrate/` becomes Phase 6, included in this branch |
| 5 | `*.witness.json` co-move | **Move now** (overrides "defer") — witnesses move with their producers; `audit-wiring.ts` + the witness-pipeline.yml path filters get upgraded to `**/*.witness.json` glob |

### Implications of (4) — substrate cluster in-scope

Phase 6 is now a real phase in this branch (was TBD-deferred).
Scope: `q_parameter`, `witness_base`, `witness_constant_staleness`,
`_precision`, `experimental_constants`, `codata_constants`,
`hecke_core`, `hecke_core_legacy`, `hecke_core_symbolic`,
`knot_volumes`, `lr_coefficients`, `char_fast`, `hecke_characters` —
~25 modules. ~70 % of compute scripts import at least one.

The path bridge from Phase 0 is what makes this tractable: scripts
keep doing `from q_parameter import Q` regardless of where
`q_parameter.py` physically lives, because `substrate/` ends up on
sys.path via the bridge. CI gate at the end of Phase 6 will catch
any script that imports a substrate module that wasn't covered by
the move table.

### Implications of (5) — witness JSON co-move

Each phase now moves both `<cluster>/<X>.py` AND
`<cluster>/<X>.witness.json` (+ `<X>.derivation.json` where
present). This roughly doubles the per-phase file count but is
mechanical via the codemod (the move-table maps script path →
new path; the same maps with `.py` → `.witness.json` are added).

**Required upgrades** (additional Phase 0 tasks):

- `scripts/audit-wiring.ts` — change `glob("computations/*.witness.json")` to recursive `glob("computations/**/*.witness.json")`.
- `.github/workflows/witness-pipeline.yml` — change `paths:` patterns from `computations/*.witness.json` to `computations/**/*.witness.json` (same for `*.derivation.json`).
- Any other tool that scans witnesses (run-pipeline.py, etc.) gets a corresponding `**` upgrade.

## Next step

Phase 0 lands now: path bridge + `__init__.py` + codemod scaffold +
`audit-wiring.ts` glob upgrade + workflow path-filter upgrades.
**0 file moves**, green CI. Then Phase 1 (`probes/`) follows.
