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
| 5 | `has_screenshot` | ✓     | Screenshot exists in `content/bib-qa-images/<id>.*` |
| 6 | `has_local_pdf`  | ✓     | Full paper PDF / data file present at `uploads/<id>*.{pdf,txt}` for offline verification (added 2026-05-19) |

\* ✓* = automated but requires `--check-urls` flag (makes network requests).

Each tag resolves to `pass`, `fail`, `warn`, or `unchecked`.
The **score** (0–6) is the count of passing tags.

### Intake & local evidence (new — `uploads/` workflow)

The `uploads/` directory holds full-paper PDFs and data tables for
offline verification of citation correctness. Once a paper is in
`uploads/`, the `has_local_pdf` tag passes, and reviewers can verify:

- That the `-- Ref: [<id>]` comment's free-text description (e.g.
  "Theorem 3.2 (Pieri rule for SYT)") actually matches the cited
  paper's content,
- That the entry's `title`, `author`, `issued.year` resolve to the
  same work the .lean comments describe (catches the Copilot-flagged
  wrong-work mismatches like `borel1986` → Borel-Wallach vs the cited
  Borel-Zagier).

#### Batch intake pipeline

| Tool | Purpose |
|------|---------|
| `scripts/gen-bib-papers-list.py` | Scan `content/schema/references.ts` for entries with publicly-downloadable URLs (arxiv, numdam, archive.org, OEIS, faculty pages); emit `scripts/bib-papers-list.txt` |
| `scripts/bib-papers-list.txt` | Generated list, one entry per line: `<url>\|<target>\|<description>` |
| `scripts/upload-bib-papers.sh` | Read the list, download each file (idempotent by file existence), commit per-paper to a fresh `claude/upload-bib-papers-<utc-ymd>` branch via SSH; optional `--pr` to auto-open PR |
| `scripts/upload-to-uploads.sh` | Single-file intake for ad-hoc additions (manual sources, scans, WHO guidelines etc.) |

Run from any clone with network access:

```bash
python3 scripts/gen-bib-papers-list.py     # regenerate the list
bash scripts/upload-bib-papers.sh --dry-run # preview
bash scripts/upload-bib-papers.sh --pr      # download + commit + push + open PR
```

The script uses `git push --force-with-lease` so re-runs after a fix
(URL pattern update, etc.) cleanly replace the prior branch tip
without manual force-push intervention.

#### `validate-bib` — comprehensive correctness audit

`content/pipeline/validate-bib.ts` is the umbrella correctness audit
(complement to `validate-refs` which is just key-resolution). Five
selectable modes:

| Flag | Mode | Network? |
|------|------|---------|
| `--doi` | HEAD/GET each DOI via doi.org with proper User-Agent; expect 301/302 (success redirect) or 200; warn on 4xx/5xx | ✓ doi.org |
| `--cross-check` | Parse `-- Ref: [<id>] <desc>` comments in .lean files; warn when neither the entry's author surname nor any significant title word appears in the description | ✗ |
| `--crossref` | Fetch `api.crossref.org/works/<DOI>` per entry; compare canonical title/author/year against the entry | ✓ api.crossref.org |
| `--arxiv` | Resolve arxiv.org URLs for entries whose URL field is on arxiv.org | ✓ arxiv.org |
| `--pandoc` | Pipe a sample LaTeX citation through pandoc-citeproc; verify the rendered output is well-formed (catches missing CSL fields) | ✗ (needs pandoc binary) |
| `--all` | Run all five | ✓ |
| `--strict` | Exit non-zero on any failure (default: warn-only) | n/a |

Network requirement: `--doi` / `--crossref` / `--arxiv` modes need
outbound HTTPS to doi.org / api.crossref.org / arxiv.org respectively.
Sandboxed environments with whitelist-only egress (Claude Code on
the web, some CI runners) cannot run these — the script reports
uniform 403s and the bib remains genuinely unvalidated. Run from a
normal-network machine.

