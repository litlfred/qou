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


def _sqrtvar_hit(line: str) -> bool:
    """`RE_C_SQRTVAR` with two guards the bare regex lacks (found 2026-09-06).

    `coneCoordRow5 q := coneRow5Numerator q / (q ^ 2 + 1) ^ 2` matched: `(\w+)`
    took the APPLIED ARGUMENT `q` of `coneRow5Numerator q` as the numerator, and
    the trailing `^ 2` on the denominator was ignored.  That is a rational
    function of q over `(q^2+1)^2` -- convention-D territory -- reported as the
    sqrt-variable disguise of C.  So: the numerator identifier must be the whole
    numerator (not preceded, ignoring whitespace, by an identifier character or a
    closing bracket), and the denominator must carry no exponent.
    """
    for m in RE_C_SQRTVAR.finditer(line):
        before = line[:m.start()].rstrip()
        if before and (before[-1].isalnum() or before[-1] in "_)]⟩"):
            continue
        after = line[m.end():].lstrip()
        if after.startswith("^"):
            continue
        return True
    return False
# `√q / (1 + q)` and `√q / (q + 1)` -- convention C written the MOST DIRECT way
# there is, and the one spelling this file was blind to until 2026-08-31.
#
# The blindness is not subtle and that is the point: the module docstring above
# names `sqrt(q)/(q+1)` as the reference form C-sqrtvar is measured against, and
# no pattern matched it. `RE_C_PLAIN` needs a square root in the DENOMINATOR;
# here the denominator is `1 + q` and the root is in the numerator.
# `RE_C_SQRTVAR` needs the same identifier top and bottom (`\1`); here they are
# `Real.sqrt q` and `q`. So each pattern misses it for a different reason, and
# `actionable 0` was reported over a surface that did not include it.
#
# Measured on 2026-08-31: 6 sites, 6 files. Three are deliberate (`zC` twice,
# `markovZC`), one is a numeric separation claim, and TWO are actionable and
# neutrally named -- `markov_parameter := Real.sqrt q / (1 + q)` in
# `QBetaPerBlockChiClosedForms.lean` and its content-block twin
# `qbeta-per-block-chi-closed-forms.lean`. Under the 2026-08-15 ruling that
# convention D is canonical, a bare `markov_parameter` valued at C is the
# `markovZ` overload problem under a different name. Taxonomy entry #23.
RE_C_RATIONAL = re.compile(
    r"Real\.sqrt\s+(\w+)\s*/\s*\(\s*(?:1\s*\+\s*\1|\1\s*\+\s*1)\s*\)")
# corroboration that the free variable really is a square root of q
RE_BINDS_SQRT = re.compile(r"Real\.sqrt|=\s*s\s*\^\s*2|q\s*=\s*s²|u²\s*=\s*q|u\^2\s*=\s*q|q\s*=\s*s\^2|√q")

# `instance` is included deliberately. A typeclass instance sets the
# convention through a FIELD ASSIGNMENT (`z := 1 / (√q + 1/√q)`), not a
# `def` body, so a def-only pattern cannot see it. That blind spot hid
# `markovTraceTower_canonical` -- the CANONICAL Markov trace tower, and the
# single most load-bearing convention site in the tree -- through every run
# of this scanner up to 2026-08-26. Taxonomy entry #15.
DEF = re.compile(r"^\s*(?:noncomputable\s+)?(?:def|abbrev|instance)\s+(\w+)")

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
    ("MarkovConventionSeparation", "markovKernel", "C-sqrtvar"),
    ("BorromeanCanonicalTraceDerivation", "zMarkov", "C-sqrtvar"),
    ("BraidGroupNStrand", "markovZN", "C-sqrtvar"),
    ("BraidGroupNStrand", "markovZN_legacy", "C-plain"),
    ("BraidImageEigenphaseExclusion", "zC", "C-sqrtvar"),
    # Renamed 2026-08-29 (markovZ -> markovZC, cosKernel) so that bare `markovZ`
    # means convention D uniformly. The renaming commits did NOT update this list,
    # so the selftest was red on `main` for two days with three stale names --
    # the very failure mode the comment above warns about, in the guard itself.
    # Corrected 2026-08-31; the sites are unchanged, only their names.
    ("EigenphaseCarrierVacuity", "markovZC", "C-plain"),
    ("GramMatrixH3Symbolic", "gramEntry", "C-sqrtvar"),
    ("HoefsmitV21CosSymmetrization", "cosKernel", "C-sqrtvar"),
    ("HoefsmitV21CosSymmetrization", "markovZ_legacy", "C-plain"),
    ("MarkovAxiomsPrimitive", "markovZax", "C-sqrtvar"),
    ("MarkovAxiomsPrimitive", "markovZax_legacy", "C-plain"),
    ("MarkovZClassicalCoincidence", "zCsub", "C-sqrtvar"),
    ("q-beta-cos-resummation", "markovZC", "C-plain"),
    # Added 2026-08-31 with `RE_C_RATIONAL`. The first two are the actionable
    # pair: a neutrally-named `markov_parameter` valued at convention C, in the
    # library file and in its content-block twin.
    ("QBetaPerBlockChiClosedForms", "markov_parameter", "C-plain"),
    ("qbeta-per-block-chi-closed-forms", "markov_parameter", "C-plain"),
    ("GroundStateOrderingRefutation", "zC", "C-plain"),
    ("MarkovConventionSeparation", "markovZC", "C-plain"),
    ("DecayLadderConventionDPositivity", "zC", "C-plain"),
]



