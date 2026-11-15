---
# qou-79vu
title: 'Library LaTeX-math overlay run: fetch arXiv sources, overlay, benchmark, re-ingest'
status: completed
type: task
priority: normal
tags:
    - library
    - ingestion
created_at: 2026-10-10T14:40:00Z
updated_at: 2026-10-10T15:56:33Z
parent: qou-1qhv
---

## Why

The section text of the ingested arXiv papers in `library/` comes from the PDF
text layer (pdftotext), which mangles mathematics: `3₁` reads as `3 1`, and
$\phi:\mathbb{R}^3\to S^2$ reads as `φ: R3 → S2`. arXiv holds the authors'
LaTeX source, which is exact. The tools that use it are in
litlfred/cat-harness-tools PR #52 (issue #51), branch `claude/latex-math-rung`:

- `scripts/arxiv-source.py`: fetches `arxiv.org/e-print/<id>` into
  `library/<entry>/source/e-print` and writes `source.json` with the URL,
  sha256, size and fetch time. It reads the id from the directory name and
  handles old-style ids (`alg-geom/9408004v1`).
- `scripts/latex-math-overlay.py`: replaces a section's text with its LaTeX
  `\section`, converted by pandoc with `$…$` maths, only when three gates pass:
  - the titles agree (sections are never paired by position);
  - at least 60% of the prose words agree;
  - the LaTeX covers at least 50% of the PDF section's words.

  It records `text_source: latex` on each section it replaces, and
  `source.math_source` in `structure.json`.
- `scripts/formula-benchmark.py`: scores section text against the paper's
  LaTeX formulas, first by exact substring, then by approximate-substring
  Levenshtein distance up to a threshold of 0.2 (Horn & Keuper,
  arXiv:2512.09874). It reports recall and mean distance, and writes to
  `build/benchmarks/` (never into a graph directory).

## Requirements before starting

1. **Network access to arxiv.org.** It returns 403 from the cloud sandbox
   (measured 2026-10-10). Run this on a machine that can reach it (owner's Mac
   via Remote Control), or once arxiv.org is on the environment allowlist.
2. **pandoc** must be installed. Without it the overlay keeps the raw LaTeX
   instead of converting it to markdown.
3. A cat-harness-tools checkout with PR #52 (merged, or on the branch).
4. Check the library-ingestion owner first. Session
   `session_01TrohkM6CvNiSBiG5czmFWJ` owns qou ingestion, the driver and the
   KG rebuild. Coordinate with it so two runs don't both write to `library/`.

## Steps

```bash
T=../cat-harness-tools/scripts
# 1. Baseline: run the benchmark on the text layer BEFORE overlaying, or the
#    "before" number is lost (overlaid sections are not scored).
python3 $T/arxiv-source.py library/arxiv-*            # 3 s between requests; ~522 entries, ~30 min
python3 $T/formula-benchmark.py library/arxiv-* --json build/benchmarks/formula-before.json
# 2. Dry run and read the gate verdicts before writing anything
python3 $T/latex-math-overlay.py library/arxiv-* --dry-run
# 3. Overlay
python3 $T/latex-math-overlay.py library/arxiv-*
# 4. Regenerate the derived files (INDEX.md, summaries, .jsonld graph
#    siblings) with the ingest driver, per the owning session's procedure.
```

## Licences decide publication (owner, 2026-10-10)

Whether a paper may be republished with the publication depends on its
recorded licence, so treat the licence counts as a deliverable, not a side
effect.
- `stated` with a CC licence (`creativecommons.org/...`): republication is
  allowed on that licence's terms.
- `stated` as `arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv's default):
  this grants rights to arXiv only, not to us.
- `stated` as `http://arxiv.org/licenses/assumed-1991-2003/`: assumed non-exclusive
  licence for submissions prior to January 2004 (arXiv was granted non-exclusive
  distribution rights equivalent to nonexclusive-distrib/1.0 by the act of submission).
- `unknown`: arXiv recorded no licence; nothing is established.

A `LICENSE` file inside a source bundle is noted in the record and not
interpreted; read it by hand. An editor-written `licence.json` is never
overwritten.

## Report

### 1. Fetch Outcome Counts
- Total arXiv entries processed: **522**
- `fetched`: **521**
- `present`: **1** (`arxiv-0705.1468v1`, pre-existing)
- `failed`: **0**
- `skipped`: **0**

