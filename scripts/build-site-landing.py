#!/usr/bin/env python3
"""build-site-landing — the site's root page: a short list of links.

Owner, 2026-11-23: "The landing page points to the web view, PDF, Lean
rendering, QA report and so on", and 2026-11-24: "not the whole thing, but the
links to". So the page is the paper's title, one line saying what it is, and a
link to each rendering of the work. Nothing is embedded.

Every link is DERIVED, so nothing here names an owner, a repository or a page:

- the paper: the first `dir:` in folio/folio.ts, the same rule
  scripts/lib/paper-env.sh uses for DEFAULT_PAPER. Its web view is the
  `<site>/<route>/<paper>/` that build-folio-site.ts wrote (the `title` of its
  outline.json is the page heading);
- its PDF: `papers/<paper>/<paper>.pdf`, the path scripts/publish-paper-pdf.sh
  writes on the publish branch (not part of `<site>`, so it is linked whether
  or not this build holds it);
- the folio's other documents: one link to build-folio-site.ts's index of
  them, `<site>/<route>/`, when it holds more than the paper;
- every `coverage.visualiser` the instance declaration (`<name>.json`) gives a
  directory, whose `ref` is under `_site/`: Lean, the work plan, the accuracy
  scorecard, QA, in declaration order. A declared page this build did not
  produce is listed as "not in this build" rather than linked or left out;
- the source repository, from the declaration's `repository`, and beside it
  the repository's CONTRIBUTING.md and LICENSE* files, when it has them (bean
  qou-zo8u lists both among the landing's links), each with the first line of
  the file as its note.

It also writes `<site>/papers/<paper>/index.html` for every paper the folio
site built: a redirect to that paper's interactive view (owner, 2026-11-24:
"I expected .../papers/quantum-observable-universe/ to be the interactive
paper through the harness, not the PDF view"), keeping any `#fragment`. The
PDF and the other files scripts/publish-paper-pdf.sh writes beside it on the
publish branch are not touched, so `papers/<paper>/<paper>.pdf` stays where
it is.

`--keep-old-root <publish checkout>`: a root `index.html` on the publish branch
that this script did not write (no generator meta) is copied beside it as
`index-<YYYY-MM>.html` (the date of its last commit there) before the
publish overwrites it. The copy is written into the publish checkout, not into
`<site>`, so the main-site manifest never lists it and a later publish never
deletes it.

Usage:
    python3 scripts/build-site-landing.py --site _site
    python3 scripts/build-site-landing.py --site _site --keep-old-root .gh-pages-worktree
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

GENERATOR = "scripts/build-site-landing.py"
MARKER = f'<meta name="generator" content="{GENERATOR}">'


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def papers(site: Path) -> list[tuple[str, str, str]]:
    """(slug, title, site-relative href) for each paper the folio site built."""
    out = []
    for outline in sorted(site.glob("**/outline.json")):
        rel = outline.parent.relative_to(site)
        # A paper's outline sits at <route>/<paper>/outline.json; deeper
        # outline/<chapter>.json files are named differently and not matched.
        if not (outline.parent / "index.html").is_file():
            continue
        try:
            title = json.loads(outline.read_text(encoding="utf-8")).get("title") or rel.name
        except (OSError, ValueError):
            title = rel.name
        out.append((rel.name, str(title), rel.as_posix() + "/"))
    return out


def visualisers(decl: dict, site: Path) -> list[tuple[str, str | None]]:
    """(title, href or None) for every declared visualiser under `_site/`."""
    out = []
    for d in decl.get("directories", []):
        for v in (d.get("coverage") or {}).get("visualiser") or []:
            ref = v.get("ref", "")
            if not ref.startswith("_site/"):
                continue
            rel = ref[len("_site/"):]
            title = v.get("title") or d.get("id", rel)
            if (site / rel).is_file():
                href = rel[: -len("index.html")] if rel.endswith("index.html") else rel
                out.append((title, href or "./"))
            else:
                out.append((title, None))
    return out


def default_branch(root: Path) -> str:
    """origin's HEAD, else "main" (scripts/lib/paper-env.sh's DEFAULT_BRANCH rule)."""
    r = subprocess.run(["git", "-C", str(root), "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"],
                       capture_output=True, text=True, check=False)
    return r.stdout.strip().removeprefix("origin/") or "main"


def lead_paper(root: Path) -> str | None:
    """The first `dir:` in folio/folio.ts (scripts/lib/paper-env.sh's DEFAULT_PAPER)."""
    try:
        m = re.search(r'dir:\s*"([^"]+)"', (root / "folio" / "folio.ts").read_text(encoding="utf-8"))
    except OSError:
        return None
    return m.group(1) if m else None


def page(decl: dict, site: Path, root: Path) -> str:
    ps = papers(site)
    lead = lead_paper(root)
    main_paper = next((p for p in ps if p[0] == lead), ps[0] if len(ps) == 1 else None)
    heading = main_paper[1] if main_paper else decl.get("description", decl.get("name", ""))
    sub = decl.get("description", "") if main_paper else ""
    items: list[str] = []
    if main_paper:
        slug, _, href = main_paper
        items.append(f'<li><a href="{esc(href)}">Paper</a> <span>the web view, chapter by chapter</span></li>')
        items.append(f'<li><a href="papers/{esc(slug)}/{esc(slug)}.pdf">PDF</a> <span>the whole paper as one file</span></li>')
    others = [p for p in ps if p is not main_paper]
    if others:
        route = Path(others[0][2]).parent.as_posix() + "/"
        label = "Other documents" if main_paper else "Documents"
        items.append(f'<li><a href="{esc(route)}">{label}</a> <span>{len(others)} more in this folio</span></li>')
    for title, href in visualisers(decl, site):
        if href is None:
            items.append(f"<li>{esc(title)} <span>not in this build</span></li>")
        else:
            items.append(f'<li><a href="{esc(href)}">{esc(title)}</a></li>')
    repo = decl.get("repository")
    if repo:
        web = f"https://github.com/{repo}"
        items.append(f'<li><a href="{esc(web)}">Source</a> <span>{esc(repo)}</span></li>')
        files = [("How to contribute", root / "CONTRIBUTING.md")] + [("License", p) for p in sorted(root.glob("LICENSE*")) if p.is_file()]
        for label, f in files:
            if not f.is_file():
                continue
            first = next((ln.strip(" #") for ln in f.read_text(encoding="utf-8", errors="replace").splitlines() if ln.strip()), "")
            note = f" <span>{esc(first)}</span>" if label == "License" and first else ""
            items.append(f'<li><a href="{esc(web)}/blob/{esc(default_branch(root))}/{esc(f.name)}">{label}</a>{note}</li>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{MARKER}
<title>{esc(heading)}</title>
<style>
body {{ margin: 0; padding: 2rem 1.5rem 3rem; font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; background: Canvas; color: CanvasText; }}
main {{ max-width: 40rem; }}
h1 {{ font-size: 1.6rem; margin: 0 0 .4rem; }}
p {{ margin: 0 0 1.4rem; opacity: .8; }}
ul {{ list-style: none; padding: 0; margin: 0; }}
li {{ padding: .55rem 0; border-top: 1px solid rgba(127,127,127,.3); font-size: 1.05rem; }}
li span {{ font-size: .85rem; opacity: .7; margin-left: .5rem; }}
</style>
</head>
<body>
<main>
<h1>{esc(heading)}</h1>
{f"<p>{esc(sub)}</p>" if sub else ""}
<ul>
{chr(10).join(items)}
</ul>
</main>
</body>
</html>
"""


def paper_redirects(site: Path) -> int:
    """`papers/<slug>/index.html` -> the paper's interactive view, for every paper."""
    n = 0
    for slug, title, href in papers(site):
        out = site / "papers" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        target = "../../" + href
        out.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{MARKER}
<title>{esc(title)}</title>
<link rel="canonical" href="{esc(target)}">
<meta http-equiv="refresh" content="0; url={esc(target)}">
<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>
</head>
<body><p>{esc(title)} is at <a href="{esc(target)}">its interactive view</a>.</p></body>
</html>
""", encoding="utf-8")
        n += 1
    return n


def find_declaration(root: Path) -> Path | None:
    """The `<name>.json` at the repository root whose `name` is its own stem and which declares `directories`."""
    for p in sorted(root.glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and d.get("name") == p.stem and isinstance(d.get("directories"), list):
            return p
    return None


def keep_old_root(pages: Path) -> None:
    old = pages / "index.html"
    if not old.is_file() or MARKER in old.read_text(encoding="utf-8", errors="replace"):
        return
    r = subprocess.run(["git", "-C", str(pages), "log", "-1", "--format=%cI", "--", "index.html"],
                       capture_output=True, text=True, check=False)
    stamp = r.stdout.strip()
    when = datetime.fromisoformat(stamp) if stamp else datetime.fromtimestamp(old.stat().st_mtime)
    keep = pages / f"index-{when.strftime('%Y-%m')}.html"
    if keep.exists():
        print(f"build-site-landing: {keep.name} already kept; the old root page is overwritten by this publish")
        return
    shutil.copyfile(old, keep)
    print(f"build-site-landing: kept the previous root page as {keep.name}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--site", required=True, type=Path)
    ap.add_argument("--declaration", type=Path, help="the instance declaration; default: the <name>.json at the repository root")
    ap.add_argument("--keep-old-root", type=Path, metavar="PAGES")
    a = ap.parse_args()
    root = Path(__file__).resolve().parent.parent
    decl_path = a.declaration
    if decl_path is None:
        decl_path = find_declaration(root)
        if decl_path is None:
            print("build-site-landing: no instance declaration found; pass --declaration", file=sys.stderr)
            return 2
    decl = json.loads(decl_path.read_text(encoding="utf-8"))
    if a.keep_old_root:
        keep_old_root(a.keep_old_root)
        return 0
    if not a.site.is_dir():
        print(f"build-site-landing: {a.site} does not exist", file=sys.stderr)
        return 2
    print(f"build-site-landing: {paper_redirects(a.site)} papers/<paper>/ redirect(s) to the interactive view")
    body = page(decl, a.site, root)
    (a.site / "index.html").write_text(body, encoding="utf-8")
    print(f"build-site-landing: {a.site}/index.html ({body.count('<li>')} entries, from {decl_path.name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
