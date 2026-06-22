import sys
from pathlib import Path
import json
from mpmath import mp

mp.dps = 200

def main():
    HERE = Path(__file__).parent.resolve()
    sys.path.insert(0, str(HERE))
    import _path_bridge as _pb
    from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402 (codata sweep)

    Q_PIN = _pb.witness_path("q-pinning-200-digit.witness.json", HERE)
    q = mp.mpf("1.1099785955573347198997632204832250266562084087801")
    m_e = mp.mpf("0.51099895000")
    Q_AME = mp.mpf(M_N_MEV_VALIDATION) - mp.mpf(M_P_MEV_VALIDATION) - m_e
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    h = q - 1 / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
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
    with open("computations/q-beta-c3-wenzl-decomposition.witness.json", "w") as f:
        json.dump(witness, f, indent=2)

    return 0

if __name__ == "__main__":
    sys.exit(main())
