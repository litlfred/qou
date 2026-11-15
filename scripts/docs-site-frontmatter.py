#!/usr/bin/env python3
"""Inject Jekyll front matter into a STAGING COPY of `docs/`, never in place.

WHY A STAGING COPY AND NOT THE REPO
-----------------------------------
This script injects into a COPY so that 3,082 dated records in `docs/` are never
rewritten to satisfy a renderer. See "WHAT IT BUYS" for why it is needed at all.

🛑 CORRECTED 2026-09-26 — the original rationale here was WRONG for this
pipeline, and the build log says so. It read: *"Jekyll converts a `.md` file to a
page only when it carries YAML front matter. Without it the file is a STATIC
ASSET and is copied verbatim ... `defaults:` does NOT close it."* That is true of
**vanilla** Jekyll and false of **github-pages**, which is what
`actions/jekyll-build-pages` runs: the gem force-enables
`jekyll-optional-front-matter`, which promotes every front-matter-less `.md` to a
page. Measured, not reasoned — run 36265760831 logs
`Generating: JekyllOptionalFrontMatter::Generator finished in 0.000179751 seconds`
alongside `jekyll-titles-from-headings` and `jekyll-default-layout`, all three of
which independently supply part of what this script writes.

So the front-matter-less tree WOULD have rendered. Do not cite the old reason.

WHAT IT BUYS (the surviving justification — nav metadata, not rendering)
-----------------------------------------------------------------------
Three things the forced plugins and `defaults:` cannot supply between them:

  * `parent:` / `grand_parent:` — just-the-docs nests the sidebar off these, and
    they are per-file (derived from the directory). `defaults:` could reach
    `parent` with one `scope:` block per directory — there are **19** — but
    `docs/` is **three** levels deep in 126 files, and a `defaults:` scope cannot
    express "the dir above my dir".
  * a date-stripped `title:` — `jekyll-titles-from-headings` takes the H1
    verbatim, so 2,584 audit titles would each open with their own date, which is
    noise in a nav label and already present in the body.
  * `nav_exclude:` per subtree — reachable via `defaults:`, and kept here so the
    three live in one place rather than split across two mechanisms.

A `defaults:`-based rewrite is therefore *partly* viable and is not obviously
worth it; recorded so the next reader does not have to re-derive the trade.

The repo's `.md` files are therefore left alone. `docs/audits/` alone is 2,584
dated records whose value IS being unedited records of their own analyses;
rewriting every one of them to satisfy a renderer would be the largest diff in
the repository and would touch nothing a reader cares about. AGENTS.md makes the
same call for the `4.66e6` drain ("dated audit docs ... deliberately left").

This mirrors the platform's own pattern, where `docs/reference/skills/*` are
GENERATED pages rather than hand-authored ones.

WHAT IT WRITES
--------------
For each `.md` under the staged tree, front matter with:
  layout: default        — the theme's page layout
  title:                 — the first `# ` heading, else a title-cased stem
  parent: / grand_parent: — from the directory, so the nav nests
  nav_exclude: true      — for `audits/` and `_archive/`, and see below

NAV_EXCLUDE ON audits/ IS DELIBERATE, NOT A SHORTCUT
----------------------------------------------------
2,584 of the 3,082 files are audits. A just-the-docs sidebar with 2,584 leaves
is not navigation, it is a wall — the nav is the feature the theme is chosen
for, and filling it with every dated audit destroys it. The audits stay fully
RENDERED, SEARCHABLE (`search_enabled: true` indexes excluded pages) and
linkable; they are reached through the generated index rather than the sidebar.

LIQUID: THE BODY IS WRAPPED IN {% raw %} WHEN — AND ONLY WHEN — IT NEEDS IT
--------------------------------------------------------------------------
Jekyll runs Liquid over every page body before markdown. This corpus contains
LaTeX, regexes, BibTeX and GitHub-Actions snippets that Liquid reads as template
syntax, and one of them took the build down:

    Liquid Exception: Liquid syntax error (line 211): Variable '{{1,4}' was not
    properly terminated with regexp: /\}\}/ in coordination/1ppq-qbeta.md

That `{{1,4}` is a **regex quantifier** inside a coordination-ledger table cell.
Measured before fixing: **6 of 3,082** files carry `{{` or `{%` — a GH-Actions
`${{ }}` in two code blocks, LaTeX `\{{}^3\mathrm{He}`, a product index
`∏_{{i,j}}`, that regex, and BibTeX `title = {{Convex Optimization}}`. **Zero are
intentional Liquid.** So the wrap is a scoped fix, not a corpus-wide one.

`render_with_liquid: false` is NOT available: it is a Jekyll **4** front-matter
key and the log records `GitHub Pages: jekyll v3.10.0` / `github-pages v232`.
`{% raw %}` is the only per-file opt-out on 3.10.

The wrap is DETECTED per file rather than listed, so a seventh such file is
handled with no edit here and no red build. It is applied to the BODY only (after
any existing front matter), and refused with a loud report if the body already
contains a raw/endraw tag, which would nest and mis-parse.

Usage:
    docs-site-frontmatter.py --stage <dir>     # copy docs/ -> dir, inject
    docs-site-frontmatter.py --check           # report the gap, write nothing
"""
from __future__ import annotations
import argparse, os, re, shutil, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(REPO, "docs")
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)
# Files that ALREADY carry front matter, or that Jekyll owns, are never rewritten.
SKIP_NAMES = {"_config.yml"}
# Liquid reads `{{` and `{%` as template syntax. Nothing in this corpus means it
# that way (see the module docstring) and one regex quantifier took the build
# down, so a body carrying either is wrapped in {% raw %}.
LIQUID = re.compile(r"\{\{|\{%")
# A body that already carries a raw/endraw tag cannot be wrapped again — the
# inner tag would close the outer one early. Refuse loudly instead.
RAWTAG = re.compile(r"\{%-?\s*(end)?raw\s*-?%\}")


