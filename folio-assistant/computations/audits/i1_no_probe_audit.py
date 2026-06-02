"""I1 audit — provable blocks with proven Lean but no probe witness.

A `prop:` / `thm:` / `lem:` / `cor:` content block whose `.lean`
sibling builds cleanly (0 sorrys, or §3b-cond conditional-class
opt-out) is mathematically discharged, but its value to the paper
is only realised when a probe witness exercises the claim at q₀
and emits a `*.witness.json` whose `contentBlock` field points at
the block's label.

The I1 antipattern in `local/compute-integration-watcher`:

  A block has `kind ∈ {theorem, proposition, lemma, corollary}`
  AND a sibling `.lean` AND that `.lean` has 0 sorrys, BUT no
  `folio-assistant/computations/*.witness.json` has the block's
  label in its `contentBlock` field.

This audit walks every provable content block and classifies:

  - `wired`             — has a probe witness referencing the
                          label
  - `i1_no_probe`       — Lean is clean but no probe witness
                          exists
  - `i1_pre_lean`       — block kind is provable but no sibling
                          `.lean` (deeper pre-I1 gap)
  - `i1_lean_with_sorry` — sibling `.lean` exists but contains
                          `sorry` (needs proof first; not an I1
                          actionable item — flagged for the
                          proof-integration-watcher)
  - `conditional_class` — §3b-cond conditional-class opt-out
                          (a `sorry` is the class instance; the
                          downstream proof is verified — counted
                          as wired-eligible)

Emits `i1-no-probe-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/i1_no_probe_audit.py [--strict]
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
CONTENT_ROOT = REPO_ROOT / "content"
WITNESS_DIR = HERE

PROVABLE_KINDS = ("theorem", "proposition", "lemma", "corollary")

LABEL_RX = re.compile(r'label:\s*"([^"]+)"')
# Kind is encoded as the builder function name (theorem(...), etc.)
# rather than a `kind:` field; match the export default builder call.
KIND_RX = re.compile(
    r'export\s+default\s+(theorem|proposition|lemma|corollary|definition|conjecture|example|remark|prose|equation|diagram|simulator)\s*\('
)
LEAN_REF_RX = re.compile(
    r'lean:\s*\{[^}]*?ref:\s*"([^:"]+):([^"]+)"', re.DOTALL
)


def _collect_probe_targets() -> dict[str, list[str]]:
    """Walk *.witness.json files; return label → list-of-witness-paths."""
    by_label: dict[str, list[str]] = {}
    for w in sorted(WITNESS_DIR.glob("*.witness.json")):
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        cb = d.get("contentBlock")
        candidates: list[str] = []
        if isinstance(cb, str):
            candidates = [cb]
        elif isinstance(cb, list):
            candidates = [c for c in cb if isinstance(c, str)]
        for c in candidates:
            c = c.strip()
            if c and any(c.startswith(p) for p in
                         ("def:", "thm:", "lem:", "prop:", "cor:", "conj:")):
                by_label.setdefault(c, []).append(w.name)
    return by_label


def _classify_block(ts_path: Path,
                    probe_map: dict[str, list[str]]) -> dict[str, Any] | None:
    """Audit one provable block."""
    try:
        text = ts_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    label_match = LABEL_RX.search(text)
    kind_match = KIND_RX.search(text)
    if not label_match or not kind_match:
        return None
    label = label_match.group(1)
    kind = kind_match.group(1)
    if kind not in PROVABLE_KINDS:
        return None

    rel = ts_path.relative_to(REPO_ROOT)
    row: dict[str, Any] = {
        "path": str(rel),
        "label": label,
        "kind": kind,
    }

    # Check the sibling .lean.
    sibling_lean = ts_path.with_suffix(".lean")
    has_sibling = sibling_lean.exists()
    sorry_count = 0
    has_class = False
    if has_sibling:
        try:
            lean_text = sibling_lean.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            lean_text = ""
        # Strip block comments for accurate sorry counting.
        stripped = re.sub(r"/-.*?-/", "", lean_text, flags=re.DOTALL)
        # Strip line comments.
        stripped = re.sub(r"--.*$", "", stripped, flags=re.MULTILINE)
        sorry_count = len(re.findall(r"\bsorry\b", stripped))
        has_class = bool(re.search(r"^\s*class\s+\w+", stripped, re.MULTILINE))

    row["sibling_lean_exists"] = has_sibling
    row["sibling_sorry_count"] = sorry_count
    row["sibling_has_class"] = has_class

    # Is there a probe witness?
    probes = probe_map.get(label, [])
    row["probe_witness_count"] = len(probes)
    row["probe_witnesses"] = probes[:5]

    # Classify.
    if not has_sibling:
        row["result"] = "i1_pre_lean"
    elif sorry_count > 0 and not has_class:
        # sorry without class — really needs proof, not a probe
        row["result"] = "i1_lean_with_sorry"
    elif sorry_count > 0 and has_class:
        row["result"] = "conditional_class"
        # treat as wired-eligible — still flag if no probe
        if not probes:
            row["result"] = "i1_no_probe_conditional"
    elif probes:
        row["result"] = "wired"
    else:
        row["result"] = "i1_no_probe"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    print("Collecting probe witness targets ...")
    probe_map = _collect_probe_targets()
    print(f"  {len(probe_map)} distinct labels covered by some witness")

    rows: list[dict[str, Any]] = []
    for ts in sorted(CONTENT_ROOT.rglob("*.ts")):
        rel = ts.relative_to(CONTENT_ROOT)
        if rel.parts[0] in ("schema", "pipeline"):
            continue
        if ts.name.endswith(".d.ts"):
            continue
        result = _classify_block(ts, probe_map)
        if result is None:
            continue
        rows.append(result)

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I1 audit — provable blocks vs probe witnesses  ({len(rows)} blocks)")
    print("=" * 80)
    for cls in ("wired", "i1_no_probe", "i1_no_probe_conditional",
                "i1_lean_with_sorry", "i1_pre_lean", "conditional_class"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} blocks)")
        for r in rs[:10]:
            print(f"    {r['label']:<55s}  ({r['path']})")
        if len(rs) > 10:
            print(f"    … and {len(rs) - 10} more")
    print()
    print(f"Summary:")
    print(f"  total provable blocks:     {len(rows)}")
    print(f"  wired (probe exists):      {len(buckets.get('wired', []))}")
    print(f"  i1_no_probe (actionable):  {len(buckets.get('i1_no_probe', []))}")
    print(f"  i1_no_probe_conditional:   {len(buckets.get('i1_no_probe_conditional', []))}")
    print(f"  i1_lean_with_sorry (proof-watcher): {len(buckets.get('i1_lean_with_sorry', []))}")
    print(f"  i1_pre_lean (no .lean yet): {len(buckets.get('i1_pre_lean', []))}")

    b = (
        WitnessBuilder("i1-no-probe-audit", engine="python")
        .set_description(
            "I1 audit per local/compute-integration-watcher: every provable "
            "content block (theorem / proposition / lemma / corollary) is "
            "cross-checked against the union of all witness `contentBlock` "
            "fields.  Blocks with proven Lean (0 sorrys, or class+sorry "
            "via §3b-cond) but no probe witness are flagged as `i1_no_probe`. "
            "Blocks with `sorry` (without conditional-class) belong to the "
            "proof-integration-watcher's queue; blocks without any `.lean` "
            "sibling are `i1_pre_lean` (deeper gap)."
        )
        .set_content_block(
            "I1 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("total_provable_blocks", len(rows))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", rows)
        .add_assertion(
            name="no_i1_no_probe_blocks",
            computed=1.0 if "i1_no_probe" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = every clean-Lean block has a probe witness)",
            source="Closure gate: when this passes, every provable block "
                   "with proven Lean is exercised by a probe at q_0.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "i1_no_probe" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
