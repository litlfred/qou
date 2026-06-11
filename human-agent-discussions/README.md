# human-agent-discussions

Archived transcripts of Claude ⇄ author discussions that shaped QOU
work, rendered to PDF and tagged with the PRs / commits / branches
that followed from each discussion.

## Layout

```
human-agent-discussions/
  README.md                  ← this file
  INDEX.md                   ← auto-generated index of all archived sessions
  tools/archive_sessions.py  ← the archiver (stdlib-only Python)
  _incoming/                 ← gitignored drop folder for raw exports
    <account>/conversations.json
    <account>/*.jsonl
  <account>/
    <YYYY-MM-DD>-<slug>/
      session.md             ← pandoc-ready transcript
      session.pdf            ← rendered PDF
      metadata.json          ← machine-readable record incl. related PRs/commits
```

`<account>` is a short alias you choose per Claude account
(e.g. `ofri`, `ofri-work`, `ofri-alt`) — lowercase letters, digits,
hyphens.

## Getting the `conversations.json` (pick one route per account)

There is **no official API** for claude.ai chat history (the developer
API at `api.anthropic.com` does not expose your conversations), so the
input is always a `conversations.json`. Three ways to produce one:

| Route | How | Pros / cons |
|---|---|---|
| **A. Official export** | claude.ai → Settings → Privacy → Export data → unzip | Sanctioned, robust; arrives by email (minutes–hours of delay) |
| **B. Browser snippet** | paste [`tools/browser-export-snippet.js`](tools/browser-export-snippet.js) into the claude.ai DevTools console | Instant, no credentials leave the browser; unofficial endpoints (may break) |
| **C. Scripted fetch** | `CLAUDE_SESSION_KEY=… python3 tools/fetch_claude_export.py --out …` | Fully scriptable; needs your `sessionKey` cookie (full account access — never commit/paste it), Cloudflare may block |

Routes B and C hit claude.ai's **internal, undocumented** endpoints and
may break without notice; A is the fallback. For C, set the cookie in the
environment only (never on the command line / in chat); see the script
header for how to obtain it.

## Quick start (repeat once per Claude account)

1. Produce `conversations.json` via route A, B, or C above.
2. Drop it into `human-agent-discussions/_incoming/<account>/`
   (gitignored — raw exports never get committed), or just note its path.
3. From the repo root:

   ```bash
   # list QOU-related conversations (numbered, nothing written)
   python3 human-agent-discussions/tools/archive_sessions.py

   # archive all matches (or --select 1,3-5 for a subset)
   python3 human-agent-discussions/tools/archive_sessions.py --select all
   ```

4. Review `git status`, then commit + push (or let the agent do it).

If exports live elsewhere, point at them explicitly:

```bash
python3 human-agent-discussions/tools/archive_sessions.py \
  --export ofri=~/Downloads/data-export/conversations.json \
  --export ofri-work=~/Downloads/work-export/conversations.json \
  --select all
```

**Claude Code CLI sessions** (local terminal sessions) are also
supported: point `--export <account>=~/.claude/projects/<project>/`
at the directory (or a single `.jsonl` file). Sessions whose working
directory contains `qou` match automatically.

## How tagging works

Each archived session gets a `related` block in `metadata.json`,
rendered as a "Related work" section in the PDF and in `INDEX.md`:

| Signal | Evidence tag |
|---|---|
| Commit trailers `https://claude.ai/code/session_<id>` matching the session | `session-trailer` |
| Conversation UUID appearing in a commit message | `uuid-trailer` |
| `#1234` / `github.com/litlfred/qou/pull/1234` mentioned in the discussion | `mentioned` |
| Commit SHAs mentioned in the discussion (verified against the repo) | `mentioned` |
| `claude/*` branch names mentioned (checked against origin) | — |

With `--github` (requires the `gh` CLI, optional) the tool also
resolves branches → PRs, commits → PRs, and enriches PR titles/states.

**Manual tags:** edit a session's `metadata.json`, add entries to
`related.manual` (free-form strings like `"PR #1821"` or
`"commit 43f413c3"`), then run the tool with `--reindex`. Manual tags
survive re-archiving.

## PDF engines

Best available engine is auto-detected:

1. `pandoc` + (`xelatex` | `lualatex` | `tectonic` | `typst` |
   `pdflatex` | `weasyprint` | `wkhtmltopdf`) — nice output, math
   rendered. Recommended install: `sudo apt install pandoc texlive-xetex`.
2. Built-in pure-Python renderer — basic but dependency-free
   (transliterates non-Latin-1 glyphs; math stays as `$...$` source).

`session.md` is always written, so PDFs can be (re)generated later with
a better engine via `--force --pdf-engine pandoc`.

### CI re-rendering

You don't need pandoc locally: the
[`render-discussions.yml`](../.github/workflows/render-discussions.yml)
workflow re-renders any committed `session.pdf` whose `metadata.json`
records a non-pandoc engine (e.g. `builtin`) using pandoc + XeLaTeX +
DejaVu fonts, and commits the upgraded PDFs back to the branch. It
triggers on any push touching `human-agent-discussions/**/session.md`,
or manually from the Actions tab (the `force` input re-renders
everything). The same operation locally:

```bash
python3 human-agent-discussions/tools/archive_sessions.py --rerender-pdfs
```

## Privacy

This repository is public. The archiver:

- never commits anything by itself — it only writes files for you to review;
- only writes conversations matching the QOU keyword filter
  (`--keyword` to extend, `--no-default-keywords` to replace);
- keeps raw exports out of git (`_incoming/` is gitignored).

Always review the numbered `--list` output before `--select all`, and
skim the generated PDFs before pushing — an export can contain
private context pasted into an otherwise-QOU conversation.

## Idempotency

Re-running is safe: sessions already archived (same conversation id)
are skipped unless the export contains newer messages (`updated_at`
moved) or `--force` is given. `INDEX.md` is regenerated on every run.
