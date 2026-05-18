"""I3 audit — WIRED-BUT-GUARDED-OFF computation paths.

A production script may import a substrate-pure / canonical
witness AND reference it in a computation, but have the actual
call gated behind `if False:`, an env-var defaulting to off, or
a legacy fallback that silently re-routes around the canonical
path.  The witness then looks wired (passes I2 / I11 checks) but
the production output ignores the canonical input.

The I3 antipattern in `local/compute-integration-watcher`:

  A script's body contains one of:
    - `if False:` / `if 0:`
    - `if not <flag>:` where `<flag>` is hard-coded `False` /
      defaulted to off
    - `if os.environ.get("ENABLE_X", "")` returning empty by
      default — gates a canonical block off
    - A `# TODO` / `# legacy` / `# disabled` marker followed by
      an unreachable block

This audit greps every Python script for these shapes, surfaces
the surrounding 5-line snippet for human triage.

Limitations:
  - Static — does NOT prove the block is dead code; some
    `if False:` may be ergonomic toggles for debug.  The witness
    flags candidates; reviewers decide.
  - The env-var detection is keyword-based: looks for `os.environ.get`
    + `""` / `"0"` / `"false"` default.
  - `# DEAD: ` / `# DISABLED: ` markers count even if the block
    below executes (they're an explicit author signal).

Emits `guarded-off-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/guarded_off_audit.py [--strict]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent

# Pattern catalogue.  Each tuple: (label, regex).
#
# `explicit_skip_block` was dropped after triage (PR follow-up to
# #750): the original regex `^\s*#\s*(?:skip|skipping|kept for
# reference|kept for compat|moved to)` matched benign comments
# mentioning "Skip" (e.g. "# Skip per-term sp.cancel: too slow",
# "# SKIP_TRACE=1 to produce a witness ...").  These weren't real
# guarded-off blocks; they were explanatory prose.  Real
# wired-but-guarded-off blocks are now captured by the four
# remaining patterns below.
GUARD_RX = (
    ("if_false_literal",
     re.compile(r'^\s*if\s+(?:False|0)\s*:')),
    ("if_not_true_literal",
     re.compile(r'^\s*if\s+not\s+(?:True|1)\s*:')),
    ("env_var_off_default",
     re.compile(
         r'os\.environ\.get\s*\(\s*[\'"][^\'"]+[\'"]\s*,\s*[\'"](?:|0|false|False|FALSE)[\'"]'
     )),
    ("dead_disabled_marker",
     re.compile(r'^\s*#\s*(?:DEAD|DISABLED|UNUSED|LEGACY|OBSOLETE|DEPRECATED):',
                re.IGNORECASE)),
)


def _classify_script(path: Path) -> dict[str, Any] | None:
    """Audit one Python script for I3 guard shapes."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "import" not in text:
        return None

    lines = text.splitlines()
    hits: list[dict[str, Any]] = []
    for i, line in enumerate(lines, start=1):
        # Skip lines explicitly triaged with `# noqa: I3 — <reason>`.
        if re.search(r'#\s*noqa:\s*I3\b', line, re.IGNORECASE):
            continue
        for label, rx in GUARD_RX:
            if rx.search(line):
                # Capture ±2 lines for context.
                start = max(0, i - 2)
                end = min(len(lines), i + 2)
                hits.append({
                    "line_number": i,
                    "pattern": label,
                    "snippet": "\n".join(lines[start:end])[:300],
                })
                break  # one pattern match per line is enough

    if not hits:
        return None

    rel = path.relative_to(REPO_ROOT)
    return {
        "path": str(rel),
        "hit_count": len(hits),
        "hits": hits[:15],
        "result": "i3_candidate",
    }


def main() -> int:
    strict = "--strict" in sys.argv

    rows: list[dict[str, Any]] = []
    for py in sorted(HERE.glob("*.py")):
        if py.name.startswith("_"):
            continue
        if py.name == "guarded_off_audit.py":
            continue
        result = _classify_script(py)
        if result is None:
            continue
        rows.append(result)

    rows.sort(key=lambda r: -r["hit_count"])

    print("=" * 80)
    print(f"I3 audit — wired-but-guarded-off computations  ({len(rows)} scripts)")
    print("=" * 80)
    for r in rows[:20]:
        print(f"  {r['path']:<70s}  {r['hit_count']} hit(s)")
    if len(rows) > 20:
        print(f"  … and {len(rows) - 20} more")
    print()
    print(f"Summary:")
    print(f"  scripts with guard-shape hits:    {len(rows)}")
    print(f"  total guard-shape lines flagged:  {sum(r['hit_count'] for r in rows)}")

    b = (
        WitnessBuilder("guarded-off-audit", engine="python")
        .set_description(
            "I3 audit per local/compute-integration-watcher: scripts that "
            "contain `if False:` / `if 0:` blocks, env-var-defaulting-to-off "
            "gates, or explicit `# DEAD`/`# DISABLED`/`# LEGACY` markers "
            "where a canonical-witness consumer may have been disabled.  "
            "Candidates only — review the per-line context to confirm the "
            "block actually wraps a canonical-path call (vs being a debug "
            "toggle / leftover scaffolding)."
        )
        .set_content_block(
            "I3 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("scripts_with_hits", len(rows))
        .add_parameter("total_guard_lines_flagged",
                       sum(r["hit_count"] for r in rows))
        .add_data("rows", rows)
        .add_assertion(
            name="no_guarded_off_candidates",
            computed=1.0 if not rows else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no script contains guarded-off shapes)",
            source="Closure gate: when this passes, every canonical-witness "
                   "consumer runs unconditionally (or behind a gate the "
                   "watcher has explicitly approved).",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and rows:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
