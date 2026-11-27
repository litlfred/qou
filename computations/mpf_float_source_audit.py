#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""Source-level `mpf(<float>)` audit — catch fake precision at authoring time.

Owner directive: "NO FLOAT64".

**Why this exists.** `witness_float64_padding_audit.py` catches float64 garbage
*after* it has been serialized into a witness. By then the run is done and the
fix is a producer re-run. This audit catches the same defect **where it
originates** — the moment a value is handed to mpmath already rounded.

**The defect.**

    mp.mpf(0.1)        # mpmath receives 0.1000000000000000055511151231257827…
    mp.mpf("0.1")      # mpmath receives 0.1 exactly, to full precision

A Python float literal is parsed to binary64 *before* mpmath ever sees it, so
`mpf(0.1)` cannot be more accurate than a double no matter what `mp.dps` is
set to. Raising the precision afterwards only prints more of the error.

**Three classes, and only one is a defect:**

| class | example | verdict |
|---|---|---|
| `DEFECT` | `mpf(1e-30)`, `mpf(0.1)` | literal is **not** exactly a binary64 → information already lost |
| `benign` | `mpf(1.0)`, `mpf(2.5)`, `mpf(1e9)` | exactly representable → nothing lost (though `mpf(1)` is cleaner) |
| `advisory-cast` | `mpf(float(x))` | an explicit downcast. Sometimes *deliberate* (measuring the nearest double); sometimes an honest marker that `x` already came from numpy/float64. Reported, not failed. |

Marking a deliberate cast:

    return abs(x - mpf(float(x))) / abs(x)   # float64-intentional: measuring
                                             # distance to the nearest double

`--strict` fails on `DEFECT` only. The baseline is **zero** — this surface was
driven to zero rather than baselined, because it is small enough to fix
outright, and a gate whose backlog is empty is one nobody learns to ignore.

