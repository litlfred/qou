#!/usr/bin/env python3
"""check-generated-lean — regenerate the machine-written Lean in memory and diff it.

Story TOOLS T9 (bean `qou-gl2k`). Two committed Lean files carry text that a
script in this repository writes:

  * `folio/quantum-observable-universe/lean/QOU/Knot/GeneratedGluing.lean` —
    every knot block, written by `scripts/gen-gluing-lean.py`. The 52-line
    module header above the first block and the closing `end` line are
    hand-written, so the comparison runs from the first block's heading to the
    line before that `end`.
  * `folio/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeCompletion.lean`
    — the depth-3 corner column (§4ae, `BokutShiaoCornerDepth3`), written by
    `scripts/gen-hecke-corner-column.py 3` and pasted in verbatim.

The depth-2 column (§4ad, `BokutShiaoCorner`) is NOT checked: the generator's
own docstring says §4ad was worked out by hand first and the script was checked
against it by *re-deriving* the same seventeen words and fifteen rules — the
same mathematics, not the same text. Measured 2026-10-05: the two differ on 964
lines while agreeing on what they prove, so a textual diff there would report
drift that is not drift.

Writes nothing: both generators print to stdout, and this script only reads
the committed files. Exit status, three states:

  0  every checked text regenerates identically
  1  drift — at least one regenerated text differs (a unified diff is printed)
  2  unknown — a generator could not run (e.g. SnapPy not installed); this is
     never reported as a pass

    python3 scripts/check-generated-lean.py
"""
from __future__ import annotations

import difflib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLUING = ROOT / "folio/quantum-observable-universe/lean/QOU/Knot/GeneratedGluing.lean"
HECKE = ROOT / "folio/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeCompletion.lean"
GLUING_END = "end QOU.Knot.GeneratedGluing"


def run(args: list[str]) -> tuple[int, str, str]:
    p = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def check_gluing() -> tuple[str, str]:
    text = GLUING.read_text()
    names = re.findall(r"^/-! ### `([^`]+)`", text, flags=re.M)
    if not names:
        return "fail", f"{GLUING.relative_to(ROOT)}: no knot block headings found"
    start = text.index(f"/-! ### `{names[0]}`")
    body = text[start:]
    tail = f"\n{GLUING_END}\n"
    if not body.endswith(tail):
        return "fail", f"{GLUING.relative_to(ROOT)}: does not end with `{GLUING_END}`"
    committed = body[: -len(tail)]
    code, out, err = run(["scripts/gen-gluing-lean.py", *names])
    if code != 0:
        why = err.strip().splitlines()[-1] if err.strip() else f"exit {code}"
        return "unknown", f"gen-gluing-lean.py could not run ({why})"
    regenerated = out.rstrip("\n") + "\n"
    if committed.rstrip("\n") + "\n" == regenerated:
        return "pass", f"GeneratedGluing.lean: {len(names)} knot blocks regenerate identically"
    diff = difflib.unified_diff(
        committed.splitlines(True), regenerated.splitlines(True),
        "committed", "regenerated", n=2,
    )
    return "fail", "GeneratedGluing.lean drifted:\n" + "".join(list(diff)[:80])


def check_corner(depth: int, namespace: str) -> tuple[str, str]:
    code, out, err = run(["scripts/gen-hecke-corner-column.py", str(depth)])
    if code != 0:
        why = err.strip().splitlines()[-1] if err.strip() else f"exit {code}"
        return "unknown", f"gen-hecke-corner-column.py {depth} could not run ({why})"
    regenerated = out.rstrip("\n")
    text = HECKE.read_text()
    if regenerated in text:
        return "pass", f"HeckeCompletion.lean: {namespace} (depth {depth}) regenerates identically"
    m = re.search(rf"^namespace {namespace}\n.*?^end {namespace}$", text, flags=re.M | re.S)
    committed = m.group(0) if m else ""
    diff = difflib.unified_diff(
        committed.splitlines(True), (regenerated + "\n").splitlines(True),
        "committed", "regenerated", n=2,
    )
    return "fail", f"HeckeCompletion.lean {namespace} drifted:\n" + "".join(list(diff)[:80])


def main() -> int:
    results = [check_gluing(), check_corner(3, "BokutShiaoCornerDepth3")]
    for verdict, msg in results:
        mark = {"pass": "✓", "fail": "✗", "unknown": "?"}[verdict]
        print(f"{mark} {msg}")
    verdicts = {v for v, _ in results}
    if "fail" in verdicts:
        return 1
    if "unknown" in verdicts:
        print("Not every generator ran, so this is NOT a pass.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
