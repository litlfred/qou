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
import ast
import json
import re
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


# ── Identifying WHICH manifold a literal is about ────────────────────
#
# Rewritten 2026-08-30 (bean qou-ckbv) after this audit reported WRONG 0 /
# OVER_CLAIMED 0 on a corpus that contained a 30-zero-padded Vol(8_11) in the
# canonical `substrate/knot_volumes.py` and an entire PSLQ basis of eight
# volumes wrong at digits 2-13. It missed all of them because it asked three
# questions in a row, every one answered by the variable's NAME:
#
#   1. grep for `= mpf("<digits>` -- so `_SNAPPY_HP_50 = "8.28..."`, whose
#      mpf() is applied to the variable a line later, was never a candidate;
#   2. `if "VOL" not in name.upper(): continue` -- so `v_6_2 = mpf("4.4008...")`
#      was dropped, though it IS a hyperbolic volume and badly wrong;
#   3. `resolve()` then needed a knot key inside that name.
#
# So the audit only ever checked constants that already followed the naming
# convention, and reported a clean corpus because the badly-named ones were
# invisible rather than correct. A detector whose recall depends on the author
# having named things well cannot find what a careless author wrote.
#
# Identification now runs two routes and takes whichever can speak:
#
#   * BY NAME, for literals so wrong that their value identifies nothing --
#     `v_7_4` was off at the SECOND significant digit (7.6e-3 relative), which
#     no value-matcher will ever recognise as Vol(7_4). Only the name knows.
#   * BY VALUE, for literals whose name says nothing -- `_SNAPPY_HP_50` is a
#     precision tag, not a knot, but the number was good to 20 digits and the
#     census identifies it at once.
#
# Neither route alone catches both, which is why the old single route caught
# neither.

# Knot/link tokens as they appear inside identifiers: `v_6_2`, `VOL_8_11`,
# `"8_5"` (a dict key), `L6a4`. Bare `\d+_\d+` deliberately does NOT match
# `_SNAPPY_HP_50` -- "HP_50" has no digit before the underscore.
_KNOT_TOKEN = re.compile(r'(?<![0-9A-Za-z])(\d{1,2}_\d{1,2})(?![0-9])')
_LINK_TOKEN = re.compile(r'(?<![0-9A-Za-z])(L\d+[an]\d+)(?![0-9])', re.I)
DECIMAL = re.compile(r'\d+\.\d+')

# Through 10 crossings: the amphichiral table in tau_amphichiral_sdp_probe
# carries 10_17/10_33/10_37/10_43/10_45, every one wrong at digit 0-1, and a
# census stopping at 9 never looked at them.
CENSUS = ([f"{n}_{i}" for n in range(3, 11) for i in range(1, 170)]
          + ["L5a1", "L6a1", "L6a2", "L6a3", "L6a4", "L6a5", "L6n1",
             "L7a1", "L7a2", "L7a3", "L7a4", "L7a5", "L7a6", "L7a7",
             "7^2_1", "L8a1", "L8a2"])

_census: dict | None = None


def census_volumes() -> dict:
    """Census volumes, hyperbolic only (torus knots have volume 0)."""
    global _census
    if _census is None:
        import snappy
        out = {}
        for name in CENSUS:
            try:
                v = mp.mpf(str(snappy.Manifold(name).volume(bits_prec=500)))
            except Exception:
                continue
            if v > 0:
                out[name] = v
        _census = out
    return _census


def identify_by_name(name: str) -> str | None:
    """The manifold the IDENTIFIER claims, whatever the number says."""
    up = name.upper()
    if any(d in up for d in DERIVED):
        return None
    m = _LINK_TOKEN.search(name)
    if m:
        for key in census_volumes():
            if key.lower() == m.group(1).lower():
                return key
    m = _KNOT_TOKEN.search(name)
    if m and m.group(1) in census_volumes():
        return m.group(1)
    return resolve(name)          # the original VOL_*/BORROMEAN/8G route


