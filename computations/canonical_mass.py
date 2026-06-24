#!/usr/bin/env python3
"""Canonical nucleon / atom mass — the SINGLE entry point (facade).

Owner ruling 2026-06-24: there is ONE correct absolute nucleon mass, the
**muon-anchored Hecke energy** (the production substrate-identity):

    m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e) = 2·(m_μ·F_Bor − 6·m_e)
    m_μ   = m_e · Vol(4₁) / ℏ_q²                      (muon = figure-8 knot 4₁)
    F_Bor = |tr_M(β_Bor)| · [3]_q! / q³               (dimensionless Hecke factor)
        → m_p ≈ 938.27 MeV, m_n ≈ 939.56 MeV  (matches CODATA; m_n predicted)

The c_q² (= 1/ℏ_q²) factor is applied ONCE, in the muon anchor m_μ, then
dressed by the *dimensionless* Borromean factor F_Bor.

DO NOT use the Borromean-volume forms for absolute nucleon/atom mass:
    m_e · Vol(𝓑₃) · λ_A / ℏ_q²       (vol_density_borromean)  → 966  (+2.96%, a FIT)
    m_e · Vol(𝓑₃) · tr_M / ℏ_q²      (vol_density_per_block)  → 406  (−57%)
Both apply 1/ℏ_q² to the wrong (Borromean) volume. They are DEPRECATED for
absolute mass (mass_vol_density emits a DeprecationWarning). Route every
absolute-mass consumer through THIS module instead.

Guardrail: docs/canonical-mass-formula-guardrail.md
Resolution: docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

_WITNESS = HERE / "m-p-substrate-identity-50dps.witness.json"


def _from_witness() -> tuple[float, float] | None:
    if not _WITNESS.exists():
        return None
    preds = json.loads(_WITNESS.read_text())["data"]["predictions"]
    return float(preds["m_p_MeV"]), float(preds["m_n_MeV"])


def _from_formula() -> tuple[float, float]:
    """Compute the muon-anchored F_Bor identity directly (fallback)."""
    import mpmath as mp
    from m_p_substrate_identity_50dps import F_Bor
    from q_parameter import Q as q0, vol_4_1_at
    from codata_constants import M_E_MEV
    q = mp.mpf(str(q0))
    m_e = mp.mpf(str(M_E_MEV))
    hbar_q_sq = ((q - 1) / q) ** 2
    m_mu = m_e * vol_4_1_at(50) / hbar_q_sq           # muon anchor (Vol(4₁))
    m_p = 2 * (m_mu * F_Bor(q) - 6 * m_e)             # dim V_(2,1)=2, |S_3|=6
    from derived_masses import q_beta_kashiwara_n2_mev
    m_n = m_p + q_beta_kashiwara_n2_mev() + m_e        # n→p+e+ν̄: Kashiwara b² Q_β (~1 ppb)
    return float(m_p), float(m_n)


def proton_neutron_mass_mev() -> tuple[float, float]:
    """Canonical (m_p, m_n) in MeV via the muon-anchored Hecke energy.

    Prefers the precomputed substrate-identity witness (50 dps); falls back
    to computing the F_Bor identity directly."""
    return _from_witness() or _from_formula()


def proton_mass_mev() -> float:
    """Canonical proton mass (MeV) — muon-anchored Hecke energy ≈ 938.27."""
    return proton_neutron_mass_mev()[0]


def neutron_mass_mev() -> float:
    """Canonical neutron mass (MeV) — muon-anchored Hecke energy ≈ 939.56."""
    return proton_neutron_mass_mev()[1]


#: CAL-point relative 1σ uncertainties.
#  'canonical' = ideal math framework (CAL-2 = m_μ/m_e, 22 ppb);
#  'proton'    = physical-observations layer (CAL-2 = m_p/m_e, 0.06 ppb re-pin).
CAL_SIGMA_REL = {
    "canonical": {"q0": 2.2e-8, "m_e": 3.1e-10},   # muon-anchored CAL-2
    "proton":    {"q0": 6.0e-11, "m_e": 3.1e-10},  # proton-anchored CAL-2
}


def prediction_uncertainty_ppb(Z: int, N: int, layer: str = "canonical") -> float:
    """CAL-propagated reliability of the constituent mass Z·m_p + N·m_n, in ppb.

    Propagates the calibration-point 1σ (q₀ from CAL-2, m_e from CAL-1) through
    the canonical formula m_p(q₀, m_e) = 2(m_e·Vol(4₁)/ℏ_q²·F_Bor − 6·m_e) by
    finite difference, summing the q₀ and m_e contributions in quadrature. q₀
    and m_e enter both nucleons coherently, so we differentiate the constituent
    sum directly. The mass formula AMPLIFIES the CAL-2 error ~21× (ℏ_q=(q−1)/q
    is steep near q₀≈1.11): canonical (muon) → ~462 ppb; proton-layer → ~1.3 ppb.

    This is the theory error bar: a model deviation (err m_sym) far exceeding
    σ_pred is a genuine formula systematic, not calibration noise."""
    import mpmath as mp
    from m_p_substrate_identity_50dps import F_Bor
    from q_parameter import Q as q0, vol_4_1_at
    from codata_constants import M_E_MEV
    from derived_masses import q_beta_kashiwara_n2_mev
    q = mp.mpf(str(q0)); m_e = mp.mpf(str(M_E_MEV))
    vol41 = vol_4_1_at(50)

    def constit(qq, mee):
        m_p = 2 * (mee * vol41 / ((qq - 1) / qq) ** 2 * F_Bor(qq) - 6 * mee)
        m_n = m_p + q_beta_kashiwara_n2_mev() + mee  # Kashiwara b² Q_β (const in FD)
        return Z * m_p + N * m_n

    base = constit(q, m_e)
    sig = CAL_SIGMA_REL.get(layer, CAL_SIGMA_REL["canonical"])
    dq = q * mp.mpf(str(sig["q0"])); dme = m_e * mp.mpf(str(sig["m_e"]))
    d_q0 = (constit(q + dq, m_e) - constit(q - dq, m_e)) / 2
    d_me = (constit(q, m_e + dme) - constit(q, m_e - dme)) / 2
    return float(mp.sqrt(d_q0 ** 2 + d_me ** 2) / abs(base) * mp.mpf(10) ** 9)


def nucleon_mass_mev(species: str) -> float:
    """Canonical nucleon mass (MeV). `species` ∈ {'p','proton','n','neutron'}."""
    s = species.lower()
    if s in ("p", "proton"):
        return proton_mass_mev()
    if s in ("n", "neutron"):
        return neutron_mass_mev()
    raise ValueError(f"unknown nucleon species {species!r} (use 'p' or 'n')")


if __name__ == "__main__":
    mp_, mn_ = proton_neutron_mass_mev()
    print(f"canonical m_p = {mp_:.6f} MeV   m_n = {mn_:.6f} MeV "
          f"(muon-anchored Hecke energy, substrate-identity)")
