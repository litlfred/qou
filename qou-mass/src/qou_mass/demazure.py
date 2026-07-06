import math
import numpy as np

def q_pochhammer(q, k):
    """Computes the finite q-Pochhammer symbol (q; q)_k"""
    if k == 0:
        return 1.0
    res = 1.0
    for i in range(1, k + 1):
        res *= (1.0 - q**i)
    return res

def evaluate_composite_1(q, u, max_k=4):
    """
    Evaluates Composite 1: Demazure x q-Pochhammer mixed trace
    F(u) = \sum_w D_w(\lambda) * (q; q)_{l(w)} * u^{l(w)}
    """
    # TODO: Implement the Demazure character generation
    pass

if __name__ == "__main__":
    q0 = 1.10998
    u = 0.00852
    print("q-Pochhammer (q0; q0)_3 =", q_pochhammer(q0, 3))