### 2. Baseline Formula Benchmark (Text Layer Before Overlay)
Artifact: `build/benchmarks/formula-before.json` (micro-averaged across all formulas):
- Total formulas scored: **326,445** across **420** entries
- Exact recall (`recall_exact`): **0.224** (22.4%)
- Recall (`recall`, exact + fuzzy Sellers distance $\le 0.2$): **0.279** (27.9%)
- Mean normalized distance: **0.492**

### 3. Overlay Counts & Gate Verdicts
- Total entries processed: **522**
- Entries overlaid: **431** (369 entries with $\ge 1$ overlaid section, 62 entries where all candidate sections failed gates)
- Entries skipped: **91** (62 plain TeX/snippet bundles lacking `\documentclass` + `\begin{document}`, 29 bundles with no `\section`)
- Entries failed: **0**
- Total sections evaluated: **8,508**
  - Sections successfully overlaid: **1,211**
  - Title gate (`no matching \section`): **6,148**
  - Prose gate (`prose gate failed — titles agree, contents do not`): **1,034**
  - Coverage gate (`coverage gate failed — LaTeX section holds only part of PDF section`): **115**

### 4. Spot-Checks (5 Overlaid Sections against Source PDFs)
1. `library/arxiv-0705.1468v1/sections/sec-001-the-skyrme-faddeev-model-and-low-charge-solitons.md`
   - Title: "The Skyrme-Faddeev model and low charge solitons"
   - Prose ratio: 0.996 | Coverage ratio: 1.000 | Converter: `pandoc`
   - Verification: Faddeev energy functional integral, topological charge integral $Q = \frac{1}{4\pi^2}\int_{S^3} F \wedge A$, Ward's conjectured energy bound $E \ge c Q^{3/4}$, bold vector fields $\mbox{\boldmath $\phi$}$ all cleanly formatted.
2. `library/arxiv-math-0305275v1/sections/sec-002-the-straightening.md`
   - Title: "The straightening"
   - Prose ratio: 0.985 | Coverage ratio: 0.995 | Converter: `pandoc`
   - Verification: Moduli in $\mathbb{H}^3$, homeomorphism $\eta \circ \varphi \circ \beta = \psi$, straightening map ${\rm Str}(D_\rho)$, definitions and lemmas rendered in Pandoc Markdown.
3. `library/arxiv-math-ph-0012035v3/sections/sec-020-4-summary.md`
   - Title: "Summary"
   - Prose ratio: 1.000 | Coverage ratio: 0.987 | Converter: `pandoc`
   - Verification: Clean prose overlay, author acknowledgments, Polish diacritics (P. Kosiński, University of Łódź) preserved.
4. `library/arxiv-cond-mat-0112325v6/sections/sec-000-1-introduction.md`
   - Title: "INTRODUCTION"
   - Prose ratio: 0.968 | Coverage ratio: 0.975 | Converter: `pandoc`
   - Verification: Gauge bosons $W_\mu$, $Z_\mu$, isotopes $^{87}{\rm Rb}$, $MgB_2$ preserved.
5. `library/arxiv-2002.04901v5/sections/sec-000-0-introduction.md`
   - Title: "Introduction"
   - Prose ratio: 0.989 | Coverage ratio: 0.835 | Converter: `pandoc`
   - Verification: Derived completions $\mrm{L}\La_{\a}(M)$, dual Koszul complexes $\opn{K}^{\vee}_{\infty}(A; \aa)$, displayed equations with labels accurately preserved.

### 5. arXiv Licence Census
- Total arXiv entries processed: **522**
- `arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv default distribution licence): **306**
- `http://arxiv.org/licenses/assumed-1991-2003/` (assumed non-exclusive licence for pre-2004 submissions): **92**
- `unknown` (no licence recorded by arXiv, post-2003 submissions): **65**
- `CC-BY` (republishable): **46**
- `CC-BY-SA` (republishable): **3**
- `CC0` (republishable): **0**
- Other CC (`CC-BY-NC-SA`: 6, `CC-BY-NC-ND`: 4): **10**
- Bundles carrying licence files: **0**
- Total republishable entries (`CC-BY` + `CC-BY-SA` + `CC0`): **49**

