#!/usr/bin/env python3
"""
library-propose-references — draft `references.ts` entries for library
documents that have none, and say how much to trust each draft.

## Proposals, not registrations

This writes nothing into `references.ts`. It emits candidate entries with a
confidence band and the evidence behind each, for an agent to read before
any of it is committed.

That split is not ceremony. An earlier pass in this session used a
mechanical quality filter and it passed *"HAL is a multi-disciplinary open
access archive"* and *"ANNALES DE LA FACULTÉ DES SCIENCES"* as paper
titles — repository boilerplate and a journal masthead. Those would have
entered the bibliography as the titles of real works, and a bibliography
that lies about a title is worse than one that omits it. So the filter
here is used to *sort* proposals, never to approve them.

## What sets the confidence band

  high    an arXiv id, plus a title that survives every junk test
  medium  a title that survives, no arXiv id — identity rests on the title
  low     the title looks like publisher furniture, is mojibake, or the
          document extracted almost no text (a scan with no text layer)

`low` is the interesting band: those documents are not registrable from
extracted metadata at all and need page 1 read by hand.

Usage:
    scripts/library-propose-references.py                 # all, by band
    scripts/library-propose-references.py --band high
    scripts/library-propose-references.py --emit          # TypeScript
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
REFS = os.path.join(REPO, "content", "schema", "references.ts")

# Boilerplate that is not a title. Every one of these was observed leading
# an extracted title in this library.
JUNK_TITLE = re.compile(
    r"HAL is a|multi-disciplinary open access|archive for the deposit"
    r"|Downloaded from|Contents lists|www\.|https?://|ISSN"
    r"|^\s*(?:ANNALES|TRANSACTIONS|PROCEEDINGS|COMMUNICATIONS|BULLETIN|JOURNAL"
    r"|MEMOIRS|ANNALS)\b[^a-z]*$"
    r"|^\s*Vol(?:ume)?\.?\s*\d|^\s*\d+\s*$"
    r"|Prepared for submission",
    re.I,
)


def is_mojibake(s: str) -> bool:
    """Text that decoded through the wrong codec — the RIMS scans arrive
    JIS-encoded and come out as `Fs=E2=7k$SL\\$Ncolored Jones`."""
    if not s:
        return True
    letters = sum(c.isalpha() for c in s)
    return letters < 0.55 * len(s)


def band(md: dict, chars: int) -> tuple[str, str]:
    title = (md.get("title") or "").strip()
    if chars < 3000:
        return "low", f"only {chars} chars extracted — probably a scan with no text layer"
    if not title or len(title) < 12:
        return "low", "no usable title extracted"
    if is_mojibake(title):
        return "low", "title is mojibake — wrong codec on an East-Asian scan"
    if JUNK_TITLE.search(title):
        return "low", "title looks like publisher furniture, not a paper title"
    if (md.get("arxiv") or {}).get("id"):
        return "high", "arXiv id anchors identity independently of the title"
    return "medium", "no arXiv id — identity rests on the extracted title alone"


def split_authors(raw: str) -> list[dict]:
    """`authors_raw` -> CSL author objects, conservatively.

    Returns [] rather than guessing when the string does not look like a
    name list: a wrong author is a worse bibliography entry than a missing
    one, and affiliation lines land in this field routinely.
    """
    if not raw:
        return []
    s = re.sub(r"\d|[∗*†‡§¶]", "", raw)
    s = re.split(r"\b(?:Department|Institute|University|School|Centre|Center|"
                 r"Laboratory|Max[- ]Planck|Fakult|CNRS)\b", s, 1)[0]
    parts = [p.strip(" ,.&") for p in re.split(r",|\band\b|&", s) if p.strip(" ,.&")]
    out = []
    for p in parts:
        toks = [t for t in p.split() if t]
        if not (2 <= len(toks) <= 4):
            return [] if len(out) == 0 else out
        if not all(re.match(r"^[^\W\d_][^\W\d_.'\-]*$", t, re.U) for t in toks):
            return out
        out.append({"family": toks[-1], "given": " ".join(toks[:-1])})
    return out[:8]


def slug_id(md: dict, doc: str) -> str:
    au = split_authors(md.get("authors_raw") or "")
    fam = re.sub(r"[^a-z]", "", (au[0]["family"] if au else "").lower())
    yr = ""
    m = re.search(r"\b(19|20)\d{2}\b", (md.get("title") or "") + " " + doc)
    if m:
        yr = m.group(0)
    ax = (md.get("arxiv") or {}).get("id") or ""
    if fam:
        return f"{fam}{yr}" if yr else f"{fam}-{ax or doc}"[:40]
    return re.sub(r"[^a-z0-9.-]", "", doc.lower())[:40]


def main() -> int:
    ap = argparse.ArgumentParser(description="Draft references.ts entries for unregistered library documents")
    ap.add_argument("--band", choices=["high", "medium", "low"])
    ap.add_argument("--emit", action="store_true", help="print TypeScript for the selected band")
    args = ap.parse_args()

    refs = open(REFS, encoding="utf-8").read()
    registered = set(re.findall(r'docId: "([^"]+)"', refs))
    existing_ids = set(re.findall(r'id:\s*"([^"]+)"', refs))

    rows = []
    for d in sorted(glob.glob(os.path.join(LIB, "*"))):
        doc = os.path.basename(d)
        sj = os.path.join(d, "structure.json")
        if not (os.path.isdir(d) and os.path.exists(sj)):
            continue
        try:
            art = json.load(open(sj))
        except Exception:
            continue
        if art.get("container") or art.get("duplicate_of") or doc in registered:
            continue
        md = art.get("metadata") or {}
        chars = sum(s.get("n_chars") or 0 for s in (art.get("sections") or []))
        b, why = band(md, chars)
        rows.append({"doc": doc, "band": b, "why": why, "md": md,
                     "pages": art.get("source", {}).get("pages"),
                     "sections": len(art.get("sections") or []),
                     "authors": split_authors(md.get("authors_raw") or "")})

    sel = [r for r in rows if not args.band or r["band"] == args.band]
    counts = {b: sum(1 for r in rows if r["band"] == b) for b in ("high", "medium", "low")}
    print(f"{len(rows)} unregistered: "
          + ", ".join(f"{b}={counts[b]}" for b in ("high", "medium", "low")) + "\n")

    if not args.emit:
        for r in sel:
            md = r["md"]
            ax = (md.get("arxiv") or {}).get("id")
            print(f"[{r['band']:>6}] {r['doc'][:40]:<40} {ax or '':<13} {r['pages']}pp")
            print(f"           title  : {(md.get('title') or '(none)')[:96]}")
            if r["authors"]:
                print(f"           authors: {'; '.join(a['family'] + ', ' + a['given'] for a in r['authors'])[:96]}")
            else:
                print(f"           authors: (not parsed) raw={(md.get('authors_raw') or '')[:66]}")
            if r["band"] == "low":
                print(f"           WHY    : {r['why']}")
        return 0

    for r in sel:
        md, doc = r["md"], r["doc"]
        rid = slug_id(md, doc)
        while rid in existing_ids:
            rid += "a"
        existing_ids.add(rid)
        ax = (md.get("arxiv") or {}).get("id")
        ver = (md.get("arxiv") or {}).get("version")
        title = re.sub(r"\s+", " ", (md.get("title") or "").strip()).replace('"', "'")
        print(f'  ref({{')
        print(f'    id: "{rid}",')
        print(f'    type: "article",')
        print(f'    title: "{title}",')
        if r["authors"]:
            inner = ", ".join('{ family: "%s", given: "%s" }' % (a["family"], a["given"])
                              for a in r["authors"])
            print(f'    author: [{inner}],')
        if md.get("doi"):
            print(f'    DOI: "{md["doi"]}",')
        if ax:
            print(f'    URL: "https://arxiv.org/abs/{ax}",')
        print(f'    note: "PDF library/{doc}/ — registered from library intake; '
              f'metadata extracted from the PDF, not verified against the publisher record.",')
        print(f'  }}),')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
