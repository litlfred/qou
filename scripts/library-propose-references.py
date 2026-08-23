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
OVERRIDES = os.path.join(REPO, "docs", "audits", "library-title-overrides.json")

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


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:60]


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
    # A digit means the line still carries title content. "E8 Lei Yang" is
    # a byline preceded by the last word of the title, and dropping the
    # whole line cost "Modular curves, invariant theory and E8" its E8.
    if re.search(r"\d", last):
        return " ".join(lines), []
    au = split_authors(last)
    # Every token of the line must be accounted for by the parsed names.
    # A tolerance of even one token is what let the E8 through.
    whole = au and len(" ".join(a["given"] + " " + a["family"] for a in au).split()) \
        == len(last.split())
    if whole and len(" ".join(head).split()) >= 3 and len(last.split()) <= 6:
        return " ".join(head), au
    return " ".join(lines), []


# Stripping a run-on journal masthead generically was tried and does not
# work. The furniture does not end at the volume/year marker — Kirby's
# offprint reads "Inventiones math. 45, 35- 56 (1978) mathematicae 9 by
# Springer-Verlag 197 A Calculus for Framed Links", with three more
# fragments after the year — and a rule loose enough to reach the title
# also cut a Communications in Mathematical Physics masthead down to
# "Mathematical Physics Springer-Verlag 1986" and called it a title.
# These go in the override file instead, one document at a time.


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
        # A digit means it is a mathematical object, not a surname: E8, K3,
        # SU2, AdS5 all end titles legitimately, and stripping them cost
        # "Modular curves, invariant theory and E8" its subject.
        while (len(words) > 5 and words[-1].isupper()
               and not any(c.isdigit() for c in words[-1])
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


def arxiv_year(ax: str) -> str:
    """Year from an arXiv id. New-style ids are YYMM.NNNNN; old-style ones
    carry YYMMNNN after the slash. Both are unambiguous back to 1991, which
    predates every paper here."""
    m = re.match(r"(\d{2})(\d{2})\.", ax or "")
    if not m:
        m = re.search(r"/(\d{2})(\d{2})\d{3}", ax or "")
    if not m:
        return ""
    yy = int(m.group(1))
    return str(1900 + yy if yy >= 91 else 2000 + yy)


# Words that are not surnames. Each was emitted as one by the parser: a
# city standing in for a university, a department, a stray fragment.
NOT_A_SURNAME = {
    "physics", "mathematics", "institute", "institut", "university", "bonn",
    "kiev", "moscow", "princeton", "korea", "japan", "china", "germany",
    "department", "faculty", "school", "centre", "center", "theory",
}
# JHEP and several other houses suffix the affiliation marker directly to
# the surname — "Adam R. Browna", "Marcos Mariñob" — and print the
# affiliations as "aPrinceton", "bKorea". The suffix is indistinguishable
# from a real final letter in one name; what gives it away is the byline
# carrying the matching lower-case-then-capital affiliation tokens.
RE_AFFIL_MARKER = re.compile(r"\b[a-z][A-Z\u00c0-\u00de]")


def authors_trustworthy(authors: list[dict], raw: str) -> bool:
    """Reject a parsed author list rather than emit a wrong one.

    An entry carrying a correct title, arXiv id and library pointer with no
    authors is honest and useful. One naming "Bonn" or "Browna" is wrong,
    and it propagates: the reference id is built from the first surname.
    """
    if not authors:
        return False
    for a in authors:
        fam = a["family"]
        if len(re.sub(r"[^\w]", "", fam)) < 2:
            return False
        if fam.lower() in NOT_A_SURNAME or a["given"].lower() in NOT_A_SURNAME:
            return False
    if RE_AFFIL_MARKER.search(raw or ""):
        return False
    # The affiliation marker is often only visible as a pattern across the
    # list: "Browna", "Robertsb", "Susskinda" are three surnames ending in
    # a stray a/b. One such name is a coincidence; two are a house style.
    suffixed = sum(1 for a in authors
                   if re.search(r"[a-z\u00e0-\u00ff][abcde]$", a["family"]))
    if suffixed >= 2:
        return False
    # A kerning-split surname ("GAROUF ALIDIS" -> family "ALIDIS") is NOT
    # detectable here and is left to the override file. The obvious test —
    # is this family preceded by another token? — is true of every author
    # that has a given name, and rejected 54 of 64 lists when tried.
    return True


def slug_id(md: dict, doc: str, authors: list[dict]) -> str:
    """`family` + year, matching the ids already in references.ts.

    The year comes from the arXiv id rather than from the text: a year
    scraped out of a title is as likely to be a cited work's date as the
    paper's own.
    """
    fam = re.sub(r"[^a-z]", "", (authors[0]["family"] if authors else "").lower())
    ax = (md.get("arxiv") or {}).get("id") or ""
    yr = arxiv_year(ax)
    if fam and yr:
        return f"{fam}{yr}"
    if fam and ax:
        return f"{fam}-{re.sub(r'[^a-z0-9.]', '', ax.lower())}"
    return re.sub(r"[^a-z0-9.-]", "", doc.lower())[:44]


def strip_comments(src: str) -> str:
    """Blank out `//` and `/* */` comments, leaving string literals alone.

    references.ts documents its own history in comments, and one of them
    quotes the code it is describing:

        // S1/PR #5187 added a second `ref({ id: "orellana1998" })`
        // block at this position — a duplicate key — and it was removed

    A scan for `id: "..."` matches inside that comment, and the block it
    then reads runs to the end of the NEXT entry — so the title of
    Kazhdan-Wenzl was being indexed under the id `orellana1998`, and a
    document with that title would have been reported as already
    registered under the wrong entry.

    Both comment forms have to be handled, and `//` alone is not enough:
    the file opens with a JSDoc block containing "Each entry's `id`", and
    that apostrophe opens a string literal that swallows the next 240
    lines — including a live `URL:` field, which then vanishes from the
    scan. Quotes are tracked so that the `//` in every entry's URL is not
    mistaken for a comment.
    """
    out: list[str] = []
    i, n = 0, len(src)
    quote: str | None = None
    while i < n:
        c = src[i]
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(src[i + 1])
                i += 2
                continue
            if c == quote:
                quote = None
            i += 1
            continue
        if c in "\"'`":
            quote = c
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            if j == -1:
                break
            out.append("\n")
            i = j + 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            if j == -1:
                break
            # Keep the newlines so line numbers in any later message survive.
            out.append("\n" * src.count("\n", i, j + 2))
            i = j + 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Draft references.ts entries for unregistered library documents")
    ap.add_argument("--band", choices=["high", "medium", "low", "registered"])
    ap.add_argument("--emit", action="store_true", help="print TypeScript for the selected band")
    args = ap.parse_args()

    refs = strip_comments(open(REFS, encoding="utf-8").read())
    overrides = (json.load(open(OVERRIDES, encoding="utf-8")).get("overrides", {})
                 if os.path.exists(OVERRIDES) else {})
    # Titles already in the bibliography. A document can be unregistered in
    # the sense that no entry names its doc-id, while the *work* is very
    # much registered — the entry simply was never joined to the library.
    # Proposing it again creates a duplicate: batch 4 did exactly that once,
    # re-registering Bokut-Chen-Li under a second id.
    existing_titles = {}
    for m in re.finditer(r'id:\s*"([^"]+)"', refs):
        blk = refs[m.start():refs.find("\n  }),", m.start())]
        mt = re.search(r'title:\s*\n?\s*"([^"]+)"', blk)
        if mt:
            existing_titles.setdefault(norm_title(mt.group(1)), m.group(1))
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
        # A hand-verified correction wins over every heuristic above. The
        # last few per cent of defects are not worth another rule: one
        # general enough to fix them starts eating real titles.
        ov = overrides.get(doc) or {}
        if ov.get("title"):
            title = ov["title"]

        # Band on the CLEANED title: that is what the entry would carry.
        # A hand-verified title outranks the "no text layer" demotion: that
        # test asks whether the document is READABLE, and an override is an
        # agent saying it read it. Without this, a document whose title was
        # recovered by OCR stayed `low` on the strength of its empty
        # embedded text.
        b, why = band(md, 10 ** 9 if ov.get("title") else chars, title)
        if ov.get("band"):
            b, why = ov["band"], ov.get("why", "hand-verified override")
        # The byline often lands in the title instead of `authors_raw`; when
        # it does, the tail the cleaner removed is where the names are.
        if not au:
            tail = (md.get("title") or "")[len(title):]
            au = split_authors(tail)
        if not authors_trustworthy(au, md.get("authors_raw") or md.get("title") or ""):
            au = []
        # Overrides last, after every fallback — an earlier position was
        # silently undone by the "no authors yet, try the title tail" step
        # below it, which refilled a list the override had just cleared.
        if ov.get("authors"):
            au = ov["authors"]
        elif ov.get("drop_authors"):
            # The field held something else entirely — the title, or a
            # masthead — so the parse is meaningless, not just imprecise.
            au = []
        already = existing_titles.get(norm_title(title))
        if already:
            b, why = "registered", f"already registered as [{already}] — join it to this doc, do not add a second entry"
        rows.append({"doc": doc, "band": b, "why": why, "md": md, "title": title,
                     "pages": art.get("source", {}).get("pages"),
                     "sections": len(art.get("sections") or []), "authors": au})

    sel = [r for r in rows if not args.band or r["band"] == args.band]
    counts = {b: sum(1 for r in rows if r["band"] == b) for b in ("high", "medium", "low", "registered")}
    print(f"{len(rows)} unregistered: "
          + ", ".join(f"{b}={counts[b]}" for b in ("high", "medium", "low", "registered")) + "\n")

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
        rid = (overrides.get(doc) or {}).get("id") or slug_id(md, doc, r["authors"])
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