def has_front_matter(path: str) -> bool:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.readline().rstrip("\n") == "---"
    except Exception:
        return False


def title_for(path: str, text: str) -> str:
    m = H1.search(text)
    if m:
        t = m.group(1).strip()
        # A leading date is noise in a nav label but useful in the body.
        t = re.sub(r"^\d{4}-\d{2}-\d{2}\s*[—–-]\s*", "", t)
        if t:
            return t[:120]
    stem = os.path.splitext(os.path.basename(path))[0]
    return stem.replace("-", " ").replace("_", " ").strip()[:120] or stem


def split_front_matter(text: str) -> tuple[str, str]:
    """(front_matter_including_delimiters, body). ('', text) when there is none."""
    if not text.startswith("---"):
        return "", text
    # The closing delimiter is the next line that is exactly `---`.
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return "\n".join(lines[:i + 1]) + "\n", "\n".join(lines[i + 1:])
    return "", text  # unterminated — treat the whole thing as body


def raw_wrap(body: str) -> tuple[str, bool]:
    """Wrap in {% raw %} iff the body needs it. Returns (body, wrapped?)."""
    if not LIQUID.search(body):
        return body, False
    return "{% raw %}\n" + body.rstrip("\n") + "\n{% endraw %}\n", True


def wrapped_changed(original: str, fm: str, body: str) -> bool:
    return fm + body != original


