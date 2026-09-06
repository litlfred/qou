#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""Catch a script that HARDCODES a value another producer computed.

## The defect

A producer computes a number and records it in its `*.witness.json`. A second
script needs that number and, instead of reading the witness, types it in:

    # binding_probe.py
    TR_M_ATOM = 0.5751234567        # <- copied from atomic-tr-m.witness.json

Two things then go wrong, and the second is the dangerous one:

* **Truncation.** The literal carries fewer digits than the witness did.
* **Staleness.** The producer is re-run, the witness changes, and the copy does
  not. The two silently disagree from then on, with nothing to detect it --
  no gate compares a source literal against a witness.

This is the generalisation of the AME case in `codata_truncation_audit.py`.
There, `8.481798` / `7.718043` / `28.295673` were traced to the *deprecated*
`ame-2020-binding-energies.witness.json` -- a hand-maintained file the registry
says "had drifted", retired as a source of truth, and still being copied from.
That was found by hand. This audit is the general version.

## Why the digit floor is high

Short decimals collide by coincidence: `0.5`, `1.25`, `2.0` appear in every
witness and every script and mean nothing. The floor is deliberately set so
that a match is implausible by chance -- with `MIN_SIG` significant digits a
collision needs the same ~11-digit mantissa to arise twice independently.

Lower it and this audit becomes noise; that is the failure mode it is most
likely to be "improved" into.

## What is NOT a finding

* A literal in the producer's OWN witness. A producer that asserts its own
  expected value is doing a regression check, not copying someone else's
  number. Keyed on the witness's `scriptFile`, not on filename similarity.
* Anything the CODATA/AME audit already owns -- reported there, not twice.
* Values inside a non-constructor string (test fixtures), same rule as the
  sibling audit.

