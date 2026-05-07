# Deprecated witnesses and producing scripts

This directory holds `*.witness.json` files that are **dead exploratory
probes** from earlier research passes:

- no content block consumes them (`computation.witness` / `:val[…]`
  registry / `witness:` array)
- no audit report under `docs/audits/*.md` cites them
- the witness body itself contains no assertions
  (`falsifiability == "no-assertions"`)

It also holds the **producing `.py` scripts** for those witnesses, when
the script is not imported by any live (non-`_deprecated/`) code.  In a
follow-on pass (this PR), 262 of the 285 candidate scripts were moved
here alongside their witnesses; the remaining 23 candidate scripts are
**kept in place** under `folio-assistant/computations/` with a
`# DEPRECATION-CANDIDATE: ...` header comment, because they are still
imported by live code and moving them would break the importer.  Those
23 should be revisited when the live importer is itself retired or
rewired off the deprecated dependency.

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
