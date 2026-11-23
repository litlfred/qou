#!/usr/bin/env python3
"""Heat-kernel time as RG time: sign of the colour one-loop coefficient (bean qou-bwwr).

Pre-registered in PREREGISTRATION-heat-kernel-beta0-sign.md (commit 58c6511cf52, pushed before
this file existed).  Constructions C1, C2, C3 and the side check C1' exactly as registered.

Exact arithmetic only: sympy rational functions in q, Fraction for classical numbers.  mpmath
only for a read-out at the proton pin q0 = qou_substrate.constants.Q_MP.  No float anywhere.
No measured value enters; QCD beta0 is quoted for comparison only.  No gluon is selected.
"""
from __future__ import annotations

import itertools
import json
import os
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
q = sp.Symbol("q", positive=True)
h = q - 1 / q
N = 3
CHECKS = []


def check(name, ok):
    CHECKS.append({"check": name, "pass": bool(ok)})
    if not ok:
        raise AssertionError(name)


def qint(k):
    return sp.cancel((q**k - q**(-k)) / (q - 1 / q))


def contents(lam):
    return [j - i for i, row in enumerate(lam) for j in range(row)]


def mu(lam):
    """Corpus Reeb-holonomy Laplacian eigenvalue sum [c][c+1]_q."""
    return sp.factor(sp.cancel(sum(qint(c) * qint(c + 1) for c in contents(lam))))


def mu_classical(lam):
    return sum(Fraction(c * (c + 1)) for c in contents(lam))


def casimir_sl3(lam):
    """Quadratic Casimir of the sl3 irrep with highest weight lam (gl3 partition), C_F = 4/3."""
    lam = list(lam) + [0] * (N - len(lam))
    n = sum(lam)
    s = sum(Fraction(lam[i] * (lam[i] - 2 * (i + 1) + N + 1)) for i in range(N))
    return s / 2 - Fraction(n * n, 2 * N)


def dimq_gl3(lam):
    lam = list(lam) + [0] * (N - len(lam))
    num = 1
    den = 1
    for i in range(N):
        for j in range(i + 1, N):
            num *= qint(lam[i] - lam[j] + j - i)
            den *= qint(j - i)
    return sp.factor(sp.cancel(num / den))


def n_syt(lam):
    n = sum(lam)
    hooks = 1
    lamc = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    for i, row in enumerate(lam):
        for j in range(row):
            hooks *= (row - j - 1) + (lamc[j] - i - 1) + 1
    return int(sp.factorial(n)) // hooks


# ---------------------------------------------------------------- checks of the setting
check("Casimir: fundamental = C_F = 4/3", casimir_sl3((1,)) == Fraction(4, 3))
check("Casimir: adjoint (2,1) = C_A = 3", casimir_sl3((2, 1)) == 3)
check("Casimir: singlet (1,1,1) = 0", casimir_sl3((1, 1, 1)) == 0)
check("dim_q adjoint at q=1 is 8", sp.limit(dimq_gl3((2, 1)), q, 1) == 8)

# ---------------------------------------------------------------- C1 and C2
C1 = []
for k in range(1, 5):
    adj = (k + 1, k, k - 1) if k > 1 else (2, 1)
    sing = (k, k, k)
    d_mu = sp.factor(sp.cancel(mu(adj) - mu(sing)))
    b_c1 = sp.factor(-d_mu)
    b_c1_cl = -(mu_classical(adj) - mu_classical(sing))
    b_c2 = -(casimir_sl3(adj) - casimir_sl3(sing))
    check(f"k={k}: classical limit of C1 matches", sp.limit(b_c1, q, 1) == sp.Rational(b_c1_cl.numerator, b_c1_cl.denominator))
    check(f"k={k}: classical C1 = -6(k-1)", b_c1_cl == -6 * (k - 1))
    check(f"k={k}: C2 = -C_A = -3", b_c2 == -3)
    C1.append({
        "k": k, "adjoint": list(adj), "singlet": list(sing),
        "mu_adj": str(mu(adj)), "mu_sing": str(mu(sing)),
        "b_C1 = -(mu_adj - mu_sing)": str(b_c1),
        "b_C1 classical": str(b_c1_cl),
        "b_C2 = -(C(adj) - C(sing))": str(b_c2),
        "prefactor ratio dim_q*f": str(sp.factor(dimq_gl3(adj) * n_syt(adj) / (dimq_gl3(sing) * n_syt(sing)))),
    })