Output: `witness-value-copy-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
COMP = ROOT / "computations"

# A match needs at least this many significant digits to beat coincidence.
MIN_SIG = 11

NUMBER = re.compile(r"\d+\.\d+")
_NUMERIC_CTORS = {"mpf", "mpmathify", "Decimal", "Fraction", "float",
                  "mpc", "mpi"}


def sig_digits(lit: str) -> int:
    return len(lit.replace(".", "").replace("-", "").lstrip("0"))


def index_witnesses() -> dict[str, set[str]]:
    """decimal literal -> set of witness paths carrying it."""
    idx: dict[str, set[str]] = defaultdict(set)
    for w in COMP.rglob("*.witness.json"):
        if "_deprecated" in w.parts:
            # Still indexed: copying from a RETIRED witness is the worst
            # case, not an exempt one. See the AME instance in the docstring.
            pass
        try:
            raw = w.read_text()
        except OSError:
            continue
        for m in NUMBER.finditer(raw):
            lit = m.group(0)
            if sig_digits(lit) >= MIN_SIG:
                idx[lit].add(str(w.relative_to(ROOT)))
    return idx


def own_witnesses(py: Path) -> set[str]:
    """Witness paths this script itself writes (by scriptFile provenance)."""
    out = set()
    for w in COMP.rglob("*.witness.json"):
        try:
            d = json.loads(w.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and d.get("scriptFile") == py.name:
            out.add(str(w.relative_to(ROOT)))
    return out


def fixture_lines(src: str) -> set[tuple[int, str]]:
    out: set[tuple[int, str]] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    protected = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            nm = getattr(n.func, "id", None) or getattr(n.func, "attr", None)
            if nm in _NUMERIC_CTORS:
                for a in ast.walk(n):
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        protected.add(id(a))
    for n in ast.walk(tree):
        if (isinstance(n, ast.Constant) and isinstance(n.value, str)
                and id(n) not in protected):
            for m in NUMBER.finditer(n.value):
                for ln in range(n.lineno, (n.end_lineno or n.lineno) + 1):
                    out.add((ln, m.group(0)))
    return out


def scan(idx: dict[str, set[str]]) -> list[dict]:
    rows: list[dict] = []
    provenance: dict[str, str] = {}
    for w in COMP.rglob("*.witness.json"):
        try:
            d = json.loads(w.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(d, dict) and isinstance(d.get("scriptFile"), str):
            provenance[str(w.relative_to(ROOT))] = d["scriptFile"]

    for f in sorted(COMP.rglob("*.py")):
        if "_deprecated" in f.parts or "__pycache__" in f.parts:
            continue
        if f.name == Path(__file__).name:
            continue
        try:
            src = f.read_text()
        except OSError:
            continue
        fx = fixture_lines(src)
        for i, line in enumerate(src.splitlines(), 1):
            st = line.strip()
            if st.startswith("#"):
                continue
            for m in NUMBER.finditer(line):
                lit = m.group(0)
                if sig_digits(lit) < MIN_SIG or lit not in idx:
                    continue
                if (i, lit) in fx:
                    continue
                carriers = idx[lit]
                # a producer asserting its own recorded value is not copying
                foreign = {w for w in carriers
                           if provenance.get(w) != f.name}
                if not foreign:
                    continue
                # SPREAD is the discriminator between the two things an
                # 11-digit match can mean.
                #
                # A value carried by ONE or a FEW witnesses is one producer's
                # output, and a script holding it has copied it: when that
                # producer is re-run the copy goes stale silently.
                #
                # A value carried by DOZENS is a shared reference constant
                # flowing in as an input -- m_e (0.51099895069) sits in 137
                # witnesses, 1/alpha_em (137.035999084) in 16. Those are not
                # copies of anybody's output, and the CODATA/AME audit already
                # owns them. Reporting them here would double-count the
                # backlog and bury the actionable class under it.
                spread = "NARROW" if len(foreign) <= 3 else "SHARED"
                rows.append({
                    "file": str(f.relative_to(ROOT)),
                    "line": i,
                    "literal": lit,
                    "sig_digits": sig_digits(lit),
                    "spread": spread,
                    "witnesses": sorted(foreign)[:4],
                    "witness_count": len(foreign),
                    "deprecated_source": any("_deprecated" in w
                                             for w in foreign),
                })
    return rows


def _selftest() -> int:
    """The digit floor must reject coincidence and accept a real copy."""
    cases = [("0.5", False, "a short decimal collides by chance everywhere"),
             ("2.224566", False, "7 digits — below the floor, coincidence"),
             ("0.57512345678", True, "11 digits — implausible by chance")]
    bad = 0
    print("selftest — digit floor")
    for lit, want, why in cases:
        got = sig_digits(lit) >= MIN_SIG
        ok = got == want
        bad += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] {lit:<16s} "
              f"accepted={got!s:<5s} want={want!s:<5s}  {why}")
    if bad:
        print("\nSELFTEST FAILED — the floor no longer separates a real copy "
              "from a coincidence; findings are not trustworthy.")
        return 1
    print(f"\nselftest ok — floor is {MIN_SIG} significant digits")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true")
    ap.add_argument("--baseline", action="store_true",
                    help="ratchet: exit 1 only on NARROW copies absent from "
                         "the baseline (blocks NEW copies)")
    ap.add_argument("--write-baseline", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    idx = index_witnesses()
    rows = scan(idx)
    narrow = [r for r in rows if r["spread"] == "NARROW"]
    dep = [r for r in narrow if r["deprecated_source"]]

    out = HERE.parent / "witness-value-copy-audit.witness.json"
    out.write_text(json.dumps({
        "engine": "python-stdlib",
        "computation": "witness-value-copy-audit",
        "scriptFile": Path(__file__).name,
        "description": (
            "Source literals of >= %d significant digits that also appear in "
            "a *.witness.json the script does not itself produce — a value "
            "copied instead of loaded. Such a copy goes stale silently when "
            "the producer is re-run." % MIN_SIG),
        "min_sig_digits": MIN_SIG,
        "indexed_literals": len(idx),
        "total": len(rows),
        "narrow_total": len(narrow),
        "narrow_files": len({r["file"] for r in narrow}),
        "shared_total": len(rows) - len(narrow),
        "files": len({r["file"] for r in rows}),
        "from_deprecated_witness": len(dep),
        "findings": rows,
    }, indent=2) + "\n")

    print("=" * 74)
    print("WITNESS-VALUE COPY AUDIT — a computed value typed in, not read")
    print("=" * 74)
    print(f"  indexed witness literals (>= {MIN_SIG} sig digits): {len(idx)}")
    print(f"  NARROW (<=3 witnesses — one producer's output, COPIED): "
          f"{len(narrow)} in {len({r['file'] for r in narrow})} file(s)")
    print(f"  SHARED (>3 — a reference constant; the CODATA/AME audit owns "
          f"these): {len(rows) - len(narrow)}")
    print(f"  of the NARROW, copied from a _deprecated/ witness: {len(dep)}")
    for r in (narrow if a.list else narrow[:20]):
        src = r["witnesses"][0]
        print(f"    {r['file']}:{r['line']}  {r['literal']}")
        print(f"        also in {src}"
              + (f" (+{r['witness_count'] - 1} more)"
                 if r["witness_count"] > 1 else ""))
    if not a.list and len(narrow) > 20:
        print(f"    ... and {len(narrow) - 20} more (--list)")
    print(f"\n  witness -> {out.name}")
    # Ratchet on NARROW only, keyed on (file, literal) -> count. Never on the
    # line number: an edit anywhere above a finding shifts it, and a ratchet
    # that cries wolf on every edit is one people re-baseline past.
    #
    # BLOCKING ON NEW, NOT ON THE BACKLOG, and deliberately so. Some of the
    # 264 existing NARROW copies are DELIBERATE freezes -- see
    # alpha_em_nonD_index_route_probe.py, whose header says "frozen from the
    # merged falsifications". Separating deliberate from accidental needs a
    # hand pass, and an attempt to automate it here (scan nearby comments for
    # "frozen"/"copied") got that very file WRONG, because its note sits six
    # lines above the value and the window was four. That split is not
    # shipped. Until the backlog is triaged the honest gate is: no NEW copies.
    bl = HERE.parent / "witness-value-copy-baseline.json"
    key = lambda r: f"{r['file']}::{r['literal']}"  # noqa: E731
    if a.write_baseline:
        counts: dict[str, int] = {}
        for r in narrow:
            counts[key(r)] = counts.get(key(r), 0) + 1
        bl.write_text(json.dumps(
            {"_comment": "Pre-existing NARROW witness-value copies, as "
                         "<file>::<literal> -> count. DRAINS, never grows. "
                         "Some entries are deliberate freezes and need a hand "
                         "pass; none may be added to silence a new copy.",
             "counts": dict(sorted(counts.items()))}, indent=2) + "\n")
        print(f"\nbaseline written: {len(counts)} entries -> {bl.name}")
        return 0
    if a.baseline:
        try:
            known = json.loads(bl.read_text())["counts"]
        except (OSError, ValueError, KeyError):
            known = {}
        seen: dict[str, int] = {}
        fresh = []
        for r in narrow:
            k = key(r)
            seen[k] = seen.get(k, 0) + 1
            if seen[k] > known.get(k, 0):
                fresh.append(r)
        print(f"\n  RATCHET: {sum(known.values())} baselined, "
              f"{len(fresh)} NEW")
        if fresh:
            print("  NEW copies — read the witness instead of typing the "
                  "value; do NOT baseline:")
            for r in fresh[:20]:
                print(f"    {r['file']}:{r['line']}  {r['literal']}"
                      f"  (in {r['witnesses'][0]})")
            return 1
        return 0

    if a.strict and narrow:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
