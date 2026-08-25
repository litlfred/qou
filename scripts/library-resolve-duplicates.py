#!/usr/bin/env python3
"""
library-resolve-duplicates — nominate a canonical copy for each duplicate
group and mark the others, without deleting anything.

`library-find-duplicates.py` *proposes* pairs. This acts on the ones an
agent has confirmed: one copy per group is named canonical, the rest get
a `duplicate_of` pointer, and the ranking and summaries stop
double-counting them.

## Why it will not act on the detector's output directly

Because the detector cannot tell "same work" from "same authors, same
topic, shared setup sections". Measured over this library: same-work
pairs score 0.248-1.000 on char-gram Jaccard, and genuinely different
papers score 0.159-0.435. Those ranges overlap, so there is no threshold
that separates them — the highest-scoring different-work pair (two
Morita papers on the Ramanujan q-difference equation, 0.435) outscores
four true duplicates.

So verdicts live in `docs/audits/library-duplicate-ledger.json`, written
by an agent who read the titles. A group is acted on only when its
verdict is `same-work`. A pair the detector proposes but nobody has read
is reported as unadjudicated and left alone. This mirrors the review
ledger the Lean vacuity audit already uses for the same reason: the
machine flags, only a reader decides.

## Nothing is deleted

A duplicate copy stays on disk with its sections intact. Something may
already cite its path — `computations/` provenance strings name library
paths, and 1,800 references across the repo were rewritten to them — and
breaking those to save a few megabytes is a bad trade. Marking is
reversible; deleting is not.

## How canonical is chosen, in order

1. **Already registered.** If exactly one copy is named by a
   `references.ts` entry's `library:` block, that copy wins. The
   bibliography has already made the choice and the entry's citations
   depend on it.
2. **Carries an arXiv id.** A stable public identifier beats a filename.
3. **More extracted text.** A published version usually carries more than
   its preprint, and more text greps better.
4. **Lexicographic**, only to make the result deterministic.

Rule 1 can disagree with rule 2, and when it does rule 1 wins on purpose:
re-pointing an existing citation is a bigger change than preferring a
prettier identifier.

## Effect

- `structure.json` of a non-canonical copy gains `duplicate_of` and
  `duplicate_note`.
- `summarize-library.py` and `library-relevance-rank.py` skip anything
  carrying `duplicate_of`, exactly as they already skip a `container`.
- The canonical copy gains `duplicate_copies` listing the others, so the
  relationship is discoverable from either end.

Usage:
    scripts/library-resolve-duplicates.py            # dry run
    scripts/library-resolve-duplicates.py --apply
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
REFS = os.path.join(REPO, "content", "schema", "references.ts")
LEDGER = os.path.join(REPO, "docs", "audits", "library-duplicate-ledger.json")


def confirmed_groups() -> tuple[list[list[str]], list[list[str]]]:
    """Union the ledger's `same-work` entries; return (confirmed, rejected).

    Union-find because a work held three times is reported as three
    overlapping pairs, and marking each pair independently would name
    three different canonicals for one work.
    """
    led = json.load(open(LEDGER, encoding="utf-8"))
    parent: dict[str, str] = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    rejected = []
    for row in led.get("adjudicated", []):
        docs = row.get("docs") or []
        if row.get("verdict") == "same-work":
            for d in docs[1:]:
                union(docs[0], d)
        elif row.get("verdict") == "different-work":
            rejected.append(docs)

    out: dict[str, list[str]] = {}
    for d in parent:
        out.setdefault(find(d), []).append(d)
    return [sorted(v) for v in out.values() if len(v) > 1], rejected


def facts(doc: str, refs: str) -> dict:
    sj = os.path.join(LIB, doc, "structure.json")
    art = {}
    if os.path.exists(sj):
        try:
            art = json.load(open(sj))
        except Exception:
            art = {}
    md = art.get("metadata") or {}
    chars = sum((s.get("n_chars") or 0) for s in (art.get("sections") or []))
    return {
        "doc": doc,
        "registered": f'docId: "{doc}"' in refs,
        "arxiv": bool((md.get("arxiv") or {}).get("id")),
        "chars": chars,
    }


def choose(group: list[str], refs: str) -> tuple[str, str]:
    f = [facts(d, refs) for d in group]
    reg = [x for x in f if x["registered"]]
    if len(reg) == 1:
        return reg[0]["doc"], "is named by a references.ts entry"
    pool = reg if reg else f
    ax = [x for x in pool if x["arxiv"]]
    if len(ax) == 1:
        return ax[0]["doc"], "carries an arXiv id"
    pool2 = ax if ax else pool
    best = max(pool2, key=lambda x: (x["chars"], x["doc"]))
    if len(pool2) > 1 and best["chars"] > min(x["chars"] for x in pool2):
        return best["doc"], "has more extracted text"
    return sorted(x["doc"] for x in pool2)[0], "won a lexicographic tie-break"


def main() -> int:
    ap = argparse.ArgumentParser(description="Mark non-canonical copies of adjudicated duplicate groups")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    refs = open(REFS, encoding="utf-8").read()
    groups, rejected = confirmed_groups()
    print(f"{len(groups)} confirmed same-work groups "
          f"({len(rejected)} pairs adjudicated different-work, left alone)\n")

    marked = 0
    for g in groups:
        canon, why = choose(g, refs)
        others = [d for d in g if d != canon]
        print(f"  canonical: {canon}   ({why})")
        for d in others:
            print(f"     dup -> {d}")
        if not args.apply:
            continue
        for d in others:
            sj = os.path.join(LIB, d, "structure.json")
            if not os.path.exists(sj):
                continue
            art = json.load(open(sj))
            art["duplicate_of"] = canon
            art["duplicate_note"] = (
                f"Same work as library/{canon}/, which was chosen as canonical because it "
                f"{why}. Kept on disk rather than deleted — existing citations may point "
                "here — but skipped by the ranking and the summary index so one work is "
                "not counted twice."
            )
            json.dump(art, open(sj, "w"), indent=1)
            marked += 1
        sjc = os.path.join(LIB, canon, "structure.json")
        if os.path.exists(sjc):
            art = json.load(open(sjc))
            art["duplicate_copies"] = others
            json.dump(art, open(sjc, "w"), indent=1)

    # Anything the detector proposes that nobody has read yet. Without
    # this the ledger silently goes stale as documents are added, and a
    # duplicate that arrived after the last reading is indistinguishable
    # from one that was read and rejected.
    seen = set()
    for row in json.load(open(LEDGER, encoding="utf-8")).get("adjudicated", []):
        seen.add(frozenset(row.get("docs") or []))
    known = {d for s in seen for d in s}
    r = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "library-find-duplicates.py"),
                        "--json"], capture_output=True, text=True, cwd=REPO)
    proposed = json.loads(r.stdout)
    pending = [(p["a"], p["b"]) for p in proposed["near"]
               if not (p["a"] in known and p["b"] in known)]
    pending += [(g[0], g[i]) for g in proposed["exact"] for i in range(1, len(g))
                if not all(d in known for d in g)]
    if pending:
        print(f"\n{len(pending)} proposed pairs NOT in the ledger — read and adjudicate these:")
        for a, b in pending:
            print(f"   {a}   {b}")

    if args.apply:
        print(f"\nmarked {marked} non-canonical copies across {len(groups)} groups")
        print("now re-run summarize-library.py --apply and library-relevance-rank.py")
    else:
        print("\ndry run — re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