Output: `mpf-float-source-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

from mpmath import mp, mpf

mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SEARCH_ROOTS = [ROOT / "computations", ROOT / "tools"]

MPF_NAMES = {"mpf", "mpmathify"}
MARKER = "float64-intentional"


def exactly_representable(v: float) -> bool:
    """True iff the literal's decimal source IS a binary64, so writing it as a
    float loses nothing. `1.0`, `2.5`, `1e9` yes; `0.1`, `1e-30` no."""
    return mpf(repr(v)) == mpf(v)


def audit_file(p: Path) -> list[dict]:
    # NEVER return [] on input we could not process. "No findings" and "no
    # information" are different answers, and returning the first for the
    # second converts breakage into silence: bean qou-brkp records this gate
    # family reporting clean on two files a remediation had just made
    # unparseable, which is why they went unnoticed for a month.
    rel = p.relative_to(ROOT).as_posix()
    try:
        src = p.read_text(encoding="utf-8")
    except Exception as e:
        return [{"file": rel, "line": 0, "class": "unreadable",
                 "arg": None, "source": f"{type(e).__name__}: {e}", "fix": None}]
    try:
        tree = ast.parse(src, filename=str(p))
    except SyntaxError as e:
        return [{"file": rel, "line": e.lineno or 0, "class": "unparseable",
                 "arg": None, "source": f"SyntaxError: {e.msg}", "fix": None}]
    except Exception as e:
        return [{"file": rel, "line": 0, "class": "unparseable",
                 "arg": None, "source": f"{type(e).__name__}: {e}", "fix": None}]
    lines = src.splitlines()
    out: list[dict] = []

    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        nm = getattr(n.func, "attr", None) or getattr(n.func, "id", "")
        if nm not in MPF_NAMES or not n.args:
            continue
        a = n.args[0]
        line = lines[n.lineno - 1].strip() if n.lineno <= len(lines) else ""
        # A marker may sit on the call line or on the 2 lines above it
        # (the usual place for an explanatory comment).
        ctx = " ".join(lines[max(0, n.lineno - 3): n.lineno])
        marked = MARKER in ctx

        if isinstance(a, ast.Constant) and isinstance(a.value, float):
            cls = "benign" if exactly_representable(a.value) else "DEFECT"
            out.append({"file": rel, "line": n.lineno, "class": cls,
                        "arg": repr(a.value), "source": line[:110],
                        "fix": f'{nm}("{a.value!r}")'.replace("'", "")})
        elif isinstance(a, ast.Call) and getattr(a.func, "id", "") == "float":
            out.append({"file": rel, "line": n.lineno,
                        "class": "marked-cast" if marked else "advisory-cast",
                        "arg": "float(...)", "source": line[:110], "fix": None})
    return out


def scan() -> list[dict]:
    rows: list[dict] = []
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.py")):
            rows.extend(audit_file(p))
    return rows


def self_test() -> int:
    cases = [(1e-30, False), (0.1, False), (1.5e-3, False),
             (1.0, True), (0.0, True), (2.5, True), (1e9, True), (1e5, True)]
    bad = [(v, e, exactly_representable(v)) for v, e in cases
           if exactly_representable(v) != e]
    if bad:
        print("SELF-TEST FAILED:")
        for v, e, g in bad:
            print(f"   {v!r}: expected exact={e}, got {g}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: non-representable literals "
          "flagged, exactly-representable ones not.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any DEFECT remains (baseline is zero)")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    rows = scan()
    by: dict[str, list[dict]] = {}
    for r in rows:
        by.setdefault(r["class"], []).append(r)
    defects = by.get("DEFECT", [])
    # A file the gate could not read is a HOLE IN THE GATE, not a pass.
    blind = by.get("unparseable", []) + by.get("unreadable", [])

    print("=" * 74)
    print("mpf(<float>) SOURCE AUDIT — fake precision at the point of authoring")
    print("=" * 74)
    for cls, note in (("DEFECT", "literal not exactly a binary64 — precision already lost"),
                      ("benign", "exactly representable — nothing lost"),
                      ("advisory-cast", "explicit float() downcast — review, not a failure"),
                      ("marked-cast", f"downcast marked `{MARKER}`"),
                      ("unparseable", "FILE DOES NOT PARSE — this gate is blind to it"),
                      ("unreadable", "FILE COULD NOT BE READ — this gate is blind to it")):
        print(f"  {cls:<15} {len(by.get(cls, [])):>4}   {note}")

    if blind:
        print("\n  BLIND SPOTS — the gate could not process these files, so their")
        print("  mpf(<float>) status is UNKNOWN, not clean (bean qou-brkp):")
        for r in blind:
            print(f"    {r['file']}:{r['line']}  {r['source']}")

    if defects:
        print("\n  DEFECTS — pass the value as a STRING so mpmath parses it at full")
        print("  precision:")
        for r in defects:
            print(f"    {r['file']}:{r['line']}")
            print(f"        {r['source']}")
            print(f"        fix: {r['fix']}")
    else:
        print("\n  ✓ no mpf(<non-representable float literal>) in the source tree")

    if by.get("advisory-cast"):
        print(f"\n  advisory — explicit float() downcasts (mark deliberate ones with")
        print(f"  `# {MARKER}: <reason>`):")
        for r in by["advisory-cast"][:15]:
            print(f"    {r['file']}:{r['line']}  {r['source']}")

    out = HERE / "mpf-float-source-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "schema": "witness/v1",
        "name": "mpf-float-source-audit",
        "description": "Source-level mpf(<float>) detection. DEFECT = the literal is "
                       "not exactly a binary64, so precision is lost before mpmath "
                       "sees it. Complements the witness-level float64-padding audit "
                       "by catching the defect at authoring time.",
        "data": {"counts": {k: len(v) for k, v in by.items()},
                 "defects": defects, "rows": rows},
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")
    print(f"\nWrote {out.name}")
    return 1 if (args.strict and (defects or blind)) else 0


if __name__ == "__main__":
    sys.exit(main())
