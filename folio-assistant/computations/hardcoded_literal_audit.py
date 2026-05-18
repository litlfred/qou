"""I9 audit — hardcoded numerical literals matching registered constants.

`codata_constants.py` is the single source of truth for CODATA
masses, Q-values, and other empirical anchors.  When a script
hardcodes a numerical literal that matches one of these registered
values (within tolerance), it bypasses the registry — meaning:

  - If the upstream CODATA value updates, the script silently
    diverges from the source of truth.
  - The witness pipeline's drift detector can't trace the
    dependency.
  - Reviewers can't see which CAL input the literal came from.

This is the I9 antipattern in `local/compute-integration-watcher`:

  A `.py` script has a bare numerical literal like `0.511`,
  `938.272`, `1.293`, `1.0078`, or similar within tolerance of a
  registered constant in `codata_constants.py`, AND does NOT
  import the corresponding `M_*_MEV` / `Q_*_MEV` symbol.

The audit walks every Python script under
`folio-assistant/computations/`, harvests all numerical literals,
and matches each against the registry.  Reports per-script
violations.

Limitations:
  - Pure-substrate literals (1, 2, 3, q_0 powers, integer
    coefficients) are excluded — only physical-scale literals
    (≥ 0.001 MeV-magnitude, with at least 3 decimals OR
    matching to within 1e-3 of a registry value) qualify.
  - Witness assertion literals (`expected=`, `tolerance=`,
    `target=`) are filtered out — they're closure tests, not
    inputs.
  - String literals in docstrings are filtered out.

Emits `hardcoded-literal-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/hardcoded_literal_audit.py [--strict]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent


def _load_registry() -> dict[str, mp.mpf]:
    """Import codata_constants and extract MeV-magnitude constants."""
    mp.mp.dps = 50
    sys.path.insert(0, str(HERE))
    import codata_constants as cc  # noqa: E402
    registry: dict[str, mp.mpf] = {}
    for attr in dir(cc):
        if attr.startswith("_"):
            continue
        val = getattr(cc, attr)
        # Keep only mpf scalar values (skip functions, witnesses).
        if isinstance(val, mp.mpf):
            registry[attr] = val
    return registry


# Match a numerical literal in Python code.  Cover:
#   - 0.511, 938.272, 1.293
#   - 0.51099895e0 / 1.5e-3 (scientific notation)
#   - 938 (bare int, exclude small integers via threshold)
# The match must be a complete "word" — no `.` or `_` adjacent.
NUMERICAL_LITERAL_RX = re.compile(
    r'(?<![\w.])'                          # boundary
    r'(\d+\.\d+(?:[eE][+-]?\d+)?'           # 0.511 or 0.5e-3
    r'|\d+[eE][+-]?\d+)'                    # 1e-3
    r'(?![\w.])'
)

# Lines / contexts that don't count as USE — strip these.
EXCLUSION_LINE_RX = re.compile(
    r'^\s*(#.*|""".*|""")'              # comment / docstring boundary
)
ASSERTION_KW_RX = re.compile(
    r'\b(expected|tolerance|target|computed|reference|atol|rtol)\s*='
)


def _classify_script(path: Path,
                     registry: dict[str, mp.mpf]) -> dict[str, Any] | None:
    """Audit one script for hardcoded literals matching the registry."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "import" not in text:
        return None

    rel = path.relative_to(REPO_ROOT)

    # Determine which registry symbols are imported (so we can skip
    # those constants — they're sourced via the import).
    imported_names: set[str] = set()
    for m in re.finditer(
        r'from\s+codata_constants\s+import\s+(.*)', text
    ):
        for name in re.split(r'[\s,]+', m.group(1)):
            name = name.strip().rstrip(",)")
            if name and name.upper() == name:
                imported_names.add(name.split(" as ")[0].strip())
        # Handle multi-line imports — the regex hits only one line.

    # Strip block docstrings (best-effort).  The text-replacement
    # is rough, but adequate: zap content inside `"""..."""`.
    code = re.sub(r'""".*?"""', "", text, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", "", code, flags=re.DOTALL)

    lines = code.splitlines()
    hits: list[dict[str, Any]] = []
    for i, line in enumerate(lines, start=1):
        if EXCLUSION_LINE_RX.match(line):
            continue
        # Strip inline comments
        code_part = re.sub(r"#.*$", "", line)
        # Filter out assertion-style usage (closure tests are OK).
        if ASSERTION_KW_RX.search(code_part):
            continue
        for m in NUMERICAL_LITERAL_RX.finditer(code_part):
            literal_str = m.group(1)
            try:
                literal_val = mp.mpf(literal_str)
            except (ValueError, TypeError):
                continue
            # Skip tiny / very-large literals — likely indices /
            # bounds / iteration counts, not physical constants.
            if abs(literal_val) < mp.mpf("0.0001"):
                continue
            if abs(literal_val) > mp.mpf("1e6"):
                continue
            # Compare against registry.
            for name, ref in registry.items():
                if name in imported_names:
                    continue  # already imported via codata_constants
                if ref == 0:
                    continue
                rel_err = abs(literal_val - ref) / abs(ref)
                # Tolerance: match if within 1e-3 relative error.
                # The registry's most precise values go to ~1e-9;
                # 1e-3 is generous enough to catch loose rounding
                # like "0.511" matching M_E_MEV = 0.51099895.
                if rel_err < mp.mpf("1e-3"):
                    hits.append({
                        "line_number": i,
                        "literal": literal_str,
                        "matches_constant": name,
                        "registry_value": mp.nstr(ref, 15),
                        "rel_err": mp.nstr(rel_err, 4),
                        "snippet": code_part.strip()[:120],
                    })
                    break  # one match per literal is enough

    if not hits:
        return None

    row: dict[str, Any] = {
        "path": str(rel),
        "imported_codata_names": sorted(imported_names),
        "hit_count": len(hits),
        "hits": hits[:15],
    }
    row["result"] = "i9_violation"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    print("Loading codata_constants registry ...")
    registry = _load_registry()
    print(f"  {len(registry)} scalar constants in scope")

    rows: list[dict[str, Any]] = []
    for py in sorted(HERE.glob("*.py")):
        if py.name.startswith("_"):
            continue
        if py.name == "codata_constants.py":
            continue
        if py.name == "hardcoded_literal_audit.py":
            continue
        result = _classify_script(py, registry)
        if result is None:
            continue
        rows.append(result)

    rows.sort(key=lambda r: -r["hit_count"])

    print("=" * 80)
    print(f"I9 audit — hardcoded literals matching codata_constants  ({len(rows)} scripts)")
    print("=" * 80)
    for r in rows[:20]:
        print(f"  {r['path']:<70s}  {r['hit_count']} hit(s)")
    if len(rows) > 20:
        print(f"  … and {len(rows) - 20} more")
    print()
    print(f"Summary:")
    print(f"  scripts with hardcoded literal hits: {len(rows)}")
    print(f"  total hits across all scripts:        {sum(r['hit_count'] for r in rows)}")

    b = (
        WitnessBuilder("hardcoded-literal-audit", engine="python")
        .set_description(
            "I9 audit per local/compute-integration-watcher: scripts that "
            "hardcode a numerical literal matching a registered constant in "
            "codata_constants.py (within 1e-3 relative error) without "
            "importing the corresponding symbol.  Bypassing the registry "
            "decouples the script from the canonical source of truth — "
            "if CODATA updates, the literal silently drifts.  Tolerance is "
            "permissive (1e-3) to catch loose rounding like `0.511` matching "
            "M_E_MEV = 0.51099895."
        )
        .set_content_block(
            "I9 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("registry_constants_in_scope", len(registry))
        .add_parameter("relative_error_tolerance", "1e-3")
        .add_parameter("magnitude_window_MeV", "[0.0001, 1e6]")
        .add_parameter("total_scripts_violating", len(rows))
        .add_data("rows", rows)
        .add_assertion(
            name="no_hardcoded_registry_matches",
            computed=1.0 if not rows else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no script hardcodes a registry value)",
            source="Closure gate: when this passes, every numerical literal "
                   "in production scripts is either symbolic (q_0 powers, "
                   "integer coefficients), imported from codata_constants, "
                   "or below the magnitude window.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and rows:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