check("C1 k=1 is exactly zero (pre-registered)", C1[0]["b_C1 = -(mu_adj - mu_sing)"] == "0")
# general k closed form: -( f(k) - f(k-3) ), f(c) = [c][c+1]
kk = sp.Symbol("k", integer=True, positive=True)
gen = -(q**(2 * kk + 1) + q**(-2 * kk - 1) - q**(2 * kk - 5) - q**(-2 * kk + 5)) / h**2
for row in C1:
    check(f"closed form at k={row['k']}", sp.simplify(gen.subs(kk, row["k"]) - sp.sympify(row["b_C1 = -(mu_adj - mu_sing)"], locals={"q": q})) == 0)
# sign for q>1, k>=2: numerator q^{2k+1}+q^{-2k-1}-q^{2k-5}-q^{5-2k} = (q^{2k-2}-q^{2-2k})(q^3-q^{-3}) > 0
check("factorisation of the C1 numerator", sp.simplify((q**(2 * kk + 1) + q**(-2 * kk - 1) - q**(2 * kk - 5) - q**(-2 * kk + 5))
                                                      - (q**(2 * kk - 2) - q**(2 - 2 * kk)) * (q**3 - q**(-3))) == 0)

# post-hoc identity (found after the run, recorded as such): b_C1(k) = -[3]_q [2k-2]_q
for row in C1:
    check(f"post-hoc: b_C1(k={row['k']}) = -[3]_q[2k-2]_q", sp.simplify(sp.sympify(row["b_C1 = -(mu_adj - mu_sing)"], locals={"q": q}) + qint(3) * qint(2 * row["k"] - 2)) == 0)

# U(1) dependence: Delta_xi is not an sl3 invariant (same sl3 irrep, different k, different mu)
check("Delta_xi not an sl3 Casimir: mu(k+1,k,k-1)-mu(k,k,k) depends on k", C1[1]["b_C1 = -(mu_adj - mu_sing)"] != C1[2]["b_C1 = -(mu_adj - mu_sing)"])

# ---------------------------------------------------------------- explicit (C^3)^{(x)3}: verify mu, C1' side check
d = N
basis = list(itertools.product(range(d), repeat=3))
idx = {b: i for i, b in enumerate(basis)}


def Rhat_pair(i, j):
    """Jimbo braided R on e_i (x) e_j for U_q(gl3): returns dict {(a,b): coef}."""
    if i == j:
        return {(i, i): q}
    if i < j:
        return {(j, i): sp.Integer(1)}
    return {(j, i): sp.Integer(1), (i, j): h}


def sigma(pos):
    M = sp.zeros(27, 27)
    for b in basis:
        col = idx[b]
        a1, a2 = b[pos], b[pos + 1]
        for (x, y), c in Rhat_pair(a1, a2).items():
            nb = list(b)
            nb[pos], nb[pos + 1] = x, y
            M[idx[tuple(nb)], col] += c
    return M


s1, s2 = sigma(0), sigma(1)
I27 = sp.eye(27)
check("Hecke relation sigma1", (s1 - q * I27) * (s1 + I27 / q) == sp.zeros(27, 27))
check("braid relation", sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(27, 27))
s1i = s1 - h * I27
s2i = s2 - h * I27
L2, L3 = s1 * s1, s2 * s1 * s1 * s2
L2i, L3i = s1i * s1i, s2i * s1i * s1i * s2i
check("L2 inverse", sp.simplify(L2 * L2i - I27) == sp.zeros(27, 27))
Delta = ((q * L2 + L2i / q - (q + 1 / q) * I27) + (q * L3 + L3i / q - (q + 1 / q) * I27)) / h**2
Delta = Delta.applyfunc(sp.cancel)
# projectors via X = L2 + L3 (eigenvalues sum q^{2c})
X = (L2 + L3).applyfunc(sp.cancel)
ev = {(3,): q**2 + q**4, (2, 1): q**2 + q**-2, (1, 1, 1): q**-2 + q**-4}
P = {}
for lam, e in ev.items():
    M = I27
    for lam2, e2 in ev.items():
        if lam2 != lam:
            M = M * (X - e2 * I27) / (e - e2)
    P[lam] = M.applyfunc(sp.cancel)
mult = {(3,): 10, (2, 1): 16, (1, 1, 1): 1}
for lam in P:
    tr = sp.cancel(P[lam].trace())
    check(f"rank of isotypic {lam}", tr == mult[lam])
    check(f"Delta = mu on isotypic {lam}", (Delta * P[lam] - mu(lam) * P[lam]).applyfunc(sp.cancel) == sp.zeros(27, 27))
