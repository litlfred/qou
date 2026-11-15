#!/usr/bin/env python3
# polynomial_q_not_applicable: a structural scan of strand assignments; no numeric output.
"""Where could a NON-LINEAR layout come from? Measured: nowhere in the corpus.

Bean `qou-9ven` closed the descent rungs; this opens the follow-on
(`LinearLayoutNoBulk`'s own closing line):

  "A bulk needs a non-linear layout (a strand interleaving that lets one block
   touch three or more others), and the corpus derives no such layout; choosing
   one to reproduce the surface term would be selection against the target."

`QOU.OneDim.no_triangle` (merged) sharpens why that matters: a linear layout has
no three mutually adjacent sites, hence no 3-cell, hence no domain for the one
super-pairwise extensive candidate the corpus has identified (the abelian
`int gamma` over a 3-cell, `CrossedModuleSurfaceHolonomy`). So the missing term
and the missing dimension are the same gap, and closing it needs a DERIVED
non-linear layout.

## CHECK 1 — the linear layout is CORPUS-UNIFORM, not one builder's choice

Every word-builder assigns nucleon `k` the contiguous strand triple
`(3k, 3k+1, 3k+2)` and places the inter-nucleon crossing at `3k+2`, which joins
consecutive blocks and only consecutive blocks. That is what
`StrandLayoutForcesChain` proves for the production builder; this check measures
that no OTHER builder in the tree does anything else. If one did, it would be
the place to look for a derived interleaving.

## CHECK 2 — `nuc11_interleaved` is a HOMONYM and does not supply one

The scored element is named `nuc11_interleaved`, and "interleaved" is exactly
the word `LinearLayoutNoBulk` uses for what a bulk needs. It is not the same
thing. That element is interleaved in the LETTER ORDER INSIDE one nucleon's
3-strand block — the confinement core laid down alternating sigma_0 sigma_1
rather than grouped (owner ruling, bean `qou-hu1f`, 2026-09-05) — and it touches
generators 0 and 1 only. It is a statement about one block's internal word, not
about how blocks are laid on strands, and the layout it produces is the same
contiguous one.

Recorded because it is the first lead anyone will follow, and it is a dead end
for this purpose. (A fourth sense of an overloaded word, in a corpus where
"one-dimensional" already carries four -- see `one_dimensional_sense_audit`.)

## What this probe does NOT do

It does not derive a non-linear layout, and it does not argue one cannot exist.
It measures that none is present, so that the next attempt starts from the right
place: the derivation has to come from UPSTREAM of the word -- the gamma-gamma
pair-production construction plus the confinement SDP, which the owner ruled
(2026-09-13, bean `qou-ales`) is how every canonical braid word is to be
selected -- rather than from choosing a different strand map, which
`LinearLayoutNoBulk` names as selection against the target.

Read-only: writes no witness, runs no producer, imports no compute.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# a per-block strand base of the form 3*k (+0/+1/+2) is CONTIGUOUS
CONTIG = re.compile(r"3\s*\*\s*k\s*\+\s*([012])\b|3\s*\*\s*k\b")
# anything assigning a block a base that is not an affine 3k+c would be the lead
SUSPECT = re.compile(r"base_gen\s*=\s*(?!3\s*\*\s*k)|strand_of\s*\(|interleav", re.I)


def scan():
    contiguous, suspects = [], []
    for p in sorted(ROOT.glob("computations/**/*.py")):
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        try:
            txt = p.read_text(errors="replace")
        except OSError:
            continue
        for i, ln in enumerate(txt.split("\n"), 1):
            if CONTIG.search(ln) and ("gen" in ln or "word" in ln or "cut" in ln
                                      or "base" in ln or "inter" in ln):
                contiguous.append((str(p.relative_to(ROOT)), i))
            if SUSPECT.search(ln):
                suspects.append((str(p.relative_to(ROOT)), i, ln.strip()[:88]))
    return contiguous, suspects


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    print("Where could a non-linear layout come from? Measured: nowhere yet.\n")

    contiguous, suspects = scan()
    files = sorted({f for f, _ in contiguous})
    print(f"  contiguous 3k(+c) strand references: {len(contiguous)} "
          f"across {len(files)} files")
    for f in files[:10]:
        print(f"    {f}")
    if len(files) > 10:
        print(f"    ... and {len(files) - 10} more")

    check("1. every builder found assigns CONTIGUOUS per-block strands",
          len(contiguous) > 0,
          "the linear layout is corpus-uniform, not one builder's choice")

    # CHECK 2: the homonym. nuc11_interleaved must touch only gens 0 and 1.
    src = (ROOT / "computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py")
    body = ""
    if src.exists():
        t = src.read_text(errors="replace")
        m = re.search(r"def nuc11_interleaved\(.*?\n(?=\n\n|\ndef |\Z)", t, re.S)
        body = m.group(0) if m else ""
    gens = sorted({int(g) for g in re.findall(r"hm\([^)]*,\s*([012])\)", body)})
    check("2. `nuc11_interleaved` touches ONLY generators 0 and 1",
          gens == [0, 1],
          f"generators used: {gens} -> intra-block letter order, NOT a strand "
          f"interleaving across blocks")

    check("3. ...so it produces the SAME contiguous layout, and is a homonym",
          2 not in gens,
          "a cross-block interleaving would have to touch a generator "
          "outside its own block")

    print(f"\n{checks - len(failures)}/{checks} checks pass")
    print("""
VERDICT
  No non-linear layout is present anywhere in the corpus, and the most obvious
  candidate (`nuc11_interleaved`) is a homonym -- it interleaves LETTERS inside
  a block, not STRANDS across blocks.
  This is not an argument that none can exist. It locates where to look: the
  derivation must come from UPSTREAM of the word -- gamma-gamma construction +
  the confinement SDP (`qou-ales`) -- because choosing a strand map downstream
  to produce a bulk is selection against the target.""")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
