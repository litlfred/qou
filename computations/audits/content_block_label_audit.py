"""I5 audit — witness `contentBlock` fields vs registered block labels.

For every `computations/*.witness.json` with a
`contentBlock` field (or list of fields), checks whether each
named label actually appears as a block label registered in some
`content/**/*.ts` manifest.

This is the I5 audit promised by the
`local/compute-integration-watcher` skill's pattern catalogue
("CONTENTBLOCK REFERENCES MISSING LABEL"), operationalising the
9-hit count from the 2026-05-18 idle sweep ([PR #737](https://github.com/litlfred/qou/pull/737)).

A label "resolves" if any `.ts` file under content/ contains the
exact label as a `label: "<value>"` declaration.

Failure modes classified:

  - `ok`                  — label registered in at least one .ts
  - `missing_label`       — label not found in any .ts manifest
  - `informational_label` — `contentBlock` value is descriptive
                             prose, not a label (e.g. starts with
                             a capital, or contains spaces) — info-only

Usage:
    python3 computations/content_block_label_audit.py [--strict]
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

#: The live computations corpus, LOCATED rather than derived by counting
#: `.parent` levels — that count was wrong in both layouts it was written for
#: (bean qou-rug0) and is exactly what breaks when a module moves.
COMPUTATIONS = next(
    (a / "computations" for a in HERE.parents if (a / "computations").is_dir()),
    HERE,
)
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent
CONTENT_ROOT = REPO_ROOT / "content"

LABEL_RX = re.compile(r'label:\s*"([^"]+)"')
LABEL_PREFIXES = ("def:", "thm:", "lem:", "prop:", "cor:", "conj:",
                  "ex:", "rem:", "sim:", "sec:")


def _collect_registered_labels() -> set[str]:
    """Walk content/**/*.ts and collect every `label: "..."` value."""
    labels: set[str] = set()
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
        for m in LABEL_RX.finditer(text):
            labels.add(m.group(1))
    return labels


def _audit_witness(path: Path, registered: set[str]) -> list[dict[str, Any]]:
    """Audit one witness file's contentBlock field(s)."""
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return []

    cb = d.get("contentBlock")
    if cb is None:
        return []

    # Accept either a string or a list.  Witnesses normalise to
    # string but some legacy ones use a list.
    if isinstance(cb, str):
        candidates = [cb]
    elif isinstance(cb, list):
        candidates = [c for c in cb if isinstance(c, str)]
    else:
        return []

    rows: list[dict[str, Any]] = []
    for c in candidates:
        c_clean = c.strip()
        rel = path.relative_to(REPO_ROOT)
        row: dict[str, Any] = {
            "witness": str(rel),
            "content_block_value": c_clean,
        }

        # Detect "informational" descriptive values vs label-shaped
        # ones.  A label starts with a known prefix (def:, thm:, ...)
        # and contains no spaces.
        is_label_shaped = (
            any(c_clean.startswith(p) for p in LABEL_PREFIXES)
            and " " not in c_clean
        )
        if not is_label_shaped:
            row["result"] = "informational_label"
        elif c_clean in registered:
            row["result"] = "ok"
        else:
            row["result"] = "missing_label"
        rows.append(row)
    return rows


def main() -> int:
    strict = "--strict" in sys.argv

    registered = _collect_registered_labels()
    print(f"Registered labels (across content/**/*.ts): {len(registered)}")

    all_rows: list[dict[str, Any]] = []
    # `HERE.glob(...)` — non-recursive, over this module's OWN directory — was
    # auditing 43 of the corpus's 2717 witnesses: 1.6%, reported as a clean
    # bill of health.
    #
    # It was correct when written. `HERE` was `computations/` until the Phase-6
    # subdirectory refactor (2026-06-02) moved this module into `audits/` while
    # the witnesses it audits stayed where they were. The committed witness is
    # stamped 2026-06-01 — the day before — and its 305 rows are what the
    # corpus-wide scan actually saw. Everything since has been a near-empty
    # scan whose output only ever got SMALLER, which read as progress:
    #
    #     2026-06-01   rows=305   ok 248 | missing_label 43 | informational 14
    #     blind        rows= 20   ok   8 | missing_label  1 | informational 11
    #
    # `missing_label` 43 -> 1 is a false improvement, not a drain.
    #
    # Fourth instance of this exact shape in one branch — `_load_chi_witness`
    # globbing its own directory after the same refactor, `witness.py`'s
    # check-all globbing the installed package directory, the lowercase-only
    # vendor scraper matching a truncated fragment — and it is the rule
    # `witness_shape_guard`'s own preamble states: A CHECK WHOSE SUCCESS
    # CONDITION IS SATISFIED BY THE EMPTY STATE IS NOT A CHECK.
    #
    # `COMPUTATIONS`, located rather than assumed, and `rglob` so a future move
    # of either this module or the witnesses cannot silently narrow it again.
    # `_deprecated` excluded, matching every other consumer in the family.
    witness_dir = COMPUTATIONS
    for w in sorted(witness_dir.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        if w.name == "content-block-label-audit.witness.json":
            continue  # don't audit ourselves
        all_rows.extend(_audit_witness(w, registered))

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in all_rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I5 audit — witness contentBlock labels  ({len(all_rows)} fields)")
    print("=" * 80)
    for cls, rs in sorted(buckets.items(), key=lambda x: -len(x[1])):
        print(f"\n  {cls}  ({len(rs)} fields)")
        for r in rs[:10]:
            print(f"    {r['witness']}  →  {r['content_block_value']}")
        if len(rs) > 10:
            print(f"    … and {len(rs) - 10} more")
    print()
    print(f"Summary:")
    print(f"  total witnesses with contentBlock:    {len(all_rows)}")
    print(f"  ok (label resolves):                  {len(buckets.get('ok', []))}")
    print(f"  missing_label (needs fix):            {len(buckets.get('missing_label', []))}")
    print(f"  informational_label (descriptive):    {len(buckets.get('informational_label', []))}")

    b = (
        WitnessBuilder("content-block-label-audit", engine="python")
        .set_description(
            "I5 audit per local/compute-integration-watcher: every "
            "computations/*.witness.json with a `contentBlock` "
            "field is cross-checked against the union of all "
            "`label: \"...\"` declarations in content/**/*.ts manifests. "
            "Reports `ok` / `missing_label` / `informational_label` per "
            "field. Operationalises the 9-hit I5 count from the "
            "2026-05-18 idle sweep (PR #737)."
        )
        .set_content_block(
            "I5 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("total_fields_audited", len(all_rows))
        .add_parameter("registered_labels_count", len(registered))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", all_rows)
        .add_assertion(
            name="no_missing_labels",
            computed=1.0 if "missing_label" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = every label-shaped contentBlock resolves)",
            source="Closure gate: when this passes, every witness's "
                   "contentBlock points at a real registered block label.  "
                   "Currently informational; the production-side fix is "
                   "a per-witness retarget.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "missing_label" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
