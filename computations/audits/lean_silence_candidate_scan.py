#!/usr/bin/env python3
"""Candidate scan: prose DERIVES a value the governing Lean never mentions.

Not a contradiction --- `da-lean-narrative-divergence` already catches those,
by comparing what the two say. This is a SILENCE: the Lean proves a structural
fact and stops, while the `.md` infers a number from it. There is no
contradiction to find, only an absence, which is why a text-level comparison
structurally cannot see it.

Worked case (bean `qou-a468`): `down-quark.lean` proves
`quark_crossing_asymmetry` --- the two quark orientations differ by a sign ---
and says nothing whatever about charge. The `.md` sibling then wrote "This
gives the down quark a Coulomb charge contribution of -1/3". Both blocks are
swept on the full `da-*` battery including `da-lean-narrative-divergence`, and
none of it fired.

CANDIDATE GENERATOR, NOT A GATE. An agent adjudicates every hit.

MEASURED, 2026-08-29, on `content/quantum-observable-universe`, BEFORE the
`qou-aymm` fix landed:

  blocks with a governing Lean (>= 15 lines)        2458
  candidates                                           3
  true positives                                       1  (the alpha_EM block)
  false positives                                      2

A run on the CURRENT tree returns 2, not 3: the true positive was fixed by
that bean, so only the two false positives remain. That is the expected
steady state and not a discrepancy with the figures above.

Both false positives are honest NEGATIVE results, and they share a shape worth
knowing: "yields +0.145 m_e, MISSING the target -4.35 m_e" and "yields ONLY a
4-dimensional quadruplet, NOT a decuplet". The derive-verb fires, but the
sentence is reporting a failure. A future tightening should look for a
negating word in the same clause.

RECALL is verified on n=2 only --- the two known positives from `qou-a468`,
both of which this predicate catches. That is a floor, not a measurement.

KNOWN LIMITS, so the numbers above are not over-read:

  - The predicate needs all three signals (derive-verb, numeric literal,
    quantity noun) in ONE sentence. A claim split across two sentences is
    invisible. So 3 is a LOWER BOUND, not a census.
  - v1 of this scan required a SIBLING `.lean` and would have missed one of
    its own two known positives: `up-quark-properties` is a remark carrying
    `interprets: "def:up-quark"` with no sibling of its own. Resolving Lean
    through `interprets`/`uses` took coverage 890 -> 2458 blocks. Calibrate
    any future narrowing against both known positives before trusting it.
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys

ROOT = pathlib.Path("content/quantum-observable-universe")

# The prose presents the number as a CONSEQUENCE, not as an aside.
DERIVE = re.compile(
    r"\b(this gives|gives|yields|therefore|hence|thus|so the|implies|"
    r"we obtain|it follows|resulting in|leads to)\b", re.I)

# A value-bearing literal: a fraction, or a decimal with >= 2 significant
# figures. A bare integer is far too common in prose to carry signal.
LITERAL = re.compile(r"(?<![\w.])([+-]?\d+\s*/\s*\d+|[+-]?\d+\.\d{2,})(?![\w])")

# Head-nouns whose absence from the governing Lean is meaningful.
NOUNS = ["charge", "mass", "energy", "width", "ratio", "radius", "moment",
         "coupling", "constant", "lifetime", "spin", "volume", "density"]

MIN_LEAN_LINES = 15   # below this, the Lean is a stub and proves nothing


def _label_index() -> dict[str, pathlib.Path]:
    out = {}
    for ts in ROOT.rglob("*.ts"):
        m = re.search(r'label:\s*"([^"]+)"', ts.read_text())
        if m:
            out[m.group(1)] = ts
    return out


def _refs(ts_path: pathlib.Path) -> list[str]:
    t = ts_path.read_text()
    out = []
    m = re.search(r'interprets:\s*"([^"]+)"', t)
    if m:
        out.append(m.group(1))
    u = re.search(r"uses:\s*\[(.*?)\]", t, re.S)
    if u:
        out += re.findall(r'"([^"]+)"', u.group(1))
    return out


def governing_lean(ts_path: pathlib.Path, by_label) -> str:
    """Every Lean this block is answerable to: its own sibling, plus the
    siblings of the blocks it interprets or uses."""
    parts = []
    own = ts_path.with_suffix(".lean")
    if own.exists():
        parts.append(own.read_text())
    for r in _refs(ts_path):
        tgt = by_label.get(r)
        if tgt is None:
            continue
        tl = tgt.with_suffix(".lean")
        if tl.exists():
            parts.append(tl.read_text())
    return "\n".join(parts)


def main() -> int:
    by_label = _label_index()
    rows, covered = [], 0

    for ts in ROOT.rglob("*.ts"):
        md = ts.with_suffix(".md")
        if not md.exists():
            continue
        lean = governing_lean(ts, by_label)
        if len(lean.splitlines()) < MIN_LEAN_LINES:
            continue
        covered += 1
        for sent in re.split(r"(?<=[.!?])\s+|\n\n", md.read_text()):
            if not DERIVE.search(sent):
                continue
            lits = LITERAL.findall(sent)
            nouns = [n for n in NOUNS if re.search(rf"\b{n}\b", sent, re.I)]
            if not (lits and nouns):
                continue
            # SILENCE: neither the value nor the quantity is in the Lean.
            if [l for l in lits
                    if re.search(re.escape(l.replace(" ", "")),
                                 lean.replace(" ", ""))]:
                continue
            if [n for n in nouns if re.search(n, lean, re.I)]:
                continue
            rows.append((str(md.relative_to(ROOT)), nouns, lits,
                         re.sub(r"\s+", " ", sent.strip())[:180]))

    print(f"blocks with a governing Lean (>= {MIN_LEAN_LINES} lines): {covered}")
    print(f"CANDIDATES (prose derives a value its Lean never mentions): "
          f"{len(rows)}")
    print("  -- candidates, not findings: an agent adjudicates each one.")
    print("  -- the two known false-positive shapes are honest NEGATIVE")
    print("     results ('yields X, MISSING the target Y').")
    print()
    for f, n in collections.Counter(r[0] for r in rows).most_common():
        print(f"  {n}x  {f}")
    print()
    for f, nouns, lits, s in rows:
        print(f"--- {f}\n    nouns={nouns} lits={lits}\n    {s}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
