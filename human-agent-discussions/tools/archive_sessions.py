#!/usr/bin/env python3
"""Archive QOU-related Claude sessions into human-agent-discussions/.

Ingests
  * claude.ai data exports   (conversations.json — Settings → Privacy → Export data)
  * Claude Code CLI sessions (~/.claude/projects/<project>/*.jsonl)

For each conversation matching the QOU keyword filter, writes

  human-agent-discussions/<account>/<YYYY-MM-DD>-<slug>/
    session.md      pandoc-ready transcript
    session.pdf     rendered PDF (best available engine)
    metadata.json   machine-readable record incl. related PRs/commits/branches

and regenerates human-agent-discussions/INDEX.md.

Related-work tagging signals:
  * commit trailers  https://claude.ai/code/session_<id>  matching the session
  * conversation UUID appearing in a commit message
  * "#1234" / pull-request URLs mentioned in the discussion
  * commit SHAs mentioned in the discussion (verified against the repo)
  * claude/* branch names mentioned (checked against origin)
  * optional --github enrichment via the `gh` CLI (branch→PR, commit→PR)

Stdlib only.  PDF engines tried in order: pandoc (+xelatex/lualatex/tectonic/
typst/pdflatex/weasyprint/wkhtmltopdf), then a builtin pure-Python renderer
(basic: non-Latin-1 glyphs transliterated, math left as $...$ source).
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.3.0"
REPO_SLUG = "litlfred/qou"
GITHUB_URL = "https://github.com/" + REPO_SLUG

DEFAULT_KEYWORDS = [
    "qou",
    "quantum observable universe",
    "quantum-observable-universe",
    "litlfred/qou",
]

PR_RE = re.compile(
    r"(?:github\.com/" + re.escape(REPO_SLUG) + r"/pull/(\d{1,6}))|(?<![\w/&#])#(\d{2,6})\b"
)
BRANCH_RE = re.compile(r"\bclaude/[A-Za-z0-9][A-Za-z0-9._-]{2,80}")
SHA_RE = re.compile(r"\b[0-9a-f]{7,40}\b")
SESSION_RE = re.compile(r"claude\.ai/code/(session_[A-Za-z0-9]+)")
ACCOUNT_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,40}$")


# ----------------------------------------------------------------- utilities

def log(msg):
    print(msg, file=sys.stderr)


def run(cmd, cwd=None, timeout=60):
    """Run a command; return (rc, stdout, stderr) without raising."""
    try:
        p = subprocess.run(
            cmd, cwd=str(cwd) if cwd else None,
            capture_output=True, text=True, timeout=timeout,
        )
        return p.returncode, p.stdout, p.stderr
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, "", str(e)


def parse_ts(s):
    """Tolerant ISO-8601 → aware UTC datetime (or None)."""
    if not s or not isinstance(s, str):
        return None
    s = s.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        m = re.match(r"(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2})", s)
        if not m:
            return None
        try:
            dt = datetime.fromisoformat(m.group(1))
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def fmt_ts(dt):
    return dt.strftime("%Y-%m-%d %H:%M UTC") if dt else "?"


def iso(dt):
    return dt.isoformat() if dt else None


def slugify(text, maxlen=48):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return (text[:maxlen].rstrip("-")) or "untitled"


def md_cell(text):
    """Escape a string for use inside a markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ")


# ----------------------------------------------------------------- parsers

def _message_from_blocks(content, opts):
    """Normalize a message `content` (str or block list) → (text, tools)."""
    text_parts, tools = [], []
    if isinstance(content, str):
        if content.strip():
            text_parts.append(content)
    elif isinstance(content, list):
        for blk in content:
            if not isinstance(blk, dict):
                continue
            bt = blk.get("type")
            if bt == "text" and blk.get("text"):
                text_parts.append(blk["text"])
            elif bt == "thinking" and opts.include_thinking and blk.get("thinking"):
                text_parts.append("> *(thinking)* " + blk["thinking"].replace("\n", "\n> "))
            elif bt == "tool_use":
                tools.append({"name": blk.get("name") or "tool", "input": blk.get("input")})
            # tool_result blocks are skipped (noisy; summarized by the tool_use line)
    return "\n\n".join(text_parts), tools


