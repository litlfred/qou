#!/usr/bin/env python3
"""
Low-isotope mass table (A ≤ 3) via the canonical pipeline.

Thin wrapper that runs `canonical_mass_table_extended.py` restricted
to the paper-canonical low-isotope subset — the 5 atoms
{p, n, D, T, ³He} across which the three independent production
paths for tr_M(𝓑_K) at q = q_0 agree to machine epsilon, per
content block `rem:recomputed-low-isotope-mass-table` — and writes
the result under the dedicated witness filename
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

`--method` defaults to `auto`, which routes per-atom (the low-isotope
set mixes free nucleons and composites, and no single method spans
both): nucleons (A < 2) via `laurent_q_rust` (pyhecke-native Rust +
MPFR H_3 Hoefsmit), composites (A ≥ 2) via `branching` (operator-valued
combiner whose χ^λ goes through the Rust MPFR kernel). Both sub-paths
are MPFR and Rust-backed. Passes through to
canonical_mass_table_extended.py.

`--no-rerun-canonical` skips the canonical re-run and projects from
the existing canonical-mass-table-extended.witness.json (faster but
relies on the canonical witness already being fresh).

## Why a wrapper rather than reuse the canonical witness directly

`canonical-mass-table-extended.witness.json` covers atoms up to
⁷Li. Consumers (paper renderers, audit scripts, the staleness
detector) that historically resolved `low-isotope-mass-table.witness.json`
need a stable artifact at that path. Projecting to A ≤ 3 here keeps
the canonical witness intact while supplying the paper-canonical
low-isotope view (5 atoms — see content block citation in the
top-of-module docstring).

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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
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

# Paper-canonical "low-isotope" set per content block
#   `rem:recomputed-low-isotope-mass-table`
#   (content/quantum-observable-universe/braids-and-knots/
#    recomputed-low-isotope-mass-table.md):
# the 5 atoms across which the three independent production paths
# for tr_M(B_K) at q = q_0 agree to machine epsilon. A ≤ 3 cleanly
# selects this set from the canonical witness rows.
# Ref: [manuscript] rem:recomputed-low-isotope-mass-table
LOW_ISOTOPE_ATOMS = ["p", "n", "D", "T", "3He"]
LOW_ISOTOPE_A_MAX = 3
CANONICAL_WITNESS = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)


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
        # Keep in sync with canonical_mass_table_extended.py's --method
        # choices (the wrapper passes this through verbatim). laurent_q_rust
        # is the Tier 1.A pyhecke-native Rust + MPFR path; branching is the
        # operator-valued combiner; auto routes per-atom across both.
        choices=["auto", "laurent_q_rust", "markov_peel", "laurent_q",
                 "rust_f64", "rust_mpfr", "branching"],
        default="auto",
        help=(
            "Canonical method to dispatch through. Default `auto` routes "
            "per-atom: free nucleons (A<2) -> laurent_q_rust (pyhecke-native "
            "Rust+MPFR H_3 Hoefsmit), composites (A>=2) -> branching "
            "(operator-valued combiner; chi via the Rust MPFR kernel). This is "
            "the only setting that covers the full low-isotope set (p,n,D,T,3He) "
            "in one run, all-MPFR and all Rust-backed."
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

    # Stamp start time BEFORE the canonical subprocess so `durationMs`
    # in the emitted witness reflects true end-to-end wall time
    # (canonical run + projection + write), not just the projection
    # step. Without this the canonical's ~245s would be invisible and
    # the wrapper would self-report ~9ms total — misleading for audit.
    t0 = time.monotonic()

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

    builder = WitnessBuilder(
        "low-isotope-mass-table",
        engine="python+mpmath",
        start_time=t0,
    )
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
