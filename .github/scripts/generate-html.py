#!/usr/bin/env python3
"""generate-html.py — enhance Pandoc HTML with dark mode, TOC header, and definition links.

Usage
-----
    python generate-html.py INPUT_HTML FLAT_TEX OUTPUT_HTML [--branch BRANCH] [--repo OWNER/REPO] [--sha SHA]

The script:
1. Parses the flattened LaTeX source to extract labelled definitions (and other
   theorem-like environments) together with their display names.
2. Reads the Pandoc-generated HTML.
3. Injects:
   - a ``<style>`` block supporting light / dark mode (auto via
     ``prefers-color-scheme`` **and** a manual toggle button);
   - a sticky header bar with a dropdown table-of-contents;
   - in-text links from each use of a defined term back to its definition
     anchor.
4. When ``--branch`` is provided (feature-branch builds):
   - adds GitHub branch / PR / issue links in the header;
   - adds a small source-link icon next to every definition / theorem heading.

Requires only the Python 3 standard library (>=3.8).
"""

from __future__ import annotations

import argparse
import html as html_mod
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# 1.  LaTeX parsing helpers
# ---------------------------------------------------------------------------

# Matches \begin{env}[optional title]\n\label{lbl} with optional \lean{} and \leanok
_ENV_RE = re.compile(
    r"\\begin\{("
    r"definition|theorem|lemma|proposition|corollary|example|remark|conjecture"
    r")\}"
    r"(?:\[([^\]]*)\])?"       # optional [Title]
    r"\s*\\label\{([^}]+)\}",  # \label{...}
    re.DOTALL,
)

# Matches \lean{Decl.Name} within environment body
_LEAN_DECL_RE = re.compile(r"\\lean\{([^}]+)\}")
# Matches \leanok within environment body
_LEANOK_RE = re.compile(r"\\leanok\b")

# Matches \chapter / \section / \subsection with optional \label
_HEADING_RE = re.compile(
    r"\\(chapter|section|subsection)\{([^}]+)\}\s*(?:\\label\{([^}]+)\})?",
)


def _strip_tex(s: str) -> str:
    """Rough plain-text rendering of a short TeX snippet."""
    s = re.sub(r"\\(?:emph|textbf|textit|mathrm|mathbb|operatorname)\{([^}]*)\}", r"\1", s)
    s = s.replace("\\\\", " ")
    s = re.sub(r"[${}\\]", "", s)
    return s.strip()


def parse_definitions(tex: str) -> list[dict]:
    """Return a list of dicts ``{env, title, label, plain_title, lean_decl, leanok}``."""
    defs: list[dict] = []
    for m in _ENV_RE.finditer(tex):
        env, title, label = m.group(1), m.group(2) or "", m.group(3)
        # Scan ahead from the match to find \lean{} and \leanok within the environment
        rest_start = m.end()
        end_env = tex.find(f"\\end{{{env}}}", rest_start)
        body = tex[rest_start:end_env] if end_env != -1 else tex[rest_start:rest_start + 500]
        lean_m = _LEAN_DECL_RE.search(body)
        lean_decl = lean_m.group(1).strip() if lean_m else ""
        leanok = bool(_LEANOK_RE.search(body))
        defs.append({
            "env": env,
            "title": title,
            "label": label,
            "plain_title": _strip_tex(title) if title else "",
            "lean_decl": lean_decl,
            "leanok": leanok,
        })
    return defs


def parse_headings(tex: str) -> list[dict]:
    """Return chapter / section / subsection headings with labels."""
    headings: list[dict] = []
    for m in _HEADING_RE.finditer(tex):
        level, title, label = m.group(1), m.group(2), m.group(3) or ""
        headings.append({
            "level": level,
            "title": _strip_tex(title),
            "label": label,
        })
    return headings


def _find_env_line(tex: str, label: str) -> int | None:
    """Return the 1-based line number of ``\\label{label}`` in *tex*."""
    for i, line in enumerate(tex.splitlines(), 1):
        if f"\\label{{{label}}}" in line:
            return i
    return None


