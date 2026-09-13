#!/usr/bin/env python3
"""Corpus-grep OVER-matching audit — the false-COVERED class.

Every entry in `docs/audits/2026-08-15-detector-blindness-taxonomy.md` before
row 40 is a detector that MISSES something, and the failure mode is a false
ALL-CLEAR: the grep comes back empty and the agent keeps looking.

This audit covers the opposite direction, and it is the worse one. A corpus-grep
term that matches as a SUBSTRING of longer words reports documents that do not
carry the topic at all, and the failure mode is a false COVERED: the agent
concludes path 5 is satisfied and STOPS. A miss leaves you looking; this does
not.

WORKED CASE (why this exists). Running corpus-grep path 5 for this repo's own
knot-energy subject, with a bare unanchored ``ohara`` in the alternation:

    grep -rliE "o'hara|ohara|m(ö|oe)bius energy|knot energy|..." library/*/sections/

reported EIGHT documents. All eight were false. Six were surnames containing
the substring ``ohara`` -- Man**ohara**n, Shin**ohara** (x3), N**ohara**,
I**ohara** -- and the strict re-run (word-boundary O'Hara, Moebius energy,
energy of knots, ropelength, self-repulsive energy) across BOTH the
``sections/`` and ``ocr/`` tiers returns ZERO documents. The library holds no
knot-energy source at all.

WHAT THIS DECIDES, AND WHAT IT DOES NOT.

  Mechanical (this script): a term whose hits are substrings of longer words.
  Reported precisely, with the enclosing words named, so the agent sees
  "Shinohara" rather than a document count.

  NOT mechanical, and deliberately not claimed: a SEMANTIC false positive --
  a term that matches as a genuine standalone word in a document about a
  different subject. In the worked case, ``arxiv-0705.1468v1`` ("Knots in the
  Skyrme-Faddeev model") really does contain the phrase "knot energy", and it
  means SOLITON energy, a different object. No string test separates that from
  the O'Hara sense; only reading does. The selftest below pins this limit so a
  later reader cannot mistake a clean run for subject coverage.

USAGE

    python3 scripts/corpus-grep-overmatch-audit.py --terms "ohara" "knot energy"
    python3 scripts/corpus-grep-overmatch-audit.py --terms ohara --show-words
    python3 scripts/corpus-grep-overmatch-audit.py --selftest

Exit status: 1 if any term is OVER-MATCHING (or if --selftest fails), else 0.

Taxonomy row 40 (bean qou-zou6).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIBRARY = REPO / "library"

# A "word" for boundary purposes: letters plus the two apostrophes that appear
# in this corpus. Deliberately EXCLUDES digits, hyphens and underscores, so
# `O'Hara` is one word (and is bounded when surrounded by space/punctuation)
# while `Manoharan` is one word (so the term `ohara` inside it is NOT bounded).
# Using this instead of `\b` is load-bearing: Python's `\b` treats `'` as a
# non-word character, so `\bo'hara\b` matches the `ohara` inside `Manoharan`'s
# neighbour spellings inconsistently and cannot be reasoned about.
WORD_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'’")


def _is_word_char(ch: str) -> bool:
    return ch in WORD_CHARS


def _enclosing_word(text: str, i: int, j: int) -> str:
    """The maximal run of word characters containing the match [i, j)."""
    a = i
    while a > 0 and _is_word_char(text[a - 1]):
        a -= 1
    b = j
    while b < len(text) and _is_word_char(text[b]):
        b += 1
    return text[a:b]


def _tier_files() -> list[tuple[str, str, Path]]:
    """(doc_id, tier, path) for every greppable library text file.

    Both tiers, because AGENTS.md records that a `sections/` grep is BLIND to
    documents whose text lives in `ocr/` -- 25 of 576 directories, ten of them
    holding under 15 % of their bytes in `sections/`.
    """
    out: list[tuple[str, str, Path]] = []
    if not LIBRARY.is_dir():
        return out
    for doc in sorted(p for p in LIBRARY.iterdir() if p.is_dir()):
        for tier, pattern in (("sections", "*.md"), ("ocr", "*.txt")):
            d = doc / tier
            if d.is_dir():
                out.extend((doc.name, tier, f) for f in sorted(d.glob(pattern)))
    return out


class TermResult:
    def __init__(self, term: str) -> None:
        self.term = term
        self.docs_any: set[str] = set()       # documents matching as a substring
        self.docs_bounded: set[str] = set()   # documents matching as a whole word
        self.enclosing: Counter[str] = Counter()
        # Per-document enclosing words. The global Counter above is a summary and
        # is NOT attributable: reading a word out of it and assigning it to a
        # document is exactly the mistake this field exists to stop. Measured
        # while writing this audit -- the global list named `Hohara`, which was
        # then attributed to the wrong document by hand; it is "S. Hohara" in a
        # reference list of `arxiv-2007.15570v1`. Report per document.
        self.enclosing_by_doc: dict[str, Counter[str]] = {}
        self.hits_any = 0
        self.hits_bounded = 0

    @property
    def docs_substring_only(self) -> set[str]:
        """Documents an unanchored grep reports and a bounded grep does not.

        This set IS the false-COVERED population: every one of them looks like
        a hit and carries none of the topic.
        """
        return self.docs_any - self.docs_bounded

    @property
    def over_matching(self) -> bool:
        return bool(self.docs_substring_only)


def scan(terms: list[str]) -> dict[str, TermResult]:
    results = {t: TermResult(t) for t in terms}
    # Plain substring search, case-insensitive, no regex: the point is to model
    # exactly what a naive `grep -i` does, so the audit cannot be more careful
    # than the thing it is auditing.
    lowered = [(t, t.lower()) for t in terms]
    for doc_id, _tier, path in _tier_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        low = text.lower()
        for term, tl in lowered:
            r = results[term]
            start = 0
            while True:
                i = low.find(tl, start)
                if i < 0:
                    break
                j = i + len(tl)
                start = j
                r.hits_any += 1
                r.docs_any.add(doc_id)
                left_ok = i == 0 or not _is_word_char(text[i - 1])
                right_ok = j == len(text) or not _is_word_char(text[j])
                if left_ok and right_ok:
                    r.hits_bounded += 1
                    r.docs_bounded.add(doc_id)
                else:
                    w = _enclosing_word(text, i, j)
                    r.enclosing[w] += 1
                    r.enclosing_by_doc.setdefault(doc_id, Counter())[w] += 1
    return results


def report(results: dict[str, TermResult], show_words: bool) -> int:
    bad = 0
    for term, r in results.items():
        verdict = "OVER-MATCHING" if r.over_matching else "clean"
        print(f"\n=== {term!r} -> {verdict}")
        print(f"    documents, substring match : {len(r.docs_any)}  ({r.hits_any} hits)")
        print(f"    documents, whole-word match: {len(r.docs_bounded)}  ({r.hits_bounded} hits)")
        if r.over_matching:
            bad += 1
            n = len(r.docs_substring_only)
            print(f"    FALSE-COVERED documents    : {n}"
                  f"  -- reported by an unanchored grep, carrying no whole-word hit")
            top = r.enclosing.most_common(12)
            words = ", ".join(f"{w} x{c}" for w, c in top)
            print(f"    enclosing words (ALL docs) : {words}")
            print("      ^ a summary, NOT attributable to any one document; "
                  "use --show-words")
            if show_words:
                for d in sorted(r.docs_substring_only):
                    per = r.enclosing_by_doc.get(d, Counter())
                    detail = ", ".join(f"{w} x{c}" for w, c in per.most_common())
                    print(f"      - {d}: {detail}")
    print()
    if bad:
        print(f"{bad} of {len(results)} term(s) OVER-MATCH. An unanchored grep on "
              f"these reports documents that do not carry the topic.")
        print("Re-run the search with whole-word boundaries before concluding the "
              "corpus covers it.")
    else:
        print(f"All {len(results)} term(s) clean: no document is reported by a "
              f"substring match alone.")
    print("\nNOTE: this decides SUBSTRING over-matching only. A term matching as a "
          "genuine word\nin a document about a different subject is a SEMANTIC false "
          "positive and is not\nmechanisable -- see the module docstring's "
          "Skyrme-Faddeev case.")
    return 1 if bad else 0


def selftest() -> int:
    """Pin both the detection and its stated limit against this corpus."""
    failures: list[str] = []

    res = scan(["ohara", "knot energy"])

    # 1. The known positive: `ohara` must be caught, and the surnames named.
    r = res["ohara"]
    if not r.over_matching:
        failures.append(
            "'ohara' was NOT flagged over-matching; the detector has been "
            "narrowed past its own worked case")
    enclosing = {w.lower() for w in r.enclosing}
    for surname in ("shinohara", "manoharan", "nohara", "iohara"):
        if surname not in enclosing:
            failures.append(f"enclosing word {surname!r} not reported for 'ohara'")

    # 2. The stated limit: `knot energy` is a SEMANTIC false positive, not a
    #    substring one, so this detector must report it CLEAN. If it ever
    #    starts flagging it, someone has widened the check past what it can
    #    actually decide, and the docstring's honesty claim is broken.
    k = res["knot energy"]
    if k.over_matching:
        failures.append(
            "'knot energy' was flagged over-matching; this detector decides "
            "substring hits only and must not claim the semantic case")

    # 3. Whole-word O'Hara must be absent from the corpus -- the finding this
    #    audit was written to protect. If a knot-energy source is ingested
    #    later this SHOULD fail, and that failure is the signal to re-scope.
    o = scan(["o'hara"])["o'hara"]
    if o.docs_bounded:
        failures.append(
            f"whole-word \"o'hara\" now matches {len(o.docs_bounded)} document(s) "
            f"({sorted(o.docs_bounded)[:5]}); the library no longer lacks a "
            f"knot-energy source -- update bean qou-6xt9 and the taxonomy row")

    if failures:
        print("SELFTEST FAILED")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK")
    print("  - 'ohara' flagged over-matching; Shinohara / Manoharan / Nohara / "
          "Iohara named")
    print("  - 'knot energy' reported clean (semantic FP is out of scope, by design)")
    print("  - whole-word \"O'Hara\": 0 documents (the library holds no "
          "knot-energy source)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--terms", nargs="+", help="search terms to audit")
    ap.add_argument("--show-words", action="store_true",
                    help="list every false-COVERED document id")
    ap.add_argument("--selftest", action="store_true",
                    help="pin the worked case and the stated limit")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.terms:
        ap.error("pass --terms or --selftest")
    return report(scan(args.terms), args.show_words)


if __name__ == "__main__":
    sys.exit(main())
