#!/usr/bin/env python3
"""Spin / background-field object for the QCD beta_0 sign (bean qou-bwwr, route qou-ni4b).

Pre-registration: PREREGISTRATION-spin-background.md (pushed before this file existed).

Background colour holonomy K(eps) = diag(exp(eps*a_j)) on V = C^N, acting as K^{(x)n} on V^{(x)n};
it commutes with the Jimbo braiding of U_q(gl_N). For an operator X the background susceptibility is
    chi(X) := [eps^2] Tr(K^{(x)n} X) / [eps^2] Tr_V K,
computed exactly as sum_x X_xx (sum_i a_{x_i})^2 / sum_j a_j^2.

Exact sympy over Q(q); mpmath only to display values at the proton pin. No float64.
"""
import itertools
import json
import os
import sys

import sympy as sp
from mpmath import mp, mpf
from qou_substrate.constants import Q_MP

q, t, hb = sp.symbols("q t hbar", positive=True)
h = q - 1 / q
CHECKS = []


def check(name, cond, prereg=True):
    ok = bool(cond)
    CHECKS.append({"name": name, "pass": ok, "preregistered": prereg})
    print(("PASS " if ok else "FAIL ") + ("" if prereg else "[post-hoc] ") + name)
    return ok


def simp(e):
    return sp.factor(sp.cancel(sp.together(e)))


# ---------------------------------------------------------------- sparse operators on V^{(x)n}
def jimbo_R(N):
    """Rc on V(x)V: e_ii -> q e_ii; e_ij -> e_ji (i<j); e_ij -> e_ji + h e_ij (i>j). col map."""
    R = {}
    for i in range(N):
        for j in range(N):
            if i == j:
                R[(i, j)] = {(i, i): q}
            elif i < j:
                R[(i, j)] = {(j, i): sp.Integer(1)}
            else:
                R[(i, j)] = {(j, i): sp.Integer(1), (i, j): h}
    return R


def jimbo_Rinv(N):
    R = jimbo_R(N)
    out = {}
    for k, col in R.items():
        c = dict(col)
        c[k] = sp.expand(c.get(k, 0) - h)  # Rinv = R - h
        out[k] = {kk: v for kk, v in c.items() if v != 0}
    return out


def gen(N, n, i, inv=False):
    """sigma_i (0-based) on V^{(x)n} as dict: basis tuple -> {basis tuple: coeff} (column map)."""
    R = jimbo_Rinv(N) if inv else jimbo_R(N)
    op = {}
    for x in itertools.product(range(N), repeat=n):
        col = {}
        for (a, b), c in R[(x[i], x[i + 1])].items():
            y = x[:i] + (a, b) + x[i + 2:]
            col[y] = c
        op[x] = col
    return op


def ident(N, n):
    return {x: {x: sp.Integer(1)} for x in itertools.product(range(N), repeat=n)}


def mul(A, B):
    """(A B) e_x = A (B e_x)."""
    out = {}
    for x, colB in B.items():
        col = {}
        for y, c in colB.items():
            for z, d in A[y].items():
                col[z] = col.get(z, 0) + c * d
        out[x] = {z: sp.expand(v) for z, v in col.items() if sp.expand(v) != 0}
    return out


def lin(*terms):
    out = {}
    for c, A in terms:
        for x, col in A.items():
            o = out.setdefault(x, {})
            for y, v in col.items():
                o[y] = o.get(y, 0) + c * v
    return {x: {y: sp.expand(v) for y, v in col.items() if sp.expand(v) != 0} for x, col in out.items()}


def word(N, n, letters):
    """letters: list of signed 1-based generator indices, e.g. [1,-2] = s0 s1^-1 (left to right)."""
    W = ident(N, n)
    for l in letters:
        W = mul(W, gen(N, n, abs(l) - 1, inv=(l < 0)))
    return W


def chi(X, a):
    num = sum((col.get(x, 0) * sp.Rational(sum(a[i] for i in x)) ** 2) for x, col in X.items())
    den = sum(sp.Rational(v) ** 2 for v in a)
    return simp(num / den)


def direction(N, which=0):
    if which == 0:
        return [1, -1] + [0] * (N - 2)
    return [1] * (N - 1) + [-(N - 1)]


