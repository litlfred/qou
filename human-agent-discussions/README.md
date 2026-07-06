# human-agent-discussions

Archived transcripts of Claude ⇄ author discussions that shaped QOU
work, rendered to PDF and tagged with the PRs / commits / branches
that followed from each discussion.

## Layout

```
human-agent-discussions/
  README.md                       ← this file
  INDEX.md                        ← auto-generated index of all archived sessions
  tools/
    archive_sessions.py           ← the archiver (stdlib-only Python)
    fetch_claude_export.py        ← scripted conversations.json fetch (route C)
    browser-export-snippet.js     ← console snippet to download an export (route B)
  _incoming/                      ← gitignored drop folder for raw exports
    <account>/conversations.json
    <account>/*.jsonl
  <account>/
    <YYYY-MM-DD>-<slug>/
      session.md                  ← pandoc-ready transcript (auto-screened)
      session.pdf                 ← rendered PDF
      metadata.json               ← machine-readable record: related PRs/commits, screen
```

Post-merge maintenance (re-tag + PDF upgrade) is automated by
[`.github/workflows/discussions-maintain.yml`](../.github/workflows/discussions-maintain.yml).

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

   # OPTIONAL: review the sensitive-info screen before writing anything
   python3 human-agent-discussions/tools/archive_sessions.py --screen

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

## Web UI (recommended — minimal typing)

A local web interface wraps the whole flow — no flags, no paths, no
retyping account names:

```bash
python3 human-agent-discussions/tools/archive_ui.py --open
# → http://127.0.0.1:8123/ (localhost only; runs against this clone)
```

1. **Account** — one click on a remembered chip. Accounts are derived
   from the directories already on disk (`<account>/` archives +
   `_incoming/<account>/` inboxes), so every account used once is
   remembered forever; "Add" registers a new alias.
2. **Add export** — drag-drop `conversations.json` *or the official
   export `.zip`* (the relevant files are extracted server-side) onto
   the drop zone; it lands in the gitignored `_incoming/<account>/`.
3. **Matched conversations** — Scan lists QOU matches with status
   (NEW / UPDATED / archived), sensitive-info severity
   (SECRET / pii / clean) and keyword hits; tick checkboxes (or
   "Select all NEW") and Archive. Results link straight to the
   rendered `session.md` / `session.pdf`.
4. **Git — staging & submission** — shows the branch, head, and every
   staged / unstaged file under `human-agent-discussions/`; Commit or
   Commit & push with an editable pre-filled message, then see the
   submission result (commit SHA linked to origin, full command log,
   push output) right in the page.

The server binds `127.0.0.1` only, accepts only `.json` / `.jsonl` /
`.zip` uploads into `_incoming/`, serves files only from inside the
archive root, and reuses the exact same archiver core (same screen,
same tagging, same idempotency). `python3 tools/archive_ui.py
--self-test` exercises upload → scan → archive → serve → commit
against a throwaway git repo.

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
`"commit 43f413c3"`), then run `--retag`. Manual tags survive
re-archiving and re-tagging, and are spliced into `session.md` +
`INDEX.md`.

### Re-tagging after the fact (`--retag`)

A discussion is usually archived *before* the PR/commit it produced
exists. `--retag` recomputes every archived session's related-work
tags against the **current** git + GitHub state — no conversation
input needed — and re-splices the "Related work" section of each
`session.md` (refreshing the PDF) plus `INDEX.md`:

```bash
python3 human-agent-discussions/tools/archive_sessions.py --retag --github
```

It is idempotent (only sessions whose tags actually changed are
rewritten) and works off a `refs_raw` record stored in each
`metadata.json` at archive time (falling back to re-parsing
`session.md` for older archives).

### Post-merge automation

The [`discussions-maintain.yml`](../.github/workflows/discussions-maintain.yml)
workflow runs `--retag --github` then `--rerender-pdfs` on every push
to `main` (and on manual dispatch), committing the result back with
`[skip ci]`. So when a PR that came out of a discussion **merges**,
the merge commit's session trailers are picked up automatically and
the discussion's archived session gains the PR/commit tag — no manual
step. (`GITHUB_TOKEN` pushes don't retrigger CI; `[skip ci]` is a
second guard.)

What stays manual: **capturing** new conversations (producing
`conversations.json` per account) can't be reliably automated — the
official export is async/email, and the unofficial routes need either
a browser session or a short-lived account credential that
Cloudflare often blocks from CI runners. So new sessions are archived
by a local run; everything *after* archiving (re-tagging, PDF
upgrade) is automatic.

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
[`discussions-maintain.yml`](../.github/workflows/discussions-maintain.yml)
workflow (see *Post-merge automation* above) re-renders any committed
`session.pdf` whose `metadata.json` records a non-pandoc engine (e.g.
`builtin`) using pandoc + XeLaTeX + DejaVu fonts. The same operation
locally:

```bash
python3 human-agent-discussions/tools/archive_sessions.py --rerender-pdfs
```

## Privacy & sensitive-info screen

This repository is public. The archiver:

- never commits anything by itself — it only writes files for you to review;
- only writes conversations matching the QOU keyword filter
  (`--keyword` to extend, `--no-default-keywords` to replace);
- keeps raw exports out of git (`_incoming/` is gitignored).

**Sensitive-info screen.** Every conversation is scanned before
rendering:

- **Secrets** (API keys — Anthropic / OpenAI / Google / AWS / Slack —
  GitHub tokens, JWTs, bearer tokens, private-key blocks, `key=…`
  assignments) are **auto-redacted** to `[REDACTED-<kind>]` in both
  `session.md` and the PDF. Counts are recorded in `metadata.json`
  under `screen.redacted` (the secret itself is never stored).
  Disable with `--no-redact` (not recommended for a public repo).
- **PII** (email, phone, IPv4) is **flagged but left in place** —
  reported under `screen.flagged` and in the `--screen` / `--list`
  output — so you decide. Add `--redact-pii` to mask it too.

Run `--screen` to review findings per conversation *before* archiving;
the numbered `--list` output also shows a `SECRET` / `pii` / `clean`
column. Pattern-matching is best-effort (expect some false positives
on phone/IPv4), so still skim the generated PDFs before pushing — an
export can contain private context pasted into an otherwise-QOU
conversation that no regex will catch.

## Idempotency

Re-running is safe: sessions already archived (same conversation id)
are skipped unless the export contains newer messages (`updated_at`
moved) or `--force` is given. `INDEX.md` is regenerated on every run.
