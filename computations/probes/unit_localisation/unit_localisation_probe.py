#!/usr/bin/env python3
"""Can one derived energy unit fix the n-p split and the deuteron at once?

Diagnostic only: no unit is adopted. Each candidate is a unit already on record
in the corpus. mpmath 50 dps; no float64. Measured values enter only in the
comparison block at the end.

Candidates (energy per dictionary unit, i.e. per unit of -ln trace):
  E0      = m_e/(q(q-1))                        (route T, order zero)
  E0_tw   = m_e q/((q-1)(2q-1))                 (tower form)
  E_osc   = m_e/(q-1)^2                         (K_A plaquette chart)
  E_mass  = m_e/hbar_q^2                        (mass-formula unit)
  E_log   = m_e/|ln tau_e|, tau_e = q^3 y3      (electron log weight, #9645 + 2026-11-27 audit)

Observables:
  flavour cell of m_n - m_p = U * 2 ln q        (exponent forced, NucleonSplitFullTower)
  deuteron B = U * (-ln r), r = gamma-gamma V(2)^3 trace ratio (gg-deuteron-bond witness)
"""
import json
import pathlib

import mpmath as mp

mp.mp.dps = 50
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

W = json.loads((ROOT / "computations/probes/gg_deuteron_bond/gg-deuteron-bond.witness.json").read_text())
q = mp.mpf(W["q0Value"])
r = mp.mpf(next(row["ratio"] for row in W["data"]["results"]["V^3"]["rows"] if row["bond"] == "V(2)^3"))
ME = mp.mpf("0.51099895069")  # CAL-1

hbar = 1 - 1 / q
y3 = (q**4 + 1) / (q**2 + 1) ** 2
tau_e = q**3 * y3
units = {
    "E0": ME / (q * (q - 1)),
    "E0_tw": ME * q / ((q - 1) * (2 * q - 1)),
    "E_osc": ME / (q - 1) ** 2,
    "E_mass": ME / hbar**2,
    "E_log": ME / abs(mp.log(tau_e)),
}

# Model EM piece of m_n - m_p (Form-B alpha x V^3 all-pairs trace), from
# docs/audits/2026-11-24-np-splitting-qbeta-legendre-coulomb-cds1-15sj-37y0.md (E07).
# Conditional on the Form-B premise classes. Used as a model term, not data.
EM = mp.mpf("-0.7571250743")

# ---- comparison boundary: data enter only below ----
DNP = mp.mpf("1.29333251")
B2H = mp.mpf("2.224566")

rows = []
for name, U in units.items():
    flav = U * 2 * mp.log(q)
    deut = U * (-mp.log(r))
    rows.append({
        "unit": name,
        "U_MeV": mp.nstr(U, 12),
        "np_flavour_MeV": mp.nstr(flav, 10),
        "np_total_with_EM_MeV": mp.nstr(flav + EM, 10),
        "deuteron_MeV": mp.nstr(deut, 10),
        "factor_needed_np_total": mp.nstr((DNP - EM) / flav, 8),
        "factor_needed_deuteron": mp.nstr(B2H / deut, 8),
    })
for x in rows:
    print(json.dumps(x))
# The ratio of required factors does not depend on the unit: U cancels.
ratio = (B2H / (-mp.log(r))) / ((DNP - EM) / (2 * mp.log(q)))
for U in units.values():
    assert abs((B2H / (U * -mp.log(r))) / ((DNP - EM) / (U * 2 * mp.log(q))) - ratio) < mp.mpf("1e-40")
print("deuteron/np required-factor ratio (unit-independent):", mp.nstr(ratio, 10))
(HERE / "result.json").write_text(json.dumps({"q0": mp.nstr(q, 30), "rows": rows,
    "unit_independent_ratio": mp.nstr(ratio, 12)}, indent=1))
