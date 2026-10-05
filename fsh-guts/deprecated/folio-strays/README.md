# folio-strays — moved out of `folio/` by owner ruling (CONTENT C7, bean `qou-4s33`, 2026-10-05)

Kept for the record; nothing here is run.

| file | was | why it moved |
|---|---|---|
| `get_fails.py`, `get_failures.py`, `get_md_files.py` | `folio/` | one-off scripts reading an `evaluations` key that no QA sidecar carries — dead |
| `triage_stubs.ts` | `folio/pipeline/` | destructive (`unlinkSync` on `.lean` "shadows", rewrites placeholders), no docblock, no caller. Moved so it cannot be run by accident during the migration. |

Evidence: `docs/audits/2026-10-04-workplan-and-migration/C7_data_and_stray_files.md`.
