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
| 6 | `has_local_pdf`  | ✓     | Full paper PDF / data file present at `library/<id>*.{pdf,txt}` for offline verification (added 2026-05-19) |
| 7 | `verification_status` | ✓ | Per-paper verification record exists in `content/bib-qa-verifications.json` with status ∈ {`verified-clean`, `partial`, `fixed`}. Pending/uncited/unfetchable/paper-mismatch all warn. (added 2026-05-19) |

\* ✓* = automated but requires `--check-urls` flag (makes network requests).

Each tag resolves to `pass`, `fail`, `warn`, or `unchecked`.
The **score** (0–7) is the count of passing tags.

### Verification status model (`bib-qa-verifications.json`)

`content/bib-qa-verifications.json` is the hand-curated sidecar
recording per-paper verification metadata. Loaded by `bib-qa.ts`
and surfaced both as the `verification_status` QA tag (#7) and in
each entry's `.verification` field of `bib-qa.json` (which
flows through to the standalone `bib-qa.html` dashboard).

Verification is orthogonal to bibliographic correctness —
"verified" means **someone has read the PDF and confirmed the
citation sites' descriptions match the cited paper's content**:

```json
{
  "entries": [
    {
      "id": "boyd-vandenberghe-2004",
      "status": "partial",
      "local_pdf": "library/boyd-vandenberghe-2004-convex-optimization.pdf",
      "verified_at": "2026-05-19T05:50:00Z",
      "verified_by": "Claude (claude-opus-4-7)",
      "fixes_applied": 4,
      "fix_commit": "66b3caf7f",
      "note": "§5.5.3→§5.5.2, ..."
    }
  ]
}
```

Status values: `pending` (not yet examined), `verified-clean`
(every citation site checked, no fix needed), `partial` (some
sites verified + fixed, others remain), `fixed` (misattributions
resolved), `pending-placement` (added 2026-05-19 — author wants to
keep the reference but hasn't decided where to cite it yet; tag
passes the verification_status QA check), `uncited` (bib entry
has zero consumers AND author hasn't claimed it; decision
pending), `paper-mismatch` (local PDF ≠ references.ts metadata;
escalate), `unfetchable` (not in `library/`).

The distinction `pending-placement` vs `uncited` matters: both
have 0 citation sites, but `pending-placement` says "keep this
entry, I'll find a citation site later" while `uncited` says
"unclaimed orphan — may be removable". Author triage moves
entries from `uncited` → `pending-placement` (or
`verified-clean` if a citation gets added in the same triage).

The `verification_status` tag passes for `verified-clean` /
`partial` / `fixed`, warns for `pending` / `uncited` /
`unfetchable`, and fails for `paper-mismatch`.

When verifying a paper:
1. Update the entry's `status`, `verified_at`, `verified_by`,
   `fixes_applied`, `fix_commit` in
   `content/bib-qa-verifications.json`.
2. Append a row to the markdown ledger's "Verification log" table
   (`docs/coordination/<date>-bib-verification-ledger.md`).
3. Commit both files alongside any `-- Ref:` fixes (one commit
   per paper is the suggested granularity).
4. Re-run `cd content && bun run pipeline/bib-qa.ts` to regenerate
   `bib-qa.json` (gitignored — but useful for the dashboard).

### Intake & local evidence (new — `library/` workflow)

The `library/` directory holds full-paper PDFs and data tables for
offline verification of citation correctness. Once a paper is in
`library/`, the `has_local_pdf` tag passes, and reviewers can verify:

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

#### MCP services for intake + reaudit (added 2026-05-22)

`.mcp.json` ships two paper/scholar MCP servers that the bib-QA
agent should leverage when they are live (i.e. the session's
network policy allows `arxiv.org` / `api.openalex.org`). The
servers fail soft in sandboxed Claude-Code-on-the-web sessions
whose allowlist only permits `github.com` — in those sessions,
fall back to the offline pipeline above and hand the download
step to a normal-network machine.

