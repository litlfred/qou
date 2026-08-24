#!/usr/bin/env python3
"""
enrich-dangling-citations — propose `references.ts` entries for citation keys
that resolve to nothing, using metadata fetched from arXiv, Crossref and
Semantic Scholar.

`check-citation-keys.py` reports which keys resolve to nothing. Closing them
needs bibliographic metadata, and this repo's discipline is that metadata is
not written from memory — the library-intake entries all say "extracted from
the PDF, not verified against the publisher record" precisely because that
was the strongest claim available. With egress to the scholarly APIs, a
stronger claim is available: the publisher record itself.

## It proposes; it does not write

Output is a candidate file for an agent to read, in the same shape as
`docs/audits/library-duplicate-ledger.json`: the machine supplies evidence,
a reader decides. Nothing touches `references.ts`. That split matters more
here than usual, because the third tier below is a *search*, and a search
returns the most-cited paper matching some words, which is not the same as
the paper a proof meant to cite.

## Three tiers, and their confidence is not comparable

  1. **`identifier`** — the citing comment carries an arXiv id or a DOI.
     The lookup is exact: whatever that id resolves to IS the work. High
     confidence, and the only tier that should be applied with light review.

  2. **`title`** — the comment names a work ("Linear Representations of
     Finite Groups") but gives no id. A title search is usually right and
     occasionally lands on a different edition, a translation, or a review
     of the book. Check the year and author against the key.

  3. **`search`** — the comment carries nothing, because a `cites: []` array
     has no room for one. All that is left is the key itself, which is a
     convention (`surname` + year), not data. `lusztig1989` says only
     "something by Lusztig around 1989", and Lusztig published a great deal
     in 1989. Treat every hit as a question, not an answer, and read the
     citing block before accepting one.

Rate limits are respected: Semantic Scholar's unauthenticated limit is low,
so requests are spaced and failures are recorded rather than retried in a
loop.

Usage:
    scripts/enrich-dangling-citations.py                  # all tiers
    scripts/enrich-dangling-citations.py --tier identifier
    scripts/enrich-dangling-citations.py --out docs/audits/citation-candidates.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(REPO, "docs", "audits", "citation-candidates.json")
UA = "qou-bibliography-enrichment (https://github.com/litlfred/qou)"
PAUSE = 1.2  # seconds between requests; Semantic Scholar is strict when unauthenticated


def fetch(url: str, timeout: int = 25) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"      ! {type(e).__name__}: {str(e)[:90]}", file=sys.stderr)
        return None
    finally:
        time.sleep(PAUSE)


# ---------------------------------------------------------------- sources

def from_arxiv(arxiv_id: str) -> dict | None:
    q = urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    body = fetch(f"https://export.arxiv.org/api/query?{q}")
    if not body:
        return None
    try:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        e = ET.fromstring(body).find("a:entry", ns)
        if e is None:
            return None
        title = " ".join((e.findtext("a:title", "", ns) or "").split())
        if not title:
            return None
        authors = [" ".join((a.findtext("a:name", "", ns) or "").split())
                   for a in e.findall("a:author", ns)]
        published = e.findtext("a:published", "", ns) or ""
        doi = e.findtext("{http://arxiv.org/schemas/atom}doi", None, ns)
        return {"source": "arxiv", "title": title, "authors": authors,
                "year": published[:4] or None, "DOI": doi,
                "URL": f"https://arxiv.org/abs/{arxiv_id}"}
    except ET.ParseError:
        return None


def from_crossref(doi: str) -> dict | None:
    body = fetch(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")
    if not body:
        return None
    try:
        m = json.loads(body).get("message") or {}
    except json.JSONDecodeError:
        return None
    title = (m.get("title") or [None])[0]
    if not title:
        return None
    parts = (m.get("issued") or {}).get("date-parts") or [[None]]
    return {
        "source": "crossref",
        "title": " ".join(title.split()),
        "authors": [" ".join(x for x in (a.get("given"), a.get("family")) if x)
                    for a in (m.get("author") or [])],
        "year": str(parts[0][0]) if parts and parts[0] and parts[0][0] else None,
        "DOI": m.get("DOI"),
        "container-title": (m.get("container-title") or [None])[0],
        "volume": m.get("volume"), "page": m.get("page"),
        "publisher": m.get("publisher"), "type": m.get("type"),
        "URL": m.get("URL"),
    }


def from_semanticscholar(query: str, limit: int = 3) -> list[dict]:
    q = urllib.parse.urlencode({
        "query": query, "limit": limit,
        "fields": "title,year,authors,externalIds,venue,publicationTypes",
    })
    body = fetch(f"https://api.semanticscholar.org/graph/v1/paper/search?{q}")
    if not body:
        return []
    try:
        data = json.loads(body).get("data") or []
    except json.JSONDecodeError:
        return []
    out = []
    for p in data:
        ext = p.get("externalIds") or {}
        out.append({
            "source": "semanticscholar",
            "title": " ".join((p.get("title") or "").split()),
            "authors": [a.get("name") for a in (p.get("authors") or []) if a.get("name")],
            "year": str(p["year"]) if p.get("year") else None,
            "DOI": ext.get("DOI"),
            "arxiv": ext.get("ArXiv"),
            "container-title": p.get("venue") or None,
        })
    return out


# ---------------------------------------------------------------- driving

def dangling() -> dict[str, dict]:
    r = subprocess.run([sys.executable,
                        os.path.join(REPO, "scripts", "check-citation-keys.py"), "--json"],
                       capture_output=True, text=True, cwd=REPO)
    rows = json.loads(r.stdout).get("dangling", [])
    out: dict[str, dict] = {}
    for s in rows:
        e = out.setdefault(s["key"], {"key": s["key"], "sites": [], "tails": set()})
        e["sites"].append(f'{os.path.relpath(s["path"], REPO)}:{s["line"]}')
        if s.get("tail"):
            e["tails"].add(s["tail"].strip())
    for e in out.values():
        e["tails"] = sorted(e["tails"], key=len, reverse=True)
    return out


def plan(entry: dict) -> tuple[str, str]:
    """(tier, query-or-id) for one dangling key."""
    tail = entry["tails"][0] if entry["tails"] else ""
    m = re.search(r"arxiv\.org/abs/([^\s\"?)]+)", tail, re.I)
    if m:
        return "identifier", "arxiv:" + m.group(1).rstrip(".,;")
    m = re.search(r"(?:doi\.org/|\bdoi:\s*)(10\.\d{4,9}/[^\s\"?)]+)", tail, re.I)
    if m:
        return "identifier", "doi:" + m.group(1).rstrip(".,;")
    prose = re.sub(r"https?://\S+", "", tail).strip(" —-–.,;:")
    if len(prose.split()) >= 3:
        return "title", prose
    # Nothing but the key: `surname` + year, by convention.
    key = entry["key"]
    year = (re.search(r"(1[89]\d{2}|20\d{2})", key) or [None])[0]
    names = re.sub(r"(1[89]\d{2}|20\d{2}).*$", "", key).replace("_", "-")
    return "search", " ".join(x for x in [names.replace("-", " ").strip(), year] if x)


def main() -> int:
    ap = argparse.ArgumentParser(description="Propose references.ts entries for dangling keys")
    ap.add_argument("--tier", choices=["identifier", "title", "search"],
                    help="only this tier")
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    keys = dangling()
    print(f"{len(keys)} dangling keys\n")
    results, done = [], 0
    for key, e in sorted(keys.items()):
        tier, q = plan(e)
        if args.tier and tier != args.tier:
            continue
        if args.limit and done >= args.limit:
            break
        done += 1
        print(f"  [{tier}] {key}  <- {q[:60]}")
        cands: list[dict] = []
        if tier == "identifier" and q.startswith("arxiv:"):
            c = from_arxiv(q[6:])
            if c:
                cands.append(c)
        elif tier == "identifier":
            c = from_crossref(q[4:])
            if c:
                cands.append(c)
        if not cands:
            cands = from_semanticscholar(q if tier != "identifier" else q.split(":", 1)[1])
        for c in cands[:3]:
            print(f"        {c.get('year') or '????'}  {str(c.get('title'))[:64]}")
        results.append({"key": key, "tier": tier, "query": q,
                        "sites": e["sites"], "comment": e["tails"][:2],
                        "candidates": cands[:3], "verdict": "needs-agent"})

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"_schema": "citation-candidates/v1",
               "_note": "Machine-proposed. Nothing is written to references.ts from this "
                        "file until an agent sets a verdict. Tier confidence is not "
                        "comparable: `identifier` is exact, `search` is a guess from a "
                        "key that is a naming convention rather than data.",
               "candidates": results},
              open(args.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    got = sum(1 for r in results if r["candidates"])
    print(f"\n{len(results)} keys queried, {got} with at least one candidate")
    print(f"wrote {os.path.relpath(args.out, REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
