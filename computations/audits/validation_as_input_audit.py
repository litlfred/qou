"""I11 audit — CODATA `_VALIDATION` constants used as production inputs.

`folio-assistant/computations/codata_constants.py` exposes a family
of `M_*_MEV_VALIDATION` constants (M_P, M_N, M_D, M_T, M_HE3, …)
explicitly tagged in the source as "DO NOT USE AS PREDICTION INPUTS
— retained only for `err = pred - M_X_VALIDATION` comparisons".

The I11 antipattern in `local/compute-integration-watcher` is:

  A script imports one of the `_VALIDATION` constants AND uses
  it in a way that is NOT a final-line comparison — e.g. feeds
  it into a formula, passes it as a function argument other than
  the comparison target, or multiplies it with a derived quantity.

This audit walks every Python script under
`folio-assistant/computations/`, looks for `_VALIDATION` imports,
and classifies the usage:

  - `ok_comparison_only`     — value only appears in `pred - ...`,
                                 `... - pred`, `abs(... - ...)`,
                                 or as a test-assertion `expected=`
                                 / `target=` keyword argument
  - `ok_acknowledged_anchor` — script docstring contains a
                                 CLASS-A / Workplan-0b banner
                                 explicitly accepting the
                                 anchor (e.g.
                                 `probe_flavor_dressed_mass_split.py`
                                 after PR #696)
  - `i11_violation`           — value is used as an input to a
                                 computation (any line that uses
                                 it outside the recognised
                                 comparison or test contexts)
  - `imported_unused`         — imported but never referenced
                                 (cleanup target)

Emits `validation-as-input-audit.witness.json` with the per-script
classification.

Usage:
    python3 folio-assistant/computations/validation_as_input_audit.py [--strict]
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent

# Validation constants exposed by codata_constants.py — kept in
# sync with the source's "DO NOT USE AS PREDICTION INPUTS" stanza.
VALIDATION_CONSTANTS = (
    "M_P_MEV_VALIDATION",
    "M_N_MEV_VALIDATION",
    "M_D_MEV_VALIDATION",
    "M_T_MEV_VALIDATION",
    "M_HE3_MEV_VALIDATION",
    "M_HE4_MEV_VALIDATION",
    "M_LI6_MEV_VALIDATION",
    "M_LI7_MEV_VALIDATION",
    "M_BE7_MEV_VALIDATION",
    "M_BE8_MEV_VALIDATION",
    "M_BE9_MEV_VALIDATION",
    "M_P_MEV_VALIDATION_ERR",
    "M_N_MEV_VALIDATION_ERR",
)

# Anchor-banner markers — when the script's docstring acknowledges
# the calibration-as-anchor status, the validation usage is OK
# (CLASS-A acknowledged-stub per Workplan-0b).
ANCHOR_BANNER_PATTERNS = (
    r"CLASS-A",
    r"acknowledged.{0,5}stub",
    r"CAL-?[34]",
    r"Workplan-0b",
    r"pending.{0,40}substrate.{0,40}derivation",
    r"M_N anchor",
)

# Comparison-line patterns — usage in these contexts is OK.  We
# match the validation name appearing on either side of a `-`
# subtraction, inside `abs(...)`, or as the value to keyword args
# `expected=`, `target=`, `validation=`, `codata=`, `reference=`.
COMPARISON_KW_PATTERN = re.compile(
    r"(?:expected|target|validation|codata|reference)\s*=\s*([A-Z_]+)"
)
# `pred - X_VAL` or `X_VAL - pred` style — match on the same line
# as a `-` operator AND any of the comparison-name hints, OR an
# abs() wrapper.
COMPARISON_LINE_INDICATORS = (
    " - ", "− ", " -=", "- ", "abs(", "math.fabs(", "mp.fabs(",
    "residual", "err", "delta", "diff",
)

# Recording / display context — storing the anchor for provenance or
# printing it is NOT a computation input (refinement, 2026-06-16: these
# were the dominant false-positive class). `add_parameter`/`add_data`/
# `add_assertion` write the reference value into the witness JSON;
# print/f-strings display it.
RECORDING_INDICATORS = (
    "add_parameter", "add_data", "add_assertion", "add_caveat",
    ".nstr(", "print(", 'f"', "f'", "logging.", "logger.",
)

# Dict-value recording — `"key": str(M_X_VALIDATION)` stores the anchor into a
# (string-keyed) data structure (e.g. an `ATOMS = {…}` roster used later in
# `B = M_codata − pred` comparisons), not a derivation input (refinement,
# 2026-06-16 — the dict-roster false-positive class, parallel to the I8 fix).
DICT_VALUE_RX = re.compile(r"""["'][^"']*["']\s*:\s*""")


def _classify_script(path: Path) -> dict[str, Any] | None:
    """Audit one Python script for validation-constant usage."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "import" not in text:
        return None

    # Quick rejection: no validation import → skip.
    found = [v for v in VALIDATION_CONSTANTS if v in text]
    if not found:
        return None

    rel = path.relative_to(REPO_ROOT)
    row: dict[str, Any] = {
        "path": str(rel),
        "validation_constants_imported": found,
    }

    # Check the module docstring for an anchor banner.
    # The docstring is the leading `"""..."""` of the module.
    docstring_match = re.search(r'^"""(.*?)"""', text, re.DOTALL)
    docstring = docstring_match.group(1) if docstring_match else ""
    has_banner = any(
        re.search(p, docstring, re.IGNORECASE) for p in ANCHOR_BANNER_PATTERNS
    )

    # Walk usage lines (any line containing one of the constants).
    lines = text.splitlines()
    usage_lines: list[tuple[int, str]] = []
    for i, line in enumerate(lines, start=1):
        # Strip Python comments (# ...) from the line for
        # classification — comments may explain the constant but
        # don't count as USE.
        code_part = re.sub(r"#.*$", "", line)
        # Also strip string literals: the constant NAME appearing inside a
        # quoted string (e.g. `"source": "... M_P_MEV_VALIDATION (reference)"`)
        # is documentation, not a use (refinement, 2026-06-16).
        code_no_str = re.sub(r'"[^"]*"|\'[^\']*\'', "", code_part)
        if any(v in code_no_str for v in found):
            usage_lines.append((i, code_part))

    # The IMPORT line itself doesn't count as usage.
    is_only_import = all(
        re.match(r"\s*(from|import)\b", line) is not None
        for _, line in usage_lines
    )
    if is_only_import:
        row["result"] = "imported_unused"
        return row

    # Classify each non-import usage line.
    # Two-step comparison (refinement, 2026-06-16): an anchor aliased to a
    # local (`m_p = mp.mpf(str(M_P_MEV_VALIDATION))`) whose local is later
    # used in a comparison is comparison-reference, not a derivation input.
    # Collect pure-alias assignments (RHS is ONLY the anchor + conversions,
    # no arithmetic), then mark those whose alias var appears in a comparison.
    alias_vars: dict[str, int] = {}
    for n, line in usage_lines:
        am = re.match(r"\s*([A-Za-z_]\w*)\s*=\s*(.+)$", line)
        if not am:
            continue
        lhs, rhs = am.group(1), am.group(2)
        core = rhs
        for v in found:
            core = core.replace(v, "")
        core = re.sub(r"(?:mpmath\.mpf|mp\.mpf|mpf|float|str|Decimal)\s*\(",
                      "(", core)
        core = re.sub(r"[()\s]", "", core)
        if core == "":  # RHS was only the anchor wrapped in conversions
            alias_vars[lhs] = n
    compared_aliases: set[str] = set()
    for line in lines:
        for var in alias_vars:
            if re.search(rf"\b{re.escape(var)}\b", line) and any(
                ind in line for ind in COMPARISON_LINE_INDICATORS
            ):
                compared_aliases.add(var)

    violation_lines: list[int] = []
    comparison_lines: list[int] = []
    for n, line in usage_lines:
        if re.match(r"\s*(from|import)\b", line):
            continue
        # Comparison-context, recording/display, or two-step alias-to-comparison?
        is_ok = (
            any(ind in line for ind in COMPARISON_LINE_INDICATORS)
            or any(
                m.group(1) in found for m in COMPARISON_KW_PATTERN.finditer(line)
            )
            or any(ind in line for ind in RECORDING_INDICATORS)
            or DICT_VALUE_RX.search(line)  # `"key": str(M_X_VALIDATION)` roster
        )
        if not is_ok:
            am = re.match(r"\s*([A-Za-z_]\w*)\s*=", line)
            if (am and am.group(1) in compared_aliases
                    and alias_vars.get(am.group(1)) == n):
                is_ok = True  # this is the alias-assignment; alias is compared
        if is_ok:
            comparison_lines.append(n)
        else:
            violation_lines.append(n)

    row["comparison_lines"] = comparison_lines[:10]
    row["violation_lines"] = violation_lines[:10]
    row["violation_count"] = len(violation_lines)

    if has_banner:
        row["result"] = "ok_acknowledged_anchor"
    elif not violation_lines:
        row["result"] = "ok_comparison_only"
    else:
        row["result"] = "i11_violation"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    rows: list[dict[str, Any]] = []
    # Scan the compute tree (HERE.parent = computations/), not just audits/.
    # Post-reorg HERE.glob saw only audits/ — missing the compute tree and
    # false-flagging sibling audits (which legitimately import validation
    # constants to police them). Skip _deprecated and the audits/ dir.
    for py in sorted((HERE.parent).rglob("*.py")):
        if "_deprecated" in py.parts or HERE.name in py.parts:
            continue
        if py.name.startswith("_"):
            continue
        if py.name == "codata_constants.py":
            continue
        if py.name == "validation_as_input_audit.py":
            continue
        result = _classify_script(py)
        if result is None:
            continue
        rows.append(result)

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I11 audit — CODATA _VALIDATION constants as production inputs")
    print(f"({len(rows)} scripts import a validation constant)")
    print("=" * 80)
    for cls in ("i11_violation", "ok_acknowledged_anchor",
                "ok_comparison_only", "imported_unused"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} scripts)")
        for r in rs[:10]:
            extras = ""
            if "violation_lines" in r and r["violation_lines"]:
                extras = f"  violations at lines {r['violation_lines'][:5]}"
            print(f"    {r['path']:<70s}{extras}")
        if len(rs) > 10:
            print(f"    … and {len(rs) - 10} more")
    print()
    print(f"Summary:")
    print(f"  total scripts auditing validation constants: {len(rows)}")
    print(f"  i11_violation:                                {len(buckets.get('i11_violation', []))}")
    print(f"  ok_acknowledged_anchor:                       {len(buckets.get('ok_acknowledged_anchor', []))}")
    print(f"  ok_comparison_only:                           {len(buckets.get('ok_comparison_only', []))}")
    print(f"  imported_unused:                              {len(buckets.get('imported_unused', []))}")

    b = (
        WitnessBuilder("validation-as-input-audit", engine="python")
        .set_description(
            "I11 audit per local/compute-integration-watcher: scripts that "
            "import M_*_MEV_VALIDATION constants from codata_constants.py "
            "are classified by usage. The validation constants are tagged "
            "'DO NOT USE AS PREDICTION INPUTS' in the source; using them "
            "outside `pred - VAL` / `abs(...)` / `expected=VAL` style "
            "comparison contexts is an I11 violation unless the script's "
            "docstring carries a CLASS-A acknowledged-anchor banner "
            "(typical for the M_N anchor pending Workplan-0b). Per-script "
            "classification surfaces the violation queue for follow-up."
        )
        .set_content_block(
            "I11 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("total_scripts", len(rows))
        .add_parameter("validation_constants_in_scope",
                       list(VALIDATION_CONSTANTS))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", rows)
        .add_assertion(
            name="no_i11_violations",
            computed=1.0 if "i11_violation" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no script uses _VALIDATION as a prediction input)",
            source="Closure gate: every script using a _VALIDATION constant "
                   "either uses it only as comparison target or carries an "
                   "explicit CLASS-A acknowledged-anchor banner.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "i11_violation" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
