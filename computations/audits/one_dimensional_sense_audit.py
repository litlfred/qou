#!/usr/bin/env python3
# polynomial_q_not_applicable: a text classifier over the corpus; no numeric output.
"""How many senses of "one-dimensional" does the corpus use, and where?

Bean `qou-st2v`. The corpus uses "one-dimensional" / "1D" for at least THREE
unrelated things, and a reader cannot tell them apart from the word:

  SPATIAL   the spatial dimension of a base manifold or a nucleon layout
            (`dim M_k = 1`, the linear layout, the filament)
  REP       a Wedderburn block / irrep / character of dimension one
            (a one-row or one-column Young diagram) -- believed the majority
  CHANNEL   a seminormal CHANNEL of dimension one (`AlphaShiftOneDimChannel`)

This script MEASURES the split. It changes nothing: per AGENTS.md's 2026-09-07
directive a rename sweep needs the owner, but measuring is exempt, and the
owner needs the blast radius before deciding.

The classifier is a HEURISTIC over a +/-2 line window, in the spirit of the
vacuity-audit's high-recall candidates: the per-hit verdict is an agent call,
not this script's. Its value is the ORDER OF MAGNITUDE of each bucket and the
UNCLASSIFIED list -- the hits no marker reaches, which are exactly the ones a
reader also cannot disambiguate.

Read-only: writes no witness, touches no file.
"""
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERM = re.compile(r"one[- ]dimensional|1[- ]?dimensional|\bone-dim\b|\bOneDim\b", re.I)

REP = re.compile(r"wedderburn|irrep|\birreducible\b|character|young|partition|"
                 r"tableau|\bblock\b|fibre|fiber|\bV_|dim_q|representation|"
                 r"\[2\]_q|quantum dimension|row|column", re.I)
SPATIAL = re.compile(r"\bdim M|manifold|\bbase\b|spatial|space-?like|filament|"
                     r"\blayout\b|\bchain\b|\blattice\b|\balong a line\b|"
                     r"\bcoordination\b|\bnucleon\b|\bsite\b|brane|descent", re.I)
CHANNEL = re.compile(r"seminormal|alpha_?shift|alphashift|scalar channel", re.I)


def classify(ctx):
    r, s, c = bool(REP.search(ctx)), bool(SPATIAL.search(ctx)), bool(CHANNEL.search(ctx))
    if c and not s:
        return "CHANNEL"
    if r and not s:
        return "REP"
    if s and not r:
        return "SPATIAL"
    if s and r:
        return "AMBIGUOUS(both)"
    return "UNCLASSIFIED"


def scan(globs):
    hits = []
    for g in globs:
        for p in ROOT.glob(g):
            if ".lake" in p.parts or "node_modules" in p.parts:
                continue
            try:
                lines = p.read_text(errors="replace").split("\n")
            except (OSError, UnicodeError):
                continue
            for i, ln in enumerate(lines):
                if TERM.search(ln):
                    ctx = "\n".join(lines[max(0, i - 2):i + 3])
                    hits.append((classify(ctx), str(p.relative_to(ROOT)), i + 1,
                                 ln.strip()[:100]))
    return hits


def main():
    surfaces = {
        "content/ (.md)": ["content/**/*.md"],
        "content/ (.ts)": ["content/**/*.ts"],
        "lean (.lean)": ["content/**/*.lean"],
        "computations/": ["computations/**/*.py"],
        "docs/": ["docs/**/*.md"],
    }
    grand = Counter()
    print('Senses of "one-dimensional" in the corpus — MEASURED, not swept\n')
    unclassified = []
    for label, globs in surfaces.items():
        hits = scan(globs)
        c = Counter(h[0] for h in hits)
        grand += c
        tot = sum(c.values())
        print(f"  {label:18} {tot:>5} hits   " +
              "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
        unclassified += [h for h in hits if h[0] in ("UNCLASSIFIED", "AMBIGUOUS(both)")]

    tot = sum(grand.values())
    print(f"\n  {'TOTAL':18} {tot:>5} hits")
    for k, v in sorted(grand.items(), key=lambda kv: -kv[1]):
        print(f"      {k:18} {v:>5}  ({100.0 * v / tot:.1f}%)")

    print(f"\n  Hits no marker disambiguates: {len(unclassified)}")
    print("  (these are exactly the ones a READER also cannot disambiguate)")
    for k, p, n, ln in unclassified[:15]:
        print(f"    [{k:16}] {p}:{n}")
        print(f"        {ln}")
    if len(unclassified) > 15:
        print(f"    ... and {len(unclassified) - 15} more")

    print("""
SCOPE
  Heuristic classifier, high recall by design; the per-hit verdict is an agent
  call. Quote the bucket ORDERS OF MAGNITUDE and the UNCLASSIFIED count, not
  the individual numbers as though they were adjudicated.
  No file is modified. A rename sweep is an owner decision (AGENTS.md
  2026-09-07); this supplies the blast radius for it.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
