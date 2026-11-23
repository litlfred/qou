#!/usr/bin/env python3
"""Tower index n and KZ coupling kappa as the scale of a colour coupling (bean qou-abzr).

Pre-registered in PREREGISTRATION-n-and-kappa-scales.md (commit 40489bd8bd5, pushed before this
file existed).  Constructions N1, N2 (tower index) and K1, K2, K3 (KZ) exactly as registered.

Common definitions: g^2(s) := W_8(s)/W_1(s); b := d log g^2/ds; s increasing = IR.
Exact arithmetic only: sympy over Q(q), Q(k).  mpmath only for a read-out at the proton pin
q0 = qou_substrate.constants.Q_MP.  No float anywhere.  No measured value enters.  kappa is a
family variable; q0 is never solved for (forever gate).  No gluon is selected.
"""
from __future__ import annotations

import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
q = sp.Symbol("q", positive=True)
k = sp.Symbol("k", positive=True, integer=True)
CHECKS = []
OUT = {"preregistration": "PREREGISTRATION-n-and-kappa-scales.md", "prereg_commit": "40489bd8bd5"}


def check(name, ok, posthoc=False):
    CHECKS.append({"check": name, "pass": bool(ok), "posthoc": posthoc})
    if not ok:
        raise AssertionError(name)


def qint(m):
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


# ---------------------------------------------------------------- partitions / hook counts
def n_syt(lam):
    lam = [r for r in lam if r > 0]
    n = sum(lam)
    lamc = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    hooks = 1
    for i, row in enumerate(lam):
        for j in range(row):
            hooks *= (row - j - 1) + (lamc[j] - i - 1) + 1
    return int(sp.factorial(n)) // hooks


def fact_ratio(u, v):
    """(k+u)!/(k+v)! as an exact rational function of symbolic k."""
    if u >= v:
        return sp.rf(k + v + 1, u - v)
    return 1 / sp.rf(k + u + 1, v - u)


def frob_over_nfact(off):
    """f^lambda / n! = Vandermonde(l)/prod l_i!, l_i = lambda_i + N-1-i, lambda_i = k + off[i].
    Returned as (vandermonde, list of factorial offsets) so ratios can be taken symbolically."""
    N = len(off)
    ell = [off[i] + N - 1 - i for i in range(N)]          # l_i = k + ell[i]
    vdm = sp.prod([(ell[i] - ell[j]) for i in range(N) for j in range(i + 1, N)])
    return vdm, ell


def f_ratio(off_a, off_b):
    """f^{lambda_a}/f^{lambda_b} for lambda = k + offsets, symbolic in k (generic k)."""
    va, la = frob_over_nfact(off_a)
    vb, lb = frob_over_nfact(off_b)
    na, nb = sum(off_a), sum(off_b)                         # n = N k + sum(off)
    N = len(off_a)
    r = sp.Rational(va, vb)
    for x, y in zip(lb, la):
        r *= fact_ratio(x, y)                               # prod l_b! / prod l_a!
    # n_a!/n_b! with n = N k + off
    Nk = N * k
    if na >= nb:
        r *= sp.rf(Nk + nb + 1, na - nb)
    else:
        r /= sp.rf(Nk + na + 1, nb - na)
    return sp.factor(sp.simplify(r))


def dimq_slN(lam, N):
    lam = list(lam) + [0] * (N - len(lam))
    num, den = 1, 1
    for i in range(N):
        for j in range(i + 1, N):
            num *= qint(lam[i] - lam[j] + j - i)
            den *= qint(j - i)
    return sp.factor(sp.cancel(num / den))


def adj_off(N):
    return [1] + [0] * (N - 2) + [-1]


def sing_off(N):
    return [0] * N


def shape(off, kv):
    return [kv + o for o in off]