def identify_by_value(val: mp.mpf) -> str | None:
    """The manifold the NUMBER is, whatever the identifier claims.

    1e-9 is tight on purpose: this route exists to name literals whose
    identifier is uninformative, and those are the nearly-right ones. A
    literal wrong in its 3rd digit is not evidence about which manifold was
    meant, so it is left to the name route.
    """
    best, best_rel = None, None
    for name, v in census_volumes().items():
        rel = abs(val - v) / v
        if best_rel is None or rel < best_rel:
            best, best_rel = name, rel
    return best if best_rel is not None and best_rel < mp.mpf("1e-9") else None


def _string_constants(path: Path) -> list:
    """(lineno, literal, enclosing-name) for every decimal string in a file.

    Parsed with `ast`, not grepped, for two reasons the old grep could not
    handle: implicit concatenation across lines (the PSLQ basis is written as
    `mpf("4.4008..." "5458...")`, and a line-oriented matcher sees only the
    first fragment, understating the printed width), and the fact that a
    literal need not sit inside an `mpf(` call to end up in one.
    """
    try:
        tree = ast.parse(path.read_text(errors="ignore"))
    except Exception:
        return []

    # Nearest enclosing label wins, so the passes run innermost-first and use
    # setdefault. Order matters and is the whole point: a table is written
    #
    #     VOLS = {"8_11": mp.mpf("8.28631808635811"), ...}
    #     amphichiral = [("8_17", mp.mpf("10.78528041739327")), ...]
    #
    # and the knot name is on the KEY, not on the assignment. An earlier cut
    # of this function ran the Assign pass first, so every row in such a table
    # was labelled `VOLS` — carrying no knot token, hence unidentifiable by
    # name — and only rows that happened to be nearly-right got caught by the
    # value route. That silently hid an 8_11 wrong at digit 8 and a 7_4 wrong
    # at digit 2, which is precisely the failure this audit was rewritten to
    # stop making.
    names: dict = {}

    def label(node, name):
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant):
                names.setdefault(sub.lineno, name)

    for node in ast.walk(tree):          # 1. dict keys: {"8_11": mpf(...)}
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    label(v, k.value)
    for node in ast.walk(tree):          # 2. pairs: ("8_17", mpf(...))
        if isinstance(node, (ast.Tuple, ast.List)) and len(node.elts) == 2:
            first, second = node.elts
            if isinstance(first, ast.Constant) and isinstance(first.value, str):
                label(second, first.value)
    for node in ast.walk(tree):          # 3. fall back to the assignment name
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    label(node.value, t.id)

    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            lit = node.value.strip()
            if DECIMAL.fullmatch(lit) and digits_printed(lit) >= 12:
                out.append((node.lineno, lit, names.get(node.lineno)))
    return out


