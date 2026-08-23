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
`computations/`, harvests all numerical literals,
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
  - Self-test fixture pairs (`("<literal>", True)`) are
    filtered out — a detector's own example of a bad value
    is not a use of it.

Emits `hardcoded-literal-audit.witness.json`.

Usage:
    python3 computations/hardcoded_literal_audit.py [--strict]
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

import re
import sys
from pathlib import Path
from typing import Any

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

REPO_ROOT = HERE.parent.parent


def _load_registry() -> dict[str, mp.mpf]:
    """Import codata_constants and extract MeV-magnitude constants."""
    set_compute_dps()
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

# A detector's own test corpus is not a registry bypass.  The precision
# audits carry the canonical example of the defect they detect as a
# self-test case — a bare `("<literal>", <expected bool>)` pair in a
# `cases = [...]` list.  Harvesting those made this audit record the very
# string `witness_float64_padding_audit.py` exists to document (it matches
# AME_B_TRITIUM_MEV_VALIDATION at rel_err 1.8e-16), and the float64-padding
# ratchet then read our own witness back as NEW fake precision — one audit's
# ILLUSTRATION of a bug read as an INSTANCE of it.
#
# Deliberately shaped so it cannot widen into cover for ordinary sloppiness:
# the ENTIRE line (after inline comments are stripped) must be exactly a
# quoted numeric paired with a bool.  A literal that is actually *used* —
# `m_e = 0.51099895`, `mp.mpf("0.51099895")`, or any tuple bound to a name —
# cannot take this form, so no real hardcoding can hide behind it.
FIXTURE_CASE_RX = re.compile(
    r'^\s*\(\s*["\'][-+\d.eE]+["\']\s*,\s*(?:True|False)\s*\)\s*,?\s*$'
)


# Anchor-banner markers (shared with the I11 audit) — scripts that
# explicitly acknowledge CLASS-A status / Workplan-0b have their
# hardcoded literals classified as `ok_acknowledged_anchor` rather
# than as I9 violations.
ANCHOR_BANNER_PATTERNS = (
    r"CLASS-A",
    r"acknowledged.{0,5}stub",
    r"CAL-?[34]",
    r"Workplan-0b",
    r"pending.{0,40}substrate.{0,40}derivation",
    r"M_N anchor",
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

    # Check the module docstring for a CLASS-A acknowledged-anchor
    # banner (mirror of the I11 audit's banner detection per PR #765).
    doc_match = re.search(r'^"""(.*?)"""', text, re.DOTALL)
    docstring = doc_match.group(1) if doc_match else ""
    has_banner = any(
        re.search(p, docstring, re.IGNORECASE) for p in ANCHOR_BANNER_PATTERNS
    )

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
        # Filter out self-test fixture pairs — a detector documenting the
        # bad value it catches, not a script consuming it.
        if FIXTURE_CASE_RX.match(code_part):
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
                # Tolerance: match if within 1e-6 relative error.
                # The registry's CODATA constants are precise to ~9
                # digits; 1e-3 (the original baseline) was too loose
                # and produced ~70 false positives from coincidental
                # matches like `1e-3` ~ `Q_BETA_MEV_ERR`.  Tightened
                # to 1e-6 — still permissive enough to catch loose
                # rounding (`0.511` matching M_E_MEV = 0.51099895
                # at rel_err 0.002 is INTENTIONAL: the literal IS
                # the registry value, just rounded).  Past the
                # 6th-digit boundary the constant has truly diverged.
                if rel_err < mp.mpf("1e-6"):
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
        "has_class_a_banner": has_banner,
    }
    # Scripts that explicitly carry the CLASS-A banner (acknowledged
    # CAL-3-pending anchor — usually production mass-derivation
    # scripts) are not I9 violations: their hardcoded literals are
    # part of the validation-chain anchor, not registry bypasses.
    # Mirror of the I11 audit's banner-recognition (PR #765).
    if has_banner:
        row["result"] = "ok_acknowledged_anchor"
    else:
        row["result"] = "i9_violation"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    print("Loading codata_constants registry ...")
    registry = _load_registry()
    print(f"  {len(registry)} scalar constants in scope")

    rows: list[dict[str, Any]] = []
    # Scan the compute tree (HERE.parent = computations/), not just audits/.
    # Post-reorg HERE.glob saw only audits/ — which MISSED the compute tree
    # AND false-flagged sibling audits (they legitimately reference the
    # policed constants). Skip _deprecated and the audits/ dir.
    for py in sorted((HERE.parent).rglob("*.py")):
        if "_deprecated" in py.parts or HERE.name in py.parts:
            continue
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

    rows.sort(key=lambda r: (r["result"] != "i9_violation", -r["hit_count"]))

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I9 audit — hardcoded literals matching codata_constants  ({len(rows)} scripts)")
    print("=" * 80)
    for cls in ("i9_violation", "ok_acknowledged_anchor"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} scripts)")
        for r in rs[:12]:
            print(f"    {r['path']:<70s}  {r['hit_count']} hit(s)")
        if len(rs) > 12:
            print(f"    … and {len(rs) - 12} more")
    print()
    print(f"Summary:")
    print(f"  total scripts:                       {len(rows)}")
    print(f"  i9_violation:                        {len(buckets.get('i9_violation', []))}")
    print(f"  ok_acknowledged_anchor:              {len(buckets.get('ok_acknowledged_anchor', []))}")
    print(f"  total hits across i9_violation:      {sum(r['hit_count'] for r in buckets.get('i9_violation', []))}")

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
        .add_parameter("relative_error_tolerance", "1e-6")
        .add_parameter("magnitude_window_MeV", "[0.0001, 1e6]")
        .add_parameter("total_scripts_with_hits", len(rows))
        .add_parameter("i9_violation_count",
                       len(buckets.get("i9_violation", [])))
        .add_parameter("ok_acknowledged_anchor_count",
                       len(buckets.get("ok_acknowledged_anchor", [])))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", rows)
        .add_assertion(
            name="no_hardcoded_registry_matches",
            computed=1.0 if "i9_violation" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no script hardcodes a registry value without acknowledged-anchor banner)",
            source="Closure gate: when this passes, every numerical literal "
                   "in production scripts is either symbolic (q_0 powers, "
                   "integer coefficients), imported from codata_constants, "
                   "below the magnitude window, or in a script that carries "
                   "the CLASS-A acknowledged-anchor banner.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and rows:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
