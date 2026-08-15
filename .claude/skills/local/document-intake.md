---
name: document-intake
roles: [collaborator, owner]
description: >
  Process uploaded documents (PDFs, scans, LaTeX, WHO L1/L2 guidelines, etc.)
  from library/ into structured content objects. Handles OCR extraction,
  environment detection, structural analysis, and content-object generation.
  Supports multi-stage pipelines: raw upload → extracted text → structured
  blocks → .ts/.md content objects.
allowed-tools: Read Write Edit Bash Grep Glob Agent WebFetch
---

# Document Intake

> **Bib human-review integration (2026-06-09).** Track per-upload ingestion
> status in `library/intake.json` (identified passage, formalised?, matched?) and
> link each upload to the `references.ts` entry it sources. An upload that
> supplies a cited source moves that ref to `source-in-repo` (agent-identified
> passage; no human photo) and then through the
> [`local/bib-human-review`](bib-human-review.md) ladder to `validated`. Existing
> `library/` follow the same agent-sourced path (design §5).

> **Per-upload state now lives in the source ledger (2026-08-08).** The
> `library/<id>/intake.json` convention below covers 1 of the corpus's 284
> documents; the per-document row — reference join, examination status, and
> relevance verdict — is now
> `content/bib-qa-verifications.json` (`source-ledger/v1`), populated by
> [`local/paper-relevance-triage`](paper-relevance-triage.md). Use the ledger
> for "what is this document, is it cited, does it matter"; keep `intake.json`
> for the multi-stage *extraction* state of a document actually being
> converted (OCR → blocks → content objects). Do not record a title, author,
> or year in the ledger — bibliographic metadata belongs in
> `content/schema/references.ts` alone.

## Overview

This skill manages the `library/` directory as an intake pipeline for
converting raw documents into structured content objects. It handles:

1. **Scanned PDFs / images** — OCR extraction → text → blocks
2. **LaTeX source** — environment extraction → blocks
3. **WHO L1 → L2 guidelines** — normative structure → blocks
4. **arXiv papers** — fetched source → blocks (delegates to paper-importer)
5. **Arbitrary documents** — best-effort structural analysis

The key distinction from `paper-importer`: this skill owns the full
lifecycle of `library/`, including tracking processing state, partial
extractions, and multi-pass refinement. Paper-importer focuses on the
final content-object generation step.

## When to Use This Skill

- User says "upload", "scan", "process document", "intake"
- User drops a file into `library/`
- User mentions WHO, L1, L2, guideline, normative
- User wants to convert a raw document into content objects
- Files appear in `library/` that haven't been processed yet

## library/ Directory Convention

```
library/
  <document-id>/
    intake.json                  ← processing state + metadata
    original.pdf                 ← raw upload (PDF, scan, etc.)
    original.tex                 ← or LaTeX source
    extracted-text.md            ← OCR or parser output (intermediate)
    extracted-blocks.json        ← structured extraction (intermediate)
    mapping.json                 ← label/section mapping decisions
    README.md                    ← human notes about the document
```

### intake.json schema

```json
{
  "id": "who-anc-2016",
  "title": "WHO Recommendations on Antenatal Care",
  "source": {
    "type": "pdf",
    "url": "https://...",
    "fetchedAt": "2026-03-25T..."
  },
  "format": "pdf|latex|scan|html|docx",
  "pipeline": {
    "stage": "uploaded|extracted|structured|mapped|generated",
    "extractedAt": null,
    "structuredAt": null,
    "generatedAt": null,
    "errors": []
  },
  "classification": {
    "type": "guideline|paper|report|standard",
    "domain": "health|physics|math|...",
    "normativeLevel": "L1|L2|L3|null"
  },
  "chapters": [],
  "blockCount": 0,
  "targetPaper": "content/<paper-id>/"
}
```

## Pipeline Stages

### Stage 1: Upload (→ `uploaded`)

Place raw files in `library/<document-id>/`. Create `intake.json`
with source metadata. Files are committed to git for reproducibility.

Supported formats:
- **PDF** — academic papers, scanned guidelines, reports
- **LaTeX** — `.tex` source bundles
- **HTML** — web-published guidelines, standards
- **DOCX** — Word documents (WHO often distributes as Word)
- **Images** — scanned pages (PNG, JPG, TIFF)

