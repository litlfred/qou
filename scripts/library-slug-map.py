#!/usr/bin/env python3
"""Compute the library/ directory -> bibliography-slug rename map.

Owner ruling 2026-09-15 (fork A = A1+A3, full normalisation): every
`library/<dir>/` is to be named for the bibliography slug that cites it, and
the directories no bib entry points at get a slug MINTED.

This script computes that map and CHANGES NOTHING. It exists because the
minting half cannot be done blind: `structure.json`'s `metadata.authors_raw`
is a heuristic first-page grab and is frequently not the authors at all --
measured values include a journal banner ("View the article online for
updates and enhancements"), HAL boilerplate, a department, a postal address
and the second line of the title. Minting `<surname><year>` off those
produces `enhancements2025` and `duality2000`, i.e. a citation key that
asserts an author who does not exist.

So every proposed slug carries a TIER saying how much it can be trusted:

  bound        a bib entry already points at this dir; slug = that bib id.
               Nothing is invented. 
  mint-high    author line passes the plausibility test AND the year comes
               from the arXiv identifier, which encodes it structurally.
               MEASURED 2026-09-15: this tier is only ~50% correct. A
               seeded sample of 14, hand-checked against the title and the
               author line, was 7 right and 7 wrong -- `pgl2013` and
               `categories2001` off title fragments, `reiter2011` off the
               SECOND author (Blatt is first), `carolynabbott2023` where OCR
               ran given+family together, `society1993` off "AMERICAN
               MATHEMATICAL SOCIETY", `krber2017` with the umlaut stripped
               from Koerber, and `ega2009` where OCR split the ligatures in
               Dolega. So do NOT execute this tier as-is: over 157 dirs it
               would mint roughly 78 wrong citation keys, silently. The
               name is kept because the tier is still the right BUCKET --
               it just needs a real metadata source (arXiv API, Crossref,
               or an agent reading page 1), not `authors_raw`.
  mint-low     author plausible, but the year comes from the PDF's docinfo
               CreationDate -- which is when the FILE was made, not when the
               work was published. Right for a fresh preprint, wrong for a
               scan of a 1907 paper.
  needs-source the author line does not survive the plausibility test, or
               there is no year at all. NOT mintable mechanically.

Usage:  python3 scripts/library-slug-map.py [--json OUT]
"""
import argparse, json, os, re, sys, glob, collections

LIB = "library"
REFS = "folio/schema/references.ts"

# Lines that are demonstrably not an author list. Every one of these was
# observed in the tree; they are not hypothetical.
BOILERPLATE = re.compile(
    r"\b(view the article|updates and enhancements|the documents may come|"
    r"teaching and research|department of|university|institute|laborator|"
    r"downloaded|copyright|all rights reserved|abstract|introduction|"
    r"proceedings|submitted|received|preprint|arxiv|doi|issn|isbn|"
    r"representation theory|algebraic approach)\b", re.I)

# A postal address / numeric noise line.
HAS_LONG_DIGITS = re.compile(r"\d{4,}")


def plausible_author_line(s):
    """Does this look like an author list rather than page furniture?"""
    if not s or not isinstance(s, str):
        return False
    s = s.strip()
    if len(s) < 3 or len(s) > 120:
        return False
    if BOILERPLATE.search(s) or HAS_LONG_DIGITS.search(s):
        return False
    # Needs at least one word of >=3 letters that is not all-caps noise.
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'’-]{3,}", s)
    if not words:
        return False
    # A title tends to be many lowercase function words; an author list is not.
    lower = sum(1 for w in words if w.islower())
    if lower > len(words) / 2:
        return False
    return True


def first_surname(s):
    """Best-effort surname of the first author. Returns None when unsure."""
    if not plausible_author_line(s):
        return None
    # Cut at the first separator between authors.
    head = re.split(r"\s+AND\s+|\s*&\s*|\s*,\s*|\s*;\s*", s.strip(), flags=re.I)[0]
    head = re.sub(r"\([^)]*\)", " ", head)          # (∗) (‡) affiliation marks
    head = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ'’ -]", " ", head)
    parts = [p for p in head.split() if len(p) > 1]
    if not parts:
        return None
    # Drop leading initials ("J.", "J ÉR ÔME" -> take the last token).
    surname = parts[-1]
    surname = re.sub(r"[^a-z]", "", surname.lower())
    return surname or None


