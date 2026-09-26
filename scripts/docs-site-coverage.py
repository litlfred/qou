#!/usr/bin/env python3
"""Per-source coverage check for the docs site: which staged `.md` produced no page?

WHY A PER-SOURCE CHECK AND NOT A PAGE COUNT
-------------------------------------------
The first version of this gate asserted `rendered_html > 2000`. Run 36266675464
passed it with **3017 pages from 3082 sources** — a 65-page gap the assertion
could not see, because a floor answers "did the build mostly work" and not "did
every document I staged come out the other side". A missing page is invisible to
navigation as well: 2,584 of the 3,082 are `nav_exclude`d audits reached only by
direct link, so a dropped one 404s with no sidebar entry to reveal it.

So this compares SOURCES to OUTPUTS by name, reports every unmapped source, and
fails on a coverage regression rather than on an absolute floor. Same discipline
AGENTS.md applies to the raw-float64 ratchet: the baseline drains, never grows.

THE MAPPING, AND THE TWO PLUGINS THAT BEND IT
---------------------------------------------
Jekyll writes `<dir>/<stem>.md` to `<dir>/<stem>.html`, with two github-pages
plugins altering it — both force-enabled, so both must be modelled here or the
checker invents failures:

  * `jekyll-readme-index` maps a directory's `README.md` to its `index.html`.
    So `README.md` and `index.md` in one directory CONTEND for a single output,
    and one of them legitimately produces no page of its own.
  * `jekyll-optional-front-matter` promotes front-matter-less `.md` to pages —
    which is why every staged `.md` is expected to map at all.

A source is counted COVERED if any of its admissible outputs exists.

Usage:
    docs-site-coverage.py --stage <dir> --site <dir> [--floor <int>]

`--floor` is the minimum number of covered sources required. Omit it to report
without failing (exit 0 unless the trees are missing).
"""
from __future__ import annotations
import argparse, os, sys


def md_sources(stage: str) -> list[str]:
    out = []
    for root, _, files in os.walk(stage):
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(root, f), stage))
    return sorted(out)


def candidate_outputs(rel: str) -> list[str]:
    d = os.path.dirname(rel)
    stem = os.path.basename(rel)[: -len(".md")]
    cands = [os.path.join(d, stem + ".html")]
    # jekyll-readme-index: README.md becomes the directory's index.
    if stem.upper() == "README":
        cands.append(os.path.join(d, "index.html"))
    # A permalink may render as <stem>/index.html rather than <stem>.html.
    cands.append(os.path.join(d, stem, "index.html"))
    return cands


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--site", required=True)
    ap.add_argument("--floor", type=int, default=None)
    ap.add_argument("--list", type=int, default=40, help="how many misses to print")
    a = ap.parse_args()

    for d in (a.stage, a.site):
        if not os.path.isdir(d):
            print(f"missing directory: {d}", file=sys.stderr)
            return 1

    srcs = md_sources(a.stage)
    missing = [s for s in srcs
               if not any(os.path.exists(os.path.join(a.site, c))
                          for c in candidate_outputs(s))]
    covered = len(srcs) - len(missing)
    html = sum(1 for r, _, fs in os.walk(a.site) for f in fs if f.endswith(".html"))

    print(f"staged .md sources : {len(srcs)}")
    print(f"covered by a page  : {covered}")
    print(f"NOT covered        : {len(missing)}")
    print(f"total .html in site: {html}  (includes theme pages, so >= covered)")

    if missing:
        # Group by directory: a systematic cause shows up as one directory, a
        # scatter of one-offs does not. That distinction is the whole diagnosis.
        bydir: dict[str, int] = {}
        for m in missing:
            bydir[os.path.dirname(m) or "."] = bydir.get(os.path.dirname(m) or ".", 0) + 1
        print("\nmisses by directory (a systematic cause is ONE directory):")
        for d, n in sorted(bydir.items(), key=lambda kv: -kv[1])[:20]:
            print(f"  {n:4d}  {d}/")
        print(f"\nfirst {min(a.list, len(missing))} unmapped sources:")
        for m in missing[: a.list]:
            print(f"  {m}")

    if a.floor is not None and covered < a.floor:
        print(f"\nCOVERAGE REGRESSION: {covered} covered < floor {a.floor}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
