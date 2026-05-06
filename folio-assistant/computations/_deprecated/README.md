# Deprecated witnesses

This directory holds `*.witness.json` files that are **dead exploratory
probes** from earlier research passes:

- no content block consumes them (`computation.witness` / `:val[…]`
  registry / `witness:` array)
- no audit report under `docs/audits/*.md` cites them
- the witness body itself contains no assertions
  (`falsifiability == "no-assertions"`)

They are kept under git history rather than deleted because the
producing scripts (in the parent `folio-assistant/computations/`
directory) may still be imported by live code, and reviving an
exploration only requires re-running the producer to re-emit the
witness next to its script.

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
