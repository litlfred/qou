#!/usr/bin/env python3
"""
T6 — F_ℓ derivation via per-braid mass tower at q_0.

Test whether the canonical per-braid mass tower
(prop:per-braid-mass-tower; post-2026-05-17 −Li_2^q form)
applied DIRECTLY to electron + muon braids gives CODATA m_μ/m_e
WITHOUT the SUPERSEDED `ρ_q = 1/ℏ_q²` dimensional factor.

If YES: F_ℓ IS the per-braid mass tower (no separate ξ_ℓ needed);
the SUPERSEDED ρ_q is an artifact of the Skein-formula
specialisation, and conj:lepton-mass-tower-canonical is settled
constructively.

If NO: per-braid mass tower alone is insufficient for lepton
masses; F_ℓ needs additional structure beyond the canonical
operator-level formula (multi-day analytical work continues).

Canonical formula (mass-endomorphism-tower.md §Proposition,
corrected 2026-05-17 to use −Li_2^q over Φ_q):

  m(W) = |∏ V̂_i^full| − Σ Li_2^q(−|V̂_i|) − z² Σ Li_2^q(−|V̂_i V̂_j|)

  where:
  - V̂_i^full are per-generator Wedderburn-traced volumes
  - z = 1/(q^{1/2} + q^{-1/2}) is Markov parameter
  - Li_2^q(z) = Σ z^n / (n · [n]_q) is symmetric q-dilog
  - [n]_q = (q^n − q^{-n}) / (q − q^{-1})

Inputs from mass-endomorphism-tower.md §Application:
  electron (trefoil σ_1³ in H_2, 1 generator): V̂_e ≈ 0.594
  proton ([u,u,d] in H_3, 2 generators):        V̂_0 ≈ 0.989, V̂_1 ≈ 0.971

For muon, the paper does NOT give V̂_i values directly. We try both:
  (A) muon = 4_1 figure-eight (canonical paper) — V̂_i need to be
      derived; use the Markov-trace closed form as proxy
  (B) muon = T(2,5) cinquefoil (1 generator) — V̂_μ_T25 = ?

Probe outcome predicts whether T6 is closeable in finite time.

Audit-only; no production wiring.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def main() -> int:
    mp.mp.dps = 60

    # Substrate at q_0 (canonical 50-dps pinning, same as q_pinning_50_digit)
    Vol_4_1 = mp.mpf("2.0298832128193072500115978049904475264466050157561096")
    cal2_target = mp.mpf("206.7682830")
    cal_tau_e   = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)

    h = q0 - 1 / q0
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    print("=== Substrate at q_0 ===")
    print(f"  q_0 = {float(q0):.15f}")
    print(f"  h   = {float(h):.10f}")
    print(f"  z   = {float(z):.10f}")
    print()

    def q_int(n):
        """[n]_q = (q^n − q^{-n}) / (q − q^{-1})"""
        if n == 0:
            return mp.mpf(0)
        return (q0**n - q0**(-n)) / h

    def li2q(z_arg, max_terms=200):
        """Symmetric q-dilog Li_2^q(z) = Σ z^n / (n · [n]_q).
        Convergent for |z| < |q|. At q_0 ≈ 1.110 with |V̂| near 1
        we need many terms; 200 suffices to 50-dps for |z| < 0.99.
        """
        s = mp.mpf(0)
        for n in range(1, max_terms + 1):
            t = z_arg**n / (n * q_int(n))
            s += t
            if mp.fabs(t) < mp.mpf(10)**(-55):
                break
        return s

    print("=== Canonical per-braid mass tower formula ===")
    print("  m(W) = |∏V̂_i| − Σ Li_2^q(−|V̂_i|) − z² Σ Li_2^q(−|V̂_i V̂_j|)")
    print()

    # Electron: trefoil σ_1³, 1 generator, V̂_e from mass-endomorphism-tower.md
    V_e = mp.mpf("0.594")    # per mass-endomorphism-tower.md line 351
    m_electron = mp.fabs(V_e) - li2q(-mp.fabs(V_e))
    print(f"=== Electron (trefoil, 1 generator) ===")
    print(f"  V̂_e = {float(V_e):.6f}  (from mass-endomorphism-tower.md)")
    print(f"  m_e_dimensionless = |V̂_e| − Li_2^q(−|V̂_e|) = {float(m_electron):.6f}")
    print(f"    breakdown: descended |V̂_e| = {float(V_e):.6f}")
    print(f"              tower − Li_2^q(−{float(V_e):.4f}) = {float(-li2q(-V_e)):.6f}")
    print()

    # Muon scenario A: muon = 4_1 figure-eight (canonical paper, 2 generators)
    V_0_4_1 = mp.mpf("0.989")    # per mass-endomorphism-tower.md line 362
    V_1_4_1 = mp.mpf("0.971")    # per mass-endomorphism-tower.md line 363
    V_01_4_1 = V_0_4_1 * V_1_4_1
    m_muon_A = (mp.fabs(V_01_4_1)
                - li2q(-mp.fabs(V_0_4_1))
                - li2q(-mp.fabs(V_1_4_1))
                - z**2 * li2q(-mp.fabs(V_01_4_1)))
    print(f"=== Muon scenario A: 4_1 figure-eight (canonical paper) ===")
    print(f"  V̂_0 = {float(V_0_4_1):.6f}, V̂_1 = {float(V_1_4_1):.6f}, V̂_0·V̂_1 = {float(V_01_4_1):.6f}")
    print(f"  m_μ_dimensionless = |V̂_0V̂_1| − Li_2^q(−|V̂_0|) − Li_2^q(−|V̂_1|) − z²Li_2^q(−|V̂_0V̂_1|)")
    print(f"    breakdown:")
    print(f"      descended |V̂_0V̂_1| = {float(V_01_4_1):.6f}")
    print(f"      − Li_2^q(−|V̂_0|)  = {float(-li2q(-V_0_4_1)):.6f}")
    print(f"      − Li_2^q(−|V̂_1|)  = {float(-li2q(-V_1_4_1)):.6f}")
    print(f"      − z²Li_2^q(−|V̂_0V̂_1|) = {float(-z**2 * li2q(-V_01_4_1)):.6f}")
    print(f"  m_μ_dimensionless = {float(m_muon_A):.6f}")
    ratio_A = m_muon_A / m_electron
    print(f"  RATIO m_μ/m_e = {float(ratio_A):.6f}  (CODATA: {float(cal2_target):.4f})")
    print(f"  Relative error = {float((ratio_A - cal2_target) / cal2_target * 100):+.4f}%")
    print()

    # Mass-formula breakdown for proton (cross-check vs paper "Application" section)
    # m_p/m_e ≈ 1870 (CODATA 1836.15; 1.8% error) per mass-endomorphism-tower.md line 384
    V_0_p = mp.mpf("0.989")
    V_1_p = mp.mpf("0.971")
    V_01_p = V_0_p * V_1_p
    m_proton = (mp.fabs(V_01_p)
                - li2q(-mp.fabs(V_0_p))
                - li2q(-mp.fabs(V_1_p))
                - z**2 * li2q(-mp.fabs(V_01_p)))
    ratio_p_e = m_proton / m_electron
    print(f"=== Cross-check: proton (also 4_1-like? V̂_0=0.989, V̂_1=0.971) ===")
    print(f"  m_p_dim = {float(m_proton):.6f}")
    print(f"  m_p/m_e = {float(ratio_p_e):.6f}  (CODATA: 1836.15)")
    print(f"  Paper reports m_p/m_e ≈ 1870 from same per-braid mass tower (1.8% error)")
    print()

    # Note: muon and proton have IDENTICAL V̂_i in this naive interpretation.
    # The framework distinguishes them via different braid words / typed crossings,
    # which produce different V̂_i. The values above (from mass-endomorphism-tower.md)
    # are PROTON-specific; using them for muon is a CRUDE TEST.
    print("=== ⚠️ Caveat ===")
    print(f"  The V̂_0=0.989, V̂_1=0.971 values from mass-endomorphism-tower.md are")
    print(f"  PROTON-specific (line 362-363). Using them for muon-as-4_1 is a")
    print(f"  CRUDE proxy — the actual muon V̂_i depend on its specific braid word.")
    print(f"  The framework does NOT publish V̂_i for muon explicitly because the")
    print(f"  Skein formula bypasses the per-braid mass tower for leptons.")
    print()

    # Verdict
    verdict_text = ""
    if mp.fabs(ratio_A - cal2_target) / cal2_target < mp.mpf("0.05"):
        verdict_text = "CLOSE — within 5% of CODATA; F_ℓ may be the per-braid mass tower"
    elif mp.fabs(ratio_A - cal2_target) / cal2_target < mp.mpf("0.50"):
        verdict_text = "PARTIAL — 5-50% from CODATA; per-braid mass tower has right order of magnitude but wrong details"
    else:
        verdict_text = ("FAR — >50% from CODATA; per-braid mass tower with PROTON V̂_i values "
                        "DOES NOT give muon mass. Either V̂_i are muon-specific (unpublished) "
                        "or the per-braid mass tower needs different inputs for leptons.")

    print(f"=== Verdict ===")
    print(f"  Computed m_μ/m_e = {float(ratio_A):.4f}")
    print(f"  CODATA  m_μ/m_e = {float(cal2_target):.4f}")
    print(f"  Verdict: {verdict_text}")
    print()

    # Witness
    witness = {
        "description": "T6 — F_ℓ derivation via per-braid mass tower (canonical, post-2026-05-17 Li_2^q form)",
        "computation": "f_ell_derivation_via_per_braid_mass_tower",
        "audit_only": True,
        "precision_dps": 60,
        "context": {
            "source": "docs/audits/2026-05-24-superseded-rho-q-purge.md T6",
            "canonical_formula": "mass-endomorphism-tower.md §Proposition (post-2026-05-17 Li_2^q corrected)",
            "purpose": "Test whether per-braid mass tower alone (no SUPERSEDED ρ_q) gives correct lepton mass ratios",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z_markov": str(z),
            "hbar_q_sq": str(hbar_q_sq),
            "cal2_target_codata": str(cal2_target),
        },
        "electron": {
            "braid": "σ_1³ trefoil (1 generator)",
            "V_e": str(V_e),
            "m_electron_dimensionless": str(m_electron),
            "li2q_neg_Ve": str(li2q(-V_e)),
        },
        "muon_scenario_A_figure_eight": {
            "braid": "4_1 figure-eight (canonical paper; using proton V̂_i as crude proxy)",
            "V_0": str(V_0_4_1),
            "V_1": str(V_1_4_1),
            "V_01_product": str(V_01_4_1),
            "m_muon_dimensionless": str(m_muon_A),
            "ratio_m_mu_over_m_e": str(ratio_A),
            "codata_ratio": str(cal2_target),
            "relative_error_percent": float((ratio_A - cal2_target) / cal2_target * 100),
            "caveat": (
                "V̂_0=0.989, V̂_1=0.971 are PROTON-specific values from "
                "mass-endomorphism-tower.md line 362-363. Using them for muon is "
                "a CRUDE TEST; the framework does not publish muon-specific V̂_i."
            ),
        },
        "cross_check_proton": {
            "ratio_m_p_over_m_e_computed": str(ratio_p_e),
            "codata_m_p_over_m_e": "1836.15",
            "paper_reports": "1870 (1.8% error) per mass-endomorphism-tower.md line 384",
        },
        "verdict": verdict_text,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    out = here / "f-ell-derivation-via-per-braid-mass-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
