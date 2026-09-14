#!/usr/bin/env python3
# polynomial_q_not_applicable: a text classifier over the corpus; no numeric output.
"""How many senses of "one-dimensional" does the corpus use, and where?

Bean `qou-st2v`. The corpus uses "one-dimensional" / "1D" for at least THREE
unrelated things, and a reader cannot tell them apart from the word:

  SPATIAL   the spatial dimension of a base manifold or a nucleon layout
            (`dim M_k = 1`, the linear layout, the filament)
  REP       a Wedderburn block / irrep / character of dimension one
            (a one-row or one-column Young diagram) -- the majority
  LINALG    a plain vector-space dimension: a solution space, a cohomology
            group, a module of forms ("HH^2 = k is one-dimensional")
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
LINALG = re.compile(r"solution space|derivation space|cohomolog|\bHH\^|\bker\b|"
                    r"vector space|eigenspace|\bsubspace\b|\bLambda\^|\bOmega\^", re.I)

# A use is QUALIFIED when a disambiguating noun follows the phrase directly.
# That is the split that matters: a qualified use is not ambiguous to anyone.
QUALIFIED = re.compile(r"(one[- ]dimensional|1[- ]dimensional)\s+"
                       r"(block|blocks|channel|channels|representation|representations|"
                       r"character|characters|irrep|irreps|rep|reps|wedderburn|radical|"
                       r"summand|module|modules|space|spaces|subspace|kernel|"
                       r"solution|state|states|stratum|sign|trivial|alternating|symmetric)",
                       re.I)
BARE = re.compile(r"(one[- ]dimensional|1[- ]dimensional)(?!\s*[A-Za-z\\$])", re.I)


def classify(ctx):
    r, s, c = bool(REP.search(ctx)), bool(SPATIAL.search(ctx)), bool(CHANNEL.search(ctx))
    l = bool(LINALG.search(ctx))
    if c and not s:
        return "CHANNEL"
    if l and not s:
        return "LINALG"
    if r and not s:
        return "REP"
    if s and not r:
        return "SPATIAL"
    if s and r:
        return "AMBIGUOUS(both)"
    return "NO-MARKER"


def scan(globs):
    hits = []
    for g in globs:
        for p in ROOT.glob(g):
            if ".lake" in p.parts or "node_modules" in p.parts:
                continue
            # The auditor does not count itself.  It lives under
            # computations/**/*.py and names the phrase many times, so without
            # this every edit to this file moved the corpus total it reports
            # (measured: 791 -> 793 when the cross-tab block was added).
            if p.resolve() == Path(__file__).resolve():
                continue
            try:
                lines = p.read_text(errors="replace").split("\n")
            except (OSError, UnicodeError):
                continue
            for i, ln in enumerate(lines):
                if TERM.search(ln):
                    ctx = "\n".join(lines[max(0, i - 2):i + 3])
                    hits.append((classify(ctx), str(p.relative_to(ROOT)), i + 1,
                                 ln.strip()[:100], ln))
    return hits


# --- SPATIAL x bare: the number the SCOPE note used to ASSERT ---------------
# Added 2026-09-14. The note below claimed "the genuinely SPATIAL bare uses
# number about four" while the script computed only the sense buckets, so the
# one figure the skip-the-sweep decision rested on could not be checked from
# the artifact.  A hand cross-tab gave 15 raw, of which 4 are this audit's own
# output and 6 are classifier false positives -- so "about four" was RIGHT.
# It is computed here instead of asserted, with the exclusions named.

# Sites that are ABOUT the phrase rather than uses of it: the disambiguation
# section this audit produced, its own tag rename, and dated audit docs (left
# alone per the qou-3nva / qou-m4au drain precedent).
# Two separate tests, because they key on different things and conflating them
# silently mislabels rows.  The PATH test catches files that are ABOUT the
# phrase; the LINE test catches the tag rename this audit itself introduced.
# NOTE the audit's own path is excluded: it lives under computations/**/*.py
# and so scans itself -- adding this very comment block moved the corpus total
# 791 -> 793 before the exclusion was added.
SELF_REFERENTIAL_PATH = re.compile(
    r"notation/notation-collisions\.md|"
    r"computations/audits/one_dimensional_sense_audit\.py|"
    r"docs/audits/\d{4}-\d{2}-\d{2}-")
SELF_REFERENTIAL_LINE = re.compile(r"spatially-one-dimensional")


def qual_kind(raw_line):
    """qualified / bare / other -- a SAME-LINE question, so use the full line."""
    if QUALIFIED.search(raw_line):
        return "qualified"
    return "bare" if BARE.search(raw_line) else "other"


def cross_tab(hits):
    """sense x {qualified,bare,other}, plus the triaged SPATIAL-bare list."""
    tab, spatial_bare = Counter(), []
    for sense, path, n, disp, raw in hits:
        tab[(sense, qual_kind(raw))] += 1
        if sense == "SPATIAL" and qual_kind(raw) == "bare":
            selfref = bool(SELF_REFERENTIAL_PATH.search(path)
                           or SELF_REFERENTIAL_LINE.search(raw))
            spatial_bare.append((path, n, disp, selfref))
    return tab, spatial_bare


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
    all_hits = []
    for label, globs in surfaces.items():
        hits = scan(globs)
        c = Counter(h[0] for h in hits)
        grand += c
        tot = sum(c.values())
        print(f"  {label:18} {tot:>5} hits   " +
              "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
        unclassified += [h for h in hits if h[0] in ("NO-MARKER", "AMBIGUOUS(both)")]
        all_hits += hits

    tot = sum(grand.values())
    print(f"\n  {'TOTAL':18} {tot:>5} hits")
    for k, v in sorted(grand.items(), key=lambda kv: -kv[1]):
        print(f"      {k:18} {v:>5}  ({100.0 * v / tot:.1f}%)")

    print(f"\n  Hits the classifier has no marker for: {len(unclassified)}")
    print("  !! NOT the same as 'a reader cannot disambiguate them'. Three separate")
    print("     samples of this bucket were plainly clear linear-algebraic and")
    print("     representation uses. Do NOT quote it as an ambiguity count.")
    for k, p, n, ln, _raw in unclassified[:15]:
        print(f"    [{k:16}] {p}:{n}")
        print(f"        {ln}")
    if len(unclassified) > 15:
        print(f"    ... and {len(unclassified) - 15} more")

    # --- the qualified/bare split, and the figure the note used to assert ---
    tab, spatial_bare = cross_tab(all_hits)
    senses = sorted({k for k, _ in tab})
    print("\n  SENSE x QUALIFIED/BARE — the split that actually matters")
    print(f"    {'sense':<18}{'qualified':>10}{'bare':>7}{'other':>7}{'TOTAL':>7}")
    for k in senses:
        q, b, o = tab[(k, "qualified")], tab[(k, "bare")], tab[(k, "other")]
        print(f"    {k:<18}{q:>10}{b:>7}{o:>7}{q + b + o:>7}")
    tq = sum(v for (k, j), v in tab.items() if j == "qualified")
    tb = sum(v for (k, j), v in tab.items() if j == "bare")
    to = sum(v for (k, j), v in tab.items() if j == "other")
    print(f"    {'TOTAL':<18}{tq:>10}{tb:>7}{to:>7}{tq + tb + to:>7}")

    raw = len(spatial_bare)
    live = [h for h in spatial_bare if not h[3]]
    print(f"\n  SPATIAL and bare: {raw} raw, {len(live)} after removing this")
    print("  audit's own output and dated audit docs. THIS is the figure the")
    print("  skip-the-sweep decision rests on, and it is now computed, not asserted.")
    for path, n, disp, selfref in spatial_bare:
        print(f"    [{'self' if selfref else 'LIVE':4}] {path}:{n}")
        print(f"        {disp}")
    print("  Of the LIVE rows, some are still classifier false positives -- the")
    print("  SPATIAL regex fires on context words (\\bbase\\b, descent, chain), so a")
    print("  linear-algebraic 'Omega^3 is one-dimensional' can land here. Read them")
    print("  before quoting the count as a defect count.")

    print("""
SCOPE -- read this before quoting any number above
  The number that MATTERS is the qualified/bare split, not the sense buckets. A
  use with a disambiguating noun after it ("one-dimensional Wedderburn block")
  is not ambiguous to anyone, and those are the large majority. Of the bare
  uses, most are still clear from their own sentence; the genuinely SPATIAL
  bare uses are FEW -- the SPATIAL-and-bare block above computes how many,
  rather than asserting it as this note used to ("about four", uncomputed).
  The sense classifier is a high-recall heuristic and its "NO-MARKER" bucket
  means the REGEX had no marker -- it is not an ambiguity count, and reading it
  as one overstates the problem by an order of magnitude. That mistake was made
  three times in this corpus before being caught; the bucket is named
  NO-MARKER rather than UNCLASSIFIED for exactly that reason.
  No file is modified. The authoring rule lives in
  content/quantum-observable-universe/notation/notation-collisions.md.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
