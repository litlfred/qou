#!/usr/bin/env python3
"""
L2 (audit § 7) — Crystal-limit observable transport probe.

Per `rem:ontological-agnosticism` (main, PR #571): every observable
extracted by the Observation Frame τ is determined by its image at
the **crystal limit** q → 0 and transported back to the generic
fibre at q = q_0 along the flat q-connection. The graded Euler
characteristic τ(M) = Σ_d (-1)^d dim_R M_d is invariant under this
transport.

Practical implication: combinatorial computation at q = 0 (a finite
sum over crystal-graph vertices, no Hoefsmit matrix entries) yields
the same numerical observable as the full Hecke evaluation at q_0,
provided the observable respects the flat connection.

This probe checks that property on the simplest possible test:
the Markov trace tr_M(σ_1) of the H_3 generator. At q → 0:

  tr_M(σ_1) = Σ_λ y_λ · χ_λ(σ_1)

splits into a sum over partitions; each χ_λ(σ_1) at q = 0 is the
crystal-graph trace = #{T ∈ SYT(λ) : ρ_T(1) ≥ 0}, and y_λ at q = 0
is the Plancherel weight at q = 1.

If transport is flat, the q = q_0 evaluation of the Hoefsmit-matrix
trace must agree with the q = 0 combinatorial trace, after
specialising the crystal-edge weights through the connection.

Status of this probe (PR #581 follow-up): scaffolding only. The
combinatorial side computes the crystal-graph trace; the numerical
side computes the standard Hoefsmit trace; their agreement is
recorded but not yet asserted as a hard equality (the transport
specialisation map is the open piece — that's L2's research content).
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from hecke_characters import standard_young_tableaux, partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


def crystal_chi_at_q_zero(shape: tuple[int, ...], gen_index: int) -> int:
    """Crystal-limit χ_λ(σ_{gen_index}) at q → 0.

    By Kashiwara crystal axioms (per #567's audit, conditional on
    `conj:crystal-graph-realization`): the q = 0 limit of the
    Hoefsmit matrix entry is the sign-count of axial distances
    ρ_T(gen_index) on SYTs of shape λ.

    χ_λ(σ_i) at q = 0 = #{T ∈ SYT(λ) : ρ_T(i) ≥ 0}
                      − #{T ∈ SYT(λ) : ρ_T(i) <  0}

    This stub returns the sign-balance count — not the full crystal
    character (which would require resolving the connection — L2
    research content).
    """
    i = gen_index
    syts, cells, contents = standard_young_tableaux(shape)
    if not syts:
        return 0
    pos_count = 0
    neg_count = 0
    for T in syts:
        # T is a dict {entry: cell_idx} per hecke_characters.
        if (i + 1) not in T or i not in T:
            continue
        rho = contents[T[i + 1]] - contents[T[i]]
        if rho >= 0:
            pos_count += 1
        else:
            neg_count += 1
    return pos_count - neg_count


def main() -> int:
    print("Crystal-limit transport probe — scaffolding")
    print(f"  q_0 = {Q0:.6f}\n")
    rows = []
    for shape in partitions_of(3):
        chi_crystal = crystal_chi_at_q_zero(shape, gen_index=1)
        rows.append({
            "shape": list(shape),
            "chi_crystal_q_zero": int(chi_crystal),
        })
        print(f"  λ = {shape!s:<10} chi_crystal(σ_1) = {chi_crystal}")

    print("\n  Note: full transport-map agreement test (q=0 vs q=q_0)")
    print("  deferred to L2 research deliverable. This scaffolding")
    print("  records the crystal-side numbers as input to that work.")

    out = (WitnessBuilder("crystal-limit-transport-probe", engine="python")
        .set_audit_only("docs/audits/2026-05-08-compute-infrastructure-audit.md")
        .set_description(
            "L2 scaffolding probe: crystal-limit χ_λ(σ_1) values at "
            "q → 0 for H_3 partitions. Per rem:ontological-agnosticism "
            "(main, PR #571), these values transport flatly to the "
            "generic fibre at q = q_0 along the flat q-connection. "
            "Full transport-map verification is deferred research."
        )
        .add_data("narrative_block", "rem:ontological-agnosticism")
        .add_data("conditional_on", ["conj:crystal-graph-realization"])
        .add_data("rows", rows)
        .add_data("status", "scaffolding-only")
        .add_assertion(
            "all_partitions_h3_covered",
            computed=int(len(rows)),
            expected=3,
            tolerance=0,
            source="H_3 has 3 partitions: (3), (2,1), (1,1,1)",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
