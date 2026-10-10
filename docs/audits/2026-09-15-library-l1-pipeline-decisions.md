# uploads/ -> library/ ingest pipeline: owner decisions and what the tree can actually support

**Date:** 2026-09-15 · **Beans:** `qou-l2cr` (session), `qou-ehgk` (naming / DC / assets), `qou-ziag` (KG precision / BPMN)

The owner asked for eight changes to the ingestion pipeline and asked for options
on the ones with a real fork. This records the four decisions taken, and the
measurement that says which half of decision A can be executed mechanically and
which half cannot.

## Measured baseline

Taken on `main` at `b6c1af8e1f`, 2026-09-15.

| | |
|---|---:|
| `library/` directories | 705 |
| still queued in `uploads/` | 11 |
| bibliography entries (`content/schema/references.ts`) | 872 |
| ...carrying `library.docId` | 441 |
| **...where `docId` equals the bib slug** | **22** |
| library dirs no bib entry points at | 265 |
| dirs with `manifest.jsonld` (the L1 graph) | 576 (129 missing) |
| standalone Dublin Core record | 0 |
| structural node-level citations from a content block | 0 (2 prose-only mentions) |
| scripts touching `library/` | 17 in qou, plus several in folio-assistant |

Two conventions already exist and shrink the work:

- **`dcterms` is already the JSON-LD vocabulary.** `folio-assistant/schemas/jsonld.ts`
  lines 484-529 map `title` to `dcterms:title` and `contains` to `dcterms:hasPart`.
  A Dublin Core record is an extension of a live context, not a new one.
- **BPMN is already a working convention.** Seven `.bpmn` files under
  `folio-assistant/docs/workflows/`, rendered by `bun run render:bpmn`, surfaced
  in `docs/publication-workflow.md` with proper participant lanes. There is no
  ingestion diagram yet; adding one follows an established path.

One constraint bites: `LibraryRef` carries its own contract in its docstring --
*"derived entirely from the library tree ... never authored, never hand-edited"* --
so an authored remote URL placed inside `library:` is dropped by the next
`sync-references-library.py` run.

## Decisions (owner, 2026-09-15)

| fork | decision |
|---|---|
| **A — folder naming** | **A1 + A3, full normalisation.** The folder name *is* the bibliography slug, including minted slugs for the 265 dirs no entry points at. (The agent had recommended A2, docId + alias; overruled.) |
| **B — Dublin Core** | **B3, both.** `dublin-core.jsonld` per folder is the record of truth; `manifest.jsonld` references it. Covers all 705 dirs, including the 129 with no manifest. |
| **C — remote assets** | **C3, first-class `assets[]`**: `kind` (pdf/png/dataset), `role` (primary/figure/data), `url` *or* local path, checksum, `retrieved`. Covers remote URLs and the hand-drawn workflow PNG in one field, and leaves `library{}` derived-only so the sync contract holds. |
| **E — citation precision** | **E3, both.** `cites` stays the bibliography; new `grounds: [{ref, node, quote?}]` carries the KG-precise claim, and the semantic-validity audit runs against it. |

## Decision A splits into a safe half and a blocked half

`scripts/library-slug-map.py` computes the rename map and changes nothing. Run:

```sh
python3 scripts/library-slug-map.py --json docs/audits/2026-09-15-library-slug-map.json
```

| tier | count | meaning |
|---|---:|---|
| `bound` | **440** | a bib entry already points here; the slug is a curated citation key, nothing is invented |
| `mint-high` | 157 | plausible author line + arXiv-encoded year |
| `mint-low` | 26 | plausible author, but the year is the PDF's `CreationDate` -- the file date, not the publication year |
| `needs-source` | 82 | no usable author line, or no year at all |

**The `bound` half is safe and self-consistent**: 418 renames, 22 already correct,
**zero** slug collisions and **zero** cases where a target name is occupied by a
different directory.

**The minted half is not executable as measured.** A seeded sample of 14
`mint-high` rows, hand-checked against the title and author line, came out **7
right and 7 wrong**:

| minted | should be | failure |
|---|---|---|
| `pgl2013`, `categories2001` | -- | title fragment read as an author |
| `reiter2011` | `blatt2011` | took the second author |
| `carolynabbott2023` | `abbott2023` | OCR ran given and family names together |
| `society1993` | -- | "AMERICAN MATHEMATICAL SOCIETY" |
| `krber2017` | `korber2017` | umlaut stripped from Koerber |
| `ega2009` | `dolega2009` | OCR split the ligatures in Dolega |

At that rate the tier would mint roughly **78 wrong citation keys across 157
directories, silently** -- keys that assert an author who does not exist. The
root cause is that `structure.json`'s `metadata.authors_raw` is a heuristic
first-page grab, not parsed authorship; observed values include a journal
banner, HAL boilerplate, a department, a postal address and the second line of
the title.

So decision A executes in two phases:

- **Phase 1 (unblocked):** rename the 440 `bound` directories. The slug is
  already curated, the map is collision-free, and the change is mechanical.
- **Phase 2 (blocked on metadata):** the 265 orphans need a real authorship
  source -- the arXiv API, Crossref via the DOI, or an agent reading page 1 --
  before any slug is minted. Minting off `authors_raw` is not an option.

Phase 2 is the whole reason the map script reports tiers rather than a flat
list: the tier is the audit trail for which slugs were derived and which were
asserted.
