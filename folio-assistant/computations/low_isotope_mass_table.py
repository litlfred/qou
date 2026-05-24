#!/usr/bin/env python3
"""
Low-isotope mass table (A ≤ 6) via the canonical pipeline.

Thin wrapper that runs `canonical_mass_table_extended.py` restricted
to the low-isotope subset (proton through ⁶Li) and writes the result
under the dedicated witness filename
`low-isotope-mass-table.witness.json` so downstream consumers that
resolve the table by its historical name continue to work.

The witness's `data.derived_from` field records the canonical
witness's scriptHash + scriptCommitSha + computedAt so the staleness
checker sees the lineage explicitly. The wrapper's own scriptHash
is also recorded (via WitnessBuilder) so an edit to this wrapper
invalidates the derived witness independently of the canonical one.

CLI:

    python3 -u low_isotope_mass_table.py [--method M] [--target-dps N]
                                         [--no-rerun-canonical]

`--method` defaults to `laurent_q` (LaurentQ-direct MPFR-50dps path,
PR #859), matching the canonical-preferred production path. Passes
through to canonical_mass_table_extended.py.

`--no-rerun-canonical` skips the canonical re-run and projects from
the existing canonical-mass-table-extended.witness.json (faster but
relies on the canonical witness already being fresh).

## Why a wrapper rather than reuse the canonical witness directly

`canonical-mass-table-extended.witness.json` covers atoms up to
⁷Li. Consumers (paper renderers, audit scripts, the staleness
detector) that historically resolved `low-isotope-mass-table.witness.json`
need a stable artifact at that path. Projecting to A ≤ 6 here keeps
the canonical witness intact while supplying the low-isotope view.

## History

The previous standalone `low_isotope_mass_table.py` (541-line
custom derivation chain) was retired on 2026-05-24 in favor of
this thin wrapper, consolidating the low-isotope view around the
canonical pipeline. The full per-row derivation status (DERIVED /
PENDING / COMPARISON_ONLY) is now provided by the canonical
script's `prediction_method` / `B_derivation_status` row fields,
so no information is lost — only the duplicated derivation logic.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

LOW_ISOTOPE_ATOMS = ["p", "n", "D", "T", "3He", "4He", "5Li", "6Li"]
LOW_ISOTOPE_A_MAX = 6
CANONICAL_WITNESS = HERE / "canonical-mass-table-extended.witness.json"


def run_canonical(method: str, target_dps: int) -> None:
    """Invoke canonical_mass_table_extended.py end-to-end."""
    cmd = [
        sys.executable, "-u",
        str(HERE / "canonical_mass_table_extended.py"),
        "--atoms", ",".join(LOW_ISOTOPE_ATOMS),
        "--method", method,
        "--target-dps", str(target_dps),
    ]
    print(f"$ {' '.join(cmd)}", flush=True)
    t0 = time.time()
    rc = subprocess.run(cmd).returncode
    elapsed = time.time() - t0
    print(f"  canonical finished in {elapsed:.1f}s (rc={rc})", flush=True)
    if rc != 0:
        sys.exit(rc)


def project_to_low_isotope() -> dict:
    """Load canonical witness; project to A ≤ LOW_ISOTOPE_A_MAX rows."""
    if not CANONICAL_WITNESS.exists():
        raise FileNotFoundError(
            f"canonical witness missing: {CANONICAL_WITNESS}. "
            f"Did canonical_mass_table_extended.py write it?"
        )
    src = json.loads(CANONICAL_WITNESS.read_text())
    rows = src["data"]["rows"]
    low_rows = [r for r in rows if r.get("A", 99) <= LOW_ISOTOPE_A_MAX]
    return {
        "src": src,
        "rows": low_rows,
        "n_atoms": len(low_rows),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--method",
        choices=["markov_peel", "laurent_q", "rust_f64", "rust_mpfr"],
        default="laurent_q",
        help=(
            "Canonical method to dispatch through. Default laurent_q "
            "(LaurentQ-direct MPFR-50dps, fastest production path)."
        ),
    )
    parser.add_argument("--target-dps", type=int, default=11)
    parser.add_argument(
        "--no-rerun-canonical",
        action="store_true",
        help=(
            "Skip the canonical re-run and project from the existing "
            "canonical-mass-table-extended.witness.json. Useful when "
            "canonical is already fresh."
        ),
    )
    args = parser.parse_args()

    if not args.no_rerun_canonical:
        run_canonical(args.method, args.target_dps)
    else:
        print(
            "  --no-rerun-canonical: projecting from existing "
            f"{CANONICAL_WITNESS.name} (may be stale)",
            flush=True,
        )

    projected = project_to_low_isotope()
    src = projected["src"]

    builder = WitnessBuilder("low-isotope-mass-table", engine="python+mpmath")
    (
        builder
        .set_description(
            f"Low-isotope mass table (A ≤ {LOW_ISOTOPE_A_MAX}) via "
            f"canonical pipeline ({args.method}). Thin projection of "
            f"canonical-mass-table-extended.witness.json restricted to "
            f"the lightest {projected['n_atoms']} atoms."
        )
        .add_parameter("method", args.method)
        .add_parameter("atoms_requested", ",".join(LOW_ISOTOPE_ATOMS))
        .add_parameter("A_max", LOW_ISOTOPE_A_MAX)
        .add_parameter("target_dps", args.target_dps)
        .add_data("rows", projected["rows"])
        .add_data("n_atoms", projected["n_atoms"])
        .add_data("derived_from", {
            "witness": "canonical-mass-table-extended.witness.json",
            "scriptHash": src.get("scriptHash"),
            "scriptCommitSha": src.get("scriptCommitSha"),
            "computedAt": src.get("computedAt"),
            "commitSha": src.get("commitSha"),
        })
    )
    out = builder.save()
    print()
    print(f"  Wrote {out.name} ({projected['n_atoms']} atoms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