| Server (`.mcp.json` key) | Package | Tools (most useful) | Use for |
|--------------------------|---------|---------------------|---------|
| `paper-search-mcp` | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | `search_arxiv`, `search_pubmed`, `search_biorxiv`, `search_medrxiv`, `search_google_scholar`, `download_arxiv`, `read_arxiv_paper` | Find arxiv preprints by title for URL-missing entries; bulk-download to `library/`; pull parsed paper text for `validate-bib --cross-check` cross-references |
| `openalex-paper-search` | [drAbreu/alex-mcp](https://github.com/drAbreu/alex-mcp)@4.1.0 | OpenAlex `get_work`, `search_works`, `get_work_citations`, `get_work_references`, author disambiguation | Fill metadata gaps for the 9 no-arxiv-URL DOI refs (canonical title/author/year/venue); resolve wrong-work mismatches via author IDs (e.g. `leitnerpawloski2004` PL-inner-product split); citation-network mapping |

(Notes: the legacy `mcp-scholar` entry in `.mcp.json` was removed
on 2026-05-22 — it's broken at every PyPI version against modern
FastMCP. Use `paper-search-mcp.search_google_scholar` instead.
See [`docs/coordination/2026-05-22-mcp-paper-search-services.md`](../../../docs/coordination/2026-05-22-mcp-paper-search-services.md)
for the design rationale and per-server feature matrix.)

**Workflows that gain leverage from these servers**

1. **URL backfill for the 37 no-URL entries** (offline-prep,
   network-only step is the actual fetch):

   ```python
   # Pseudo-code; run from a session with arxiv.org allowed.
   for entry in references.ts where entry.url is None and entry.type in {"article-journal","article"}:
     hits = paper_search_mcp.search_arxiv(query=entry.title, max_results=3)
     if best_match(hits, entry).confidence > 0.8:
       propose entry.url = hits[0].url   # human reviewer accepts
   ```

2. **Verification cross-check** — for any entry in
   `bib-qa-verifications.json` whose status is `partial` or
   `pending`, `read_arxiv_paper(arxiv_id)` returns the parsed
   body. Grep the cited `-- Ref: [<id>] <description>` keywords
   against that body to confirm the description anchors a real
   passage. Beats opening the PDF in a viewer.

3. **Author-ID-based wrong-work resolution** — when a single
   bib key citation-splits across two unrelated works (the
   leitnerpawloski2004 PL-inner-product mismatch is the
   canonical example), OpenAlex author IDs cleanly disambiguate
   "Pawlowski-Leitner-arXiv-math/0409565" from
   "Pawlowski-thesis-or-other-paper".

4. **Metadata enrichment for paywalled entries** — for the 141
   doi.org URLs we can't fetch, `alex-mcp.get_work(doi=…)`
   returns canonical title/author/year/venue without paywall.
   Useful for filling `references.ts` gaps without ever
   downloading the PDF.

**When the new MCP services are NOT available**: drop back to the
offline pipeline (`gen-bib-papers-list.py` + `upload-bib-papers.sh`
on a normal-network machine). The new services are an
accelerator, not a replacement.

**Local CLI wrapper for both paths** (added 2026-05-22):
[`scripts/bib-mcp-cli.py`](../../../scripts/bib-mcp-cli.py) drives
the same `paper-search-mcp` / `pyalex` libraries as a normal Python
CLI — no MCP server needed. Designed to run from a normal-network
machine when the Claude-Code-on-the-web allowlist blocks
arxiv/openalex/scholar:

```bash
# Prereqs (one-time):
pip install paper-search-mcp pyalex
pip install playwright && playwright install chromium  # for scholar-snapshot

# Status — probes network, lists what's possible:
scripts/bib-mcp-cli.py status

# Backfill URLs for the 37 no-URL entries (dry-run by default):
scripts/bib-mcp-cli.py backfill-urls          # propose
scripts/bib-mcp-cli.py backfill-urls --apply  # write to references.ts

# Download missing arxiv PDFs:
scripts/bib-mcp-cli.py download --apply

# Enrich DOI-only entries with OpenAlex canonical metadata:
scripts/bib-mcp-cli.py enrich-doi --apply

# Capture HTTP 'as-viewed-on' evidence pages (HTML/PDF + SHA-256):
scripts/bib-mcp-cli.py snapshot --apply

# Capture Google Scholar / Books preview PDFs via headless Chromium:
scripts/bib-mcp-cli.py scholar-snapshot --apply

# Run all of the above in dry-run mode:
scripts/bib-mcp-cli.py audit
```

Each subcommand is idempotent: re-running skips entries already
done. Network probes fail-fast with a friendly error when the
required host is in the deny-list. The `snapshot` /
`scholar-snapshot` outputs land in `content/bib-qa-evidence/<refid>/`
as `<utc>-<source>.{html,pdf}` + `<utc>-<source>.meta.json` (the
"as-viewed-on" provenance record) — humans can review the
snapshot to validate the citation without re-fetching.

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
library/                      ← Full-paper PDFs / data tables for
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
   place the PDF in `library/<id>.pdf` directly via
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

1. **Confirm by inspecting `library/<id>.pdf`** if present:
   `file library/<id>.pdf` → real PDFs report "PDF document, version X.X";
   landing pages report "HTML document". HTML files are likely intake
   failures (numdam landing pages, NIST CGI lookups etc.).
2. **For HTML landing pages**: update the URL-pattern logic in
   `scripts/gen-bib-papers-list.py` (e.g. numdam.org/item/<id>/ →
   /item/<id>.pdf), regenerate `bib-papers-list.txt`, delete the
   broken `library/<id>.pdf`, re-run `upload-bib-papers.sh`.
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

## Verification status rendered in PDF/HTML (added 2026-05-19)

The bib-qa-verifications.json status surfaces in the rendered
bibliography (PDF + HTML) via the `annotation` field in
`references.bib`:

  @book{boyd-vandenberghe-2004,
    author     = {...},
    title      = {{Convex Optimization}},
    annotation = {[Verified+Fixed] 18 fixes by Claude (claude-opus-4-7) 2026-05-19},
  }

`content/pipeline/export-bibtex.ts` reads
`content/bib-qa-verifications.json` at export time and injects a
short status marker per entry. Format:

  [<status-symbol>] [<N fixes>] [by <verifier>] [<date>]

Status symbols:
  [Verified]        — verified-clean (every site checked, no fix)
  [Verified+Fixed]  — fixed (misattributions resolved)
  [Partial]         — partial (some sites verified + fixed)
  [Pending]         — pending (not yet examined)
  [Uncited]         — bib orphan (no QOU citations)
  [Paper-Mismatch]  — local PDF ≠ bib metadata
  [Unfetchable]     — not in library/

Rendering targets:
- **LaTeX/biblatex**: the `annotation` field renders via
  `\printfield[brackets]{annotation}` in custom styles, or
  `\bibliographystyle{plainnat-annote}` for natbib.
- **Pandoc HTML**: CSL templates that include the `annote` field
  display it inline; some styles render it as a separate
  paragraph.
- **bib-qa.html dashboard**: already surfaces the full
  `verification` object from `bib-qa.json` (typed sidecar).

When adding new entries or updating verification status, regen
both:

  cd content
  bun run export-bibtex   # → references.bib with annotations
  bun run pipeline/bib-qa.ts   # → bib-qa.json for dashboard

## Always cross-check arxiv for mirror preprints (added 2026-05-19)

When verifying a published-journal paper, always check arxiv.org for
a freely-accessible mirror. Most math/physics authors deposit the
preprint version to arxiv either before or after journal publication.
The mirror URL is the right intake target for `library/` because:

- arxiv mirrors are stable + freely-accessible (no doi.org paywall).
- Content is usually the same as the published version (modulo
  copy-editing differences in section numbering).
- `gen-bib-papers-list.py` already handles `arxiv.org/abs/<id>` →
  `arxiv.org/pdf/<id>` conversion automatically.

Workflow when adding/auditing an entry whose primary URL is a
publisher landing page (doi.org, journal site, etc.):

1. Search the paper title on https://arxiv.org for an `arXiv:<id>`
   preprint by the same authors.
2. If found, add `URL: https://arxiv.org/abs/<id>` to the
   `references.ts` entry (alongside, not instead of, the DOI).
3. The auto-extracted batch intake will then pick up the arxiv URL
   automatically on next regen.

Verified arxiv-mirror finds during the 2026-05-19 22-paper batch:
`faddeev_kashaev1994` (hep-th/9310070), `baez2004` (math/0307200),
`hu-mathas2012graded` (1008.1462), `freed2010` (0905.0731),
`berarducci-mantova2018` (1503.00315), `yekutieli2008` (0801.3233),
`leitnerpawloski2004` (math/0409565), `bilson-thompson2005` (hep-ph/0503213),
`bufetov2020` (2003.02730), `blitvic2012` (1205.4003),
`finster2021/2022/2024` + `dappiaggi2024` (all arxiv-natives).

## Paper-mismatch class: PDF resolves to wrong content (added 2026-05-19)

A failure mode surfaced during the 2026-05-19 batch: the
`gen-bib-papers-list.py` URL converter can yield a syntactically-valid
PDF that contains the WRONG content. Two cases observed:

- **numdam volume prelims**: `numdam.org/item/AST_YYYY__VOL__R1_0/`
  resolves to the volume's PRELIMINARY PAGES (front matter, pp. I-XII),
  NOT a specific Astérisque chapter. The per-chapter URL pattern is
  `/item/AST_YYYY__VOL__<startpage>_0/` — different starting page per
  chapter. (Discovered for `zink2002` — got volume 278 prelims instead
  of Zink's "Display of a Formal p-Divisible Group" chapter.)

- **archive.org filename guess**: `archive.org/download/<id>/<id>.pdf`
  works only when the PDF filename inside the item matches the item
  id. For re-digitised scans where the upload was named differently
  (`<id>_bw.pdf`, `<id>_text.pdf`, an arbitrary stem), the guess
  fails with 401/503/404. The reliable fix is to consult
  `archive.org/metadata/<id>` JSON to discover the actual PDF filename
  — deferred to a future `gen-bib-papers-list.py` improvement.

Detection workflow:

1. `pdftotext -layout -f 1 -l 1 library/<id>.pdf` and inspect the
   title page.
2. Compare the title page to the `references.ts` entry's `title` field.
3. If they disagree, mark the entry as `paper-mismatch` in
   `content/bib-qa-verifications.json` with a note explaining the
   downloaded content vs the expected content.
4. The `references.ts` URL itself usually needs the fix (not the
   entry's bib metadata); update the URL and re-run
   `upload-bib-papers.sh` to fetch the correct file.

## Cross-citation-content verification workflow (added 2026-05-19)

When verifying a paper against its QOU citation sites, the canonical
procedure (per the 2026-05-19 batch experience):

1. **Extract the PDF** from the upload branch:
   `git show origin/claude/upload-bib-papers-<date>:library/<file> > /tmp/<id>.pdf`.
2. **Read the title page** (`pdftotext -layout -f 1 -l 1`) — confirm
   the local PDF matches the `references.ts` entry's `title`.
3. **Read the section list** (`pdftotext -layout` + grep for
   `^[0-9]+\.\s+[A-Z]` or `^Section`) — identify the chapters /
   subsections cited in QOU.
4. **For each citation site** (`-- Ref: [<id>]` line in `.lean` or
   `\cite{<id>}` in `.md`): read the surrounding code/prose to find
   the specific claim being attributed, then verify the paper covers
   that claim. Common types:
     - **Title/scope match**: paper title or §N heading verbatim
       matches the citation text → verified-clean.
     - **§N misattribution**: paper has §N but it covers a different
       topic than the citation says (the boyd §5.5.3 case) → fix the
       § number in the citation.
     - **Wrong work**: paper covers a different topic entirely (the
       leitnerpawloski2004 inner-product case) → flag as partial /
       paper-mismatch; defer to author judgement.
5. **Update both**: `content/bib-qa-verifications.json` status +
   `docs/coordination/<date>-bib-verification-ledger.md` log row.
6. **Commit** per-paper (granular history); the
   `local/bib-qa` skill picks up the new status on next `bib-qa.ts`
   run.

Skill outputs:
- `bib-qa.json` (gitignored, regenerated via
  `cd content && bun run pipeline/bib-qa.ts`) carries the
  `verification` field on each entry, including `status`,
  `verified_at`, `verified_by`, `fixes_applied`, `fix_commit`, `note`.
- The `verification_status` QA tag passes for verified-clean /
  partial / fixed; warns for pending / uncited / unfetchable; fails
  for paper-mismatch.
