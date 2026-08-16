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


# Where a title stops being a title. The extractor often fails to spot the
# author line and runs the two together, so the drafted `title:` would read
# "Fricke S-duality in CHL models Daniel Persson 1 Roberto Volpato 2,3
# 1Fundamental Physics, Chalmers". Each of these is a boundary marker that
# only ever appears at or after the byline, never inside a title.
RE_TITLE_END = re.compile(
    r"(?P<cut>"
    r"[\u2217*\u2020\u2021\u00a7\u00b6]"      # footnote marker on the first author
    # An affiliation superscript: a bare number, at the end or before a
    # comma or another capitalised name. NOT "hyperbolic 3-manifolds" —
    # requiring the digit to stand alone is what keeps a real title whole,
    # and without it "On the number of hyperbolic 3-manifolds of a given
    # volume" was cut to "On the number of hyperbolic".
    r"|(?<=[a-z\u00e0-\u00ff])\s+\d{1,2}(?=\s*(?:,|$)|\s+[A-Z\u00c0-\u00de])"
    r"|\b(?:Department|Institute|Institut|University|Universit|School|Faculty"
    r"|Fakult|Centre|Center|Laborator|Max[- ]Planck|CNRS|Academy|Academia"
    r"|College|Graduate School)\b"
    r"|\b(?:e-?mail|E-?MAIL)\b"
    r")", re.U)

# A dedication or epigraph printed above the title. Greedy to the closing
# word: non-greedy stopped inside the phrase and left "OF HIS 60 TH
# BIRTHDAY" glued to the front of the title.
RE_DEDICATION = re.compile(
    r"^\s*(?:DEDICATED\s+TO|IN\s+MEMORY\s+OF|IN\s+HONOU?R\s+OF)\b"
    r"[^.]*\b(?:BIRTHDAY|ANNIVERSARY|RETIREMENT)\b\s*", re.I)


def strip_byline_line(md: dict) -> tuple[str, list[dict]]:
    """Use `metadata.title_lines` to split a byline off the title.

    The line break is the only reliable boundary. The producer's
    author-line test needs a comma or an "and", so a *single-author*
    byline slips past it and gets appended to the title — and once the
    lines are joined nothing can recover it, because in an all-caps title
    "THEORY TOM BRIDGELAND" has the same shape as "TORUS KNOT".

    Only applied when the producer found no author line at all. If it did,
    the title lines are all title, and dropping the last one would eat a
    two-line title whose second line happens to read like a name ("Hopf
    Algebras").
    """
    lines = md.get("title_lines") or []
    if len(lines) < 2 or (md.get("authors_raw") or "").strip():
        return " ".join(lines) if lines else (md.get("title") or ""), []
    head, last = lines[:-1], lines[-1]
    au = split_authors(last)
    whole = au and len(" ".join(a["given"] + " " + a["family"] for a in au).split()) \
        >= len(last.split()) - 1
    if whole and len(" ".join(head).split()) >= 3 and len(last.split()) <= 6:
        return " ".join(head), au
    return " ".join(lines), []


def clean_title(t: str, authors: list[dict] | None = None) -> str:
    """Trim a title that ran into the byline, and drop a leading dedication.

    When the authors parsed, the first author's own name is the most
    reliable boundary there is — better than any punctuation heuristic,
    which cut "Fricke S-duality in CHL models Daniel Persson 1 ..." only as
    far as "... Daniel Persson".
    """
    if not t:
        return t
    t = RE_DEDICATION.sub("", t).strip()
    if authors:
        first = authors[0]
        for probe in (f"{first['given']} {first['family']}", first["given"]):
            if not probe.strip():
                continue
            i = t.find(probe)
            if i >= 12:
                t = t[:i]
                break
    m = RE_TITLE_END.search(t)
    if m and m.start() >= 12:
        t = t[:m.start()]
    # A trailing name the extractor appended. When the title is mixed-case
    # a trailing all-caps run gives it away; when the title is *itself* all
    # caps that signal is gone, and the tell is a bare initial — "THE
    # STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS ANH T. TRAN".
    words = t.split()
    if len(words) > 5 and not t.isupper():
        while (len(words) > 5 and words[-1].isupper()
               and len(re.sub(r"[^\w]", "", words[-1])) <= 8):
            words.pop()
        t = " ".join(words)
    elif len(words) > 6:
        for i in range(len(words) - 1, max(4, len(words) - 5), -1):
            tail = words[i:]
            if (any(re.fullmatch(r"[A-Z]\.", w) for w in tail)
                    and all(re.fullmatch(r"[^\W\d_][^\W\d_.'\-]*\.?", w, re.U)
                            and len(w) <= 12 for w in tail)):
                t = " ".join(words[:i])
                break
    return re.sub(r"\s{2,}", " ", t).strip(" ,.;:-\u2014\u2217*\u2020\u2021\u00a7\u00b6")


def is_mojibake(s: str) -> bool:
    """Text that decoded through the wrong codec — the RIMS scans arrive
    JIS-encoded and come out as `Fs=E2=7k$SL\\$Ncolored Jones`."""
    if not s:
        return True
    letters = sum(c.isalpha() for c in s)
    return letters < 0.55 * len(s)