def yaml_quote(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def front_matter(rel: str, text: str) -> str:
    parts = rel.split(os.sep)
    lines = ["---", "layout: default", f"title: {yaml_quote(title_for(rel, text))}"]
    if len(parts) >= 2:
        lines.append(f"parent: {yaml_quote(parts[-2].replace('-', ' '))}")
    if len(parts) >= 3:
        lines.append(f"grand_parent: {yaml_quote(parts[-3].replace('-', ' '))}")
    # audits/ (2584 files) and _archive/ (43 historical) are rendered and
    # searchable but kept OUT of the sidebar — see the module docstring.
    if parts[0] in ("audits", "_archive"):
        lines.append("nav_exclude: true")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def walk_md():
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if f.endswith(".md") and f not in SKIP_NAMES:
                p = os.path.join(root, f)
                yield p, os.path.relpath(p, DOCS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", help="directory to copy docs/ into and inject")
    ap.add_argument("--check", action="store_true", help="report only")
    a = ap.parse_args()

    total = missing = liquid = 0
    for p, rel in walk_md():
        total += 1
        if not has_front_matter(p):
            missing += 1
        try:
            if LIQUID.search(open(p, encoding="utf-8").read()):
                liquid += 1
        except Exception:
            pass

    if a.check or not a.stage:
        print(f"docs/**/*.md            : {total}")
        print(f"  WITH front matter     : {total - missing}")
        print(f"  WITHOUT (need inject) : {missing}")
        print(f"  carrying {{{{ or {{%       : {liquid}  -> wrapped in {{% raw %}}")
        print("\nFront matter here buys NAV METADATA (parent/grand_parent, a")
        print("date-stripped title, nav_exclude) — not rendering: github-pages")
        print("force-enables jekyll-optional-front-matter. See the docstring.")
        return 0

    stage = os.path.abspath(a.stage)
    if os.path.exists(stage):
        shutil.rmtree(stage)
    shutil.copytree(DOCS, stage)

    injected = kept = wrapped = 0
    nested: list[str] = []
    for root, _, files in os.walk(stage):
        for f in files:
            if not f.endswith(".md") or f in SKIP_NAMES:
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, stage)
            try:
                text = open(p, encoding="utf-8").read()
            except Exception as e:
                print(f"  SKIP (unreadable) {rel}: {e}", file=sys.stderr)
                continue

            existing, body = split_front_matter(text)
            if existing:
                kept += 1
                fm = existing
            else:
                fm = front_matter(rel, text)
                injected += 1

            # A body already carrying a raw tag cannot be wrapped — say so and
            # leave it, rather than emitting markup whose tags do not pair.
            if LIQUID.search(body) and RAWTAG.search(body):
                nested.append(rel)
            else:
                body, did = raw_wrap(body)
                wrapped += did

            if existing and not wrapped_changed(text, fm, body):
                continue  # untouched: no front matter to add, no wrap needed
            open(p, "w", encoding="utf-8").write(fm + body)

    print(f"staged: {stage}")
    print(f"  injected      : {injected}")
    print(f"  kept          : {kept}  (already had front matter)")
    print(f"  liquid-wrapped: {wrapped}  ({{{{ or {{% in body -> {{% raw %}})")
    if nested:
        print(f"  NOT wrapped (already contains a raw tag): {len(nested)}")
        for n in nested:
            print(f"    {n}")
    # The invariant that matters: every .md in the stage is now a Jekyll PAGE.
    bad = [os.path.relpath(os.path.join(r, f), stage)
           for r, _, fs in os.walk(stage) for f in fs
           if f.endswith(".md") and f not in SKIP_NAMES
           and not has_front_matter(os.path.join(r, f))]
    print(f"  still without front matter: {len(bad)}")
    if bad:
        for b in bad[:5]:
            print(f"    {b}")
        return 1

    # Second invariant: every {% raw %} pairs with exactly one {% endraw %}.
    # An unpaired tag is a Liquid syntax error, i.e. the failure this wrap fixes.
    unpaired = []
    for r, _, fs in os.walk(stage):
        for f in fs:
            if not f.endswith(".md") or f in SKIP_NAMES:
                continue
            fp = os.path.join(r, f)
            try:
                t = open(fp, encoding="utf-8").read()
            except Exception:
                continue
            if t.count("{% raw %}") != t.count("{% endraw %}"):
                unpaired.append(os.path.relpath(fp, stage))
    print(f"  unpaired raw tags: {len(unpaired)}")
    if unpaired:
        for u in unpaired[:5]:
            print(f"    {u}")
        return 1
    if nested:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
