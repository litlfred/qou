#!/usr/bin/env python3
"""library-ingest-fidelity-probe — a document can be fully sectioned, carry no
`ocr/` directory, and still be UNSEARCHABLE for the concepts it is about.

WHY THIS EXISTS.  Bean `qou-o6ml` instructs *"re-run path 5 before the next
'this is open' or 'no theorem exists' declaration on this arc"*, and PR #7315
reported `O'Hara's own paper greppable: yes` after ingesting it.  Running that
re-check found the claim is true only in the sense that `grep` executes.
`library/1-s20-0040938391900102-main/` is O'Hara, *Energy of a Knot*, Topology
30(2) 1991 -- a SCANNED pre-digital paper -- and a grep of its sections for the
vocabulary the paper is built on returns **zero**:

    intrinsic distance | regulariz* | renormaliz* | geodesic distance
    | Mobius | arc length | shorter arc          ->  0 hits, all of them

Not because the concepts are absent.  Because the OCR destroyed the mathematics.
Its proof section reads, where an integral belongs:

    I;,,$_~), ~;,(,)~(~l~"'~+~~~~'~z+'+~~~"'i~+~:'lli")r-'di
    b'((S - I). b'(l) 2 2((r + a)-' -2(S+a)-'--2(~+u+2r)~')

🛑 THIS IS A NEW BLIND-SPOT VARIANT, not the one AGENTS.md documents.  The
documented tier-4 trap is *text lives in `ocr/`, `sections/` holds a stub*, and
its discriminator is **does an `ocr/` directory exist**.  Here there is **no
`ocr/` directory at all** -- the degraded OCR *is* the `sections/` content, the
page ranges cover the whole paper (1-4, 4-7), and the byte count is unremarkable.
Every documented check passes.  A reader following AGENTS.md's tier-4 advice
finds no `ocr/`, concludes the sections are good, and greps a wall of rubble.

## TWO DISCRIMINATORS THAT DO NOT WORK -- reported so nobody re-spends them

1. **Whole-document OCR-fidelity statistics.**  Clean-token rate and
   maths-marker density put O'Hara at 69.5 % / 3.52-per-kchar, squarely inside
   the healthy cluster's 69.4-77.7 % / 2.18-4.45.  `arxiv-1904.13129v1`, a
   healthy arXiv paper, scores *lower* on clean-token rate.  It fails because
   the PROSE is largely intact -- the front matter reads fine -- and only the
   mathematics is destroyed, which a word-level statistic cannot see.

2. **Per-section token density.**  Fires on 13 of 20 sections of a healthy
   paper: `tok/kchar < 90` just means "this section is maths-dense", which is
   true of most of a maths paper.

Do not fish for a third threshold.  Trying variants until one separates a
sample of one is selection against the target.

## THE DISCRIMINATOR THIS PROBE IMPLEMENTS, AND ITS LIMIT

**Hypothesis, stated before it was run:** a healthy ingest reproduces most of
its own abstract's content words somewhere in its body; a maths-destroyed one
does not.  `doc_brief` is extractive from the abstract, so the terms come from
the document itself rather than from a judgement about it.

Measured over the 14-document knot-energy cluster:

    O'Hara (known bad)   60.0 %      3 of 5 terms
    every other          85-100 %    12 of 13 at exactly 100 %

🛑 **A LEAD, NOT A VALIDATED DETECTOR.**  O'Hara's brief yields only **5**
terms against 10-20 for the healthy set -- itself a signal, since an extractive
brief drawn from a garbled abstract is short -- but it makes the 60 % a
three-of-five statistic.  And the sample has exactly **one** known-bad
document, so the threshold below is a description of that one point, not a
calibration.  Treat a flag as *"open this and look"*, never as a verdict, and
do not tune the threshold until there are more known-bad documents to tune on.

NOT CLAIMED: that the O'Hara ingest can be repaired (that needs a better OCR
pass over the source scan, which is not this probe's job); that any other
library document is degraded (the cluster is 14 of ~705); or that the recall
statistic would survive contact with a larger sample.
"""

from __future__ import annotations

import glob
import re
import sys

# Function words and paper boilerplate: present in every document regardless of
# ingest quality, so they carry no signal and would inflate every recall score.
STOPWORDS = set("""
the a an and or of to in is are was were for with on at by from as that this
these those it its be been being have has had not no but if then than we our us
they their there here which who whom what when where how all any some each more
most other such only own same so too very can will just should now paper show
shows using used use also may might one two both new
""".split())

# Below this, open the document and look. NOT a verdict — see the module
# docstring: one known-bad point is not a calibration.
RECALL_FLOOR = 0.75
MIN_TERMS = 4  # a brief this short cannot support a recall statistic at all


def brief_terms(doc_dir: str) -> list[str]:
    """Content words of the document's own `doc_brief` (extractive from its
    abstract, so this is the document describing itself)."""
    for path in sorted(glob.glob(f"{doc_dir}/sections/*.md")):
        parts = open(path, encoding="utf-8", errors="replace").read().split("---")
        if len(parts) < 2:
            continue
        match = re.search(r'doc_brief:\s*"(.*?)"\s*$', parts[1], re.S | re.M)
        if match:
            words = re.findall(r"[A-Za-z][A-Za-z-]{3,}", match.group(1))
            return [w.lower() for w in words if w.lower() not in STOPWORDS]
    return []


def body_text(doc_dir: str) -> str:
    out = []
    for path in sorted(glob.glob(f"{doc_dir}/sections/*.md")):
        raw = open(path, encoding="utf-8", errors="replace").read()
        out.append(raw.split("---", 2)[-1].lower())
    return "".join(out)


def score(doc_dir: str) -> tuple[int, int, float] | None:
    terms = sorted(set(brief_terms(doc_dir)))
    if len(terms) < MIN_TERMS:
        return None
    body = body_text(doc_dir)
    found = [t for t in terms if t in body]
    return len(terms), len(found), len(found) / len(terms)


def main(argv: list[str]) -> int:
    targets = argv[1:] or sorted(glob.glob("library/*/"))
    rows: list[tuple[str, int, int, float]] = []
    skipped_short = 0
    for d in targets:
        d = d.rstrip("/")
        r = score(d)
        if r is None:
            skipped_short += 1
            continue
        rows.append((d.rsplit("/", 1)[-1], *r))

    rows.sort(key=lambda r: r[3])
    flagged = [r for r in rows if r[3] < RECALL_FLOOR]

    print(f"{'doc-id':40s} {'terms':>6s} {'found':>6s} {'recall':>7s}")
    for name, n, f, rec in rows[:25]:
        mark = "  <-- OPEN AND LOOK" if rec < RECALL_FLOOR else ""
        print(f"{name:40s} {n:6d} {f:6d} {rec * 100:6.1f}%{mark}")
    if len(rows) > 25:
        print(f"... {len(rows) - 25} more at or above the floor")

    print(f"\nscored {len(rows)}; {skipped_short} skipped "
          f"(doc_brief under {MIN_TERMS} content words — too short to score, "
          f"and itself worth a look)")
    print(f"below the {RECALL_FLOOR:.0%} floor: {len(flagged)}")
    print("\nA flag means OPEN THE DOCUMENT, not 'this is broken'. The floor "
          "describes one known-bad point (O'Hara 1991, 3 of 5 terms); it is "
          "not calibrated, and two cheaper discriminators are already spent — "
          "see the module docstring before adding a third.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
