"""Landauer tier-1 probe: crossing energy vs crossing information — is E per q-bit a substrate scale?

Audit-only probe (2026-07-04 audit
docs/audits/2026-07-04-zero-point-channel-energy-and-information.md sec 5 follow-up 1;
owner question "kinetic oscillation energy = amount of information in the channels?").

The corpus defines both sides independently:
  * crossing ENERGY (notation table 3): E_H = m_H * c_q^2, c_q^2 = 1/hbar_q^2;
  * crossing INFORMATION (fibre-channel-capacity / operational-entropy):
    a length-l braid carries at most l * eta_q q-bits, eta_q = (2q-1)/q^3.

The Landauer-type identification, if any, is E_H = kT_eff * (l * eta_q) for a substrate
temperature scale kT_eff. This probe computes the IMPLIED per-q-bit energy

    kT_eff(H) = E_H / (l * eta_q)

for the proton and neutron (Borromean B_3 word, l = 6 crossings) and compares it —
ratio only, tiered reporting, no fit — against the canonical candidate scales
{m_e c_q^2, m_mu, E_0, m_e/hbar_q, E_0 c_q^2}. A ratio within 5% of 1 is reported as a
near-match; anything else refutes the simple identification at tier 1 (scope-a).
Masses via the canonical facade (canonical_mass).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import time
from datetime import datetime, timezone

import mpmath as mp

from q_parameter import Q_MP as Q0  # noqa: E402
from canonical_mass import proton_mass_mev, neutron_mass_mev  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402

COMPUTE_DPS = 70
DPS = 50
BORROMEAN_CROSSINGS = 6  # standard 6-crossing B_3 diagram (sigma1 sigma2^-1)^3


def main() -> int:
    start = time.monotonic()
    mp.mp.dps = COMPUTE_DPS
    q0 = mp.mpf(str(Q0))
    hbar_q = 1 - 1 / q0
    cq2 = 1 / hbar_q**2
    eta_q = (2 * q0 - 1) / q0**3
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(m_e, q0)  # E_0 = m_e/(q0(q0-1)), the canonical binding scale

    info_qbits = BORROMEAN_CROSSINGS * eta_q
    scales = {
        "m_e_cq2": m_e * cq2,
        "m_mu_pred": m_e * mp.mpf(str(M_MU_OVER_M_E)),  # shared CODATA ratio (provenance-central)
        "E0": e0,
        "m_e_over_hbar_q": m_e / hbar_q,
        "E0_cq2": e0 * cq2,
    }

    rows = {}
    near = {}
    for name, m_h in (("proton", mp.mpf(str(proton_mass_mev()))),
                      ("neutron", mp.mpf(str(neutron_mass_mev())))):
        e_h = m_h * cq2
        kt_eff = e_h / info_qbits
        ratios_raw = {k: kt_eff / v for k, v in scales.items()}
        ratios = {k: mp.nstr(r, mp.mp.dps) for k, r in ratios_raw.items()}
        rows[name] = {
            "m_H_MeV": mp.nstr(m_h, DPS), "E_H_MeV": mp.nstr(e_h, DPS),
            "info_qbits": mp.nstr(info_qbits, DPS),
            "kT_eff_MeV_per_qbit": mp.nstr(kt_eff, DPS),
            "ratio_vs_scale": ratios,
        }
        print(f"  {name:8s}: E_H = {mp.nstr(e_h, 8)} MeV, info = {mp.nstr(info_qbits, 8)} "
              f"q-bits, kT_eff = {mp.nstr(kt_eff, 8)} MeV/q-bit")
        for k, r in ratios.items():
            print(f"      kT_eff / {k:16s} = {r}")
        near[name] = {k: ratios[k] for k, r in ratios_raw.items()
                      if abs(r - 1) < mp.mpf("0.05")}

    print(f"\n  near-matches (|ratio-1| < 5%): {near}")

    witness = {
        "description": ("Landauer tier-1 probe: implied per-q-bit energy "
                        "kT_eff = E_H/(l*eta_q) for p/n (Borromean, 6 crossings) vs "
                        "canonical substrate scales; tiered ratios, no fit."),
        "audit_only": True,
        "tier": "shape-probe (parameter-free; tiered ratio reporting)",
        "precision_dps": {"compute": COMPUTE_DPS, "serialized": DPS},
        "constants": {"q_0": mp.nstr(q0, 20), "eta_q": mp.nstr(eta_q, 20),
                      "hbar_q": mp.nstr(hbar_q, 20), "E0_MeV": mp.nstr(e0, 20),
                      "crossings": BORROMEAN_CROSSINGS},
        "scales_MeV": {k: mp.nstr(v, 20) for k, v in scales.items()},
        "hadrons": rows,
        "near_matches_5pct": {n: list(v.keys()) for n, v in near.items()},
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "landauer-crossing-energy-probe", witness,
        script_path=__file__, engine="mpmath", start_time=start,
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
