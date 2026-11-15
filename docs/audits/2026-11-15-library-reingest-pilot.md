# Library re-ingest pilot (2026-11-15) — stopped before the full run

Owner instruction (relayed by coordinator, epic `qou-s4ws`): *"ingest existing with new
ingestion tools as KG"*. Tool: platform `cat ingest --instance /home/user/qou`
(`cat-harness-tools/scripts/ingest-document.ts`) at platform pin `82b389982`.
**Nothing was promoted into an existing `library/` entry.** The pilot hit the
stop condition: re-ingest renames the section files the corpus cites, and
regresses at least one OCR-only document.

## Baseline (measured before any change, qou `074a97326`)

| quantity | count |
|---|---|
| directories under `library/` | 736 |
| `INDEX.md` rows | 712 |
| dirs with `manifest.jsonld` + `blocks/` (KG nodes already present) | 735 (all but `codata-2022`, a dataset) |
| `.jsonld` files | 33,932 |
| dirs with `ocr/` | 31 |
| `structure.json` `toc_source` | outline 447, inferred 269, undetermined 14, headings 4, none 1 |
| `summary.json` provenance | extractive 715, **agent 18** |
| dirs with `candidates.json` | 497 |
| dirs with `images.json` | 0 |

So the library is **already a KG** at the L1 level. What the current tools add is
mainly `images.json` / image narratives, `figures/`, `vector-labels.json`, and a
re-run section split.

Doc ids are stable: `_pdf_doc_id.derive_doc_id_from_pdf` maps **736 of 737** PDFs back
to their current directory (outlier: `1-s2-0-0097316595900136-main` → `1-s20-…`).

## Pilot: 34 documents staged (5 chosen + a 30-doc random sample; 3 more failed)

Staged only (`ingest-staging/`), compared with `library/`:

- **9 / 34** keep an identical set of section filenames.
- **25 / 34 rename or renumber section files** (e.g. `arxiv-0706.2213v3` 20 → 25
  sections, 1 filename in common; `kondev-2021-…` 24 → 119). Section files are named
  `sec-NNN-<slug>.md`, so any citation of a specific section path breaks.
- Text volume mostly within ±5 %, outliers −11 % (`arxiv-1006.1099v3`) and +64 %
  (`arxiv-2510.21576v1`).
- **`procrsoclondona92` (Moffatt–Ricca 1992, the AGENTS.md path-5 worked example):
  section text 52,088 → 6,279 bytes (−88 %)**. The current rule sees 1,637
  characters of embedded text (the JSTOR banner), takes the text-layer rung instead
  of OCR, and the title regresses to "The Royal Society is collaborating with JSTOR…".
- 3 OCR documents (`0510388v1`, `2018sorus020`, `arxiv-0707.3682v2`) failed: tesseract
  was not installed in the container (since installed; not re-run).

Corpus references at risk: **45** distinct `library/<id>/sections/<file>.md` paths are
cited across `folio/ docs/ beans/ computations/ .claude/` (33 checked: 21 resolve
today, 12 already dangle).

Also observed: `check:l1-complete` flags `summary.json` as an "unexpected child" in
every entry (it is a qou file, incl. the 18 agent-written summaries). Promotion uses
`cpSync` (merge), so it would not delete it — but it would leave old `sec-*` and
`blocks/*` files beside the new ones, a mixed tree.

## Decision needed (owner)

1. **Re-ingest only documents whose section filenames do not change** (~26 % in the
   sample). Cheap, no path breaks, small gain.
2. **Full re-ingest, then rewrite the cited section paths** (45 cites; old files deleted
   per entry before promote). Gains the new split everywhere; touches beans/audits.
3. **Additive only**: run just the new arms (`pdf-images.py`, image narratives, vector
   labels) into existing entries, keeping sections/blocks as they are. No path breaks;
   needs a platform entry point that does not exist yet.
4. **Do nothing** (default). The library stays at its 2026-10 ingest; it is already
   KG-shaped.

In every option `procrsoclondona92` and other OCR-only entries must be excluded or
forced onto the OCR rung, or they lose most of their text.

Recommendation (judgement): option 3 if the platform can expose it, else option 1;
option 2 is a large mechanical sweep with a real regression risk and modest gain.
