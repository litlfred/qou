#!/usr/bin/env python3
"""SCREEN: Lean files carrying numeric literals whose cited producer has moved.

A Lean file that documents its constants as coming from a `computations/` script
is making a **provenance claim**. Nothing in this corpus checks it. When the
producer changes, the Lean keeps the old numbers and keeps the old sentence, and
both look fine: the theorems still typecheck, the file still compiles, `#print
axioms` is still clean. Only the claim is false.

THE CASE THAT PROMPTED THIS (2026-09-14, beans `qou-xc8t` / `qou-1n7g`).
`QOU/Archimedean/JetOrderIndependence.lean` documents

    jetJacobianBase = !![1/4, -1, 55/16; 1/2, 0, -1/16; 1, 0, 0]

as "witnessed from the framework's own canonical Markov traces
(`computations/jet_order_pivots.py`)". Running that producer today gives
`!![1/4, 0, 11/4; 1/2, 1, 1/4; 1, 0, 0]` -- elimination determinant `-11/4`, not
the `1/16` the Lean carries, and LU pivots `(1/4, 1, -11)` rather than
`(1/4, 2, 1/8)`. Two of three rows moved. The conclusion survives (`-11/4 != 0`
as much as `1/16 != 0`) so no theorem is wrong; the *provenance* is.

That file had been verified three separate times (2026-08-22, 2026-09-08,
2026-09-14) and none of the three caught it, because all three checked the SHAPE
of the discharge -- is there a fabricated instance? -- and none re-ran the
producer.

WHY NOTHING ELSE COVERS IT. The three nearest audits are each scoped away:

    assertion_on_literal_audit.py  -- Python witness assertions, not Lean
    hardcoded_literal_audit.py     -- rglob("*.py"), and about CODATA constants
    lean_ref_resolution_audit.py   -- rglob("*.ts"), resolution not values

This is the same shape as `convention-c-producer-audit.py` walking only `*.py`
while the Lean surface went uncounted for weeks (AGENTS.md, detector-blindness
taxonomy). Every literal audit in this corpus is Python-scoped.

WHAT THIS IS AND IS NOT

It is a **screen**, not a verdict. It reports a Lean file when BOTH:

  1. the file carries a rational or decimal literal, AND
  2. it names a `computations/` producer whose committed witness records a
     `scriptHash` that no longer matches that producer's source.

Condition 2 is NECESSARY for the defect and nowhere near sufficient. AGENTS.md
records ~700 self-stale witnesses corpus-wide, of which the staleness triage has
found essentially none safe to refresh -- so a self-stale citation is the normal
state, not an alarm. What the screen buys is the intersection: a *provenance
claim* over *numbers* whose *source has moved*. Confirming one means reading the
Lean's literals against a fresh producer run, which only an agent can do.

A hit is therefore a candidate to READ, never a file to change. Do not "fix" a
hit by adopting the producer's current numbers: the 2026-06 numbers may be the
right ones and the producer may be what regressed. Establish what changed first
(`qou-xc8t` enumerates the options).

KNOWN LIMITS, stated so the next reader does not rediscover them

  - Association is by stem: witness `<a-b-c>.witness.json` <-> producer
    `<a_b_c>.py`. A producer whose witness is named differently is invisible.
  - A producer with no committed witness is invisible (nothing to compare).
  - `scriptHash` is a whole-file hash, so a comment-only edit drifts it. That
    makes the screen noisy, not wrong -- it is why this is a screen.
  - It cannot see import-cone drift: a producer byte-stable while a module it
    calls changed emits different numbers and is NOT flagged here. Use
    `witness_import_cone_staleness_audit.py` for that half.
  - `.lake/` is excluded. An earlier draft of this screen did not exclude it and
    reported "11869 Lean files scanned" -- 8013 of them Mathlib's own source.
    The candidate count was unaffected (no Mathlib file cites a
    `computations/*.py`) but every denominator was inflated ~3x.

MEASURED 2026-09-14 on main `6229029329`:

    corpus Lean files (excluding .lake)          3856
      ... carrying a numeric literal             2086
    live producers under computations/           4434
    witnesses carrying a scriptHash              3121
    CANDIDATES (distinct lean/producer pairs)      46   = 2.2% of 2086
      ... confirmed defects                         1   (JetOrderIndependence)
      ... unverified                               45

Read-only. Writes no witness and no file.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# A Lean numeric literal that could plausibly be witnessed data: a rational or a
# decimal. Bare small integers are excluded deliberately -- `Fin 3`, `n + 1` and
# exponents would drown the signal.
NUM = re.compile(r"(?<![\w.])(?:\d+\s*/\s*\d+|\d+\.\d+)(?![\w.])")
PY_CITE = re.compile(r"[\w./-]*?([A-Za-z_][\w-]*)\.py\b")

# The one confirmed positive. --selftest FAILS if the screen stops reporting it.
# A calibration the audit asserts about itself cannot discover its own blind
# spot (AGENTS.md detector-blindness taxonomy, row 45), so this pins a real file.
SELFTEST_LEAN = "QOU/Archimedean/JetOrderIndependence.lean"
SELFTEST_PRODUCER = "computations/jet_order_pivots.py"


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def corpus_lean() -> list[Path]:
    """Every .lean under content/, EXCLUDING .lake (Mathlib + package source)."""
    return sorted(
        p for p in (ROOT / "content").rglob("*.lean") if ".lake" not in p.parts
    )


def scan() -> tuple[list[tuple], dict]:
    lean_files = corpus_lean()

    producers: dict[str, list[Path]] = {}
    for p in (ROOT / "computations").rglob("*.py"):
        if "_deprecated" in p.parts:
            continue
        producers.setdefault(p.stem, []).append(p)

    wit: dict[str, tuple[Path, str | None]] = {}
    for w in (ROOT / "computations").rglob("*.witness.json"):
        try:
            d = json.loads(w.read_text())
        except Exception:
            continue
        wd = d.get("witness", d)
        wit[w.name[: -len(".witness.json")]] = (w, wd.get("scriptHash"))

    # witness stem -> producer stem (the corpus convention is hyphen vs underscore)
    wit_by_producer_stem: dict[str, tuple[Path, str]] = {}
    for wstem, (wpath, whash) in wit.items():
        if whash:
            wit_by_producer_stem[wstem.replace("-", "_")] = (wpath, whash)

    rows, seen = [], set()
    n_with_literals = 0
    for lf in lean_files:
        try:
            txt = lf.read_text()
        except Exception:
            continue
        n_lits = len(NUM.findall(txt))
        if not n_lits:
            continue
        n_with_literals += 1
        for stem in set(PY_CITE.findall(txt)):
            if stem not in producers or stem not in wit_by_producer_stem:
                continue
            wpath, whash = wit_by_producer_stem[stem]
            for prod in producers[stem]:
                live = sha12(prod)
                if live == whash:
                    continue
                key = (str(lf), str(prod))
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    (
                        lf.relative_to(ROOT),
                        prod.relative_to(ROOT),
                        wpath.relative_to(ROOT),
                        whash,
                        live,
                        n_lits,
                    )
                )

    stats = {
        "lean_files": len(lean_files),
        "lean_with_literals": n_with_literals,
        "producers": sum(len(v) for v in producers.values()),
        "witnesses_with_scripthash": len(wit_by_producer_stem),
        "candidates": len(rows),
    }
    return sorted(rows), stats



# --------------------------------------------------------------------------
# STAGE 2 -- narrow before spending producer runs.
#
# Stage 1's signal is necessary and weak. The defect shape is sharper: the Lean
# literal MATCHES THE STALE WITNESS, so the Lean is carrying that witness's data
# and the producer has since moved. When none of a Lean file's literals appear
# anywhere in the cited witness, the citation is a pointer ("see this script")
# rather than a provenance claim over numbers, and no producer run is needed.
#
# Measured 2026-09-14: 46 -> 22 needing a run, 24 pointers. The one confirmed
# defect ranks FIRST by shared-literal count (5 of 5), which is the ordering a
# triage filter should produce and was not tuned for.
#
# The "pointer" bucket is a triage bucket, NOT an all-clear: a Lean file could
# carry a number the producer emits in a form this extractor does not match
# (different precision, symbolic form).
# --------------------------------------------------------------------------

def _witness_numbers(wpath: Path) -> set[str]:
    """Numeric-looking tokens anywhere in the witness, normalised."""
    txt = (ROOT / wpath).read_text()
    out = {m.replace(" ", "") for m in re.findall(r"-?\d+\.\d+|-?\d+\s*/\s*\d+", txt)}
    try:
        d = json.loads(txt)
    except Exception:
        return out

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, float):
            out.add(repr(o))
        elif isinstance(o, str):
            for m in re.findall(r"-?\d+\.\d+|-?\d+\s*/\s*\d+", o):
                out.add(m.replace(" ", ""))

    walk(d)
    return out


def stage2(rows):
    """Split stage-1 rows into (needs_run, pointer), ranked by shared literals."""
    needs, pointer = [], []
    for lf, prod, wpath, wh, lh, n in rows:
        lits = {x.replace(" ", "") for x in NUM.findall((ROOT / lf).read_text())}
        shared = sorted(lits & _witness_numbers(wpath))
        (needs if shared else pointer).append((lf, prod, wpath, shared, len(lits)))
    needs.sort(key=lambda r: -len(r[3]))
    pointer.sort()
    return needs, pointer


def main(argv: list[str]) -> int:
    selftest = "--selftest" in argv
    rows, stats = scan()

    if selftest:
        hit = any(
            str(r[0]).endswith(SELFTEST_LEAN) and str(r[1]) == SELFTEST_PRODUCER
            for r in rows
        )
        print(f"selftest: known positive {SELFTEST_LEAN}")
        print(f"          cited producer {SELFTEST_PRODUCER}")
        print(f"          detected: {hit}")
        if not hit:
            print(
                "FAIL — the screen no longer reports its one confirmed positive.\n"
                "Either the defect was fixed (update SELFTEST_* and say so) or the\n"
                "screen has acquired a blind spot. Do NOT report a clean scan until\n"
                "you know which."
            )
            return 1
        print("PASS")
        return 0

    print(f"corpus Lean files (excluding .lake)  : {stats['lean_files']}")
    print(f"  ... carrying a numeric literal     : {stats['lean_with_literals']}")
    print(f"live producers under computations/   : {stats['producers']}")
    print(f"witnesses carrying a scriptHash      : {stats['witnesses_with_scripthash']}")
    print()
    print(f"CANDIDATES (Lean w/ literals citing a producer whose witness is stale)")
    print(f"  distinct (lean, producer) pairs    : {stats['candidates']}")
    print()
    for lf, prod, wpath, wh, lh, n in rows:
        print(f"  {lf}")
        print(f"      producer {prod}")
        print(f"      witness  {wpath}   scriptHash {wh} != live {lh}   ({n} literals)")
    print()
    if "--stage2" in argv:
        needs, pointer = stage2(rows)
        print("=" * 70)
        print(f"STAGE 2 -- needs a fresh producer run : {len(needs)}")
        print(f"          pointer, not a claim        : {len(pointer)}")
        print()
        for lf, prod, wpath, shared, nl in needs:
            print(f"  {lf}")
            print(f"      producer {prod}")
            print(f"      {len(shared)} of {nl} Lean literals also in the witness: "
                  f"{shared[:8]}{' ...' if len(shared) > 8 else ''}")
        print()
        for lf, prod, wpath, shared, nl in pointer:
            print(f"  [pointer] {lf}  ({nl} literals, 0 shared)  <- {prod}")
        print()

    print("These are CANDIDATES TO READ, not files to change. A hit means the")
    print("provenance claim is unverified, not that the Lean's numbers are wrong;")
    print("confirming one means reading its literals against a fresh producer run.")
    print("See beans qou-xc8t / qou-1n7g for the one confirmed instance.")
    # Non-zero is informational here: nothing is wired to this, and the class has
    # not been triaged. Do not promote it to a gate without a triage pass.
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