def year_from_arxiv(arx):
    """arXiv ids encode the year: 0706.2213 -> 2007, 2411.03801 -> 2024,
    math/0405258 -> 2004. Structural, so trustworthy."""
    if not arx:
        return None
    ident = arx.get("id") if isinstance(arx, dict) else str(arx)
    if not ident:
        return None
    m = re.search(r"(?:^|/)(\d{2})(\d{2})\.", ident)      # new style YYMM.NNNNN
    if not m:
        m = re.search(r"(?:^|/)(\d{2})(\d{2})\d{3}", ident)  # old style YYMMNNN
    if not m:
        return None
    yy = int(m.group(1))
    return str(1900 + yy) if yy >= 90 else str(2000 + yy)


def year_from_docinfo(di):
    if not isinstance(di, dict):
        return None
    for k in ("year", "date", "CreationDate", "ModDate"):
        v = di.get(k)
        if v:
            m = re.search(r"(19|20)\d{2}", str(v))
            if m:
                return m.group(0)
    return None


def bib_bindings(path):
    """docId -> bib id, parsed from the references.ts ref({...}) blocks."""
    src = open(path, encoding="utf-8").read()
    out = {}
    for b in re.findall(r"ref\(\{(.*?)\n  \}\)", src, re.S):
        i = re.search(r'id:\s*"([^"]+)"', b)
        d = re.search(r'docId:\s*"([^"]+)"', b)
        if i and d:
            out[d.group(1)] = i.group(1)
    return out, set(re.findall(r'^\s*id:\s*"([^"]+)"', src, re.M))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="write the full map here")
    a = ap.parse_args()

    bound, all_slugs = bib_bindings(REFS)
    dirs = sorted(os.path.basename(p.rstrip("/")) for p in glob.glob(f"{LIB}/*/"))

    rows = []
    for d in dirs:
        try:
            meta = json.load(open(f"{LIB}/{d}/structure.json", encoding="utf-8")).get("metadata", {})
        except Exception:
            meta = {}
        if d in bound:
            rows.append(dict(dir=d, slug=bound[d], tier="bound", why="bib entry points here"))
            continue
        surname = first_surname(meta.get("authors_raw"))
        y_hi = year_from_arxiv(meta.get("arxiv"))
        y_lo = year_from_docinfo(meta.get("docinfo"))
        if surname and y_hi:
            rows.append(dict(dir=d, slug=f"{surname}{y_hi}", tier="mint-high",
                             why="plausible author + arXiv-encoded year"))
        elif surname and y_lo:
            rows.append(dict(dir=d, slug=f"{surname}{y_lo}", tier="mint-low",
                             why="plausible author + docinfo CreationDate (file date, not publication year)"))
        else:
            reason = []
            if not surname:
                reason.append("author line not usable" if meta.get("authors_raw") else "no author line")
            if not (y_hi or y_lo):
                reason.append("no year")
            rows.append(dict(dir=d, slug=None, tier="needs-source", why="; ".join(reason)))

    # Deterministic collision suffixes, over minted slugs only. A minted slug
    # may also collide with an EXISTING bib id, which is the worse case: it
    # would silently merge two different works under one citation key.
    seen = collections.Counter()
    for r in sorted((r for r in rows if r["slug"] and r["tier"] != "bound"),
                    key=lambda r: r["dir"]):
        base = r["slug"]
        clash_existing = base in all_slugs
        n = seen[base]
        seen[base] += 1
        if clash_existing or n:
            r["slug"] = f"{base}{chr(ord('a') + n)}"
            r["collision"] = "existing bib id" if clash_existing else f"#{n+1} minted"

    tiers = collections.Counter(r["tier"] for r in rows)
    renames = sum(1 for r in rows if r["slug"] and r["slug"] != r["dir"])
    noop = sum(1 for r in rows if r["slug"] == r["dir"])

    print(f"library dirs                  {len(rows)}")
    for t in ("bound", "mint-high", "mint-low", "needs-source"):
        print(f"  {t:<14} {tiers[t]:>4}")
    print(f"\ndirs whose name already IS the slug   {noop}")
    print(f"dirs that would be renamed            {renames}")
    print(f"collisions needing a suffix           {sum(1 for r in rows if r.get('collision'))}")
    print(f"NOT mintable without a human/agent    {tiers['needs-source']}")

    bad = [r for r in rows if r["tier"] == "mint-low"]
    if bad:
        print(f"\nmint-low samples (year is the FILE date, verify before use):")
        for r in bad[:6]:
            print(f"  {r['dir'][:40]:<42} -> {r['slug']}")
    ns = [r for r in rows if r["tier"] == "needs-source"]
    if ns:
        print(f"\nneeds-source samples:")
        for r in ns[:6]:
            print(f"  {r['dir'][:40]:<42} ({r['why']})")

    if a.json:
        os.makedirs(os.path.dirname(a.json) or ".", exist_ok=True)
        json.dump({"schema": "library-slug-map/v1", "rows": rows},
                  open(a.json, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
