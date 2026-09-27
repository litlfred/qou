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
                                         [--rerun-canonical]

`--method` defaults to `auto`, which routes per-atom (the low-isotope
set mixes free nucleons and composites, and no single method spans
both): nucleons (A < 2) via `laurent_q_rust` (pyhecke-native Rust +
MPFR H_3 Hoefsmit), composites (A ≥ 2) via `branching` (operator-valued
combiner whose χ^λ goes through the Rust MPFR kernel). Both sub-paths
are MPFR and Rust-backed. Passes through to
canonical_mass_table_extended.py.

By default this projects from the existing
canonical-mass-table-extended.witness.json and does NOT touch it — a
projection should not rewrite its own source. `--rerun-canonical` opts
into refreshing the canonical table first, at full coverage.

That is the reverse of how it behaved until 2026-08-28 (bean
`qou-7e1t`), when the re-run was the default and this wrapper's own
narrower arguments — `--target-dps 11` against a committed 60 —
silently replaced the canonical artifact with a coarser one. Note
`--target-dps` is the active-set pruning threshold, not a formatting
knob, so that rewrite changed which Wedderburn blocks entered the sum.

`--no-rerun-canonical` is still accepted, means exactly what it said,
and is now simply the default.

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

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

# Paper-canonical "low-isotope" set per content block
#   `rem:recomputed-low-isotope-mass-table`
#   (folio/quantum-observable-universe/braids-and-knots/
#    recomputed-low-isotope-mass-table.md):
# the 5 atoms across which the three independent production paths
# for tr_M(B_K) at q = q_0 agree to machine epsilon. A ≤ 3 cleanly
# selects this set from the canonical witness rows.
# Ref: [manuscript] rem:recomputed-low-isotope-mass-table
LOW_ISOTOPE_ATOMS = ["p", "n", "D", "T", "3He"]
LOW_ISOTOPE_A_MAX = 3
CANONICAL_WITNESS = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)


