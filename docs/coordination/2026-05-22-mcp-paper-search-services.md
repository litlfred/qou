# MCP paper-search services — features, status, integration with bib-qa

**Date:** 2026-05-22
**Branch:** `claude/cool-newton-JXanC`
**Triggering request:** "new MCP services related to arxiv, scholar,
bibliography. review features and see what we can do."

## TL;DR

Three new MCP servers are configured in `.mcp.json`. As-shipped, **two
of three failed to start** — fixed in this branch. Even fixed, **PDF
download paths are blocked by the Claude-Code-on-the-web network
allowlist** (only `github.com` is reachable from this environment), so
the actual paper intake still has to run from a normal-network machine
via `scripts/upload-bib-papers.sh` (existing infra). The new servers
become useful for **online metadata enrichment + reaudit** when the
network policy is relaxed.

## The three configured servers

| `.mcp.json` key | Package | Status as shipped | Fix applied |
|------------------|---------|-------------------|-------------|
| `paper-search-mcp` | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | **broken**: bare `uvx paper-search-mcp` errors "Package provides no executables" | use `uvx --from paper-search-mcp python -m paper_search_mcp.server` |
| `openalex-paper-search` | (none — package name is wrong) | **broken**: `openalex-mcp-server` does not exist on PyPI | swap to `alex-mcp` (drAbreu, OpenAlex API client) via `uvx --from git+https://github.com/drAbreu/alex-mcp.git@4.1.0 alex-mcp` |
| `mcp-scholar` | [renyumeng1/mcp_scholar](https://pypi.org/project/mcp-scholar/) | **broken at every PyPI version (0.1.7 – 0.2.0)**: `FastMCP.__init__()` rejects `verbose=` since FastMCP 2.x. No working version pin found. | removed entry — `paper-search-mcp.search_google_scholar` covers the same use case |

Result: two working servers (`paper-search-mcp`, `openalex-paper-search`
via alex-mcp) once the next session reconnects MCP after the
`.mcp.json` change.

## Features once live

### `paper-search-mcp` (13 tools)

```
search_arxiv         search_pubmed       search_biorxiv
search_medrxiv       search_google_scholar
download_arxiv       download_pubmed     download_biorxiv
download_medrxiv
read_arxiv_paper     read_pubmed_paper   read_biorxiv_paper
read_medrxiv_paper
```

Each `search_*` returns title, authors, abstract, year, DOI/URL.
Each `download_*` writes a PDF to a target directory. Each `read_*`
returns the parsed text body.

**Most useful for bib-qa:**
- `search_arxiv("<title>")` — for the **37 references that currently
  lack a URL** in `references.ts`, find their arxiv preprint (where
  one exists) and add `url: "https://arxiv.org/abs/..."` to the entry.
- `download_arxiv("<arxiv-id>", "library/")` — bulk-fetch the 36
  arxiv preprints still missing from `library/` (see
  `scripts/bib-papers-list.txt` for the canonical list).
- `read_arxiv_paper("<arxiv-id>")` — pull the parsed body for
  cross-check verification (`validate-bib --cross-check`): does the
  `-- Ref: [<id>] <description>` text actually match the paper?

### `openalex-paper-search` (via `alex-mcp`)

[OpenAlex](https://openalex.org) is a free 270M-publication catalog
with author disambiguation, ORCID resolution, citation networks, and
institution metadata. Most useful for bib-qa:

- **Metadata completeness** — for the 9 references with no arxiv URL
  but a DOI, OpenAlex's `get_work` returns the canonical title /
  author / year / journal / venue, ideal for filling
  `references.ts` gaps.
- **Citation network mapping** — `get_work_citations` / `get_work_references`
  for the in-paper provenance graph (which works cite ours / which works
  we should cite).
- **Author disambiguation** — useful for the leitnerpawloski2004
  case (the QOU bib cites this for **two unrelated works** under the
  same key; OpenAlex author IDs would split them cleanly).

## What this branch does

1. **Fixed `.mcp.json`** so both working servers actually start on the
   next session reconnect. Removed the unrecoverable `mcp-scholar`
   entry.

2. **Fixed `leitnerpawloski2004` verification** — its `local_pdf`
   pointed at a non-existent
   `library/leitnerpawloski2004.pdf` alias; the actual file is
   `library/arxiv-math-0409565v2/0409565v2.pdf` (arxiv-id-named). Corrected the path so
   `bib-qa.ts` finds the file and `has_local_pdf` flips to `pass`.

3. **Audited the bib-papers ledger.** Findings:

   | Bucket | Count | Recoverable from this env? |
   |--------|-------|----------------------------|
   | References without URL/DOI in `references.ts` | 37 | No (need search → 9 are pre-1990 books, 28 are findable arxiv preprints) |
   | Verifications with broken `local_pdf` path (file truly missing) | 45 | No (network blocked) |
   | Verifications with broken `local_pdf` path (file exists under different name) | 1 (leitnerpawloski2004) | **Yes — fixed in this commit** |
   | `scripts/bib-papers-list.txt` entries missing from `library/` | 56 of 58 | No (network blocked) |

## Why we can't do more in this session

This Claude-Code-on-the-web environment has a restrictive
[network policy](https://code.claude.com/docs/en/claude-code-on-the-web)
that only allows `github.com`. Probed:

```
arxiv.org              403 host_not_allowed
export.arxiv.org       403 host_not_allowed
api.openalex.org       403 host_not_allowed
api.semanticscholar.org 403 host_not_allowed
doi.org                403 host_not_allowed
www.numdam.org         403 host_not_allowed
api.crossref.org       (not probed; same allowlist)
```

`WebFetch` is also blocked — the same allowlist applies.
`WebSearch` works (it surfaces abstracts via Anthropic's
infrastructure) but cannot return binary PDFs.

## To complete the audit (handoff for normal-network machine)

The mechanical work is **bash one-liners against existing infra**:

```bash
# 1. Regenerate the download list from the current bib.
python3 scripts/gen-bib-papers-list.py

# 2. Download all 58 publicly-accessible PDFs/data files and
#    commit them per-paper to a fresh branch.
bash scripts/upload-bib-papers.sh --pr

# 3. Once that PR merges, re-run the QA audit and the verification
#    backfill should bring 45+ has_local_pdf from fail/unchecked to pass.
cd content && bun run pipeline/bib-qa.ts
```

For the 37 URL-missing references, the `paper-search-mcp` tools (once
the next MCP reconnect picks up our `.mcp.json` change AND the
network policy allows arxiv.org) make this scriptable rather than
manual:

```python
# Pseudo-code for an offline metadata-enrichment pass
for entry in references.ts where url is null and type == article-journal:
    hits = search_arxiv(entry.title)
    if best_match(hits, entry).confidence > 0.8:
        propose update entry.url = hits[0].arxiv_url
```

That script is **not** added in this branch — it's premature without
network access to test. The author should triage the 37 URL-missing
list manually or queue it for a future session with a relaxed
policy.

## Why this matters

- **Bib QA is the first line of scholarly defence.** Every
  `\cite{}` / `-- Ref:` in QOU is a hostage to the bibliography being
  correct. A wrong-work resolution (Borel-Wallach vs Borel-Zagier,
  the leitnerpawloski2004 PL-inner-product mismatch) silently
  corrupts the paper's claims.
- **Local PDFs make verification fast.** Without `library/<id>.pdf`,
  every cross-check requires a network round-trip and an agent
  re-reading the paper. With it, `bib-qa.ts` can directly grep
  the cited text.
- **270M+ catalogue access is qualitatively new.** Pre-OpenAlex
  every URL-missing entry was a manual lookup. With it, the 37
  no-URL entries become a scriptable backlog.

## Cross-references

- Skill: [`bib-qa`](.claude/skills/local/bib-qa.md) — full QA workflow
- Skill: [`paper-importer`](.claude/skills/local/paper-importer.md) —
  arxiv intake pipeline
- Skill: [`document-intake`](.claude/skills/local/document-intake.md) —
  WHO guidelines and other non-paper intake
- Coordination log:
  [`docs/coordination/2026-05-19-bib-verification-ledger.md`](2026-05-19-bib-verification-ledger.md)
- Network policy:
  [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)

## Coordination ledger

| Date | PR | Phase | Status | Cherry-pick / dependency |
|------|----|-------|--------|--------------------------|
| 2026-05-22 | [#883](https://github.com/litlfred/qou/pull/883) | `.mcp.json` repair + bib audit + design doc | open · branch-tip [`a6319b41`](https://github.com/litlfred/qou/commit/a6319b41caaa9981ed0cbb2231c7a5397ee75e93) (not yet merged to main) | **Depends on [#880](https://github.com/litlfred/qou/pull/880)** — without that PR's `$HOME/.local/bin` PATH fix in `scripts/start-folio-assistant.sh`, the `uvx`-based MCP servers I configured won't be found by the session-start launcher. Order: land #880 first or together. |
| 2026-05-22 | [#880](https://github.com/litlfred/qou/pull/880) | MCP PATH fix + proof-axis backlog drain | open · branch-tip [`39b7f740`](https://github.com/litlfred/qou/commit/39b7f7407c33dbb4d26ee47a7f9aa51435ac1f84) (not yet merged to main) — `scripts/start-folio-assistant.sh` PATH export | prerequisite for #883's MCP server fixes to function in remote-execution sessions |

## Sibling scope map (snapshot 2026-05-22)

| PR | Branch | Overlap with #883 | Dependency | Cherry-pick | Coordination posted |
|----|--------|---|---|---|---|
| #880 | `claude/friendly-wright-GH0qG` | none (different files) | I depend on theirs | none | [comment](https://github.com/litlfred/qou/pull/880#issuecomment-4519815234) |
| #881 | `claude/prepare-merge-no-squash-default-2026-05-22` | none | independent | none | — |
| #882 | `claude/eager-gauss-S36Uk` | none (one-voice sidecars ≠ bib) | independent | none | — |
| #875 | `copilot/integration-backlog-proof` (now under #880 author per [their coord reply](https://github.com/litlfred/qou/pull/883#issuecomment-4519821141)) | none (`content/pipeline/qa-checkers-extended.ts`) | independent | none | — |
| #872 | `claude/qa-script-criteria-2026-05-20` | none | independent | none | — |
| #878 | `claude/wenzl-lr-consumer-fix-2026-05-22` | none | independent | none | — |
| #871 | `copilot/optimize-compute-pipeline` [DRAFT] | none | independent | none | — |
| #876 | `copilot/review-pull-872` | none | independent | none | — |
| #807 | `claude/compute-audit-P33-P34-2026-05-19` | none | independent | none | — |
| #818 | `claude/i1-probe-knot-factor-borromean-composite-2026-05-19` | none | independent | none | — |
| #827 | `copilot/sub-pr-826` | none | independent | none | — |
| #817 | `claude/cor-knot-factor-amphicheiral-revise-2026-05-19` | none | independent | none | — |
| #761 | `claude/combine-all-open-prs` | none (chirality/Hoefsmit/GP stack) | independent | none | — |
| #774 | `claude/iw-meta-tighten-guarded-off-heuristic` | none | independent | none | — |
| #646 | `copilot/fix-lake-errors` | none | independent | none | — |
| #650 | `copilot/add-q-clt-proof-derivation` | none | independent | none | — |
| #31  | `copilot/add-svg-illustration-affine-light` | none | independent | none | — |
| #411 | `copilot/sub-pr-410` | none (Dockerfile only — different surface; both touch MCP infra but no shared files) | independent | none | — |

## Main delta during session

- `236d742f… → 56c4dcaa…` — 14 commits across three PRs:
  - **#879** (3 commits) — `docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md` (210× scale-gap audit, third pass)
  - **#875** (8 commits, merged by #880's author) — `content/pipeline/qa-checkers-extended.ts` + `content/pipeline/script-sidecars/proof-no-trivial-skeleton.script.json`
  - **#888** (3 commits) — CAL-4 truth-in-naming `LAMBDA_*_FITTED` + I13 audit (canonical-witness refresh, new audit infrastructure)
- File overlap with this branch: **empty**. Per §8a all three PRs are additive; will resolve cleanly on PR merge. Delta is above §8c's >10 threshold but the empty overlap removes any rebase-storm risk; flagged here per the §8c "continue + flag" branch.