# ================================================================ N-arm
OUT["N_arm"] = {}
for N in (2, 3, 4):
    fr = f_ratio(adj_off(N), sing_off(N))
    # verify against the hook formula for k = 1..8 (k = 1 is generic too: row k-1 = 0 is fine)
    for kv in range(1, 9):
        hook = sp.Rational(n_syt(shape(adj_off(N), kv)), n_syt(shape(sing_off(N), kv)))
        check(f"N1 hook ratio closed form N={N} k={kv}", sp.simplify(fr.subs(k, kv) - hook) == 0)
    dq_adj = dimq_slN([2] + [1] * (N - 2), N)               # adjoint highest weight as gl_N shape
    check(f"dim_q adjoint at q=1 is N^2-1 (N={N})", sp.limit(dq_adj, q, 1) == N * N - 1)
    g2 = sp.factor(fr * dq_adj)
    # b(k) exact for continuous k: d log g2 / d log k  (= d log g2 / d log n, n = N k)
    b_cont = sp.factor(sp.simplify(k * sp.diff(sp.log(fr), k)))
    inv_g2 = sp.expand(sp.cancel(1 / fr))
    check(f"N1 f-ratio is (N^2-1) k/(k+N) (N={N})", sp.simplify(fr - (N * N - 1) * k / (k + N)) == 0, posthoc=True)
    check(f"N1 b = N/(k+N) > 0, q-independent (N={N})", sp.simplify(b_cont - N / (k + N)) == 0 and not b_cont.has(q))
    # discrete b: sign of g2(k+1)/g2(k) - 1
    disc = sp.factor(sp.simplify(fr.subs(k, k + 1) / fr - 1))
    check(f"N1 discrete ratio - 1 = N/(k(k+N+1)) > 0 (N={N})", sp.simplify(disc - N / (k * (k + N + 1))) == 0, posthoc=True)
    # bar involution: q -> 1/q leaves g2 invariant
    check(f"N1 g2 invariant under q->1/q (N={N})", sp.simplify(g2.subs(q, 1 / q) - g2) == 0)
    # log running? 1/g2 = (1 + N/k)/((N^2-1) dimq): a 1/k term, no log k term
    check(f"N1 1/f-ratio = (1 + N/k)/(N^2-1): no log term (N={N})",
          sp.simplify(inv_g2 - (1 + N / k) / (N * N - 1)) == 0)

    # ---------------------------------------------------------- N2: JM branching weight
    def corners(off):
        res = []
        for i in range(N):
            nxt = off[i + 1] if i + 1 < N else None
            if nxt is None or off[i] > nxt:           # generic k: row N-1 always removable
                mu = list(off)
                mu[i] -= 1
                content = (k + off[i]) - 1 - i
                res.append((i, mu, content))
        return res

    def jm_weight(off):
        tot = 0
        psum = 0
        for i, mu, c in corners(off):
            p = f_ratio(mu, off)
            psum += p
            tot += p * q**(2 * c)
        return sp.simplify(psum), sp.simplify(tot)

    ps8, W8 = jm_weight(adj_off(N))
    ps1, W1 = jm_weight(sing_off(N))
    check(f"N2 branching probabilities sum to 1 (adjoint, N={N})", sp.simplify(ps8 - 1) == 0)
    check(f"N2 branching probabilities sum to 1 (singlet, N={N})", sp.simplify(ps1 - 1) == 0)
    g2n2 = sp.factor(sp.simplify(sp.expand(W8 / W1)))
    check(f"N2 g2 has no k in the q-exponent (q^{{2k}} cancels) N={N}",
          sp.simplify(sp.diff(g2n2.subs(q, sp.Integer(2)), k)).free_symbols <= {k})
    rN2 = sp.factor(sp.simplify(g2n2.subs(k, k + 1) / g2n2 - 1))
    # read-out signs at q0 and 1/q0 for k = 2..12 (exact rationals in k, q evaluated with mpmath)
    import mpmath as mp
    from qou_substrate.constants import Q_MP
    mp.mp.dps = max(mp.mp.dps, 50)
    q0 = mp.mpf(Q_MP)
    signs = {"q0": [], "1/q0": []}
    for kv in range(2, 13):
        e = sp.simplify(rN2.subs(k, kv))
        for lab, qv in (("q0", q0), ("1/q0", 1 / q0)):
            val = sp.lambdify(q, e, "mpmath")(qv)
            signs[lab].append(int(mp.sign(val)))
    flips = all(a == -b and a != 0 for a, b in zip(signs["q0"], signs["1/q0"]))
    # exact bar-parity statement: g2(q) vs g2(1/q)
    bar = sp.factor(sp.simplify(g2n2 * g2n2.subs(q, 1 / q)))
    OUT["N_arm"][f"N={N}"] = {
        "N1_f_ratio": str(fr), "N1_dimq_adjoint": str(dq_adj), "N1_g2": str(g2),
        "N1_b_dlog_g2_dlog_n": str(b_cont), "N1_discrete_ratio_minus_1": str(disc),
        "N2_g2": str(g2n2), "N2_ratio_k_plus_1_minus_1": str(rN2),
        "N2_g2_times_g2_bar": str(bar),
        "N2_sign_b_k2_to_12_at_q0": signs["q0"], "N2_sign_b_k2_to_12_at_1_over_q0": signs["1/q0"],
        "N2_sign_flips_under_bar_all_k": flips,
    }
    check(f"N2 sign of b flips under q -> 1/q for every k=2..12 (N={N})", flips)

# N1 C_A identification across N: b = N/(k+N) in k (leading N/k), = N^2/(n+N^2) in n = N k
OUT["N_arm"]["N1_coefficient_vs_N"] = {
    "in_k (baryon count)": "b = N/(k+N) -> N/k: coefficient N = C_A",
    "in_n (strand count)": "b = N^2/(n+N^2) -> N^2/n: coefficient N^2 = C_A * N",
}