# Deliberateness markers. A convention-C definition is NOT automatically a
# defect: the corpus keeps C objects on purpose for comparison, and keeps
# `_legacy` shims while a migration runs. Mirrors the Python audit's
# declared-C bucket. Evidence is taken from the declaration name and from the
# ~12 lines of docstring/attribute above it, never from shape.
RE_DELIB_NAME = re.compile(
    r"legacy|_?C$|C_?sub|Classical|Coincidence|Exclusion|Historical|_old|Compare|Vs")
# NOTE: bare "legacy" is deliberately NOT a marker. `markovZN`'s docstring says
# "Use this in new code instead of `markovZN_legacy`" -- it names the legacy
# shim in order to steer readers AWAY from it, and a bare-"legacy" marker read
# that as self-deprecation and classified a live convention-C definition as
# `deliberate`. That is an error in the reassuring direction, which is the one
# that matters here. A declaration that is itself legacy carries `@[deprecated]`
# or `_legacy` in its own name, both still matched.
RE_DELIB_DOC = re.compile(
    r"@\[deprecated|convention[- ]C|conventionC|historical|"
    r"for comparison|comparison only|excised|superseded|do not use",
    re.IGNORECASE)


def _deliberate(path_text_lines, i: int, decl: str) -> str:
    """`deliberate` if the site announces itself as C; else `actionable`.

    The evidence window is the declaration's WHOLE preceding docstring, found by
    walking back to its opening `/--`. A fixed line count silently mis-reports:
    `q-beta-cos-resummation` was scoped deliberate with a 20-line docstring
    explaining exactly why it cannot be migrated, and a 13-line window could not
    see the words "Convention C, deliberately" at its top, so the site came back
    `actionable` on the next run. A detector whose verdict depends on how verbose
    the explanation is, is measuring the wrong thing.

    The walk stops at a declaration keyword or a namespace boundary -- NOT at a
    blank line. Blank lines are normal *inside* a docstring, and breaking on one
    was the first version of this fix, which failed on the very file that
    motivated it. `i` is 1-indexed, so the declaration itself is at index i-1 and
    the search starts at i-2.
    """
    if RE_DELIB_NAME.search(decl):
        return "deliberate"
    STOP = re.compile(r"^\s*(noncomputable\s+)?(def|abbrev|theorem|lemma|instance|"
                      r"structure|class|end|namespace|section)\b")
    start = None
    for j in range(i - 2, max(-1, i - 250), -1):
        line = path_text_lines[j]
        if "/--" in line:
            start = j
            break
        if STOP.match(line):
            break
    lo = start if start is not None else max(0, i - 13)
    above = " ".join(path_text_lines[lo:i - 1])
    if RE_DELIB_DOC.search(above):
        return "deliberate"
    return "actionable"


def _kind(i: int, def_lines: set) -> str:
    """A `z` inside a definition body DEFINES the convention; a `z` in a
    theorem statement or proof merely MENTIONS it. Counting them together
    inflates the total several-fold and hides which sites are load-bearing."""
    return "def" if any((i - off) in def_lines for off in range(0, 4)) else "stmt"


def classify(path: pathlib.Path):
    """Yield (line_no, decl, verdict, snippet) for each Markov-shaped site."""
    text = path.read_text(errors="replace")
    def_lines = {i for i, l in enumerate(text.split("\n"), 1) if DEF.match(l)}
    all_lines = text.split("\n")
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
            yield i, decl, "D", _kind(i, def_lines), _deliberate(all_lines, i, decl), stripped[:90]
        elif RE_C_PLAIN.search(line) or RE_C_RATIONAL.search(line):
            yield i, decl, "C-plain", _kind(i, def_lines), _deliberate(all_lines, i, decl), stripped[:90]
        elif _sqrtvar_hit(line):
            v = "C-sqrtvar" if file_binds_sqrt else "C-shape-unbound"
            yield i, decl, v, _kind(i, def_lines), _deliberate(all_lines, i, decl), stripped[:90]


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
        for ln, decl, verdict, kind, delib, snip in classify(p):
            hits.append((p.relative_to(REPO), ln, decl, verdict, kind, delib, snip))

    counts, defcounts = {}, {}
    for _, _, _, v, k, _, _ in hits:
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
    tri = {}
    for _, _, _, v, k, d, _ in hits:
        if k == "def" and v.startswith("C"):
            tri[d] = tri.get(d, 0) + 1
    print(f"  convention-C definitions: {sum(tri.values())}  "
          f"-> actionable {tri.get('actionable', 0)}, "
          f"deliberate {tri.get('deliberate', 0)}")
    print("  `deliberate` = the site announces itself (a `_legacy`/`C`-ish name,")
    print("  a @[deprecated], or a docstring saying comparison/historical).")
    print("  It is evidence of INTENT, not a clean bill -- a deliberate C object")
    print("  can still be cited as though it were D.\n")
    for rel, ln, decl, verdict, kind, delib, snip in hits:
        if kind != "def":
            continue
        flag = "  " if verdict == "D" else ("->" if delib == "actionable" else " ~")
        tag = verdict if verdict == "D" else f"{verdict}/{delib}"
        print(f"{flag} [{tag:<26}] {rel}:{ln}  ({decl})")
        print(f"       {snip}")

    if args.selftest:
        print("\n--- SELFTEST ---")
        found = {}
        for rel, _, decl, verdict, kind, _, _ in hits:
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
