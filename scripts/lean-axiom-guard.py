#!/usr/bin/env python3
"""Keystone axiom guard — `#print axioms` as a QA gate, not a one-off check.

Motivation (2026-08-07). Two keystones were merged claiming a discharge that a
per-declaration axiom check refutes: `OVTopAssembly.sum_numSYT_sq_eq_factorial`
and everything reindexed from it depend on `sorryAx`. File-level `grep sorry` is
a *screen*; the proof term is the *verdict*. See
`docs/audits/2026-08-07-ov-cone-axiom-audit-overclaim-correction.md`.

This script pins the measured axiom status of named declarations so that:

  * a declaration recorded `clean` that starts depending on `sorryAx` FAILS the
    gate (regression — the usual direction of harm);
  * a declaration recorded `sorryAx` that becomes clean is reported as a
    PROMOTION (someone closed an upstream gap; update the registry and the
    claims that were scoped around it).

Usage
-----
    scripts/lean-axiom-guard.py                 # check every entry
    scripts/lean-axiom-guard.py --filter TAIL   # substring filter on decl name
    scripts/lean-axiom-guard.py --registry F    # alternate registry file

Exit codes: 0 = all as recorded; 1 = regression; 2 = environment/setup problem.
A promotion alone exits 0 (it is good news) but prints a LOUD notice.

Registry format (one entry per line, `#` comments allowed):

    <import-module> | <fully-qualified-decl> | clean|sorryAx

The Lean root is `content/quantum-observable-universe/lean`; `LEAN_PATH` must
already be set for lean-direct use (see `.claude/skills/local/lean-environment-setup.md`
— restore the olean cache first, and note that a declaration's own module olean
must exist).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LEAN_ROOT = Path("content/quantum-observable-universe/lean")

# Measured 2026-08-07 by `#print axioms`. Keep sorted by module for readability.
DEFAULT_REGISTRY = """
# --- the (TAIL) first-instance chain (covariance-kernel epic qou-x631) ---
# The SIGN is genuinely sorry-free and is the content of the (TAIL) instance.
QOU.BraidsAndKnots.YoungDiagramTailFirstInstance | QOU.BraidsAndKnots.YoungDiagramTailFirstInstance.nuV_top_nonneg | clean
# The SYT-encoding bridge is genuinely sorry-free.
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux | sorryAx-free-expected-clean-alias
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numStandardYoungTableaux_le_numSYT | clean

# --- known-BAD: the RSK identity and everything reindexed from it ---
# The real gap is upstream (RegularRepBlockTrace's sorry on the specialised
# lemma, plus the Specht-core cone: 16 of 23 modules carry sorry).
QOU.BraidKnot.OVTopAssembly | QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial | sorryAx
QOU.BraidKnot.RSKBurnsideDischarge | QOU.BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional | sorryAx

