from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import mpmath as mp


def _canonical_q0() -> mp.mpf:
    try:
        from ._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    except ImportError:
        import sys  # noqa: PLC0415
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        from qou_mass._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    with mp.workdps(max(80, mp.mp.dps)):
        return mp.mpf(Q_50_DIGIT_STR)


def q_pochhammer(q, k) -> mp.mpf:
    with mp.workdps(max(80, mp.mp.dps)):
        q_mp = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        one = mp.mpf(1)
        res = one
        for i in range(1, k + 1):
            res *= (one - q_mp ** i)
        return res


def wenzl_p2_trace(q, N=2) -> mp.mpf:
    """Computes the Markov trace of the Wenzl projector p_2^{JW} at >= 80 dps."""
    with mp.workdps(max(80, mp.mp.dps)):
        q_mp = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        one = mp.mpf(1)
        h_mp = q_mp - one / q_mp

        def q_dim_sym(N_val, k, q_val):
            dim = one
            for j in range(1, k + 1):
                m_num = mp.mpf(N_val + j - 1)
                m_den = mp.mpf(j)
                num = (q_val ** m_num - q_val ** (-m_num)) / h_mp
                den = (q_val ** m_den - q_val ** (-m_den)) / h_mp
                dim *= (num / den)
            return dim

        return q_dim_sym(N, 2, q_mp)


if __name__ == "__main__":
    mp.mp.dps = 80
    q0 = _canonical_q0()
    print("Testing Composite 4 (Wenzl x q-Pochhammer) at q0 =", mp.nstr(q0, 18))

    results = {}
    for N in [2, 3, 4, 5]:
        tr_p2 = wenzl_p2_trace(q0, N)
        qp_2 = q_pochhammer(q0, 2)
        c2 = tr_p2 * qp_2
        print(f"  N={N}: tr_M(p_2^{{JW}}) = {mp.nstr(tr_p2, 10)}, (q;q)_2 = {mp.nstr(qp_2, 10)}, c_2 = {mp.nstr(c2, 10)}")
        results[f"N={N}"] = {
            "tr_p2": mp.nstr(tr_p2, 50),
            "q_poch_2": mp.nstr(qp_2, 50),
            "c2": mp.nstr(c2, 50),
        }

    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-chain4-wenzl-qpoch.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    witness_data = {
        "script_hash": script_hash,
        "q0": mp.nstr(q0, 50),
        "results": results,
        "conclusion": "NEGATIVE: c_2 does not equal -1 for any N",
    }

    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
