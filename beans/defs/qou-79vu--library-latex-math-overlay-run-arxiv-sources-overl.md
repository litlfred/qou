---
# qou-79vu
title: 'Library LaTeX-math overlay run: fetch arXiv sources, overlay, benchmark, re-ingest'
status: todo
type: task
priority: normal
tags:
    - library
    - ingestion
parent: qou-1qhv
created_at: 2026-10-10T14:40:00Z
updated_at: 2026-10-10T14:40:00Z
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

## Report (in this bean, when done)

- Fetch outcome counts: fetched / PDF-only / failed.
- Overlay counts: entries overlaid, sections overlaid, and failures for each
  gate. A high prose-gate failure rate means the gates need tuning and needs a
  look before step 3.
- Benchmark before the overlay: formulas, recall (exact), recall, and mean
  distance. This measures how much maths the text layer lost.
- Spot-check 5 overlaid sections by eye against the PDF.

## Not in scope

- The ~200 non-arXiv entries. They need a vision/OCR rung, which requires a
  model API key at run time. That is a separate bean.
- The benchmark's LLM-judge stage. It isn't implemented, for the same reason.

## Done when

The overlay has run on every arXiv entry that has a source, the derived files
are regenerated and committed in a PR, and the counts above are recorded here.
