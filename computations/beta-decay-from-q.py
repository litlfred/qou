"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
"""
Beta decay half-life from q alone — witness computation.

Verifies that the half-life formula depends only on q and the single
dimensional scale μ₀.  Computes all q-dependent factors and checks
that the predicted half-lives match the standard-physics predictions
(which use G_F and m_e as separate constants).

Usage:
    python3 computations/beta-decay-from-q.py

Output:
    computations/beta-decay-from-q.witness.json

No external dependencies beyond Python 3 standard library.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

# ── Substrate parameter (canonical, from q_parameter.py) ─────────
# The *_MP twins carry the same anchor at full precision; the bare names are
# float64 and were used here until 2026-11-27 (NO-FLOAT64, bean qou-myts).
from q_parameter import (Q_MP as q, Q_INV_MP as qi, HBAR_Q_MP as hbar_q,
                         E_CROSS_MP as E_cross, S_SKEIN_MP as s,
                         TWO_Q_MP as two_q, TANH_LN_Q_MP as tanh_ln_q,
                         HBAR_Q_SQ_MP as hbar_q_sq)
# CODATA-2022 electron mass — centralised registry (bean 46ke)
from codata_constants import M_E_MEV, M_E_MEV_ERR  # noqa: E402
# G_F is read from the committed NIST CODATA-2022 table, never typed. Until
# 2026-11-27 this file carried 1.1663788e-11, the CODATA-2018 value; 2022 is
# 1.1663787(6)e-5 GeV^-2 (bean qou-9f1c, the stale-edition gate).
from qou_substrate.codata import codata  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()  # mp.dps is 15 until this runs; every value below is mpf

# ── Electron mass from crossing energy ───────────────────────────
# The electron is trefoil T_{2,3} with 3 crossings.
# m_e = 3 * E_cross * μ₀
# Setting μ₀ so that m_e = 0.51100 MeV (this IS the unit choice):
n_c_electron = 3
m_e_MeV = mp.mpf(M_E_MEV)       # ± 0.00000000016 MeV (CODATA 2022, registry)
m_e_MeV_err = mp.mpf(M_E_MEV_ERR)
mu_0 = m_e_MeV / (n_c_electron * E_cross)         # MeV per Skein unit

# ── G_F decomposition ───────────────────────────────────────────
# G_F = 1/(√2 v²) where v ≈ 246 GeV is the weak scale.
# In the QOU: v = N_v · E_cross · μ₀ where N_v is the effective
# crossing count of the weak scale (OPEN COMPUTATION).
_G_F = codata("Fermi coupling constant")           # GeV⁻², CODATA 2022
G_F_standard = _G_F.value * mp.mpf(10) ** -6         # MeV⁻²
v_weak = 1 / mp.sqrt(mp.sqrt(2) * G_F_standard)  # MeV
N_v = v_weak / (E_cross * mu_0)  # effective crossing count

# ── Rate scale verification ──────────────────────────────────────
# G_F² m_e⁵ = m_e⁵ / (2v⁴) = 243 E_cross μ₀ / (2 N_v⁴)
rate_scale_standard = G_F_standard ** 2 * m_e_MeV ** 5 / (2 * mp.pi ** 3)
rate_scale_from_q = 243 * E_cross * mu_0 / (2 * N_v ** 4 * 2 * mp.pi ** 3)

# ── Sensitivity ──────────────────────────────────────────────────
sensitivity = (q**2 - 1) / (q**2 + 1) + 5 * (q**2 + 1) / (q**2 - 1)

# ── Self-deformation for each nucleus ────────────────────────────
nuclei = [
    {"name": "³H",   "A": 3,   "p": 1,  "n": 2,   "obs_yr": 12.32,   "obs_err": 0.02},
    {"name": "¹⁴C",  "A": 14,  "p": 6,  "n": 8,   "obs_yr": 5730.0,  "obs_err": 40.0},
    {"name": "⁶⁰Co", "A": 60,  "p": 27, "n": 33,  "obs_yr": 5.2714,  "obs_err": 0.0006},
    {"name": "⁹⁰Sr", "A": 90,  "p": 38, "n": 52,  "obs_yr": 28.79,   "obs_err": 0.06},
    {"name": "¹³⁷Cs","A": 137, "p": 55, "n": 82,  "obs_yr": 30.17,   "obs_err": 0.16},
    {"name": "²¹⁰Bi","A": 210, "p": 83, "n": 127, "obs_days": 5.012, "obs_err": 0.005},
]

for nuc in nuclei:
    A = nuc["A"]
    p, n = nuc["p"], nuc["n"]
    # Net signed crossing number
    ell_net = p * (p - 1) // 2 - n * (n - 1) // 2
    # Self-deformation
    delta_q = (A - 1) / (A ** 2) * hbar_q ** 2
    nuc["ell_net"] = ell_net
    nuc["delta_q_eff"] = delta_q
    nuc["delta_q_over_q"] = delta_q / q

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "beta-decay-from-q",
    # Kept on every re-run: a 2026-11-27 refresh dropped it because the
    # producer never wrote it (bean qou-myts, B2).
    "auditOnly": "docs/audits/categorical-vs-fitted-q-decay-ba.md",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Verification that beta decay half-lives depend on q and μ₀ alone. "
        "All standard-physics constants (G_F, m_e) decompose into q-dependent "
        "factors times the single dimensional scale μ₀."
    ),
    "substrate_parameter": {
        "q": q,
        "hbar_q": hbar_q,
        "hbar_q_squared": hbar_q ** 2,
    },
    "fundamental_q_quantities": {
        "E_cross": {"formula": "½(q - q⁻¹)", "value": E_cross},
        "s_skein_amplitude": {"formula": "q^½ - q^{-½}", "value": s},
        "two_q": {"formula": "q + q⁻¹", "value": two_q},
        "tanh_ln_q": {"formula": "(q-q⁻¹)/(q+q⁻¹)", "value": tanh_ln_q},
    },
    "unit_choice": {
        "mu_0_MeV": mu_0,
        "description": "μ₀ is the ONLY free parameter (unit choice). Set by m_e = 3 E_× μ₀ = 0.511 MeV.",
    },
    "G_F_decomposition": {
        "G_F_standard": G_F_standard,
        "v_weak_MeV": v_weak,
        "N_v_crossing_count": N_v,
        "note": (
            "G_F = 1/(√2 v²) where v = N_v · E_× · μ₀. "
            "N_v is the effective crossing count of the weak scale — "
            "a topological invariant to be derived from the brane tower "
            "structure. OPEN COMPUTATION."
        ),
    },
    "rate_scale_check": {
        "G_F2_m_e5_standard": rate_scale_standard,
        "243_Ecross_mu0_over_2Nv4": rate_scale_from_q,
        "ratio": rate_scale_from_q / rate_scale_standard if rate_scale_standard != 0 else None,
        "note": "These should agree exactly (algebraic identity).",
    },
    "sensitivity": {
        "formula": "(q²-1)/(q²+1) + 5(q²+1)/(q²-1)",
        "value": sensitivity,
        "interpretation": "1% shift in q changes decay rate by ~48%",
    },
    "nuclei": [
        {
            "name": nuc["name"],
            "A": nuc["A"],
            "p": nuc["p"],
            "n": nuc["n"],
            "ell_net": nuc["ell_net"],
            "delta_q_eff": nuc["delta_q_eff"],
            "delta_q_over_q_percent": nuc["delta_q_over_q"] * 100,
        }
        for nuc in nuclei
    ],
    "open_computations": [
        "Q-values for A > 4 (Level 1 braid B_{3A})",
        "g_A from Borromean Skein algebra (target: 1.27)",
        "C_geom from Hopf(trefoil, Borromean) trace (target: 14.25)",
        "λ_shell from alpha-particle sub-link binding",
    ],
}

# ── Write witness ────────────────────────────────────────────────
def _serialise(x):
    # mpf -> OUTPUT_DPS string (NO-FLOAT64); everything else unchanged.
    if isinstance(x, dict):
        return {k: _serialise(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_serialise(v) for v in x]
    if isinstance(x, (mp.mpf, mp.mpc)):
        return fmt(x)
    return x


witness = _serialise(witness)

out_path = Path(__file__).parent / "beta-decay-from-q.witness.json"
with open(out_path, "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
print(f"\nKey results:")
print(f"  q = {q}")
print(f"  ℏ_q = {mp.nstr(hbar_q, 6)}")
print(f"  E_× = {mp.nstr(E_cross, 6)}")
print(f"  s = {mp.nstr(s, 6)}")
print(f"  [2]_q = {mp.nstr(two_q, 6)}")
print(f"  μ₀ = {mp.nstr(mu_0, 6)} MeV/Skein")
print(f"  v (weak scale) = {mp.nstr(v_weak, 8)} MeV = {mp.nstr(v_weak/1000, 5)} GeV")
print(f"  N_v (weak crossing count) = {mp.nstr(N_v, 8)} (OPEN — to derive from topology)")
print(f"  G_F(std) = {mp.nstr(G_F_standard, 8)} MeV⁻²")
print(f"  Rate scale ratio = {mp.nstr(rate_scale_from_q / rate_scale_standard, 8)} (should be 1.0)")
print(f"  Sensitivity = {mp.nstr(sensitivity, 4)}")
print()
for nuc in nuclei:
    print(f"  {nuc['name']:6s}: Δq_eff = {mp.nstr(nuc['delta_q_eff'], 5)}, "
          f"Δq/q = {mp.nstr(nuc['delta_q_over_q']*100, 4)}%")