# --- the gluing/volume arc cited by the mass-theory exposition blocks (PR #4925) ---
# Three content blocks assert these are proved; the assertion is only as good as an
# axiom check, so the check is pinned here rather than left as a one-off.  Measured
# 2026-08-10: all six depend on [propext, Classical.choice, Quot.sound] and nothing
# else.  A `sorry` appearing anywhere upstream regresses this gate, which is the
# point — the blocks would then be claiming more than the Lean delivers.
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.strictConcaveOn_tetVolLine | clean
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.cot_quadratic_pos | clean
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.deriv_deriv_Lob | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.norm_eq_sin_div_sin | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.log_sin_sub_log_sin | clean
QOU.Knot.KummerRadial | QOU.Knot.KummerRadial.kummer | clean
# The volume functor's definitional layer (same PR).  `volume_rotate` is the
# well-definedness that makes "the volume of an ideal tetrahedron" a property of
# the tetrahedron rather than of a chosen edge label.
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.volume_rotate | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.rotate_angles | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.volume_eq_dilog | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTriangulation.volume_eq_dilog | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.param_prod | clean
"""


def parse_registry(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            print(f"axiom-guard: malformed registry line: {raw!r}", file=sys.stderr)
            sys.exit(2)
        module, decl, expected = parts
        # Tolerate the alias marker used for entries whose module differs from
        # the declaration's own namespace.
        if expected.startswith("sorryAx-free"):
            expected = "clean"
        if expected not in {"clean", "sorryAx"}:
            print(f"axiom-guard: bad expectation {expected!r} in: {raw!r}", file=sys.stderr)
            sys.exit(2)
        out.append((module, decl, expected))
    return out


def run_axiom_check(entries: list[tuple[str, str, str]]) -> dict[str, set[str]]:
    """Return {decl: set-of-axioms}. One lean invocation for the whole batch."""
    modules = sorted({m for m, _, _ in entries})
    body = "".join(f"import {m}\n" for m in modules)
    body += "".join(f"#print axioms {d}\n" for _, d, _ in entries)

    # The file must live under the Lean root (lean rejects outside paths).
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".lean", prefix="AxiomGuard", dir=LEAN_ROOT, delete=False
    ) as fh:
        fh.write(body)
        tmp = Path(fh.name)
    try:
        proc = subprocess.run(
            ["lean", tmp.name],
            cwd=LEAN_ROOT,
            capture_output=True,
            text=True,
            timeout=3600,
        )
    except FileNotFoundError:
        print("axiom-guard: `lean` not on PATH — restore the toolchain first.", file=sys.stderr)
        sys.exit(2)
    finally:
        tmp.unlink(missing_ok=True)

    out = proc.stdout + proc.stderr
    if "object file" in out and "does not exist" in out:
        print("axiom-guard: a module olean is missing; build it lean-direct first:", file=sys.stderr)
        for line in out.splitlines():
            if "does not exist" in line:
                print("  " + line.strip(), file=sys.stderr)
        sys.exit(2)

    # `#print axioms X` prints: 'X' depends on axioms: [a, b,\n c]
    found: dict[str, set[str]] = {}
    for m in re.finditer(
        r"'([^']+)' depends on axioms: \[([^\]]*)\]", out, re.S
    ):
        decl = m.group(1)
        axs = {a.strip() for a in m.group(2).split(",") if a.strip()}
        found[decl] = axs
    # A declaration proved without any axiom prints a different sentence.
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", out):
        found[m.group(1)] = set()
    if not found:
        print("axiom-guard: no `#print axioms` output parsed. Raw:", file=sys.stderr)
        print(out[:2000], file=sys.stderr)
        sys.exit(2)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=Path, default=None)
    ap.add_argument("--filter", default=None, help="substring filter on declaration name")
    args = ap.parse_args()

    if not LEAN_ROOT.is_dir():
        print(f"axiom-guard: run from the repo root (missing {LEAN_ROOT})", file=sys.stderr)
        return 2

    text = args.registry.read_text() if args.registry else DEFAULT_REGISTRY
    entries = parse_registry(text)
    if args.filter:
        entries = [e for e in entries if args.filter in e[1]]
    if not entries:
        print("axiom-guard: nothing to check")
        return 0

    found = run_axiom_check(entries)

    regressions: list[str] = []
    promotions: list[str] = []
    missing: list[str] = []
    for _, decl, expected in entries:
        if decl not in found:
            missing.append(decl)
            continue
        has_sorry = "sorryAx" in found[decl]
        status = "sorryAx" if has_sorry else "clean"
        mark = "ok  " if status == expected else "FAIL"
        print(f"  [{mark}] {decl}: {status} (recorded {expected})")
        if status == expected:
            continue
        if expected == "clean" and has_sorry:
            regressions.append(decl)
        else:
            promotions.append(decl)

    if missing:
        print("\naxiom-guard: declarations not found in the environment:", file=sys.stderr)
        for d in missing:
            print("  " + d, file=sys.stderr)
        return 2

    if promotions:
        print("\n*** PROMOTION — an upstream gap closed: " + ", ".join(promotions))
        print("    Update the registry AND the claims that were scoped around the sorryAx.")
    if regressions:
        print("\n*** REGRESSION — these were clean and now depend on sorryAx:")
        for d in regressions:
            print("      " + d)
        return 1
    print("\naxiom-guard: all declarations match their recorded axiom status.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
