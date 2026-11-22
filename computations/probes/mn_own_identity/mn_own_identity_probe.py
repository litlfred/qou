#!/usr/bin/env python3
"""m_n by its own identity: the neutron analogue of the convention-D proton identity.

Pre-registration (committed first): PREREGISTRATION.md in this directory.
Lean: folio/quantum-observable-universe/lean/QOU/MassTheory/NeutronOwnIdentity.lean.

Proton identity (production, convention D):
    m_p/m_e = 2 (Vol(4_1)/hbar_q^2) F_Bor(q) - 12,  F_Bor = |tr_M(V^3)| [3]_q! / q^3.

Checks (exact, sympy over Q(q)):
  S1  tr_M(V^3) = (q^3 + q tr_Wp + q^-1 tr_Wn + q^-3)/[2]^3   (whole-space, four T3 sectors)
  S2  invariant under K -> K^-1 (u <-> d)
  S3  N0 neutron F equals F_Bor (so m_n = m_p)
  S4  N1 sector ratio eps_n/eps_p = q^-2
  S5  N2 bar mirror ratios F_Bor(1/q)/F_Bor(q) = q^6 and with hbar_q: q^4
Values (mpmath, 60 dps) at the muon pin (CAL-2: m_mu/m_e = Vol/hbar^2, CODATA 2022 ratio) and
the proton pin (production q0, solved from m_p: a round trip). CODATA m_p, m_n enter
comparison rows only. Nothing is fitted.
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
checks: list[tuple[str, bool]] = []

# ---------- exact part ----------
q = sp.symbols("q", positive=True)
h = q - 1 / q
d2 = q + 1 / q
qf3 = (q + 1 / q) * (q**2 + 1 + q**-2)
P = q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1


def rho(word_mats):
    out = sp.eye(3)
    for m in word_mats:
        out = out * m
    return out


# weight-space matrices exactly as in NucleonWeightSpaceTraces.lean (Jimbo R)
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, q - 1 / q]])
A2 = sp.Matrix([[0, 1, 0], [1, q - 1 / q, 0], [0, 0, q]])
B1 = sp.Matrix([[0, 1, 0], [1, q - 1 / q, 0], [0, 0, q]])
B2 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, q - 1 / q]])
VA = A1 * A2.inv()
VB = B1 * B2.inv()
trWp = sp.simplify((VA**3).trace())
trWn = sp.simplify((VB**3).trace())
checks.append(("tr_Wp(V3) = -P/q^6", sp.simplify(trWp + P / q**6) == 0))
checks.append(("tr_Wn(V3) = tr_Wp(V3)", sp.simplify(trWn - trWp) == 0))

trM_closed = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
whole = (q**3 * 1 + q * trWp + q**-1 * trWn + q**-3 * 1) / d2**3
checks.append(("S1 whole-space sector sum = tr_M closed form", sp.simplify(whole - trM_closed) == 0))
reflected = (q**-3 * 1 + q**-1 * trWp + q * trWn + q**3 * 1) / d2**3
checks.append(("S2 K -> K^-1 invariance", sp.simplify(reflected - whole) == 0))
F = trM_closed * qf3 / q**3
F_n0 = reflected * qf3 / q**3
checks.append(("S3 F^(n)_N0 = F_Bor", sp.simplify(F_n0 - F) == 0))
eps_p = q * trWp / d2**3
eps_n = q**-1 * trWn / d2**3
checks.append(("S4 eps_n/eps_p = q^-2", sp.simplify(eps_n / eps_p - q**-2) == 0))
F_bar = F.subs(q, 1 / q)
checks.append(("S5a F_Bor(1/q)/F_Bor(q) = q^6", sp.simplify(F_bar / F - q**6) == 0))
hb = 1 - 1 / q
checks.append(("S5b [F/hbar^2](1/q) / [F/hbar^2](q) = q^4",
               sp.simplify((F_bar / hb.subs(q, 1 / q) ** 2) / (F / hb**2) - q**4) == 0))
checks.append(("F_Bor(1) = 6", sp.simplify(F.subs(q, 1) - 6) == 0))

# sector shares of tr_M at q (exact functions, evaluated below)
share_expr = {
    "uuu": q**3 / d2**3,
    "uud (proton)": q * trWp / d2**3,
    "udd (neutron)": q**-1 * trWn / d2**3,
    "ddd": q**-3 / d2**3,
}

# ---------- values ----------
vol = 2 * clsin(2, pi / 3)
me = mpf(M_E_MEV)
mp_cod = mpf(M_P_MEV_VALIDATION)
mn_cod = mpf(M_N_MEV_VALIDATION)
ratio_mu = mpf(MASS_RATIO_MU_E_STR)

hbar_mu = sqrt(vol / ratio_mu)
q_mu = 1 / (1 - hbar_mu)
q_p = mpf(Q_50_DIGIT_STR)

Ff = sp.lambdify(q, F, "mpmath")
eps_pf = sp.lambdify(q, eps_p, "mpmath")
eps_nf = sp.lambdify(q, eps_n, "mpmath")


def ppm(x, ref):
    return (x - ref) / ref * mpf(10) ** 6


rows = {}
for pin, qq in (("muon", q_mu), ("proton", q_p)):
    hb2 = (1 - 1 / qq) ** 2
    S = 2 * vol / hb2  # 2 Vol / hbar^2
    Fv = Ff(qq)
    m_p_pred = me * (S * Fv - 12)
    m_n_N0 = me * (S * Fv - 12)
    m_n_N1 = me * (S * Fv * qq**-2 - 12)
    m_n_N2a = me * (S * Fv * qq**6 - 12)
    m_n_N2b = me * (S * Fv * qq**4 - 12)
    shares = {k: nstr(sp.lambdify(q, v, "mpmath")(qq) / (sp.lambdify(q, trM_closed, "mpmath")(qq)), 12)
              for k, v in share_expr.items()}
    rows[pin] = {
        "q0": nstr(qq, 30),
        "F_Bor": nstr(Fv, 25),
        "m_p_pred_MeV": nstr(m_p_pred, 15),
        "m_p_ppm_vs_CODATA": nstr(ppm(m_p_pred, mp_cod), 8),
        "N0_m_n_MeV": nstr(m_n_N0, 15),
        "N0_m_n_ppm_vs_CODATA": nstr(ppm(m_n_N0, mn_cod), 8),
        "N0_m_n_minus_CODATA_MeV": nstr(m_n_N0 - mn_cod, 10),
        "N1_m_n_MeV": nstr(m_n_N1, 12),
        "N1_m_n_pct_vs_CODATA": nstr(ppm(m_n_N1, mn_cod) / 10**4, 6),
        "N2a_m_n_MeV": nstr(m_n_N2a, 12),
        "N2a_pct": nstr(ppm(m_n_N2a, mn_cod) / 10**4, 6),
        "N2b_m_n_MeV": nstr(m_n_N2b, 12),
        "N2b_pct": nstr(ppm(m_n_N2b, mn_cod) / 10**4, 6),
        "sector_shares_of_trM": shares,
        "eps_n_over_eps_p": nstr(eps_nf(qq) / eps_pf(qq), 15),
    }

ok = all(c for _, c in checks)
for name, c in checks:
    print(("PASS " if c else "FAIL ") + name)
print(json.dumps(rows, indent=1, ensure_ascii=False))
out = {
    "probe": "mn_own_identity_probe",
    "preregistration": "PREREGISTRATION.md",
    "checks": {n: c for n, c in checks},
    "all_pass": ok,
    "values": rows,
    "note": "CODATA m_p, m_n in comparison rows only; m_mu/m_e (CAL-2) fixes the muon pin.",
}
(HERE / "mn_own_identity_probe.out.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
sys.exit(0 if ok else 1)
