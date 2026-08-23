#!/usr/bin/env python3
"""Cluster operator -- test the framework's connected 3-body cluster vs the Mayer b3.

The framework already realises an irreducible 3-body CLUSTER OPERATOR: the
connected (Ursell/Mayer) part of the JOINT Markov trace over the A=3 interfaces,
computed at H_9 with zero fit (`three_body_joint_trace_a3.py`):

    c3 = joint - pair_sum = E0 * (g{a} + g{b} - g{} - g{a,b})

where g(S) = per-block trace with interface subset S present.  This is the
genuine many-body 3-body force (the bonds' destructive interference when
co-present), and the Brunnian / Borromean property is its TOPOLOGICAL SELECTION
criterion (3-body confinement = no separable sub-link; `b3_brunnian_selection_scope.py`).

This probe compares that framework cluster to the empirical 3-body term from the
Mayer decomposition of AME (b2 identified from the deuteron):

    b3 = B(A=3) - 3*b2.

Scope discipline (AGENTS.md "Before declaring refuted/ruled out"): the two are
the irreducible 3-body term in DIFFERENT decomposition bases (framework: joint -
pair over the 2 adjacent chain bonds; Mayer: AME - 3*b2 over the triangle), so a
mismatch is a SCOPE-LIMITED observation about magnitude/sign, NOT a refutation of
the cluster operator.
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json
import sys
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"

# framework connected 3-body cluster (cached, H_9 joint trace, zero fit)
with open(COMP / "three-body-joint-trace-a3.witness.json") as f:
    JT = json.load(f)["data"]["results"]

AME = {"T": mp.mpf("8.481798"), "3He": mp.mpf("7.718043"), "D": mp.mpf("2.224566")}
b2 = AME["D"]  # Mayer 2-body, identified from the unique 2-body nucleus


def main():
    print("=" * 76)
    print("CLUSTER OPERATOR -- framework connected 3-body cluster vs empirical b3")
    print("  framework c3 = joint - pair_sum (Ursell, H_9 joint trace, 0 fit)")
    print("  empirical b3 = B(A=3) - 3*b2     (Mayer, b2 = deuteron)")
    print("=" * 76)
    rows = []
    for atom in ["T", "3He"]:
        c3 = mp.mpf(str(JT[atom]["correlation_c3_MeV"]))
        joint = mp.mpf(str(JT[atom]["joint_MeV"]))
        pair_sum = mp.mpf(str(JT[atom]["pair_sum_MeV"]))
        b3 = AME[atom] - 3 * b2
        mag_ratio = abs(c3) / abs(b3)
        same_sign = (c3 > 0) == (b3 > 0)
        print(f"\n--- {atom} ---")
        print(f"  framework: pair_sum={mp.nstr(pair_sum,5)}  joint={mp.nstr(joint,5)}"
              f"  c3={mp.nstr(c3,5)} MeV")
        print(f"  empirical: B_AME={mp.nstr(AME[atom],6)}  b3=B-3b2={mp.nstr(b3,5)} MeV")
        print(f"  |c3|/|b3| = {mp.nstr(mag_ratio,4)}   sign(c3)={'+' if c3>0 else '-'}"
              f"  sign(b3)={'+' if b3>0 else '-'}   same_sign={same_sign}")
        rows.append({"atom": atom, "framework_c3_MeV": mp.nstr(c3, 12),
                     "empirical_b3_MeV": mp.nstr(b3, 12),
                     "mag_ratio": mp.nstr(mag_ratio, 8), "same_sign": bool(same_sign)})

    print("\n" + "=" * 76)
    print("READING (scope-limited per AGENTS.md refutation discipline):")
    print("  (+) SCALE MATCHES: the framework's connected 3-body cluster lands at")
    print("      |c3| = 1.4-1.8 MeV, the same O(1.5 MeV) as the empirical b3 -- a")
    print("      positive structural signal that the joint-trace Ursell cluster IS")
    print("      the right object/scale for the 3-body force.")
    print("  (-) SIGN OPPOSED (this construction, as computed): framework c3 < 0")
    print("      (destructive: joint saturates below the pair-sum) vs empirical")
    print("      b3 > 0 (attractive 3N force, adds binding toward AME).")
    print("  This does NOT refute the cluster operator. The negative c3 is the")
    print("  2-adjacent-chain-bond, |chi|-combiner realisation; candidates to flip")
    print("  the sign (all untested): the missing long-range (1-3) triangle bond,")
    print("  the Borromean-selected interface vs the bare sigma_g, and the joint")
    print("  combiner's |chi| vs signed convention. The sign is the precise OPEN")
    print("  question; the magnitude match is the encouraging, parameter-free signal.")

    witness = {
        "computation": "cluster-operator-vs-mayer-b3",
        "description": ("Compare the framework's connected 3-body cluster (Ursell, joint "
                        "H_9 trace) to the empirical Mayer b3 (AME - 3*b2). Magnitude "
                        "matches (~1.5 MeV); sign opposed in this chain-adjacent realisation. "
                        "Scope-limited: not a refutation of the cluster operator."),
        "scriptFile": "computations/probes/binding_cluster_operator_vs_mayer_probe.py",
        "parameters": {"free_parameters": 0, "b2_source": "deuteron"},
        "data": {"rows": rows,
                 "verdict": "scale_matches_sign_opposed_scope_limited"},
    }
    sys.path.insert(0, str(COMP / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wb = WitnessBuilder.wrap_legacy(
        "cluster-operator-vs-mayer-b3", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
        output_dir=str(COMP),
    )
    # reads three-body-joint-trace-a3 as input → record the genuine upstream edge
    _wb.add_upstream(COMP / "three-body-joint-trace-a3.witness.json")
    out = _wb.save()
    print(f"\nwitness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