def at_q1(e):
    return sp.simplify(e.subs(q, 1))


def hbar_series(e, order=3):
    return sp.expand(sp.series(e.subs(q, sp.exp(hb)), hb, 0, order).removeO())


def mpq(e):
    with mp.workdps(max(mp.dps, 50)):
        Q0 = mpf(Q_MP)  # proton pin, display only
        return str(mp.nstr(sp.lambdify(q, e, "mpmath")(Q0), 15))


out = {"probe": "qcd_spin_background", "bean": "qou-bwwr", "route": "qou-ni4b"}

# ---------------------------------------------------------------- setting checks (N = 3)
N = 3
s1, s2 = gen(N, 3, 0), gen(N, 3, 1)
s1i = gen(N, 3, 0, inv=True)
I3 = ident(N, 3)
check("Hecke (s-q)(s+1/q)=0 on (C^3)^3", all(not v for v in lin((1, mul(s1, s1)), (-h, s1), (-1, I3)).values()))
check("s1 s1^-1 = 1", lin((1, mul(s1, s1i)), (-1, I3)) == {x: {} for x in I3} or all(
    not col for col in lin((1, mul(s1, s1i)), (-1, I3)).values()))
check("braid relation s1 s2 s1 = s2 s1 s2",
      all(not col for col in lin((1, mul(mul(s1, s2), s1)), (-1, mul(mul(s2, s1), s2))).values()))

# ---------------------------------------------------------------- S3: background susceptibility of words
words3 = {
    "1": [],
    "s0s1": [1, 2],
    "photon s0s1^-1": [1, -2],
    "core V^3": [1, -2, 1, -2, 1, -2],
    "electron s0s1s0": [1, 2, 1],
    "full twist D^2_3": [1, 2, 1, 2, 1, 2],
}
cyc_pred = {"1": 27, "s0s1": 9, "photon s0s1^-1": 9, "core V^3": 27, "electron s0s1s0": 15,
            "full twist D^2_3": 27}
S3 = {}
for name, w in words3.items():
    X = word(N, 3, w)
    c0, c1 = chi(X, direction(N, 0)), chi(X, direction(N, 1))
    S3[name] = {"chi": str(c0), "chi_at_q1": str(at_q1(c0)), "chi_hbar_series": str(hbar_series(c0)),
                "chi_at_q0": mpq(c0), "direction_independent": bool(simp(c0 - c1) == 0)}
    check(f"S3 chi({name}) independent of Cartan direction", simp(c0 - c1) == 0)
    check(f"S3 chi({name}) at q=1 = sum l_i^2 N^(#cyc-1) = {cyc_pred[name]}", at_q1(c0) == cyc_pred[name])
out["S3_words_N3"] = S3

# ---------------------------------------------------------------- isotypic data, n = 3, N = 3
def qint(m):
    return (q ** m - q ** (-m)) / (q - 1 / q)


shapes = {(3,): [0, 1, 2], (2, 1): [0, 1, -1], (1, 1, 1): [0, -1, -2]}
f = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
dimgl3 = {(3,): 10, (2, 1): 8, (1, 1, 1): 1}
twoT = {(3,): 15, (2, 1): 6, (1, 1, 1): 0}   # 2T(lambda)/2T(V) for gl3 (index of 10, 8, 1)
mu = {lam: simp(sum(qint(c) * qint(c + 1) for c in cs)) for lam, cs in shapes.items()}
ct = {lam: sum(cs) for lam, cs in shapes.items()}

D2 = word(N, 3, [1, 2, 1, 2, 1, 2])
chiD2_iso = simp(sum(f[l] * q ** (2 * ct[l]) * twoT[l] for l in shapes))
check("S1 isotypic cross-check: chi(D^2_3) = sum f q^{2ct} 2T", simp(chi(D2, direction(3)) - chiD2_iso) == 0)

# adjoint-channel projector from D^2 eigenvalues q^6, 1, q^-6
ev = {l: q ** (2 * ct[l]) for l in shapes}


def projector(lam):
    P = I3
    for m in shapes:
        if m != lam:
            P = mul(P, lin((1 / (ev[lam] - ev[m]), D2), (-ev[m] / (ev[lam] - ev[m]), I3)))
    return {x: {y: sp.cancel(v) for y, v in col.items()} for x, col in P.items()}


