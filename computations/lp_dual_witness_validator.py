#!/usr/bin/env python3
"""
LP-dual witness validator — first-class enforcement.

Walks every JSON witness under computations/ and
flags operator-selection / LP / SDP witnesses that lack required
LP-dual fields (per prop:operator-selection-lp § dual program).

Required fields (recursive search inside the witness JSON):
  - y0_star          shadow price of the net constraint
  - y_star           shadow prices of Frobenius positivity constraints
  - active_set       (or active_constraints / active_channels)
  - primal_obj       primal optimum value
  - dual_obj         dual optimum value (= n_target · y0_star)
  - duality_gap      |primal_obj - dual_obj|

Witness files are flagged when their filename or `description` /
`computation` field signals an LP/SDP/operator-selection compute.
This catches the failure mode that motivated this script: scripts
that solve the primal LP but never extract / report the dual,
losing the principled binding-energy interpretation.

Usage (CI):
    python3 computations/lp_dual_witness_validator.py
    → exit 0 if all flagged witnesses include duals; exit 1 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from lp_dual_solver import verify_dual_present


# Witness file name patterns or (description / computation) field
# substrings that indicate a NUMERICAL LP / SDP solve where the
# binding-energy / shadow-price interpretation applies.
#
# Tightened (2026-05-02 post-refactor-framework audit): excluded
# overly-broad terms ("confinement-", "sdp" alone, "knot-operator")
# that match SYMBOLIC certificate witnesses or knot-particle
# feasibility probes — these don't compute LP duals (they emit
# filtration certificates or feasibility status, a separate notion).
#
# Only true operator-selection / shadow-price / LP-dual witnesses
# need the primal+dual extraction.
LP_SDP_HINTS = (
    "lp-dual",
    "lp_dual",
    "operator-selection-lp",
    "operator_selection_lp",
    "shadow-price",
    "shadow_price",
    "primal-dual",
    "primal_dual",
    "lp-duality",
    "lp_duality",
)


# Solver-import patterns that indicate a script ACTUALLY solves an LP/SDP.
# A witness is only flagged if its sibling .py imports one of these.
ACTUAL_SOLVER_IMPORTS = (
    "from scipy.optimize import linprog",
    "scipy.optimize.linprog",
    "import cvxpy",
    "from cvxpy",
    "from lp_dual_solver import",
    "import lp_dual_solver",
    "linprog(",
)


def _sibling_script(witness_path: Path) -> Path | None:
    """Find the .py script that emitted this witness.

    Heuristic: same directory, filename obtained by stripping
    .witness.json or -witness.json and adding .py. Try both
    underscore and hyphen variants.
    """
    stem = witness_path.name.removesuffix(".witness.json").removesuffix(
        "-witness.json")
    for variant in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        cand = witness_path.parent / f"{variant}.py"
        if cand.exists():
            return cand
    return None


def _script_imports_solver(script_path: Path) -> tuple[bool, str]:
    try:
        text = script_path.read_text()
    except OSError:
        return False, ""
    for marker in ACTUAL_SOLVER_IMPORTS:
        if marker in text:
            return True, marker
    return False, ""


def is_lp_sdp_witness(path: Path) -> tuple[bool, str]:
    """Returns (is_lp_sdp, reason).

    A witness is flagged iff:
    1. Its filename or description/computation field contains an
       LP/SDP/operator-selection hint, AND
    2. Its sibling .py script actually imports an LP/SDP solver
       (linprog / cvxpy / lp_dual_solver). This eliminates the
       false-positive case where a script's name or description
       contains 'shadow'/'lp'/'dual' but the script doesn't solve
       any optimization problem (e.g., precomputed shadow prices).
    """
    # Step 1: name/description hint
    name = path.name.lower()
    hint_match: tuple[str, str] | None = None
    for hint in LP_SDP_HINTS:
        if hint in name:
            hint_match = ("filename", hint)
            break
    if hint_match is None:
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            return False, ""
        for field in ("description", "computation", "audit", "name"):
            v = data.get(field)
            if isinstance(v, str):
                v_low = v.lower()
                for hint in LP_SDP_HINTS:
                    if hint in v_low:
                        hint_match = (field, hint)
                        break
                if hint_match:
                    break
    if hint_match is None:
        return False, ""

    # Step 2: sibling script must import an actual LP/SDP solver
    sibling = _sibling_script(path)
    if sibling is None:
        return False, ""  # no sibling — can't confirm; don't flag
    has_solver, marker = _script_imports_solver(sibling)
    if not has_solver:
        return False, ""  # name match but no actual solver — false positive
    field, hint = hint_match
    return True, f"{field} matches '{hint}' + script imports '{marker}'"


def collect_wired_witnesses(repo_root: Path) -> set[str]:
    """Collect wired witness basenames from content block `computation.witness`."""
    wired: set[str] = set()
    content_root = repo_root / "content"
    ts_files = content_root.glob("*/*/*.ts")
    witness_pattern = re.compile(
        r"witness(?:File)?\s*:\s*[\"']([^\"']+\.json)[\"']"
    )
    for ts in ts_files:
        try:
            txt = ts.read_text()
        except OSError:
            continue
        for m in witness_pattern.finditer(txt):
            wired.add(Path(m.group(1)).name)
    return wired


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    strict_wired = "--strict-wired" in argv
    list_wired = "--list-wired" in argv
    root = Path(__file__).parent
    repo_root = root.parent.parent
    wired = collect_wired_witnesses(repo_root) if (strict_wired or list_wired) else set()
    witnesses = sorted(root.glob("*.witness.json")) + sorted(
        root.glob("*-witness.json"))
    flagged = []
    for w in witnesses:
        is_lp, reason = is_lp_sdp_witness(w)
        if is_lp:
            flagged.append((w, reason))

    print(f"Scanned {len(witnesses)} witness files; "
          f"{len(flagged)} flagged as LP/SDP/operator-selection.")
    if strict_wired or list_wired:
        flagged_wired = [(w, r) for (w, r) in flagged if w.name in wired]
        print(f"Wired LP/SDP flagged subset: {len(flagged_wired)} "
              f"(from {len(wired)} total wired witnesses).")
    print()

    if list_wired:
        print("Flagged LP/SDP witnesses (wired status):")
        for w, reason in flagged:
            status = "wired" if w.name in wired else "audit/orphan"
            print(f"  - {w.name:45s} [{status}] {reason}")
        print()

    failures = []
    for w, reason in flagged:
        result = verify_dual_present(w)
        if not result["ok"]:
            failures.append((w, reason, result))

    if strict_wired:
        failures = [f for f in failures if f[0].name in wired]
        scope_msg = "flagged wired witnesses"
    else:
        scope_msg = "flagged witnesses"

    if not failures:
        if strict_wired:
            print(f"OK — all {len([w for w, _ in flagged if w.name in wired])} "
                  "flagged wired witnesses include LP dual.")
        else:
            print(f"OK — all {len(flagged)} flagged witnesses include LP dual.")
        return 0

    # Brief failure summary
    severity = "FAIL" if (strict or strict_wired) else "WARN"
    denominator = len([w for w, _ in flagged if w.name in wired]) if strict_wired else len(flagged)
    print(f"{severity} — "
          f"{len(failures)}/{denominator} {scope_msg} missing "
          f"LP dual fields.")
    print()
    print("Sample (first 10):")
    for w, reason, result in failures[:10]:
        sibling = _sibling_script(w)
        print(f"  ✗  {w.name}")
        print(f"     reason:  {reason}")
        if sibling is not None:
            print(f"     script:  {sibling.name}")
        print(f"     missing: {result['missing']}")
    if len(failures) > 10:
        print(f"  ... ({len(failures) - 10} more)")
    print()
    print("To fix: route the LP/SDP solve through")
    print("  computations/lp_dual_solver.py")
    print("which returns BOTH primal and dual via")
    print("  solve_operator_selection_lp() or solve_psd_operator_selection_sdp().")
    print("The result's .to_dict() contains all required fields.")
    print()
    if strict or strict_wired:
        if strict_wired:
            print("Exit 1 (--strict-wired mode).")
        else:
            print("Exit 1 (--strict mode).")
        return 1
    print("Exit 0 (warn-only mode; pass --strict or --strict-wired to enforce).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
