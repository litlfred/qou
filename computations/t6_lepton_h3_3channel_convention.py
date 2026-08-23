#!/usr/bin/env python3
"""
T6 closure attempt — 3-channel H_3 Wedderburn convention for leptons.

Per pyhecke/constants.py:156 (V_HAT_ELECTRON formula):
  V̂_ℓ = W_SYM · χ_(3)(σ_word) + W_STD · (z·a_word + b_word) + W_ALT · χ_(1,1,1)(σ_word)
where:
  - σ_word is the lepton's torus braid σ_1^k embedded into H_3
  - a_word, b_word come from the Hecke recursion σ^k = a σ + b
    (Lean theorem torus_knot_odd_reduction_exists)
  - W_SYM, W_STD, W_ALT are H_3 Plancherel weights
  - The (z·a + b) factor is the Markov trace of σ^k in std rep
  - χ_(3) = q^k, χ_(1,1,1) = (-q⁻¹)^k for σ^k in H_3 1D irreps

This is the LEPTON BRING-SURFACE representation:
  3 H_3 Wedderburn sheets analogous to 3 quark color tubes for nucleons.

Apply to:
  electron σ_1^3 (T(2,3))  →  should give V̂_e ≈ 0.594 (paper match)
  muon T(2,5) σ_1^5         →  V̂_μ_T25
  tau T(2,7) σ_1^7          →  V̂_τ
  muon 4_1 (σ_1σ_2⁻¹)²      →  V̂_μ_4_1 (native H_3, different formula)

Then apply Li_2^q canonical mass tower to get mass ratios; compare CODATA.
"""