def run_canonical(method: str, target_dps: int) -> None:
    """Invoke canonical_mass_table_extended.py end-to-end, at FULL coverage.

    Deliberately does **not** pass `--atoms` (bean `qou-xwet`).

    This used to restrict the canonical run to `LOW_ISOTOPE_ATOMS` as a speed
    optimisation. That was destructive and redundant at the same time:

    * **Destructive** — the canonical script's output filename is fixed, so the
      restricted run overwrote `canonical-mass-table-extended.witness.json`
      with a five-row table. On `main` that dropped 4He and every A >= 5 row,
      and silently repointed `registry.ts`'s positional `B_2H_AME_MeV` pin
      (`data.rows.2.B_AME_MeV`) at a different nuclide.
    * **Redundant** — `project_to_low_isotope()` below already filters to
      `A <= LOW_ISOTOPE_A_MAX`, so restricting the *upstream* run bought
      nothing this wrapper needs.

    Full coverage is slower. That is the correct trade for a shared committed
    artifact, and `--no-rerun-canonical` remains available when the canonical
    witness is already fresh. The canonical script now also refuses a partial
    write outright, so this call could not silently regress again.
    """
    cmd = [
        sys.executable, "-u",
        str(HERE / "canonical_mass_table_extended.py"),
        "--method", method,
    ]
    # Omit --target-dps entirely when unset, so the canonical script uses its
    # OWN default (OUTPUT_DPS) rather than inheriting this wrapper's.
    if target_dps is not None:
        cmd += ["--target-dps", str(target_dps)]
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
    src = record_upstream(CANONICAL_WITNESS, _UPSTREAM_RECORDS)
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
    # Default None = INHERIT the canonical script's own default, and record
    # what the projected witness was actually built at.
    #
    # This used to default to 11, and that number is the mechanism of the whole
    # defect: it is what the wrapper passed down when the re-run was the
    # default, and it is what replaced a committed 60 with a coarser table.
    # It also mislabelled the projection — the committed witness records
    # `parameters.target_dps: 11` while holding data a 60-dps run produced, a
    # setting that was never applied to the numbers in the file.
    #
    # An explicit `--target-dps` is still passed through, so a deliberate
    # coarser run is still expressible; `canonical_mass_table_extended` then
    # refuses the downgrade unless `--allow-precision-downgrade` is given.
    parser.add_argument("--target-dps", type=int, default=None)
    parser.add_argument(
        "--rerun-canonical",
        action="store_true",
        help=(
            "Also re-run canonical_mass_table_extended.py first, at FULL "
            "coverage, before projecting. Off by default: this script is a "
            "projection, and a projection should not rewrite its own source."
        ),
    )
    parser.add_argument(
        "--no-rerun-canonical",
        action="store_true",
        help=argparse.SUPPRESS,   # accepted, now the default; see below
    )
    args = parser.parse_args()

    # The re-run is OPT-IN as of 2026-08-28 (bean `qou-7e1t`, option 1). It was
    # the default, which made "project the low-isotope view" silently rewrite
    # the canonical table it projects FROM — with this script's own narrower
    # arguments, `--target-dps 11` against a committed 60. `--target-dps` is not
    # a formatting knob: it is the active-set pruning threshold, so the rewrite
    # changed which Wedderburn blocks were summed, not just how many digits
    # were printed.
    #
    # `--no-rerun-canonical` is still accepted and still means what it said, so
    # every existing invocation and doc line keeps working; it is simply the
    # default now, and hidden from --help rather than removed. Passing both is
    # not a contradiction — they agree.
    #
    # This was NOT safe to do until the canonical table carried p and n. Until
    # then a light reproject dropped them and the paper's 5-atom low-isotope
    # set silently became 3 — which is why the 2026-06-14 triage audit called
    # this change architecturally significant rather than small. The preceding
    # commit (option 3, `--method` default -> `auto`) is what removed that
    # objection: canonical is 9 rows now, so the projection is 5 again.
    rerun = args.rerun_canonical and not args.no_rerun_canonical

    # Stamp start time BEFORE the canonical subprocess so `durationMs`
    # in the emitted witness reflects true end-to-end wall time
    # (canonical run + projection + write), not just the projection
    # step. Without this the canonical's ~245s would be invisible and
    # the wrapper would self-report ~9ms total — misleading for audit.
    t0 = time.monotonic()

    if rerun:
        run_canonical(args.method, args.target_dps)
    else:
        print(
            f"  projecting from the existing {CANONICAL_WITNESS.name} "
            "(may be stale; pass --rerun-canonical to refresh it first)",
            flush=True,
        )

    projected = project_to_low_isotope()
    src = projected["src"]

    builder = WitnessBuilder(
        "low-isotope-mass-table",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
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
        # The value the projected DATA was built at, not the flag this process
        # happened to carry. When --target-dps is unset those differ, and the
        # witness must describe the numbers it holds.
        .add_parameter(
            "target_dps",
            args.target_dps if args.target_dps is not None
            else src.get("parameters", {}).get("target_dps"),
        )
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
    # Declare the q0 pin, INHERITED from the witness this projects.
    #
    # `builder.save()` was called bare, so the emitted witness carried
    # `q0Anchor: null` and `q0Value: null` — it could not say which anchor
    # layer its numbers belonged to. AGENTS.md: "Say which pin you used."
    #
    # That is not a cosmetic gap. A witness that does not declare its layer is
    # the enabling condition for comparing across layers and reading the
    # difference as a defect — which is exactly the mistake retracted in bean
    # `qou-4e5k` on this arc (a ~7.8e-08 "second discrepancy" between this
    # table and a MUON-anchored one, where the gap was the layer separation
    # itself, not an error).
    #
    # Inherited rather than re-derived: this producer computes nothing. It is a
    # thin projection of `canonical-mass-table-extended.witness.json` restricted
    # to A <= LOW_ISOTOPE_A_MAX, so its rows are that witness's rows and its
    # layer is that witness's layer by construction. Reading `q_parameter`
    # directly here would be worse — it would declare the pin this process
    # happens to import rather than the pin the numbers were computed at, and
    # the two can differ precisely when the source witness is stale.
    out = builder.save({
        "q0Anchor": src.get("q0Anchor"),
        "q0Value": src.get("q0Value"),
    })
    print()
    print(f"  Wrote {out.name} ({projected['n_atoms']} atoms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
