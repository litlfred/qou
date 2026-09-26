#!/usr/bin/env python3
"""Inject Jekyll front matter into a STAGING COPY of `docs/`, never in place.

WHY A STAGING COPY AND NOT THE REPO
-----------------------------------
Jekyll converts a `.md` file to a page only when it carries YAML front matter.
Without it the file is a STATIC ASSET and is copied verbatim — so a
just-the-docs site over a front-matter-less tree publishes raw markdown, not
rendered pages. Measured on this repo: **0 of 400** sampled `docs/**/*.md` carry
front matter, against **277 of 300** in the platform's own `cat-harness/docs/`.
So the gap is 3,070 files, and `defaults:` in `_config.yml` does NOT close it —
`defaults` supply values to pages, and a file with no front matter is not a page.

The repo's `.md` files are therefore left alone. `docs/audits/` alone is 2,832
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
  nav_exclude: true      — for `audits/`, and see below

NAV_EXCLUDE ON audits/ IS DELIBERATE, NOT A SHORTCUT
----------------------------------------------------
2,832 of the 3,070 files are audits. A just-the-docs sidebar with 2,832 leaves
is not navigation, it is a wall — the nav is the feature the theme is chosen
for, and filling it with every dated audit destroys it. The audits stay fully
RENDERED, SEARCHABLE (`search_enabled: true` indexes excluded pages) and
linkable; they are reached through the generated index rather than the sidebar.

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


def yaml_quote(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def front_matter(rel: str, text: str) -> str:
    parts = rel.split(os.sep)
    lines = ["---", "layout: default", f"title: {yaml_quote(title_for(rel, text))}"]
    if len(parts) >= 2:
        lines.append(f"parent: {yaml_quote(parts[-2].replace('-', ' '))}")
    if len(parts) >= 3:
        lines.append(f"grand_parent: {yaml_quote(parts[-3].replace('-', ' '))}")
    if parts[0] == "audits":
        lines.append("nav_exclude: true")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def walk_md():
    for root, dirs, files in os.walk(DOCS):
        dirs[:] = [d for d in dirs if d != "_archive"]
        for f in files:
            if f.endswith(".md") and f not in SKIP_NAMES:
                p = os.path.join(root, f)
                yield p, os.path.relpath(p, DOCS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", help="directory to copy docs/ into and inject")
    ap.add_argument("--check", action="store_true", help="report only")
    a = ap.parse_args()

    total = missing = 0
    for p, rel in walk_md():
        total += 1
        if not has_front_matter(p):
            missing += 1

    if a.check or not a.stage:
        print(f"docs/**/*.md            : {total}")
        print(f"  WITH front matter     : {total - missing}")
        print(f"  WITHOUT (need inject) : {missing}")
        print("\nA file without front matter is a STATIC ASSET to Jekyll — it is")
        print("copied verbatim, not rendered. `defaults:` does not change that.")
        return 0

    stage = os.path.abspath(a.stage)
    if os.path.exists(stage):
        shutil.rmtree(stage)
    shutil.copytree(DOCS, stage, ignore=shutil.ignore_patterns("_archive"))

    injected = kept = 0
    for root, _, files in os.walk(stage):
        for f in files:
            if not f.endswith(".md") or f in SKIP_NAMES:
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, stage)
            if has_front_matter(p):
                kept += 1
                continue
            try:
                text = open(p, encoding="utf-8").read()
            except Exception as e:
                print(f"  SKIP (unreadable) {rel}: {e}", file=sys.stderr)
                continue
            open(p, "w", encoding="utf-8").write(front_matter(rel, text) + text)
            injected += 1

    print(f"staged: {stage}")
    print(f"  injected : {injected}")
    print(f"  kept     : {kept}  (already had front matter)")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
