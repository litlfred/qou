import sys
from pathlib import Path
import json
from mpmath import mp

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This file bound the RETIRED
# self-certified muon pin A as a literal -- superseded 2026-08-22 by the
# CODATA-2022 derivation, so the value was ~46 ppb stale AND could not follow
# the anchor. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR` resolves to
# the PROTON pin, which the 2026-08-30 owner ruling makes the default.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent / 'substrate',
              _Path_qp(__file__).resolve().parent.parent / 'computations',
              _Path_qp(__file__).resolve().parent.parent / 'computations' / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV

mp.dps = 200

def main():
    HERE = Path(__file__).parent.resolve()
    sys.path.insert(0, str(HERE))
    import _path_bridge as _pb
    from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402 (codata sweep)

    Q_PIN = _pb.witness_path("q-pinning-200-digit.witness.json", HERE)
    q = Q_MP
    m_e = M_E_MEV
    Q_AME = mp.mpf(M_N_MEV_VALIDATION) - mp.mpf(M_P_MEV_VALIDATION) - m_e
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2
    hbar_q4 = hbar_q ** 4
    hbar_q6 = hbar_q ** 6
    alpha = (z - 1) * h / 2

    def q_num(n, q):
        return (q**n - q**(-n)) / (q - 1/q)

    def q_fact(n, q):
        res = mp.mpf(1)
        for i in range(1, n+1):
            res *= q_num(i, q)
        return res

    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)

    alpha_N1 = alpha - b * hbar_q2 / 2
    cos_N1 = mp.cos(alpha_N1)
    Q_N1 = Q_A * cos_N1
    Q_N2 = Q_N1 * (1 - b ** 2 * hbar_q4)

    W3 = 1 / q_fact(3, q)
    W4 = 1 / q_fact(4, q)
    W5 = 1 / q_fact(5, q)
    
    W3_alt = 1 / q_fact(3, -1/q) # Alternating Wenzl weight
    W4_alt = 1 / q_fact(4, -1/q)

    print("Q_N2 / Q_AME = ", Q_N2 / Q_AME)
    print("Residual gap (ppm) = ", (Q_N2 / Q_AME - 1) * 1e6)
    
    print("\n--- Testing Wenzl Multipliers ---")
    
    # We want Q_N3 = Q_N2 * (1 + C * b^3 * hbar_q6)
    # Let's test C being related to W3, W4, etc.
    
    c_best = mp.mpf('-2') - mp.mpf('1.5') * W4
    q_pred = Q_N2 * (1 + c_best * b**3 * hbar_q6)
    eps_best = (q_pred / Q_AME - 1) * 1e6
    
    print(f"C_best = -2 - 1.5 * W_4 => eps = {float(eps_best):+.4f} ppm")
    
    witness = {
        "description": "Q_beta N=3 brane-tower truncation Wenzl product decomposition",
        "data": {
            "c_best_expr": "-2 - 1.5 * W_4",
            "c_best_val": str(c_best),
            "eps_ppm": float(eps_best),
            "W_4_val": str(W4)
        }
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(HERE / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = Path(__file__).name
    with open(HERE / "q-beta-c3-wenzl-decomposition.witness.json", "w") as f:
        json.dump(witness, f, indent=2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
