#!/usr/bin/env python3
"""Which convention does each Markov-parameter definition in `.lean` use?

Bean `qou-cxjq`, fix step 2. Companion to
`scripts/convention-c-producer-audit.py`, which walks `rglob("*.py")` four
times and has no `.lean` path in it at all -- so the Lean surface had never
been counted, and its absence was being read as a zero. See
`docs/audits/2026-08-26-convention-c-in-lean-and-the-markovz-overload.md`
and taxonomy entry #14.

## What it looks for

The Markov parameter `z`, in the three spellings the corpus actually uses:

    D          z = q^3 / (q^2 + 1)                       CANONICAL (owner R1)
    C-plain    z = 1 / (sqrt q + 1/sqrt q)               convention C, visible
    C-sqrtvar  z = u / (u^2 + 1)   with  u^2 = q         convention C, disguised

`C-sqrtvar` is the one a `q`-shaped grep cannot catch: `u/(u^2+1)` shares no
lexeme with `sqrt(q)/(q+1)` and is algebraically identical to it. It is only
convention C once something ties the variable to a square root of `q` -- so
this script does not call a bare `u/(u^2+1)` convention C on shape alone. It
requires corroboration in the same file: a `sqrt`-valued specialisation
(`f (Real.sqrt q)`), or a docstring stating the substitution (`q = s^2`,
`u^2 = q`). Without that, the site is reported `C-shape-unbound` -- a
candidate, not a verdict.

That distinction is the point. Four of the seven known sites write
`Real.sqrt q` in plain sight and were never hidden; only three use the
disguise. "A grep cannot in principle catch this" was too strong -- mostly
nothing had grepped.

## Self-test

`--selftest` fails unless every known site is still detected with its recorded
verdict. Without it a future narrowing of the patterns could report a clean
tree, which is exactly how this surface stayed at zero. A site that is
legitimately migrated should be REMOVED from `KNOWN` in the same commit that
migrates it, so the removal is reviewable.

Usage:
    python3 scripts/lean-markov-convention-audit.py            # report
    python3 scripts/lean-markov-convention-audit.py --selftest # gate
    python3 scripts/lean-markov-convention-audit.py --strict   # exit 1 if any C
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SCAN_ROOT = REPO / "content"

# --- shapes -----------------------------------------------------------------
# Whitespace-tolerant. `\s*` everywhere because Lean formatting varies.
RE_D = re.compile(r"(\w+)\s*\^\s*3\s*/\s*\(\s*\1\s*\^\s*2\s*\+\s*1\s*\)")
_SQ = r"(?:\(?\s*Real\.sqrt\s+\w+\s*\)?|\w*_half)"
# `1/(√q + 1/√q)` and `1/(√q + (√q)⁻¹)`, and the same sum appearing as a
# DENOMINATOR of something else (`… / (√q + 1/√q)`), which is how
# `pairSkeinMass` spells it.
RE_C_PLAIN = re.compile(
    r"/\s*\(\s*" + _SQ + r"\s*\+\s*(?:1\s*/\s*)?" + _SQ + r"\s*(?:⁻¹)?\s*\)"
)
RE_C_SQRTVAR = re.compile(r"(\w+)\s*/\s*\(\s*\1\s*\^\s*2\s*\+\s*1\s*\)")
# corroboration that the free variable really is a square root of q
RE_BINDS_SQRT = re.compile(r"Real\.sqrt|=\s*s\s*\^\s*2|q\s*=\s*s²|u²\s*=\s*q|u\^2\s*=\s*q|q\s*=\s*s\^2|√q")

DEF = re.compile(r"^\s*(?:noncomputable\s+)?(?:def|abbrev)\s+(\w+)")

# Recorded convention-C definition sites, measured 2026-08-26. A site that is
# legitimately migrated should be REMOVED here in the SAME commit that migrates
# it, so the removal is reviewable -- otherwise a narrowing of the patterns can
# report a clean tree, which is exactly how this surface stayed uncounted.
#
# NOT ALL OF THESE ARE DEFECTS. Three are named `_legacy` and carry deprecation
# attributes; several (`zC`, `zCsub`, and the two `MarkovZClassicalCoincidence`
# / `BraidImageEigenphaseExclusion` sites) are DELIBERATE convention-C
# comparison objects, the Lean analogue of the Python audit's declared-C bucket.
# Separating actionable from deliberate is triage this script does not do.
KNOWN_C = [
    ("BorromeanCanonicalTraceDerivation", "zMarkov", "C-sqrtvar"),
    ("BraidGroupNStrand", "markovZN", "C-sqrtvar"),
    ("BraidGroupNStrand", "markovZN_legacy", "C-plain"),
    ("BraidImageEigenphaseExclusion", "zC", "C-sqrtvar"),
    ("ClosedFormInterfaceFactors", "markovZ", "C-sqrtvar"),
    ("EigenphaseCarrierVacuity", "markovZ", "C-plain"),
    ("GramMatrixH3Symbolic", "gramEntry", "C-sqrtvar"),
    ("HoefsmitV21CosSymmetrization", "markovZ", "C-sqrtvar"),
    ("HoefsmitV21CosSymmetrization", "markovZ_legacy", "C-plain"),
    ("JonesNuclearQuotient", "markovZ", "C-plain"),
    ("MarkovAxiomsPrimitive", "markovZax", "C-sqrtvar"),
    ("MarkovAxiomsPrimitive", "markovZax_legacy", "C-plain"),
    ("MarkovZClassicalCoincidence", "zCsub", "C-sqrtvar"),
    ("QBetaCategoricalPrecisionLadder", "markovZ", "C-plain"),
    ("categorical-chain-convergence-mechanisms", "markovZc", "C-plain"),
    ("generator-volume-decomposition", "generatorVolume", "C-plain"),
    ("markov-trace-factorization", "markovZ", "C-plain"),
    ("q-beta-cos-resummation", "markovZ", "C-plain"),
    ("q-beta-spectral-bridge", "markovZ", "C-plain"),
    ("skein-polynomial-transfer-matrix", "tracedVolumeFromMatrix", "C-plain"),
    ("y-lambda-closed-form-wenzl-bridge", "jonesMarkovZ", "C-plain"),
]



def _kind(i: int, def_lines: set) -> str:
    """A `z` inside a definition body DEFINES the convention; a `z` in a
    theorem statement or proof merely MENTIONS it. Counting them together
    inflates the total several-fold and hides which sites are load-bearing."""
    return "def" if any((i - off) in def_lines for off in range(0, 4)) else "stmt"


def classify(path: pathlib.Path):
    """Yield (line_no, decl, verdict, snippet) for each Markov-shaped site."""
    text = path.read_text(errors="replace")
    def_lines = {i for i, l in enumerate(text.split("\n"), 1) if DEF.match(l)}
    file_binds_sqrt = bool(RE_BINDS_SQRT.search(text))
    lines = text.split("\n")
    decl = "?"
    for i, line in enumerate(lines, 1):
        m = DEF.match(line)
        if m:
            decl = m.group(1)
        # a comment line states intent but is not the definition
        stripped = line.strip()
        if stripped.startswith("--") or stripped.startswith("/-"):
            continue
        # KNOWN LIMITATION, deliberately not hacked around. A Lean expression
        # can wrap, and `pairSkeinMass` spells `/(√q + 1/√q)` on the line AFTER
        # its numerator, so a per-line regex misses it. A 3-line joined window
        # catches it and BREAKS decl attribution on four other sites (the
        # window swallows a docstring's `1/(u + u⁻¹)` and reports the
        # definition under the wrong verdict) -- measured, then reverted. Fixing
        # this properly needs an expression parser, not a wider window.
        if RE_D.search(line):
            yield i, decl, "D", _kind(i, def_lines), stripped[:90]
        elif RE_C_PLAIN.search(line):
            yield i, decl, "C-plain", _kind(i, def_lines), stripped[:90]
        elif RE_C_SQRTVAR.search(line):
            v = "C-sqrtvar" if file_binds_sqrt else "C-shape-unbound"
            yield i, decl, v, _kind(i, def_lines), stripped[:90]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    # `content/<paper>/lean/.lake/` holds Mathlib and every other dependency.
    # An unfiltered rglob reports 11206 files and 112 "D" sites, almost all of
    # them somebody else's code -- measuring the harness, not the corpus.
    def tracked():
        for p in sorted(SCAN_ROOT.rglob("*.lean")):
            if ".lake" in p.parts or "lake-packages" in p.parts:
                continue
            yield p

    hits = []
    for p in tracked():
        for ln, decl, verdict, kind, snip in classify(p):
            hits.append((p.relative_to(REPO), ln, decl, verdict, kind, snip))

    counts, defcounts = {}, {}
    for _, _, _, v, k, _ in hits:
        counts[v] = counts.get(v, 0) + 1
        if k == "def":
            defcounts[v] = defcounts.get(v, 0) + 1

    print("LEAN MARKOV-PARAMETER CONVENTION AUDIT")
    print(f"  scanned: {sum(1 for _ in tracked())} .lean files "
          f"under {SCAN_ROOT.relative_to(REPO)}/ (.lake excluded)")
    print(f"  sites:   {len(hits)}")
    print(f"    {'verdict':<18} {'defs':>5} {'all':>5}")
    for v in sorted(counts):
        print(f"    {v:<18} {defcounts.get(v, 0):>5} {counts[v]:>5}")
    print("\n  `defs` are definition bodies -- the sites that DEFINE a")
    print("  convention. `all` also counts theorem statements and proofs that")
    print("  merely mention the shape. Quote `defs`.\n")
    for rel, ln, decl, verdict, kind, snip in hits:
        if kind != "def":
            continue
        flag = "  " if verdict == "D" else "->"
        print(f"{flag} [{verdict:<15}] {rel}:{ln}  ({decl})")
        print(f"       {snip}")

    if args.selftest:
        print("\n--- SELFTEST ---")
        found = {}
        for rel, _, decl, verdict, kind, _ in hits:
            if kind == "def":
                found.setdefault(rel.stem, set()).add((decl, verdict))
        bad = []
        for stem, decl, verdict in KNOWN_C:
            got = found.get(stem, set())
            if (decl, verdict) not in got:
                bad.append(f"  MISSING {stem}: expected ({decl}, {verdict}), got {sorted(got) or 'nothing'}")
        if bad:
            print("SELFTEST FAILED — the scanner no longer sees a site it is known to detect.")
            print("If a site was legitimately migrated, remove it from KNOWN in the")
            print("SAME commit, so the removal is reviewable.")
            print("\n".join(bad))
            return 1
        print(f"SELFTEST PASSED — all {len(KNOWN_C)} recorded convention-C sites still detected.")

    n_c = sum(v for k, v in defcounts.items() if k.startswith("C"))
    if args.strict and n_c:
        print(f"\nSTRICT: {n_c} non-D site(s). Convention D is canonical (owner ruling R1, 2026-08-15).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
