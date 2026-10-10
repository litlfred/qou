#!/usr/bin/env python3
"""Cross-block disagreement on quoted ppb / ppm / % agreement figures.

Several blocks quote an agreement-with-experiment figure for the SAME named
quantity and the numbers disagree, because one block was corrected and the
others were not. That is the shape of the `qou-aymm` alpha_EM cascade, which
was found by luck --- reading a probe --- rather than by construction. This
finds it by construction.

CANDIDATE GENERATOR, NOT A GATE. Grouping is by "the paragraph mentions this
quantity", which is COARSE: a paragraph naming `\\alpha` may be about alpha_s,
a gauge coupling, or an experimental uncertainty. Expect noise. An agent
adjudicates every hit, and READS THE BLOCK FIRST --- see the false positive
below, where editing on this script's say-so would have destroyed a correct
record.

WHAT IT CAUGHT (2026-08-29, bean `qou-aymm`). Run against the tree before the
fix, alpha_EM showed the `-2.1 ppm` figure live in FOUR files and `-468 ppb`
in four others. Three of the four `2.1 ppm` sites had been missed by the
Lean-silence scan, so an incomplete fix shipped and this is what exposed it.
The three figures turned out to be one quantity at three generations, each
correct for its own:

    -2.1 ppm   kappa = 1 (no Gram factor),  muon pin    -> -2.128 ppm
    -399 ppb   kappa = 1.722, order-2,      muon pin    -> -399.53 ppb
    -468 ppb   kappa = 1.722, resummed,     proton pin  -> -467.6 ppb

A KNOWN FALSE POSITIVE, and the reason to read before editing: it flags `399`
in `em-coupling-projection-table1-data.md`. That block is EXEMPLARY --- it
carries -468 ppb and explains the 399 as a deliberately recorded superseded
figure. A disagreement between a live value and a properly-labelled historical
one is not a defect.

WHY v1 REPORTED THE CORPUS CONSISTENT: its regex could not cross `$`
delimiters, so `$-468$ ppb` and `$2.1\;\\mathrm{ppm}$` were invisible --- and
it therefore missed the very cascade it was written to find. Normalising TeX
first is the whole fix. Calibrate any future change against that same
pre-fix commit before trusting a clean result.

Arithmetic is exact (`fractions.Fraction`): the inputs are decimal literals
lifted from documents, so there is no reason to introduce float error into a
comparison whose entire purpose is deciding whether two quoted numbers differ.
"""

from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys
from fractions import Fraction

ROOT = pathlib.Path("folio/quantum-observable-universe")

FIG = re.compile(r"([+-]?\d+(?:\.\d+)?)\s*(ppb|ppm|%)\b")

# What the figure is ABOUT. Coarse by construction -- see the docstring.
QTY = {
    "alpha_EM": r"\\alpha|fine[- ]structure",
    "m_p": r"\bm_\{?\\?(?:mathfrak\{)?p\b|proton mass",
    "m_n": r"\bm_\{?\\?(?:mathfrak\{)?n\b|neutron mass",
    "m_mu": r"m_\\mu|muon mass",
    "Q_beta": r"Q_\{?\\?beta",
    "mK_mpi": r"m_K\s*/\s*m_\\pi",
}

_PPB = {"ppb": Fraction(1), "ppm": Fraction(1000), "%": Fraction(10) ** 7}


def normalise_tex(t: str) -> str:
    """Strip the TeX that hides a figure from a plain regex. v1 omitted this
    and was blind to every math-delimited number in the corpus."""
    t = re.sub(r"\\(?:mathrm|text|mbox)\{(ppb|ppm)\}", r"\1", t)
    t = re.sub(r"\\[;,:!]", " ", t)
    return t.replace("$", " ").replace("\\%", "%")


def to_ppb(value: str, unit: str) -> Fraction:
    """Exact --- these are decimal literals, so Fraction loses nothing."""
    return abs(Fraction(value) * _PPB[unit])


def read(md: pathlib.Path, rev: str | None) -> str:
    if rev is None:
        return md.read_text()
    try:
        return subprocess.run(["git", "show", f"{rev}:{md}"],
                              capture_output=True, text=True,
                              check=True).stdout
    except subprocess.CalledProcessError:
        return ""


def main() -> int:
    rev = sys.argv[1] if len(sys.argv) > 1 else None
    hits = collections.defaultdict(list)

    for md in ROOT.rglob("*.md"):
        raw = read(md, rev)
        for para in re.split(r"\n\n+", raw):
            figs = FIG.findall(normalise_tex(para))
            if not figs:
                continue
            for name, pat in QTY.items():
                if not re.search(pat, para):
                    continue
                for value, unit in figs:
                    hits[name].append((str(md.relative_to(ROOT)), value, unit))

    print(f"scan target: {rev or 'working tree'}")
    print("candidates, not findings -- read the block before editing; a")
    print("properly-labelled superseded figure is not a defect.\n")

    for name, rows in sorted(hits.items()):
        mags = collections.defaultdict(set)
        for f, v, u in rows:
            mags[to_ppb(v, u)].add(f)
        files = len({r[0] for r in rows})
        tag = "CONSISTENT" if len(mags) <= 1 else f"{len(mags)} DISTINCT"
        print(f"{name:10} {tag:14} ({len(rows)} mentions, {files} files)")
        if len(mags) > 1:
            for m in sorted(mags):
                for f in sorted(mags[m]):
                    print(f"           {float(m):>13,.3f} ppb   {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
