#!/usr/bin/env python3
"""site-extras — qou's own pieces of the platform-built site.

qou's site is built by cat-harness-tools' build-instance-site.ts from the
recipe in index.config.json (owner ruling 2026-11-24, "1 qou is platform
later"; the dth-hrh layout). The platform writes the "Documents" landing and
one interactive page per paper (folio-assistant-core build-document-site.ts).
This script writes the few things that are qou's own, each called from
scripts/site-step.sh:

  --landing-source SRC   add CONTRIBUTING, LICENSE and the source repository to
                         the landing's "Also on this site" list in SRC/index.md
                         (the platform lists the declared visualisers there:
                         Accuracy, QA, Work plan, Lean). Idempotent.
  --redirects SITE       SITE/papers/<slug>/index.html -> en/<slug>/ for every
                         paper the site built, keeping ?query#fragment (owner,
                         2026-11-24: ".../papers/quantum-observable-universe/
                         [should be] the interactive paper through the harness,
                         not the PDF view"). Files already on the publish branch
                         under papers/ (the PDFs publish-paper-pdf.sh writes)
                         are not part of this build and are not touched.
  --export-index DIR --paper SLUG
                         DIR/index.html: the paper's exports, every file in DIR
                         with its size, as the platform's export page lists them.
  --contributing MD --out HTML
                         CONTRIBUTING.md as a page (pandoc when present, else
                         preformatted), for the rail pass to frame.
  --relink SITE          the papers' own links that the page cannot serve, made
                         to resolve: a link to a block's .md becomes that block's
                         anchor on the page (its label); an image beside a block is
                         copied next to the page; a simulator page is copied to
                         /simulators/; any other repository file (a witness .json,
                         a .lean, a .py) links to it on GitHub at this commit.
                         What none of these covers is left for the link check.
  --keep-old-root PAGES  a root index.html on the publish checkout that the
                         platform did not write is kept as index-<YYYY-MM>.html
                         before the publish replaces it.

Every link is derived from the checkout; nothing names a page by hand except
the three repository files above.
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

ROOT = Path(__file__).resolve().parent.parent
MARK = "<!-- qou site-extras -->"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def declaration() -> dict:
    return json.loads((ROOT / "qou.json").read_text(encoding="utf-8"))


def landing_source(src: Path) -> int:
    idx = src / "index.md"
    if not idx.is_file():
        print(f"site-extras: {idx} not found (site:document writes it)", file=sys.stderr)
        return 2
    text = idx.read_text(encoding="utf-8")
    if MARK in text:
        return 0
    repo = declaration().get("repository", "")
    items = [
        '<li><a href="contributing/">Contributing</a></li>',
        '<li><a href="LICENSE.txt">License (CC BY 4.0)</a></li>',
    ]
    if repo:
        items.append(f'<li><a href="https://github.com/{esc(repo)}">Source repository</a></li>')
    block = MARK + "\n" + "\n".join(items) + "\n"
    if "<h2>Also on this site</h2>" in text:
        text = re.sub(r"(<h2>Also on this site</h2>\s*<ul>\n)", lambda m: m.group(1) + block, text, count=1)
    else:
        text = text.replace("{% endraw %}", f"<h2>Also on this site</h2>\n<ul>\n{block}</ul>\n{{% endraw %}}", 1)
    idx.write_text(text, encoding="utf-8")
    print(f"site-extras: {len(items)} link(s) added to the landing")
    return 0


def built_papers(site: Path) -> list[tuple[str, str]]:
    out = []
    for d in sorted((ROOT / "folio").iterdir()):
        s = d.name
        if (d / f"{s}.ts").is_file() and (site / "en" / s / "index.html").is_file():
            page = (site / "en" / s / "index.html").read_text(encoding="utf-8", errors="replace")
            m = re.search(r"<title>(.*?)</title>", page, re.S)
            out.append((s, html.unescape(m.group(1).split("|")[0].strip()) if m else s))
    return out


def redirects(site: Path) -> int:
    n = 0
    for slug, title in built_papers(site):
        out = site / "papers" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        target = f"../../en/{slug}/"
        out.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<link rel="canonical" href="{esc(target)}">
<meta http-equiv="refresh" content="0; url={esc(target)}">
<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>
</head>
<body><p>{esc(title)} is at <a href="{esc(target)}">its page</a>.</p></body>
</html>
""", encoding="utf-8")
        n += 1
    print(f"site-extras: {n} papers/<slug>/ redirect(s) to en/<slug>/")
    return 0


ATTR = re.compile(r'(\s(?:href|src)=")([^"#?]*)([^"]*)(")')


def block_labels(slug: str) -> dict[str, list[str]]:
    """block file stem -> its label(s), from folio/<slug>/**/<stem>.ts."""
    out: dict[str, list[str]] = {}
    for ts in (ROOT / "folio" / slug).rglob("*.ts"):
        m = re.search(r'\blabel:\s*["\']([^"\']+)["\']', ts.read_text(encoding="utf-8", errors="replace"))
        if m:
            out.setdefault(ts.stem, []).append(m.group(1))
    return out


def commit_sha() -> str:
    import os
    sha = os.environ.get("SITE_COMMIT")
    if sha:
        return sha
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() or "main"


