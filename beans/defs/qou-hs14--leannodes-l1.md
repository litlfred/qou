---
# qou-hs14
title: '[LEANNODES L1] Probe R1/R2'
status: completed
type: feature
priority: normal
tags:
    - migration
    - leannodes
    - needs-owner
created_at: 2026-10-04T16:35:47Z
updated_at: 2026-10-05T15:21:17Z
parent: qou-ahxm
---

From the LEANNODES migration analysis (2026-10-04), story L1. Full report: docs/audits/2026-10-04-workplan-and-migration/LEANNODES_report.md.

| L1 | Probe R1/R2 | One dispatch builds one chapter's glob; result recorded; fallback chosen if Lake rejects | S | L0, owner dispatch |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


2026-10-05 — PROBED with the real toolchain (Lean/Lake v4.24.0 from the GitHub release, matching lean-toolchain), using scripts/lean-blocks-lake-probe.sh (new, reproducible; it builds a throwaway package with no Mathlib and touches nothing in the repo).
- R1 kebab-case globs: FAIL. Lake's TOML parser rejects "braids-and-knots.+" with 'expected glob' at the globs line. The guillemet-quoted form «braids-and-knots».+ is rejected the same way.
- R2 srcDir outside the package (srcDir = ".."): PASS, with identifier-safe module names. A sibling importing a QOU library module (QOU.Base) builds.
- FALLBACK CHOSEN: a generated shadow tree of identifier-safe symlinks (e.g. blocks-shadow/MassTheory/RhoKH3aRefinement.lean -> ../../../mass-theory/rho-k-h3a-refinement.lean), with the QOUBlocks lib at srcDir = "blocks-shadow", globs one per chapter. It builds, and an edit to the real file rebuilds through the link. Source files are NOT renamed, as the report requires: no-orphan-lean's matching stems keep working, and lean.ref is unaffected because declaration names come from in-file namespaces.
- Deviation from done-when: no CI dispatch of a real chapter. The question was Lake config acceptance, and the real toolchain answers it on toy modules without owner dispatch or Actions spend. Building a real chapter's siblings belongs to L2/L3, whose builds need the Mathlib cache.
- Content parity: no content, Lean, witness or lakefile change; adds one script.
Implication for L2: generate the shadow tree (and the per-chapter globs) from the paper manifest, with a check that the generated set equals the manifest's chapters.