def parse_claude_export(path, account, opts):
    """claude.ai data-export conversations.json → list of normalized convs."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        log("WARN: cannot parse %s: %s" % (path, e))
        return []
    if isinstance(data, dict):
        data = data.get("conversations") or []
    convs = []
    for c in data:
        if not isinstance(c, dict):
            continue
        msgs = []
        for m in c.get("chat_messages") or []:
            if not isinstance(m, dict):
                continue
            text, tools = _message_from_blocks(m.get("content"), opts)
            if not text and m.get("text"):
                text = m["text"]
            atts = []
            for a in m.get("attachments") or []:
                if isinstance(a, dict):
                    atts.append({
                        "name": a.get("file_name") or "attachment",
                        "content": a.get("extracted_content") or "",
                    })
            for f in m.get("files") or []:
                if isinstance(f, dict):
                    atts.append({"name": f.get("file_name") or "file", "content": ""})
            msgs.append({
                "role": "human" if m.get("sender") == "human" else "assistant",
                "ts": parse_ts(m.get("created_at")),
                "text": text or "",
                "tools": tools,
                "attachments": atts,
            })
        if not msgs:
            continue
        cid = c.get("uuid") or ""
        convs.append({
            "source": "claude-export",
            "account": account,
            "id": cid,
            "url": ("https://claude.ai/chat/" + cid) if cid else None,
            "title": (c.get("name") or "").strip() or "(untitled)",
            "created_at": parse_ts(c.get("created_at")),
            "updated_at": parse_ts(c.get("updated_at")) or parse_ts(c.get("created_at")),
            "messages": msgs,
            "extra": {"summary": c.get("summary") or "", "export_file": str(path)},
        })
    return convs


def parse_code_jsonl(path, account, opts):
    """Claude Code CLI session .jsonl → one normalized conv (or None)."""
    msgs, title, sid, cwd, branch = [], None, None, None, None
    t0 = t1 = None
    try:
        fh = open(path, encoding="utf-8")
    except OSError as e:
        log("WARN: cannot read %s: %s" % (path, e))
        return None
    with fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(rec, dict):
                continue
            rt = rec.get("type")
            if rt == "summary" and rec.get("summary"):
                title = rec["summary"]
                continue
            sid = sid or rec.get("sessionId")
            cwd = cwd or rec.get("cwd")
            branch = branch or rec.get("gitBranch")
            ts = parse_ts(rec.get("timestamp"))
            if ts:
                t0 = ts if (t0 is None or ts < t0) else t0
                t1 = ts if (t1 is None or ts > t1) else t1
            if rt not in ("user", "assistant") or rec.get("isMeta"):
                continue
            message = rec.get("message") or {}
            text, tools = _message_from_blocks(message.get("content"), opts)
            if not text and not tools:
                continue
            msgs.append({
                "role": "human" if rt == "user" else "assistant",
                "ts": ts,
                "text": text,
                "tools": tools,
                "attachments": [],
            })
    if not msgs:
        return None
    if not title:
        first = next((m["text"] for m in msgs if m["role"] == "human" and m["text"]), "")
        title = first.splitlines()[0][:80] if first else Path(path).stem
    return {
        "source": "claude-code",
        "account": account,
        "id": sid or Path(path).stem,
        "url": None,
        "title": title.strip() or "(untitled)",
        "created_at": t0,
        "updated_at": t1 or t0,
        "messages": msgs,
        "extra": {"cwd": cwd or "", "git_branch": branch or "", "jsonl_file": str(path)},
    }


# ----------------------------------------------------------------- filtering

def keyword_hits(conv, keywords):
    """Return sorted list of matched filter signals for a conversation."""
    hay = [conv["title"], conv.get("extra", {}).get("summary", "")]
    for m in conv["messages"]:
        hay.append(m["text"])
        for a in m["attachments"]:
            hay.append(a["name"])
            hay.append(a["content"][:20000])
    blob = "\n".join(h for h in hay if h).lower()
    hits = sorted({k for k in keywords if k.lower() in blob})
    cwd = conv.get("extra", {}).get("cwd", "")
    if conv["source"] == "claude-code" and "qou" in cwd.lower():
        hits.append("cwd:qou")
    return hits


# ----------------------------------------------------------------- git layer

class Repo:
    def __init__(self, path):
        self.path = Path(path)
        self._branch_cache = {}

    def ok(self):
        rc, _, _ = run(["git", "rev-parse", "--git-dir"], cwd=self.path)
        return rc == 0

    def trailer_map(self):
        """session_id → [{sha, subject}] from claude.ai/code/session_ trailers."""
        rc, out, _ = run(
            ["git", "log", "--all", "--grep", r"claude\.ai/code/session_",
             "--format=%H%x01%s%x01%b%x02"],
            cwd=self.path, timeout=180,
        )
        mapping = {}
        if rc != 0:
            return mapping
        for chunk in out.split("\x02"):
            if not chunk.strip():
                continue
            parts = chunk.strip("\n").split("\x01")
            sha = parts[0].strip()
            subject = parts[1] if len(parts) > 1 else ""
            body = parts[2] if len(parts) > 2 else ""
            for sid in set(SESSION_RE.findall(subject + "\n" + body)):
                mapping.setdefault(sid, []).append({"sha": sha, "subject": subject})
        return mapping

    def verify_commit(self, sha):
        """Resolve a mentioned SHA to {sha, subject} if it exists; else None."""
        rc, out, _ = run(
            ["git", "rev-parse", "--verify", "--quiet", sha + "^{commit}"],
            cwd=self.path,
        )
        if rc != 0 or not out.strip():
            return None
        full = out.strip()
        _, subj, _ = run(["git", "show", "-s", "--format=%s", full], cwd=self.path)
        return {"sha": full, "subject": subj.strip()}

    def grep_commits(self, needle, cap=20):
        rc, out, _ = run(
            ["git", "log", "--all", "--grep", needle, "--format=%H%x01%s"],
            cwd=self.path, timeout=120,
        )
        found = []
        if rc != 0:
            return found
        for line in out.splitlines()[:cap]:
            if "\x01" in line:
                sha, subj = line.split("\x01", 1)
                found.append({"sha": sha, "subject": subj})
        return found

    def branch_on_origin(self, name, fast=False):
        """True/False if determinable, None when unknown.

        Checks local remote-tracking refs first; with fast=False falls back
        to a `git ls-remote` network probe. With fast=True the network probe
        is skipped (returns None for branches absent from local refs) so the
        default offline path makes no network calls.
        """
        if name in self._branch_cache:
            return self._branch_cache[name]
        result = None
        rc, _, _ = run(
            ["git", "rev-parse", "--verify", "--quiet", "refs/remotes/origin/" + name],
            cwd=self.path,
        )
        if rc == 0:
            result = True
        elif not fast:
            rc, out, _ = run(
                ["git", "ls-remote", "--heads", "origin", name],
                cwd=self.path, timeout=20,
            )
            result = bool(out.strip()) if rc == 0 else None
        self._branch_cache[name] = result
        return result


# ----------------------------------------------------------- ref extraction

def extract_refs(conv):
    texts = [conv["title"]]
    for m in conv["messages"]:
        texts.append(m["text"])
        for t in m["tools"]:
            try:
                texts.append(json.dumps(t.get("input"), ensure_ascii=False))
            except (TypeError, ValueError):
                pass
    blob = "\n".join(texts)
    prs = sorted({int(a or b) for a, b in PR_RE.findall(blob)})
    branches = sorted({b.rstrip("».,;:)'\"`") for b in BRANCH_RE.findall(blob)})
    shas = []
    for s in SHA_RE.findall(blob):
        if not s.isdigit() and s not in shas:
            shas.append(s)
    session_ids = sorted(set(SESSION_RE.findall(blob)))
    return prs, branches, shas[:200], session_ids


EVIDENCE_RANK = {"session-trailer": 0, "uuid-trailer": 1, "mentioned": 2}


def build_related(conv, repo, trailers, use_github):
    """→ (related dict, refs_raw dict). refs_raw is the extracted-refs record
    persisted in metadata so --retag can recompute tags post-merge without
    the original conversation."""
    prs, branches, shas, sess_mentioned = extract_refs(conv)
    refs_raw = {"prs": prs, "branches": branches, "shas": shas,
                "session_ids_mentioned": sess_mentioned}
    related = build_related_from_refs(refs_raw, str(conv["id"]), repo,
                                      trailers, use_github)
    return related, refs_raw


def build_related_from_refs(refs_raw, conv_id, repo, trailers, use_github):
    """Pure-ish tag builder: (extracted refs + current git/GitHub state) →
    related dict. Re-runnable post-merge to attach newly-landed PRs/commits."""
    prs = refs_raw.get("prs", [])
    branches = refs_raw.get("branches", [])
    shas = refs_raw.get("shas", [])
    sess_mentioned = refs_raw.get("session_ids_mentioned", [])
    commits = []  # (rank, {sha, subject, evidence}); sha kept full (40-char)

    def add_commit(sha, subject, evidence):
        commits.append((EVIDENCE_RANK.get(evidence, 9), {
            "sha": sha, "subject": subject, "evidence": evidence,
        }))

    sids = set(sess_mentioned)
    if str(conv_id).startswith("session_"):
        sids.add(str(conv_id))
    for sid in sorted(sids):
        for c in trailers.get(sid, []):
            add_commit(c["sha"], c["subject"], "session-trailer")

    cid = str(conv_id)
    if cid and len(cid) >= 8 and not cid.startswith("session_"):
        for c in repo.grep_commits(cid):
            add_commit(c["sha"], c["subject"], "uuid-trailer")

    for s in shas:
        v = repo.verify_commit(s)
        if v:
            add_commit(v["sha"], v["subject"], "mentioned")

    # dedupe commits, strongest evidence wins
    seen, commit_list = {}, []
    for rank, c in sorted(commits, key=lambda rc_: rc_[0]):
        if c["sha"] not in seen:
            seen[c["sha"]] = True
            commit_list.append(c)

    pr_map = {}
    for n in prs:
        pr_map[n] = {"number": n, "url": "%s/pull/%d" % (GITHUB_URL, n),
                     "evidence": "mentioned"}

    branch_list = [{"name": b, "exists_on_origin": repo.branch_on_origin(b, fast=not use_github)}
                   for b in branches]

    if use_github and shutil.which("gh"):
        _gh_enrich(pr_map, branch_list, commit_list)

    return {
        "prs": [pr_map[n] for n in sorted(pr_map)],
        "commits": commit_list,
        "branches": branch_list,
        "session_ids": sorted(sids),
        "manual": [],
    }


def _gh_enrich(pr_map, branch_list, commit_list):
    """Optional gh-CLI enrichment: PR titles/states, branch→PR, commit→PR."""
    def gh_json(args, timeout=20):
        rc, out, _ = run(["gh"] + args, timeout=timeout)
        if rc != 0:
            return None
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            return None

    for n, pr in list(pr_map.items()):
        d = gh_json(["pr", "view", str(n), "--repo", REPO_SLUG,
                     "--json", "number,title,state,url"])
        if d:
            pr.update({"title": d.get("title"), "state": d.get("state"),
                       "url": d.get("url") or pr["url"]})

    for b in branch_list:
        d = gh_json(["pr", "list", "--repo", REPO_SLUG, "--head", b["name"],
                     "--state", "all", "--json", "number,title,state,url"])
        for pr in d or []:
            n = pr.get("number")
            if n and n not in pr_map:
                pr_map[n] = {"number": n, "url": pr.get("url"),
                             "title": pr.get("title"), "state": pr.get("state"),
                             "evidence": "via-branch:" + b["name"]}

    for c in commit_list[:20]:
        d = gh_json(["api", "repos/%s/commits/%s/pulls" % (REPO_SLUG, c["sha"])])
        for pr in d or []:
            n = pr.get("number")
            if n and n not in pr_map:
                pr_map[n] = {"number": n, "url": pr.get("html_url"),
                             "title": pr.get("title"), "state": pr.get("state"),
                             "evidence": "via-commit:" + c["sha"]}


# ------------------------------------------------------- sensitive-info screen

# High-confidence secrets: auto-redacted by default (must never reach a public
# repo). Each pattern → label. Ordered most-specific first.
SECRET_PATTERNS = [
    ("anthropic-key", re.compile(r"sk-ant-[A-Za-z0-9_-]{16,}")),
    ("github-token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("openai-key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9]{20,}\b")),
    ("private-key-block", re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
    ("bearer-token", re.compile(r"[Bb]earer\s+[A-Za-z0-9._\-]{20,}")),
    ("generic-secret-assign", re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|passwd|token)\b\s*[:=]\s*"
        r"['\"]?([A-Za-z0-9/+_\-]{12,})['\"]?")),
]

# Lower-confidence PII: flagged for human review, redacted only with
# --redact-pii (expect false positives, e.g. version strings as IPv4).
PII_PATTERNS = [
    ("email", re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")),
    ("phone", re.compile(
        r"(?<![\w.])(?:\+?\d{1,3}[ .\-]?)?\(?\d{3}\)?[ .\-]\d{3}[ .\-]\d{4}(?!\d)")),
    ("ipv4", re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")),
]


def _redact_text(text, redact_pii):
    """→ (redacted_text, counts). Secrets always masked; PII only if asked."""
    counts = {}
    if not text:
        return text, counts
    groups = list(SECRET_PATTERNS) + (list(PII_PATTERNS) if redact_pii else [])
    for label, pat in groups:
        def _sub(m, _label=label):
            counts[_label] = counts.get(_label, 0) + 1
            return "[REDACTED-%s]" % _label
        text = pat.sub(_sub, text)
    return text, counts


def scan_text(text):
    """→ {label: count} of secret + PII matches (no mutation; for reporting)."""
    counts = {}
    if not text:
        return counts
    for label, pat in SECRET_PATTERNS + PII_PATTERNS:
        n = len(pat.findall(text))
        if n:
            counts[label] = counts.get(label, 0) + n
    return counts


def conv_blob(conv):
    """All free text in a conversation (title + messages + attachments)."""
    parts = [conv.get("title", "")]
    for m in conv["messages"]:
        parts.append(m.get("text", ""))
        for a in m.get("attachments", []):
            parts.append(a.get("content", ""))
    return "\n".join(p for p in parts if p)


def screen_conv(conv, redact=True, redact_pii=False):
    """Scan a conversation; if redact, mutate its text to mask secrets
    (always) and PII (only when redact_pii). → {"redacted": {label: n},
    "flagged": {label: n}}; `flagged` = matches left in place for the user
    to review (PII when redact_pii is off, everything when redact is off)."""
    total = scan_text(conv_blob(conv))
    redacted = {}
    if redact:
        def _apply(s):
            new, c = _redact_text(s, redact_pii)
            for k, v in c.items():
                redacted[k] = redacted.get(k, 0) + v
            return new
        conv["title"] = _apply(conv.get("title", ""))
        for m in conv["messages"]:
            m["text"] = _apply(m.get("text", ""))
            for a in m.get("attachments", []):
                a["content"] = _apply(a.get("content", ""))
    flagged = {k: v for k, v in total.items() if v > redacted.get(k, 0)}
    return {"redacted": redacted, "flagged": flagged}


def screen_severity(summary):
    """High if any secret label present (redacted or flagged); else pii/clean."""
    secret_labels = {lbl for lbl, _ in SECRET_PATTERNS}
    hit = set(summary.get("redacted", {})) | set(summary.get("flagged", {}))
    if hit & secret_labels:
        return "SECRET"
    if hit:
        return "pii"
    return "clean"


# ------------------------------------------------------------- md rendering

SOURCE_LABEL = {"claude-export": "claude.ai export", "claude-code": "Claude Code session log"}

# Sentinels delimiting the auto-maintained "Related work" section in
# session.md, so --retag can splice it in place without touching the
# transcript below.
RELATED_BEGIN = "<!-- related-work:begin (auto-maintained by archive_sessions.py) -->"
RELATED_END = "<!-- related-work:end -->"


def related_md_lines(related):
    """Markdown lines for the Related-work section, wrapped in splice
    sentinels. Used at archive time and re-spliced by --retag."""
    L = [RELATED_BEGIN, "## Related work", ""]
    any_rel = False
    for pr in related.get("prs", []):
        any_rel = True
        bits = "**PR [#%d](%s)**" % (pr["number"], pr["url"])
        if pr.get("title"):
            bits += " — " + md_cell(pr["title"])
        if pr.get("state"):
            bits += " (%s)" % pr["state"].lower()
        bits += " — *%s*" % pr.get("evidence", "")
        L.append("- " + bits)
    for c in related.get("commits", []):
        any_rel = True
        L.append("- **Commit `%s`** — %s — *%s*"
                 % (c["sha"][:12], md_cell(c["subject"] or ""), c["evidence"]))
    for b in related.get("branches", []):
        any_rel = True
        exists = b["exists_on_origin"]
        note = ("on origin" if exists else
                ("not found on origin" if exists is False else "origin unchecked"))
        L.append("- **Branch `%s`** (%s)" % (b["name"], note))
    for mtag in related.get("manual", []):
        any_rel = True
        L.append("- %s — *manual*" % md_cell(str(mtag)))
    if not any_rel:
        L.append("*No related PRs / commits / branches detected automatically.*")
    L.append(RELATED_END)
    return L


def render_markdown(conv, related, hits, opts):
    L = []
    title = conv["title"]
    L.append("---")
    L.append("title: " + json.dumps(title))
    L.append("author: " + json.dumps("Claude session archive — account: " + conv["account"]))
    L.append("date: " + json.dumps(fmt_ts(conv["created_at"])))
    L.append("colorlinks: true")
    L.append("---")
    L.append("")
    L.append("# " + title)
    L.append("")
    L.append("| Field | Value |")
    L.append("|---|---|")
    L.append("| Account | `%s` |" % conv["account"])
    L.append("| Source | %s |" % SOURCE_LABEL.get(conv["source"], conv["source"]))
    sid_cell = "`%s`" % conv["id"] if conv["id"] else "?"
    if conv.get("url"):
        sid_cell = "[%s](%s)" % (sid_cell, conv["url"])
    L.append("| Session | %s |" % sid_cell)
    L.append("| Started | %s |" % fmt_ts(conv["created_at"]))
    L.append("| Last activity | %s |" % fmt_ts(conv["updated_at"]))
    L.append("| Messages | %d |" % len(conv["messages"]))
    if conv.get("extra", {}).get("cwd"):
        L.append("| Working dir | `%s` |" % md_cell(conv["extra"]["cwd"]))
    if conv.get("extra", {}).get("git_branch"):
        L.append("| Git branch | `%s` |" % md_cell(conv["extra"]["git_branch"]))
    L.append("| Filter hits | %s |" % md_cell(", ".join(hits) or "—"))
    L.append("")

    L.extend(related_md_lines(related))
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Transcript")
    L.append("")

    for i, m in enumerate(conv["messages"], 1):
        who = "Human" if m["role"] == "human" else "Claude"
        L.append("### %d. %s — %s" % (i, who, fmt_ts(m["ts"])))
        L.append("")
        if m["text"]:
            L.append(m["text"])
            L.append("")
        for t in m["tools"]:
            if opts.tools == "none":
                break
            if opts.tools == "full":
                L.append("> *[tool: %s]*" % t["name"])
                L.append("")
                try:
                    inp = json.dumps(t.get("input"), ensure_ascii=False, indent=2)
                except (TypeError, ValueError):
                    inp = str(t.get("input"))
                L.append("~~~~json")
                L.append(inp)
                L.append("~~~~")
            else:
                try:
                    inp = json.dumps(t.get("input"), ensure_ascii=False)
                except (TypeError, ValueError):
                    inp = str(t.get("input"))
                inp = inp.replace("`", "'")
                if len(inp) > 140:
                    inp = inp[:140] + "…"
                L.append("> *[tool: %s — %s]*" % (t["name"], md_cell(inp)))
            L.append("")
        for a in m["attachments"]:
            n_chars = len(a["content"])
            note = " (%d chars extracted)" % n_chars if n_chars else ""
            L.append("> *[attachment: %s%s]*" % (md_cell(a["name"]), note))
            L.append("")
            if n_chars and opts.attachment_chars > 0:
                excerpt = a["content"][:opts.attachment_chars]
                L.append("~~~~")
                L.append(excerpt)
                if n_chars > opts.attachment_chars:
                    L.append("… [truncated]")
                L.append("~~~~")
                L.append("")

    L.append("---")
    L.append("")
    L.append("*Archived by `archive_sessions.py` v%s on %s.*"
             % (VERSION, datetime.now(timezone.utc).strftime("%Y-%m-%d")))
    L.append("")
    return "\n".join(L)


# ------------------------------------------------------------ PDF rendering

PANDOC_PDF_ENGINES = ["xelatex", "lualatex", "tectonic", "typst", "pdflatex",
                      "weasyprint", "wkhtmltopdf"]


def detect_engine(pref):
    """→ ('pandoc', engine) | ('builtin',) | None."""
    if pref == "none":
        return None
    if pref in ("auto", "pandoc") and shutil.which("pandoc"):
        for eng in PANDOC_PDF_ENGINES:
            if shutil.which(eng):
                return ("pandoc", eng)
        log("WARN: pandoc found but no PDF engine (xelatex/…); falling back")
        if pref == "pandoc":
            return ("builtin",)
    if pref in ("auto", "builtin"):
        return ("builtin",)
    return ("builtin",)


def render_pdf(md_path, pdf_path, md_text, title, engine, fonts=None):
    """Render PDF; returns the engine label actually used (or None)."""
    if engine is None:
        return None
    if engine[0] == "pandoc":
        cmd = [
            "pandoc", str(md_path), "-o", str(pdf_path), "--standalone",
            "--from", "markdown+autolink_bare_uris",
            "--pdf-engine=" + engine[1],
            "-V", "geometry:margin=2.2cm", "-V", "fontsize=10pt",
            "-V", "colorlinks=true", "--highlight-style=tango",
        ]
        if fonts:
            mainfont, monofont = fonts
            if mainfont:
                cmd += ["-V", "mainfont=" + mainfont]
            if monofont:
                cmd += ["-V", "monofont=" + monofont]
        rc, _, err = run(cmd, timeout=300)
        if rc == 0 and pdf_path.exists():
            return "pandoc+" + engine[1]
        log("WARN: pandoc failed (%s); using builtin renderer" % err.strip()[:200])
    builtin_pdf(md_text, pdf_path, title)
    return "builtin"


# --- builtin renderer: markdown-ish text → simple multi-page PDF -----------

_TRANSLIT = {
    "—": "--", "–": "-", "‘": "'", "’": "'", "“": '"', "”": '"', "…": "...",
    "→": "->", "←": "<-", "⇒": "=>", "≈": "~=", "≃": "~=", "≤": "<=", "≥": ">=",
    "×": "x", "·": "*", "−": "-", "∞": "inf", "≠": "!=", "±": "+/-",
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "Δ": "Delta",
    "ε": "eps", "λ": "lambda", "μ": "mu", "π": "pi", "ρ": "rho", "σ": "sigma",
    "τ": "tau", "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega", "Ω": "Omega",
    "ℏ": "hbar", "√": "sqrt", "∑": "sum", "∏": "prod", "∈": "in", "⊗": "(x)",
    "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "²": "^2", "³": "^3", "⁴": "^4",
    "🔧": "[tool]", "⋄": "*",
}


def _latin1(s):
    s = "".join(_TRANSLIT.get(ch, ch) for ch in s)
    return s.encode("latin-1", "replace").decode("latin-1")


def _pdf_escape(s):
    return s.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def _md_to_styled_lines(md_text, width=100):
    """Strip front matter; classify lines into (style, text) for the builtin PDF."""
    body = re.sub(r"\A---\n.*?\n---\n", "", md_text, flags=re.S)
    lines, in_fence = [], False
    for raw in body.splitlines():
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~~"):
            in_fence = not in_fence
            lines.append(("code", ""))
            continue
        if in_fence:
            # Preserve exact indentation/spacing (code is whitespace-
            # sensitive); only hard-chunk lines wider than the page.
            if len(raw) <= width:
                lines.append(("code", raw))
            else:
                for i in range(0, len(raw), width):
                    lines.append(("code", raw[i:i + width]))
            continue
        if stripped.startswith("# "):
            lines.append(("h1", stripped[2:]))
        elif stripped.startswith("## "):
            lines.append(("h2", stripped[3:]))
        elif stripped.startswith("### "):
            lines.append(("blank", ""))
            lines.append(("h3", stripped[4:]))
        elif stripped == "---":
            lines.append(("body", "-" * 60))
        elif not stripped:
            lines.append(("blank", ""))
        else:
            for seg in textwrap.wrap(raw, width=width,
                                     subsequent_indent="  ") or [""]:
                lines.append(("body", seg))
    return lines


_STYLE_FONT = {"h1": ("F2", 13), "h2": ("F2", 11), "h3": ("F2", 10),
               "body": ("F1", 9), "code": ("F3", 8), "blank": ("F1", 9)}


def builtin_pdf(md_text, pdf_path, title):
    """Dependency-free basic PDF (A4, Helvetica/Courier, Latin-1)."""
    page_w, page_h, margin, leading = 595, 842, 48, 11.5
    usable = page_h - margin - 60
    per_page = int(usable / leading)

    styled = _md_to_styled_lines(md_text)
    pages = [styled[i:i + per_page] for i in range(0, len(styled), per_page)] or [[]]

    streams = []
    for pi, page_lines in enumerate(pages):
        ops = ["BT", "%.1f TL" % leading, "1 0 0 1 %d %d Tm" % (margin, page_h - margin - 10)]
        cur = None
        for style, text in page_lines:
            font, size = _STYLE_FONT[style]
            if (font, size) != cur:
                ops.append("/%s %d Tf" % (font, size))
                cur = (font, size)
            ops.append("(%s) Tj T*" % _pdf_escape(_latin1(text)))
        ops.append("ET")
        footer = "Page %d of %d - %s" % (pi + 1, len(pages), _latin1(title)[:70])
        ops.append("BT /F1 7 Tf 1 0 0 1 %d 26 Tm (%s) Tj ET"
                   % (margin, _pdf_escape(footer)))
        streams.append("\n".join(ops).encode("latin-1"))

    objs = []  # 1-indexed object bodies
    n_pages = len(streams)
    kids = " ".join("%d 0 R" % (6 + 2 * k) for k in range(n_pages))
    objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(("<< /Type /Pages /Kids [%s] /Count %d >>" % (kids, n_pages)).encode())
    for name in ("Helvetica", "Helvetica-Bold", "Courier"):
        objs.append(("<< /Type /Font /Subtype /Type1 /BaseFont /%s "
                     "/Encoding /WinAnsiEncoding >>" % name).encode())
    for k, stream in enumerate(streams):
        objs.append((
            "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %d %d] "
            "/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
            "/Contents %d 0 R >>" % (page_w, page_h, 7 + 2 * k)
        ).encode())
        objs.append(b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
                    + stream + b"\nendstream")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for i, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += ("%d 0 obj\n" % i).encode() + body + b"\nendobj\n"
    xref_pos = len(out)
    out += ("xref\n0 %d\n" % (len(objs) + 1)).encode()
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += ("%010d 00000 n \n" % off).encode()
    out += ("trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF"
            % (len(objs) + 1, xref_pos)).encode()
    pdf_path.write_bytes(bytes(out))


def rerender_pdfs(root, args):
    """Re-render committed session PDFs with pandoc (CI / post-hoc upgrade).

    Targets sessions whose metadata records a non-pandoc engine (or whose
    PDF is missing); --force re-renders everything. No-op without pandoc.
    """
    engine = detect_engine(args.pdf_engine)
    if not engine or engine[0] != "pandoc":
        log("No pandoc+engine available — nothing to re-render "
            "(existing PDFs left as-is).")
        return 0
    fonts = (args.pdf_mainfont, args.pdf_monofont)
    n_done = n_skip = n_fallback = 0
    for md_path in sorted(root.glob("*/*/session.md")):
        sdir = md_path.parent
        meta_path = sdir / "metadata.json"
        pdf_path = sdir / "session.pdf"
        meta = {}
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                meta = {}
        current = meta.get("pdf_engine") or ""
        if pdf_path.exists() and current.startswith("pandoc") and not args.force:
            n_skip += 1
            continue
        md_text = md_path.read_text(encoding="utf-8")
        used = render_pdf(md_path, pdf_path, md_text,
                          meta.get("title") or sdir.name, engine, fonts=fonts)
        if used and used.startswith("pandoc"):
            n_done += 1
        else:
            n_fallback += 1
        if meta and meta.get("pdf_engine") != used:
            meta["pdf_engine"] = used
            meta_path.write_text(
                json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8")
        print("  %s: %s" % (sdir.relative_to(root), used))
    print("Re-render: %d upgraded, %d already pandoc, %d fell back to builtin."
          % (n_done, n_skip, n_fallback))
    return 0


def extract_refs_from_md(md_text):
    """Fallback ref extraction from an archived session.md (for sessions
    predating the stored refs_raw field)."""
    faux = {"title": "", "messages": [{"text": md_text, "tools": []}]}
    prs, branches, shas, sess = extract_refs(faux)
    return {"prs": prs, "branches": branches, "shas": shas,
            "session_ids_mentioned": sess}


def splice_related(md_text, related):
    """Replace the sentinel-delimited Related-work section. → new md, or None
    if the sentinels are absent (older archive predating them)."""
    if RELATED_BEGIN not in md_text or RELATED_END not in md_text:
        return None
    pre = md_text.split(RELATED_BEGIN, 1)[0]
    post = md_text.split(RELATED_END, 1)[1]
    return pre + "\n".join(related_md_lines(related)) + post


def retag(root, repo, args):
    """Recompute related-work tags for every archived session against the
    CURRENT git/GitHub state (no conversation input needed). Run post-merge
    so a newly-landed PR/commit attaches to the discussion it came from.
    Manual tags are preserved; INDEX.md + each session.md are refreshed."""
    trailers = repo.trailer_map() if repo.ok() else {}
    changed = 0
    for meta_path in sorted(root.glob("*/*/metadata.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        md_path = meta_path.parent / "session.md"
        refs_raw = meta.get("refs_raw")
        if refs_raw is None and md_path.exists():
            refs_raw = extract_refs_from_md(md_path.read_text(encoding="utf-8"))
        if refs_raw is None:
            continue
        manual = meta.get("related", {}).get("manual", [])
        new_related = build_related_from_refs(refs_raw, meta.get("id", ""),
                                              repo, trailers, args.github)
        new_related["manual"] = manual
        meta_changed = (new_related != meta.get("related")
                        or meta.get("refs_raw") != refs_raw)
        # Re-splice session.md when its Related section is out of sync with
        # the (recomputed + manual-preserved) tags — covers both newly-landed
        # commits and hand-edited related.manual.
        spliced = None
        md_changed = False
        if md_path.exists():
            cur_md = md_path.read_text(encoding="utf-8")
            spliced = splice_related(cur_md, new_related)
            md_changed = spliced is not None and spliced != cur_md
        if not meta_changed and not md_changed:
            continue
        if md_changed:
            md_path.write_text(spliced, encoding="utf-8")
            # Refresh the PDF from the re-spliced markdown so its Related
            # section stays consistent (renderer works straight from md).
            pdf_path = meta_path.parent / "session.pdf"
            engine = detect_engine(getattr(args, "pdf_engine", "auto"))
            used = render_pdf(md_path, pdf_path, spliced, meta.get("title") or "",
                              engine, fonts=(args.pdf_mainfont, args.pdf_monofont))
            if used and meta.get("pdf_engine") != used:
                meta["pdf_engine"] = used
                meta_changed = True
        if meta_changed:
            meta["related"] = new_related
            meta["refs_raw"] = refs_raw
            meta_path.write_text(
                json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        changed += 1
        print("  retagged %s" % meta_path.parent.relative_to(root))
    n = regenerate_index(root)
    print("Retag: %d session(s) updated; INDEX.md lists %d." % (changed, n))
    return 0


def screen_report(matched):
    """Print the sensitive-info screen for matched conversations; write
    nothing. Lets the user eyeball findings before archiving."""
    print("Sensitive-info screen (no files written):\n")
    any_secret = False
    for i, (conv, _hits) in enumerate(matched, 1):
        summary = screen_conv(conv, redact=False)  # scan only
        sev = screen_severity(summary)
        any_secret = any_secret or sev == "SECRET"
        findings = summary["flagged"]
        desc = ", ".join("%s x%d" % (k, v) for k, v in sorted(findings.items())) or "clean"
        print("  [%2d] %-7s %-8s %s" % (i, sev, conv["account"], conv["title"][:54]))
        print("        %s" % desc)
    if any_secret:
        print("\nWARNING: SECRET-class matches found. These are auto-redacted on "
              "archive (disable with --no-redact — NOT recommended for a public repo).")
    else:
        print("\nNo secret-class matches. PII (email/phone/ipv4) is flagged only; "
              "pass --redact-pii to mask it on archive.")
    return 0


# ----------------------------------------------------------------- indexing

def load_existing(root):
    """conversation id → (session_dir, metadata) for everything archived."""
    existing = {}
    for meta_path in root.glob("*/*/metadata.json"):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        key = (meta.get("account"), meta.get("id"))
        existing[key] = (meta_path.parent, meta)
    return existing


def regenerate_index(root):
    entries = []
    for meta_path in sorted(root.glob("*/*/metadata.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        entries.append((meta, meta_path.parent.relative_to(root)))

    by_account = {}
    for meta, rel in entries:
        by_account.setdefault(meta.get("account", "?"), []).append((meta, rel))

    L = ["# Index of archived discussions", ""]
    L.append("*Auto-generated by `tools/archive_sessions.py` — do not edit by hand. "
             "%d session(s) across %d account(s); updated %s.*"
             % (len(entries), len(by_account),
                datetime.now(timezone.utc).strftime("%Y-%m-%d")))
    L.append("")
    for account in sorted(by_account):
        rows = by_account[account]
        rows.sort(key=lambda mr: mr[0].get("created_at") or "", reverse=True)
        L.append("## %s" % account)
        L.append("")
        L.append("| Date | Discussion | PDF | Related |")
        L.append("|---|---|---|---|")
        for meta, rel in rows:
            date = (meta.get("created_at") or "?")[:10]
            title = md_cell(meta.get("title") or "(untitled)")
            rel_posix = rel.as_posix()
            related = meta.get("related", {})
            cells = []
            for pr in related.get("prs", []):
                cells.append("[#%d](%s)" % (pr["number"], pr["url"]))
            for c in related.get("commits", []):
                cells.append("`%s`" % c["sha"][:8])
            for b in related.get("branches", []):
                cells.append("`%s`" % b["name"])
            for mtag in related.get("manual", []):
                cells.append(md_cell(str(mtag)))
            rel_cell = ", ".join(cells[:12]) or "—"
            L.append("| %s | [%s](%s/session.md) | [PDF](%s/session.pdf) | %s |"
                     % (date, title, rel_posix, rel_posix, rel_cell))
        L.append("")
    (root / "INDEX.md").write_text("\n".join(L), encoding="utf-8")
    return len(entries)


# ----------------------------------------------------------------- archiving

def archive_one(conv, hits, root, repo, trailers, engine, opts, existing):
    key = (conv["account"], conv["id"])
    prior = existing.get(key)
    if prior:
        out_dir, prior_meta = prior
        prior_updated = parse_ts(prior_meta.get("updated_at"))
        if not opts.force and prior_updated and conv["updated_at"] \
                and conv["updated_at"] <= prior_updated:
            return out_dir, "skipped (already archived)"
        manual = prior_meta.get("related", {}).get("manual", [])
        status = "updated"
    else:
        date = conv["created_at"] or conv["updated_at"] or datetime.now(timezone.utc)
        dirname = "%s-%s" % (date.strftime("%Y-%m-%d"), slugify(conv["title"]))
        out_dir = root / conv["account"] / dirname
        if out_dir.exists():
            dirname += "-" + str(conv["id"])[:8]
            out_dir = root / conv["account"] / dirname
        manual = []
        status = "archived"

    related, refs_raw = build_related(conv, repo, trailers, opts.github)
    related["manual"] = manual

    # Sensitive-info screen: redact secrets (always) + PII (opt-in) BEFORE
    # rendering, so neither md nor PDF can carry them into the public repo.
    screen = screen_conv(conv, redact=not opts.no_redact, redact_pii=opts.redact_pii)
    if screen["redacted"]:
        log("    screen: redacted %s" % screen["redacted"])
    if screen["flagged"]:
        log("    screen: FLAGGED (left in place, review) %s" % screen["flagged"])

    md_text = render_markdown(conv, related, hits, opts)
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "session.md"
    pdf_path = out_dir / "session.pdf"
    md_path.write_text(md_text, encoding="utf-8")
    engine_used = render_pdf(md_path, pdf_path, md_text, conv["title"], engine,
                             fonts=(opts.pdf_mainfont, opts.pdf_monofont))

    meta = {
        "schema": "human-agent-discussions/metadata@1",
        "account": conv["account"],
        "source": conv["source"],
        "id": conv["id"],
        "url": conv.get("url"),
        "title": conv["title"],
        "created_at": iso(conv["created_at"]),
        "updated_at": iso(conv["updated_at"]),
        "message_count": len(conv["messages"]),
        "keyword_hits": hits,
        "related": related,
        "refs_raw": refs_raw,
        "screen": screen,
        "pdf_engine": engine_used,
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "archiver": "archive_sessions.py@" + VERSION,
        "extra": conv.get("extra", {}),
    }
    (out_dir / "metadata.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out_dir, status


# ----------------------------------------------------------------- CLI flow

def discover_inputs(args, root):
    """→ list of (account, kind, path); kind ∈ {export, jsonl}."""
    pairs = []

    def add_path(account, p):
        p = Path(p).expanduser()
        if p.is_dir():
            for f in sorted(p.rglob("conversations*.json")):
                pairs.append((account, "export", f))
            for f in sorted(p.rglob("*.jsonl")):
                pairs.append((account, "jsonl", f))
        elif p.suffix == ".jsonl":
            pairs.append((account, "jsonl", p))
        elif p.suffix == ".json":
            pairs.append((account, "export", p))
        else:
            log("WARN: skipping %s (not .json/.jsonl/dir)" % p)

    if args.export:
        for spec in args.export:
            account, sep, path = spec.partition("=")
            if not sep:
                log("ERROR: --export needs ACCOUNT=PATH (got %r)" % spec)
                sys.exit(2)
            account = account.strip().lower()
            if not ACCOUNT_RE.match(account):
                log("ERROR: bad account alias %r (lowercase letters/digits/hyphens)" % account)
                sys.exit(2)
            add_path(account, path)
    else:
        incoming = root / "_incoming"
        if incoming.is_dir():
            for sub in sorted(incoming.iterdir()):
                if sub.is_dir() and ACCOUNT_RE.match(sub.name):
                    add_path(sub.name, sub)
    return pairs


def parse_select(spec, n):
    if spec.strip().lower() == "all":
        return list(range(n))
    idxs = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            idxs.update(range(int(a) - 1, int(b)))
        else:
            idxs.add(int(part) - 1)
    return sorted(i for i in idxs if 0 <= i < n)


def find_repo_root(start):
    p = Path(start).resolve()
    for cand in [p] + list(p.parents):
        if (cand / ".git").exists():
            return cand
    return p


def collect_keywords(args):
    keywords = [] if args.no_default_keywords else list(DEFAULT_KEYWORDS)
    keywords += args.keyword or []
    if args.keywords_file:
        for line in Path(args.keywords_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                keywords.append(line)
    return keywords


def main(argv=None):
    default_root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(
        description="Archive QOU-related Claude sessions to human-agent-discussions/.")
    ap.add_argument("--export", action="append", metavar="ACCOUNT=PATH",
                    help="conversations.json / .jsonl / directory for an account "
                         "(repeatable; default: scan _incoming/<account>/)")
    ap.add_argument("--select", metavar="all|1,3-5",
                    help="which matches to archive (omit to just list)")
    ap.add_argument("--list", action="store_true", help="list matches and exit")
    ap.add_argument("--force", action="store_true",
                    help="re-archive even if already archived and unchanged")
    ap.add_argument("--keyword", action="append", metavar="KW",
                    help="extra filter keyword (repeatable)")
    ap.add_argument("--keywords-file", metavar="FILE",
                    help="file with one keyword per line")
    ap.add_argument("--no-default-keywords", action="store_true",
                    help="drop the built-in QOU keyword list")
    ap.add_argument("--include-thinking", action="store_true",
                    help="include assistant thinking blocks (Claude Code logs)")
    ap.add_argument("--tools", choices=["summary", "full", "none"], default="summary",
                    help="how to render tool calls (default: summary)")
    ap.add_argument("--attachment-chars", type=int, default=0, metavar="N",
                    help="include up to N chars of each attachment (default 0: name only)")
    ap.add_argument("--pdf-engine", choices=["auto", "pandoc", "builtin", "none"],
                    default="auto")
    ap.add_argument("--pdf-mainfont", metavar="FONT", default=None,
                    help="mainfont for pandoc+xelatex (e.g. 'DejaVu Serif')")
    ap.add_argument("--pdf-monofont", metavar="FONT", default=None,
                    help="monofont for pandoc+xelatex (e.g. 'DejaVu Sans Mono')")
    ap.add_argument("--rerender-pdfs", action="store_true",
                    help="re-render archived PDFs with pandoc (with --force: all) "
                         "and exit; used by CI to upgrade builtin-engine PDFs")
    ap.add_argument("--root", type=Path, default=default_root,
                    help="archive root (default: %s)" % default_root)
    ap.add_argument("--repo", type=Path, default=None,
                    help="git repo for tagging (default: auto-detect)")
    ap.add_argument("--github", action="store_true",
                    help="enrich tags via the gh CLI (PR titles, branch→PR, commit→PR)")
    ap.add_argument("--no-redact", action="store_true",
                    help="do NOT auto-redact detected secrets (not recommended "
                         "for a public repo)")
    ap.add_argument("--redact-pii", action="store_true",
                    help="also redact PII (email / phone / ipv4), not just secrets")
    ap.add_argument("--screen", action="store_true",
                    help="report the sensitive-info screen for matches and exit "
                         "(writes nothing)")
    ap.add_argument("--reindex", action="store_true",
                    help="only regenerate INDEX.md and exit")
    ap.add_argument("--retag", action="store_true",
                    help="recompute related-work tags for already-archived sessions "
                         "against current git/GitHub state and exit (post-merge); "
                         "no conversation input needed")
    ap.add_argument("--self-test", action="store_true",
                    help="run the end-to-end fixture self-test and exit")
    ap.add_argument("--version", action="version", version="%(prog)s " + VERSION)
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    root = args.root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    repo = Repo(args.repo or find_repo_root(root))
    if not repo.ok():
        log("WARN: %s is not a git repo — tagging disabled signals will be empty" % repo.path)

    if args.reindex:
        n = regenerate_index(root)
        log("INDEX.md regenerated (%d sessions)." % n)
        return 0

    if args.rerender_pdfs:
        return rerender_pdfs(root, args)

    if args.retag:
        return retag(root, repo, args)

    pairs = discover_inputs(args, root)
    if not pairs:
        log("No inputs. Drop exports into %s/_incoming/<account>/ or use "
            "--export ACCOUNT=PATH. See README.md." % root)
        return 1

    keywords = collect_keywords(args)
    convs = []
    for account, kind, path in pairs:
        if kind == "export":
            batch = parse_claude_export(path, account, args)
            log("Parsed %s (%s): %d conversation(s)" % (path.name, account, len(batch)))
            convs.extend(batch)
        else:
            c = parse_code_jsonl(path, account, args)
            if c:
                convs.append(c)

    matched = []
    for conv in convs:
        hits = keyword_hits(conv, keywords)
        if hits:
            matched.append((conv, hits))
    matched.sort(key=lambda ch: (ch[0]["created_at"] or datetime.min.replace(tzinfo=timezone.utc)))

    if args.screen:
        return screen_report(matched)

    existing = load_existing(root)

    print("QOU-related conversations: %d matched of %d scanned.\n"
          % (len(matched), len(convs)))
    any_secret = False
    for i, (conv, hits) in enumerate(matched, 1):
        key = (conv["account"], conv["id"])
        if key not in existing:
            status = "NEW"
        else:
            prior_updated = parse_ts(existing[key][1].get("updated_at"))
            status = ("UPDATED" if prior_updated and conv["updated_at"]
                      and conv["updated_at"] > prior_updated else "archived")
        sev = screen_severity(screen_conv(conv, redact=False))  # scan only
        any_secret = any_secret or sev == "SECRET"
        print("  [%2d] %s  %-12s %4d msgs  %-8s  %-6s  %s" % (
            i, (conv["created_at"] or conv["updated_at"]).strftime("%Y-%m-%d")
            if (conv["created_at"] or conv["updated_at"]) else "????-??-??",
            conv["account"], len(conv["messages"]), status, sev,
            conv["title"][:64]))
        print("        hits: %s" % ", ".join(hits))

    if any_secret:
        print("\nWARNING: SECRET-class matches present; auto-redacted on archive "
              "(see --screen for detail, --no-redact to disable).")

    if args.list or not args.select:
        if not args.list:
            print("\nNothing written. Re-run with --select all (or --select 1,3-5). "
                  "Use --screen first to review sensitive-info findings.")
        return 0

    sel = parse_select(args.select, len(matched))
    if not sel:
        log("Selection matched nothing.")
        return 1

    engine = detect_engine(args.pdf_engine)
    trailers = repo.trailer_map() if repo.ok() else {}
    log("\nPDF engine: %s | session-trailer commits known: %d"
        % ("+".join(engine) if engine else "none", sum(len(v) for v in trailers.values())))

    results = []
    for i in sel:
        conv, hits = matched[i]
        out_dir, status = archive_one(conv, hits, root, repo, trailers,
                                      engine, args, existing)
        results.append((out_dir, status))
        print("  -> %s: %s" % (out_dir.relative_to(root), status))

    n = regenerate_index(root)
    print("\nDone. %d session(s) processed; INDEX.md lists %d total." % (len(results), n))
    print("Review with `git status`, then commit + push.")
    return 0


# ----------------------------------------------------------------- self-test

def self_test():
    repo_root = find_repo_root(Path(__file__).parent)
    repo = Repo(repo_root)
    assert repo.ok(), "self-test must run inside the qou repo"
    rc, head, _ = run(["git", "rev-parse", "HEAD"], cwd=repo_root)
    assert rc == 0
    head = head.strip()
    trailers = repo.trailer_map()
    sid0 = next(iter(sorted(trailers)), None)
    print("self-test: repo=%s head=%s trailer-sessions=%d"
          % (repo_root, head[:12], len(trailers)))

    qou_text = (
        "Let's revisit the Q_beta c_3 truncation order in litlfred/qou. "
        "PR #1821 settled the real-q family; commit %s is the latest probe. "
        "Branch claude/qbeta-ck-audit-2026-05-31 had the audit doc. "
        "My key is sk-ant-api03-AAAABBBBCCCCDDDDEEEE1111 and token "
        "ghp_AAAABBBBCCCCDDDDEEEE1111; reach me at alice@example.com." % head[:10]
    )
    if sid0:
        qou_text += " The Code session was https://claude.ai/code/%s." % sid0
    export = [
        {
            "uuid": "11111111-2222-3333-4444-555555555555",
            "name": "QOU: Q_beta c_3 truncation order discussion",
            "created_at": "2026-06-01T12:00:00Z",
            "updated_at": "2026-06-01T13:00:00Z",
            "chat_messages": [
                {"sender": "human", "created_at": "2026-06-01T12:00:00Z",
                 "text": qou_text},
                {"sender": "assistant", "created_at": "2026-06-01T12:01:00Z",
                 "text": "Recall $c_2 = -1$ is Taylor-exact while $c_3$ is a "
                         "near-match; the truncation order $N$ is chosen by "
                         "target precision — *not* a wire/un-wire gate."},
            ],
        },
        {
            "uuid": "99999999-8888-7777-6666-555555555555",
            "name": "Pasta recipes",
            "created_at": "2026-06-02T12:00:00Z",
            "updated_at": "2026-06-02T12:30:00Z",
            "chat_messages": [
                {"sender": "human", "text": "Best cacio e pepe technique?"},
                {"sender": "assistant", "text": "Toss quickly off heat."},
            ],
        },
    ]
    jsonl_lines = [
        {"type": "summary", "summary": "fix lean build for hecke module"},
        {"type": "user", "sessionId": "aaaa-bbbb", "cwd": "/home/user/qou",
         "gitBranch": "claude/test-branch", "timestamp": "2026-06-03T10:00:00Z",
         "message": {"role": "user", "content": [
             {"type": "text", "text": "lake build QOU fails on HeckeH3"}]}},
        {"type": "assistant", "sessionId": "aaaa-bbbb", "cwd": "/home/user/qou",
         "timestamp": "2026-06-03T10:01:00Z",
         "message": {"role": "assistant", "content": [
             {"type": "text", "text": "Import was missing; fixed."},
             {"type": "tool_use", "name": "Bash", "input": {"command": "lake build QOU"}}]}},
    ]

    tmp = Path(tempfile.mkdtemp(prefix="had-selftest-"))
    try:
        inbox = tmp / "in" / "testacct"
        inbox.mkdir(parents=True)
        (inbox / "conversations.json").write_text(json.dumps(export), encoding="utf-8")
        (inbox / "session1.jsonl").write_text(
            "\n".join(json.dumps(l) for l in jsonl_lines), encoding="utf-8")
        archive_root = tmp / "archive"

        argv = ["--export", "testacct=" + str(inbox), "--root", str(archive_root),
                "--repo", str(repo_root), "--select", "all"]
        rc = main(argv)
        assert rc == 0, "main() failed"

        metas = list(archive_root.glob("testacct/*/metadata.json"))
        assert len(metas) == 2, "expected 2 archived sessions, got %d" % len(metas)
        by_title = {}
        for mp in metas:
            meta = json.loads(mp.read_text(encoding="utf-8"))
            by_title[meta["title"]] = meta
            pdf = mp.parent / "session.pdf"
            assert pdf.exists() and pdf.read_bytes()[:5] == b"%PDF-", "bad PDF for " + meta["title"]
            assert (mp.parent / "session.md").exists()

        qmeta = by_title["QOU: Q_beta c_3 truncation order discussion"]
        rel = qmeta["related"]
        assert any(p["number"] == 1821 for p in rel["prs"]), "PR #1821 not tagged"
        assert any(c["sha"].startswith(head[:10]) and c["evidence"] == "mentioned"
                   for c in rel["commits"]), "mentioned HEAD sha not verified"
        assert any(b["name"] == "claude/qbeta-ck-audit-2026-05-31"
                   for b in rel["branches"]), "branch not tagged"
        if sid0:
            assert sid0 in rel["session_ids"], "session id not captured"
            assert any(c["evidence"] == "session-trailer" for c in rel["commits"]), \
                "session-trailer commit not linked"

        cmeta = by_title["fix lean build for hecke module"]
        assert "cwd:qou" in cmeta["keyword_hits"], "claude-code cwd match missing"

        # refs_raw persisted for post-merge retag
        assert 1821 in qmeta.get("refs_raw", {}).get("prs", []), "refs_raw missing PRs"

        # sensitive-info screen: secrets redacted, PII flagged-not-redacted
        qdir = next(p.parent for p in metas
                    if json.loads(p.read_text())["title"].startswith("QOU:"))
        qmd = (qdir / "session.md").read_text(encoding="utf-8")
        assert "sk-ant-api03-AAAABBBB" not in qmd, "anthropic key not redacted"
        assert "ghp_AAAABBBB" not in qmd, "github token not redacted"
        assert "[REDACTED-anthropic-key]" in qmd, "redaction marker missing"
        assert "alice@example.com" in qmd, "email should be flagged, not redacted by default"
        assert qmeta["screen"]["redacted"].get("anthropic-key", 0) >= 1
        assert qmeta["screen"]["flagged"].get("email", 0) >= 1, "email not flagged"
        assert RELATED_BEGIN in qmd, "related-work splice sentinels missing"

        index = (archive_root / "INDEX.md").read_text(encoding="utf-8")
        assert "Q_beta c_3" in index and "Pasta" not in index

        # idempotency: second run skips both
        rc = main(argv)
        assert rc == 0
        metas2 = list(archive_root.glob("testacct/*/metadata.json"))
        assert len(metas2) == 2, "idempotent re-run created extra dirs"

        # retag: inject a manual tag, recompute against current state, confirm
        # auto-tags survive, manual tag is preserved + spliced into session.md
        qmp = qdir / "metadata.json"
        qm = json.loads(qmp.read_text(encoding="utf-8"))
        qm["related"]["manual"] = ["PR #9999 (hand-added)"]
        qmp.write_text(json.dumps(qm, indent=2) + "\n", encoding="utf-8")
        rc = main(["--retag", "--root", str(archive_root), "--repo", str(repo_root)])
        assert rc == 0, "retag failed"
        qm2 = json.loads(qmp.read_text(encoding="utf-8"))
        assert any(p["number"] == 1821 for p in qm2["related"]["prs"]), "retag lost auto tag"
        assert "PR #9999 (hand-added)" in qm2["related"]["manual"], "retag dropped manual tag"
        qmd2 = (qdir / "session.md").read_text(encoding="utf-8")
        assert "PR #9999 (hand-added)" in qmd2, "manual tag not spliced into session.md"
        # retag again = no-op (idempotent)
        rc = main(["--retag", "--root", str(archive_root), "--repo", str(repo_root)])
        assert rc == 0

        print("SELF-TEST PASS (2 sessions archived; tagging + PDF + index + "
              "screen-redaction + retag OK; engine=%s)" % qmeta["pdf_engine"])
        shutil.rmtree(tmp, ignore_errors=True)
        return 0
    except AssertionError as e:
        print("SELF-TEST FAIL: %s\n(artifacts kept at %s)" % (e, tmp))
        return 1


if __name__ == "__main__":
    sys.exit(main())