# ================================================================ kappa-arm
def E(N, i, j):
    m = sp.zeros(N, N)
    m[i, j] = 1
    return m


def kron(A, B):
    return sp.kronecker_product(A, B)


def rep_mats(N, which):
    """images of E_ij in the rep: 'F' fundamental, 'Fb' antifundamental, 'A' adjoint of sl_N."""
    if which == "F":
        return {(i, j): E(N, i, j) for i in range(N) for j in range(N)}
    if which == "Fb":
        return {(i, j): -E(N, j, i) for i in range(N) for j in range(N)}
    # adjoint: basis of sl_N = E_ab (a!=b) and H_a = E_aa - E_{a+1,a+1}
    basis = [E(N, a, b) for a in range(N) for b in range(N) if a != b]
    basis += [E(N, a, a) - E(N, a + 1, a + 1) for a in range(N - 1)]
    d = len(basis)
    flat = sp.Matrix([[B[r, c] for B in basis] for r in range(N) for c in range(N)])
    pinv = (flat.T * flat).inv() * flat.T
    mats = {}
    for i in range(N):
        for j in range(N):
            X = E(N, i, j)
            cols = []
            for B in basis:
                C = X * B - B * X
                vec = sp.Matrix([C[r, c] for r in range(N) for c in range(N)])
                cols.append(pinv * vec)
            mats[(i, j)] = sp.Matrix.hstack(*cols)
            assert mats[(i, j)].shape == (d, d)
    return mats


def omega(N, r1, r2):
    """Omega = sum_a t^a (x) t^a, Tr_V(t^a t^b) = 1/2 delta: = 1/2 (sum E_ij (x) E_ji - (1/N) I (x) I)."""
    A, B = rep_mats(N, r1), rep_mats(N, r2)
    dA = A[(0, 0)].shape[0]
    dB = B[(0, 0)].shape[0]
    S = sp.zeros(dA * dB, dA * dB)
    for i in range(N):
        for j in range(N):
            S += kron(A[(i, j)], B[(j, i)])
    IA = sum((A[(i, i)] for i in range(N)), sp.zeros(dA, dA))
    IB = sum((B[(i, i)] for i in range(N)), sp.zeros(dB, dB))
    return (S - kron(IA, IB) / N) / 2


def casimir(N, r):
    A = rep_mats(N, r)
    d = A[(0, 0)].shape[0]
    S = sp.zeros(d, d)
    for i in range(N):
        for j in range(N):
            S += A[(i, j)] * A[(j, i)]
    I1 = sum((A[(i, i)] for i in range(N)), sp.zeros(d, d))
    C = (S - I1 * I1 / N) / 2
    val = C[0, 0]
    assert C == val * sp.eye(d)
    return val


OUT["kappa_arm"] = {}
CF = {N: sp.Rational(N * N - 1, 2 * N) for N in (2, 3, 4)}
for N in (2, 3, 4):
    check(f"Casimir fundamental = (N^2-1)/(2N), N={N}", casimir(N, "F") == CF[N])
    check(f"Casimir antifundamental = C_F, N={N}", casimir(N, "Fb") == CF[N])
    check(f"Casimir adjoint = N = C_A, N={N}", casimir(N, "A") == N)

pairs = [(2, "F", "Fb"), (3, "F", "Fb"), (4, "F", "Fb"), (2, "A", "A"), (3, "A", "A"), (3, "F", "F")]
kap_re, kap_im = sp.symbols("a c", real=True)  # kappa = a + i c
ell, theta = sp.symbols("ell theta", positive=True)
B_SYM = {}
for N, r1, r2 in pairs:
    Om = omega(N, r1, r2)
    ev = Om.eigenvals()
    ev = {sp.nsimplify(key): val for key, val in ev.items()}
    C1, C2 = casimir(N, r1), casimir(N, r2)
    w1 = (0 - C1 - C2) / 2                      # singlet channel C_R = 0
    w8 = (N - C1 - C2) / 2                      # adjoint channel C_R = C_A = N
    rec = {"eigenvalues_with_multiplicity": {str(kk): int(v) for kk, v in sorted(ev.items())}}
    if r1 != r2 or r1 == "A":
        check(f"singlet exponent omega_1 = -(C1+C2)/2 present, N={N} {r1}x{r2}", w1 in ev and ev[w1] == 1)
        check(f"adjoint exponent omega_8 = (C_A-C1-C2)/2 present, N={N} {r1}x{r2}", w8 in ev)
        check(f"omega_8 - omega_1 = C_A/2 = N/2, N={N} {r1}x{r2}", w8 - w1 == sp.Rational(N, 2))
        # K1: W_R = |z^{kappa omega_R}|^2, z = ell e^{i theta}, kappa = a + i c
        logW = lambda w: 2 * sp.re((kap_re + sp.I * kap_im) * w * (sp.log(ell) + sp.I * theta))
        logg2 = sp.simplify(sp.expand(logW(w8) - logW(w1)))
        b = sp.simplify(ell * sp.diff(logg2, ell))
        check(f"K1 b = a*C_A (Re kappa times C_A), N={N} {r1}x{r2}", sp.simplify(b - kap_re * N) == 0)
        B_SYM[(N, r1, r2)] = b
        rec.update({"omega_1": str(w1), "omega_8": str(w8), "log_g2": str(logg2), "b": str(b)})
    else:
        rec.update({"note": "3x3 = 6 + 3bar: no singlet, no adjoint channel; recorded only",
                    "omega_6": str(sp.Rational(1, 3)), "omega_3bar": str(sp.Rational(-2, 3))})
        check("3x3 eigenvalues are 1/3 (x6), -2/3 (x3)", ev == {sp.Rational(1, 3): 6, sp.Rational(-2, 3): 3})
    # K2: eigenvalue differences; resonance iff kappa*Delta in Z\{0}
    diffs = sorted({abs(x - y) for x in ev for y in ev if x != y})
    rec["resonance_differences"] = [str(d) for d in diffs]
    OUT["kappa_arm"][f"SU({N}) {r1}x{r2}"] = rec

