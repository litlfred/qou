# Deprecated witnesses and producing scripts

> **Note (2026-06-01):** `hecke_core_legacy.py` was moved out of this
> directory because 9 live importers still depend on its symbols
> (5 in `folio-assistant/computations/` + 4 in `tools/pyhecke/python/
> pyhecke/`). It now sits at `../hecke_core_legacy.py` with a
> `DEPRECATION-CANDIDATE` banner, matching the convention used by the
> 23 other still-live deprecated scripts mentioned below.

This directory holds `*.witness.json` files that are **dead exploratory
probes** from earlier research passes:

- no content block consumes them (`computation.witness` / `:val[…]`
  registry / `witness:` array)
- no audit report under `docs/audits/*.md` cites them
- the witness body itself contains no assertions
  (`falsifiability == "no-assertions"`)

It also holds the **producing `.py` scripts** for those witnesses, when
the script is not imported by any live (non-`_deprecated/`) code.  In a
follow-on pass, 262 of the 285 candidate scripts were moved here
alongside their witnesses; the remaining 23 candidate scripts are
**kept in place** under `folio-assistant/computations/` with a
`# DEPRECATION-CANDIDATE: ...` header comment, because they are still
imported by live code and moving them would break the importer.  Those
23 should be revisited when the live importer is itself retired or
rewired off the deprecated dependency.

A subsequent **"unwrap chains"** pass (this PR) moved the 30 remaining
orphan witnesses from the live area, plus their producer scripts, plus
the transitive closure of producer scripts that became unimported as a
result.  This brought the orphan-witness count to **0** and the live
script count from 522 down to ~225.  Restoration safety net: any wired
or audit-only witness whose `scriptFile` claim was about to be moved
was detected and the producer (and its transitive imports) were kept
in the live area.  Canonical scripts named in
[`../README.md`](../README.md) (`gb_residue_tower.py`,
`habiro_residue_symbolic.py`, `frobenius_partition_sum.py`,
`y_lambda_symbolic_validate.py`, `atom_mass_partition.py`) were also
explicitly preserved.

Reviving an exploration only requires running the producer to re-emit
the witness next to its script.

## Audit-wiring behavior

`scripts/audit-wiring.ts` scans `folio-assistant/computations/*.witness.json`
(glob without `**`), so witnesses in this `_deprecated/` subdirectory
are excluded from every bucket (wired / audit-only / orphan).  This is
intentional — the directory is the storage location for "intentionally
not part of the live wiring graph".

## Reviving a witness

To bring a deprecated witness back into the audit:

1. `git mv folio-assistant/computations/_deprecated/<name>.witness.json
   folio-assistant/computations/<name>.witness.json`
2. Either:
   - add `"auditOnly": "docs/audits/<report>.md"` and `WitnessBuilder.set_audit_only(...)` in the producer, or
   - point a content block's `computation.witness` (or a `content/values/registry.ts` `witnessFile:`) at it.

Bulk deletion of this directory is owner-only.

## 2026-05-28 pass — orphan re-sweep

Added `folio-assistant/computations/cleanup_legacy_witnesses.py` which
codifies the same four heuristics from the original sweep plus two
guards added after the first dry-run produced false positives:

1. No top-level `contentBlock` self-claim on the witness JSON.
2. Not marked `auditOnly`.
3. Not imported by any live (non-`_deprecated/`) python file.
4. Not cited by name in any markdown under `_audits/` or `docs/audits/`.
5. Not referenced by **full filename** (with extension) from any CI
   workflow, shell script, content-pipeline TS file, or other live
   python file under `computations/`.
6. Script name does not end in `_audit`, `_scan`, `_compliance`,
   `_dashboard`, or `_validator` (I14 infra convention — these are
   always live regardless of contentBlock).

This pass moved **9 orphan scripts** + their `*.witness.json` sidecars
into `_deprecated/`. Re-run the helper any time the orphan list
appears to grow:

    python3 folio-assistant/computations/cleanup_legacy_witnesses.py            # dry run
    python3 folio-assistant/computations/cleanup_legacy_witnesses.py --apply --git

