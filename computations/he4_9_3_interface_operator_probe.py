"""Option E PROBE 2: 4He (9,3) Interface Operator Target.

Computes the per-block A^(9,3)_{ξν}(I) interface operator for A=4,
targeting the (2,1) block of ν (S3) which corresponds to the h^4 = -3/4
coefficient of the Borromean H3(q) Markov trace (S5-SO3 fiber action).
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import mpmath as mp
mp.mp.dps = 60

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "a_operator"))

from a_operator.a_operator_categorical import q0_mp
from a_operator.a_operator_recursive import interface_blocks
from lr_coefficients import partitions_of

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: the
# bar-symmetriser of z, which averages the two flavours 50/50 and so cannot
# see the substrate flavour split. Imported, not open-coded, so there is one
# definition; the import is hard on purpose because a fallback would compute
# the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

def run_probe():
    dps = 50
    q = q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1/q
    bridge_coef = _pn_d(h)

    print("=== Option E PROBE 2: A=4 (9,3) Interface Operator ===", flush=True)
    print(f"Targeting ν = (2, 1) block of H_3(q) (Borromean h^4 trace coefficient)")
    print(f"Bridge generator coefficient: -h/2 = {mp.nstr(bridge_coef, 6)}")

    target_nu = (2, 1)
    
    # Compute A-operator interface blocks for 4He (λ ⊢ 12, inner=9, block=3)
    results = {}
    
    # In order to be practical, we only run on a few dominant partitions of 12
    # that are typically relevant (e.g. ones with few rows, since A=4).
    lams = [(10, 2), (11, 1), (9, 3), (8, 4), (12,), (8, 2, 1, 1)]
    for lam in lams:
        try:
            A_dict = interface_blocks(lam, 9, 3, q_str, bridge_coef, dps=dps)
            
            # Filter for ν = (2, 1)
            matching_blocks = {k: v for k, v in A_dict.items() if k[1] == target_nu}
            if matching_blocks:
                results[lam] = matching_blocks
                print(f"  λ={lam} contains {len(matching_blocks)} sub-blocks with ν=(2, 1)")
        except Exception as e:
            print(f"  λ={lam} skipped due to error: {e}")

    print("\n--- Interface Block Traces for ν = (2, 1) ---")
    for lam, blocks in results.items():
        total_trace = mp.mpf(0)
        for (xi, nu), info in blocks.items():
            A_mat = info["A"]
            # Compute trace of A
            tr_A = sum(A_mat[i, i] for i in range(A_mat.rows))
            total_trace += tr_A
            print(f"  λ={lam}, ξ={xi}: tr(A) = {mp.nstr(tr_A, 6)} (dim={A_mat.rows}x{A_mat.cols})")
        

        print(f"  => Total (2,1) trace for λ={lam}: {mp.nstr(total_trace, 6)}")
        
    import json
    from datetime import datetime, timezone
    
    witness = {
        "engine": "python",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "he4_9_3_interface_operator_probe",
        "description": "Option E PROBE 2 A=4 interface operator traces for dominant partitions (nu=(2,1) block).",
        "results": {str(lam): float(total_trace) for lam in results.keys()}
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(Path(__file__).parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.wrap_legacy(
        "he4-9-3-interface-operator-probe", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
        output_dir=str(Path(__file__).parent / "probes"),
    ).save()
    print("Wrote computations/probes/he4-9-3-interface-operator-probe.witness.json")


if __name__ == "__main__":
    run_probe()
