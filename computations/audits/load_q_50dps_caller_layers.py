#!/usr/bin/env python3
"""load_q_50dps_caller_layers.py — which q₀ layer each `load_q_50dps()` caller
now resolves, after the 2026-08-08 default flip.

CONTEXT
    `_li_2_q_util.load_q_50dps()` used to default to the **muon** pinning
    witness for every caller. Owner decision 2026-08-08: the default is now the
    **caller's own resolved pin** (`q_parameter.Q`), with `layer="muon"` as the
    explicit escape for deliberate cross-anchor comparison probes.

    So a no-arg call now resolves MUON iff the calling producer's stem is
    declared `ideal_muon` in `q0_anchor_manifest.json` (or `QOU_Q0_ANCHOR` is
    set), and PROTON otherwise. This script reports that split so the value
    movement is predicted before anything is regenerated.

CATEGORIES
    MUON-explicit  `layer="muon"` — comparison probe, unchanged by the flip.
    MUON-resolved  no-arg, stem declared `ideal_muon` — value UNCHANGED
                   (it was getting muon before, and still does).
    PROTON-resolved no-arg, stem undeclared — value **MOVES** by ~11.5 ppb.
    path=          explicit path argument — unchanged.

Read-only. Reports; changes nothing.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MANIFEST = REPO / "computations" / "q0_anchor_manifest.json"


def _muon_stems() -> set[str]:
    d = json.loads(MANIFEST.read_text())
    return set(d.get("ideal_muon", []))


def _calls(tree: ast.AST) -> list[tuple[int, str]]:
    """(lineno, kind) for each load_q_50dps call. kind ∈ {noarg, muon, caller, path}."""
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
        if name != "load_q_50dps":
            continue
        kw = {k.arg: k.value for k in node.keywords if k.arg}
        if node.args or "path" in kw:
            out.append((node.lineno, "path"))
        elif "layer" in kw:
            v = kw["layer"]
            lit = v.value if isinstance(v, ast.Constant) else "?"
            out.append((node.lineno, str(lit)))
        else:
            out.append((node.lineno, "noarg"))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--include-deprecated", action="store_true")
    ap.add_argument("--movers-only", action="store_true",
                    help="print just the stems whose values move to proton")
    ap.add_argument("--muon-resolved-only", action="store_true",
                    help="print just the stems that still resolve muon")
    args = ap.parse_args(argv)

    muon = _muon_stems()
    buckets: dict[str, list[tuple[str, int]]] = {
        "MUON-explicit": [], "MUON-resolved": [],
        "PROTON-resolved": [], "path=": [],
    }

    for p in sorted(REPO.rglob("*.py")):
        if ".git" in p.parts:
            continue
        if not args.include_deprecated and "_deprecated" in p.parts:
            continue
        if p.name == "_li_2_q_util.py" or p.parent == HERE:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        if "load_q_50dps" not in src:
            continue
        try:
            tree = ast.parse(src)
        except Exception:  # noqa: BLE001
            continue
        rel = str(p.relative_to(REPO))
        for lineno, kind in _calls(tree):
            if kind == "path":
                buckets["path="].append((rel, lineno))
            elif kind == "muon":
                buckets["MUON-explicit"].append((rel, lineno))
            else:  # noarg or layer="caller"
                key = "MUON-resolved" if p.stem in muon else "PROTON-resolved"
                buckets[key].append((rel, lineno))

    if args.movers_only:
        for rel, _ in buckets["PROTON-resolved"]:
            print(Path(rel).stem)
        return 0
    if args.muon_resolved_only:
        for rel, _ in buckets["MUON-resolved"]:
            print(Path(rel).stem)
        return 0

    print("=" * 72)
    print("load_q_50dps caller layers (post-flip)")
    print("=" * 72)
    for key in ("MUON-explicit", "MUON-resolved", "path=", "PROTON-resolved"):
        rows = buckets[key]
        files = sorted({r for r, _ in rows})
        print(f"\n  {key:<16} {len(rows):>3} call(s) in {len(files)} file(s)")
        for f in files:
            print(f"      {f}")
    print()
    print(f"  → {len(sorted({r for r, _ in buckets['PROTON-resolved']}))} producers"
          f" whose values MOVE (muon → proton, ~11.5 ppb).")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
