# C9: bibliography and references migration plan (owner request, 2026-10-05)

The owner asked for this while ruling on C7 (*"plan bib/references migration.
issues?"*). Measured on `main` `f5e20a23f6` against platform `fa-test`
`6afb5d5e93`.

**Issues.** No GitHub issue covers this in `litlfred/qou` or
`litlfred/folio-assistant`; semantic searches for bibliography, references and
bib verification return 0 results in both. No bean covers it either. C5
(`qou-f2ri`) is about *editorial* cross-references, not the bibliography.
T12 (`qou-oumk`) covers only *upstreaming the bib tooling*. This plan opens
tracking issue litlfred/qou#7528 and bean C9.

## 1. What exists today

| artefact | size | what it is | today's home |
|---|---|---|---|
| `folio/schema/references.ts` | 742 KB, 892 `ref()` entries | CSL-JSON bibliography, the source of truth | folio content (the platform reads it through `references-registry-di.ts`) |
| `references.bib` | 278 KB, committed | BibTeX, **generated** from `references.ts` by `export-bibtex.ts` | repo root |
| `folio/schema/references.review.json` | 2 entries (`ohara1991` issue-open, `leitnerpawloski2004` validated) | **human** review status per reference, hash-pinned (bib-human-review phase 1) | beside the bibliography |
| `folio/bib-qa-verifications.json` | 1.3 MB, 456 entries: 355 agent verdicts, 101 with no `verified_by` | a check of each reference against its PDF or an external source | folio root |
| `folio/bib-qa-images/` | empty (`.gitkeep`) | upload target for photo evidence | folio root |
| `library/<doc-id>/` | ~660 dirs | the ingested sources; `doc-id` is the join key to verifications | declared `library` directory |
| `scripts/`: `bib-agent-backfill.ts`, `check-reference-pdfs.py`, `drain-reference-literals.py`, `library-propose-references.py`, `library-refresh-metadata.py`, `sync-references-library.py`, `run-validate-references.ts` | — | qou-side tools | undeclared |
| skills `bib-qa`, `bib-human-review`, `bib-photo-ingestion-watcher`, `document-intake` | — | procedure | `skills/local/` |

The platform already has schemas and tools for most of this:
- `cat-harness/schemas/bib-verification.ts` (the `Verifier` union: agent or human);
- `validate-bib`, `validate-references`, `validate-references-human-review`, `bib-qa`, `export-bibtex`, `citations`, `migrate-bib-verifier`;
- the `attestations`, `qa`, `library` and `uploads` graph kinds;
- `library-ref.ts` (cross-instance source references).

## 2. Where each piece should go

| artefact | proposed home | why |
|---|---|---|
| `references.ts` | **stays** in `folio/schema/` | it is folio content; the platform's DI seam already reads it there |
| `references.bib` | **generated, checked by `export-bibtex --check`**; then gitignore it once the PDF build regenerates it | a committed copy of derived data drifts. (The build no longer runs on Actions, so that build must be the local one.) |
| `references.review.json` | **`attestations`** family `bib-human-review` under `test/attestations/` | a human judgement pinned to a hash is exactly what `qa-attestations/v1` holds; it survives deletion of derived results |
| `bib-qa-verifications.json` | **`attestations`** family `bib-verification`, one file per reference | agent and human verdicts are both judgements (the kind's own summary says so). The 101 entries with no verifier get recorded as `unknown` and are never upgraded to agent or human. |
| `bib-qa-images/` | the declared **`uploads`** directory | it is evidence intake, not content |
| `bib-qa.json` (derived) | **`qa`**, published to `qa-reports` | derived; not committed |
| qou bib scripts | **T12**: upstream the generic ones to `folio-assistant-core`; declare the rest as Tool nodes in `tool-defs/` | no tool should sit outside the KG (owner ruling 2026-10-04) |
| bib skills | **upstream** to `folio-assistant-core` (SKILLS2 analysis) | the platform copy is the one other folios read |

## 3. Known defects to fix along the way

1. **`run-validate-references.ts` exits 1.** The folio has 5 papers, and the platform's `validate-references` requires `--paper` when there is more than one. qou's wrapper does not pass it (CONTENT report §6). The fix is in qou's wrapper only.
2. **101 verifications have no verifier.** The migration must carry them as unknown and must not attribute them.
3. **Human review covers 2 of 892 references.** That is not a migration defect, but the attestations move should make the gap visible.

## 4. Stories (proposed, in order)

| # | story | done-when (parity P-C: no `.md`/`.lean`/`.ts` content blob changes except the files named) | owner? |
|---|---|---|---|
| B1 | Fix `run-validate-references.ts` to pass `--paper` per paper | exits 0 or reports real findings for each of the 5 papers | no |
| B2 | Declare `uploads` (`folio/bib-qa-images/`) and wire `export-bibtex --check` into compute-QA | gate reports drift between `references.bib` and `references.ts` without rewriting | no |
| B3 | Migrate `references.review.json` → `attestations/bib-human-review` (2 entries, hashes preserved) | `validate-references-human-review` reads the new home and gives identical verdicts | **yes**: human-judgement data moves |
| B4 | Migrate `bib-qa-verifications.json` → `attestations/bib-verification` (456 entries; 101 as unknown) | a round-trip test proves every entry is preserved byte-for-byte in substance | **yes** |
| B5 | Tool nodes for the 7 qou bib scripts (or upstream under T12) | `tools()` lists them; none runs automatically | no |
| B6 | Gitignore `references.bib` once the local PDF build regenerates it | the build produces it; `--check` is clean | **yes** |

Nothing in this plan edits a reference entry, a citation key, or any paper text.
