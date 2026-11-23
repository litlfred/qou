#!/usr/bin/env python3
"""Which term of the categorical mass formula can carry the n-p split.

Pre-registration: PREREGISTRATION-cartan-constant.md (committed before this ran).

Assembly m_N = sum_k c_k omega_k(N) t_k, each term bare (omega = 1) or
Cartan-weighted (omega(p) = s q, omega(n) = s/q). Exact sympy checks, then mpmath
values (60 dps) at the muon pin (E1 comparison, proton vs muon pin) and the proton pin (round trip).
CODATA and literature values appear in comparison fields only.
"""
from __future__ import annotations

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
q, s, A, a, c = sp.symbols("q s A a c", positive=True)
h = q - 1 / q
checks: list[tuple[str, bool]] = []

# --- exact: K^{(x)3} eigenvalue on the nucleon weight spaces ---------------------
K = sp.diag(q, 1 / q)  # u, d
def k3(word):  # word in {'u','d'}^3
    v = sp.Integer(1)
    for f in word:
        v *= K[0, 0] if f == "u" else K[1, 1]
    return v
checks.append(("K^3 = q on uud, udu, duu", all(sp.simplify(k3(w) - q) == 0 for w in ("uud", "udu", "duu"))))
checks.append(("K^3 = 1/q on udd, dud, ddu", all(sp.simplify(k3(w) - 1 / q) == 0 for w in ("udd", "dud", "ddu"))))

# --- exact: assembly split law ---------------------------------------------------
# weighted volume term a (coefficient of the positive term), weighted constant c
def m(N, wvol, wconst):
    om = s * q if N == "p" else s / q
    vol = A * (om if wvol else 1)
    const = -c * (om if wconst else 1)
    return vol + const
for wv, wc in ((False, False), (True, False), (False, True), (True, True)):
    diff = sp.simplify(m("n", wv, wc) - m("p", wv, wc))
    weighted = (A if wv else 0) + (-c if wc else 0)
    law = sp.simplify(diff - (-s * h * weighted))
    checks.append((f"split law, vol weighted={wv}, const weighted={wc}", law == 0))

K1 = sp.simplify(12 * (1 - q**-2))  # s = 1/q, proton normalised
K2 = sp.simplify(12 * h)             # s = 1, plain K^{(x)3}
checks.append(("K1 = 12(1 - q^-2) = (12/q) h", sp.simplify(K1 - 12 * h / q) == 0))

# --- values ------------------------------------------------------------------------
trM = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
qf3 = (q + 1 / q) * (q**2 + 1 + q**-2)
F = trM * qf3 / q**3
checks.append(("F_Bor(1) = 6", sp.simplify(F.subs(q, 1) - 6) == 0))
vol = 2 * clsin(2, pi / 3)
me = mpf(M_E_MEV)
mp_cod, mn_cod = mpf(M_P_MEV_VALIDATION), mpf(M_N_MEV_VALIDATION)
dnp_cod = mn_cod - mp_cod
q_mu = 1 / (1 - sqrt(vol / mpf(MASS_RATIO_MU_E_STR)))
q_p = mpf(Q_50_DIGIT_STR)
ev = lambda e, qq: sp.lambdify(q, e, "mpmath")(qq)
ppm = lambda x, r: nstr((x - r) / r * 10**6, 8)
pct = lambda x, r: nstr((x - r) / r * 100, 8)

LIT = {  # n - p totals (MeV), comparison only
    "experiment (CODATA)": nstr(dnp_cod, 10),
    "BMW 2015 lattice QCD+QED": "1.51(16)(23)",
    "QCDSF-UKQCD 2015 (Horsley et al.)": "1.35(18)(8)",
}

rows = {}
for pin, qq in (("muon", q_mu), ("proton", q_p)):
    big = me * 2 * vol / (1 - 1 / qq) ** 2 * ev(F, qq)  # 2 m_mu F_Bor
    hv = qq - 1 / qq
    r = {"q0": nstr(qq, 25), "h": nstr(hv, 20)}
    base_p = big - 12 * me
    r["N0_isospin_limit"] = {"m_p": nstr(base_p, 15), "m_p_ppm": ppm(base_p, mp_cod),
                             "m_n": nstr(base_p, 15), "n_minus_p": "0"}
    # K0 control: volume term weighted (s = 1/q so proton unchanged), constant bare
    mn0 = big / qq**2 - 12 * me
    r["K0_volume_weighted"] = {"m_p": nstr(base_p, 15), "m_n": nstr(mn0, 15),
                               "n_minus_p": nstr(mn0 - base_p, 12)}
    # K1: constant weighted, s = 1/q
    mn1 = big - 12 * me / qq**2
    r["K1_const_weighted_proton_normalised"] = {
        "m_p": nstr(base_p, 15), "m_p_ppm": ppm(base_p, mp_cod),
        "m_n": nstr(mn1, 15), "m_n_ppm": ppm(mn1, mn_cod),
        "n_minus_p": nstr(mn1 - base_p, 12), "n_minus_p_pct_vs_CODATA": pct(mn1 - base_p, dnp_cod)}
    # K2: constant weighted, s = 1
    mp2, mn2 = big - 12 * me * qq, big - 12 * me / qq
    r["K2_const_weighted_symmetric"] = {
        "m_p": nstr(mp2, 15), "m_p_ppm": ppm(mp2, mp_cod),
        "m_n": nstr(mn2, 15), "m_n_ppm": ppm(mn2, mn_cod),
        "n_minus_p": nstr(mn2 - mp2, 12), "n_minus_p_pct_vs_CODATA": pct(mn2 - mp2, dnp_cod),
        "average": nstr((mp2 + mn2) / 2, 15),
        "average_ppm_vs_CODATA_average": ppm((mp2 + mn2) / 2, (mp_cod + mn_cod) / 2)}
    r["K1_over_K2"] = nstr(1 / qq, 15)
    rows[pin] = r

ok = all(cc for _, cc in checks)
for nm, cc in checks:
    print(("PASS " if cc else "FAIL ") + nm)
print(json.dumps(rows, indent=1, ensure_ascii=False))
out = {"probe": "mn_cartan_constant_probe", "preregistration": "PREREGISTRATION-cartan-constant.md",
       "checks": {n: cc for n, cc in checks}, "all_pass": ok,
       "split_law": "m_n - m_p = -s (q - 1/q) * (sum of Cartan-weighted coefficients)",
       "K1_exact": str(K1), "K2_exact": str(K2),
       "values": rows, "literature_n_minus_p_MeV": LIT,
       "note": "CODATA and literature in comparison fields only; m_mu/m_e (CAL-2) fixes the muon pin."}
(HERE / "mn_cartan_constant_probe.out.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
sys.exit(0 if ok else 1)
