#!/usr/bin/env python3
"""Every hand-typed hyperbolic volume in the corpus, checked against SnapPy.

## Why

`Vol(4_1)` was carried as a decimal literal in a dozen places and as a closed
form in a handful more. The literals disagreed with each other and with the
truth; the closed forms did not. This audit exists because a decimal literal
cannot be checked by reading it, and the corpus has ~114 of them.

Found by this audit on first run (2026-08-21):

* **A wrong value labelled as census data.** `VOL_6_2 = 4.40083298054544839393`
  in two deuteron probes, annotated "SnapPy census", against the true
  `4.40083251612304610144` -- wrong at digit 9, 1.06e-7 relative.
* **A `Vol(4_1)` literal that prints 53 digits and is correct to 20**, copied
  into eight files. It diverges at digit 21; 33 digits are fabricated.
* A `Vol(6_1)` literal printing 46 digits, correct to 21.

## What "correct to N digits" means here, and why SnapPy is trustworthy for it

`Vol(4_1) = 2*Cl_2(pi/3)` has a closed form, so it can be checked with no
external data at all. Measured: SnapPy's `volume(bits_prec=500)` agrees with
`2*mp.clsin(2, mp.pi/3)` to **55 digits, relative error exactly 0**. So when
this audit says a literal is correct to 20 digits, that is a statement about
the literal, not about SnapPy's resolution.

## Three outcomes, deliberately distinguished

A short literal is not a defect. `VOL_B3 = 7.3277248` is correct at every
digit it prints; it just prints eight. Conflating that with a value that is
WRONG at a digit it prints would bury two real defects under twenty
non-defects, so:

* ``WRONG``       -- disagrees within the digits it prints. A defect.
* ``OVER_CLAIMED``-- prints materially more digits than are correct. The
                     value reads as measured and is not; fabricated tail.
* ``OK``          -- correct at every digit printed, however few.

## False positives this learned to avoid

The first version flagged ``VOL41_OVER_PI = 0.6461320971509606`` as 68 % wrong.
It is `Vol(4_1)/pi`, exactly right. A name containing a volume is not
necessarily a volume, so derived-quantity suffixes are excluded rather than
silently mis-compared -- and anything unrecognised is reported as
``UNRECOGNISED``, never as a pass.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

REPO = HERE.parent

# Name fragment -> SnapPy manifold. Longest match wins, so `8_11` beats `8_1`.
KNOWN = {
    "4_1": "4_1", "41": "4_1", "FIGURE_EIGHT": "4_1", "FIG8": "4_1",
    "5_2": "5_2", "52": "5_2",
    "6_1": "6_1", "61": "6_1",
    "6_2": "6_2", "62": "6_2",
    "6_3": "6_3", "63": "6_3",
    "7_4": "7_4", "74": "7_4",
    "8_1": "8_1",
    "8_11": "8_11", "811": "8_11",
    "L6A4": "L6a4", "BORROMEAN": "L6a4", "BOR": "L6a4", "B3": "L6a4",
    "8G": "L6a4",
    "WHITEHEAD": "L5a1", "L5A1": "L5a1",
}

# A name carrying one of these is a DERIVED quantity, not the volume itself.
# Comparing it to the census volume produces a confident, wrong answer.
DERIVED = ("OVER_", "_PER_", "_SQ", "SQUARED", "_RATIO", "_DENSITY", "_EPS",
           "_ERR", "_TARGET", "PRE_REGISTERED", "_HYP_D", "PHASE4")

LITERAL = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:mp\.)?mpf\(\s*"([0-9.]+)"')

_cache: dict[str, mp.mpf] = {}


def true_volume(mfld: str) -> mp.mpf:
    """Census volume at 500 bits -- verified exact against 2*Cl_2(pi/3)."""
    if mfld not in _cache:
        import snappy
        _cache[mfld] = mp.mpf(str(snappy.Manifold(mfld).volume(bits_prec=500)))
    return _cache[mfld]


def resolve(name: str) -> str | None:
    up = name.upper()
    if "VOL" not in up:
        return None
    if any(d in up for d in DERIVED):
        return None
    stem = up.replace("VOL", "")
    for key in sorted(KNOWN, key=len, reverse=True):
        if key in stem:
            return KNOWN[key]
    return None


def digits_printed(lit: str) -> int:
    """Significant digits the literal CLAIMS, trailing zeros included."""
    return len(lit.replace(".", "").lstrip("0"))


def digits_correct(lit: str, true: mp.mpf) -> int:
    got = mp.mpf(lit)
    if got == true:
        return digits_printed(lit)
    rel = abs(got - true) / abs(true)
    return max(0, int(mp.floor(-mp.log10(rel))))


def scan() -> list[dict]:
    grep = subprocess.run(
        ["grep", "-rn", "--include=*.py", "-E", r'= *(mp\.)?mpf\("[0-9]',
         "computations", "tools"],
        capture_output=True, text=True, cwd=REPO,
    ).stdout

    rows: list[dict] = []
    for line in grep.splitlines():
        if "_deprecated" in line:
            continue
        parts = line.split(":", 2)
        if len(parts) != 3:
            continue
        path, lineno, code = parts
        m = LITERAL.match(code)
        if not m:
            continue
        name, lit = m.group(1), m.group(2)
        if "VOL" not in name.upper():
            continue
        mfld = resolve(name)
        row = {"file": path, "line": int(lineno), "name": name, "literal": lit,
               "manifold": mfld}
        if mfld is None:
            row["verdict"] = "UNRECOGNISED"
            rows.append(row)
            continue
        true = true_volume(mfld)
        printed = digits_printed(lit)
        correct = digits_correct(lit, true)
        row.update({"digits_printed": printed, "digits_correct": correct,
                    "true": mp.nstr(true, 30)})
        if correct < printed - 1:
            # Wrong within what it prints, or padded far past what it backs.
            row["verdict"] = "WRONG" if correct < printed - 3 and correct < 12 \
                else "OVER_CLAIMED"
        else:
            row["verdict"] = "OK"
        rows.append(row)
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit JSON, no prose")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any WRONG or OVER_CLAIMED literal remains")
    args = ap.parse_args()

    try:
        import snappy  # noqa: F401
    except ImportError:
        print("snappy is not installed -- this audit cannot run without it.\n"
              "  pip install snappy", file=sys.stderr)
        return 77  # skip, not fail: absence of the tool is not a clean corpus

    rows = scan()
    by = {v: [r for r in rows if r["verdict"] == v]
          for v in ("WRONG", "OVER_CLAIMED", "OK", "UNRECOGNISED")}

    if args.json:
        print(json.dumps({"counts": {k: len(v) for k, v in by.items()},
                          "rows": rows}, indent=1))
    else:
        print(f"hyperbolic-volume literals scanned: {len(rows)}\n")
        for verdict, blurb in [
            ("WRONG", "disagree within the digits they print"),
            ("OVER_CLAIMED", "print materially more digits than are correct"),
        ]:
            print(f"{verdict}  ({len(by[verdict])}) -- {blurb}")
            for r in sorted(by[verdict], key=lambda r: r["digits_correct"]):
                print(f"  {r['file']}:{r['line']}  {r['name']}")
                print(f"      prints {r['digits_printed']}, correct to "
                      f"{r['digits_correct']}   Vol({r['manifold']}) = {r['true']}")
            print()
        print(f"OK            ({len(by['OK'])}) -- correct at every digit printed")
        print(f"UNRECOGNISED  ({len(by['UNRECOGNISED'])}) -- not matched to a "
              f"census manifold; NOT a pass")

    if args.strict and (by["WRONG"] or by["OVER_CLAIMED"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
