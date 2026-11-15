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
updated_at: 2026-11-15T13:30:00Z
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

## Progress, 2026-10-14 (branch `claude/l7pj-references-per-entry-split`)

Done on the branch, not merged:

- **Split.** 913 entries are `folio/references/<id>.json`: `$schema` first, then the CSL item as the module evaluated it. 48 comment lines that sat inside an entry are that file's `_comment` array (dropped on load).
- **Built by code, still inline:** `leitner2026` (from `paperIdentity`).
- **Order.** The `ORDER` list in `references.ts` holds one `{ id: … }` line per entry, plus the 742 comment lines between entries. The loader refuses a duplicate, a missing file or an unlisted file. The `id:` spelling keeps the key-only text scanners working (platform `bib-cite-resolves`, `check-citation-keys.py`).
- **`sync-references-library.py`** writes per-entry files and refuses the old layout (exit 2).
- **Seven Python text scanners** read the entries through `scripts/lib/references_dir.py`.

Measured:

- the exported array equals main's;
- `references.bib` is byte-identical (clock frozen, sha256 `b523e450…`);
- `run-validate-references` output is identical (0 errors / 183 warnings / 460 info);
- all 913 files pass core `ReferenceNodeSchema`;
- with the declaration added, core's `bibliography-page` `collect()` at platform main reads 913 entries, 0 invalid.

**Still open:**

1. **The `qou.json` declaration is NOT committed.** At the pinned platform (`c56b73b`), `readDeclaration` throws `unknown graph typology "references"`. That misroots every platform script, the trap `.folio-assistant-pin` records. The declaration needs a pin bump past a core that registers `references`, which is an owner call.
2. **Platform-side text readers of `references.ts`** still scan for entry bodies and will see only `leitner2026`:
   - `source-ledger-index.ts` (ids, arXiv, URL);
   - `audit-tex-source.ts` Rule A (title/note);
   - core `src/routes/relevance.ts`.

   `bib-cite-resolves` is unaffected because ORDER keeps `id:`.
3. **Done-when item 4** (63q4's `references/<key>.jsonld` generator) belongs to the platform.
4. **Skills docs** under `skills/local/` still say "add a `ref()` in references.ts".

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