def _find_label_in_sources(label: str, src_dir: str = ".") -> tuple[str, int] | None:
    """Find *label* in original chapter files and return ``(rel_path, line_no)``.

    Falls back to scanning all ``.tex`` files under *src_dir*.
    """
    chapters_dir = os.path.join(src_dir, "chapters")
    tex_files: list[str] = []
    if os.path.isdir(chapters_dir):
        for fn in sorted(os.listdir(chapters_dir)):
            if fn.endswith(".tex"):
                tex_files.append(os.path.join("chapters", fn))
    # Also check main.tex
    main_path = os.path.join(src_dir, "main.tex")
    if os.path.isfile(main_path):
        tex_files.append("main.tex")

    needle = f"\\label{{{label}}}"
    for rel_path in tex_files:
        full = os.path.join(src_dir, rel_path)
        if not os.path.isfile(full):
            continue
        for i, line in enumerate(open(full, encoding="utf-8", errors="replace"), 1):
            if needle in line:
                return (rel_path, i)
    return None


# ---------------------------------------------------------------------------
# 2.  HTML helpers
# ---------------------------------------------------------------------------

_DARK_LIGHT_CSS = r"""
/* ── Base (light) ───────────────────────────────────────────────── */
:root {
  --bg:          #ffffff;
  --fg:          #1a1a1a;
  --link:        #0055cc;
  --heading:     #111111;
  --pre-bg:      #f6f8fa;
  --pre-border:  #e1e4e8;
  --header-bg:   #f0f0f0;
  --header-fg:   #222;
  --toc-bg:      #ffffff;
  --toc-shadow:  rgba(0,0,0,0.15);
  --badge-bg:    #e8e8e8;
  --badge-fg:    #333;
  --border:      #ddd;
  --src-link:    #888;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:          #181a1b;
    --fg:          #d4d4d4;
    --link:        #6cb4ff;
    --heading:     #e0e0e0;
    --pre-bg:      #2a2d2e;
    --pre-border:  #444;
    --header-bg:   #23272a;
    --header-fg:   #d4d4d4;
    --toc-bg:      #23272a;
    --toc-shadow:  rgba(0,0,0,0.5);
    --badge-bg:    #333;
    --badge-fg:    #ccc;
    --border:      #444;
    --src-link:    #888;
  }
}
[data-theme="dark"] {
  --bg:          #181a1b;
  --fg:          #d4d4d4;
  --link:        #6cb4ff;
  --heading:     #e0e0e0;
  --pre-bg:      #2a2d2e;
  --pre-border:  #444;
  --header-bg:   #23272a;
  --header-fg:   #d4d4d4;
  --toc-bg:      #23272a;
  --toc-shadow:  rgba(0,0,0,0.5);
  --badge-bg:    #333;
  --badge-fg:    #ccc;
  --border:      #444;
  --src-link:    #888;
}
body {
  max-width: 860px; margin: 0 auto; padding: 70px 1.2rem 2rem;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.7; color: var(--fg); background: var(--bg);
  transition: background 0.25s, color 0.25s;
}
h1,h2,h3,h4,h5,h6 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: var(--heading);
}
a { color: var(--link); }
pre, code.sourceCode {
  background: var(--pre-bg); border: 1px solid var(--pre-border);
  padding: 0.6em 0.8em; border-radius: 4px; overflow-x: auto;
}
code { font-size: 90%; }

/* ── Sticky header ──────────────────────────────────────────────── */
#site-header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  background: var(--header-bg); color: var(--header-fg);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 1rem; height: 48px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 0.9rem;
}
#site-header .title { font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
#site-header .controls { display: flex; gap: 0.5rem; align-items: center; }

/* TOC dropdown */
.toc-wrapper { position: relative; }
.toc-btn {
  background: none; border: 1px solid var(--border); color: var(--header-fg);
  padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 0.85rem;
}
.toc-btn:hover { background: var(--badge-bg); }
.toc-dropdown {
  display: none; position: absolute; right: 0; top: 110%;
  background: var(--toc-bg); border: 1px solid var(--border);
  border-radius: 6px; padding: 0.6rem 0;
  min-width: 280px; max-height: 70vh; overflow-y: auto;
  box-shadow: 0 4px 16px var(--toc-shadow); z-index: 1001;
}
.toc-dropdown.open { display: block; }
.toc-dropdown a {
  display: block; padding: 4px 1rem; text-decoration: none;
  color: var(--fg); font-size: 0.85rem; white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis;
}
.toc-dropdown a:hover { background: var(--badge-bg); }
.toc-dropdown a.toc-ch  { font-weight: 700; padding-left: 1rem; }
.toc-dropdown a.toc-sec { padding-left: 2rem; }
.toc-dropdown a.toc-ssec{ padding-left: 3rem; font-size: 0.8rem; }

/* Theme toggle */
.theme-toggle {
  background: none; border: 1px solid var(--border); color: var(--header-fg);
  padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 1rem;
  line-height: 1;
}

/* Source links & badges */
.src-link { color: var(--src-link); text-decoration: none; font-size: 0.8em; margin-left: 0.4em; }
.src-link:hover { color: var(--link); }
.gh-badge {
  display: inline-block; background: var(--badge-bg); color: var(--badge-fg);
  padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; text-decoration: none;
  margin-right: 0.4rem;
}
.gh-badge:hover { filter: brightness(0.9); }
#gh-bar { padding: 2px 0; }
.defn-link { border-bottom: 1px dotted var(--link); text-decoration: none; }

/* ── Proof-status badges ───────────────────────────────────────── */
.proof-status {
  display: inline-block; font-size: 0.75em; padding: 1px 7px;
  border-radius: 10px; margin-left: 0.5em; text-decoration: none;
  font-weight: 600; vertical-align: middle; line-height: 1.6;
  transition: filter 0.15s;
}
.proof-status:hover { filter: brightness(0.85); }
.proof-status.proved {
  background: #228B22; color: #fff;
}
.proof-status.stated {
  background: #DAA520; color: #fff;
}
.proof-status.has-sorry {
  background: #FF8C00; color: #fff;
}
.proof-status.not-started {
  background: #DC143C; color: #fff;
}
.proof-status.mathlib-ok {
  background: #006400; color: #fff;
}
/* Legend bar */
.proof-legend {
  text-align: center; padding: 6px 0; font-size: 0.8rem;
  border-bottom: 1px solid var(--border); margin-bottom: 1rem;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.proof-legend .proof-status { cursor: default; pointer-events: none; }
"""

