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


def arm_length(partition, i, j):
    """i, j are 0-indexed row and column"""
    return partition[i] - 1 - j


def leg_length(partition, i, j):
    """i, j are 0-indexed row and column"""
    count = 0
    for r in range(i + 1, len(partition)):
        if partition[r] > j:
            count += 1
        else:
            break
    return count


def macdonald_principal_eval(partition, q, t) -> mp.mpf:
    """Evaluates P_lambda(1, t, t^2, ...) using the hook-length product at >= 80 dps."""
    with mp.workdps(max(80, mp.mp.dps)):
        q_mp = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
        t_mp = t if isinstance(t, mp.mpf) else mp.mpf(str(t))
        one = mp.mpf(1)
        n_lambda = sum(i * partition[i] for i in range(len(partition)))
        res = t_mp ** n_lambda
        for i, row in enumerate(partition):
            for j in range(row):
                a = arm_length(partition, i, j)
                l = leg_length(partition, i, j)
                num = one - (q_mp ** a) * (t_mp ** (l + 1))
                den = one - (q_mp ** (a + 1)) * (t_mp ** l)
                res *= (num / den)
        return res


if __name__ == "__main__":
    mp.mp.dps = 80
    q0 = _canonical_q0()
    one = mp.mpf(1)

    t_choices = {
        "t = q": q0,
        "t = q^2": q0 ** 2,
        "t = 1/q": one / q0,
        "t = -q": -q0,
        "t = -1/q": -one / q0,
    }

    results = {}
    print("Testing DAHA/Macdonald principal evaluations for c_2 (partition [2])")

    partition = [2]
    for label, t_val in t_choices.items():
        y_2 = macdonald_principal_eval(partition, q0, t_val)
        print(f"{label}: P_[2](t^rho; q, t) = {mp.nstr(y_2, 12)}")
        results[label] = mp.nstr(y_2, 50)

    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-daha-macdonald.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    witness_data = {
        "script_hash": script_hash,
        "q0": mp.nstr(q0, 50),
        "results": results,
        "conclusion": "Checking if any natural t gives -1",
    }

    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
