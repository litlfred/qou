"""I7 audit — witness staleness vs content-block `.md` modification time.

For every `folio-assistant/computations/*.witness.json` with a
label-shaped `contentBlock` (matching `def:` / `thm:` / `prop:`
/ `lem:` / `cor:` / `conj:`), locates the corresponding
`.md` content-block file and compares the git-log timestamp of
the latest `.md` modification against the witness's own latest
modification.

A witness is "stale" if its content-block `.md` was modified
more recently than the witness was regenerated.  The threshold
defaults to 7 days (matching the I7 catalogue text in
`local/compute-integration-watcher`).

This is the I7 audit promised by the
`local/compute-integration-watcher` skill's pattern catalogue
("PROBE STALE > 7 DAYS BEHIND BLOCK .md"), operationalising the
86-hit count from the 2026-05-18 idle sweep
([PR #737](https://github.com/litlfred/qou/pull/737)).

Failure modes classified:

  - `ok`              — witness modified after .md, or within
                        threshold
  - `stale`           — .md modified > THRESHOLD days after the
                        witness's last commit
  - `md_missing`      — `contentBlock` points at a label whose
                        .md cannot be located (likely I5
                        territory; reported as info)

Usage:
    python3 folio-assistant/computations/stale_probe_audit.py [--strict]

With --strict, exits non-zero if any `stale` entry is observed.
Without --strict (default), returns 0 and reports the breakdown.
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
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent
CONTENT_ROOT = REPO_ROOT / "content"

STALE_DAYS_THRESHOLD = 7

LABEL_PREFIXES = ("def:", "thm:", "lem:", "prop:", "cor:", "conj:")
LABEL_RX = re.compile(r'label:\s*"([^"]+)"')


def _git_log_mtime(path: Path) -> int | None:
    """Return committer-time of the latest commit touching `path`,
    as a UNIX timestamp.  None if not in git or never committed."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0 and out.stdout.strip():
            return int(out.stdout.strip())
    except (subprocess.SubprocessError, OSError, ValueError):
        pass
    return None


def _build_label_index() -> dict[str, Path]:
    """Map every label to its .md sibling path."""
    index: dict[str, Path] = {}
    for ts in CONTENT_ROOT.rglob("*.ts"):
        rel = ts.relative_to(CONTENT_ROOT)
        if rel.parts[0] in ("schema", "pipeline"):
            continue
        if ts.name.endswith(".d.ts"):
            continue
        try:
            text = ts.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        m = LABEL_RX.search(text)
        if not m:
            continue
        label = m.group(1)
        md = ts.with_suffix(".md")
        if md.exists():
            index[label] = md
    return index


def _audit_witness(path: Path,
                   label_index: dict[str, Path]) -> list[dict[str, Any]]:
    """Audit one witness file's staleness vs its content-block .md."""
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return []

    cb = d.get("contentBlock")
    if cb is None:
        return []

    candidates = [cb] if isinstance(cb, str) else (cb if isinstance(cb, list) else [])
    candidates = [c.strip() for c in candidates if isinstance(c, str)]

    label_candidates = [
        c for c in candidates
        if any(c.startswith(p) for p in LABEL_PREFIXES) and " " not in c
    ]
    if not label_candidates:
        return []  # informational contentBlock; skip per I5 audit

    rows: list[dict[str, Any]] = []
    witness_mtime = _git_log_mtime(path)
    if witness_mtime is None:
        # Witness not in git or untracked; skip — drift policy
        # requires git-committed witnesses.
        return []

    for label in label_candidates:
        md = label_index.get(label)
        rel_witness = path.relative_to(REPO_ROOT)
        row: dict[str, Any] = {
            "witness": str(rel_witness),
            "label": label,
            "witness_mtime_unix": witness_mtime,
        }
        if md is None:
            row["result"] = "md_missing"
            rows.append(row)
            continue

        md_mtime = _git_log_mtime(md)
        if md_mtime is None:
            row["result"] = "md_missing"
            rows.append(row)
            continue

        row["md"] = str(md.relative_to(REPO_ROOT))
        row["md_mtime_unix"] = md_mtime
        delta_days = (md_mtime - witness_mtime) / 86400.0
        row["md_minus_witness_days"] = round(delta_days, 2)

        if delta_days > STALE_DAYS_THRESHOLD:
            row["result"] = "stale"
        else:
            row["result"] = "ok"
        rows.append(row)
    return rows


def main() -> int:
    strict = "--strict" in sys.argv

    print(f"Building label → .md index ...")
    label_index = _build_label_index()
    print(f"  indexed {len(label_index)} labels")

    all_rows: list[dict[str, Any]] = []
    for w in sorted(HERE.glob("*.witness.json")):
        if w.name == "stale-probe-audit.witness.json":
            continue
        all_rows.extend(_audit_witness(w, label_index))

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in all_rows:
        buckets.setdefault(r["result"], []).append(r)

    # Sort stale buckets by lateness (most stale first).
    if "stale" in buckets:
        buckets["stale"].sort(key=lambda r: -r.get("md_minus_witness_days", 0))

    print("=" * 80)
    print(f"I7 audit — witness staleness vs .md  ({len(all_rows)} fields)")
    print("=" * 80)
    for cls in ("stale", "ok", "md_missing"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} fields)")
        for r in rs[:12]:
            days = r.get("md_minus_witness_days", "—")
            print(f"    {r['witness']:<70s} {r['label']:<50s} {days:>6} d")
        if len(rs) > 12:
            print(f"    … and {len(rs) - 12} more")
    print()
    print(f"Summary:")
    print(f"  total fields audited:          {len(all_rows)}")
    print(f"  ok (within {STALE_DAYS_THRESHOLD}d threshold): {len(buckets.get('ok', []))}")
    print(f"  stale (>{STALE_DAYS_THRESHOLD}d behind .md):  {len(buckets.get('stale', []))}")
    print(f"  md_missing (label has no .md):  {len(buckets.get('md_missing', []))}")

    b = (
        WitnessBuilder("stale-probe-audit", engine="python")
        .set_description(
            "I7 audit per local/compute-integration-watcher: every "
            "folio-assistant/computations/*.witness.json with a label-shaped "
            "`contentBlock` is cross-checked against the git-log mtime of its "
            "`.md` sibling.  A witness is stale if its `.md` was modified "
            f">{STALE_DAYS_THRESHOLD} days after the witness was last "
            "committed.  Operationalises the 86-hit I7 count from the "
            "2026-05-18 idle sweep (PR #737)."
        )
        .set_content_block(
            "I7 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("stale_threshold_days", STALE_DAYS_THRESHOLD)
        .add_parameter("total_fields_audited", len(all_rows))
        .add_parameter("registered_labels_count", len(label_index))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", all_rows)
        .add_assertion(
            name="no_stale_probes",
            computed=1.0 if "stale" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no probe witness > threshold days behind .md)",
            source="Closure gate: when this passes, every label-shaped "
                   "witness is current with its content-block .md.  "
                   "Currently informational; the production-side fix is "
                   "rerunning each stale probe's producer.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "stale" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