_TOGGLE_JS = r"""
<script>
(function(){
  var root = document.documentElement;
  var btn  = document.getElementById('theme-toggle');
  var saved = localStorage.getItem('theme');
  if (saved) root.setAttribute('data-theme', saved);
  btn.addEventListener('click', function(){
    var cur = root.getAttribute('data-theme');
    var next;
    if (!cur) {
      // currently following system; pick the opposite of system pref
      next = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'light' : 'dark';
    } else {
      next = cur === 'dark' ? 'light' : 'dark';
    }
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    btn.textContent = next === 'dark' ? '\u2600\uFE0F' : '\uD83C\uDF19';
  });
  // set initial icon
  var isDark = saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches);
  btn.textContent = isDark ? '\u2600\uFE0F' : '\uD83C\uDF19';
})();

// TOC dropdown
(function(){
  var btn = document.getElementById('toc-btn');
  var dd  = document.getElementById('toc-dropdown');
  if (!btn || !dd) return;
  btn.addEventListener('click', function(e){ e.stopPropagation(); dd.classList.toggle('open'); });
  document.addEventListener('click', function(){ dd.classList.remove('open'); });
  dd.addEventListener('click', function(e){ if(e.target.tagName==='A') dd.classList.remove('open'); });
})();
</script>
"""


def _make_toc_html(headings: list[dict]) -> str:
    """Build the TOC dropdown ``<div>`` from parsed headings."""
    lines: list[str] = ['<div id="toc-dropdown" class="toc-dropdown">']
    for h in headings:
        cls_map = {"chapter": "toc-ch", "section": "toc-sec", "subsection": "toc-ssec"}
        cls = cls_map.get(h["level"], "toc-sec")
        anchor = h["label"] or re.sub(r"\W+", "-", h["title"].lower()).strip("-")
        lines.append(f'  <a class="{cls}" href="#{anchor}">{html_mod.escape(h["title"])}</a>')
    lines.append("</div>")
    return "\n".join(lines)


