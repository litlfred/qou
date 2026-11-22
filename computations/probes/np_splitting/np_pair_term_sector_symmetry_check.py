"""Exact check of the relations behind QOU.QBeta.PairTermSectorSymmetry, over Q(q), n = 6.

J is the permutation matrix that flips every strand (u <-> d) and reverses the strand order.
D = Delta_A Delta_B is the product of the half twists sigma_lo sigma_{lo+1} sigma_lo in each block.
Checked as identities of 64 x 64 matrices over Q(q), with the Jimbo R-matrix of
np_all_q_symbolic_probe.py:

  (1) J R_i J = R_{4-i} for every generator and its inverse;
  (2) J C J = C^{-1} for the core C = V_A^3 V_B^3;
  (3) D C D^{-1} = C^{-1};
  (4) D commutes with every sector projector (it preserves each block's up-count);
  (6) the U_q pair Casimir (R-compatible coproduct) and the KZ monodromy M = beta_AB^2 are
      fixed by X -> D^{-1} J X J D, so pp = nn for them; the opposite-coproduct Casimir is not;
  (5) consequence: dE_X(Q_A, Q_B) = dE_{X'}(1 - Q_B, 1 - Q_A), X' = D^{-1} J X J D,
      on a fixed set of words X.

No float enters the arithmetic. Run from the repo root:
  PYTHONPATH=computations/probes/np_splitting python3 -u \
    computations/probes/np_splitting/np_pair_term_sector_symmetry_check.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import np_all_q_symbolic_probe as P  # noqa: E402
from np_all_q_symbolic_probe import (  # noqa: E402
    ONE, ZERO, GEN, CORE, bits, frombits, sp_eye, sp_mul, sp_add, word, readout, charge, casimir,
)

D = P.D


def perm_matrix(f):
    return {f(s): {s: ONE} for s in range(D)}


def eq(A, B):
    for i in set(A) | set(B):
        a, b = A.get(i, {}), B.get(i, {})
        for j in set(a) | set(b):
            if a.get(j, ZERO) != b.get(j, ZERO):
                return False
    return True


J = perm_matrix(lambda s: frombits([1 - x for x in reversed(bits(s))]))
C = word(CORE)
Cinv = word([(i, not inv) for i, inv in reversed(CORE)])
DELTA = [(0, False), (1, False), (0, False), (3, False), (4, False), (3, False)]
Dm = word(DELTA)
Dmi = word([(i, True) for i, _ in reversed(DELTA)])

def main():
    checks = {}
    checks["(1) J R_i J = R_{4-i}"] = all(
        eq(sp_mul(sp_mul(J, GEN[(i, inv)]), J), GEN[(4 - i, inv)]) for i in range(5) for inv in (False, True))
    checks["    C C^{-1} = 1"] = eq(sp_mul(C, Cinv), sp_eye())
    checks["(2) J C J = C^{-1}"] = eq(sp_mul(sp_mul(J, C), J), Cinv)
    checks["(3) D C D^{-1} = C^{-1}"] = eq(sp_mul(sp_mul(Dm, C), Dmi), Cinv)


    def sector(s):
        b = bits(s)
        return (charge(b, 0), charge(b, 3))


    checks["(4) D preserves sectors"] = all(
        sector(r) == sector(c) for r, row in Dm.items() for c in row)

    T1 = readout(sp_eye())
    WORDS = [
        [(2, False)], [(2, True)], [(1, False), (2, True)], [(2, False), (3, True)],
        [(0, False), (2, False), (4, True)], [(1, True), (2, False), (3, False), (2, True)],
        [(4, False), (3, True), (2, False), (1, False), (0, True)],
    ]
    ok5 = True
    for w in WORDS:
        X = word(w)
        Xp = sp_mul(sp_mul(Dmi, sp_mul(sp_mul(J, X), J)), Dm)
        TX, TXp = readout(X), readout(Xp)
        for (qa, qb), v in T1.items():
            if not v:
                continue
            key = (1 - qb, 1 - qa)
            if TX.get((qa, qb), ZERO) / v != TXp.get(key, ZERO) / T1[key]:
                ok5 = False
    checks[f"(5) dE symmetric on {len(WORDS)} words"] = ok5

    A_, B_, AB_ = [0, 1, 2], [3, 4, 5], list(range(6))

    def fixed(X):
        return eq(sp_mul(sp_mul(Dmi, sp_mul(sp_mul(J, X), J)), Dm), X)

    for op in (False, True):
        X = sp_add([(ONE, casimir(AB_, op)), (-ONE, casimir(A_, op)), (-ONE, casimir(B_, op))])
        name = "(6) G-q, R-compatible coproduct, fixed" if not op else "(6) control: G-q, opposite coproduct, NOT fixed"
        checks[name] = fixed(X) if not op else not fixed(X)
    beta = word([(2, False), (1, False), (0, False), (3, False), (2, False), (1, False),
                 (4, False), (3, False), (2, False)])
    checks["(6) KZ monodromy M fixed"] = fixed(sp_mul(beta, beta))

    for k, v in checks.items():
        print(f"{k}: {v}")
    print("ALL PASS" if all(checks.values()) else "FAIL")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