def relink(site: Path) -> int:
    import os
    repo = declaration().get("repository", "")
    sha = commit_sha()
    blob = f"https://github.com/{repo}/blob/{sha}/"
    counts = {"anchor": 0, "copied": 0, "github": 0, "left": 0}
    for slug, _title in built_papers(site):
        labels = block_labels(slug)
        chapters = [d for d in (ROOT / "folio" / slug).iterdir() if d.is_dir()]
        page_dir = site / "en" / slug
        for page in sorted(page_dir.glob("index*.html")):
            text = page.read_text(encoding="utf-8")

            def fix(m: re.Match) -> str:
                pre, path, rest, post = m.groups()
                if not path or re.match(r"^[a-z][a-z0-9+.-]*:", path) or path.startswith("//"):
                    return m.group(0)
                if path.startswith("/"):
                    name = path.lstrip("/")
                    src = ROOT / "simulators" / name
                    if src.is_file():
                        dst = site / "simulators" / name
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(src, dst)
                        counts["copied"] += 1
                        return f"{pre}../../simulators/{name}{rest}{post}"
                    counts["left"] += 1
                    return m.group(0)
                if (page_dir / path).exists():
                    return m.group(0)
                if path.endswith(".md"):
                    lab = labels.get(Path(path).stem, [])
                    if len(lab) == 1:
                        counts["anchor"] += 1
                        return f"{pre}#{lab[0]}{post}"
                for base in [*chapters, ROOT / "folio" / slug]:
                    repo_path = Path(os.path.normpath(base / path))
                    if not repo_path.is_file():
                        continue
                    try:
                        rel = repo_path.relative_to(ROOT).as_posix()
                    except ValueError:
                        continue
                    if repo_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"} and ".." not in path:
                        dst = page_dir / path
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(repo_path, dst)
                        counts["copied"] += 1
                        return m.group(0)
                    counts["github"] += 1
                    return f"{pre}{blob}{rel}{rest}{post}"
                counts["left"] += 1
                return m.group(0)

            new = ATTR.sub(fix, text)
            if new != text:
                page.write_text(new, encoding="utf-8")
    print(f"site-extras: relinked papers' own links: {counts}")
    return 0


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return str(n)


def export_index(d: Path, slug: str) -> int:
    files = sorted(p for p in d.iterdir() if p.is_file() and p.name != "index.html")
    rows = "\n".join(f'<li><a href="{esc(p.name)}">{esc(p.name)}</a> — {human(p.stat().st_size)}</li>' for p in files)
    (d / "index.html").write_text(f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Exports | {esc(slug)}</title></head>
<body><main>
<h1>Exports</h1>
<p>The PDF is typeset with LaTeX (scripts/build-paper-pdf.sh); the Word file is the platform's export
(document-export.ts). Both are built from the same commit as this site.</p>
<ul>
{rows}
</ul>
<p><a href="../">Back to the paper</a></p>
</main></body>
</html>
""", encoding="utf-8")
    return 0


def contributing(md: Path, out: Path) -> int:
    out.parent.mkdir(parents=True, exist_ok=True)
    body = None
    if shutil.which("pandoc"):
        r = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", str(md)], capture_output=True, text=True)
        if r.returncode == 0:
            body = r.stdout
    if body is None:
        body = f"<pre>{esc(md.read_text(encoding='utf-8'))}</pre>"
    repo = declaration().get("repository", "")
    blob = f"https://github.com/{repo}/blob/main/"

    def gh(m: re.Match) -> str:
        pre, path, rest, post = m.groups()
        if not path or re.match(r"^[a-z][a-z0-9+.-]*:", path) or path.startswith(("/", "//")):
            return m.group(0)
        return f"{pre}{blob}{path}{rest}{post}"

    body = ATTR.sub(gh, body)
    out.write_text(f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Contributing | qou</title></head>
<body><main>
{body}
</main></body>
</html>
""", encoding="utf-8")
    return 0


def keep_old_root(pages: Path) -> int:
    old = pages / "index.html"
    if not old.is_file():
        return 0
    text = old.read_text(encoding="utf-8", errors="replace")
    if "<title>Documents |" in text:
        return 0
    r = subprocess.run(["git", "-C", str(pages), "log", "-1", "--format=%cI", "--", "index.html"],
                       capture_output=True, text=True, check=False)
    stamp = r.stdout.strip()
    when = datetime.fromisoformat(stamp) if stamp else datetime.fromtimestamp(old.stat().st_mtime)
    keep = pages / f"index-{when.strftime('%Y-%m')}.html"
    if not keep.exists():
        shutil.copyfile(old, keep)
        print(f"site-extras: kept the previous root page as {keep.name}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--landing-source", type=Path)
    ap.add_argument("--redirects", type=Path)
    ap.add_argument("--export-index", type=Path)
    ap.add_argument("--paper")
    ap.add_argument("--contributing", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--keep-old-root", type=Path)
    ap.add_argument("--relink", type=Path)
    a = ap.parse_args()
    if a.landing_source:
        return landing_source(a.landing_source)
    if a.redirects:
        return redirects(a.redirects)
    if a.export_index:
        return export_index(a.export_index, a.paper or a.export_index.parent.name)
    if a.contributing:
        return contributing(a.contributing, a.out)
    if a.keep_old_root:
        return keep_old_root(a.keep_old_root)
    if a.relink:
        return relink(a.relink)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