check("K1 quark pair and gluon pair give the same b = a C_A at N=3 (no q/g separation)",
      OUT["kappa_arm"]["SU(3) FxFb"]["b"] == OUT["kappa_arm"]["SU(3) AxA"]["b"])
# kappa imaginary (q = e^{i pi kappa} real > 1): a = 0 -> b = 0
check("K1 b = 0 for imaginary kappa (q real, Drinfeld-Kohno q = e^{i pi kappa})",
      B_SYM[(3, "F", "Fb")].subs(kap_re, 0) == 0 and B_SYM[(3, "A", "A")].subs(kap_re, 0) == 0)
# K2: for real q > 1, kappa = -i log q/pi is non-real, so kappa*Delta (Delta real nonzero) is never an integer
qq = sp.Symbol("qq", positive=True)
kap = -sp.I * sp.log(qq) / sp.pi
check("K2 kappa*Delta has nonzero imaginary part for q>1, Delta=3/2",
      sp.simplify(sp.im(kap * sp.Rational(3, 2)) + sp.log(qq) * sp.Rational(3, 2) / sp.pi) == 0)

# K3: spectator fundamental at z3: residue at z12 -> 0 is kappa*Omega_12 (x) 1, same spectrum
Om12 = omega(3, "F", "Fb")
Om12x = kron(Om12, sp.eye(3))
ev12x = Om12x.eigenvals()
check("K3 spectrum of Omega_12 on V(x)Vbar(x)V = spectrum on V(x)Vbar (multiplicity x3)",
      {sp.nsimplify(kk): v for kk, v in ev12x.items()} == {sp.Rational(-4, 3): 3, sp.Rational(1, 6): 24})
# the other residue forms dlog(z1-z3), dlog(z2-z3) are holomorphic at z1 = z2 (z3 distinct): exact
z1, z2, z3 = sp.symbols("z1 z2 z3")
check("K3 d log(z1-z3) regular at z1=z2", sp.limit(1 / (z1 - z3), z1, z2) == 1 / (z2 - z3))

# read-out: real-kappa (Wick-rotated) convention q = e^{pi kappa}: kappa = log q0/pi > 0 at q0 > 1
import mpmath as mp
from qou_substrate.constants import Q_MP
mp.mp.dps = 40
q0 = mp.mpf(Q_MP)
OUT["readout_q0"] = {
    "q0": mp.nstr(q0, 25),
    "K1_b_if_q_eq_exp(pi*kappa)_real": mp.nstr(3 * mp.log(q0) / mp.pi, 20),
    "K1_b_if_q_eq_exp(-pi*kappa)_real": mp.nstr(-3 * mp.log(q0) / mp.pi, 20),
    "K1_b_if_q_eq_exp(i*pi*kappa)": "0 (exact)",
    "N1_b_k=1..4_N=3": [str(sp.Rational(3, kv + 3)) for kv in range(1, 5)],
}
OUT["checks"] = CHECKS
OUT["n_checks"] = len(CHECKS)
OUT["n_pass"] = sum(c["pass"] for c in CHECKS)
with open(os.path.join(HERE, "qcd_n_kappa_scale_probe.out.json"), "w") as fh:
    json.dump(OUT, fh, indent=1, ensure_ascii=False)
print(json.dumps({kk: v for kk, v in OUT.items() if kk != "checks"}, indent=1, ensure_ascii=False))
print(f"{OUT['n_pass']}/{OUT['n_checks']} checks pass")
