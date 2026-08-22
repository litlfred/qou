#!/usr/bin/env python3
"""
library-refresh-metadata — re-derive each document's title and authors with
the current extractor, without disturbing anything else.

## Why not just re-run the producer

Because `pdf-structure.py` writes a whole `structure.json`, and this
library's `structure.json` files now carry state the producer knows
nothing about: `container` markers from the bound-volume split, and
`duplicate_of` / `duplicate_copies` from the duplicate adjudication. A
straight re-run silently discards all of it.

So the producer is called in `--json` mode, which writes nothing, and only
`metadata` is merged. Section files are left alone: their text is
unchanged by a metadata fix, and rewriting 6,900 files to no effect is not
free for a reviewer.

## What actually changes

`pdf-structure.py` learned to repair two kinds of PDF extraction damage —
ligatures and floating accents (`Reﬁned`, `Gr¨ obner`) and kerning splits
(`STA VROS GAROUF ALIDIS`) — and to skip more publisher front matter that
was being taken as the title. Titles extracted before that landed in
`library/INDEX.md` and in `references.ts`, where a search for
"Garoufalidis" does not match "GAROUF ALIDIS".

The previous title is kept as `metadata.title_prev` whenever it differs,
so a bad repair is visible and reversible rather than silently overwriting
what a reader may have already cited.

## Where a title comes from, in order of authority

1. **An override** in `docs/audits/library-title-overrides.json` — a reader
   opened the document and wrote down what it says.
2. **The registered bibliography title**, when `references.ts` has an entry
   whose `library:` block names this document. That title was read and
   reviewed when the entry was written, so it is a reader verdict too, and
   it is normally the better one: it has the byline, the masthead and the
   journal furniture already stripped.
3. **The extractor**, for everything else.

Rule 2 is applied only when the two differ by more than case and
punctuation. Where they are the same words, the document's own rendering is
kept — an all-caps title is not a defect and rewriting 117 of those would be
churn with no reader benefit.

## Hand verdicts are applied here too

`docs/audits/library-title-overrides.json` records titles a reader
corrected by opening the document. Those were reaching `references.ts`,
because the proposer applies them, and *not* reaching `structure.json` —
so the bibliography said "TURAEV-VIRO INVARIANTS" while every corpus-grep
hit in that document still carried `doc_title: "TURAEV-VIRO INV ARIANTS"`
in its front matter. One file of verdicts, two sinks, and only one of them
was reading it.

Applying an override rewrites the section files' `doc_title` and the title
prefix of `doc_brief` as well. It has to: a `structure.json` that disagreed
with its own sections would be worse than either being wrong alone, since
a reader has no way to tell which one is stale.

Usage:
    scripts/library-refresh-metadata.py                # dry run, shows diffs
    scripts/library-refresh-metadata.py --apply
    scripts/library-refresh-metadata.py --only <doc-id>
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
PRODUCER = os.path.join(os.path.dirname(REPO), "folio-assistant",
                        "scripts", "pdf-structure.py")

# `title_lines` matters as much as `title`: it is what lets a consumer
# split a byline off, and omitting it here silently withheld the fix
# that had just been added to the producer for exactly that purpose.
FIELDS = ("title", "title_lines", "authors_raw", "abstract", "arxiv", "doi")

OVERRIDES = os.path.join(REPO, "docs", "audits", "library-title-overrides.json")
REFS = os.path.join(REPO, "content", "schema", "references.ts")


def registered_titles() -> dict[str, str]:
    """docId -> title, for every references.ts entry naming a library copy.

    Brace-matched rather than line-scanned: an entry's fields are indented
    and its `title` and `docId` sit in different nested objects, so a
    regex over the whole file pairs a title with the wrong document about
    as often as not.
    """
    try:
        src = open(REFS, encoding="utf-8").read()
    except Exception:
        return {}
    out: dict[str, str] = {}
    for m in re.finditer(r"\bref\(\{", src):
        i = src.index("{", m.start())
        depth = 0
        block = ""
        for j in range(i, len(src)):
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
                if depth == 0:
                    block = src[i:j + 1]
                    break
        d = re.search(r'docId:\s*"([^"]+)"', block)
        t = re.search(r'title:\s*"((?:[^"\\]|\\.)*)"', block)
        if d and t:
            out[d.group(1)] = t.group(1).replace('\\"', '"')
    return out


def same_words(a: str, b: str) -> bool:
    """Equal ignoring case, punctuation, accents and spacing."""
    f = lambda s: re.sub(r"[^a-z0-9]", "",
                         unicodedata.normalize("NFKD", s or "").lower())
    return f(a) == f(b)


def overrides() -> dict:
    try:
        return json.load(open(OVERRIDES, encoding="utf-8")).get("overrides") or {}
    except Exception:
        return {}


def propagate(doc: str, title: str) -> int:
    """Rewrite `doc_title` and the `doc_brief` title prefix in one doc's sections.

    `doc_brief` opens with the title followed by " — ", so only that prefix
    is replaced; the extracted sentence after it is untouched. A brief that
    does not start with the old title is left entirely alone rather than
    guessed at.
    """
    n = 0
    secs = os.path.join(LIB, doc, "sections")
    for f in sorted(glob.glob(os.path.join(secs, "*.md"))):
        text = open(f, encoding="utf-8").read()
        out, changed = [], False
        for line in text.split("\n"):
            if line.startswith("doc_title: \""):
                new = f'doc_title: "{title[:180]}"'
                changed |= new != line
                line = new
            elif line.startswith("doc_brief: \""):
                body = line[len('doc_brief: "'):].rstrip('"')
                if " — " in body:
                    _, rest = body.split(" — ", 1)
                    new = f'doc_brief: "{title} — {rest}"'
                    changed |= new != line
                    line = new
            out.append(line)
        if changed:
            open(f, "w", encoding="utf-8").write("\n".join(out))
            n += 1
    return n


def extract(pdf: str) -> dict | None:
    r = subprocess.run([sys.executable, PRODUCER, "--json", pdf],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return json.loads(r.stdout).get("metadata") or {}
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Re-derive library metadata with the current extractor")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", help="single doc-id")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    if not os.path.exists(PRODUCER):
        sys.exit(f"producer not found: {PRODUCER}\n"
                 "run scripts/setup-folio-assistant.sh first")

    docs = sorted(os.listdir(LIB))
    if args.only:
        docs = [d for d in docs if d == args.only]

    ovr = overrides()
    reg = registered_titles()
    changed = failed = seen = propagated = 0
    for doc in docs:
        d = os.path.join(LIB, doc)
        sj = os.path.join(d, "structure.json")
        if not (os.path.isdir(d) and os.path.exists(sj)):
            continue
        pdfs = sorted(glob.glob(os.path.join(d, "*.pdf")))
        if not pdfs:
            continue
        seen += 1
        if args.limit and changed >= args.limit:
            break
        try:
            art = json.load(open(sj))
        except Exception:
            failed += 1
            continue
        # A container's own metadata describes the bound issue, not a
        # paper; its children carry the papers and are refreshed on their
        # own terms.
        if art.get("container"):
            continue

        fresh = extract(pdfs[0])
        if fresh is None:
            failed += 1
            print(f"  !! {doc}: extraction failed")
            continue

        # A hand verdict outranks the extractor. It was read out of the
        # document by someone who opened it, and re-deriving would put the
        # damage straight back on the next run.
        for field, key in (("title", "title"), ("authors_raw", "authors_raw")):
            if (ovr.get(doc) or {}).get(key):
                fresh[field] = ovr[doc][key]

        # Then the bibliography, which has already had a reader strip the
        # masthead and the byline. Only when it is a different title, not
        # merely a different casing of the same one.
        if doc in reg and not (ovr.get(doc) or {}).get("title"):
            if not same_words(fresh.get("title") or "", reg[doc]):
                fresh["title"] = reg[doc]

        old = art.get("metadata") or {}
        diffs = {k: (old.get(k), fresh.get(k)) for k in FIELDS
                 if fresh.get(k) and old.get(k) != fresh.get(k)}
        if not diffs:
            continue
        changed += 1
        for k, (a, b) in diffs.items():
            if k in ("abstract", "arxiv", "doi"):
                continue
            print(f"  {doc}")
            print(f"     {k}: {str(a)[:88]}")
            print(f"     {'':>{len(k)}}  -> {str(b)[:88]}")

        if args.apply:
            md = dict(old)
            for k, (a, b) in diffs.items():
                if k == "title" and a:
                    md["title_prev"] = a
                md[k] = b
            art["metadata"] = md
            json.dump(art, open(sj, "w"), indent=1, ensure_ascii=False)
            if "title" in diffs:
                n = propagate(doc, md["title"])
                propagated += n
                if n:
                    print(f"     -> rewrote doc_title in {n} section files")

    print(f"\n{seen} documents, {changed} with changed metadata, {failed} failed"
          + (f", {propagated} section files re-titled" if propagated else ""))
    if not args.apply:
        print("dry run — re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
