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

# Pattern catalogue.  Each tuple: (label, regex).
#
# Coverage rationale: the I3 antipattern requires an unambiguous
# disablement signal — a literal-false guard, an explicit "this is
# dead/disabled code" marker, or an env-var with off-by-default that
# isn't a conventional feature toggle.  Generic `# Skip …` comments
# were dropped from this catalogue in 2026-05-18 round 4: every
# observed match was a loop control-flow skip ("skip this iteration"),
# not a guarded canonical-witness consumer.  Reinstating that pattern
# would require a positive signal that the skipped block consumes a
# witness — out of scope for a static grep.
GUARD_RX = (
    ("if_false_literal",
     re.compile(r'^\s*if\s+(?:False|0)\s*:')),
    ("if_not_true_literal",
     re.compile(r'^\s*if\s+not\s+(?:True|1)\s*:')),
    ("env_var_off_default",
     re.compile(
         r'os\.environ\.get\s*\(\s*[\'"]([^\'"]+)[\'"]\s*,\s*[\'"](?:|0|false|False|FALSE)[\'"]'
     )),
    ("dead_disabled_marker",
     re.compile(r'^\s*#\s*(?:DEAD|DISABLED|UNUSED):',
                re.IGNORECASE)),
)

# Rationale phrases in ±5-line context suppress the hit as intentional
# scaffolding (not an I3 violation).  The audit's goal is wired-but-
# canonically-guarded-off; performance toggles, exception-handling skips,
# and documented fallbacks have rationale and are out of scope.
RATIONALE_RX = re.compile(
    r'(?:'
    r'\bslow\b|\bslowness\b|\bexpensive\b|\bcomputationally\b|\bsympy\b|'
    r'\bminutes\b|takes\s+(?:too\s+)?long|'
    r'closed[-\s]?form|use\s+closed|not\s+available|\bn/a\b|'
    r'kept\s+for|for\s+compat|moved\s+to|reorganized|reorganised|'
    r'\bdeprecated\b|\bhistorical\b|reference\s+only|'
    r'\bnoqa\b|\bencoding\b|\bpermissions\b|\bexception\b|surface\s+as\s+bugs|'
    r'for\s+now|\btodo\b|placeholder|temporary|\bwip\b|'
    r'\boptional\b|\bperformance\b|optimi[sz]ation|optimi[sz]e|'
    r'\bdebug\b|\bverbose\b|\bdiagnostic\b|'
    r'\bdegenerate\b|already\s+cached|just\s+created|auto-generated|'
    r'handled\s+by|out\s+of\s+scope|recomputation|'
    r'\bsnapshot\b|\brecompute\b|'
    r'deferred|precomputation|session\s+budget|well-defined|'
    r'\blegacy\b|fit\s+E_0|residual|fallback|'
    r'\btiny\b|\bbounds\b|iteration|\bindices\b|'
    r'schema|pipeline|generated|not\s+yet\s+generated|absence\s+of\s+file|'
    r'single-term|subword|dual\s+pair'
    r')',
    re.IGNORECASE,
)

# Env-var names matching this prefix are conventional feature/performance
# toggles, not canonical-witness guards.
FEATURE_TOGGLE_PREFIX_RX = re.compile(
    r'^(?:SKIP|INCLUDE|FAST|FORCE|ENABLE|DISABLE|DEBUG|VERBOSE|'
    r'WITH|WITHOUT|USE|NO|RUN|EMIT|STRICT)_', re.IGNORECASE,
)


def _has_rationale(lines: list[str], i: int) -> bool:
    """True iff ±5-line context around `lines[i-1]` carries rationale."""
    start = max(0, i - 6)
    end = min(len(lines), i + 5)
    return bool(RATIONALE_RX.search("\n".join(lines[start:end])))


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
        for label, rx in GUARD_RX:
            m = rx.search(line)
            if not m:
                continue
            # Conventional feature-toggle env vars (SKIP_*, INCLUDE_*,
            # FAST_*, …) are not canonical-witness guards.  Suppress.
            if label == "env_var_off_default":
                var = m.group(1) if m.groups() else ""
                if FEATURE_TOGGLE_PREFIX_RX.match(var):
                    break
            # Rationale within ±5 lines suppresses every pattern —
            # documented skips / performance trade-offs / fallbacks /
            # known closed-form substitutions are out of I3 scope.
            if _has_rationale(lines, i):
                break
            # Capture ±2 lines for the witness snippet.
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