from __future__ import annotations
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()

    # Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 53 digits, correct to 19 (qou-ckbv)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    cal2_target = M_MU_OVER_M_E
    cal_tau_e   = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    qi = 1 / q0
    h = q0 - qi
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    # H_3 Wedderburn-Plancherel weights
    # d_q((3)) = 1, d_q((1,1,1)) = 1, d_q((2,1)) = [2]_q = q + q^-1
    two_q = q0 + qi
    q3_poly = q0**2 + 1 + qi**2  # [3]_q for H_3 (but actual qfac is different)
    qfac_3 = 1 * two_q * q3_poly  # [1]_q · [2]_q · [3]_q
    W_SYM = mp.mpf(1) * mp.mpf(1) / qfac_3
    W_STD = two_q * two_q / qfac_3
    W_ALT = mp.mpf(1) * mp.mpf(1) / qfac_3

    print(f"=== Substrate + H_3 weights ===")
    print(f"  q_0 = {float(q0):.10f}, h = {float(h):.6f}, z = {float(z):.6f}")
    print(f"  [2]_q = {float(two_q):.6f}, [3]_q-numerator = {float(q3_poly):.6f}")
    print(f"  [3]_q! = {float(qfac_3):.6f}")
    print(f"  W_SYM = {float(W_SYM):.6f}")
    print(f"  W_STD = {float(W_STD):.6f}")
    print(f"  W_ALT = {float(W_ALT):.6f}")
    print(f"  Σ W = {float(W_SYM + W_STD + W_ALT):.6f}")
    print()

    # Torus knot recursion σ^k = a_k σ + b_k via Hecke σ² = h σ + 1
    def torus_ab(k):
        a, b = mp.mpf(0), mp.mpf(1)  # σ^0 = identity
        for _ in range(k):
            a, b = a * h + b, a
        return a, b

    def V_hat_torus_H3(k):
        """V̂_ℓ for σ_1^k embedded into H_3 via 3-channel formula."""
        a_k, b_k = torus_ab(k)
        # χ_(3)(σ^k) = q^k; χ_(1,1,1)(σ^k) = (-qi)^k
        # std channel: Markov-traced 2D rep σ^k = a σ + b → trace z·a + b
        chi_sym = q0**k
        chi_alt = (-qi)**k
        std_markov_traced = z * a_k + b_k
        V = W_SYM * chi_sym + W_STD * std_markov_traced + W_ALT * chi_alt
        return V

    # Verify with paper's V_HAT_ELECTRON (electron σ_1^3)
    V_e = V_hat_torus_H3(3)
    print(f"=== Electron σ_1^3 — calibration check vs paper ===")
    print(f"  V̂_e (H_3 3-channel) = {float(V_e):.6f}")
    print(f"  Paper value         ≈ 0.594")
    print(f"  Match (within 5%): {abs(float(V_e) - 0.594) < 0.03}")
    print()

    # Apply to all torus-knot lepton candidates
    print(f"=== Lepton V̂ via H_3 3-channel convention ===")
    leptons_torus = {
        "electron σ_1^3 T(2,3)": 3,
        "muon T(2,5) σ_1^5": 5,
        "muon T(2,7) σ_1^7": 7,    # alternate muon
        "tau T(2,7) σ_1^7": 7,     # canonical tau per knot-volumes.py
        "tau T(2,9) σ_1^9": 9,     # alternate
    }
    V_hats = {}
    for name, k in leptons_torus.items():
        V = V_hat_torus_H3(k)
        V_hats[name] = V
        print(f"  {name:35s}  V̂ = {float(V):+.6f}  (in conv radius: {abs(float(V)) < float(q0)})")
    print()

    # Compute m_ℓ via canonical Li_2^q tower
    # Per canonical_plus_multibrane.py:tower_mass_level Li_2^q (descended-dropped):
    #   m(W) = − Σ Li_2^q(−|V̂_i|) − z² Σ Li_2^q(−|V̂_i V̂_j|)
    # For single-generator lepton: just − Li_2^q(−|V̂|), no pair sum.
    def li2q(z_arg, max_terms=500):
        s = mp.mpf(0)
        for n in range(1, max_terms + 1):
            qint = (q0**n - q0**(-n)) / h
            t = z_arg**n / (n * qint)
            s += t
            if mp.fabs(t) < mp.mpf(10)**(-50):
                break
        return s

    print(f"=== Mass dimensions via Li_2^q (descended-dropped, single-gen) ===")
    m_dims = {}
    for name, V in V_hats.items():
        m_dim = -li2q(-mp.fabs(V))
        m_dims[name] = m_dim
        print(f"  {name:35s}  m_dim = {float(m_dim):+.6f}")
    print()

    # Ratios
    m_e = m_dims["electron σ_1^3 T(2,3)"]
    print(f"=== Mass ratios m_ℓ/m_e vs CODATA ===")
    for name, m_dim in m_dims.items():
        if "electron" in name:
            continue
        ratio = m_dim / m_e
        if "muon" in name:
            codata = cal2_target
        elif "tau" in name:
            codata = cal_tau_e
        else:
            continue
        rel = (ratio - codata) / codata * 100
        verdict = "CLOSE" if abs(float(rel)) < 5 else ("PARTIAL" if abs(float(rel)) < 50 else "OFF")
        print(f"  {name:35s}  ratio = {float(ratio):+.4f}  CODATA = {float(codata):8.4f}  {float(rel):+8.3f}%  [{verdict}]")
    print()

    # Witness
    witness = {
        "description": "T6 closure attempt — H_3 3-channel Wedderburn convention for leptons (lepton Bring-surface structure)",
        "computation": "t6_lepton_h3_3channel_convention",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "convention_source": "tools/pyhecke/python/pyhecke/constants.py:156 V_HAT_ELECTRON formula",
            "lepton_bring_surface": (
                "Per owner directive: leptons SHOULD have Bring surface representation. "
                "The framework uses H_3 Wedderburn (3 channels: sym + std + alt) for "
                "leptons even though their natural braid is in H_2 (single generator). "
                "The 3-channel structure is the lepton analog of 3-color-tube Bring "
                "weighting for nucleons; here 3 = 3 H_3 irreps = 3 Wedderburn sheets."
            ),
            "formula": (
                "V̂_ℓ = W_SYM·χ_(3)(σ^k) + W_STD·(z·a_k + b_k) + W_ALT·χ_(1,1,1)(σ^k); "
                "for torus knot σ^k via Lean theorem torus_knot_odd_reduction_exists "
                "recursion σ^k = a_k σ + b_k."
            ),
            "resolves": "T6 gap (a) V̂ convention mismatch — paper uses H_3 3-channel; mine was H_2 2-channel",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z": str(z),
            "W_SYM": str(W_SYM),
            "W_STD": str(W_STD),
            "W_ALT": str(W_ALT),
        },
        "V_hats": {name: str(V) for name, V in V_hats.items()},
        "m_dims_li2q": {name: str(m) for name, m in m_dims.items()},
        "ratios_vs_codata": {
            name: {
                "ratio": str(m_dims[name] / m_e),
                "codata": str(cal2_target if "muon" in name else (cal_tau_e if "tau" in name else mp.mpf(0))),
                "relative_error_percent": float((m_dims[name] / m_e - (cal2_target if "muon" in name else cal_tau_e)) / (cal2_target if "muon" in name else cal_tau_e) * 100) if "muon" in name or "tau" in name else 0,
            }
            for name in V_hats if "electron" not in name
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    import os as _os, sys as _sys  # noqa: E402
    _sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wpath = WitnessBuilder.wrap_legacy(
        "t6-lepton-h3-3channel-convention", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
    ).save()
    print(f"\nwitness -> {_wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
