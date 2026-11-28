"""Range of the three-strand ring mass of def:mass-identity over odd 3-braid words.

Thread "Derive the tau lepton's word", hierarchy follow-up (2026-11-28). Exact sympy
arithmetic in Q(q); the evaluation at the substrate q0 is display only (mpmath, 30 dps).
Nothing is compared with measurement. Lean: QOU/Observations/LeptonMassGrowthBound.lean.

m(beta) = [2]^3 q^{-2w} (y3 q^w + y21 tr rho21(beta)),  y3 = 1 - 2/[2]^2, y21 = 1/[2]^2.
"""
import itertools
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
q = sp.symbols("q")
GEN = {1: sp.Matrix([[q, 1], [0, -1 / q]]), 2: sp.Matrix([[-1 / q, 0], [1, q]])}
INV = {k: v.inv() for k, v in GEN.items()}
B = q + 1 / q
Y3, Y21 = 1 - 2 / B**2, 1 / B**2
Q0 = sp.Rational("1.1099785827513808")  # proton pin (qou_substrate.constants.Q)


def mass(word):
    M = sp.eye(2)
    for g in word:
        M = M * (GEN[g] if g > 0 else INV[-g])
    w = sum(1 if g > 0 else -1 for g in word)
    return sp.cancel(B**3 * q ** (-2 * w) * (Y3 * q**w + Y21 * M.trace()))


def main(max_len=7):
    checks = []
    e = sp.factor(mass((1, 2, 1)))
    checks.append(("electron [4]/q^3", sp.simplify(e - (q**2 + 1) * (q**4 + 1) / q**6) == 0))
    # recurrence on sigma_1 sigma_2^{-k}
    fam = [sp.cancel(mass((1,) + (-2,) * k)) for k in range(1, 7)]
    rec = all(sp.simplify(fam[k + 2] + q * (q**2 - 1) * fam[k + 1] - q**4 * fam[k]) == 0
              for k in range(4))
    checks.append(("recurrence m_{k+2} = -q(q^2-1) m_{k+1} + q^4 m_k", rec))
    me = mp.mpf(str(sp.N(e.subs(q, Q0), 30)))
    for L in range(1, max_len + 1, 2):
        vals = []
        for w in itertools.product([1, -1, 2, -2], repeat=L):
            if any(w[i] == -w[i + 1] for i in range(L - 1)):
                continue
            vals.append(abs(mp.mpf(str(sp.N(mass(w).subs(q, Q0), 30)))))
        print(f"length {L}: |m| at q0 in [{mp.nstr(min(vals), 6)}, {mp.nstr(max(vals), 6)}],"
              f" max / m_e = {mp.nstr(max(vals) / me, 6)}  (display only)")
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    return all(ok for _, ok in checks)


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