**For academic papers, prefer the MCP fetch path** (added 2026-05-22):
when the session network allows the upstream host, use
`paper-search-mcp` (arxiv / PubMed / bioRxiv / medRxiv) or
`openalex-paper-search` (alex-mcp; OpenAlex catalog) rather than
`curl`/`WebFetch`. The MCP tools return canonical metadata and the
PDF in one call, eliminating the OCR-then-extract-then-name dance.
See [`paper-importer.md §Phase 1`](paper-importer.md#phase-1-acquisition)
for the per-tool routing table. Sandboxed Claude-Code-on-the-web
sessions (github-only allowlist) cannot reach those hosts; in
those sessions, queue the fetch onto a normal-network machine
per [`bib-qa.md §Batch intake pipeline`](bib-qa.md#batch-intake-pipeline).

### Stage 2: Extraction (→ `extracted`)

Convert raw format to `extracted-text.md`:

| Format | Extraction method |
|--------|-------------------|
| PDF (text) | `pdftotext` or PDF.js |
| PDF (scan) | Tesseract OCR / Claude vision |
| LaTeX | Direct parse (strip preamble) |
| HTML | Readability + turndown |
| DOCX | Pandoc → markdown |
| Images | Claude vision API |

For scanned documents, use Claude's vision capability to extract
text with structural awareness (headings, lists, tables, boxes).

**Output**: `extracted-text.md` — raw markdown with preserved structure.

### Stage 3: Structural Analysis (→ `structured`)

Analyze extracted text for formal environments and document structure:

#### For academic papers:
Same as paper-importer Phase 2 — detect theorem/definition/lemma
environments, sections, cross-references.

#### For WHO guidelines (L1 → L2):
WHO guidelines have a specific normative structure:

| WHO element | Content block kind | Notes |
|------------|-------------------|-------|
| **Recommendation** (numbered, boxed) | `definition` | Normative statement |
| **Evidence summary** | `prose` | Supporting narrative |
| **Remarks** | `remark` | Implementation notes |
| **Good practice statement** | `proposition` | Consensus-based |
| **Research priority** | `conjecture` | Open questions |
| **Background** | `prose` | Context sections |
| **GRADE table** | `diagram` | Evidence quality |

**L1 vs L2**:
- **L1** = Recommendation (what to do) — maps to `definition` blocks
- **L2** = Implementation guidance (how to do it) — maps to `prose`
  blocks tagged `["implementation", "L2"]`

The structural analysis identifies these elements and maps them to
the content-object type system.

**Output**: `extracted-blocks.json` — array of detected blocks with
provisional kinds, titles, and content.

### Stage 4: Mapping (→ `mapped`)

Interactive step — present extracted blocks to user for review:

1. Show block count by kind
2. Let user rename, reclassify, skip, or merge blocks
3. Let user define chapter/section structure
4. Let user set the target paper ID
5. Generate `mapping.json` with confirmed decisions

### Stage 5: Content Generation (→ `generated`)

Generate content objects under `content/<paper-id>/`:

1. **`.ts` manifests** via `content/schema/builders.ts`
2. **`.md` content** in project markdown conventions
3. **Chapter `.ts` manifests** with section structure
4. **Paper `.ts` manifest** (new or updated)

Tag all generated blocks with:
```typescript
tags: ["imported", "source:<document-id>"]
```

Add `meta.source` referencing the upload:
```typescript
meta: {
  source: "library/<document-id>",
  originalSection: "3.2",
  importedAt: "2026-03-25T..."
}
```

## WHO-Specific Processing

### Detecting WHO guideline structure

WHO guidelines follow predictable patterns:

```
RECOMMENDATION N:
<recommendation text in bold/box>

Remarks:
- Implementation note 1
- Implementation note 2

Summary of evidence:
<narrative text>

GRADE table:
<quality assessment>
```

### Label conventions for guidelines

| Element | Label pattern | Example |
|---------|--------------|---------|
| Recommendation | `def:who-<guideline>-rec-<N>` | `def:who-anc-rec-1` |
| Evidence summary | `prose:who-<guideline>-evidence-<N>` | — |
| Remark | `rem:who-<guideline>-remark-<N>` | `rem:who-anc-remark-1` |
| Good practice | `prop:who-<guideline>-gps-<N>` | `prop:who-anc-gps-1` |
| Research priority | `conj:who-<guideline>-research-<N>` | `conj:who-anc-research-1` |

### Cross-referencing WHO recommendations

WHO recommendations often reference each other and external evidence.
Map these to `uses[]` in content objects:

```typescript
export default definition({
  label: "def:who-anc-rec-3",
  title: "Recommendation 3: Daily iron supplementation",
  uses: ["def:who-anc-rec-1"],  // references Rec 1
  tags: ["imported", "source:who-anc-2016", "L1", "normative"],
  meta: {
    source: "library/who-anc-2016",
    strength: "strong",
    quality: "moderate",
    gradeLevel: "⊕⊕⊕◯",
  }
});
```

## Integration with Other Skills

| Skill | Integration point |
|-------|-------------------|
| `paper-importer` | Delegates Phase 5 generation for academic papers |
| `content-validation` | Validates generated content objects |
| `editor` | Reviews generated narrative content |
| `scientific-accuracy` | Checks extracted statements |
| `ontologist` | Maps terminology to glossary |

## Resuming Partial Processing

The `intake.json` pipeline stage tracks where processing stopped.
To resume:

1. Read `intake.json` → check `pipeline.stage`
2. Skip completed stages
3. Continue from the current stage
4. Update `intake.json` after each stage

This allows multi-session processing of large documents.

## Checklist

Before marking intake complete:

- [ ] Raw files committed to `library/<document-id>/`
- [ ] `intake.json` has complete metadata
- [ ] `extracted-text.md` reviewed for OCR errors
- [ ] `extracted-blocks.json` reviewed and confirmed by user
- [ ] All content objects generated with correct builders
- [ ] Blocks tagged with `["imported", "source:<document-id>"]`
- [ ] Chapter/section structure matches document
- [ ] Cross-references mapped to `uses[]`
- [ ] `intake.json` stage set to `generated`
- [ ] Content validation passes (`content_validate`)
