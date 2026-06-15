"""I2 audit — probe witnesses not consumed in production.

A probe script may emit a `*.witness.json` whose `contentBlock`
points at a real provable block label, yet no production-side
script (paper_six_term_isotope_sweep, derive_m_p / derive_m_n /
atomic_mass_via_rho_k / mass_table_ppb / canonical_tr_m_via_rust)
imports the witness file or references the underlying constant.

The probe is then a "shelf piece" — its result is recorded but
never enters the paper's predicted mass / coupling / energy
tables.

The I2 antipattern in `local/compute-integration-watcher`:

  A `*.witness.json` exists with `contentBlock` pointing at a
  label, but none of the production consumers references either:
    - the witness filename, OR
    - the contentBlock label, OR
    - the witness's `upstream_witness_hashes` reverse-lookup
      (a downstream consumer would name this witness as upstream).

This audit walks every witness with a label-shaped contentBlock,
and for each one greps the production-consumer set + every other
witness's `upstream_witness_hashes` for references.

Production consumers (from compute-integration-watcher.md):

  - paper_six_term_isotope_sweep.py
  - derive_m_p*.py
  - derive_m_n*.py
  - atomic_mass_via_rho_k.py
  - mass_table_ppb.py
  - canonical_tr_m_via_rust.py
  - cross_check_trM_*.py

Classifications:

  - `wired_production`     — referenced by a production consumer
  - `wired_upstream`       — referenced as upstream by another
                             witness
  - `i2_probe_only`        — neither: the probe is a shelf piece
  - `informational_label`  — contentBlock is not a label-shape
                             (skipped, info-only)

Emits `i2-probe-only-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/i2_probe_only_audit.py [--strict]
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

PRODUCTION_CONSUMER_PATTERNS = (
    "paper_six_term_isotope_sweep",
    "derive_m_p",
    "derive_m_n",
    "atomic_mass_via_rho_k",
    "mass_table_ppb",
    "canonical_tr_m_via_rust",
    "cross_check_trM",
)

LABEL_PREFIXES = ("def:", "thm:", "lem:", "prop:", "cor:", "conj:")


def _enumerate_production_scripts() -> list[Path]:
    """Find production consumer scripts by name pattern."""
    scripts: list[Path] = []
    for py in sorted(HERE.glob("*.py")):
        if any(pat in py.name for pat in PRODUCTION_CONSUMER_PATTERNS):
            scripts.append(py)
    return scripts


def _collect_upstream_refs() -> dict[str, list[str]]:
    """Map witness-file-name → list of other witnesses that name it
    as an upstream (via `upstream_witness_hashes`)."""
    upstream_map: dict[str, list[str]] = {}
    for w in sorted(HERE.glob("*.witness.json")):
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        # upstream_witness_hashes is typically a dict
        # {witness_filename: sha} at top level or under "results".
        def _walk(obj):
            if isinstance(obj, dict):
                if "upstream_witness_hashes" in obj:
                    uwh = obj["upstream_witness_hashes"]
                    if isinstance(uwh, dict):
                        for k in uwh:
                            upstream_map.setdefault(k, []).append(w.name)
                for v in obj.values():
                    _walk(v)
            elif isinstance(obj, list):
                for v in obj:
                    _walk(v)
        _walk(d)
    return upstream_map


def _audit_witness(path: Path,
                   production_scripts: list[Path],
                   upstream_map: dict[str, list[str]]) -> dict[str, Any] | None:
    """Audit one witness for production consumption."""
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None

    cb = d.get("contentBlock")
    candidates: list[str] = []
    if isinstance(cb, str):
        candidates = [cb]
    elif isinstance(cb, list):
        candidates = [c for c in cb if isinstance(c, str)]
    candidates = [c.strip() for c in candidates if isinstance(c, str)]

    label_candidates = [
        c for c in candidates
        if any(c.startswith(p) for p in LABEL_PREFIXES) and " " not in c
    ]
    if not label_candidates:
        return None  # informational; skip

    rel = path.relative_to(REPO_ROOT)
    row: dict[str, Any] = {
        "witness": str(rel),
        "labels": label_candidates,
    }

    # Production consumer reference check.
    production_refs: list[str] = []
    for prod in production_scripts:
        try:
            ptext = prod.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if path.name in ptext or any(label in ptext for label in label_candidates):
            production_refs.append(prod.name)

    row["production_consumers"] = production_refs

    # Upstream reverse-lookup.
    upstream_refs = upstream_map.get(path.name, [])
    row["upstream_consumers"] = upstream_refs

    # Classify.
    if production_refs:
        row["result"] = "wired_production"
    elif upstream_refs:
        row["result"] = "wired_upstream"
    else:
        row["result"] = "i2_probe_only"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    print("Enumerating production consumers ...")
    prod_scripts = _enumerate_production_scripts()
    print(f"  {len(prod_scripts)} production scripts in scope:")
    for p in prod_scripts:
        print(f"    {p.name}")

    print("\nBuilding upstream-witness reverse index ...")
    upstream_map = _collect_upstream_refs()
    print(f"  {len(upstream_map)} witnesses named as upstream by others")

    rows: list[dict[str, Any]] = []
    for w in sorted(HERE.glob("*.witness.json")):
        if w.name == "i2-probe-only-audit.witness.json":
            continue
        result = _audit_witness(w, prod_scripts, upstream_map)
        if result is None:
            continue
        rows.append(result)

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    print("=" * 80)
    print(f"I2 audit — probe-only witnesses  ({len(rows)} label-bearing witnesses)")
    print("=" * 80)
    for cls in ("wired_production", "wired_upstream", "i2_probe_only"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} witnesses)")
        for r in rs[:10]:
            extras = ""
            if r.get("production_consumers"):
                extras = f"  ← {r['production_consumers'][0]}"
            elif r.get("upstream_consumers"):
                extras = f"  ← upstream of {r['upstream_consumers'][0]}"
            print(f"    {r['witness']:<70s}{extras}")
        if len(rs) > 10:
            print(f"    … and {len(rs) - 10} more")
    print()
    print(f"Summary:")
    print(f"  total label-bearing witnesses:  {len(rows)}")
    print(f"  wired_production:               {len(buckets.get('wired_production', []))}")
    print(f"  wired_upstream:                 {len(buckets.get('wired_upstream', []))}")
    print(f"  i2_probe_only (actionable):     {len(buckets.get('i2_probe_only', []))}")

    b = (
        WitnessBuilder("i2-probe-only-audit", engine="python")
        .set_description(
            "I2 audit per local/compute-integration-watcher: every "
            "*.witness.json with a label-shaped `contentBlock` is checked "
            "for references from the production-consumer set (paper_six_term_"
            "isotope_sweep, derive_m_p/n, atomic_mass_via_rho_k, mass_table_"
            "ppb, canonical_tr_m_via_rust, cross_check_trM_*) and from "
            "other witnesses' `upstream_witness_hashes`.  Unreferenced "
            "witnesses are I2 probe-only shelf pieces."
        )
        .set_content_block(
            "I2 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("production_consumers_count", len(prod_scripts))
        .add_parameter("total_label_bearing_witnesses", len(rows))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("production_consumers", [p.name for p in prod_scripts])
        .add_data("rows", rows)
        .add_assertion(
            name="no_i2_probe_only_witnesses",
            computed=1.0 if "i2_probe_only" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = every probe is consumed somewhere)",
            source="Closure gate: when this passes, every probe witness is "
                   "consumed by production OR is named as upstream by a "
                   "downstream witness.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "i2_probe_only" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