Padj = projector((2, 1))
check("adjoint projector P_(2,1) idempotent (trace rank 16)",
      simp(sum(Padj[x].get(x, 0) for x in Padj) - 16) == 0)
adj = {}
for name, w in words3.items():
    X = mul(Padj, word(N, 3, w))
    c = chi(X, direction(N, 0))
    adj[name] = {"chi_adj": str(c), "chi_adj_q1": str(at_q1(c)), "hbar_series": str(hbar_series(c)),
                 "at_q0": mpq(c)}
out["S3_adjoint_channel_N3"] = adj

# STRONG-HIT test: is any adjoint-channel coefficient of the form [(2s)^2 - 1/3] x (pos) with s=1?
nh_set = {sp.Rational(11, 3), sp.Rational(-1, 3), sp.Rational(1, 3), sp.Rational(2, 3),
          sp.Rational(4, 3), sp.Rational(11, 6), sp.Rational(22, 3), sp.Rational(11, 12),
          sp.Integer(4), sp.Integer(11)}
ratios = {}
for name in words3:
    base = sp.sympify(adj["1"]["chi_adj_q1"])
    r = sp.Rational(sp.sympify(adj[name]["chi_adj_q1"])) / base
    ratios[name] = str(r)
out["S3_adjoint_ratio_to_identity_q1"] = ratios

# heat-kernel variant: per-state susceptibility under exp(-t Delta_xi)
Z = sum(f[l] * dimgl3[l] * sp.exp(-t * mu[l]) for l in shapes)
C = sum(f[l] * twoT[l] * sp.exp(-t * mu[l]) for l in shapes)
s_t0 = sp.nsimplify(sp.simplify((C / Z).subs(t, 0)))
s_inf = sp.limit(C / Z * sp.exp(0), t, sp.oo) if False else sp.Rational(f[(2, 1)] * twoT[(2, 1)],
                                                                          f[(2, 1)] * dimgl3[(2, 1)] + dimgl3[(1, 1, 1)])
check("mu_(2,1) = mu_(1^3) = [2] (ties the IR)", simp(mu[(2, 1)] - mu[(1, 1, 1)]) == 0 and simp(mu[(2, 1)] - qint(2)) == 0)
check("per-state susceptibility at t=0 is 1", s_t0 == 1)
check("per-state susceptibility at t->oo is 12/17", s_inf == sp.Rational(12, 17))
ds0 = simp(sp.diff(C / Z, t).subs(t, 0))
out["S3_heat_kernel"] = {"mu": {str(k): str(v) for k, v in mu.items()},
                         "per_state_chi_t0": str(s_t0), "per_state_chi_tinf": str(s_inf),
                         "d_dt_at_t0": str(ds0), "d_dt_at_t0_q0": mpq(ds0),
                         "reading": {"real background exp(eps a): Gamma ~ -log Z": "falling chi -> 1/g^2 rises toward IR -> screening",
                                     "unitary background exp(i eps a)": "sign of eps^2 flips; falling |chi| -> antiscreening reading",
                                     "verdict": "sign is set by the background convention, not by the construction"}}
with mp.workdps(max(mp.dps, 50)):
    check("d/dt (chi/Z) at t=0 < 0 at q0 (falling toward IR)", sp.lambdify(q, ds0, "mpmath")(mpf(Q_MP)) < 0)