def scan() -> list[dict]:
    roots = [REPO / "computations", REPO / "tools", REPO / "qou-mass"]
    rows: list[dict] = []
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.py")):
            if any(p in {"_deprecated", "__pycache__", ".git"}
                   for p in path.parts):
                continue
            if path.resolve() == Path(__file__).resolve():
                continue
            rel = str(path.relative_to(REPO))
            for lineno, lit, name in _string_constants(path):
                val = mp.mpf(lit)
                by_name = identify_by_name(name) if name else None
                by_value = identify_by_value(val)
                mfld = by_name or by_value
                if mfld is None:
                    # Only UNRECOGNISED when the NAME advertises a volume;
                    # otherwise every long decimal in the corpus lands here
                    # and the signal drowns.
                    if name and "VOL" in name.upper():
                        rows.append({"file": rel, "line": lineno, "name": name,
                                     "literal": lit, "manifold": None,
                                     "verdict": "UNRECOGNISED"})
                    continue
                true = true_volume(mfld)
                # A label that MENTIONS a knot does not make its value that
                # knot's volume. `SHAPES = {"6_1": ("0.8951...", ...)}` holds
                # tetrahedra shape parameters; `THETA_T4["muon (4_1)"]` is an
                # angle; `"-Vol(4_1)/(2pi)"` labels a derived expression whose
                # literal is the half-volume. The name route reaches all three.
                #
                # Real transcription defects stay near the value they meant:
                # the worst found in this corpus was 25 % off (an 8_3 entry
                # holding 6.5517 for 5.2387). The false positives above sit at
                # 50-97 %. 0.35 separates them, but it is a heuristic, not a
                # proof — so anything beyond it is REPORTED as LABEL_ONLY
                # rather than silently dropped, and does not gate.
                if (by_name and not by_value
                        and abs(mp.mpf(lit) - true) / true > mp.mpf("0.35")):
                    rows.append({"file": rel, "line": lineno, "name": name,
                                 "literal": lit, "manifold": mfld,
                                 "identified_by": "name",
                                 "verdict": "LABEL_ONLY"})
                    continue
                # An EXACT float64 expansion is a deliberate record, not a
                # fabricated tail: 2.0298832128193073920385813835309818387\
                # 03155517578125 is the exact decimal value of a double, and
                # witness_regen_classify.py carries it as a TEST FIXTURE for
                # the very classifier that recognises f64 padding. Flagging
                # it would ask an author to corrupt a fixture to quiet a gate.
                # Compare against the double's EXACT value (mp.mpf(float(x))
                # is a binary conversion), not against repr(), which shortens
                # to 17 digits and never matches a 52-digit expansion.
                with mp.workdps(80):
                    _is_f64_exact = (digits_printed(lit) > 17
                                     and mp.mpf(lit) == mp.mpf(float(lit)))
                if _is_f64_exact:
                    rows.append({"file": rel, "line": lineno,
                                 "name": name or "(unnamed)", "literal": lit,
                                 "manifold": mfld,
                                 "identified_by": "name" if by_name else "value",
                                 "verdict": "F64_EXACT"})
                    continue
                printed = digits_printed(lit)
                correct = digits_correct(lit, true)
                row = {"file": rel, "line": lineno, "name": name or "(unnamed)",
                       "literal": lit, "manifold": mfld,
                       "digits_printed": printed, "digits_correct": correct,
                       "true": mp.nstr(true, 30),
                       "identified_by": "name" if by_name else "value"}
                if by_name and by_value and by_name != by_value:
                    # The identifier says one manifold and the number is
                    # exactly another's volume. That is a mislabel, not a
                    # precision problem, and wants a different fix.
                    row["verdict"] = "MISLABELLED"
                    row["value_is"] = by_value
                elif correct < printed - 1:
                    row["verdict"] = "WRONG" if (correct < printed - 3
                                                 and correct < 12) \
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
          for v in ("WRONG", "MISLABELLED", "OVER_CLAIMED", "OK",
                    "UNRECOGNISED", "LABEL_ONLY", "F64_EXACT")}

    if args.json:
        print(json.dumps({"counts": {k: len(v) for k, v in by.items()},
                          "rows": rows}, indent=1))
    else:
        print(f"hyperbolic-volume literals scanned: {len(rows)}\n")
        for verdict, blurb in [
            ("WRONG", "disagree within the digits they print"),
            ("MISLABELLED", "the number is a DIFFERENT manifold's volume, exactly"),
            ("OVER_CLAIMED", "print materially more digits than are correct"),
        ]:
            print(f"{verdict}  ({len(by[verdict])}) -- {blurb}")
            for r in sorted(by[verdict], key=lambda r: r["digits_correct"]):
                print(f"  {r['file']}:{r['line']}  {r['name']}"
                      f"   [identified by {r['identified_by']}]")
                if verdict == "MISLABELLED":
                    print(f"      named for {r['manifold']} but the value is "
                          f"Vol({r['value_is']})")
                else:
                    print(f"      prints {r['digits_printed']}, correct to "
                          f"{r['digits_correct']}   Vol({r['manifold']}) "
                          f"= {r['true']}")
            print()
        print(f"OK            ({len(by['OK'])}) -- correct at every digit printed")
        print(f"UNRECOGNISED  ({len(by['UNRECOGNISED'])}) -- not matched to a "
              f"census manifold; NOT a pass")
        print(f"F64_EXACT     ({len(by['F64_EXACT'])}) -- exact float64 "
              f"expansions, recorded deliberately; advisory, does not gate")
        print(f"LABEL_ONLY    ({len(by['LABEL_ONLY'])}) -- label names a knot "
              f"but the value is nowhere near its volume (usually a derived "
              f"quantity); advisory, does not gate")
        for r in by["LABEL_ONLY"]:
            print(f"    {r['file']}:{r['line']}  {r['name']} -> "
                  f"Vol({r['manifold']})")

    if args.strict and (by["WRONG"] or by["OVER_CLAIMED"] or by["MISLABELLED"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
