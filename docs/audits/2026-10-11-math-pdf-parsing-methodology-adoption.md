# Math-PDF parsing methodology: what the ingest pipeline already uses, and what it does not

Owner request, 2026-10-10: three papers were uploaded "with new methodologies
on scanning math papers to add to process/tools". This note maps each paper's
method onto a step of qou's library ingestion. That pipeline is
`litlfred/cat-harness-tools`, driven for qou by `scripts/library-ingest.ts`.
The note says which methods are already in the code and proposes the rest.
Owner selected options A and B on 2026-10-11: write this note, and open
platform issues.

Bean `qou-0nko` (epic `qou-uwxm`). All three papers are ingested into
`library/` on PR #7608.

## The three papers

| paper | method | headline measurement (the paper's own) |
|---|---|---|
| Horn & Keuper, *Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs*, arXiv:2512.09874v3 | Synthetic PDFs with exact LaTeX ground truth. Parsed formulas are aligned by a two-stage match (LLM extraction, then fuzzy validation) and scored by an LLM judge for **semantic** equivalence. | Judge vs. humans: Pearson r = 0.78 (250 pairs, 750 ratings), against r = 0.34 for character-level CDM and r ≈ 0 for text similarity. 20+ parsers compared; rule-based extractors are the weakest tier. |
| Pluzhnikov, Satpute, Schubotz, Teschke, Gipp, *LLM-supported document separation for printed reviews from zbMATH Open*, arXiv:2604.00554v1 | OCR to LaTeX (Mathpix judged best by BLEU and edit distance). Then fine-tuned generative LLMs, combined by **majority vote**, find where each document starts and ends inside a scanned multi-document volume. | 97.5 % accuracy given the text. Start and end indexes found for 90.6 % of documents, 98.4 % correct where applicable, 89.1 % overall. 810,977 documents processed. |
| Mali, Kukkadapu, Mahdavi, Zanibbi, *ScanSSD: Scanning Single Shot Detector for Mathematical Formulas in PDF Document Images*, arXiv:2003.08005v1 | Locates displayed and embedded formulas from **visual features only** (600 dpi page image, sliding windows, page-level pooling). Works on born-digital and scanned pages alike. | Character-level f-score 0.926. Formula f-score 0.796 at IoU ≥ 0.5 and 0.733 at IoU ≥ 0.75 (TFD-ICDAR2019v2). |

## What is already in the pipeline

Read off `cat-harness-tools` at `b7351df` (2026-10-11):

- **Pluzhnikov et al.'s propose-then-verify principle is in `latex-math-overlay.py`.**
  The overlay replaces a section's text-layer prose with the author's own
  LaTeX section. It only does so after three gates pass: titles agree,
  prose agrees, coverage agrees. The docstring names both 2604.00554 and
  Horn & Keuper's two-stage matching as the source of the design.
  `ingest-document.ts` runs it as an arm. On qou's `main` it has been applied
  to **448** entries (`source.math_source: "latex"`), out of 535 `arxiv-*`
  directories and 737 entries in total.
- **Horn & Keuper's string stages are in `formula-benchmark.py`.** It runs
  exact substring matching, then approximate-substring Levenshtein matching
  at a 0.2 threshold.
- **Horn & Keuper's LLM judge is deliberately NOT run.** The script's own
  docstring says: "a third stage, an LLM judge of semantic equivalence, is not
  run here: it needs a model at run time." That third stage is the one the
  paper validates against humans (r = 0.78). Their measurement puts
  character-level matching at r = 0.34, so the benchmark as it stands
  measures the weaker signal.

## What is not in the pipeline, and where it would apply

1. **No mathematics at all for scanned documents.** 31 entries carry an
   `ocr/` tier (`library/*/ocr/page-*.txt`, measured 2026-10-11). The
   overlay cannot help them, because they have no LaTeX source. Their OCR
   text holds formulas as character soup, and nothing marks where a formula
   is.
   - A ScanSSD-style detector would at least *locate* each formula as a
     page region. That is a determined, citable span, even before anyone
     transcribes it.
   - zbMATH's finding is that Mathpix gives the best OCR-to-LaTeX
     transcription. Mathpix is a paid external service, so whether to use it
     is a cost and licence decision for the owner, not a tool choice.
2. **Cutting multi-article scans is done by hand.** On 2026-10-10 a sibling
   session cut four *Invent. Math.* 106 (1991) articles out of a GDZ volume
   scan (`c61cfb205d`). `ant-v14-n7-s` is another multi-article volume, with
   ten `-pNN` children. Pluzhnikov et al. solve exactly this problem:
   boundary detection in a scanned volume, by majority vote over LLMs. It
   fits as a proposal arm (propose boundaries, then a person or a check
   confirms them). The platform's existing "refuse an inferred structure
   unless it passes trust tests" rule already gives the shape for that
   confirmation.
3. **The formula benchmark measures similarity, not meaning.** Adding the
   LLM-judge stage, run offline and with its output recorded as data the way
   image verdicts are, would turn `formula-benchmark.py` into the measurement
   the paper validates.

## Proposed platform issues

Filed on `litlfred/cat-harness-tools`, where the rung code lives:

- [#130](https://github.com/litlfred/cat-harness-tools/issues/130): an LLM-judge stage for `formula-benchmark.py`, with verdicts recorded as
  data;
- [#131](https://github.com/litlfred/cat-harness-tools/issues/131): formula-region detection for OCR'd or scanned pages (ScanSSD-style),
  emitted as a sidecar;
- [#132](https://github.com/litlfred/cat-harness-tools/issues/132): volume-scan document separation as a proposal arm with majority-vote
  boundaries (zbMATH method), confirmed before anything is promoted.

## What this note does not claim

- No method above has been run on qou's corpus. The paper figures are the
  papers' own, on their own datasets. They are not measurements of this
  library.
- Whether a detector or a judge would be accurate *on this corpus* is not
  established here. Each issue asks for a benchmark against held ground truth
  before any output enters `library/`.
