#!/usr/bin/env python3
"""m_n by its own identity, four-strand lepton test.

Pre-registration (committed first): PREREGISTRATION-four-strand.md (commit ab73baa376a).
Exact sympy over Q(q) on V^{(x)4} (and V^{(x)3} for the electron word); mpmath 60 dps for values.
Jimbo R as in NucleonWeightSpaceTraces.lean: R(uu)=q uu, R(dd)=q dd, R(ud)=du, R(du)=ud+h du.
Arms: L-A spectator lepton strand (V^3 (x) 1), L-B selected four-strand word (#8636),
L-C electron word sigma0 sigma1 sigma0 split-unioned with the nucleon braid.
CODATA m_p, m_n in comparison rows only. Nothing fitted.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, clsin, pi, sqrt, nstr

HERE = Path(__file__).resolve().parent
COMP = HERE.parent.parent
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: E402,F401
from q_parameter import Q_50_DIGIT_STR, MASS_RATIO_MU_E_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

mp.dps = 60
q = sp.symbols("q", positive=True)
h = q - 1 / q
d2 = q + 1 / q
checks: list[tuple[str, bool]] = []


def basis(n):
    return ["".join(t) for t in itertools.product("ud", repeat=n)]


def sigma(n, i, inv=False):
    """Jimbo R on strands i, i+1 (1-indexed) of V^{(x)n}; columns = images of basis states."""
    B = basis(n)
    idx = {s: k for k, s in enumerate(B)}
    M = sp.zeros(len(B))
    for s in B:
        a, b = s[i - 1], s[i]
        pre, post = s[: i - 1], s[i + 1:]
        if a == b:
            M[idx[s], idx[s]] = q
        elif a + b == "ud":
            M[idx[pre + "du" + post], idx[s]] = 1
        else:  # du -> ud + h du
            M[idx[pre + "ud" + post], idx[s]] = 1
            M[idx[s], idx[s]] = h
    return M.inv() if inv else M


def Kfull(n):
    return sp.diag(*[q ** (s.count("u") - s.count("d")) for s in basis(n)])


def restrict(M, n, states):
    B = basis(n)
    ix = [B.index(s) for s in states]
    return M.extract(ix, ix)


# --- convention checks against the three-strand probe ---
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
Wp = ["uud", "udu", "duu"]
Wn = ["udd", "dud", "ddu"]
s1_3, s2_3 = sigma(3, 1), sigma(3, 2)
checks.append(("R reproduces A1 on W_p", sp.simplify(restrict(s1_3, 3, Wp) - A1) == sp.zeros(3)))
checks.append(("R reproduces A2 on W_p", sp.simplify(restrict(s2_3, 3, Wp) - A2) == sp.zeros(3)))
checks.append(("Hecke relation", sp.simplify(s1_3 * s1_3 - h * s1_3 - sp.eye(8)) == sp.zeros(8)))
checks.append(("braid relation", sp.simplify(s1_3 * s2_3 * s1_3 - s2_3 * s1_3 * s2_3) == sp.zeros(8)))
V3_3 = (s1_3 * s2_3.inv()) ** 3
trM_closed = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
trM_quantum = (Kfull(3) * V3_3).trace() / d2**3
checks.append(("tr_M(V^3) = Tr(K^3 V^3)/[2]^3", sp.simplify(trM_quantum - trM_closed) == 0))

# --- four strands ---
n4 = 4
s1, s2, s3 = sigma(4, 1), sigma(4, 2), sigma(4, 3)
N = ["uddu", "dudu", "dduu"]
P = ["duud", "udud", "uudd"]
K4 = Kfull(4)
checks.append(("K^{(x)4} = 1 on N and P",
               all(K4[basis(4).index(s), basis(4).index(s)] == 1 for s in N + P)))
V3_4 = (s1 * s2.inv()) ** 3

# L-A: spectator lepton strand
trN_A = sp.simplify(restrict(V3_4, 4, N).trace())
trP_A = sp.simplify(restrict(V3_4, 4, P).trace())
checks.append(("L-A tr_N(V3 x 1) = tr_P(V3 x 1)", sp.simplify(trN_A - trP_A) == 0))
# two-term connected part, SM charges, covariant all-pairs on each sector
CHG = {"u": sp.Rational(2, 3), "d": sp.Rational(-1, 3)}
LEP = {"u": sp.Integer(0), "d": sp.Integer(-1)}  # nu = u, e = d (C-lep)


def pair_op(states):
    vals = []
    for s in states:
        c = [CHG[s[0]], CHG[s[1]], CHG[s[2]], LEP[s[3]]]
        vals.append(sum(c[i] * c[j] for i in range(4) for j in range(i + 1, 4)))
    return sp.diag(*vals)


conn = {}
for name, S in (("N", N), ("P", P)):
    X = pair_op(S)
    W = restrict(V3_4, 4, S)
    raw = sp.simplify((X * W).trace())
    connected = sp.simplify(raw - X.trace() / 3 * W.trace())
    conn[name] = (raw, connected)
checks.append(("L-A two-term connected = 0 on N", conn["N"][1] == 0))
checks.append(("L-A two-term connected = 0 on P", conn["P"][1] == 0))

# L-B: selected four-strand words (#8636): sigma1 sigma3^{-1} and sigma3^{-1} sigma1
words = {"s1*s3inv": s1 * s3.inv(), "s3inv*s1": s3.inv() * s1}
LB = {}
for wn, w in words.items():
    tN = sp.factor(sp.simplify(restrict(w, 4, N).trace()))
    tP = sp.factor(sp.simplify(restrict(w, 4, P).trace()))
    LB[wn] = (tN, tP, sp.factor(sp.simplify(tN / tP)))
# #8636 amplitude <P|s1 s3^{-1}|N>
B4 = basis(4)
amp = sp.simplify(words["s1*s3inv"].extract([B4.index(s) for s in P], [B4.index(s) for s in N]))
amp_ref = sp.Matrix([[1, (q**2 - 1) / q, 0], [0, 1, 0], [0, 0, 0]])
amp_norm = sp.simplify(sum(x**2 for x in amp))
checks.append(("#8636 |<P|s1 s3^-1|N>|^2 = (q^4+1)/q^2", sp.simplify(amp_norm - (q**4 + 1) / q**2) == 0))

# L-C: electron word sigma0 sigma1 sigma0 on its own three strands
E = s1_3 * s2_3 * s1_3
trD_e = sp.factor(sp.simplify((Kfull(3) * E).trace() / d2**3))
checks.append(("tr_D(s0 s1 s0) = q^3(q^4+1)/(q^2+1)^2",
               sp.simplify(trD_e - q**3 * (q**4 + 1) / (q**2 + 1) ** 2) == 0))
# split-union factorisation on 6 strands: Tr(K^6 (V3 (x) E)) / [2]^6 = tr_M(V3) tr_D(E)
split = sp.simplify((sp.kronecker_product(Kfull(3) * V3_3, Kfull(3) * E)).trace() / d2**6)
checks.append(("split union factorises", sp.simplify(split - trM_closed * trD_e) == 0))

# --- values ---
qf3 = (q + 1 / q) * (q**2 + 1 + q**-2)
F = trM_closed * qf3 / q**3
vol = 2 * clsin(2, pi / 3)
me = mpf(M_E_MEV)
mp_cod, mn_cod = mpf(M_P_MEV_VALIDATION), mpf(M_N_MEV_VALIDATION)
q_mu = 1 / (1 - sqrt(vol / mpf(MASS_RATIO_MU_E_STR)))
q_p = mpf(Q_50_DIGIT_STR)


def ev(expr, qq):
    return sp.lambdify(q, expr, "mpmath")(qq)


def rel(x, ref):
    return (x - ref) / ref


rows = {}
for pin, qq in (("muon", q_mu), ("proton", q_p)):
    S = 2 * vol / (1 - 1 / qq) ** 2
    Fv = ev(F, qq)
    m_p_pred = me * (S * Fv - 12)
    r = {"q0": nstr(qq, 25), "m_p_pred_MeV": nstr(m_p_pred, 15),
         "LA_m_n_MeV": nstr(m_p_pred, 15),
         "LA_m_n_ppm": nstr(rel(m_p_pred, mn_cod) * 10**6, 8)}
    for wn, (tN, tP, ratio) in LB.items():
        rv = ev(ratio, qq)
        mn = me * (S * Fv * rv - 12)
        r[f"LB_{wn}"] = {"trN": str(tN), "trP": str(tP), "ratio": nstr(rv, 20),
                         "m_n_MeV": nstr(mn, 15), "pct_vs_CODATA_mn": nstr(rel(mn, mn_cod) * 100, 8)}
    te = ev(trD_e, qq)
    m_pe = me * ((S * Fv) * te - 12)
    r["LC_trD_e"] = nstr(te, 20)
    r["LC_m(n x nu)_MeV"] = nstr(m_p_pred, 15)
    r["LC_m(p x e)_MeV"] = nstr(m_pe, 15)
    r["LC_vs_mp_plus_me_pct"] = nstr(rel(m_pe, mp_cod + me) * 100, 8)
    rows[pin] = r

ok = all(c for _, c in checks)
for nm, c in checks:
    print(("PASS " if c else "FAIL ") + nm)
print("amp <P|s1 s3^-1|N> =", amp.tolist())
print("L-A raw two-term:", {k: str(v[0]) for k, v in conn.items()})
print(json.dumps(rows, indent=1, ensure_ascii=False))
out = {"probe": "mn_four_strand_probe", "preregistration": "PREREGISTRATION-four-strand.md",
       "checks": {n: c for n, c in checks}, "all_pass": ok,
       "LA_two_term_raw": {k: str(v[0]) for k, v in conn.items()},
       "amp_P_s1s3inv_N": [[str(x) for x in row] for row in amp.tolist()],
       "values": rows,
       "note": "CODATA m_p, m_n in comparison rows only; m_mu/m_e (CAL-2) fixes the muon pin."}
(HERE / "mn_four_strand_probe.out.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
sys.exit(0 if ok else 1)
