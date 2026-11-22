---
# qou-agth
title: 'Antigravity: download Thurston GT3M (full notes, at least Ch. 4 and 7) and ingest into library/'
status: todo
type: task
priority: high
owner: Antigravity
tags:
    - for-antigravity
parent: qou-1qhv
blocking:
    - qou-2hc7
created_at: 2026-11-22T11:00:00Z
updated_at: 2026-11-22T12:00:00Z
---

Owner request 2026-11-22 (thread "cite-intake"): put the Thurston download as a
bean for Antigravity. Owner ruling 2026-11-21 (docs/coordination/owner-rulings.md
row 33): work that fails here on resource limits goes to Antigravity.

Why it fails here: the cloud proxy returns 403 for library.msri.org / slmath, so
the PDFs cannot be fetched from a Claude Code remote session.

## Sources (SLMath, formerly MSRI; free)
- Index: http://library.msri.org/books/gt3m/
- Ch. 4 (hyperbolic Dehn surgery, §4.5 gluing equations): http://library.msri.org/books/gt3m/PDF/4.pdf
- Ch. 7 (Milnor, volumes / Lobachevsky function): http://library.msri.org/books/gt3m/PDF/7.pdf
- Chapter URLs are from memory and unverified; if one fails, take the links
  from the index page. Prefer the whole set of chapter PDFs.

## Current state
`library/thurston/Thurston.pdf` holds only Ch. 1-2 (33 pages). About 156 files
cite `thurston1978`, mostly Lean `-- Ref:` locators to Ch. 7 and Ch. 4, which
cannot be checked against the held excerpt. The `thurston1978` entry in
`folio/references/` has a garbled `note` and some citing sites carry DOI
10.1007/978-1-4612-9903-6, which is unverified for these notes.

## To do
1. Download the chapter PDFs (at least 4 and 7, ideally all 13).
2. Ingest into `library/thurston/` (or a new doc-id) with the folio-assistant
   `pdf-structure.py` + `extract-candidates.py` pipeline, then
   `python3 scripts/summarize-library.py --apply`.
3. Hand back to bean `qou-2hc7`: verify each Ch. 4 / Ch. 7 locator, fix the
   `note` field, and confirm or drop the DOI.

## Also ingest (owner OK 2026-11-22)
- McPhail-Snyder 2025, *A quantization of the SL2(C) Chern-Simons invariant of
  tangle exteriors*, arXiv:2509.02365 (v3): https://arxiv.org/abs/2509.02365 ,
  PDF https://arxiv.org/pdf/2509.02365v3 . Registered as `mcphail-snyder-2025`
  (PR #8861); cited by `QOU/QBeta/McPhailSnyderBridgeExclusion.lean`. After
  ingesting, add a `library` block to `folio/references/mcphail-snyder-2025.json`.