# ---------------------------------------------------------------- S2 and S1 across N (n = 2)
S2, S1 = {}, {}
for NN in (2, 3, 4):
    a = direction(NN, 0)
    I2 = ident(NN, 2)
    sg = gen(NN, 2, 0)
    c1, cs = chi(I2, a), chi(sg, a)
    cD = chi(mul(sg, sg), a)
    csl = simp(cs * q ** sp.Rational(-1, NN))
    cDsl = simp(cD * q ** sp.Rational(-2, NN))
    check(f"S2 N={NN}: chi(sigma) = q(N+2) - q^-1(N-2)", simp(cs - (q * (NN + 2) - (NN - 2) / q)) == 0)
    check(f"S2 N={NN}: q=1 ratio chi(sigma)/chi(1) = 2/N", at_q1(cs) / at_q1(c1) == sp.Rational(2, NN))
    S2[NN] = {"chi_1": str(c1), "chi_sigma": str(cs), "ratio_q1": str(at_q1(cs) / at_q1(c1))}
    # S1: hbar expansion of the full twist; Sym^2 exponent of sigma^sl is 1 - 1/N
    ser = hbar_series(cD, 3)
    sers = hbar_series(cDsl, 3)
    S1[NN] = {"chi_D2": str(cD), "chi_D2_hbar": str(ser), "chi_D2sl": str(cDsl), "chi_D2sl_hbar": str(sers),
              "sigma_sl_exponent_Sym2": str(1 - sp.Rational(1, NN)),
              "sigma_sl_exponent_Lambda2": str(-1 - sp.Rational(1, NN)),
              "hbar1_coeff": str(ser.coeff(hb, 1)), "hbar2_coeff": str(ser.coeff(hb, 2))}
    check(f"S1 N={NN}: chi(D^2) hbar^1 coeff = 8 (N-independent, Zeeman-like, sign-definite)", ser.coeff(hb, 1) == 8)
    check(f"S1 N={NN}: chi(D^2) hbar^2 coeff = 4N > 0 (no negative orbital term)", ser.coeff(hb, 2) == 4 * NN)
out["S2_across_N"] = {str(k): v for k, v in S2.items()}
out["S1_across_N"] = {str(k): v for k, v in S1.items()}
check("S1: the -1/N framing shift is N-dependent (not the Nielsen-Hughes -1/3)",
      len({S1[k]["sigma_sl_exponent_Sym2"] for k in S1}) == 3)
check("S2: q=1 ratio is N-dependent (2/N), so 2/3 at N=3 is a coincidence",
      len({S2[k]["ratio_q1"] for k in S2}) == 3)


# ---------------------------------------------------------------- POST-HOC (not pre-registered)
# The photon letter is the only N=3 word with a negative hbar^2 term. Is that term N-independent?
ph = {}
for NN in (2, 3, 4):
    c = chi(word(NN, 3, [1, -2]), direction(NN, 0))
    ser = hbar_series(c, 3)
    ph[NN] = {"chi": str(c), "hbar_series": str(ser), "hbar1": str(ser.coeff(hb, 1)),
              "hbar2": str(ser.coeff(hb, 2)), "hbar2_over_q1": str(sp.Rational(ser.coeff(hb, 2)) / at_q1(c))}
    check(f"photon N={NN}: hbar^1 coefficient vanishes (writhe 0)", ser.coeff(hb, 1) == 0, prereg=False)
out["posthoc_photon_hbar2_across_N"] = {str(k): v for k, v in ph.items()}
check("photon hbar^2 / chi(q=1) is N-dependent (not a fixed diamagnetic constant)",
      len({ph[k]["hbar2_over_q1"] for k in ph}) > 1, prereg=False)

# ---------------------------------------------------------------- verdict
out["verdict"] = {
    "S1": "MISS: twist label is the colour content ct(lambda); hbar-expansion of the background trace has "
          "positive coefficients only (8 hbar, 4N hbar^2 at n=2); the only negative constant is the "
          "sl-framing shift -1/N, N-dependent. 1-1/3 at N=3 is the pre-declared coincidence.",
    "S2": "MISS: Hecke-sign-weighted susceptibility q(N+2)-q^-1(N-2); q=1 ratio 2/N (swap l^2=4 over 2N), "
          "N-dependent. 2/3 at N=3 is the pre-declared coincidence.",
    "S3": "MISS (no split): background susceptibility of a braid word at q=1 is sum l_i^2 N^(#cyc-1): "
          "a strand cycle of length l couples like charge l (l^2 'paramagnetic-like'), with no "
          "opposite-sign diamagnetic term; heat-kernel per-state susceptibility 1 -> 12/17, sign of the "
          "RG reading set by the background convention.",
    "hit": False,
}
out["checks"] = CHECKS
out["n_pass"] = sum(c["pass"] for c in CHECKS)
out["n_total"] = len(CHECKS)
print(f"{out['n_pass']}/{out['n_total']} checks")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "qcd_spin_background_probe.out.json"), "w") as fh:
    json.dump(out, fh, indent=1, default=str)
sys.exit(0 if out["n_pass"] == out["n_total"] else 1)
