"""I10 audit (heuristic) — legacy formula competing with canonical.

A production script may carry a legacy formula side-by-side with a
canonical-derived formula, with both still callable.  Reviewers
can't tell from a grep alone which one the script actually uses
for its published witness output — and historical patterns show
the legacy path often wins (silent re-route).

The I10 antipattern in `local/compute-integration-watcher`:

  A script defines two functions / blocks for the same physical
  quantity, where one is marked `_legacy` / `_old` / `_v1` /
  `_pre_*` / `_deprecated` / has a `# LEGACY` / `# DEPRECATED`
  banner, AND the canonical sibling exists in the same module.
  Both being CALLABLE is the violation — only one should remain
  reachable from the main entry point.

This audit is HEURISTIC:

  1. Grep function-name suffixes for legacy markers.
  2. Look for a sibling canonical-named function in the same
     module (same stem, no suffix).
  3. Check whether both are referenced from the script body
     (not just the legacy one in a `# kept for reference` block).

False positives:
  - Audit / test scripts that compare a legacy to a canonical
    BY DESIGN (e.g. cross-validation).  The witness flags these;
    reviewers apply a `# noqa: I10` mark.
  - Pure-rename refactors where the `_legacy` name is still
    imported elsewhere but the script itself doesn't call it.

Emits `legacy-formula-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/legacy_formula_audit.py [--strict]
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent

# Function-name suffix markers indicating legacy / superseded form.
LEGACY_SUFFIXES = (
    "_legacy", "_old", "_v1", "_v0", "_pre_canonical",
    "_deprecated", "_orig", "_original", "_first",
)

# Banner markers immediately above a `def` block.
LEGACY_BANNER_RX = re.compile(
    r'^\s*#\s*(?:LEGACY|DEPRECATED|OBSOLETE|SUPERSEDED|OLD)\b',
    re.IGNORECASE | re.MULTILINE,
)

DEF_RX = re.compile(r'^\s*def\s+(\w+)\s*\(', re.MULTILINE)


def _strip_legacy_suffix(name: str) -> str | None:
    """Return the canonical stem if name has a legacy suffix, else None."""
    for sfx in LEGACY_SUFFIXES:
        if name.endswith(sfx):
            return name[: -len(sfx)]
    return None


def _classify_script(path: Path) -> dict[str, Any] | None:
    """Audit one Python script for I10 patterns."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "def " not in text:
        return None

    # Collect all top-level `def`s + their line numbers.
    defs: list[tuple[int, str]] = []
    for m in DEF_RX.finditer(text):
        lineno = text[: m.start()].count("\n") + 1
        defs.append((lineno, m.group(1)))

    def_names = {name for _, name in defs}

    # Strategy 1 — suffix-named legacies with a canonical sibling.
    suffix_hits: list[dict[str, Any]] = []
    for lineno, name in defs:
        canonical = _strip_legacy_suffix(name)
        if canonical and canonical in def_names:
            # Both exist.  Check if both are CALLED from elsewhere.
            legacy_call_count = len(
                re.findall(rf'\b{re.escape(name)}\s*\(', text)
            )
            canonical_call_count = len(
                re.findall(rf'\b{re.escape(canonical)}\s*\(', text)
            )
            # Subtract definitions themselves (`def name(`).
            legacy_call_count = max(0, legacy_call_count - 1)
            canonical_call_count = max(0, canonical_call_count - 1)
            if legacy_call_count > 0 and canonical_call_count > 0:
                suffix_hits.append({
                    "legacy_name": name,
                    "legacy_def_line": lineno,
                    "canonical_name": canonical,
                    "legacy_call_count": legacy_call_count,
                    "canonical_call_count": canonical_call_count,
                })
            elif legacy_call_count > 0:  # legacy only, no canonical caller
                suffix_hits.append({
                    "legacy_name": name,
                    "legacy_def_line": lineno,
                    "canonical_name": canonical,
                    "legacy_call_count": legacy_call_count,
                    "canonical_call_count": 0,
                    "note": "legacy still called, canonical defined-but-unused",
                })

    # Strategy 2 — banner markers above a def.
    banner_hits: list[dict[str, Any]] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if LEGACY_BANNER_RX.match(line):
            # Look ahead for the next non-comment line — is it a def?
            for j in range(i + 1, min(i + 4, len(lines))):
                m = re.match(r'\s*def\s+(\w+)\s*\(', lines[j])
                if m:
                    banner_hits.append({
                        "marker_line": i + 1,
                        "banner": line.strip()[:80],
                        "def_line": j + 1,
                        "def_name": m.group(1),
                    })
                    break

    if not suffix_hits and not banner_hits:
        return None

    rel = path.relative_to(REPO_ROOT)
    return {
        "path": str(rel),
        "suffix_hits": suffix_hits,
        "banner_hits": banner_hits,
        "total_signals": len(suffix_hits) + len(banner_hits),
        "result": (
            "i10_violation"
            if any(
                h.get("legacy_call_count", 0) > 0
                and h.get("canonical_call_count", 0) > 0
                for h in suffix_hits
            )
            else "i10_candidate"
        ),
    }


def main() -> int:
    strict = "--strict" in sys.argv

    rows: list[dict[str, Any]] = []
    for py in sorted(HERE.glob("*.py")):
        if py.name.startswith("_"):
            continue
        if py.name == "legacy_formula_audit.py":
            continue
        result = _classify_script(py)
        if result is None:
            continue
        rows.append(result)

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I10 audit — legacy formula competing with canonical (heuristic)")
    print("=" * 80)
    for cls in ("i10_violation", "i10_candidate"):
        rs = sorted(buckets.get(cls, []), key=lambda r: -r["total_signals"])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} scripts)")
        for r in rs[:12]:
            sh = len(r["suffix_hits"])
            bh = len(r["banner_hits"])
            print(f"    {r['path']:<70s}  suffix={sh}, banner={bh}")
        if len(rs) > 12:
            print(f"    … and {len(rs) - 12} more")
    print()
    print(f"Summary:")
    print(f"  i10_violation (both forms still called):  {len(buckets.get('i10_violation', []))}")
    print(f"  i10_candidate (markers found, triage):    {len(buckets.get('i10_candidate', []))}")

    b = (
        WitnessBuilder("legacy-formula-audit", engine="python")
        .set_description(
            "I10 audit (heuristic) per local/compute-integration-watcher: "
            "scripts where a `<name>_legacy` / `_old` / `_v1` / `_v0` / "
            "`_pre_canonical` / `_deprecated` / `_orig` / `_original` / "
            "`_first` function coexists with a canonical sibling (`<name>`), "
            "AND both are still CALLED in the script body.  Strategy 2 also "
            "flags banner-marked defs (`# LEGACY`, `# DEPRECATED`, "
            "`# OBSOLETE`, `# SUPERSEDED`, `# OLD` above a `def`).  Per-script "
            "evidence in `rows[]` lets reviewers triage real I10 violations "
            "from intentional A/B cross-validation scripts."
        )
        .set_content_block(
            "I10 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("scripts_with_signals", len(rows))
        .add_parameter("i10_violation_count",
                       len(buckets.get("i10_violation", [])))
        .add_parameter("i10_candidate_count",
                       len(buckets.get("i10_candidate", [])))
        .add_data("rows", rows)
        .add_assertion(
            name="no_i10_violations",
            computed=1.0 if "i10_violation" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no script has both legacy + canonical called)",
            source="Closure gate: when this passes, no script keeps a "
                   "legacy formula reachable alongside its canonical "
                   "counterpart.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "i10_violation" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
