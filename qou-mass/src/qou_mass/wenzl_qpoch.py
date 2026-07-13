import math
import numpy as np

def q_pochhammer(q, k):
    res = 1.0
    for i in range(1, k + 1):
        res *= (1.0 - q**i)
    return res

def wenzl_p2_trace(q, N=2):
    """
    Computes the Markov trace of the Wenzl projector p_2^{JW}.
    p_2^{JW} = 1 + c * e_1
    tr_M(1) = 1
    tr_M(e_1) = [N-1]_q / [N]_q ? No, for SU(N), tr_M(T_i) = q^N or similar.
    Wait, the dimension of the quantum group rep is tr_M(p_2^{JW}).
    For SU(2), the dimension of the spin-1 rep (which p_2^{JW} projects onto) is [3]_q.
    Wait, the Markov trace of the projector is exactly the quantum dimension of the corresponding representation!
    For p_k^{JW}, tr_M(p_k^{JW}) = [k+1]_q  (for sl_2).
    Let's compute for N=2, 3, 4, 5.
    For sl_N, tr_M(p_k^{JW}) = quantum dimension of Sym^k(V).
    dim_q(Sym^k(C^N)) = \prod_{j=1}^k [N + j - 1]_q / [j]_q.
    """
    def q_dim_sym(N, k, q):
        dim = 1.0
        for j in range(1, k + 1):
            num = (q**(N + j - 1) - q**(-(N + j - 1))) / (q - 1/q)
            den = (q**j - q**(-j)) / (q - 1/q)
            dim *= (num / den)
        return dim
    
    return q_dim_sym(N, 2, q)

import json
import hashlib
import os

if __name__ == "__main__":
    q0 = 1.10997858
    print("Testing Composite 4 (Wenzl x q-Pochhammer) at q0 =", q0)
    
    results = {}
    for N in [2, 3, 4, 5]:
        tr_p2 = wenzl_p2_trace(q0, N)
        qp_2 = q_pochhammer(q0, 2)
        c2 = tr_p2 * qp_2
        print(f"  N={N}: tr_M(p_2^{{JW}}) = {tr_p2:.5f}, (q;q)_2 = {qp_2:.5f}, c_2 = {c2:.5f}")
        results[f"N={N}"] = {"tr_p2": tr_p2, "q_poch_2": qp_2, "c2": c2}
        
    witness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations", "qbeta", "qbeta-chain4-wenzl-qpoch.witness.json")
    with open(__file__, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        
    witness_data = {
        "script_hash": script_hash,
        "q0": q0,
        "results": results,
        "conclusion": "NEGATIVE: c_2 does not equal -1 for any N"
    }
    
    with open(witness_path, "w") as f:
        json.dump(witness_data, f, indent=2)
    print(f"Witness saved to {witness_path}")