The `--cross-check` heuristic was iterated v1→v4 to drop false-positive
rate from 149→25 (the remaining 25 warnings are mostly Ref descriptions
that name a theorem/section number without an author or title anchor).
Heuristic parameters (5-word prose threshold, 4-char title-word
threshold, stopword list) are documented inline in `validate-bib.ts`.

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
  pipeline/bib-qa.ts          ← QA pipeline script (5-tag pass/fail)
  pipeline/validate-bib.ts    ← Comprehensive correctness audit
                                (--doi / --cross-check / --crossref /
                                --arxiv / --pandoc)
  pipeline/validate-references.ts  ← Key-resolution + citation cross-check
  bib-qa.json                 ← Generated QA report (gitignored)
  bib-qa-images/              ← Screenshot evidence
    <refid>.png               ← Named by reference id
    <refid>-1.png             ← Multiple images per reference
uploads/                      ← Full-paper PDFs / data tables for
                                offline citation verification.
  <id>.pdf                    ← One file per cited paper (where
                                publicly downloadable)
  *.mas20.txt                 ← Numerical data tables (AME 2020, etc.)
scripts/
  gen-bib-papers-list.py      ← Scan references.ts → bib-papers-list.txt
  bib-papers-list.txt         ← Generated batch-intake list
  upload-bib-papers.sh        ← Batch download → commit-per-paper →
                                SSH push → optional gh pr create
  upload-to-uploads.sh        ← Single-file intake (ad-hoc additions)
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
2. **DOI**: Include if available (validates format automatically;
   `validate-bib --doi` confirms it resolves)
3. **URL**: Include direct link to article page (prefer arxiv,
   numdam, archive.org, or faculty pages — these are the patterns
   `gen-bib-papers-list.py` can auto-extract for intake)
4. **Run QA**: `cd content && bun run pipeline/bib-qa.ts`
5. **Cross-check description**: When adding `-- Ref: [<id>] <desc>`
   to a .lean file, include the author surname or a significant title
   word in `<desc>` so `validate-bib --cross-check` confirms the
   description anchors the entry. Bare theorem/section refs
   ("Theorem 3.2") will warn; ideally write
   "Smith, Theorem 3.2 — uniqueness of …".
6. **Run validate-bib**: `cd content && bun run validate-bib --cross-check`
   to confirm no anchor mismatch; pair with `--strict` in CI.
7. **Local PDF intake** (optional but recommended for theorem-citing
   references): add the paper to `scripts/bib-papers-list.txt` or
   place the PDF in `uploads/<id>.pdf` directly via
   `bash scripts/upload-to-uploads.sh <url-or-local-path>`.
8. **Screenshot** (Optional): For theorem/result citations, capture
   the relevant page to `content/bib-qa-images/<id>.png`.
9. **Cross-check citation site**: Ensure `\cite{<id>}` appears in
   the relevant `.md` file or `-- Ref: [<id>]` in the relevant
   `.lean` file.

## Investigating wrong-work resolutions

When `validate-bib --cross-check` or a code reviewer (e.g. Copilot)
flags an entry's metadata as not matching the .lean citation comment,
the canonical workflow is:

1. **Confirm by inspecting `uploads/<id>.pdf`** if present:
   `file uploads/<id>.pdf` → real PDFs report "PDF document, version X.X";
   landing pages report "HTML document". HTML files are likely intake
   failures (numdam landing pages, NIST CGI lookups etc.).
2. **For HTML landing pages**: update the URL-pattern logic in
   `scripts/gen-bib-papers-list.py` (e.g. numdam.org/item/<id>/ →
   /item/<id>.pdf), regenerate `bib-papers-list.txt`, delete the
   broken `uploads/<id>.pdf`, re-run `upload-bib-papers.sh`.
3. **For wrong-work resolution** (entry metadata names a different
   paper than the .lean comment intends): two options —
     a. Update the entry's `title` / `author` / `DOI` / `issued` to
        match the cited work (.lean comment is canonical), or
     b. Split the key into `<id>a` and `<id>b` and update each .lean
        citation site to use the right variant.
   This is an author-judgement call; the bib QA agent should propose
   a resolution but defer the choice via `AskUserQuestion`.

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
