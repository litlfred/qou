---
# qou-l7pj
title: 'Bibliography: split references.ts into one CSL-JSON file per entry in a declared directory (each a Reference node), keep LaTeX/BibTeX output identical'
status: todo
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-14T17:50:00Z
updated_at: 2026-10-14T17:50:00Z
parent: qou-8tlx
---

## Owner ruling, 2026-10-14 (session https://claude.ai/code/session_01QHu5UpKG62GzKEgprQkzDh)

Asked "what does qou need to do to align its bibliography? … options? impact?" and offered:
1. keep CSL-JSON as source, generate one KG node per entry;
2. split `references.ts` into one authored CSL-JSON file per entry;
3. migrate authoring to Dublin Core;
4. wait.

The owner chose **"1 + 2"**. Option 1 is platform work, in folio-assistant bean `folio-assistant-63q4`: Reference KG nodes, a path-limited bibliography viewer like the glossary, and exports in BibTeX / CSL-JSON / RIS / Dublin Core. This bean is qou's half of option 2.

Dublin Core was not chosen as the **source**, for two reasons. It has no proper fields for volume, issue, page or series; for example, `rogers1907` is Proc. LMS *series 2*. Moving to it would also force `export-bibtex` to change and risk lossy PDFs. Every Reference node will still *read* as Dublin Core through its JSON-LD context (63q4).

This supersedes one line of the C9 plan (`docs/audits/2026-10-04-workplan-and-migration/C9_bib_references_migration_plan.md` §2), which kept `references.ts` as a single module.

## What changes

- **Split** `folio/schema/references.ts` (~915 `ref()` entries) into `folio/references/<key>.json`, one file per entry.
  - Each file is CSL-JSON plus the derived `library` block, with `$schema: folio-reference/v1` (the schema comes from 63q4).
  - Declare the directory in qou's declaration with graph typology `references` (or the name 63q4 fixes).
  - The split is mechanical: no key, field, entry or paper text changes, and the `library` blocks are carried byte for byte.
- **Keep a thin `references.ts`** that loads the directory and still exports the registry. Then:
  - `references-registry-di.ts`, `export-bibtex`, `validate-references`, `bib-qa`, the four `bib-*` QA criteria (`qa-criteria-registry.ts:2776-2782`) and Lean `-- Ref:` checks work unchanged;
  - they are re-pointed at the directory one at a time, and the shim is removed last.
- **Point `scripts/sync-references-library.py`** at the per-entry files. It writes the `library` block, so it must edit one file, not a 17k-line module.
- **Leave the 12 open sync cases** (`8tlx` B6) to the owner's ruling, as now.

## Done when

- `export-bibtex --check` gives a byte-identical `references.bib` before and after the split, so the LaTeX/PDF output is unchanged.
- `run-validate-references.ts` reports the same counts as before.
- Each `folio/references/<key>.json` passes the `folio-reference/v1` validator (once 63q4 lands; until then, the CSL-JSON Zod check `ref()` applies now).
- The 63q4 generator emits `references/<key>.jsonld` for every entry, so every `cito:cites` IRI in qou's block JSON-LD resolves.

## Impact

| | |
|---|---|
| Content | none (mechanical split) |
| LaTeX / PDF pipeline | none (BibTeX still from CSL; checked byte-identical) |
| Tools | `sync-references-library.py`, and anything that greps `references.ts` |
| Lean | none (`-- Ref:` keys unchanged) |
| Diff size | one large PR (~915 new files, one module shrunk) |

## Order

After `folio-assistant-63q4`'s schema step, so files carry the right `$schema` from the start. The split can go first with `$schema` added in a second pass, if the owner prefers.
