#!/usr/bin/env python3
"""qbeta_energy_map_probe — the ruled Q_β cell under the spectator-invariant (log) map.

Pre-registered in PREREGISTRATION.md (same directory) before this file was written.
Lean: QOU/QBeta/SpectatorEnergyMap.lean. Exact sympy for the identities, mpmath at 60 dps
for numbers, proton q₀ (Q_50_DIGIT_STR). No float64 in any computed value. CODATA is read only
in the last section, as a comparison, and nothing is selected by it.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402

mp.mp.dps = 60
FAILED: list = []
OUT: dict = {"preregistration": "PREREGISTRATION.md", "checks": [], "numbers": {}, "comparison": {}}


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    OUT["checks"].append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def s(x, n=14):
    return mp.nstr(x, n)


# ---------------------------------------------------------------- 1. exact identities (sympy)
print("1. Exact identities")
q, t, D, c, d, lam, x, y = sp.symbols("q t D c d lam x y", positive=True)
P = q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1
tau = -P / q**6                      # tr_{W_p}(V³) = tr_{W_n}(V³)  (trace_borromeanV3A/B)
qd2 = q + 1 / q
epsP = q * tau / qd2**3
epsN = tau / q / qd2**3
check("ratio eps_n/eps_p = q^-2", sp.simplify(epsN / epsP - q**-2) == 0, "every word with equal traces")
Phi = lambda u: c * sp.log(u) + d  # noqa: E731
check("log map is spectator invariant",
      sp.simplify(sp.expand_log(Phi(lam * x) - Phi(lam * y) - (Phi(x) - Phi(y)), force=True)) == 0,
      "Phi(lam x) - Phi(lam y) = Phi(x) - Phi(y)")
cell_generic = sp.expand_log(Phi(t / q / D) - Phi(q * t / D), force=True)
check("log cell = -2c log q", sp.simplify(cell_generic + 2 * c * sp.log(q)) == 0, "t, D drop out")
lin = lambda u: c * u  # noqa: E731
check("linear map fails S (lam=2, x=1, y=2)",
      sp.simplify(lin(2 * 1) - lin(2 * 2) - (lin(1) - lin(2))) != 0, "c*(-2) != c*(-1) for c != 0")
e0 = 1 / (q * (q - 1))
e0T = e0 / (1 - (1 - 1 / q) ** 2)
check("tower ratio = q^2/(2q-1)", sp.simplify(e0T / e0 - q**2 / (2 * q - 1)) == 0, "exact")

# ---------------------------------------------------------------- 2. numbers at the proton q0
print("2. Numbers at the proton q0 (model only)")
q0 = mp.mpf(C.Q_50_DIGIT_STR)
me = mp.mpf(C.M_E_MEV_STR)
f = sp.lambdify(q, [epsP, epsN, tau], "mpmath")
eP, eN, tau0 = f(q0)
E0 = me / (q0 * (q0 - 1))
hb = 1 - 1 / q0
E0T = E0 / (1 - hb**2)
L = mp.log(q0)
check("eps_p matches the coordinator's 0.408718179341", abs(eP - mp.mpf("0.408718179341")) < mp.mpf("1e-12"), s(eP))
check("eps_n matches 0.331737644740", abs(eN - mp.mpf("0.331737644740")) < mp.mpf("1e-12"), s(eN))
lo, hi = 2 / q0**2, 2 / q0
v = 2 * L / (q0 * (q0 - 1))
check("Lean bound 2/q^2 < 2 e0 log q < 2/q at q0", lo < v < hi, f"{s(lo,8)} < {s(v,10)} < {s(hi,8)}")

rows = {
    "linear_E0": E0 * abs(eN - eP),
    "linear_E0full": E0T * abs(eN - eP),
    "L0_log_E0": 2 * E0 * L,
    "LT_log_E0full": 2 * E0T * L,
    "S0_perstep_E0": 2 * E0,
    "ST_perstep_E0full": 2 * E0T,
    # Addendum 1, route D (dictionary beta = ln q): the cell is exactly 2 units; the unit is not
    # fixed by the dictionary. Diagnostics for the two energy units the corpus uses:
    "D_unit_me_cq2": 2 * me / (q0 - 1) ** 2,
    "D_unit_me": 2 * me,
}
OUT["numbers"] = {
    "q0": s(q0, 30), "m_e_MeV": s(me, 14), "eps_p": s(eP, 15), "eps_n": s(eN, 15),
    "eps_flavour": s(eN - eP, 15), "tau_V3": s(tau0, 15), "log_q0": s(L, 20),
    "E0_MeV": s(E0, 15), "E0full_MeV": s(E0T, 15), "tower_ratio": s(E0T / E0, 15),
    "rows_MeV": {k: s(val, 12) for k, val in rows.items()},
    "rows_over_me": {k: s(val / me, 12) for k, val in rows.items()},
}
for k, val in rows.items():
    print(f"  {k:22s} {s(val, 10)} MeV  = {s(val / me, 8)} m_e")

kT = me * (1 / (q0 - 1)) ** 2 * ((q0 - 1) / q0)
check("route T: m_e c_q^2 hbar_q = E0", abs(kT - E0) < mp.mpf("1e-50"), s(kT))
check("route D: -ln(eps_n)/ln q + ln(eps_p)/ln q = 2", abs((mp.log(eP) - mp.log(eN)) / L - 2) < mp.mpf("1e-50"), "exact 2")
check("two inverse temperatures differ: ln q < 1/hbar_q", L < 1 / hb, f"{s(L,8)} vs {s(1/hb,8)}")

unitD = (L / (1 / hb)) * me / (q0 - 1) ** 2  # addendum 2: dictionary unit in MeV
check("addendum 2: dictionary unit = E0 ln q", abs(unitD - E0 * L) < mp.mpf("1e-50"), s(unitD))
check("addendum 2: route D converted = route T", abs(2 * unitD - rows["L0_log_E0"]) < mp.mpf("1e-50"), s(2 * unitD))

# A common factor: linear cell rescales, log cell does not (S in numbers).
fL = mp.mpf(3) / 4  # an arbitrary common factor; the identity holds for every f > 0
lin_shared = E0T * abs(fL * eN - fL * eP)
log_shared = E0T * (mp.log(fL * eP) - mp.log(fL * eN))
check("shared factor: log cell unchanged", abs(log_shared - rows["LT_log_E0full"]) < mp.mpf("1e-50"), s(log_shared))
check("shared factor: linear cell scales by f", abs(lin_shared / rows["linear_E0full"] - fL) < mp.mpf("1e-50"), s(lin_shared))

# ---------------------------------------------------------------- 3. comparison (outside any proof)
print("3. Comparison with CODATA/AME (last; nothing selected)")
mn, mpp = mp.mpf(C.M_N_MEV_STR), mp.mpf(C.M_P_MEV_STR)
Qb, dnp = mn - mpp - me, mn - mpp
OUT["comparison"] = {"Q_beta_MeV": s(Qb, 12), "mn_minus_mp_MeV": s(dnp, 12), "rows": {}}
for k, val in rows.items():
    a, b = 100 * (val / Qb - 1), 100 * (val / dnp - 1)
    OUT["comparison"]["rows"][k] = {"vs_Q_beta_pct": s(a, 6), "vs_mn_minus_mp_pct": s(b, 6)}
    print(f"  {k:22s} vs Q_β {s(a, 5):>9s} %   vs m_n−m_p {s(b, 5):>9s} %")

OUT["ok"] = not FAILED
(_HERE / "qbeta-energy-map.witness.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False) + "\n")
print(f"{len(OUT['checks']) - len(FAILED)}/{len(OUT['checks'])} checks passed")
sys.exit(1 if FAILED else 0)
