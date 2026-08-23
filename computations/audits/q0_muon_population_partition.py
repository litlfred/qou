#!/usr/bin/env python3
"""Partition the muon-valued q₀ population in computations/.

Why this exists
---------------
`qou-1c4y` has twice carried a headline count of "muon witnesses" that was
produced by grepping a *prefix* of the muon pin.  A 12-digit prefix does not
identify the muon pin: the corpus carries **two** muon values that agree to
11 digits and diverge at the 12th —

    current     1.10997859555733471989...   (live ideal / CAL-2 pin)
    superseded  1.10997859555418057528...   (the "old muon value")

so a prefix grep silently sums two populations with different defects and
different fixes.  This script keeps the split honest and re-runnable.

It is pure string/JSON inspection — no arithmetic — so the NO-FLOAT64
discipline is satisfied vacuously.

Usage
-----
    python3 computations/audits/q0_muon_population_partition.py
    python3 computations/audits/q0_muon_population_partition.py --list-contradictions
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter

COMP = pathlib.Path(__file__).resolve().parent.parent

# The two muon values, to enough digits to separate them (they share 11).
MUON_CURRENT = "1.109978595557334"
MUON_OLD = "1.109978595554180"
# Loose prefix: matches BOTH, and nothing proton (proton is 1.10997858275...).
MUON_LOOSE = "1.1099785955"

PIN_WITNESS = "q-pinning-50-digit"
ROUTES_ANCHOR = re.compile(
    r"(import\s+q_parameter|from\s+q_parameter"
    r"|qou_substrate.*constants|\bq_at\(|Q_50_DIGIT_STR)"
)
READS_JSON = re.compile(r"(json\.load|read_text|open\()")


def witness_populations() -> dict:
    """Split every witness carrying a muon-family value by WHICH muon value."""
    tally = Counter()
    stamp_by_value = Counter()
    for path in sorted(COMP.rglob("*.witness.json")):
        text = path.read_text(errors="replace")
        if MUON_LOOSE not in text:
            continue
        cur, old = MUON_CURRENT in text, MUON_OLD in text
        kind = "both" if (cur and old) else ("current" if cur else ("old" if old else "rounded"))
        tally[kind] += 1
        try:
            anchor = json.loads(text).get("q0Anchor")
        except Exception:
            anchor = None
        stamp_by_value[(anchor, kind)] += 1
    return {"tally": tally, "stamp_by_value": stamp_by_value}


# One-hop transitive path through `_li_2_q_util.load_q_50dps`.
#
# HISTORY, because the right pattern here changed once already.  Until
# 2026-08-22 that helper's signature was `load_q_50dps(path=None)` and a
# `None` path defaulted to the MUON-anchored pin witness -- so the BARE
# no-arg call was the muon route, and a scan that only looked for the
# witness filename inside each producer missed it, undercounting the
# contradictions by 9.
#
# The helper now takes `anchor="proton"` and the bare call resolves to the
# experimental pin.  So the bare form is CORRECT and must NOT be flagged;
# the muon route is now an explicit `anchor="muon"` or an explicit path to
# the pin witness.  A detector keyed on the old shape would report every
# fixed caller as a defect.
_MUON_ANCHOR_ARG = re.compile(
    r"(?<![\w.])load_q_50dps\s*\([^)]*anchor\s*=\s*[\"']muon[\"']"
)
_LOAD_WITH_PIN_PATH = re.compile(
    r"(?<![\w.])load_q_50dps\s*\(\s*[A-Za-z_][\w.]*\s*[,)]"
)


def _uses_muon_via_helper(text: str) -> bool:
    """True if the producer asks `load_q_50dps` for the ideal/muon pin.

    Comment and docstring lines are excluded: a `# Was: load_q_50dps()`
    marker left by an earlier fix records the trap, it is not an instance.
    """
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or '"""' in stripped:
            continue
        if _MUON_ANCHOR_ARG.search(line):
            return True
    return False


def direct_pinners() -> list[tuple[str, str]]:
    """Producers that bind q₀ straight out of the muon-anchored pin witness.

    A producer here never imports the anchor-resolving module, so it inherits
    whatever anchor that witness carries rather than choosing one.  Returns
    (relative path, manifest bucket).
    """
    manifest = json.loads((COMP / "q0_anchor_manifest.json").read_text())
    bucket = {
        stem: name
        for name in ("ideal_muon", "physical_proton", "ambiguous")
        for stem in manifest.get(name, [])
    }
    out = []
    for path in sorted(COMP.rglob("*.py")):
        if "_deprecated" in path.parts:
            continue
        text = path.read_text(errors="replace")
        direct = (
            PIN_WITNESS in text
            and READS_JSON.search(text)
            and re.search(r'derived_50_digit"\]', text)
            and re.search(r'\[\s*"q"\s*\]', text)
        )
        via_helper = _uses_muon_via_helper(text)
        if not (direct or via_helper):
            continue
        if ROUTES_ANCHOR.search(text):
            continue  # resolves its anchor properly
        rel = str(path.relative_to(COMP))
        out.append((rel, bucket.get(path.stem, "UNDECLARED"), classify_intent(text),
                    co_read_fields(text)))
    return out


