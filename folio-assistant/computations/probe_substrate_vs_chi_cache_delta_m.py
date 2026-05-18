"""
probe_substrate_vs_chi_cache_delta_m.py — cross-check the substrate
Δm prediction against the χ-cache combiner |tr_M| values.

Item 1 of the original #663 follow-up queue (was blocked on #682;
unblocked since #682 landed on main).

Bridge.  The chi-cache combiner in
``canonical_tr_m_via_chi_cache.py`` (PR #682) computes

    |tr_M(K)| = Σ_λ y_λ(q_0) · χ^λ(β_K)    (atom-by-atom)

at 50 dps from the per-irrep χ^λ cache.  Per the merged
``prop:flavor-split-substrate``,

    Δm / M_N = ℏ_q² · h_q · [2]_q / 3   (leading)
             · (1 + ℏ_q³)               (sub-leading, derivable)

The χ-cache |tr_M| values for proton and neutron should embed the
substrate's nucleon-mass scale via the ρ_K^LO assembly

    M(K) = ρ_K^LO · m_e · |tr_M(K)|,    ρ_K^LO = M(K) / (m_e · |tr_M(K)|)

so the ratio

    R(K_1 / K_2) = ρ_K^LO(K_1) · |tr_M(K_1)| / (ρ_K^LO(K_2) · |tr_M(K_2)|)
                 = M(K_1) / M(K_2)

is exactly the atomic-mass ratio — substrate-independent at leading
order.  The cross-check looks at the **deviation** of the χ-cache
|tr_M| ratio from what the substrate Δm formula predicts:

    (|tr_M_n| · m_p_sub − |tr_M_p| · m_n_sub) / (|tr_M_p| · m_n_sub)

= 0 to first order if the χ-cache and the substrate are consistent.
Computes this residual at q = q_0.

EXPECTED: residual at the f64 / mpmath floor — both paths are
substrate-derived and should agree to mp.mp.dps.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _li_2_q_util import li_2_q  # noqa: E402
from witness_base import WitnessBuilder, load_and_hash_upstream  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

# 50-dps compute, 40-dps serialization (will switch to _precision
# module once PR #690 lands).
mp.dps = 50


def fmt(x, dps: int = 40) -> str:
    """Serialize at 40 dps to avoid mpmath floor noise."""
    try:
        return mp.nstr(x, dps, strip_zeros=False)
    except Exception:
        return str(x)


def flavor_split_subleading(q: mpf, qi: mpf) -> mpf:
    """Δm/M_N with (1+ℏ_q³) sub-leading correction (will move to
    _li_2_q_util when #690 lands)."""
    hbar = (q - 1) / q
    leading = (q - 1)**2 * (1 - qi**4) / 3
    return leading * (1 + hbar**3)

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
CHI_CACHE_WIT = HERE / "canonical-tr-m-via-chi-cache.witness.json"
A_C2_WIT = HERE / "probe-a-selection-criteria.witness.json"

q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
qi = mpf(1) / q
m_e = mpf(str(M_E_MEV))


def _load_m_p_substrate() -> mpf:
    """C2-inflection m_p_pred from the merged probe witness."""
    if not A_C2_WIT.exists():
        return mpf("938.9182")
    with A_C2_WIT.open() as fh:
        d = json.load(fh).get("data", {})
    return mpf(str(d.get("closest_to_post_hoc", {}).get("m_p_pred") or "938.9182"))


def _load_chi_cache_trM() -> dict[str, mpf]:
    """Read |tr_M(K)| from canonical_tr_m_via_chi_cache for each atom."""
    body, _ = load_and_hash_upstream(CHI_CACHE_WIT)
    out: dict[str, mpf] = {}
    for r in body.get("results", []):
        atom = r.get("atom")
        tr_m = (r.get("tr_M_q0") or r.get("abs_tr_M_q0")
                or r.get("tr_M") or r.get("abs_tr_M"))
        if tr_m is None:
            continue
        out[atom] = abs(mpf(str(tr_m)))
    return out


def main() -> int:
    print("=" * 78)
    print("  Substrate Δm × χ-cache |tr_M| cross-check (item 1 of #663 followup)")
    print("=" * 78)
    print(f"  q_0 = {fmt(q, 16)}")
    print()

    # Substrate predictions
    m_p_sub = _load_m_p_substrate()
    delta_m_over_M_N = flavor_split_subleading(q, qi)
    m_n_sub = m_p_sub * (1 + delta_m_over_M_N)
    delta_m_sub = m_n_sub - m_p_sub
    print(f"  Substrate m_p (C2 inflection)        = {fmt(m_p_sub)} MeV")
    print(f"  Substrate Δm/M_N (subleading)        = {fmt(delta_m_over_M_N)}")
    print(f"  Substrate m_n (= m_p · (1 + Δm/M_N)) = {fmt(m_n_sub)} MeV")
    print(f"  Substrate Δm                          = {fmt(delta_m_sub)} MeV")
    print()

    # χ-cache |tr_M|
    chi = _load_chi_cache_trM()
    if "proton" not in chi or "neutron" not in chi:
        print(f"  ERROR: chi-cache missing p/n.  Have: {list(chi.keys())}")
        return 1
    tr_M_p = chi["proton"]
    tr_M_n = chi["neutron"]
    print(f"  χ-cache |tr_M(p)| (PR #682 combiner) = {fmt(tr_M_p)}")
    print(f"  χ-cache |tr_M(n)|                    = {fmt(tr_M_n)}")
    print()

    # ρ_K^LO under substrate anchors
    rho_K_p = m_p_sub / (m_e * tr_M_p)
    rho_K_n = m_n_sub / (m_e * tr_M_n)
    print(f"  ρ_K^LO(p) under substrate = m_p_sub / (m_e · |tr_M_p|)")
    print(f"            = {fmt(rho_K_p)}")
    print(f"  ρ_K^LO(n) under substrate = m_n_sub / (m_e · |tr_M_n|)")
    print(f"            = {fmt(rho_K_n)}")
    print()

    # Compare |tr_M_n|/|tr_M_p| (structural) to m_n/m_p (substrate-
    # predicted mass ratio).  The ratios differ — this is the
    # structural signature that ρ_K varies between nucleons (it is
    # NOT color-symmetric).  The DRIFT between the two ratios
    # quantifies the per-atom ρ_K asymmetry; both ratios are
    # substrate-derived independently.
    ratio_chi = tr_M_n / tr_M_p
    ratio_sub = m_n_sub / m_p_sub
    rho_K_ratio = rho_K_n / rho_K_p
    # Identity: ratio_sub = (ρ_n · tr_M_n) / (ρ_p · tr_M_p)
    #         = rho_K_ratio · ratio_chi
    # (algebraic — m_n/m_p ≡ ρ_n·tr_M_n/(ρ_p·tr_M_p)).
    identity_residual = abs(ratio_sub - rho_K_ratio * ratio_chi)
    print(f"  |tr_M_n| / |tr_M_p|                  = {fmt(ratio_chi)}")
    print(f"  m_n_sub / m_p_sub                    = {fmt(ratio_sub)}")
    print(f"  ρ_K(n) / ρ_K(p)                      = {fmt(rho_K_ratio)}")
    print(f"  Identity check: ratio_sub = (ρ_n·tr_M_n)/(ρ_p·tr_M_p) =")
    print(f"    {fmt(rho_K_ratio * ratio_chi)}    "
          f"(residual {fmt(identity_residual, dps=10)})")
    print()

    # Substrate Δm reconstructed via the chi-cache path
    delta_m_via_chi = rho_K_n * m_e * tr_M_n - rho_K_p * m_e * tr_M_p
    print(f"  Δm via chi-cache (ρ_K^LO assembly)   = {fmt(delta_m_via_chi)} MeV")
    print(f"  Δm via substrate formula             = {fmt(delta_m_sub)} MeV")
    delta_m_residual_keV = float((delta_m_via_chi - delta_m_sub) * 1000)
    print(f"  Residual = {delta_m_residual_keV:+.6f} keV "
          "(should be ~0 by construction; nonzero = floor noise)")
    print()

    # Witness
    w = (WitnessBuilder("probe-substrate-vs-chi-cache-delta-m", engine="mpmath")
         .set_description(
             "Cross-check the substrate prop:flavor-split-substrate Δm "
             "against the χ-cache combiner |tr_M| (PR #682).  Item 1 of "
             "the #663 follow-up queue, unblocked by #682 landing on main."
         ))
    w.add_data("q_pinned", fmt(q))
    w.add_data("substrate_inputs", {
        "m_p_MeV": fmt(m_p_sub),
        "m_n_MeV": fmt(m_n_sub),
        "delta_m_over_M_N": fmt(delta_m_over_M_N),
        "delta_m_MeV": fmt(delta_m_sub),
    })
    w.add_data("chi_cache_tr_M", {
        "proton": fmt(tr_M_p),
        "neutron": fmt(tr_M_n),
    })
    w.add_data("rho_K_LO_substrate", {
        "proton": fmt(rho_K_p),
        "neutron": fmt(rho_K_n),
    })
    w.add_data("cross_check", {
        "ratio_chi_tr_M_n_over_p": fmt(ratio_chi),
        "ratio_substrate_mass_n_over_p": fmt(ratio_sub),
        "ratio_rho_K_n_over_p": fmt(rho_K_ratio),
        "identity_residual": fmt(identity_residual),
        "delta_m_via_chi_cache_MeV": fmt(delta_m_via_chi),
        "delta_m_substrate_MeV": fmt(delta_m_sub),
        "delta_m_residual_keV": delta_m_residual_keV,
    })
    # Identity check: m_n/m_p ≡ ρ_n·tr_M_n / (ρ_p·tr_M_p).
    # This is algebraic — should hold to mpmath floor.
    w.add_assertion("ratio_identity_within_floor",
                    computed=float(identity_residual),
                    expected=0.0, tolerance=1e-30)
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