#### Republishable entries (49):
- `arxiv-1907.03683v4` (CC-BY 4.0)
- `arxiv-1910.09966v1` (CC-BY 4.0)
- `arxiv-2007.15570v1` (CC-BY 4.0)
- `arxiv-2101.05931v3` (CC-BY 4.0)
- `arxiv-2104.01786v1` (CC-BY 4.0)
- `arxiv-2104.04941v2` (CC-BY 4.0)
- `arxiv-2106.01332v4` (CC-BY 4.0)
- `arxiv-2106.07444v2` (CC-BY 4.0)
- `arxiv-2108.09349v2` (CC-BY 4.0)
- `arxiv-2109.04664v4` (CC-BY 4.0)
- `arxiv-2111.06645` (CC-BY-SA 4.0)
- `arxiv-2111.06645v3` (CC-BY-SA 4.0)
- `arxiv-2111.12409v4` (CC-BY 4.0)
- `arxiv-2201.05665v1` (CC-BY 4.0)
- `arxiv-2205.06874v2` (CC-BY 4.0)
- `arxiv-2205.07095v1` (CC-BY 4.0)
- `arxiv-2206.14086v3` (CC-BY 4.0)
- `arxiv-2208.12678v4` (CC-BY 4.0)
- `arxiv-2208.13448v2` (CC-BY 4.0)
- `arxiv-2208.13692v1` (CC-BY 4.0)
- `arxiv-2211.13362v2` (CC-BY 4.0)
- `arxiv-2301.00125v3` (CC-BY 4.0)
- `arxiv-2301.08311v4` (CC-BY 4.0)
- `arxiv-2302.08363v2` (CC-BY-SA 4.0)
- `arxiv-2305.07425v1` (CC-BY 4.0)
- `arxiv-2305.14884v2` (CC-BY 4.0)
- `arxiv-2306.13098v2` (CC-BY 4.0)
- `arxiv-2311.02632v2` (CC-BY 4.0)
- `arxiv-2311.14221v2` (CC-BY 4.0)
- `arxiv-2312.00624v1` (CC-BY 4.0)
- `arxiv-2401.04019v1` (CC-BY 4.0)
- `arxiv-2402.04839v2` (CC-BY 4.0)
- `arxiv-2402.08782v1` (CC-BY 4.0)
- `arxiv-2406.02111v3` (CC-BY 4.0)
- `arxiv-2411.03801v2` (CC-BY 4.0)
- `arxiv-2412.02281v1` (CC-BY 4.0)
- `arxiv-2501.03424v1` (CC-BY 4.0)
- `arxiv-2505.00799v2` (CC-BY 4.0)
- `arxiv-2506.10206v2` (CC-BY 4.0)
- `arxiv-2507.12454v1` (CC-BY 4.0)
- `arxiv-2508.03145v1` (CC-BY 4.0)
- `arxiv-2509.04267v3` (CC-BY 4.0)
- `arxiv-2509.20302v1` (CC-BY 4.0)
- `arxiv-2512.18642v1` (CC-BY 4.0)
- `arxiv-2604.16077v1` (CC-BY 4.0)
- `arxiv-2605.09605v2` (CC-BY 4.0)
- `arxiv-2605.19310v1` (CC-BY 4.0)
- `arxiv-2605.28781v1` (CC-BY 4.0)
- `arxiv-2608.25107v1` (CC-BY 4.0)

### 6. Derived Files & Graph Regeneration
- Emitted `source/manifest.jsonld` across all 522 arXiv entries in `library/` carrying `meta.files` and `dcterms:license`.
- `scripts/summarize-library.py --apply`: refreshed `library/INDEX.md`, `summary.json`, and injected contextual `doc_brief` into 13,546 section files. Verified up to date with `scripts/summarize-library.py --check`.
- `scripts/sync-references-library.py --check`: verified 440 usable joins, `references.ts` up to date.

## Not in scope

- The ~200 non-arXiv entries. They need a vision/OCR rung, which requires a
  model API key at run time. That is a separate bean.
- The benchmark's LLM-judge stage. It isn't implemented, for the same reason.

## Done when

Every arXiv entry has a licence record and, where arXiv has one, its source in
the graph; the overlay has run on every entry that has a source; the derived files
are regenerated and committed in a PR, and the counts above are recorded here.