# Intent signals, searched in COMMENTS AND DOCSTRINGS only.
#
# The CAL-2 trap: a comment saying "CAL-2 q_0" names WHICH CALIBRATION, not
# which pin to evaluate at.  AGENTS.md is explicit that the 2026-08-07
# directive "is about which numerical evaluation code defaults to, not about
# redefining the 3-CAL triple".  Reading a CAL-2 mention as ideal-layer intent
# is the exact conflation the directive prevents -- it was made and retracted
# on this branch, and applying the correction as a rule reclassified 3 of 5
# producers.  So CAL-2 / CAL-1 mentions are deliberately NOT muon signals here.
_PROTON_INTENT = re.compile(
    r"proton[- ]pin|proton anchor|physical[- ]observation|experimental (pin|anchor)", re.I)
_MUON_INTENT = re.compile(
    r"muon[- ]pin|muon anchor|ideal (pin|anchor|layer)", re.I)


def _prose(text: str) -> str:
    """Comments and docstrings only -- intent is stated, not computed."""
    comments = "\n".join(l for l in text.splitlines() if l.strip().startswith("#"))
    docstrings = "\n".join(re.findall(r'"""(.*?)"""', text, re.S))
    return comments + "\n" + docstrings


def classify_intent(text: str) -> str:
    """Which layer does this producer SAY it wants?  Most say nothing."""
    blob = _prose(text)
    proton, muon = bool(_PROTON_INTENT.search(blob)), bool(_MUON_INTENT.search(blob))
    if proton and muon:
        return "both (comparison?)"
    if proton:
        return "proton-intent"
    if muon:
        return "muon-pin intent"
    return "silent on the pin"


# Fields of the pin witness OTHER than the q₀ bind itself.  A producer that
# reads one of these too cannot be migrated by re-pointing only its `["q"]`
# read -- the rest would stay on the muon anchor, straddling two layers inside
# one quantity, which AGENTS.md forbids outright.
_CO_READ_FIELDS = (
    "calibration_inputs", "quantum_integers", "quantum_factorials",
    "plancherel_weights_n3", "physical_anchoring_bound",
    "universal_shape_coupling", "hbar_q", "hbar_q_sq", "q_inv",
    "H_A", "two_q", "z_markov", "s_skein", "Vol_4_1_str",
)


def co_read_fields(text: str) -> list[str]:
    """Which other pin-witness fields does this producer actually READ?

    The test is dict-key use -- a subscript or `.get()` against the loaded
    witness -- NOT the bare field name appearing anywhere in the file.  That
    distinction is the whole point: a substring scan counts local variables
    (`hbar_q_num`, `hbar_q_sym`) and emitted output keys (`hbar_q_50dps`) as
    though they were reads, and it over-reports by 7x.  Measured 2026-08-22:
    substring says 21 producers, dict-key says 3.  The inflated figure reached
    a merged audit doc before it was caught.
    """
    found = []
    for field in _CO_READ_FIELDS:
        quoted = re.escape(field)
        if re.search(r'\[\s*["\']' + quoted + r'["\']\s*\]', text) or \
           re.search(r'\.get\(\s*["\']' + quoted + r'["\']', text):
            found.append(field)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-contradictions", action="store_true",
                    help="list only the producers declared proton that pin muon")
    args = ap.parse_args()

    pins = direct_pinners()
    contradictions = [r for r, b, _, _ in pins if b == "physical_proton"]

    if args.list_contradictions:
        for rel in contradictions:
            print(rel)
        return 1 if contradictions else 0

    pops = witness_populations()
    tally = pops["tally"]
    print("witness populations carrying a muon-family q₀ value")
    print(f"  current  {MUON_CURRENT}…  {tally['current']}")
    print(f"  OLD      {MUON_OLD}…  {tally['old']}   <- superseded pin, stale on its own terms")
    print(f"  both (cross-anchor comparison)          {tally['both']}")
    print(f"  rounded / low-precision                 {tally['rounded']}")
    print(f"  TOTAL matching the loose prefix         {sum(tally.values())}")
    print()
    print("  NOTE: a grep for the 12-digit prefix sums the first two rows and")
    print("        reports one number.  They are different defects.")
    print()
    print(f"producers binding q₀ direct from {PIN_WITNESS}.witness.json")
    print("  (no anchor resolution — inherits whatever that witness carries)")
    by_bucket = Counter(b for _, b, _, _ in pins)
    for name, count in by_bucket.most_common():
        print(f"  {count:4d}  declared {name}")
    print()
    print("  of the UNDECLARED, what each producer SAYS it wants:")
    by_intent = Counter(i for _, b, i, _ in pins if b == "UNDECLARED")
    for name, count in by_intent.most_common():
        print(f"    {count:4d}  {name}")
    print()
    print("    'silent' means the directive default (proton) already answers it;")
    print("    a 'CAL-2 q_0' mention is NOT a muon signal -- see classify_intent().")
    print()
    co = [(r, f) for r, _, _, f in pins if f]
    print(f"  co-read a SECOND pin-witness field (cannot be re-pointed alone): {len(co)}")
    for rel, fields in co:
        print(f"    {rel}  {fields}")
    print("    (dict-key test, not substring -- see co_read_fields())")
    print()
    if contradictions:
        print(f"CONTRADICTION — declared physical_proton, pins muon: {len(contradictions)}")
        for rel in contradictions:
            print(f"    {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
