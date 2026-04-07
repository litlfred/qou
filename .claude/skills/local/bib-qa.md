---
name: bib-qa
roles: [reader, collaborator, owner]
description: >
  Bibliography quality-assurance agent — validates every reference in
  content/schema/references.ts against five QA checks: URL availability,
  URL resolution, metadata completeness, citation coverage, and
  screenshot/image evidence.  Generates bib-qa.json consumed by the
  standalone bib-qa.html dashboard.
allowed-tools: Read Write Edit Bash Grep Glob WebFetch Agent
---

# Bibliography QA Skill

## Purpose

Ensure every entry in the bibliography (`content/schema/references.ts`)
is well-formed, reachable, accurately cited, and backed by evidence.
The skill operates at two levels:

1. **Automated pipeline** — `bun run pipeline/bib-qa.ts` evaluates five
   machine-checkable tags per reference.
2. **Agent-assisted review** — when invoked by a collaborator or during
   QC, the agent performs deeper checks that require network access or
   content understanding.

## QA Tags (per reference)

| # | Tag              | Auto? | Description |
|---|------------------|-------|-------------|
| 1 | `has_url`        | ✓     | Entry has a URL or DOI-derived URL |
| 2 | `url_resolves`   | ✓*    | URL responds with HTTP 2xx AND page contains expected title/author (`--check-urls` flag) |
| 3 | `metadata_ok`    | ✓     | Title, author(s), year present; type-specific fields complete |
| 4 | `cited_in_paper` | ✓     | Referenced by `\cite{}` in .md/.tex or `-- Ref:` in .lean |
| 5 | `has_screenshot`  | ✓     | Screenshot exists in `content/bib-qa-images/<id>.*` |

\* ✓* = automated but requires `--check-urls` flag (makes network requests).

Each tag resolves to `pass`, `fail`, `warn`, or `unchecked`.
The **score** (0–5) is the count of passing tags.

## When to Invoke

- User says "validate bibliography", "check references", "bib QA"
- During QC review of a chapter or the full paper
- When authoring: adding a new `ref()` entry to `references.ts`
- Before submission / publication readiness checks

## Workflow

### 1. Generate the QA report

```bash
cd content && bun run pipeline/bib-qa.ts
# → writes content/bib-qa.json

# With URL checking (slower, needs network):
cd content && bun run pipeline/bib-qa.ts --check-urls
```

### 2. Review the dashboard

Open `folio-assistant/ui/bib-qa.html` in a browser (served at
`/folio/bib-qa.html` when the folio server is running).  The page
loads `bib-qa.json` and displays:

- Summary cards (total, clean, warning, failing)
- Filterable/searchable reference list
- Per-reference detail panel with QA tags, metadata, citations, and images
- Lightbox for screenshot viewing

### 3. Fix issues (agent workflow)

For each failing reference, the agent should:

1. **Missing URL**: Search for the article DOI or URL.  Use `WebFetch`
   to verify the URL loads.  Update `references.ts` with the URL/DOI.

2. **URL does not resolve**: Check if the DOI has changed.  Try
   `https://doi.org/<DOI>` and common publisher patterns.  Update if
   the canonical URL has moved.

3. **Incomplete metadata**: Fill in missing fields (authors, year,
   journal, publisher) from the article page or CrossRef API:
   `https://api.crossref.org/works/<DOI>`

4. **Uncited reference**: Determine if the reference is used somewhere
   not yet scanned (e.g., a comment, a proof sketch).  If genuinely
   orphaned, flag for author review — do NOT delete without consent.

5. **Missing screenshot**: For references where the cited result
   (theorem, figure, table) is critical to the paper's argument,
   capture a screenshot of the relevant page/result and save it to
   `content/bib-qa-images/<refid>.png` (or `.jpg`, `.pdf`).
   Multiple images: `<refid>-1.png`, `<refid>-2.png`.

### 4. Re-run and verify

```bash
cd content && bun run pipeline/bib-qa.ts --check-urls
```

All references should score ≥ 4/5 (screenshot is optional for
non-critical references).

## File Layout

```
content/
  schema/references.ts        ← Bibliography source of truth (CSL-JSON)
  pipeline/bib-qa.ts          ← QA pipeline script
  bib-qa.json                 ← Generated QA report (gitignored)
  bib-qa-images/              ← Screenshot evidence
    <refid>.png               ← Named by reference id
    <refid>-1.png             ← Multiple images per reference
folio-assistant/
  ui/bib-qa.html              ← Standalone QA dashboard
```

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `scientific-accuracy` | Bib-QA runs as part of formalization cross-reference checks |
| `editor` | When adding `\cite{}` to content, verify the reference exists and passes QA |
| `content-validation` | The `uses-resolve` constraint validates `\cite{}` keys; bib-qa adds deeper checks |
| `todo-review` | Low-scoring references can generate TodoItems for the author |

## Adding a New Reference (checklist)

When authoring adds a `ref()` entry:

1. **Required fields**: `id`, `type`, `title`, `author`, `issued`
2. **DOI**: Include if available (validates format automatically)
3. **URL**: Include direct link to article page
4. **Run QA**: `cd content && bun run pipeline/bib-qa.ts`
5. **Screenshot**: For theorem/result citations, capture the relevant page
6. **Cross-check**: Ensure `\cite{<id>}` appears in the relevant `.md` file

## Output Format

The `bib-qa.json` schema:

```json
{
  "generated": "2026-04-07T...",
  "totalRefs": 101,
  "summary": { "pass": 380, "warn": 45, "fail": 12, "unchecked": 68 },
  "entries": [
    {
      "id": "einstein1905",
      "type": "article-journal",
      "title": "...",
      "authors": "Albert Einstein",
      "year": "1905",
      "url": "https://doi.org/...",
      "doi": "10.1002/...",
      "journal": "Annalen der Physik",
      "tags": [
        { "key": "has_url", "label": "Has URL", "status": "pass", "detail": "..." },
        ...
      ],
      "citedIn": ["content/.../relativity.md"],
      "images": ["bib-qa-images/einstein1905.png"],
      "score": 5
    }
  ]
}
```