# Body text that reached the title slot because the extractor never found a
# title to stop at — a formula, a table of contents, a mid-sentence
# fragment. All observed in this library's "high" band, where an arXiv id
# had wrongly implied the title was fine too.
RE_BODY_TEXT = re.compile(
    r"[∈∏∑√∂≤≥≠×∫⊗ℕℚℝℤ]"
    r"|\bContents\s+\d|\[\d{1,3}\]|\b\d\.\d\.\s|\(\d\.\d\)"
    r"|^\s*[a-zà-ÿ]"                    # opens mid-sentence
    r"|^\s*(?:which|where|and|but|for|with|that|this|it|we|in|of)\b"
    r"|\bc©|\bRevised Edition\b",
    re.U,
)

# A title that is only a department, a field, or a bare institutional word.
RE_TOO_GENERIC = re.compile(
    r"^\s*(?:Department|Mathematics|Physics|Institute|Faculty|School|Abstract)"
    r"(?:\s+(?:of|for|de|des)\s+\w+)?\s*$", re.I)


def band(md: dict, chars: int, title: str | None = None) -> tuple[str, str]:
    """Confidence in the *drafted entry*, which needs the title to be right.

    An arXiv id used to be enough for `high`. It is not: the id makes
    identity certain and says nothing about the title, and five documents
    whose "title" was a formula or a table of contents were banded high on
    the strength of their id alone.
    """
    raw = (md.get("title") or "").strip()
    title = raw if title is None else title
    if chars < 3000:
        return "low", f"only {chars} chars extracted — probably a scan with no text layer"
    if not title or len(title) < 12:
        return "low", "no usable title extracted"
    if is_mojibake(title):
        return "low", "title is mojibake — wrong codec on an East-Asian scan"
    if JUNK_TITLE.search(title):
        return "low", "title looks like publisher furniture, not a paper title"
    if RE_BODY_TEXT.search(title):
        return "low", "title slot holds body text — a formula, a contents list, or a fragment"
    if RE_TOO_GENERIC.match(title):
        return "low", "title is a bare department or field name"
    if (md.get("arxiv") or {}).get("id"):
        return "high", "arXiv id anchors identity, and the title survives every check"
    return "medium", "no arXiv id — identity rests on the extracted title alone"


def split_authors(raw: str) -> list[dict]:
    """`authors_raw` (or a title's byline tail) -> CSL author objects.

    Conservative by construction: returns [] rather than guess. A wrong
    author is a worse bibliography entry than a missing one, and this field
    routinely receives affiliation lines instead of names.

    Two things it has to get right, both from observed damage. Splitting on
    a bare "and" left a fragment beginning with "AND", which then became a
    given name ("YAMAGUCHI, AND YOSHIKAZU"). And affiliation superscripts
    run into the surname — "Davide Gaiotto, 1 Gregory W. Moore 2 and Andrew
    Neitzke 3" — so the digits have to go before the split, not after, or
    the second and third authors are lost.
    """
    if not raw:
        return []
    s = re.split(r"\b(?:Department|Institute|Institut|University|Universit|"
                 r"School|Faculty|Fakult|Centre|Center|Laborator|Max[- ]Planck|"
                 r"CNRS|Academy|Academia|College)\b", raw, 1)[0]
    s = re.sub(r"[\d\u2217*\u2020\u2021\u00a7\u00b6]", " ", s)
    parts = [p.strip(" ,.&") for p in re.split(r",|\band\b|&", s, flags=re.I)
             if p.strip(" ,.&")]
    out = []
    for p in parts:
        toks = [t for t in p.split() if t]
        if toks and toks[0].lower() in ("and", "with"):
            toks = toks[1:]
        if not (2 <= len(toks) <= 4):
            return out
        # A letter, then letters/dots/apostrophes/hyphens: "W.", "O'Brien",
        # "Dubois-Violette". The dot has to be *allowed*, not excluded — as a
        # negated class it rejected every middle initial, which silently
        # truncated author lists at the first one.
        if not all(re.match(r"^[^\W\d_](?:[^\W\d_]|[.'\-])*$", t, re.U) for t in toks):
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
        au = split_authors(md.get("authors_raw") or "")
        # The line break is the strongest title/byline boundary there is.
        raw_title, byline_au = strip_byline_line(md)
        au = au or byline_au
        title = clean_title(raw_title, au)
        # Band on the CLEANED title: that is what the entry would carry.
        b, why = band(md, chars, title)
        # The byline often lands in the title instead of `authors_raw`; when
        # it does, the tail the cleaner removed is where the names are.
        if not au:
            tail = (md.get("title") or "")[len(title):]
            au = split_authors(tail)
        rows.append({"doc": doc, "band": b, "why": why, "md": md, "title": title,
                     "pages": art.get("source", {}).get("pages"),
                     "sections": len(art.get("sections") or []), "authors": au})

    sel = [r for r in rows if not args.band or r["band"] == args.band]
    counts = {b: sum(1 for r in rows if r["band"] == b) for b in ("high", "medium", "low")}
    print(f"{len(rows)} unregistered: "
          + ", ".join(f"{b}={counts[b]}" for b in ("high", "medium", "low")) + "\n")

    if not args.emit:
        for r in sel:
            md = r["md"]
            ax = (md.get("arxiv") or {}).get("id")
            print(f"[{r['band']:>6}] {r['doc'][:40]:<40} {ax or '':<13} {r['pages']}pp")
            print(f"           title  : {(r['title'] or '(none)')[:96]}")
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
        title = re.sub(r"\s+", " ", r["title"]).replace('"', "'")
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