def _make_header_html(
    headings: list[dict],
    branch: str | None = None,
    repo: str | None = None,
) -> str:
    """Build the sticky header bar."""
    parts: list[str] = []
    parts.append('<header id="site-header">')
    parts.append('  <span class="title">Quantum Observable Universe</span>')
    parts.append('  <span class="controls">')

    # GitHub badges (feature branch)
    if branch and repo:
        repo_url = f"https://github.com/{repo}"
        parts.append(f'    <a class="gh-badge" href="{repo_url}/tree/{branch}"'
                     f' target="_blank">&#x1F33F; {html_mod.escape(branch)}</a>')

    # TOC dropdown
    parts.append('    <span class="toc-wrapper">')
    parts.append('      <button id="toc-btn" class="toc-btn">&#9776; Contents</button>')
    parts.append("      " + _make_toc_html(headings).replace("\n", "\n      "))
    parts.append("    </span>")

    # Theme toggle
    parts.append('    <button id="theme-toggle" class="theme-toggle" '
                 'aria-label="Toggle light/dark mode">&#x1F319;</button>')

    parts.append("  </span>")
    parts.append("</header>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# 2b. Proof-status badge injection
# ---------------------------------------------------------------------------

_LEAN_DOCS_BASE = "https://litlfred.github.io/qou/lean/"
_LEAN_SRC_BASE = "https://github.com/litlfred/qou/blob/main/lean/"

_STATUS_LABELS = {
    "proved":      ("&#x2713; proved",   "proved"),
    "mathlib_ok":  ("&#x2713;&#x2713; mathlib", "mathlib-ok"),
    "stated":      ("&#x2200; stated",   "stated"),
    "has_sorry":   ("&#x26A0; sorry",    "has-sorry"),
    "not_started": ("&#x2717; no Lean",  "not-started"),
}


def _proof_status_for_def(d: dict, manifest_lookup: dict) -> str:
    """Return the formalization status string for a definition dict."""
    label = d["label"]
    # Check manifest first (authoritative)
    if label in manifest_lookup:
        return manifest_lookup[label].get("formalization_status", "not_started")
    # Fall back to LaTeX parsing
    if d.get("lean_decl"):
        return "proved" if d.get("leanok") else "stated"
    return "not_started"


def _make_status_badge(status: str, lean_decl: str = "", lean_file: str = "") -> str:
    """Build an HTML badge element for the given proof status."""
    label_text, css_class = _STATUS_LABELS.get(status, _STATUS_LABELS["not_started"])
    if lean_decl:
        href = f"{_LEAN_DOCS_BASE}{lean_decl}"
        return (f'<a class="proof-status {css_class}" href="{href}" '
                f'target="_blank" title="Lean: {html_mod.escape(lean_decl)}">'
                f'{label_text}</a>')
    return f'<span class="proof-status {css_class}">{label_text}</span>'


def _make_proof_legend() -> str:
    """Build the proof-status legend bar."""
    parts = ['<div class="proof-legend"><strong>Proof status:</strong> ']
    for status, (label_text, css_class) in _STATUS_LABELS.items():
        parts.append(f'<span class="proof-status {css_class}">{label_text}</span> ')
    parts.append("</div>")
    return "".join(parts)


def _inject_proof_badges(
    body_html: str,
    defs: list[dict],
    manifest_path: str | None = None,
) -> str:
    """Insert proof-status badges next to each definition/theorem heading in the HTML."""
    # Build lookup from manifest if available
    manifest_lookup: dict[str, dict] = {}
    if manifest_path and os.path.isfile(manifest_path):
        try:
            with open(manifest_path, encoding="utf-8") as f:
                data = json.load(f)
            for obj in data.get("objects", []):
                manifest_lookup[obj["label"]] = obj
        except Exception as exc:
            print(f"::warning::Could not read manifest: {exc}", file=sys.stderr)

    # Split to protect header/TOC from modification
    header_end = 0
    for marker in ("</header>", 'id="gh-bar"'):
        idx = body_html.find(marker)
        if idx != -1:
            close = body_html.find("</div>", idx) if marker == 'id="gh-bar"' else idx
            if close != -1:
                header_end = max(header_end, close + 6)
    prefix = body_html[:header_end]
    content = body_html[header_end:]

    for d in defs:
        label = d["label"]
        status = _proof_status_for_def(d, manifest_lookup)
        lean_decl = d.get("lean_decl", "")
        # Also check manifest for lean info
        if not lean_decl and label in manifest_lookup:
            lean_info = manifest_lookup[label].get("lean", {})
            lean_decl = lean_info.get("decl", "")
        lean_file = ""
        if label in manifest_lookup:
            lean_file = manifest_lookup[label].get("lean", {}).get("file", "")

        badge = _make_status_badge(status, lean_decl, lean_file)

        # Find the anchor for this label and insert badge after the heading text
        anchor_id = label.replace(":", "-")
        for aid in (anchor_id, label):
            # Look for end of the heading tag that contains this anchor
            pattern = re.compile(
                r'(<[^>]+\bid="' + re.escape(aid) + r'"[^>]*>)'
                r'(.*?)(</(?:h[1-6]|strong|span|div)>)',
                re.DOTALL,
            )
            m = pattern.search(content)
            if m:
                insert_pos = m.end(2)
                content = content[:insert_pos] + " " + badge + content[insert_pos:]
                break
        else:
            # Fallback: try to insert after any element with this id
            pattern2 = re.compile(r'(<[^>]+\bid="' + re.escape(anchor_id) + r'"[^>]*>)')
            m2 = pattern2.search(content)
            if m2:
                content = content[:m2.end()] + badge + content[m2.end():]

    return prefix + content


# ---------------------------------------------------------------------------
# 3.  Definition-term linking
# ---------------------------------------------------------------------------

def _build_term_map(defs: list[dict]) -> list[tuple[re.Pattern, str, str]]:
    """Build (compiled regex, anchor, title) for each definition with a name.

    Returns longest-first so overlapping names are handled correctly.
    """
    entries: list[tuple[str, str, str]] = []
    for d in defs:
        name = d["plain_title"]
        if not name or len(name) < 3:
            continue
        entries.append((name, d["label"], d["title"]))
    # sort longest first to avoid partial matches
    entries.sort(key=lambda x: -len(x[0]))
    result: list[tuple[re.Pattern, str, str]] = []
    for name, label, title in entries:
        # Match the name as a whole word, case-insensitive
        pattern = re.compile(r"(?<![#\w/])(" + re.escape(name) + r")(?!\w)", re.IGNORECASE)
        result.append((pattern, label, title))
    return result


def _link_terms_in_html(body_html: str, term_map: list[tuple[re.Pattern, str, str]]) -> str:
    """Replace first occurrence of each defined term in every <p> with a link."""
    if not term_map:
        return body_html

    def _process_paragraph(p_html: str) -> str:
        # Don't touch headings, already-linked text, or TOC/header
        if any(tag in p_html for tag in ("<h1", "<h2", "<h3", "<h4", "<header", "toc-dropdown")):
            return p_html
        for pattern, label, _title in term_map:
            # Only link first occurrence per paragraph, and skip if already inside an <a> tag
            def _replace_first(m: re.Match) -> str:
                start = m.start()
                before = p_html[:start]
                # Skip if inside an HTML tag (between < and >)
                open_angle = before.rfind("<")
                close_angle = before.rfind(">")
                if open_angle > close_angle:
                    return m.group(0)
                # Skip if inside an <a> tag
                open_a = len(re.findall(r'<a[\s>]', before))
                close_a = before.count("</a>")
                if open_a > close_a:
                    return m.group(0)
                return f'<a class="defn-link" href="#{label}">{m.group(0)}</a>'
            p_html = pattern.sub(_replace_first, p_html, count=1)
        return p_html

    # Split on paragraph boundaries and process each
    parts = re.split(r"(<p[^>]*>.*?</p>)", body_html, flags=re.DOTALL)
    return "".join(_process_paragraph(p) if p.startswith("<p") else p for p in parts)


# ---------------------------------------------------------------------------
# 4.  Feature-branch helpers
# ---------------------------------------------------------------------------

def _fetch_open_prs(repo: str, branch: str) -> list[dict]:
    """Query the GitHub API for open PRs whose head matches *branch*."""
    prs: list[dict] = []
    try:
        url = (f"https://api.github.com/repos/{repo}/pulls"
               f"?head={repo.split('/')[0]}:{branch}&state=open&per_page=10")
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        for pr in data:
            prs.append({"number": pr["number"], "title": pr["title"], "url": pr["html_url"]})
    except Exception as exc:
        print(f"::warning::Could not fetch PRs: {exc}", file=sys.stderr)
    return prs


def _make_branch_bar(branch: str, repo: str, sha: str, prs: list[dict], diff_pdf: str | None = None) -> str:
    """Build a small info bar with GitHub links (feature branches only)."""
    repo_url = f"https://github.com/{repo}"
    lines = ['<div id="gh-bar" style="text-align:center; padding:4px 0; font-size:0.82rem;">']
    lines.append(f'  <a class="gh-badge" href="{repo_url}/tree/{branch}">&#x1F33F; {html_mod.escape(branch)}</a>')
    if sha:
        lines.append(f'  <a class="gh-badge" href="{repo_url}/commit/{sha}">&#x1F4DD; {sha[:7]}</a>')
    for pr in prs:
        lines.append(f'  <a class="gh-badge" href="{pr["url"]}">PR #{pr["number"]}</a>')
    if diff_pdf:
        lines.append(f'  <a class="gh-badge" href="{html_mod.escape(diff_pdf)}" title="Changes vs main branch">&#x1F4C4; Diff PDF</a>')
    lines.append("</div>")
    return "\n".join(lines)


def _add_source_links(
    body_html: str,
    defs: list[dict],
    tex: str,
    repo: str,
    branch: str,
    src_dir: str = ".",
) -> str:
    """Insert a small link-to-source icon next to each definition / theorem heading."""
    repo_url = f"https://github.com/{repo}"

    # Only modify body content, not the header/TOC
    header_end = 0
    for marker in ("</header>", 'id="gh-bar"'):
        idx = body_html.find(marker)
        if idx != -1:
            close = body_html.find("</div>", idx) if marker == 'id="gh-bar"' else idx
            if close != -1:
                header_end = max(header_end, close + 6)
    prefix = body_html[:header_end]
    content = body_html[header_end:]

    for d in defs:
        label = d["label"]
        # Try original chapter files first, fall back to flattened tex
        loc = _find_label_in_sources(label, src_dir)
        if loc:
            file_path, line_no = loc
        else:
            line_no = _find_env_line(tex, label)
            if line_no is None:
                continue
            file_path = ""

        link_html = (
            f'<a class="src-link" href="{repo_url}/blob/{branch}/'
            f'{file_path}#L{line_no}" target="_blank" title="View source">'
            f"&#x1F4C4;</a>"
        )
        anchor_id = label.replace(":", "-")
        for aid in (anchor_id, label):
            pattern = re.compile(r'(<[^>]+\bid="' + re.escape(aid) + r'"[^>]*>)')
            m = pattern.search(content)
            if m:
                insert_pos = m.end()
                content = content[:insert_pos] + link_html + content[insert_pos:]
                break
    return prefix + content


# ---------------------------------------------------------------------------
# 5.  Pandoc anchor normalisation
# ---------------------------------------------------------------------------

def _ensure_anchors(body_html: str, defs: list[dict], headings: list[dict]) -> str:
    """Ensure that every labelled item has an ``id`` anchor in the HTML.

    Pandoc may strip or rename some LaTeX labels.  We add ``<span id="...">``
    markers so that our TOC and term links always resolve.

    Anchors are only inserted in the main body content — never inside the
    sticky header or the TOC dropdown.
    """
    existing_ids = set(re.findall(r'id="([^"]+)"', body_html))
    inserts: list[tuple[str, str]] = []

    for d in defs:
        label = d["label"]
        for candidate in (label, label.replace(":", "-")):
            if candidate in existing_ids:
                break
        else:
            plain = d["plain_title"]
            if plain:
                inserts.append((plain, label))

    for h in headings:
        label = h["label"]
        if not label:
            continue
        for candidate in (label, label.replace(":", "-")):
            if candidate in existing_ids:
                break
        else:
            inserts.append((h["title"], label))

    if not inserts:
        return body_html

    # Split the HTML to only modify the main body content, not the header/TOC
    # Find the end of the site-header + gh-bar region
    header_end = 0
    for marker in ("</header>", 'id="gh-bar"'):
        idx = body_html.find(marker)
        if idx != -1:
            # Move past the closing tag of the element
            close = body_html.find("</div>", idx) if marker == 'id="gh-bar"' else idx
            if close != -1:
                header_end = max(header_end, close + 6)

    prefix = body_html[:header_end]
    content = body_html[header_end:]

    for text, label in inserts:
        escaped = re.escape(html_mod.escape(text))
        pattern = re.compile(r"(?=(" + escaped + r"))", re.IGNORECASE)
        anchor = f'<span id="{label}"></span>'
        content = pattern.sub(anchor, content, count=1)

    return prefix + content


# ---------------------------------------------------------------------------
# 6.  Main assembly
# ---------------------------------------------------------------------------

def enhance_html(
    raw_html: str,
    tex: str,
    branch: str | None = None,
    repo: str | None = None,
    sha: str | None = None,
    src_dir: str = ".",
    diff_pdf: str | None = None,
    manifest_path: str | None = None,
) -> str:
    """Return the enhanced HTML string."""
    defs = parse_definitions(tex)
    headings = parse_headings(tex)

    # Build pieces
    header_html = _make_header_html(headings, branch=branch, repo=repo)
    term_map = _build_term_map(defs)

    # ── Inject CSS ──────────────────────────────────────────────────────────
    style_block = f"<style>{_DARK_LIGHT_CSS}</style>"
    if "</head>" in raw_html:
        # Remove any existing <link rel="stylesheet" href="style.css"> since we inline it
        raw_html = re.sub(r'<link[^>]+href="style\.css"[^>]*>', "", raw_html)
        raw_html = raw_html.replace("</head>", style_block + "\n</head>")
    else:
        raw_html = style_block + "\n" + raw_html

    # ── Inject header after <body> ──────────────────────────────────────────
    body_tag_match = re.search(r"<body[^>]*>", raw_html)
    if body_tag_match:
        insert_pos = body_tag_match.end()
        extra = "\n" + header_html + "\n"
        # Feature-branch bar
        if branch and repo:
            prs = _fetch_open_prs(repo, branch) if repo else []
            extra += _make_branch_bar(branch, repo, sha or "", prs, diff_pdf=diff_pdf) + "\n"
        # Proof-status legend
        extra += _make_proof_legend() + "\n"
        raw_html = raw_html[:insert_pos] + extra + raw_html[insert_pos:]

    # ── Ensure anchors exist for all labelled items ─────────────────────────
    raw_html = _ensure_anchors(raw_html, defs, headings)

    # ── Inject proof-status badges ──────────────────────────────────────────
    raw_html = _inject_proof_badges(raw_html, defs, manifest_path=manifest_path)

    # ── Link defined terms ──────────────────────────────────────────────────
    raw_html = _link_terms_in_html(raw_html, term_map)

    # ── Source links (feature branch) ───────────────────────────────────────
    if branch and repo:
        raw_html = _add_source_links(raw_html, defs, tex, repo, branch, src_dir)

    # ── Inject JS before </body> ────────────────────────────────────────────
    if "</body>" in raw_html:
        raw_html = raw_html.replace("</body>", _TOGGLE_JS + "\n</body>")
    else:
        raw_html += _TOGGLE_JS

    return raw_html


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Enhance Pandoc HTML for QOU")
    ap.add_argument("input_html", help="Path to Pandoc-generated HTML")
    ap.add_argument("flat_tex", help="Path to flattened LaTeX source (main-flat.tex)")
    ap.add_argument("output_html", help="Output HTML path")
    ap.add_argument("--branch", default=None, help="Git branch name (omit for main)")
    ap.add_argument("--repo", default=None, help="GitHub owner/repo")
    ap.add_argument("--sha", default=None, help="Git commit SHA")
    ap.add_argument("--src-dir", default=".", help="Root directory of the LaTeX source tree")
    ap.add_argument("--diff-pdf", default=None, help="Filename of the diff PDF (feature branches only)")
    ap.add_argument("--manifest", default=None, help="Path to proof-objects.json for status badges")
    args = ap.parse_args()

    raw_html = Path(args.input_html).read_text(encoding="utf-8")
    tex = Path(args.flat_tex).read_text(encoding="utf-8")
    result = enhance_html(
        raw_html, tex,
        branch=args.branch, repo=args.repo, sha=args.sha,
        src_dir=args.src_dir, diff_pdf=args.diff_pdf,
        manifest_path=args.manifest,
    )
    Path(args.output_html).write_text(result, encoding="utf-8")
    print(f"✓ Enhanced HTML written to {args.output_html}")


if __name__ == "__main__":
    main()
