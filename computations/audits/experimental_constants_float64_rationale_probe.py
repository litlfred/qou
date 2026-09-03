#!/usr/bin/env python3
"""Why bucket B exists: the CODATA masses are float64 BY DECISION, and the
decision's stated reason is half obsolete.

`computations/substrate/experimental_constants.py` casts every CODATA mass to
binary64 at import:

    M_E_MEV     = float(_M_E_MEV)
    M_P_MEV     = float(_M_P_MEV)
    M_N_MEV     = float(_M_N_MEV)

with this rationale in the comment above it:

    "float()-cast on import so the ~266 importers' float arithmetic /
     json.dumps stay intact (an mpf would break json.dumps)"

That single cast is the upstream cause of most of the "bucket B" population in
`assertion_value_float64_triage.py` -- producers that import mpmath, call
mp.log, and are nonetheless float64-equivalent end to end, because every input
they start from is already a double. `channel_product_mass.py` is the clearest
case and the single largest offender in the corpus at 64 assertion fields: it
computes `M_free = Z*M_P_MEV + N*m_n_derived_3input + Z*me` in pure float64 and
then wraps the result in mpmath calls, which cannot restore what was never
there.

This probe MEASURES the rationale rather than arguing with it, because the
answer is not a simple "the comment is wrong" -- it is right about one thing
and wrong about another, and which half applies depends on the consumer:

  1. "an mpf would break json.dumps" -- TRUE of a BARE `json.dumps`, and there
     are producers in the tree that hand-roll one. FALSE of the witness path,
     which every producer that emits a witness goes through: `WitnessBuilder`
     serializes with `json.dump(..., default=str)`, and `default=str` renders
     an mpf at full precision. So the reason does not cover the case it is
     most often invoked for.
  2. "the importers' float arithmetic stays intact" -- mpf interoperates with
     float for arithmetic, comparison and f-string formatting, so the ordinary
     cases are fine. The real hazard is narrower and worse: `math.log(mpf)`
     does not raise, it SILENTLY DOWNCASTS. A module-level flip would therefore
     not fail loudly at the sites where it matters most.

It also re-counts the importers, because the comment's "~266" is a hand-kept
figure and this repo has a documented habit of those decaying.

Writes no witness. Read-only, and deliberately so: this probe exists to size a
decision, not to take it. Flipping the constants moves numbers across the whole
mass sector and is the owner's call (bean qou-p77d).
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import subprocess
import sys


def _repo_root() -> pathlib.Path:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True)
        return pathlib.Path(out.stdout.strip())
    except Exception:
        return pathlib.Path(".").resolve()


_IMPORT = re.compile(
    r"^\s*(?:from\s+experimental_constants\s+import|import\s+experimental_constants)",
    re.M)


def count_importers(root: pathlib.Path) -> tuple[int, int]:
    """(live importers, importers excluding the generated qou-mass mirror)."""
    live = mirror = 0
    for p in root.rglob("*.py"):
        s = str(p)
        if ".git" in s or "_deprecated" in s:
            continue
        try:
            if not _IMPORT.search(p.read_text(encoding="utf-8", errors="replace")):
                continue
        except Exception:
            continue
        if "qou-mass" in s:
            mirror += 1
        else:
            live += 1
    return live, mirror


def main() -> int:
    from mpmath import mp, mpf
    mp.dps = 50
    root = _repo_root()
    x = mpf("0.51099895069")          # M_E_MEV at full CODATA-2022 width
    checks: list[tuple[str, bool, str]] = []

    # --- claim 1 --------------------------------------------------------
    try:
        json.dumps({"v": x})
        bare_breaks = False
    except TypeError:
        bare_breaks = True
    checks.append((
        "bare json.dumps(mpf) breaks", bare_breaks,
        "the comment's reason is REAL for a hand-rolled dumps"))

    via_default = json.dumps({"v": x}, default=str)
    default_ok = "0.51099895069" in via_default
    checks.append((
        "json.dumps(mpf, default=str) preserves it", default_ok,
        "…and does NOT apply to the witness path, which uses default=str"))

    # The witness path is the one that matters; assert it directly rather
    # than trusting the paragraph above.
    # `witness_base` in computations/ is a thin shim; the serializer that
    # actually writes the file lives in the qou-substrate package. Assert
    # against THAT file -- an earlier version of this probe checked
    # computations/witness_base.py, found no `default=str`, and reported a
    # FAIL for a property that holds.
    wb = (root / "tools" / "qou-substrate" / "python" / "qou_substrate"
          / "witness.py")
    wb_uses_default = False
    if wb.exists():
        wb_uses_default = "default=str" in wb.read_text(encoding="utf-8",
                                                        errors="replace")
    checks.append((
        f"{wb.name} serializes with default=str", wb_uses_default,
        "so a producer emitting a witness would NOT be broken by an mpf"))

    # --- claim 2 --------------------------------------------------------
    arith_ok = True
    try:
        _ = x * 3.0, 3.0 / x, x < 1.0, f"{x:.6f}"
    except Exception:
        arith_ok = False
    checks.append((
        "mpf interoperates with float arithmetic", arith_ok,
        "the ordinary importer sites are unaffected by a flip"))

    downcasts = False
    try:
        r = math.log(x)
        downcasts = isinstance(r, float)
    except Exception:
        pass
    checks.append((
        "math.log(mpf) SILENTLY downcasts to float", downcasts,
        "the real hazard: a flip would not fail loudly where it matters"))

    # --- the stale figure ----------------------------------------------
    live, mirror = count_importers(root)
    stated = 266
    checks.append((
        f"importer count is {live} live (+{mirror} generated), not ~{stated}",
        live != stated,
        "the comment's figure is hand-kept and has decayed like the others"))

    print("experimental_constants float64 rationale — measured\n")
    ok = True
    for label, got, why in checks:
        ok &= got
        print(f"  {'PASS' if got else 'FAIL'}  {label}")
        print(f"        {why}")
    print(f"\n  live importers of experimental_constants : {live}")
    print(f"  generated-mirror importers               : {mirror}")
    print("\nREADING: the rationale is HALF right. It correctly protects a bare")
    print("json.dumps, and it does not apply to the witness path at all — which")
    print("is where the bucket-B assertion fields come from. A flip is therefore")
    print("defensible on the serialization argument alone, but it moves numbers")
    print("across the mass sector and `math.log` would absorb an mpf silently,")
    print("so it is sized here and NOT taken. See bean qou-p77d.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