check("projectors sum to 1", (sum(P.values(), sp.zeros(27, 27)) - I27).applyfunc(sp.cancel) == sp.zeros(27, 27))

# C1' side check: F-coefficient of e^{-t Delta} = sum_lam e^{-t mu_lam} fCoef(P_lam);
# F = -(1/4)(C - C^2), C the cyclic permutation; <F,X> prop. tr(C^2 X) - tr(C X) (HS, C^dagger = C^2)
def perm_matrix(p):
    M = sp.zeros(27, 27)
    for b in basis:
        nb = tuple(b[p[i]] for i in range(3))
        M[idx[nb], idx[b]] = 1
    return M


Cyc = perm_matrix((1, 2, 0))
fpair = {}
for lam in P:
    val = sp.cancel((Cyc * Cyc * P[lam]).trace() - (Cyc * P[lam]).trace())
    fpair[str(lam)] = str(val)
    check(f"C1': F-component of P{lam} is zero", val == 0)

# ---------------------------------------------------------------- C3: (1/2) Tr_R H^2 per field
C3 = {
    "Casimir": {
        "gluon field (adjoint, dim 8)": str(Fraction(1, 2) * 8 * casimir_sl3((2, 1))**2),
        "quark field (fundamental, dim 3)": str(Fraction(1, 2) * 3 * casimir_sl3((1,))**2),
    },
    "Delta_xi": {
        "gluon field (adjoint realised as (2,1), dim 8)": str(sp.factor(sp.Rational(1, 2) * 8 * mu((2, 1))**2)),
        "quark field (fundamental realised as (1), dim 3)": str(sp.Rational(1, 2) * 3 * mu((1,))**2),
    },
}
check("C3: quark Delta_xi eigenvalue is 0 (one box, content 0)", mu((1,)) == 0)
check("C3: Casimir entries both > 0", Fraction(C3["Casimir"]["gluon field (adjoint, dim 8)"]) > 0
      and Fraction(C3["Casimir"]["quark field (fundamental, dim 3)"]) > 0)

# ---------------------------------------------------------------- proton pin read-out
import mpmath as mp
from qou_substrate.constants import Q_MP
mp.mp.dps = max(mp.mp.dps, 50)
pin = {}
for row in C1:
    expr = sp.sympify(row["b_C1 = -(mu_adj - mu_sing)"], locals={"q": q})
    f = sp.lambdify(q, expr, "mpmath")
    pin[f"b_C1 k={row['k']}"] = mp.nstr(f(mp.mpf(Q_MP)), 30)
check("C1 k=2 negative at q0", mp.mpf(pin["b_C1 k=2"]) < 0)
fg = sp.lambdify(q, sp.Rational(1, 2) * 8 * mu((2, 1))**2, "mpmath")
pin["C3 Delta_xi gluon"] = mp.nstr(fg(mp.mpf(Q_MP)), 30)

out = {
    "preregistration": "PREREGISTRATION-heat-kernel-beta0-sign.md @ 58c6511cf52",
    "convention": "t -> infinity is IR; b = d log g^2_eff / dt; b > 0 antiscreening, b < 0 screening",
    "C1_channel_ratio_Delta_xi": C1,
    "C1_general_k": "b_C1(k) = -(q^(2k-2) - q^(2-2k))(q^3 - q^(-3)) / (q - q^-1)^2 = -[3]_q [2k-2]_q  (= -6(k-1) at q=1); the [3] is the row-length shift k -> k-3, i.e. N",
    "C2_channel_ratio_casimir": "b_C2 = -C_A = -3 for every k",
    "C1prime_F_projection": {"<F, P_lam> up to the constant": fpair, "verdict": "F-projection of e^{-t Delta_xi} is 0 for all t, q"},
    "C3_log_coefficient_half_Tr_R_H2": C3,
    "proton_pin": {"q0": mp.nstr(mp.mpf(Q_MP), 30), **pin},
    "n_f": "cannot enter C1, C2 (fixed channel of fixed n); enters C3 only as an input multiplicity",
    "checks": CHECKS,
    "checks_passed": f"{sum(c['pass'] for c in CHECKS)}/{len(CHECKS)}",
}
with open(os.path.join(HERE, "qcd_heat_kernel_beta0_sign_probe.out.json"), "w") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print(json.dumps(out, indent=2, ensure_ascii=False))
